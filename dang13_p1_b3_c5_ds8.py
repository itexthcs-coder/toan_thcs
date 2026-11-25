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

def bt_dang13_p1_b3_c5_ds8(self):
    # Dạng 13: Giải thích sự thay đổi hình dạng đường gấp khúc khi co giãn trục đứng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v = [120, 135, 130, 150]
        delta = random.choice([0, 10, 20])
        v = [x + delta for x in v]
        
        da = 'Lan chia khoảng đơn vị trên trục đứng rộng hơn (hoặc giới hạn trục đứng nhỏ hơn) so với Mai'
        s_pool = [
            'Lan đã cộng thêm $100$ vào tất cả các số liệu trong bảng của Mai',
            'hai bạn sử dụng hai bộ số liệu hoàn toàn khác nhau để vẽ biểu đồ',
            'Mai đã vẽ sai thứ tự các quý từ Quý I đến Quý IV trên trục ngang'
        ]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        # Vẽ 2 hình nhỏ song song minh họa: hình 1 trục đứng 110..170, hình 2 trục đứng 0..300
        y_min1 = 110 + delta
        y_max1 = 170 + delta
        ys1 = [round((x - y_min1) / 20.0, 2) for x in v]
        ys2 = [round(x / 100.0, 2) for x in v]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            # Hình a (Lan)
            '\\draw[line width=1pt, ->] (0,0) -- (4.2,0) node[below] {Quý};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[left] {Sách};\n' +
            '\\node[left] at (0,0) {$%s$};\n' % y_min1 +
            '\\node[left] at (0,3) {$%s$};\n' % y_max1 +
            '\\coordinate (A1) at (0.8,%s);\n' % ys1[0] +
            '\\coordinate (A2) at (1.8,%s);\n' % ys1[1] +
            '\\coordinate (A3) at (2.8,%s);\n' % ys1[2] +
            '\\coordinate (A4) at (3.8,%s);\n' % ys1[3] +
            '\\draw[line width=1pt] (A1)--(A2)--(A3)--(A4);\n' +
            '\\fill (A1) circle (1pt) (A2) circle (1pt) (A3) circle (1pt) (A4) circle (1pt);\n' +
            '\\node[below] at (2.1,-0.5) {Biểu đồ của Lan};\n' +
            # Hình b (Mai)
            '\\begin{scope}[xshift=6.2cm]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.2,0) node[below] {Quý};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[left] {Sách};\n' +
            '\\node[left] at (0,0) {$0$};\n' +
            '\\node[left] at (0,3) {$300$};\n' +
            '\\coordinate (B1) at (0.8,%s);\n' % ys2[0] +
            '\\coordinate (B2) at (1.8,%s);\n' % ys2[1] +
            '\\coordinate (B3) at (2.8,%s);\n' % ys2[2] +
            '\\coordinate (B4) at (3.8,%s);\n' % ys2[3] +
            '\\draw[line width=1pt] (B1)--(B2)--(B3)--(B4);\n' +
            '\\fill (B1) circle (1pt) (B2) circle (1pt) (B3) circle (1pt) (B4) circle (1pt);\n' +
            '\\node[below] at (2.1,-0.5) {Biểu đồ của Mai};\n' +
            '\\end{scope}\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Hai bạn Lan và Mai cùng vẽ biểu đồ đoạn thẳng biểu diễn số quyển sách đọc được trong $4$ quý của thư viện trường lần lượt là $%s, %s, %s, %s$ như hình vẽ dưới đây:\n' % (v[0], v[1], v[2], v[3]) +
                         tikz_code + '\n' +
                         'Biểu đồ của Lan có đường gấp khúc dốc và nhọn hơn hẳn so với biểu đồ của Mai có đường gấp khúc gần như nằm ngang. Nguyên nhân hợp lí nhất là')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Cả hai biểu đồ đều biểu diễn cùng một dãy số liệu ($%s, %s, %s, %s$).\\\\' +
                   'Tuy nhiên, khi thay đổi tỉ lệ chia khoảng trên trục đứng (kéo giãn khoảng đơn vị hoặc thu hẹp giới hạn trên của trục đứng), độ cao chênh lệch giữa các điểm tăng lên làm cho đường gấp khúc trở nên dốc hơn.\\\\' +
                   'Vậy nguyên nhân là do %s.'
                   ) % (v[0], v[1], v[2], v[3], da)

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
