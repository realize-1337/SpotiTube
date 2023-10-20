import os
import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject
import subprocess
from functools import partial
import packages.Spotify as sp
import packages.YTMusic as yt
import ytmusicapi.auth.oauth as ytmoauth
from difflib import SequenceMatcher
import re
import requests
import webbrowser
import json
import logging
# UI_FILE = './GUI/GUI.ui'
# PY_FILE = './GUI/gui.py'
# subprocess.run(['pyuic6', '-x', UI_FILE, '-o', PY_FILE])
# UI_FILE_settings = './GUI/settings.ui'
# PY_FILE_settings = './GUI/settings.py'
# subprocess.run(['pyuic6', '-x', UI_FILE_settings, '-o', PY_FILE_settings])
from GUI.gui import Ui_SpotiTube as mainSpotiTube
from GUI.settings import Ui_SpotiTube as settingSpotiTube

class WorkerSignals(QObject):
    push = pyqtSignal(dict)
    finished = pyqtSignal() 

class Worker(QRunnable):

    def __init__(self, list, path):
        super().__init__()
        self.list = list
        self.path = os.path.join(path, 'oauth.json')
        self.signals = WorkerSignals()

    def run(self):
        try:
            ytm = yt.yt(self.path)
            result = ytm.findTables(self.list[0], self.list[1], duration=int(self.list[2]), count=int(self.list[3]), filter=self.list[4])
            self.signals.push.emit(result)
        finally:
            self.signals.finished.emit()

