# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'naver_real_estate_uiEsqsNR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import copy
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QThread, Signal,QEventLoop,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient, 
    QIcon, QImage, QKeySequence, QLinearGradient, 
    QPainter, QPalette, QPixmap, QRadialGradient, QMovie,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenu, QToolButton, QDoubleSpinBox, QMessageBox,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,QDialog,QVBoxLayout, QComboBox, QPlainTextEdit,
    QSpinBox, QSplitter, QStatusBar, QWidget, QAbstractItemView)

# superqt
from superqt import QRangeSlider

import pandas as pd
import os
from datetime import datetime
from module.Naver_seoul_land import Naver_seoul_land
from module.Naver_fetch_articles import Naver_fetch_articles
from module.FileManager import FileManager
# 위젯
from widget.ProgressBarWidget import ProgressBarWidget  # 추가된 부분
from widget.CheckBoxWidget import CheckBoxWidget


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException
import time






class Ui_MainWindow(object):
    def __init__(self, authorization_token = None, cookies = None) :
        self.filemanager = FileManager()        
        self.result = pd.DataFrame()
        self.folder_path = self.filemanager.result_folder
        self.naver = Naver_fetch_articles(authorization_token = authorization_token, cookies = cookies)
        self.data = self.naver.total_apts_naver_got.copy()
        self.authorization = self.naver.authorization
        self.cookies = self.naver.cookies
        tik = time.time()
        # self.load_header_cookies()
        tok = time.time()
        print(tok - tik,"초가소요되었습니다. 쿠키가져오는데")
        print(self.cookies)



    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1273, 1042)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # GIF QLabel 추가
        self.loading_label = QLabel("zz",self.centralwidget)
        self.loading_label.setGeometry(280, 942, 50, 50)
        self.loading_label.setVisible(True)  # 초기에는 숨겨둠
        self.loading_label.setScaledContents(True)
        self.loading_movie = QMovie("loading.gif")
        self.loading_label.setMovie(self.loading_movie)

        self.progressBar = ProgressBarWidget(self.centralwidget)  # 수정된 부분
        self.progresslabel = QLabel(self.centralwidget)
        self.progresslabel.setGeometry(380, 950, 281, 32)
        self.progresslabel.setStyleSheet(u"font-size:20px;")

        
        
        
        
        
        


        # ToolButton 추가
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(750, 950, 41, 41))
        self.toolButton.clicked.connect(self.show_dialog)
        self.toolButton.setText('...')


        # 중단버튼 추가
        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(1120, 950, 131, 41))
        self.pushButton_stop.clicked.connect(self.stop_fetching)
        self.pushButton_stop.setText('수집중단')
        self.pushButton_stop.setStyleSheet(u"background-color:red;\n"
"color:white;\n"
"font-size:20px;\n"
"")
        self.pushButton_stop.setVisible(False)
        

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(1120, 950, 131, 41))
        self.pushButton_start.setStyleSheet(u"background-color:green;\n"
"color:white;\n"
"font-size:20px;\n"
"")
        self.pushButton_start.clicked.connect(self.fetching)    


        self.pushButton_to_excel = QPushButton(self.centralwidget)
        self.pushButton_to_excel.setObjectName(u"pushButton_to_excel")
        self.pushButton_to_excel.setGeometry(QRect(980, 950, 131, 41))
        self.pushButton_to_excel.clicked.connect(lambda : self.download(saving_format='csv'))
        self.pushButton_openFolder = QPushButton(self.centralwidget)
        self.pushButton_openFolder.setObjectName(u"pushButton_openFolder")
        self.pushButton_openFolder.setGeometry(QRect(840, 950, 131, 41))
        self.pushButton_openFolder.setStyleSheet(u"")
        self.pushButton_openFolder.clicked.connect(self.open_folder)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(1010, 520, 231, 411))
        
        self.listWidget_selected = QListWidget(self.groupBox_2)
        
        self.listWidget_selected.setObjectName(u"listWidget_selected")
        self.listWidget_selected.setGeometry(QRect(10, 50, 211, 361))

        self.pushButton_selectAll_selected = QPushButton(self.groupBox_2)
        self.pushButton_selectAll_selected.setObjectName(u"pushButton_selectAll_selected")
        self.pushButton_selectAll_selected.setGeometry(QRect(10, 20, 211, 20))
        self.pushButton_selectAll_selected.setText(u"전체선택/해제")
        self.pushButton_selectAll_selected.clicked.connect(lambda : self.selectAllOrNone(self.listWidget_selected))

        self.pushButton_add = QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(920, 640, 75, 61))
        self.pushButton_add.clicked.connect(self.get_selected_complex_data)
        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(920, 720, 75, 61))
        self.pushButton_delete.clicked.connect(self.delete_selected_items)
        
        self.splitter_17 = QSplitter(self.centralwidget)
        self.splitter_17.setObjectName(u"splitter_17")
        self.splitter_17.setGeometry(QRect(10, 20, 1231, 491))
        self.splitter_17.setOrientation(Qt.Vertical)
        self.groupBox_4 = QGroupBox(self.splitter_17)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"font-size :15px;")
        self.splitter_16 = QSplitter(self.groupBox_4)
        self.splitter_16.setObjectName(u"splitter_16")
        self.splitter_16.setGeometry(QRect(20, 30, 681, 20))
        self.splitter_16.setOrientation(Qt.Horizontal)
        self.checkBox_realEstateType_APT = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_APT.setObjectName(u"checkBox_realEstateType_APT")
        self.checkBox_realEstateType_APT.stateChanged.connect(self.get_infos)
        self.checkBox_realEstateType_APT.setChecked(True)
        self.splitter_16.addWidget(self.checkBox_realEstateType_APT)
        self.checkBox_realEstateType_ABYG = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_ABYG.setObjectName(u"checkBox_realEstateType_ABYG")
        self.checkBox_realEstateType_ABYG.stateChanged.connect(self.get_infos)
        self.splitter_16.addWidget(self.checkBox_realEstateType_ABYG)
        self.checkBox_realEstateType_JGC = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_JGC.setObjectName(u"checkBox_realEstateType_JGC")
        self.checkBox_realEstateType_JGC.stateChanged.connect(self.get_infos)
        self.splitter_16.addWidget(self.checkBox_realEstateType_JGC)
        self.checkBox_realEstateType_OPST = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_OPST.setObjectName(u"checkBox_realEstateType_OPST")
        self.checkBox_realEstateType_OPST.stateChanged.connect(self.get_infos)
        self.splitter_16.addWidget(self.checkBox_realEstateType_OPST)
        self.checkBox_realEstateType_OBYG = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_OBYG.setObjectName(u"checkBox_realEstateType_OBYG")
        self.checkBox_realEstateType_OBYG.stateChanged.connect(self.get_infos)
        self.splitter_16.addWidget(self.checkBox_realEstateType_OBYG)
        self.checkBox_realEstateType_JGB = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_JGB.setObjectName(u"checkBox_realEstateType_JGB")
        self.checkBox_realEstateType_JGB.stateChanged.connect(self.get_infos)
        self.splitter_16.addWidget(self.checkBox_realEstateType_JGB)
        self.checkBox_realEstateType_PRE = QCheckBox(self.splitter_16)
        self.checkBox_realEstateType_PRE.setObjectName(u"checkBox_realEstateType_PRE")
        self.checkBox_realEstateType_PRE.stateChanged.connect(self.get_infos)
        self.checkBox_realEstateType_PRE.setChecked(True)
        self.splitter_16.addWidget(self.checkBox_realEstateType_PRE)
        self.splitter_17.addWidget(self.groupBox_4)
        self.groupBox_3 = QGroupBox(self.splitter_17)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"font-size:15px")
        self.splitter_4 = QSplitter(self.groupBox_3)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(20, 30, 201, 20))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.checkBox_tradeType_A1 = CheckBoxWidget(self.splitter_4)
        # self.checkBox_tradeType_A1 = QCheckBox(self.splitter_4)
        # self.checkBox_tradeType_A1.setObjectName(u"checkBox_tradeType_A1")
        # self.checkBox_tradeType_A1.stateChanged.connect(self.get_infos)
        # self.checkBox_tradeType_A1.setChecked(True)
        self.splitter_4.addWidget(self.checkBox_tradeType_A1)
        self.checkBox_tradeType_B1 = QCheckBox(self.splitter_4)
        self.checkBox_tradeType_B1.setObjectName(u"checkBox_tradeType_B1")
        self.checkBox_tradeType_B1.stateChanged.connect(self.get_infos)
        self.splitter_4.addWidget(self.checkBox_tradeType_B1)
        self.splitter_17.addWidget(self.groupBox_3)
        self.groupBox_5 = QGroupBox(self.splitter_17)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"font-size :15px;")
        self.spinBox_minPrice = QSpinBox(self.groupBox_5)
        self.spinBox_minPrice.setObjectName(u"spinBox_minPrice")
        self.spinBox_minPrice.valueChanged.connect(self.get_infos)
        self.spinBox_minPrice.setGeometry(QRect(20, 40, 161, 31))
        self.spinBox_minPrice.setMaximum(899999999)
        self.spinBox_minPrice.setSingleStep(1000)
        self.spinBox_maxPrice = QSpinBox(self.groupBox_5)
        self.spinBox_maxPrice.setObjectName(u"spinBox_maxPrice")
        self.spinBox_maxPrice.valueChanged.connect(self.get_infos)
        self.spinBox_maxPrice.setGeometry(QRect(260, 40, 161, 31))
        self.spinBox_maxPrice.setMinimum(1)
        self.spinBox_maxPrice.setMaximum(900000000)
        self.spinBox_maxPrice.setSingleStep(1000)
        self.spinBox_maxPrice.setValue(1000000)
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 50, 201, 16))
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 50, 21, 16))
        self.label_dealRange = QLabel(self.groupBox_5)
        self.label_dealRange.setObjectName(u"label_dealRange")
        self.label_dealRange.setGeometry(QRect(800, 20, 411, 51))
        self.label_dealRange.setStyleSheet(u"color : red;\n"
"")
        self.splitter_17.addWidget(self.groupBox_5)
        self.groupBox_6 = QGroupBox(self.splitter_17)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"font-size :15px;")
        self.splitter_10 = QSplitter(self.groupBox_6)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setGeometry(QRect(30, 30, 300, 20))
        self.splitter_10.setOrientation(Qt.Horizontal)
        self.splitter_11 = QSplitter(self.splitter_10)
        self.splitter_11.setObjectName(u"splitter_11")
        self.splitter_11.setOrientation(Qt.Horizontal)

        # 평수범위
        self.comboBox_areaMin = QComboBox(self.splitter_11)
        self.comboBox_areaMin.setObjectName(u"comboBox_areaMin")
        self.label_areaRange = QLabel("< 면적 <",self.splitter_11)
        self.comboBox_areaMax = QComboBox(self.splitter_11)
        self.comboBox_areaMax.setObjectName(u"comboBox_areaMax")
        self.comboBox_areaMin.currentIndexChanged.connect(self.get_infos)
        self.comboBox_areaMax.currentIndexChanged.connect(self.get_infos)

        self.areaMinList = ['0평','10평','20평','30평','40평','50평','60평','70평' ]
        self.areaMaxList = ['10평','20평','30평','40평','50평','60평','70평',"70평~" ]

        for area in  self.areaMinList :
            self.comboBox_areaMin.addItem(area)
        for area in  self.areaMaxList :
            self.comboBox_areaMax.addItem(area)
        self.comboBox_areaMax.setCurrentIndex(self.comboBox_areaMax.count()-1)
        self.splitter_11.setSizes([100, 50, 100])




        # self.slider = QRangeSlider(self.groupBox_5)
        # self.slider.setOrientation(Qt.Horizontal)
        # self.slider.setValue((20, 80))
        # self.checkBox_area_00 = QCheckBox(self.splitter_11)
        # self.checkBox_area_00.setObjectName(u"checkBox_area_00")
        # self.checkBox_area_00.clicked.connect(self.get_infos)
        # self.checkBox_area_00.setChecked(True)
        # self.splitter_11.addWidget(self.checkBox_area_00)
        # self.checkBox_area_10 = QCheckBox(self.splitter_11)
        # self.checkBox_area_10.setObjectName(u"checkBox_area_10")
        # self.checkBox_area_10.clicked.connect(self.get_infos)
        # self.checkBox_area_10.setChecked(True)
        # self.splitter_11.addWidget(self.checkBox_area_10)
        # self.checkBox_area_20 = QCheckBox(self.splitter_11)
        # self.checkBox_area_20.setObjectName(u"checkBox_area_20")
        # self.checkBox_area_20.clicked.connect(self.get_infos)
        # self.checkBox_area_20.setChecked(True)
        # self.splitter_11.addWidget(self.checkBox_area_20)
        # self.checkBox_area_30 = QCheckBox(self.splitter_11)
        # self.checkBox_area_30.setObjectName(u"checkBox_area_30")
        # self.checkBox_area_30.clicked.connect(self.get_infos)
        # self.checkBox_area_30.setChecked(True)
        # self.splitter_11.addWidget(self.checkBox_area_30)
        # self.checkBox_area_40 = QCheckBox(self.splitter_11)
        # self.checkBox_area_40.setObjectName(u"checkBox_area_40")
        # self.checkBox_area_40.clicked.connect(self.get_infos)
        # self.checkBox_area_40.setChecked(True)
        # self.splitter_11.addWidget(self.checkBox_area_40)
        # self.checkBox_area_50 = QCheckBox(self.splitter_11)
        # self.checkBox_area_50.setObjectName(u"checkBox_area_50")
        # self.checkBox_area_50.clicked.connect(self.get_infos)
        # self.checkBox_area_50.setChecked(True)
        # self.splitter_11.addWidget(self.checkBox_area_50)
        # self.checkBox_area_60 = QCheckBox(self.splitter_11)
        # self.checkBox_area_60.setObjectName(u"checkBox_area_60")
        # self.checkBox_area_60.clicked.connect(self.get_infos)
        # self.checkBox_area_60.setChecked(True)
        # self.checkBox_area_60.setTristate(False)
        # self.splitter_11.addWidget(self.checkBox_area_60)
        self.splitter_10.addWidget(self.splitter_11)
        self.label_areaRange = QLabel(self.groupBox_6)
        self.label_areaRange.setObjectName(u"label_areaRange")
        self.label_areaRange.setGeometry(QRect(800, 10, 411, 51))
        self.label_areaRange.setStyleSheet(u"color : red;\n"
                                           
        #    평 / 제곱미터 구분

"")
        self.splitter_17.addWidget(self.groupBox_6)
        self.groupBox_7 = QGroupBox(self.splitter_17)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"font-size :15px;")
        self.splitter_12 = QSplitter(self.groupBox_7)
        self.splitter_12.setObjectName(u"splitter_12")
        self.splitter_12.setGeometry(QRect(30, 30, 300, 20))
        self.splitter_12.setOrientation(Qt.Horizontal)
        self.splitter_13 = QSplitter(self.splitter_12)
        self.splitter_13.setObjectName(u"splitter_13")
        self.splitter_13.setOrientation(Qt.Horizontal)
                # 현재 연도 계산
        self.current_year = datetime.now().year
        self.years = ["40","35","30", "25", "20", "15", "10","5","0"]
        

        # 승인 날짜 범위
        self.comboBox_old = QComboBox(self.splitter_13)
        self.comboBox_old.setObjectName("comboBox_old")
        self.label_dateRange = QLabel("< 승인 날짜 <", self.splitter_13)
        self.comboBox_recent = QComboBox(self.splitter_13)
        self.comboBox_recent.setObjectName("comboBox_recent")
        self.recentList = [f"{year}년 전" for year in self.years] + ["입주예정"]
        self.oldList = ["최고"] + [f"{year}년 전" for year in self.years]
        
        self.splitter_13.setSizes([100, 50, 100])

        for year in self.recentList:
            self.comboBox_recent.addItem(year)
        for year in self.oldList:
            self.comboBox_old.addItem(year)
        self.comboBox_recent.setCurrentIndex(len(self.oldList) - 2)

        self.comboBox_recent.currentIndexChanged.connect(self.get_infos)
        self.comboBox_old.currentIndexChanged.connect(self.get_infos)

        # self.checkBox_approvalDate_0 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_0.setObjectName(u"checkBox_approvalDate_0")
        # self.checkBox_approvalDate_0.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_0.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_0)
        # self.checkBox_approvalDate_2 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_2.setObjectName(u"checkBox_approvalDate_2")
        # self.checkBox_approvalDate_2.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_2.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_2)
        # self.checkBox_approvalDate_4 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_4.setObjectName(u"checkBox_approvalDate_4")
        # self.checkBox_approvalDate_4.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_4.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_4)
        # self.checkBox_approvalDate_10 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_10.setObjectName(u"checkBox_approvalDate_10")
        # self.checkBox_approvalDate_10.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_10.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_10)
        # self.checkBox_approvalDate_15 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_15.setObjectName(u"checkBox_approvalDate_15")
        # self.checkBox_approvalDate_15.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_15.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_15)
        # self.checkBox_approvalDate_20 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_20.setObjectName(u"checkBox_approvalDate_20")
        # self.checkBox_approvalDate_20.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_20.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_20)
        # self.checkBox_approvalDate_25 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_25.setObjectName(u"checkBox_approvalDate_25")
        # self.checkBox_approvalDate_25.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_25.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_25)
        # self.checkBox_approvalDate_30 = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_30.setObjectName(u"checkBox_approvalDate_30")
        # self.checkBox_approvalDate_30.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_30.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_30)
        # self.checkBox_approvalDate_max = QCheckBox(self.splitter_13)
        # self.checkBox_approvalDate_max.setObjectName(u"checkBox_approvalDate_max")
        # self.checkBox_approvalDate_max.stateChanged.connect(self.get_infos)
        # self.checkBox_approvalDate_max.setChecked(True)
        # self.splitter_13.addWidget(self.checkBox_approvalDate_max)
        self.splitter_12.addWidget(self.splitter_13)
        self.label_approvalDateRange = QLabel(self.groupBox_7)
        self.label_approvalDateRange.setObjectName(u"label_approvalDateRange")
        self.label_approvalDateRange.setGeometry(QRect(800, 20, 411, 51))
        self.label_approvalDateRange.setStyleSheet(u"color : red;\n"
"")
        self.splitter_17.addWidget(self.groupBox_7)
        self.groupBox_8 = QGroupBox(self.splitter_17)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"font-size :15px;")
        self.label_totalHouseholdsRange = QLabel(self.groupBox_8)
        self.label_totalHouseholdsRange.setObjectName(u"label_totalHouseholdsRange")
        self.label_totalHouseholdsRange.setGeometry(QRect(800, 10, 411, 51))
        self.label_totalHouseholdsRange.setStyleSheet(u"color : red;\n"
"")
        self.splitter_14 = QSplitter(self.groupBox_8)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setGeometry(QRect(30, 30, 300, 20))
        self.splitter_14.setOrientation(Qt.Horizontal)
        


        self.houseHolds = ['0', '300', '500', '700', '1000', '1500', '2000', '3000']
        self.comboBox_minHouseHoldCount = QComboBox(self.splitter_14)
        self.comboBox_minHouseHoldCount.setObjectName("comboBox_minHouseHoldCount")
        self.comboBox_minHouseHoldCount.setCurrentIndex(0)
        self.label_dateRange = QLabel("< 세대수 <", self.splitter_14)
        self.comboBox_maxHouseHoldCount = QComboBox(self.splitter_14)
        self.comboBox_maxHouseHoldCount.setObjectName("comboBox_maxHouseHoldCount")
        
        
        self.comboBox_minHouseHoldCount.addItems(self.houseHolds[:-1])
        self.comboBox_maxHouseHoldCount.addItems(self.houseHolds[1:] + ["최대"])
        
        self.comboBox_maxHouseHoldCount.setCurrentIndex(self.comboBox_maxHouseHoldCount.count() -3)
        self.comboBox_minHouseHoldCount.currentIndexChanged.connect(self.get_infos)
        self.comboBox_maxHouseHoldCount.currentIndexChanged.connect(self.get_infos)
        self.splitter_14.setSizes([100, 50, 100])



        # self.checkBox_totalHouseholds_0 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_0.setObjectName(u"checkBox_totalHouseholds_0")
        # self.checkBox_totalHouseholds_0.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_0.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_0)
        # self.checkBox_totalHouseholds_100 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_100.setObjectName(u"checkBox_totalHouseholds_100")
        # self.checkBox_totalHouseholds_100.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_100.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_100)
        # self.checkBox_totalHouseholds_300 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_300.setObjectName(u"checkBox_totalHouseholds_300")
        # self.checkBox_totalHouseholds_300.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_300.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_300)
        # self.checkBox_totalHouseholds_500 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_500.setObjectName(u"checkBox_totalHouseholds_500")
        # self.checkBox_totalHouseholds_500.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_500.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_500)
        # self.checkBox_totalHouseholds_700 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_700.setObjectName(u"checkBox_totalHouseholds_700")
        # self.checkBox_totalHouseholds_700.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_700.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_700)
        # self.checkBox_totalHouseholds_1000 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_1000.setObjectName(u"checkBox_totalHouseholds_1000")
        # self.checkBox_totalHouseholds_1000.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_1000.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_1000)
        # self.checkBox_totalHouseholds_1500 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_1500.setObjectName(u"checkBox_totalHouseholds_1500")
        # self.checkBox_totalHouseholds_1500.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_1500.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_1500)
        # self.checkBox_totalHouseholds_2000 = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_2000.setObjectName(u"checkBox_totalHouseholds_2000")
        # self.checkBox_totalHouseholds_2000.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_2000.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_2000)
        # self.checkBox_totalHouseholds_max = QCheckBox(self.splitter_14)
        # self.checkBox_totalHouseholds_max.setObjectName(u"checkBox_totalHouseholds_max")
        # self.checkBox_totalHouseholds_max.stateChanged.connect(self.get_infos)
        # self.checkBox_totalHouseholds_max.setChecked(True)
        # self.splitter_14.addWidget(self.checkBox_totalHouseholds_max)
        self.splitter_17.addWidget(self.groupBox_8)
        self.splitter_18 = QSplitter(self.centralwidget)
        self.splitter_18.setObjectName(u"splitter_18")
        self.splitter_18.setGeometry(QRect(10, 520, 901, 411))
        self.splitter_18.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_18)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 101, 21))
        self.label.setStyleSheet(u"font-size :15px;")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(680, 20, 101, 21))
        self.label_2.setStyleSheet(u"font-size :15px;")
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 50, 0, 361))
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter_2 = QSplitter(self.splitter)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_3 = QSplitter(self.splitter_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_2.addWidget(self.splitter_3)
        self.splitter.addWidget(self.splitter_2)
        self.splitter_all_select = QSplitter(self.groupBox)
        
        self.splitter_all = QSplitter(self.groupBox)
        self.splitter_all.setObjectName(u"splitter_all")
        self.splitter_all.setGeometry(QRect(20, 20, 871, 361))
        self.splitter_all.setOrientation(Qt.Horizontal)
        
        
            


            
        


        self.splitter_5 = QSplitter(self.groupBox)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(20, 50, 871, 361))
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.listWidget_1 = QListWidget(self.splitter_5)
        self.listWidget_1.setObjectName(u"listWidget_1")

        
        # item1 = self.dataSetting(type='province')
        # self.listWidget_1.addItem(item1)
        for provinceNo in list(self.data['provinceNo'].unique()) :
            name = self.data[self.data['provinceNo'] == provinceNo]['provinceName'].values[0]
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, provinceNo)
            self.listWidget_1.addItem(item)
        # self.listWidget_1.addItems()
        self.listWidget_1.itemSelectionChanged.connect(self.display_district)
        self.splitter_5.addWidget(self.listWidget_1)
        self.listWidget_2 = QListWidget(self.splitter_5)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.itemSelectionChanged.connect(self.display_dong)
        self.splitter_5.addWidget(self.listWidget_2)
        self.listWidget_3 = QListWidget(self.splitter_5)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.itemSelectionChanged.connect(self.display_complex)
        self.splitter_5.addWidget(self.listWidget_3)
        
        self.listWidget_4 = QListWidget(self.splitter_5)
        self.listWidget_4.setObjectName(u"listWidget_4")

        
        
        
        

        self.splitter_5.addWidget(self.listWidget_4)


        # 다중 선택 가능하게 설정
        self.listWidget_1.setSelectionMode(QAbstractItemView.MultiSelection)  # 다중 선택 가능하게 설정
        self.listWidget_2.setSelectionMode(QAbstractItemView.MultiSelection)  # 다중 선택 가능하게 설정
        self.listWidget_3.setSelectionMode(QAbstractItemView.MultiSelection)  # 다중 선택 가능하게 설정
        self.listWidget_4.setSelectionMode(QAbstractItemView.MultiSelection)  # 다중 선택 가능하게 설정
        self.listWidget_selected.setSelectionMode(QAbstractItemView.MultiSelection)  # 다중 선택 가능하게 설정

        # 전체선택기능
        # 전체선택버튼
        self.pushButton_selectAll_1 = QPushButton(self.splitter_all)
        self.pushButton_selectAll_1.setText(u"전체선택/해제")
        self.pushButton_selectAll_1.setObjectName(u"pushButton_selectAll_1")
        self.pushButton_selectAll_1.clicked.connect(lambda : self.selectAllOrNone(self.listWidget_1))

        self.pushButton_selectAll_2 = QPushButton(self.splitter_all)
        self.pushButton_selectAll_2.setText(u"전체선택/해제")
        self.pushButton_selectAll_2.setObjectName(u"pushButton_selectAll_2")
        self.pushButton_selectAll_2.clicked.connect(lambda : self.selectAllOrNone(self.listWidget_2))

        self.pushButton_selectAll_3 = QPushButton(self.splitter_all)
        self.pushButton_selectAll_3.setText(u"전체선택/해제")
        self.pushButton_selectAll_3.setObjectName(u"pushButton_selectAll_3")
        self.pushButton_selectAll_3.clicked.connect(lambda : self.selectAllOrNone(self.listWidget_3))

        self.pushButton_selectAll_4 = QPushButton(self.splitter_all)
        self.pushButton_selectAll_4.setText(u"전체선택/해제")
        self.pushButton_selectAll_4.setObjectName(u"pushButton_selectAll_4")
        self.pushButton_selectAll_4.clicked.connect(lambda : self.selectAllOrNone(self.listWidget_4))


        self.splitter_18.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1273, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

        self.get_infos()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc9d1\uc2dc\uc791", None))
        self.pushButton_to_excel.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140\ub2e4\uc6b4\ub85c\ub4dc", None))
        self.pushButton_openFolder.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc \ud3f4\ub354 \uc5f4\uae30", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00 \u25b6", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u25c0 \uc81c\uac70", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\uc885\ub958", None))
        self.checkBox_realEstateType_APT.setText(QCoreApplication.translate("MainWindow", u"\uc544\ud30c\ud2b8", None))
        self.checkBox_realEstateType_ABYG.setText(QCoreApplication.translate("MainWindow", u"\uc544\ud30c\ud2b8\ubd84\uc591\uad8c", None))
        self.checkBox_realEstateType_JGC.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uac74\ucd95", None))
        self.checkBox_realEstateType_OPST.setText(QCoreApplication.translate("MainWindow", u"\uc624\ud53c\uc2a4\ud154", None))
        self.checkBox_realEstateType_OBYG.setText(QCoreApplication.translate("MainWindow", u"\uc624\ud53c\uc2a4\ud154\ubd84\uc591\uad8c", None))
        self.checkBox_realEstateType_JGB.setText(QCoreApplication.translate("MainWindow", u"\uc7ac\uac1c\ubc1c", None))
        self.checkBox_realEstateType_PRE.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uc591\uc911 / \uc608\uc815", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4\ubc29\uc2dd", None))
        self.checkBox_tradeType_A1.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4", None))
        self.checkBox_tradeType_B1.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc138", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4\uac00/\ubd84\uc591\uac00/\uc804\uc138\uac00", None))
        self.spinBox_maxPrice.setSuffix("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"(\ub9cc\uc6d0) (\uc608\uc2dc : 10000 = 1\uc5b5)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_dealRange.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c : ( ) ~ ( ) ", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\uba74\uc801", None))
        # self.checkBox_area_00.setText(QCoreApplication.translate("MainWindow", u"00~33\u33A1\ub300", None))
        # self.checkBox_area_10.setText(QCoreApplication.translate("MainWindow", u"33~66\u33A1", None))
        # self.checkBox_area_20.setText(QCoreApplication.translate("MainWindow", u"66~99\u33A1", None))
        # self.checkBox_area_30.setText(QCoreApplication.translate("MainWindow", u"99~132\u33A1", None))
        # self.checkBox_area_40.setText(QCoreApplication.translate("MainWindow", u"132~165\u33A1", None))
        # self.checkBox_area_50.setText(QCoreApplication.translate("MainWindow", u"165~198\u33A1", None))
        # self.checkBox_area_60.setText(QCoreApplication.translate("MainWindow", u"198\u33A1~\uCD5C\uB300", None))
        self.label_areaRange.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c : ( ) ~ ( ) ", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c", None))
        # self.checkBox_approvalDate_0.setText(QCoreApplication.translate("MainWindow", u"\uc785\uc8fc\uc608\uc815", None))
        # self.checkBox_approvalDate_2.setText(QCoreApplication.translate("MainWindow", u"2\ub144", None))
        # self.checkBox_approvalDate_4.setText(QCoreApplication.translate("MainWindow", u"4\ub144", None))
        # self.checkBox_approvalDate_10.setText(QCoreApplication.translate("MainWindow", u"10\ub144", None))
        # self.checkBox_approvalDate_15.setText(QCoreApplication.translate("MainWindow", u"15\ub144", None))
        # self.checkBox_approvalDate_20.setText(QCoreApplication.translate("MainWindow", u"20\ub144", None))
        # self.checkBox_approvalDate_25.setText(QCoreApplication.translate("MainWindow", u"25\ub144", None))
        # self.checkBox_approvalDate_30.setText(QCoreApplication.translate("MainWindow", u"30\ub144", None))
        # self.checkBox_approvalDate_max.setText(QCoreApplication.translate("MainWindow", u"30\ub144~", None))
        self.label_approvalDateRange.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c : ( ) ~ ( ) ", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\uc138\ub300\uc218", None))
        self.label_totalHouseholdsRange.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc2b9\uc778\uc77c : ( ) ~ ( ) ", None))
        # self.checkBox_totalHouseholds_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        # self.checkBox_totalHouseholds_100.setText(QCoreApplication.translate("MainWindow", u"~100", None))
        # self.checkBox_totalHouseholds_300.setText(QCoreApplication.translate("MainWindow", u"300", None))
        # self.checkBox_totalHouseholds_500.setText(QCoreApplication.translate("MainWindow", u"500", None))
        # self.checkBox_totalHouseholds_700.setText(QCoreApplication.translate("MainWindow", u"700", None))
        # self.checkBox_totalHouseholds_1000.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        # self.checkBox_totalHouseholds_1500.setText(QCoreApplication.translate("MainWindow", u"1500", None))
        # self.checkBox_totalHouseholds_2000.setText(QCoreApplication.translate("MainWindow", u"2000", None))
        # self.checkBox_totalHouseholds_max.setText(QCoreApplication.translate("MainWindow", u"2000~", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc5ed\uc120\ud0dd", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubb3c\uac74\uc120\ud0dd", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84\ubd80\ub3d9\uc0b0", None))
        
    # retranslateUi

    def collect_realEstateType(self):
        # 체크박스 상태 정보 모으기
        checkboxes = {
            "APT": self.checkBox_realEstateType_APT.isChecked(),
            "ABYG": self.checkBox_realEstateType_ABYG.isChecked(),
            "JGC": self.checkBox_realEstateType_JGC.isChecked(),
            "OPST": self.checkBox_realEstateType_OPST.isChecked(),
            "OBYG": self.checkBox_realEstateType_OBYG.isChecked(),
            "JGB": self.checkBox_realEstateType_JGB.isChecked(),
            "PRE": self.checkBox_realEstateType_PRE.isChecked()
        }
        checked_ordered = [key for key in ["APT", "ABYG", "JGC", "OPST", "OBYG", "PRE", "JGB"] if checkboxes[key]]
        real_estate_result = ":".join(checked_ordered)
        print(checked_ordered)
        return checked_ordered, real_estate_result
    
    


    def collect_tradeType(self) :
                # Trade Type 체크박스 상태 정보 모으기
        trade_type_checkboxes = {
            "A1": self.checkBox_tradeType_A1.isChecked(),
            "B1": self.checkBox_tradeType_B1.isChecked()
        }
        checked_trade_type_ordered = [key for key in ["A1", "B1"] if trade_type_checkboxes[key]]
        trade_type_result = ":".join(checked_trade_type_ordered)

        return trade_type_result

    
    def popup_dialogue(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("최대값은 최소값보다 높게 설정되어야 합니다.")
        msg.setWindowTitle("경고")
        msg.exec_()

    def collect_area(self):
        go = True
        while go:
            # 현재 선택된 값 가져오기
            area_min_index = self.comboBox_areaMin.currentIndex()
            area_max_index = self.comboBox_areaMax.currentIndex()
            
            # 면적 값을 숫자로 변환
            area_min = int(self.areaMinList[area_min_index].split('평')[0])
            area_max_str = self.areaMaxList[area_max_index]

            if area_max_str == "70평~":
                area_max = 900000
            else:
                area_max = int(area_max_str.split('평')[0])

            if area_min >= area_max:
                if self.sender().objectName() == "comboBox_areaMax":
                    self.popup_dialogue()  # 다이얼로그 팝업
                    break
                else:
                    area_max_index += 1
                    if area_max_index >= len(self.areaMaxList):  # 인덱스가 범위를 벗어나지 않도록 체크
                        area_max_index = len(self.areaMaxList) - 1
                        break
                    self.comboBox_areaMax.setCurrentIndex(area_max_index)  # UI 갱신
                    QApplication.processEvents(QEventLoop.ExcludeUserInputEvents)  # 이벤트 루프 처리
            else:
                go = False

        return area_min, area_max


    
    def collect_approval_date(self):
        # 현재 선택된 값 가져오기
        recent_index = self.comboBox_recent.currentIndex()
        old_index = self.comboBox_old.currentIndex()
        recent_text = self.comboBox_recent.currentText()
        old_text = self.comboBox_old.currentText()

        # 값을 숫자로 변환
        recent_str = self.recentList[recent_index]
        old_str = self.oldList[old_index]

        # 값 가져오기
        if recent_str == "입주예정":
            recentlyBuildYears = ""
        else:
            recentlyBuildYears = int(recent_str.split('년')[0])

        if old_str == "최고" :
            oldBuildYears = ""
        else:
            oldBuildYears = int(old_str.split('년')[0]  )
            


        if recentlyBuildYears == "" or oldBuildYears == "":
            return str(recentlyBuildYears), str(oldBuildYears)

        if recentlyBuildYears >= oldBuildYears:
            self.comboBox_recent.setCurrentIndex(self.comboBox_recent_current_index)
            self.comboBox_old.setCurrentIndex(self.comboBox_old_current_index)
            self.popup_dialogue()  # 다이얼로그 팝업
        else :            
            return recentlyBuildYears, oldBuildYears

        



    def collect_total_households(self):
        # 값을 숫자로 변환
        minHouseHoldCount = int(self.comboBox_minHouseHoldCount.currentText())
        maxHouseHoldCount = self.comboBox_maxHouseHoldCount.currentText()
        # 값 가져오기
        if maxHouseHoldCount == "최대":
            maxHouseHoldCount = ""  # "최대"를 무한대 값으로 설정
            return str(minHouseHoldCount), str(maxHouseHoldCount)
        else:
            maxHouseHoldCount = int(maxHouseHoldCount)

        if minHouseHoldCount >= maxHouseHoldCount:
            
            # 기존 선택을 유지하도록 인덱스를 원래 상태로 되돌림
            self.comboBox_minHouseHoldCount.setCurrentIndex(self.comboBox_minHouseHoldCount_current_index)
            self.comboBox_maxHouseHoldCount.setCurrentIndex(self.comboBox_MaxHouseHoldCount_current_index)
            self.popup_dialogue()  # 다이얼로그 팝업
        else:
            return str(minHouseHoldCount), str(maxHouseHoldCount)


    
    

    def get_infos(self) : 
        try :
            self.tradeType = self.collect_tradeType()
            self.realEstateTypeOrdered, self.realEstateType = self.collect_realEstateType()

            
            self.minPrice = int(self.spinBox_minPrice.value())
            self.maxPrice = int(self.spinBox_maxPrice.value())

            if self.minPrice >= self.maxPrice :
                self.spinBox_minPrice.setValue(self.spinBox_minPrice_current_value)
                self.spinBox_maxPrice.setValue(self.spinBox_maxPrice_current_value)
                self.popup_dialogue()
            else :
                self.spinBox_minPrice_current_value = self.spinBox_minPrice.value()
                self.spinBox_maxPrice_current_value = self.spinBox_maxPrice.value()
            
            self.pyeongMin, self.pyeongMax = self.collect_area()
            self.pyeongMin, self.pyeongMax = int(self.pyeongMin), int(self.pyeongMax)
            self.areaMin, self.areaMax = int(self.pyeongMin * 3.3), int(self.pyeongMax * 3.3)
            self.recentlyBuildYears, self.oldBuildYears = self.collect_approval_date()
            self.minHouseHoldCount, self.maxHouseHoldCount = self.collect_total_households()
            self.names, self.ids = self.get_selected_items_data(self.listWidget_selected, searching_type='all')
            
            
            self.label_dealRange.setText(f'조회가격범위 : {self.minPrice/10000} ~ {self.maxPrice/10000}(억원)')
            self.label_areaRange.setText(f'조회평수범위 : {self.areaMin} ~ {self.areaMax}(제곱미터)')
            self.label_approvalDateRange.setText(f'조회사용승인범위 : {self.oldBuildYears}(년 전) ~ {self.recentlyBuildYears}(년 전)')
            self.label_totalHouseholdsRange.setText(f'조회세대수 : {self.minHouseHoldCount} ~ {self.maxHouseHoldCount}(세대)')
            self.comboBox_areaMin_current_index = self.comboBox_areaMin.currentIndex()
            self.comboBox_areaMax_current_index = self.comboBox_areaMax.currentIndex()
            self.comboBox_old_current_index = self.comboBox_old.currentIndex()
            self.comboBox_recent_current_index = self.comboBox_recent.currentIndex()
            self.comboBox_minHouseHoldCount_current_index = self.comboBox_minHouseHoldCount.currentIndex()
            self.comboBox_MaxHouseHoldCount_current_index = self.comboBox_maxHouseHoldCount.currentIndex()

            self.display_complex()
        except : 
            pass

    def display_district(self):
        selected_items = self.listWidget_1.selectedItems()
        province_nos = [item.data(Qt.UserRole) for item in selected_items]
        
        # provinceNo를 기반으로 matching_rows 필터링
        matching_rows = self.data[self.data['provinceNo'].isin(province_nos)]
        unique_districts = matching_rows[['districtName', 'districtNo']].drop_duplicates()
        self.listWidget_2.clearSelection()
        self.listWidget_2.clear()
        for i in range(len(unique_districts)):
            item = QListWidgetItem(unique_districts.iloc[i]['districtName'])
            item.setData(Qt.UserRole, unique_districts.iloc[i]['districtNo'])
            self.listWidget_2.addItem(item)


    def display_dong(self):
        
        self.listWidget_3.clearSelection()
        self.listWidget_3.clear()
        self.listWidget_4.clear()

        
        selected_items = self.listWidget_2.selectedItems()
        district_nos = [item.data(Qt.UserRole) for item in selected_items]
        print("length district_nos", len(district_nos))
        # districtNo를 기반으로 matching_rows 필터링
        matching_rows = self.data[self.data['districtNo'].isin(district_nos)]
        unique_dongs = matching_rows[['dongName', 'dongNo']].drop_duplicates()

        
        for i in range(len(unique_dongs)):
            item = QListWidgetItem(unique_dongs.iloc[i]['dongName'])
            item.setData(Qt.UserRole, unique_dongs.iloc[i]['dongNo'])
            self.listWidget_3.addItem(item)


    # def display_complex(self):
        
    #     tik = time.time()
    #     tok = time.time()
    #     print(f"{tok - tik}초 ")
    #     selected_items = self.listWidget_3.selectedItems()        
    #     dong_nos = [item.data(Qt.UserRole) for item in selected_items]

    #     print("length dong_nos", len(dong_nos))

    #     # 세대수 스크리닝
    #     min_household = int(self.minHouseHoldCount)
    #     # print("min_household", min_household)
    #     max_household = float('inf') if self.maxHouseHoldCount == "" else int(self.maxHouseHoldCount)

    #     # 사용승인일 스크리닝
    #     current_year = datetime.now().year
    #     recently_build_years = float('inf') if self.recentlyBuildYears == "" else int(self.recentlyBuildYears)
    #     old_build_years = float('inf') if self.oldBuildYears == "" else int(self.oldBuildYears)
    #     self.data['useApproveYear'] = self.data['useApproveYmd'].astype(str).str[:4].astype(int)
        
    #     tok = time.time()
    #     print(f"{tok - tik}초 ")
    #     # 필터링
    #     self.listWidget_4.clear()
    #     filtered_data = self.data[
    #         (self.data['dongNo'].isin(dong_nos)) &
    #         (self.data['totalHouseHoldCount'] >= min_household) &
    #         (self.data['totalHouseHoldCount'] <= max_household) &
    #         (current_year - self.data['useApproveYear'] >= recently_build_years) &
    #         (current_year - self.data['useApproveYear'] <= old_build_years)
    #     ]

    #     unique_complexes = filtered_data[['complexName', 'complexNo']].drop_duplicates()

    #     tok = time.time()
    #     print(f"{tok - tik}초 ")

    #     for a,b in zip(unique_complexes['complexName'] , unique_complexes['complexNo']):
    #         item = QListWidgetItem(a)
    #         item.setData(Qt.UserRole, b)
    #         self.listWidget_4.addItem(item)


    #     tok = time.time()
    #     print(f"{tok - tik}초 ")

    def display_complex(self):
        tik = time.time()

        selected_items = self.listWidget_3.selectedItems()
        dong_nos = [item.data(Qt.UserRole) for item in selected_items]
        print("length dong_nos", len(dong_nos))

        # 세대수 스크리닝
        min_household = int(self.minHouseHoldCount)
        max_household = float('inf') if self.maxHouseHoldCount == "" else int(self.maxHouseHoldCount)

        # 사용승인일 스크리닝
        current_year = datetime.now().year
        recently_build_years = -float('inf') if self.recentlyBuildYears == "" else int(self.recentlyBuildYears)
        old_build_years = float('inf') if self.oldBuildYears == "" else int(self.oldBuildYears)
        self.data['useApproveYear'] = self.data['useApproveYmd'].astype(str).str[:4].astype(int)

        tok = time.time()
        print(f"Data preparation: {tok - tik}초")

        # 필터링
        filtered_data = self.data[
            (self.data['dongNo'].isin(dong_nos)) &
            (self.data['realEstateType'].isin(self.realEstateTypeOrdered)) &
            (self.data['totalHouseHoldCount'] >= min_household) &
            (self.data['totalHouseHoldCount'] <= max_household) &
            (current_year - self.data['useApproveYear'] >= recently_build_years) &
            (current_year - self.data['useApproveYear'] <= old_build_years)
        ]

        unique_complexes = filtered_data[['complexName', 'complexNo']].drop_duplicates()

        tok = time.time()
        print(f"Filtering data: {tok - tik}초")

        # 기존의 listWidget_4에 있는 항목들 수집
        existing_items_data = {self.listWidget_4.item(i).data(Qt.UserRole) for i in range(self.listWidget_4.count())}

        # 변경 사항만 반영하여 업데이트
        new_items_data = set(unique_complexes['complexNo'])
        items_to_add = new_items_data - existing_items_data
        items_to_remove = existing_items_data - new_items_data

        # 항목 제거
        for i in range(self.listWidget_4.count()-1, -1, -1):
            item = self.listWidget_4.item(i)
            if item.data(Qt.UserRole) in items_to_remove:
                self.listWidget_4.takeItem(i)

        # 항목 추가
        for a, b in zip(unique_complexes['complexName'], unique_complexes['complexNo']):
            if b in items_to_add:
                item = QListWidgetItem(a)
                item.setData(Qt.UserRole, b)
                self.listWidget_4.addItem(item)

        tok = time.time()
        print(f"UI 업데이트: {tok - tik}초")

    

    def get_selected_complex_data(self):
        selected_items = self.listWidget_4.selectedItems()
        
        # 이미 등록된 아이템 데이터 집합 생성
        existing_items_data = {self.listWidget_selected.item(i).data(Qt.UserRole) for i in range(self.listWidget_selected.count())}
        
        tik = time.time()

        for item in selected_items:
            item_data = item.data(Qt.UserRole)  # 고유한 데이터 가져오기
            
            if item_data not in existing_items_data:
                copied_item = QListWidgetItem(item)
                copied_item.setData(Qt.UserRole, item_data)  # 데이터 설정
                self.listWidget_selected.addItem(copied_item)
                existing_items_data.add(item_data)  # 집합에 추가하여 중복 방지

        tok = time.time()
        print(f"{tok - tik:.4f}초가 소요되었습니다.")


    def delete_selected_items(self):
        selected_items = self.listWidget_selected.selectedItems()
        for item in selected_items:
            row = self.listWidget_selected.row(item)
            self.listWidget_selected.takeItem(row)

        

    

    def get_selected_items_data(self, target_widget, searching_type='selected'):
        selected_items= []
        if searching_type == 'selected' :
            selected_items = target_widget.selectedItems()
        elif searching_type == 'all' :
            for index in range(target_widget.count()):
                selected_items.append(target_widget.item(index))
            
            
        texts, datas = [], []
        for item in selected_items:
            texts.append(item.text())
            datas.append(str(item.data(Qt.UserRole)))  # 데이터를 문자열로 변환
        return texts, datas

    

        
    def fetching(self):
        self.get_infos()

        if len(self.ids) < 1 :
            dialog = QDialog(self)
            dialog.setWindowTitle("Popup Dialog")
            # 레이아웃 생성
            layout = QVBoxLayout(dialog)
            # 라벨 생성
            label = QLabel(f"""수집대상이 없습니다. 수집대상을 추가해주세요.""")
            
            # 취소 버튼 생성
            diag_cancel_button = QPushButton("확인", dialog)
            diag_cancel_button.clicked.connect(dialog.accept)  # QDialog의 accept 메서드를 연결
            
            # 레이아웃에 위젯 추가
            layout.addWidget(label)
            layout.addWidget(diag_cancel_button)
            
            # 다이얼로그 실행
            dialog.exec()
        else :
            dialog = QDialog(self)
            dialog.setWindowTitle("Popup Dialog")

            # 레이아웃 생성
            layout = QVBoxLayout(dialog)

            # 라벨 생성
            label = QLabel(f"""
    ✅ 조회정보
        ▪ 조회매물수 : {len(self.names)}
        ▪ 거래유형 : {self.tradeType.replace('A1','매매').replace('B1','전세')}
        ▪ 가격 : {self.minPrice / 10000} ~ {self.maxPrice / 10000} (억)
        ▪ 면적(평) : {self.pyeongMin} ~ {self.pyeongMax} (평)
        ▪ 면적(제곱미터) : {self.areaMin} ~ {self.areaMax} (제곱미터)
        ▪ 사용승인일 : {self.oldBuildYears} ~ {self.recentlyBuildYears} (년 전)
        ▪ 세대 수 : {self.minHouseHoldCount} ~ {self.maxHouseHoldCount} (세대)

    🛑 매물 당 약 15초의 시간이 소요됩니다.
        """, dialog)

            # 수행 버튼 생성
            diag_start_button = QPushButton("수집시작", dialog)
            diag_start_button.clicked.connect(lambda: self.start_fetching(dialog))  # start_fetching 메서드를 연결

            # 취소 버튼 생성
            diag_cancel_button = QPushButton("취소", dialog)
            diag_cancel_button.clicked.connect(dialog.accept)  # QDialog의 accept 메서드를 연결

            self.res = QLabel(dialog)  # self.res를 다이얼로그에 다시 정의

            # 레이아웃에 위젯 추가
            layout.addWidget(label)
            layout.addWidget(diag_start_button)
            layout.addWidget(diag_cancel_button)
            layout.addWidget(self.res)  # self.res를 레이아웃에 추가

            # 다이얼로그 실행
            dialog.exec()

    def start_fetching(self, dialog):

        dialog.accept()  # 다이얼로그 닫기
        self.pushButton_stop.setVisible(True)
        self.pushButton_start.setVisible(False)
        self.loading_label.setVisible(True)  # GIF 활성화
        self.loading_movie.start()  # GIF 재생 시작
        self.req()
        
        
        

    def req(self):
        import requests

        self.res.setText('시작합니다.')
        # self.result = self.naver.fetch(
        #         complexNos=[int(id) for id in self.ids],
        #         realEstateType = self.realEstateType,
        #         tradeType=self.tradeType,
        #         areaNos='',
        #         page=1,
        #         rentPriceMin=self.minPrice,
        #         rentPriceMax=self.maxPrice,
        #         priceMin=self.minPrice,
        #         priceMax=self.maxPrice,
        #         areaMin=self.areaMin,
        #         areaMax=self.areaMax,
        #         oldBuildYears=self.oldBuildYears,
        #         recentlyBuildYears=self.recentlyBuildYears,
        #         minHouseHoldCount=self.minHouseHoldCount,
        #         maxHouseHoldCount=self.maxHouseHoldCount,
        #         # progressChanged=self.progressChanged,
        #     )

        self.worker = self.Worker(self)
        self.worker.progressChanged.connect(self.update_progress)
        self.worker.progressNameChanged.connect(self.update_progressName)
        self.worker.resultChanged.connect(self.update_result)
        self.worker.runningChanged.connect(self.toggle_running)
        self.worker.start()
    
    def update_progress(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            self.loading_label.setVisible(False)  # 완료 시 GIF 숨김
            self.loading_movie.stop()  # GIF 재생 중지
    def update_progressName(self, value):
        self.progresslabel.setText(value)
    def update_result(self, value):
        self.result = value

    def download(self, saving_format = "csv") :
        # 현재 시간을 YYYYMMDDhhmm 형식으로 추출
        current_time = datetime.now().strftime('%Y%m%d%H%M')
        if saving_format == 'csv' :
            self.result.to_csv(os.path.join(self.folder_path, f'결과_{current_time}.csv'), encoding='cp949', index=False)
        if format == 'excel' :
            self.result.to_excel(os.path.join(self.folder_path, f'결과_{current_time}.xlsx'), encoding='cp949', index=False)
    
    def open_folder(self):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        os.startfile(self.folder_path)  # For Windows


    class Worker(QThread) :
        progressChanged = Signal(int)
        progressNameChanged = Signal(str)
        resultChanged = Signal(type(pd.DataFrame()))        
        runningChanged = Signal(bool)        
        
        def __init__(self, parent) :
            super().__init__(parent)
            self.parent = parent
            self.running = True
            
        
        def run(self):
            self.parent.result = self.parent.naver.fetch(
                complexNos=[int(id) for id in self.parent.ids],
                realEstateType = self.parent.realEstateType,
                tradeType=self.parent.tradeType,
                areaNos='',
                page=1,
                rentPriceMin=self.parent.minPrice,
                rentPriceMax=self.parent.maxPrice,
                priceMin=self.parent.minPrice,
                priceMax=self.parent.maxPrice,
                areaMin=self.parent.areaMin,
                areaMax=self.parent.areaMax,
                oldBuildYears=self.parent.oldBuildYears,
                recentlyBuildYears=self.parent.recentlyBuildYears,
                minHouseHoldCount=self.parent.minHouseHoldCount,
                maxHouseHoldCount=self.parent.maxHouseHoldCount,
                progressChanged=self.progressChanged,
                progressNameChanged=self.progressNameChanged,
                resultChanged=self.resultChanged,
                running=self.running
            )
            self.parent.pushButton_stop.setVisible(False)
            self.parent.pushButton_start.setVisible(True)
            self.parent.naver.running = True # 혹시 바뀌었을 상황에 대비하기 위해서

    def show_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Set Delay")

        layout = QVBoxLayout()

        label_delay = QLabel("최대지연 (초) : 2초 권장 ")
        layout.addWidget(label_delay)
        double_spin_box = QDoubleSpinBox()
        double_spin_box.setRange(0.0, 100.0)
        double_spin_box.setDecimals(1)
        double_spin_box.setValue(2.0)
        double_spin_box.setSingleStep(0.1)
        layout.addWidget(double_spin_box)
        
        label_authorization = QLabel("Authorization code:")
        self.plain_text_authorization = QPlainTextEdit()
        self.plain_text_authorization.setPlainText(self.authorization)
        self.plain_text_authorization.textChanged.connect(self.update_authorization)
        layout.addWidget(label_authorization)
        layout.addWidget(self.plain_text_authorization)

        label_cookies = QLabel("Cookies:")
        self.plain_text_cookies = QPlainTextEdit()
        self.plain_text_cookies.setPlainText(json.dumps(self.cookies))  # dict를 문자열로 변환
        self.plain_text_cookies.textChanged.connect(self.update_cookies)
        layout.addWidget(label_cookies)
        layout.addWidget(self.plain_text_cookies)
        
        button = QPushButton("OK")
        button.clicked.connect(lambda: self.set_delay(dialog, double_spin_box.value()))
        layout.addWidget(button)

        dialog.setLayout(layout)
        dialog.exec()

    def update_authorization(self):
        self.authorization = self.plain_text_authorization.toPlainText()
    
    def stop_fetching(self) :
        self.worker.runningChanged.emit(False)
    
    def toggle_running(self) :
        self.naver.running = False
        
        

    def update_cookies(self):
        try:
            self.cookies = json.loads(self.plain_text_cookies.toPlainText())
        except json.JSONDecodeError:
            pass  # 유효하지 않은 JSON 형식인 경우

    def set_delay(self, dialog, value):
        self.delay = value
        dialog.accept()

    
    
    
    


    def selectAllOrNone(self, target):
        if len(target.selectedItems()) < target.count():
            target.selectAll()
        else:
            target.clearSelection()

    def measure_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"{func.__name__} executed in {elapsed_time:.4f} seconds")
            return result
        return wrapper

    
    
    








# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow
# from app import Ui_MainWindow  # 변환된 UI 파일 import

# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()

