# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 518)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/default/img/app/haikutwitter64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 401, 491))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("width: ")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 110, 381, 341))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_5 = QtWidgets.QFrame(self.tab)
        self.frame_5.setGeometry(QtCore.QRect(110, 10, 281, 91))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_30 = QtWidgets.QLabel(self.frame_5)
        self.label_30.setGeometry(QtCore.QRect(30, 40, 49, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_5)
        self.label_31.setGeometry(QtCore.QRect(110, 40, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_5)
        self.label_32.setGeometry(QtCore.QRect(10, 40, 21, 16))
        self.label_32.setAutoFillBackground(False)
        self.label_32.setStyleSheet("")
        self.label_32.setScaledContents(False)
        self.label_32.setWordWrap(False)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_5)
        self.label_33.setGeometry(QtCore.QRect(90, 40, 20, 20))
        self.label_33.setObjectName("label_33")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #555")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(120, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #555")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setGeometry(QtCore.QRect(100, 60, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 40, 41, 41))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/default/img/app/Website_Edit_Profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.tabWidget_2.raise_()
        self.frame_2.raise_()
        self.frame_5.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 381, 131))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.label_5.setStyleSheet("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(120, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(120, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(160, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #555")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(230, 90, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(270, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #555")
        self.label_14.setObjectName("label_14")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 140, 381, 421))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(10, 10, 91, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_6 = QtWidgets.QFrame(self.tab_2)
        self.frame_6.setGeometry(QtCore.QRect(110, 10, 261, 111))
        self.frame_6.setAutoFillBackground(True)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_34 = QtWidgets.QLabel(self.frame_6)
        self.label_34.setGeometry(QtCore.QRect(10, 40, 61, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:#555")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_6)
        self.label_35.setGeometry(QtCore.QRect(10, 60, 49, 17))
        self.label_35.setObjectName("label_35")
        self.label_4.raise_()
        self.frame_6.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.tabWidget_3.raise_()
        self.frame.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 381, 111))
        self.label_15.setStyleSheet("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(10, 40, 91, 91))
        self.label_16.setStyleSheet("")
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(10, 140, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(10, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(40, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: #555")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(110, 170, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 200, 381, 361))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_4.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tabWidget_4.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget_4.addTab(self.tab_16, "")
        self.label_29 = QtWidgets.QLabel(self.tab_4)
        self.label_29.setGeometry(QtCore.QRect(160, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: #555")
        self.label_29.setObjectName("label_29")
        self.frame_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4.setGeometry(QtCore.QRect(10, 40, 91, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 381, 111))
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("")
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(10, 40, 91, 91))
        self.label_23.setStyleSheet("")
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setGeometry(QtCore.QRect(10, 140, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_5)
        self.label_25.setGeometry(QtCore.QRect(10, 170, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_5)
        self.label_26.setGeometry(QtCore.QRect(40, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: #555")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_5)
        self.label_27.setGeometry(QtCore.QRect(110, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setGeometry(QtCore.QRect(170, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: #555")
        self.label_28.setObjectName("label_28")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 200, 381, 361))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tabWidget_5.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tabWidget_5.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.tabWidget_5.addTab(self.tab_19, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.tabWidget_5.addTab(self.tab_20, "")
        self.frame_3 = QtWidgets.QFrame(self.tab_5)
        self.frame_3.setGeometry(QtCore.QRect(10, 40, 91, 91))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tabWidget.addTab(self.tab_5, "")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("background:#a0a0a")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Display")
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        self.menuFind = QtWidgets.QMenu(self.menubar)
        self.menuFind.setObjectName("menuFind")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuText = QtWidgets.QMenu(self.menuSettings)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/default/img/app/Prefs_Fonts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuText.setIcon(icon2)
        self.menuText.setObjectName("menuText")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_app = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionAbout_app.setFont(font)
        self.actionAbout_app.setObjectName("actionAbout_app")
        self.actionAbout_qt = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionAbout_qt.setFont(font)
        self.actionAbout_qt.setObjectName("actionAbout_qt")
        self.actionEnter_to_Twitter = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/default/img/app/Action_Login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnter_to_Twitter.setIcon(icon3)
        font = QtGui.QFont()
        self.actionEnter_to_Twitter.setFont(font)
        self.actionEnter_to_Twitter.setObjectName("actionEnter_to_Twitter")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/default/img/app/Server_NewsFeed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon4)
        font = QtGui.QFont()
        self.actionUpdate.setFont(font)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionQuit_2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/default/img/app/Action_GoBack_3_Large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit_2.setIcon(icon5)
        font = QtGui.QFont()
        self.actionQuit_2.setFont(font)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionIncrease_text = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionIncrease_text.setFont(font)
        self.actionIncrease_text.setObjectName("actionIncrease_text")
        self.actionReduce_text = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionReduce_text.setFont(font)
        self.actionReduce_text.setObjectName("actionReduce_text")
        self.actionDefault_font_size = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        self.actionDefault_font_size.setFont(font)
        self.actionDefault_font_size.setObjectName("actionDefault_font_size")
        self.actionFind_user = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/default/img/app/App_TextSearch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind_user.setIcon(icon6)
        self.actionFind_user.setObjectName("actionFind_user")
        self.actionFind_user_by = QtWidgets.QAction(MainWindow)
        self.actionFind_user_by.setIcon(icon6)
        self.actionFind_user_by.setObjectName("actionFind_user_by")
        self.actionFind_tweets_by = QtWidgets.QAction(MainWindow)
        self.actionFind_tweets_by.setIcon(icon6)
        self.actionFind_tweets_by.setObjectName("actionFind_tweets_by")
        self.actionIncrease = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/default/img/app/List_Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIncrease.setIcon(icon7)
        self.actionIncrease.setObjectName("actionIncrease")
        self.actionReduce = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/default/img/app/Action_Stop_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReduce.setIcon(icon8)
        self.actionReduce.setObjectName("actionReduce")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setIcon(icon2)
        self.actionDefault.setObjectName("actionDefault")
        self.actionAbout_QT = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/default/img/app/qt"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_QT.setIcon(icon9)
        self.actionAbout_QT.setObjectName("actionAbout_QT")
        self.actionAbout_QtTwitter = QtWidgets.QAction(MainWindow)
        self.actionAbout_QtTwitter.setIcon(icon)
        self.actionAbout_QtTwitter.setObjectName("actionAbout_QtTwitter")
        self.menuAccount.addAction(self.actionEnter_to_Twitter)
        self.menuAccount.addAction(self.actionUpdate)
        self.menuAccount.addSeparator()
        self.menuAccount.addAction(self.actionQuit_2)
        self.menuFind.addAction(self.actionFind_user)
        self.menuFind.addAction(self.actionFind_user_by)
        self.menuFind.addAction(self.actionFind_tweets_by)
        self.menuText.addAction(self.actionIncrease)
        self.menuText.addAction(self.actionReduce)
        self.menuText.addAction(self.actionDefault)
        self.menuSettings.addAction(self.menuText.menuAction())
        self.menuHelp.addAction(self.actionAbout_QT)
        self.menuHelp.addAction(self.actionAbout_QtTwitter)
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuFind.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtTwitter"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tweets"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Tweets and replies"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Media"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Likes"))
        self.label_3.setText(_translate("MainWindow", "Кайзер öф Раша"))
        self.label_30.setText(_translate("MainWindow", "Ukraine"))
        self.label_31.setText(_translate("MainWindow", "Joined 11/19"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><img width=21 src=\":/default/img/app/Misc_Earth.png\"/></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><img width=16 src=\":/default/img/app/App_Clock.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "98"))
        self.label_7.setText(_translate("MainWindow", "Following"))
        self.label_8.setText(_translate("MainWindow", "Followers"))
        self.label_9.setText(_translate("MainWindow", "23"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/@jDan734/img/@jDan734/image.jpg\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "@jDan734"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"381\" height=\"131\" src=\":/@navalny/img/@navalny/600x200\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/@navalny/img/@navalny/h-qrVrmY_400x400.jpg\" width=\"91\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Alexey Navalny"))
        self.label_11.setText(_translate("MainWindow", "1.2K"))
        self.label_12.setText(_translate("MainWindow", "Following"))
        self.label_13.setText(_translate("MainWindow", "2.1M"))
        self.label_14.setText(_translate("MainWindow", "Followers"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), _translate("MainWindow", "Tweets"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MainWindow", "Tweets and replies"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Media"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Likes"))
        self.label_34.setText(_translate("MainWindow", "@navalny"))
        self.label_35.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "@navalny"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"381\" height=\"111\" src=\":/@PutinGame/img/@PutinGame/600x200\"/></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"91\" src=\":/@PutinGame/img/@PutinGame/r7MLH5S3_400x400.jpeg\"/></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Путин Играющий"))
        self.label_18.setText(_translate("MainWindow", "178"))
        self.label_19.setText(_translate("MainWindow", "Following"))
        self.label_20.setText(_translate("MainWindow", "44.1K"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), _translate("MainWindow", "Tweets"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MainWindow", "Tweets and replies"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), _translate("MainWindow", "Media"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), _translate("MainWindow", "Likes"))
        self.label_29.setText(_translate("MainWindow", "Followers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "@PutinGame"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"381\" height=\"111\" src=\":/@max_katz/img/@max_katz/600x200\"/></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><img width=\"91\" height=\"91\" src=\":/@max_katz/img/@max_katz/5vBuo9nc_400x400.jpg\"/></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "Максим Кац"))
        self.label_25.setText(_translate("MainWindow", "411"))
        self.label_26.setText(_translate("MainWindow", "Following"))
        self.label_27.setText(_translate("MainWindow", "181.3K"))
        self.label_28.setText(_translate("MainWindow", "Followers"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), _translate("MainWindow", "Tweets"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("MainWindow", "Tweets and replies"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_19), _translate("MainWindow", "Media"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_20), _translate("MainWindow", "Likes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "@max_katz"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.menuFind.setTitle(_translate("MainWindow", "Find"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuText.setTitle(_translate("MainWindow", "Font size"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout_app.setText(_translate("MainWindow", "About QtTwitter"))
        self.actionAbout_qt.setText(_translate("MainWindow", "About QT"))
        self.actionEnter_to_Twitter.setText(_translate("MainWindow", "Enter to Twitter"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionQuit_2.setText(_translate("MainWindow", "Quit"))
        self.actionIncrease_text.setText(_translate("MainWindow", "Increase font size"))
        self.actionReduce_text.setText(_translate("MainWindow", "Reduce font size"))
        self.actionDefault_font_size.setText(_translate("MainWindow", "Default font size"))
        self.actionFind_user.setText(_translate("MainWindow", "Find user"))
        self.actionFind_user_by.setText(_translate("MainWindow", "Find user by @"))
        self.actionFind_tweets_by.setText(_translate("MainWindow", "Find tweets by #"))
        self.actionIncrease.setText(_translate("MainWindow", "Increase"))
        self.actionReduce.setText(_translate("MainWindow", "Reduce"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionAbout_QT.setText(_translate("MainWindow", "About QT"))
        self.actionAbout_QtTwitter.setText(_translate("MainWindow", "About QtTwitter"))
import qttwitter_rc
