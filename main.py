from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QComboBox, QTableWidgetItem
from PyQt6 import QtCore, QtGui
import subprocess
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
    }  
}

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tableYT(options)
        self.ui.spFound.setText('Enter Playlist ID or link')
        self.ui.spSearch.clicked.connect(self.getSpotifyPlaylist)

    def getSpotifyPlaylist(self):
        # Missing: Regex
        id = self.ui.spId.text()
        print(id)

    def tableYT(self, options:dict):
        for k, v in options.items():
            row_count = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(row_count)
            combo_box = QComboBox()
            maxRatio = 0
            run = 0
            for key, value in v.items():
                if key == 'target':
                    item = QTableWidgetItem(value['title'])
                    self.ui.tableWidget_2.setItem(row_count, 0, item)
                    item = QTableWidgetItem(value['artist'])
                    self.ui.tableWidget_2.setItem(row_count, 1, item)
                    continue
                text = f"{value['title']} - {value['artist']} // (R: {'%.2f' % float(value['matchRatio'])})"
                combo_box.addItem(text)
                combo_box.setItemData(run, key)
                if float(value['matchRatio']) > maxRatio: 
                    maxRatio = float(value['matchRatio'])
                    combo_box.setCurrentIndex(run)
                    item = QTableWidgetItem(f'{"%.2f" % maxRatio}')
                    self.ui.tableWidget_2.setItem(row_count, 2, item)
                run += 1
            self.ui.tableWidget_2.setCellWidget(row_count, 3, combo_box)

        
    def push(self, id):
        print(id)


app = QApplication([])
window = UI()
window.show()
app.exec()