class UI(QMainWindow):
    def __init__(self, alternativePath:str=None):
        super().__init__()
        self.ui = mainSpotiTube()
        self.ui.setupUi(self)
        if alternativePath: self.path = alternativePath
        else: self.path = str(os.path.expanduser('~\\Documents\\SpotiTube'))
        self.code:dict
        self.oauth = ytmoauth.YTMusicOAuth(requests.Session())
        
        if not os.path.isdir(self.path) or not os.path.exists(os.path.join(self.path, 'keys.json')) or not os.path.exists(os.path.join(self.path, 'oauth.json')): 
            if not os.path.isdir(self.path): os.mkdir(self.path, mode=777)
            self.ytLoginState = False
            self.spKeyState = False
            self.settings()
        else:
            self.ytLoginState = True
            self.spKeyState = True
            self.loadSetting()
        self.spPath = os.path.join(self.path, 'keys.json')
        self.sp = sp.sp(self.spPath)
        self.ui.spFound.setText('Enter Playlist ID or link')
        self.ui.spSearch.clicked.connect(self.getSpotifyPlaylist)
        self.ui.spId.returnPressed.connect(self.getSpotifyPlaylist)
        self.ui.playlistNameYT.returnPressed.connect(self.createPlaylist)
        self.spDict = {}
        self.spChange = False
        self.ui.ytProgress.setValue(0)
        self.ui.tabWidget.currentChanged.connect(self.createYTdict)
        self.ui.menuWindow_2.aboutToShow.connect(self.softwareInfo)
        self.ui.action_Settings.triggered.connect(self.settings)
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
        header = []
        self.ui.tableWidget.setRowCount(0)
        for item in range(self.ui.tableWidget.columnCount()):
            header.append(self.ui.tableWidget.takeHorizontalHeaderItem(item).text())
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
           
        regex_pattern = r'https://open.spotify.com/playlist/(\w+)(?:\?si=\w+)?|(\w+)'
        
        self.ui.spFound.setText('Loading Playlist Items ...')
        try:
            id = self.ui.spId.text()
            if not id: raise ValueError
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
        self.ui.ytProgress.setValue(100)
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

            self.ui.tableWidget_2.resizeColumnToContents(0)
            self.ui.tableWidget_2.resizeColumnToContents(1)
            self.ui.tableWidget_2.resizeColumnToContents(2)

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
            worker = Worker(item, self.path)
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

        ytm = yt.yt(os.path.join(self.path, 'oauth.json'))
        self.playlistId = ytm.createPlaylist(self.ui.playlistNameYT.text())
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
            url = rf"https://music.youtube.com/playlist?list={self.playlistId}"
            webbrowser.open(url, 2)
        else:
            newbox.setText('<b>Something went wrong</b>')
            newbox.setWindowTitle('Error')
        newbox.setTextFormat(QtCore.Qt.TextFormat.RichText)
        # newbox.setWindowIcon(QtGui.QIcon('assets/VC_Logo.ico'))
        newbox.exec() 
              
    def softwareInfo(self):
        newbox = QMessageBox()
        newbox.setText('<b>Spotify to YT Music Playlist Converter</b><br><br> <a href="https://github.com/realize-1337/SpotiyTube">© 2023 David \'rEaliZe\' M.</a>')
        newbox.setWindowTitle('Info')
        newbox.setTextFormat(QtCore.Qt.TextFormat.RichText)
        # newbox.setWindowIcon(QtGui.QIcon('assets/VC_Logo.ico'))
        newbox.exec()
    
    def settings(self):
        self.ui.centralwidget.setDisabled(True)
        dialog = QDialog()
        dialog.ui = settingSpotiTube()
        dialog.ui.setupUi(dialog)
        dialog.ui.spSecret.setEchoMode(QLineEdit.EchoMode.Password)
        dialog.ui.settingsButtons.accepted.connect(partial(self.settingsAccepted, dialog))
        dialog.ui.settingsButtons.rejected.connect(partial(self.settingsDeclined, dialog))
        dialog.ui.ytLogin.clicked.connect(partial(self.loginToYTM, dialog))
        if self.ytLoginState == True: 
            dialog.ui.label_5.setText('Already logged in')
            dialog.ui.ytLogin.setText('Press button to renew login')
        else: dialog.ui.label_5.setText('Press the button above to login')

        if self.spKeyState == True:
            id, sc = self.loadSetting()
            dialog.ui.spKey.setText(f"{id}")
            dialog.ui.spSecret.setText(f"{sc}")
        dialog.show()
        dialog.exec()
        
        self.ui.centralwidget.setDisabled(False)
        
    def settingsAccepted(self, dialog):
        spKey = dialog.ui.spKey.text()
        spSecret = dialog.ui.spSecret.text()
        dict = {
            'client_id': spKey,
            'client_secret': spSecret
        }
        if not os.path.exists(os.path.join(self.path, 'keys.json')): 
            with open(os.path.join(self.path, 'keys.json'), encoding="utf8", mode="x+") as file:
                json.dump(dict, file, indent=True)
        else:
            with open(os.path.join(self.path, 'keys.json'), encoding="utf8", mode="w+") as file:
                json.dump(dict, file, indent=True)
                
        self.sp = sp.sp(os.path.join(self.path, 'keys.json'))
        dialog.close()

    def settingsDeclined(self, dialog):
        print('NO')
        dialog.close()

    def loginToYTM(self, dialog):
        dialog.ui.ytLogin.setText('Press this Button after you logged in')
        dialog.ui.ytLogin.clicked.disconnect()
        dialog.ui.ytLogin.clicked.connect(partial(self.afterLogin, dialog))
        if not os.path.isdir(self.path):
            os.mkdir(self.path, mode=777)
        self.code = self.oauth.get_code()
        url = f"{self.code['verification_url']}?user_code={self.code['user_code']}"
        dialog.ui.ytLogin.setText(f'Press this Button after you logged in! Login-Code: {self.code["user_code"]}')
        webbrowser.open(url)

    def afterLogin(self, dialog):
        token = self.oauth.get_token_from_code(self.code["device_code"])
        if len(self.path) > 255:
            return
        with open(os.path.join(self.path, 'oauth.json'), encoding="utf8", mode="w+") as file:
            json.dump(token, file, indent=True)

    def loadSetting(self):
        with open(os.path.join(self.path, 'keys.json'), mode='r+') as oauth:
            self.spKeyState = True
            keys = json.load(oauth)
            return(keys['client_id'], keys['client_secret'])


if __name__ == '__main__':
    alternativePath = None
    if len(sys.argv) > 1: alternativePath = os.path.abspath(sys.argv[1]) 
    app = QApplication([])
    window = UI(alternativePath)
    window.show()
    app.exec()