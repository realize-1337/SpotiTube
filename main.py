import typing
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal, QObject, QThread
import subprocess
from functools import partial
import packages.Spotify as sp
import packages.YTMusic as yt
from difflib import SequenceMatcher
import re
from time import sleep
import logging
UI_FILE = './GUI/GUI.ui'
PY_FILE = './GUI/gui.py'
subprocess.run(['pyuic6', '-x', UI_FILE, '-o', PY_FILE])
from GUI.gui import Ui_MainWindow

options = {
    'song_1':{
        'target': {
            'title': 'Last Resort',
            'artist': 'Papa Roach'
        },
        'id_0': {
            'title': 'Last Resort Remix',
            'artist': 'Papa Roach',
            'matchRatio': '0.85'
            }, 
        'id_1': {
            'title': 'Last Resort (Karaoke)',
            'artist': 'Papa Roach',
            'matchRatio': '0.75'
            },
        'id_2': {
            'title': 'Last Resort',
            'artist': 'Papa Roach',
            'matchRatio': '1.0'
        }
    },
    'song_2':{
        'target': {
            'title': 'Last Resort 2',
            'artist': 'Papa Roach'
        },
        'id_0': {
            'title': 'Last Resort Remix 2',
            'artist': 'Papa Roach',
            'matchRatio': '0.88'
            }, 
        'id_1': {
            'title': 'Last Resort (Karaoke) 2',
            'artist': 'Papa Roach',
            'matchRatio': '0.99'
            },
        'id_2': {
            'title': 'Last Resort 2',
            'artist': 'Papa Roach',
            'matchRatio': '1.1'
        }
    }  
}

class WorkerSignals(QObject):
    push = pyqtSignal(dict)
    finished = pyqtSignal() 

class Worker(QRunnable):

    def __init__(self, list):
        super().__init__()
        self.list = list
        self.signals = WorkerSignals()

    def run(self):
        try:
            ytm = yt.yt()
            result = ytm.findTables(self.list[0], self.list[1], duration=int(self.list[2]), count=int(self.list[3]), filter=self.list[4])
            self.signals.push.emit(result)
        finally:
            self.signals.finished.emit()

