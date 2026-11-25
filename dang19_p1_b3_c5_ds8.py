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

def bt_dang19_p1_b3_c5_ds8(self):
    # Dạng 19: Kết hợp biểu đồ cột kép để tìm chênh lệch thực tế
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        e24_6 = random.randint(330, 360)
        d6 = random.randint(20, 35)
        e25_6 = e24_6 - d6
        
        e24_7 = random.randint(370, 400)
        d7 = random.randint(25, 40)
        e25_7 = e24_7 - d7
        
        tong_tk = d6 + d7
        
        da = '$%s\\text{ kWh}$' % tong_tk
        s_pool = [
            '$%s\\text{ kWh}$' % d6,
            '$%s\\text{ kWh}$' % d7,
            '$%s\\text{ kWh}$' % (tong_tk + 15),
            '$%s\\text{ kWh}$' % (abs(d7 - d6))
        ]
        das1 = random.choice(s_pool)
        s_pool.remove(das1)
        das2 = random.choice(s_pool)
        s_pool.remove(das2)
        das3 = random.choice(s_pool)
        
        # Tỉ lệ trục đứng 400 -> 4.0 cm
        y24_6 = round(e24_6 / 100.0, 2)
        y25_6 = round(e25_6 / 100.0, 2)
        y24_7 = round(e24_7 / 100.0, 2)
        y25_7 = round(e25_7 / 100.0, 2)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[below] {Tháng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Điện năng ($\\text{kWh}$)};\n' +
            '\\foreach \\y/\\lbl in {1/100, 2/200, 3/300, 4/400}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (4.8,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            # Tháng 6
            '\\draw[line width=1pt, fill=black!15] (0.8,0) rectangle (1.5,%s);\n' % y24_6 +
            '\\node[above] at (1.15,%s) {$%s$};\n' % (y24_6, e24_6) +
            '\\draw[line width=1pt, fill=black!45] (1.5,0) rectangle (2.2,%s);\n' % y25_6 +
            '\\node[above] at (1.85,%s) {$%s$};\n' % (y25_6, e25_6) +
            '\\node[below] at (1.5,0) {Tháng $6$};\n' +
            # Tháng 7
            '\\draw[line width=1pt, fill=black!15] (2.9,0) rectangle (3.6,%s);\n' % y24_7 +
            '\\node[above] at (3.25,%s) {$%s$};\n' % (y24_7, e24_7) +
            '\\draw[line width=1pt, fill=black!45] (3.6,0) rectangle (4.3,%s);\n' % y25_7 +
            '\\node[above] at (3.95,%s) {$%s$};\n' % (y25_7, e25_7) +
            '\\node[below] at (3.6,0) {Tháng $7$};\n' +
            # Chú thích
            '\\draw[line width=1pt, fill=black!15] (5.4,3.2) rectangle (5.8,3.5) node[right, yshift=-4pt] {Năm $2024$};\n' +
            '\\draw[line width=1pt, fill=black!45] (5.4,2.4) rectangle (5.8,2.7) node[right, yshift=-4pt] {Năm $2025$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây ghi lại lượng điện tiêu thụ (đơn vị: $\\text{kWh}$) của gia đình bác Hùng trong tháng $6$ và tháng $7$ của hai năm $2024$ và $2025$:\n' +
                         tikz_code + '\n' +
                         'Tổng lượng điện gia đình bác Hùng tiết kiệm được trong hai tháng $6$ và $7$ của năm $2025$ so với cùng kì năm $2024$ là bao nhiêu?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Từ biểu đồ cột kép ta có:\\\\' +
                   '- Lượng điện tiết kiệm được trong tháng $6$ năm $2025$ so với tháng $6$ năm $2024$ là: $%s - %s = %s\\text{ (kWh)}$.\\\\' +
                   '- Lượng điện tiết kiệm được trong tháng $7$ năm $2025$ so với tháng $7$ năm $2024$ là: $%s - %s = %s\\text{ (kWh)}$.\\\\' +
                   'Tổng lượng điện gia đình bác Hùng tiết kiệm được trong hai tháng là:\\\\' +
                   '$$%s + %s = %s\\text{ (kWh)}.$$\\\\' +
                   'Vậy chọn phương án: %s.'
                   ) % (e24_6, e25_6, d6, e24_7, e25_7, d7, d6, d7, tong_tk, da)

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
