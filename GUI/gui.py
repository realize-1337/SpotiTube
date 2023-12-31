# Form implementation generated from reading ui file './GUI/GUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SpotiTube(object):
    def setupUi(self, SpotiTube):
        SpotiTube.setObjectName("SpotiTube")
        SpotiTube.resize(1275, 1090)
        self.centralwidget = QtWidgets.QWidget(parent=SpotiTube)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(35)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 25)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.spId = QtWidgets.QLineEdit(parent=self.tab)
        self.spId.setObjectName("spId")
        self.gridLayout_3.addWidget(self.spId, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.spSearch = QtWidgets.QPushButton(parent=self.tab)
        self.spSearch.setMinimumSize(QtCore.QSize(0, 25))
        self.spSearch.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spSearch.setObjectName("spSearch")
        self.verticalLayout.addWidget(self.spSearch)
        self.spFound = QtWidgets.QLabel(parent=self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spFound.sizePolicy().hasHeightForWidth())
        self.spFound.setSizePolicy(sizePolicy)
        self.spFound.setMinimumSize(QtCore.QSize(0, 16))
        self.spFound.setMaximumSize(QtCore.QSize(16777215, 13))
        font = QtGui.QFont()
        font.setBold(True)
        self.spFound.setFont(font)
        self.spFound.setAutoFillBackground(False)
        self.spFound.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.spFound.setLineWidth(0)
        self.spFound.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.spFound.setScaledContents(True)
        self.spFound.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spFound.setWordWrap(True)
        self.spFound.setIndent(0)
        self.spFound.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.spFound.setObjectName("spFound")
        self.verticalLayout.addWidget(self.spFound)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ytProgress = QtWidgets.QProgressBar(parent=self.tab_2)
        self.ytProgress.setProperty("value", 0)
        self.ytProgress.setObjectName("ytProgress")
        self.gridLayout_7.addWidget(self.ytProgress, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reloadYT = QtWidgets.QPushButton(parent=self.tab_2)
        self.reloadYT.setObjectName("reloadYT")
        self.horizontalLayout.addWidget(self.reloadYT)
        self.commitYT = QtWidgets.QPushButton(parent=self.tab_2)
        self.commitYT.setObjectName("commitYT")
        self.horizontalLayout.addWidget(self.commitYT)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1229, 839))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.playlistNameYT = QtWidgets.QLineEdit(parent=self.tab_2)
        self.playlistNameYT.setObjectName("playlistNameYT")
        self.horizontalLayout_2.addWidget(self.playlistNameYT)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        SpotiTube.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SpotiTube)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1275, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(parent=self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuWindow_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menuWindow_2.setObjectName("menuWindow_2")
        SpotiTube.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SpotiTube)
        self.statusbar.setObjectName("statusbar")
        SpotiTube.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(parent=SpotiTube)
        self.action_Open.setObjectName("action_Open")
        self.action_Settings = QtGui.QAction(parent=SpotiTube)
        self.action_Settings.setObjectName("action_Settings")
        self.menuMain.addAction(self.action_Settings)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuWindow_2.menuAction())

        self.retranslateUi(SpotiTube)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SpotiTube)

    def retranslateUi(self, SpotiTube):
        _translate = QtCore.QCoreApplication.translate
        SpotiTube.setWindowTitle(_translate("SpotiTube", "SpotiTube"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SpotiTube", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SpotiTube", "Artist"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SpotiTube", "Album"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SpotiTube", "Duration"))
        self.label.setText(_translate("SpotiTube", "Spotify Playlist Id or Link"))
        self.spId.setPlaceholderText(_translate("SpotiTube", "ID or Link to Spotify Playlist"))
        self.spSearch.setText(_translate("SpotiTube", "Search Playlist"))
        self.spFound.setText(_translate("SpotiTube", "Found Playlist"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SpotiTube", "Spotify"))
        self.reloadYT.setText(_translate("SpotiTube", "Reload Results"))
        self.commitYT.setText(_translate("SpotiTube", "Commit to YT Music"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("SpotiTube", "Title"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("SpotiTube", "Artist"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("SpotiTube", "Match Ratio"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("SpotiTube", "YouTube Item"))
        self.label_2.setText(_translate("SpotiTube", "Playlist Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SpotiTube", "Youtube Music"))
        self.label_3.setText(_translate("SpotiTube", "Spotify to YT Music Playlist Converter"))
        self.menuMain.setTitle(_translate("SpotiTube", "Main"))
        self.menuWindow_2.setTitle(_translate("SpotiTube", "Info"))
        self.action_Open.setText(_translate("SpotiTube", "&Open"))
        self.action_Settings.setText(_translate("SpotiTube", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpotiTube = QtWidgets.QMainWindow()
    ui = Ui_SpotiTube()
    ui.setupUi(SpotiTube)
    SpotiTube.show()
    sys.exit(app.exec())