class UI(QMainWindow):
    global ytDict
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.sp = sp.sp()
        self.ui.setupUi(self)
        #self.tableYT(options)
        self.ui.spFound.setText('Enter Playlist ID or link')
        self.ui.spSearch.clicked.connect(self.getSpotifyPlaylist)
        self.spDict = {}
        self.spChange = False
        self.ui.ytProgress.setValue(0)
        self.ui.tabWidget.currentChanged.connect(self.tabChange)
        self.ui.reloadYT.clicked.connect(self.createYTdict)
        self.ui.commitYT.clicked.connect(self.createPlaylist)
        self.ytDict = {}
        self.currentId = 0
        self.finished = 0
        self.items=[]
        self.progressActual = 0.0

    def getSpotifyPlaylist(self):
        # Set Zero State
        self.ytDict = {}
        self.currentId = 0
        self.finished = 0
        self.items=[]
        self.progressActual = 0.0
        self.spDict = {}

        # Missing: Regex

        regex_pattern = r'https://open.spotify.com/playlist/(\w+)(?:\?si=\w+)?|(\w+)'
        

        self.ui.spFound.setText('Loading Playlist Items ...')
        try:
            id = self.ui.spId.text()
            match = re.search(regex_pattern, id)
            id = match.group(1) or match.group(2)
        except:
            self.ui.spFound.setText('Please enter valid id or link')
            return
        print(id)
        try: 
            name = self.sp.getPlaylist(id)
        except: 
            self.ui.spFound.setText('Playlist not found. Is it set to public?')
            return
        print(name)
        self.ui.spFound.setText(rf'Loaded Playlist: {name}')
        self.ui.playlistNameYT.setText(rf'{name}')
        self.spDict = {}
        self.spDict = self.sp.songDict()
        for k, v in self.spDict.items():
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            item = QTableWidgetItem(rf"{v['title']}")
            self.ui.tableWidget.setItem(row_count, 0, item)
            
            item = QTableWidgetItem(rf"{v['artist']}")
            self.ui.tableWidget.setItem(row_count, 1, item)
            
            item = QTableWidgetItem(rf"{v['album']}")
            self.ui.tableWidget.setItem(row_count, 2, item)
            
            sec = int(v['duration'])
            m = int(sec/60)
            s = int(sec % 60)
            item = QTableWidgetItem(f'{m:02d}:{s:02d}')
            self.ui.tableWidget.setItem(row_count, 3, item)
            
        self.ui.tableWidget.resizeColumnToContents(0)
        self.ui.tableWidget.resizeColumnToContents(1)
        self.ui.tableWidget.resizeColumnToContents(2)
        self.ui.tableWidget.resizeColumnToContents(3)
        self.spChange = True
        self.createYTdict()
    
    def tableYT(self, options:dict):
        for k, v in options.items():
            row_count = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(row_count)
            combo_box = QComboBox()
            maxRatio = 0
            run = 0
            targetArtist = ''
            for key, value in v.items():
                if key == 'target':
                    item = QTableWidgetItem(value['title'])
                    self.ui.tableWidget_2.setItem(row_count, 0, item)
                    item = QTableWidgetItem(value['artist'])
                    targetArtist = value['artist']
                    self.ui.tableWidget_2.setItem(row_count, 1, item)
                    continue
                text = f"{value['title']} - {value['artist']} // (R: {'%.2f' % float(value['matchRatio'])})"
                combo_box.addItem(text)
                combo_box.setItemData(run, [key, float(value['matchRatio'])])
                if float(value['matchRatio']) > maxRatio: 
                    maxRatio = float(value['matchRatio'])
                    if SequenceMatcher(None, targetArtist.lower(), value['artist'].lower()).ratio() < 0.25:
                        item = QTableWidgetItem(f'! {"%.2f" % maxRatio}')
                    else: item = QTableWidgetItem(f'{"%.2f" % maxRatio}')
                    combo_box.setCurrentIndex(run)
                    
                    self.ui.tableWidget_2.setItem(row_count, 2, item)
                run += 1
            self.ui.tableWidget_2.setCellWidget(row_count, 3, combo_box)

            matchRatioCell = self.ui.tableWidget_2.item(row_count, 2)
            c_box = self.ui.tableWidget_2.cellWidget(row_count, 3)
            combo_box.currentTextChanged.connect(partial(self.update_YT_table, matchRatioCell, c_box))

    def update_YT_table(self, matchCell, combo_box):
        selected_key = combo_box.currentIndex()
        selected_value = combo_box.itemData(selected_key)
        matchCell.setText(f'{"%.2f" % selected_value[1]}')

    def createYTdict(self, count=10, filter='songs'):
        if self.ui.tabWidget.currentIndex() == 1 and self.spDict and self.spChange:
            self.spChange = False
            items = []
            results = {}
            song = 0
            for k, v in self.spDict.items():
                items.append([v['title'], v['artist'], int(v['duration']), int(count), rf"{filter}"])
            self.items = items
            self.run_threads(items)

    def tabChange(self):
        sleep(1)
        self.createYTdict()

    def threadComplete(self):
        logging.info('Thread finished')

    def run_threads(self, items):
        threads = []
        threadpool = QThreadPool.globalInstance()
        self.currentId = 0
        self.finished = len(items)
        self.ui.ytProgress.setValue(0)
        for item in items:
            print(item)
            worker = Worker(item)
            worker.signals.push.connect(self.merger)
            worker.signals.finished.connect(self.threadComplete)
            threadpool.start(worker)

    def merger(self, dict):
        self.ytDict[f'{self.currentId}'] = dict
        self.currentId += 1
        self.progressActual += 100/len(self.items)
        self.ui.ytProgress.setValue(int(self.progressActual))

        if self.currentId == len(self.items):
            self.tableYT(self.ytDict)

    def createPlaylist(self):
        ids = []
        for row in range(self.ui.tableWidget_2.rowCount()):
            combo_box = self.ui.tableWidget_2.cellWidget(row, 3)
            index = combo_box.currentIndex()
            id = combo_box.itemData(index)[0]
            if id == 'NULL': continue
            else: ids.append(id)

        ytm = yt.yt()
        playlistId = ytm.createPlaylist(self.ui.playlistNameYT.text())
        ytm.ids = ids
        try: 
            ytm.addSongs()
            self.infobox(True)
        except: self.infobox(False)

    def infobox(self, success):
        newbox = QMessageBox()
        if success:
            newbox.setText('<b>Successfully created Playlist</b>')
            newbox.setWindowTitle('Success')
        else:
            newbox.setText('<b>Something went wrong</b>')
            newbox.setWindowTitle('Error')

        newbox.setTextFormat(QtCore.Qt.TextFormat.RichText)
        # newbox.setWindowIcon(QtGui.QIcon('assets/VC_Logo.ico'))
        newbox.exec()


if __name__ == '__main__':
    app = QApplication([])
    window = UI()
    window.show()
    app.exec()