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

def bt_dang7_p1_b3_c5_ds8(self):
    # Dạng 7: Đọc số liệu trên biểu đồ đoạn thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        times = ['4h', '8h', '12h', '16h', '20h']
        temps_raw = random.sample([37.5, 38.0, 38.4, 38.8, 39.2, 39.5], 5)
        
        idx_max = temps_raw.index(max(temps_raw))
        da = 'Lúc $%s$' % times[idx_max]
        
        s_pool = ['Lúc $%s$' % times[i] for i in range(5) if i != idx_max]
        das1 = random.choice(s_pool)
        s_pool.remove(das1)
        das2 = random.choice(s_pool)
        s_pool.remove(das2)
        das3 = random.choice(s_pool)
        
        def fmt_vn(val):
            s = str(val)
            return s.replace('.', ',')
            
        t_str = [fmt_vn(v) for v in temps_raw]
        # Gốc trục đứng 37, mỗi đơn vị 0.5 -> y = (val - 37) * 1.5
        ys = [round((v - 37.0) * 1.5, 2) for v in temps_raw]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.5,0) node[below] {Giờ};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Nhiệt độ ($^\\circ\\text{C}$)};\n' +
            '\\foreach \\y/\\lbl in {0/37, 1.5/38, 3.0/39, 4.2/39{,}8}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (6.0,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\coordinate (P1) at (1.0,%s);\n' % ys[0] +
            '\\coordinate (P2) at (2.2,%s);\n' % ys[1] +
            '\\coordinate (P3) at (3.4,%s);\n' % ys[2] +
            '\\coordinate (P4) at (4.6,%s);\n' % ys[3] +
            '\\coordinate (P5) at (5.8,%s);\n' % ys[4] +
            '\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5);\n' +
            '\\fill (P1) circle (1pt) node[above] {$%s$};\n' % t_str[0] +
            '\\fill (P2) circle (1pt) node[above] {$%s$};\n' % t_str[1] +
            '\\fill (P3) circle (1pt) node[above] {$%s$};\n' % t_str[2] +
            '\\fill (P4) circle (1pt) node[above] {$%s$};\n' % t_str[3] +
            '\\fill (P5) circle (1pt) node[above] {$%s$};\n' % t_str[4] +
            '\\node[below] at (1.0,0) {$4\\text{h}$};\n' +
            '\\node[below] at (2.2,0) {$8\\text{h}$};\n' +
            '\\node[below] at (3.4,0) {$12\\text{h}$};\n' +
            '\\node[below] at (4.6,0) {$16\\text{h}$};\n' +
            '\\node[below] at (5.8,0) {$20\\text{h}$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng sau ghi lại nhiệt độ cơ thể của một bệnh nhân sốt xuất huyết được đo cách nhau mỗi $4$ giờ trong ngày:\n' +
                         tikz_code + '\n' +
                         'Thời điểm nào trong ngày nhiệt độ của bệnh nhân đạt mức cao nhất?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Đọc số liệu tại các điểm trên biểu đồ đoạn thẳng ta có:\\\\' +
                   '- Lúc $4\\text{h}$: $%s^\\circ\\text{C}$; lúc $8\\text{h}$: $%s^\\circ\\text{C}$; lúc $12\\text{h}$: $%s^\\circ\\text{C}$; lúc $16\\text{h}$: $%s^\\circ\\text{C}$; lúc $20\\text{h}$: $%s^\\circ\\text{C}$.\\\\' +
                   'Điểm cao nhất trên đường gấp khúc có tung độ là $%s^\\circ\\text{C}$ ứng với thời điểm %s.\\\\' +
                   'Vậy nhiệt độ của bệnh nhân đạt mức cao nhất %s.'
                   ) % (t_str[0], t_str[1], t_str[2], t_str[3], t_str[4], t_str[idx_max], da.lower(), da.lower())

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
