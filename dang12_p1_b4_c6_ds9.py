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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang12_p1_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        dist = random.choice([800, 900, 1000, 1200])
        dv = random.choice([50, 80, 100])
        nghi_phut = random.choice([30, 45, 90])
        nghi_gio = Decimal(str(nghi_phut)) / Decimal('60')
        tong_gio = Decimal(str(random.choice(['4.5', '5.5', '6'])))
        bay_gio = tong_gio - nghi_gio
        sai_tong = tong_gio + nghi_gio

        tong_str = str(tong_gio.normalize()).replace('.', ',')
        nghi_str = str(nghi_gio.normalize()).replace('.', ',')
        bay_str = str(bay_gio.normalize()).replace('.', ',')
        sai_str = str(sai_tong.normalize()).replace('.', ',')

        # Các đáp án trắc nghiệm
        du = ['$\\dfrac{%s}{x} + \\dfrac{%s}{x + %s} = %s$' % (dist, dist, dv, bay_str)]
        da = random.choice(du)
        s = [
            '$\\dfrac{%s}{x} + \\dfrac{%s}{x + %s} = %s$' % (dist, dist, dv, tong_str),
            '$\\dfrac{%s}{x} + \\dfrac{%s}{x - %s} = %s$' % (dist, dist, dv, bay_str),
            '$\\dfrac{%s}{x} + \\dfrac{%s}{x + %s} = %s$' % (dist, dist, dv, sai_str),
            '$\\dfrac{%s}{x} - \\dfrac{%s}{x + %s} = %s$' % (dist, dist, dv, bay_str)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Một máy bay bay từ thành phố A đến thành phố B cách nhau $%s\\text{ km}$, nghỉ tại B $%s\\text{ phút}$ rồi quay trở lại A với vận tốc lớn hơn vận tốc lúc đi là $%s\\text{ km/h}$. Tổng thời gian cả đi, nghỉ và về hết $%s\\text{ giờ}$. Gọi $x\\text{ (km/h)}$ ($x > 0$) là vận tốc máy bay lúc đi, phương trình của bài toán là'''
                         % (dist, nghi_phut, dv, tong_str))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Đổi $%s\\text{ phút} = %s\\text{ giờ}$.\\\\
Thời gian máy bay đi từ A đến B là $\\dfrac{%s}{x}$ (giờ).\\\\
Vận tốc máy bay lúc về là $x + %s\\text{ (km/h)}$ nên thời gian bay từ B về A là $\\dfrac{%s}{x + %s}$ (giờ).\\\\
Tổng thời gian cả đi, nghỉ và về là $%s\\text{ giờ}$ nên ta có phương trình:
$$\\dfrac{%s}{x} + %s + \\dfrac{%s}{x + %s} = %s \\text{ hay } \\dfrac{%s}{x} + \\dfrac{%s}{x + %s} = %s.$$'''
                   % (nghi_phut, nghi_str, dist, dv, dist, dv, tong_str, dist, nghi_str, dist, dv, tong_str, dist, dist, dv, bay_str))
    
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
