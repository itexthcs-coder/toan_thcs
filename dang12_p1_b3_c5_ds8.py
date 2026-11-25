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

def bt_dang12_p1_b3_c5_ds8(self):
    # Dạng 12: Giải thích ngộ nhận độ dốc do trục ngang chia không đều
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        y1 = random.randint(2014, 2016)
        y2 = y1 + 1
        y3 = y2 + 1
        gap = random.choice([4, 5, 6])
        y4 = y3 + gap
        
        v1 = random.randint(100, 120)
        v2 = v1 + random.randint(10, 15)
        v3 = v2 + random.randint(10, 15)
        v4 = v3 + random.randint(45, 65)
        
        da = 'khoảng cách thời gian giữa mốc $%s$ và $%s$ là $%s$ năm, không đều với các mốc $1$ năm trước đó' % (y3, y4, gap)
        s_pool = [
            'gốc trục đứng của biểu đồ bắt đầu từ giá trị $0$',
            'số lượng cây xanh không phải là số liệu thống kê theo thời gian',
            'biểu đồ đoạn thẳng không dùng để biểu diễn số lượng cây trồng'
        ]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.0,0) node[below] {Năm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số cây};\n' +
            '\\foreach \\y/\\lbl in {1/50, 2/100, 3/150, 4/200}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (5.5,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (A) at (1.0,%s);\n' % round(v1/50.0, 2) +
            '\\coordinate (B) at (2.2,%s);\n' % round(v2/50.0, 2) +
            '\\coordinate (C) at (3.4,%s);\n' % round(v3/50.0, 2) +
            '\\coordinate (D) at (4.6,%s);\n' % round(v4/50.0, 2) +
            '\\draw[line width=1pt] (A)--(B)--(C)--(D);\n' +
            '\\fill (A) circle (1pt) node[above left] {$%s$};\n' % v1 +
            '\\fill (B) circle (1pt) node[above left] {$%s$};\n' % v2 +
            '\\fill (C) circle (1pt) node[above left] {$%s$};\n' % v3 +
            '\\fill (D) circle (1pt) node[above] {$%s$};\n' % v4 +
            '\\node[below] at (1.0,0) {$%s$};\n' % y1 +
            '\\node[below] at (2.2,0) {$%s$};\n' % y2 +
            '\\node[below] at (3.4,0) {$%s$};\n' % y3 +
            '\\node[below] at (4.6,0) {$%s$};\n' % y4 +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây biểu diễn số lượng cây xanh trồng được của một phường tại các năm $%s, %s, %s, %s$:\n' % (y1, y2, y3, y4) +
                         tikz_code + '\n' +
                         'Trên biểu đồ, đoạn thẳng nối từ năm $%s$ đến năm $%s$ dốc đứng lên rất mạnh. Ta không thể kết luận năm $%s$ tốc độ trồng cây tăng đột biến so với năm trước đó vì' % (y3, y4, y4))
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Trong biểu đồ đoạn thẳng, khi các điểm quan sát trên trục ngang chia không đều nhau, ta không thể dựa vào độ dốc của đoạn thẳng để kết luận về tốc độ tăng hay giảm của đại lượng.\\\\' +
                   'Ở biểu đồ này, ba mốc đầu cách nhau $1$ năm ($%s, %s, %s$), nhưng mốc cuối nhảy cách $%s$ năm (từ $%s$ đến $%s$) mà vẫn vẽ cùng độ rộng trên trục ngang.\\\\' +
                   'Vậy nguyên nhân là do %s.'
                   ) % (y1, y2, y3, gap, y3, y4, da)

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
