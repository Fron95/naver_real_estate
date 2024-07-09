# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLabel, QPushButton
import pandas as pd
from datetime import datetime
from module.Naver_seoul_land import Naver_seoul_land
from module.Naver_fetch_articles import Naver_fetch_articles
from module.FileManager import FileManager
from widget.ProgressBarWidget import ProgressBarWidget
from widget.CheckBoxWidget import CheckBoxWidget
from PySide6.QtCore import QThread, Signal

class Ui_MainWindow(object):
    def __init__(self):
        self.naver = Naver_fetch_articles()
        self.filemanager = FileManager()        
        self.data = self.naver.total_apts_naver_got.copy()
        self.result = pd.DataFrame()
        self.folder_path = self.filemanager.result_folder

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 1042)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.progressBar = ProgressBarWidget(self.centralwidget)
        self.progressBar.setGeometry(280, 900, 800, 50)  # progressBar 위치와 크기 설정

        self.progresslabel = QLabel(self.centralwidget)
        self.progresslabel.setGeometry(280, 850, 281, 32)  # progresslabel 위치와 크기 설정
