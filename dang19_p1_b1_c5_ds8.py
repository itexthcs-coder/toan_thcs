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


def bt_dang19_p1_b1_c5_ds8(self):
    # Dạng 19: Phân loại dữ liệu tổng hợp từ bảng thống kê nhiều cột
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        t1 = round(random.uniform(6.20, 6.60), 2)
        t2 = round(t1 - random.uniform(0.15, 0.30), 2)
        t3 = round(t2 - random.uniform(0.10, 0.25), 2)
        
        s_t1 = str(t1).replace('.', ',')
        s_t2 = str(t2).replace('.', ',')
        s_t3 = str(t3).replace('.', ',')
        
        c1 = random.randint(18, 22)
        c2 = random.randint(17, 21)
        c3 = random.randint(16, 20)
        
        bang_vdv = (
            "\\begin{center}\n"
            "\\begin{tabular}{|l|c|c|c|}\n"
            "\\hline\n"
            "\\textbf{Tên vận động viên} & \\textbf{Huy chương} & \\textbf{Số lần nhảy} & \\textbf{Thành tích cao nhất (m)} \\\\\n"
            "\\hline\n"
            "Nguyễn Văn Hùng & Vàng & $%s$ & $%s$ \\\\\n"
            "\\hline\n"
            "Trần Quốc Dũng & Bạc & $%s$ & $%s$ \\\\\n"
            "\\hline\n"
            "Lê Minh Tuấn & Đồng & $%s$ & $%s$ \\\\\n"
            "\\hline\n"
            "\\end{tabular}\n"
            "\\end{center}"
            % (c1, s_t1, c2, s_t2, c3, s_t3)
        )
        
        da = "$2$ cột (cột Tên vận động viên và cột Huy chương)"
        das1 = "$1$ cột (chỉ có cột Tên vận động viên)"
        das2 = "$3$ cột (cột Tên vận động viên, cột Huy chương và cột Số lần nhảy)"
        das3 = "$0$ cột (tất cả các cột đều biểu diễn số liệu)"
        
        noidungcauhoi = ('''Cho bảng thống kê thông tin của một nhóm vận động viên nhảy xa dưới đây:
%s
Trong bảng thống kê trên, có bao nhiêu cột dữ liệu thuộc nhóm \\textbf{dữ liệu không là số}?'''
                         % bang_vdv)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('''Ta phân loại dữ liệu của từng cột trong bảng thống kê:\\\\
- Cột \\textbf{Tên vận động viên} (Nguyễn Văn Hùng, Trần Quốc Dũng, Lê Minh Tuấn): là dữ liệu không là số, không thể sắp thứ tự.\\\\
- Cột \\textbf{Huy chương} (Vàng, Bạc, Đồng): là dữ liệu không là số, có thể sắp thứ tự.\\\\
- Cột \\textbf{Số lần nhảy} ($%s; %s; %s$): là số liệu rời rạc.\\\\
- Cột \\textbf{Thành tích cao nhất (m)} ($%s; %s; %s$): là số liệu liên tục.\\\\
Vậy có tất cả $2$ cột dữ liệu thuộc nhóm dữ liệu không là số.'''
                   % (c1, c2, c3, s_t1, s_t2, s_t3))

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
