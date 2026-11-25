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

def bt_dang16_p1_b3_c5_ds8(self):
    # Dạng 16: Phân tích xu thế biến đổi của một đại lượng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        y_start = random.randint(2017, 2019)
        years = [y_start + i for i in range(5)]
        
        # Tạo dãy giảm liên tục
        p0 = round(random.uniform(17.5, 19.5), 1)
        p1 = round(p0 - random.uniform(2.5, 3.2), 1)
        p2 = round(p1 - random.uniform(2.2, 2.8), 1)
        p3 = round(p2 - random.uniform(2.5, 3.3), 1)
        p4 = round(p3 - random.uniform(2.0, 2.8), 1)
        vals = [p0, p1, p2, p3, p4]
        
        def fmt_vn(val):
            return str(val).replace('.', ',')
            
        v_str = [fmt_vn(x) for x in vals]
        ys = [round(x / 5.0, 2) for x in vals]
        
        da = 'Giảm liên tục qua các năm'
        s_pool = [
            'Tăng đều qua các năm',
            'Không ổn định, lúc tăng lúc giảm',
            'Giữ nguyên không đổi trong suốt giai đoạn'
        ]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Năm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Tỉ lệ ($\\%%$)};\n' +
            '\\foreach \\y/\\lbl in {1/5, 2/10, 3/15, 4/20}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (P1) at (1.0,%s);\n' % ys[0] +
            '\\coordinate (P2) at (2.1,%s);\n' % ys[1] +
            '\\coordinate (P3) at (3.2,%s);\n' % ys[2] +
            '\\coordinate (P4) at (4.3,%s);\n' % ys[3] +
            '\\coordinate (P5) at (5.4,%s);\n' % ys[4] +
            '\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5);\n' +
            '\\fill (P1) circle (1pt) node[above] {$%s$};\n' % v_str[0] +
            '\\fill (P2) circle (1pt) node[above] {$%s$};\n' % v_str[1] +
            '\\fill (P3) circle (1pt) node[above] {$%s$};\n' % v_str[2] +
            '\\fill (P4) circle (1pt) node[above] {$%s$};\n' % v_str[3] +
            '\\fill (P5) circle (1pt) node[above] {$%s$};\n' % v_str[4] +
            '\\node[below] at (1.0,0) {$%s$};\n' % years[0] +
            '\\node[below] at (2.1,0) {$%s$};\n' % years[1] +
            '\\node[below] at (3.2,0) {$%s$};\n' % years[2] +
            '\\node[below] at (4.3,0) {$%s$};\n' % years[3] +
            '\\node[below] at (5.4,0) {$%s$};\n' % years[4] +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Quan sát biểu đồ đoạn thẳng biểu diễn tỉ lệ hộ nghèo của một huyện miền núi từ năm $%s$ đến năm $%s$:\n' % (years[0], years[4]) +
                         tikz_code + '\n' +
                         'Nhận xét nào sau đây đúng về xu thế của tỉ lệ hộ nghèo tại huyện này?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Từ trái sang phải, đường biểu diễn đi xuống liên tục từ $%s\\%%$ (năm $%s$) xuống $%s\\%%$ (năm $%s$), $%s\\%%$ (năm $%s$), $%s\\%%$ (năm $%s$) và còn $%s\\%%$ (năm $%s$).\\\\' +
                   'Vậy xu thế của tỉ lệ hộ nghèo tại huyện này là: %s.'
                   ) % (v_str[0], years[0], v_str[1], years[1], v_str[2], years[2], v_str[3], years[3], v_str[4], years[4], da.lower())

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
