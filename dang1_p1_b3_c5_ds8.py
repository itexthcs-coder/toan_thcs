import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

def bt_dang1_p1_b3_c5_ds8(self):
    # Dạng 1: Nhận diện dữ liệu liên tục và dữ liệu rời rạc
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        n_hs = random.randint(35, 48)
        lop = random.choice(['8A', '8B', '8C', '8D', '8E'])
        sea_games = random.choice([31, 32, 33])
        n_ngay = random.randint(5, 14)
        
        du_list = [
            'Chiều cao (tính theo $\\text{cm}$) của $%s$ học sinh lớp $%s$ trong đợt khám sức khỏe định kì' % (n_hs, lop),
            'Cân nặng (tính theo $\\text{kg}$) của $%s$ học sinh lớp $%s$ đầu năm học' % (n_hs, lop),
            'Thời gian chạy cự li $100\\text{ m}$ (tính theo giây) của $%s$ học sinh lớp $%s$' % (n_hs, lop),
            'Nhiệt độ không khí ngoài trời (tính theo $^\\circ\\text{C}$) đo được tại các thời điểm trong ngày'
        ]
        da = random.choice(du_list)
        
        s_pool = [
            'Số lượng sách giáo khoa bán được trong từng ngày của một nhà sách suốt $%s$ ngày' % n_ngay,
            'Số huy chương vàng mà các đoàn thể thao đạt được tại SEA Games %s' % sea_games,
            'Tên các loại trái cây đặc sản được bày bán tại hội chợ nông sản địa phương',
            'Số học sinh nghỉ học trong từng ngày của lớp $%s$ trong một tuần' % lop,
            'Danh sách các câu lạc bộ ngoại khóa mà học sinh khối $8$ đăng kí tham gia'
        ]
        das1 = random.choice(s_pool)
        s_pool.remove(das1)
        das2 = random.choice(s_pool)
        s_pool.remove(das2)
        das3 = random.choice(s_pool)
        
        noidungcauhoi = ('Trong các dãy dữ liệu thu thập được dưới đây, dữ liệu nào là số liệu liên tục?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Số liệu liên tục là số liệu định lượng có thể nhận mọi giá trị thực trong một khoảng nào đó (thường gắn với các đại lượng đo lường như chiều cao, cân nặng, thời gian, nhiệt độ,...).\\\\' +
                   'Do đó, dãy dữ liệu "%s" là số liệu liên tục.\\\\' +
                   'Các dãy dữ liệu còn lại là dữ liệu định tính hoặc số liệu rời rạc (đếm được bằng các số tự nhiên).'
                   ) % (da)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
