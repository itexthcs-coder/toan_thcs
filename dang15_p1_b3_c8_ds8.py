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


def bt_dang15_p1_b3_c8_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Tổng điểm từ 2 đến 12
        f2 = random.randint(2, 4)
        f3 = random.randint(5, 8)
        f4 = random.randint(7, 10)
        f5 = random.randint(10, 14)
        f6 = random.randint(13, 17)
        f7 = random.randint(15, 20)
        f8 = random.randint(12, 16)
        f9 = random.randint(9, 13)
        f10 = random.randint(6, 10)
        f11 = random.randint(4, 8)
        f12 = 100 - (f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)
        while f12 < 1:
            f7 -= 1
            f12 += 1
            
        # Số nguyên tố trong {2..12}: 2, 3, 5, 7, 11
        k_nt = f2 + f3 + f5 + f7 + f11
        val_nt = Decimal(k_nt) / Decimal(100)
        str_nt = str(val_nt.normalize()).replace('.', ',')
        
        du = ['$%s$' % str_nt]
        da = random.choice(du)
        
        s = [
            '$%s$' % str((Decimal(k_nt - f2) / Decimal(100)).normalize()).replace('.', ','),
            '$%s$' % str((Decimal(k_nt + f9) / Decimal(100)).normalize()).replace('.', ','),
            '$%s$' % str((Decimal(100 - k_nt) / Decimal(100)).normalize()).replace('.', ','),
            '$%s$' % str((Decimal(k_nt + 2) / Decimal(100)).normalize()).replace('.', ',')
        ]
        s = list(dict.fromkeys([item for item in s if item != da]))
        
        while len(s) < 3:
            extra_cand = '$\\frac{%s}{%s}$' % (random.randint(1, 9), random.randint(10, 29))
            if extra_cand != da and extra_cand not in s:
                s.append(extra_cand)
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        bang = ('\\begin{center}\n'
                '\\begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}\n'
                '\\hline\n'
                'Tổng số chấm & $2$ & $3$ & $4$ & $5$ & $6$ & $7$ & $8$ & $9$ & $10$ & $11$ & $12$ \\\\ \\hline\n'
                'Số lần & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n'
                '\\end{tabular}\n'
                '\\end{center}' % (f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12))
        
        noidungcauhoi = ('Bình gieo đồng thời hai con xúc xắc $100$ lần và ghi lại tổng số chấm xuất hiện ở mỗi lần gieo như bảng dưới đây:\n%s\nXác suất thực nghiệm của biến cố $E$: “Tổng số chấm xuất hiện trên hai con xúc xắc là số nguyên tố”'' bằng'
                         % bang)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Trong các kết quả tổng số chấm từ $2$ đến $12$, các số nguyên tố gồm: $2; 3; 5; 7; 11$.\\'
                   'Số lần xuất hiện tổng số chấm là số nguyên tố trong $100$ lần gieo là $%s + %s + %s + %s + %s = %s$ (lần).\\'
                   'Vậy xác suất thực nghiệm của biến cố $E$ là $\\dfrac{%s}{100} = %s$.'
                   % (f2, f3, f5, f7, f11, k_nt, k_nt, str_nt))

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
