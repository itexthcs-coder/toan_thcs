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

def bt_dang17_p1_b3_c5_ds8(self):
    # Dạng 17: So sánh xu thế hai đại lượng trên cùng một biểu đồ
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # A tăng: 11, 14, 18, 22
        # B giảm: 21, 17, 13, 10
        d_a = random.randint(0, 2)
        a_vals = [11 + d_a, 14 + d_a, 18 + d_a, 22 + d_a]
        b_vals = [21 + d_a, 17 + d_a, 13 + d_a, 10 + d_a]
        
        da = 'Giữa Quý II và Quý III; tại thời điểm giao nhau doanh thu hai cửa hàng bằng nhau, sau đó Cửa hàng A vượt lên dẫn trước'
        s_pool = [
            'Giữa Quý I và Quý II; tại thời điểm này doanh thu của cả hai cửa hàng đều đạt mức thấp nhất',
            'Giữa Quý III và Quý IV; sau thời điểm này Cửa hàng B vượt lên dẫn trước Cửa hàng A',
            'Hai đường biểu diễn luôn song song với nhau nên không có điểm cắt nhau'
        ]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        ya = [round(v / 5.0, 2) for v in a_vals]
        yb = [round(v / 5.0, 2) for v in b_vals]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[below] {Quý};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,5.2) node[left] {Doanh thu (tỉ đồng)};\n' +
            '\\foreach \\y/\\lbl in {1/5, 2/10, 3/15, 4/20, 5/25}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (5.0,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            # Đường A (nét liền)
            '\\coordinate (A1) at (1.0,%s);\n' % ya[0] +
            '\\coordinate (A2) at (2.2,%s);\n' % ya[1] +
            '\\coordinate (A3) at (3.4,%s);\n' % ya[2] +
            '\\coordinate (A4) at (4.6,%s);\n' % ya[3] +
            '\\draw[line width=1pt] (A1)--(A2)--(A3)--(A4);\n' +
            '\\fill (A1) circle (1pt) node[below] {$%s$};\n' % a_vals[0] +
            '\\fill (A2) circle (1pt) node[below] {$%s$};\n' % a_vals[1] +
            '\\fill (A3) circle (1pt) node[above] {$%s$};\n' % a_vals[2] +
            '\\fill (A4) circle (1pt) node[above] {$%s$};\n' % a_vals[3] +
            # Đường B (nét đứt)
            '\\coordinate (B1) at (1.0,%s);\n' % yb[0] +
            '\\coordinate (B2) at (2.2,%s);\n' % yb[1] +
            '\\coordinate (B3) at (3.4,%s);\n' % yb[2] +
            '\\coordinate (B4) at (4.6,%s);\n' % yb[3] +
            '\\draw[line width=1pt, dashed] (B1)--(B2)--(B3)--(B4);\n' +
            '\\fill (B1) circle (1pt) node[above] {$%s$};\n' % b_vals[0] +
            '\\fill (B2) circle (1pt) node[above] {$%s$};\n' % b_vals[1] +
            '\\fill (B3) circle (1pt) node[below] {$%s$};\n' % b_vals[2] +
            '\\fill (B4) circle (1pt) node[below] {$%s$};\n' % b_vals[3] +
            '\\node[below] at (1.0,0) {Quý I};\n' +
            '\\node[below] at (2.2,0) {Quý II};\n' +
            '\\node[below] at (3.4,0) {Quý III};\n' +
            '\\node[below] at (4.6,0) {Quý IV};\n' +
            # Chú thích
            '\\draw[line width=1pt] (5.3,3.8) -- (6.0,3.8) node[right] {Cửa hàng A};\n' +
            '\\draw[line width=1pt, dashed] (5.3,3.1) -- (6.0,3.1) node[right] {Cửa hàng B};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây biểu diễn doanh thu (tỉ đồng) của Cửa hàng A và Cửa hàng B trong $4$ quý của năm:\n' +
                         tikz_code + '\n' +
                         'Hai đường biểu diễn doanh thu của hai cửa hàng cắt nhau tại khoảng thời gian nào và mang ý nghĩa gì?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Quan sát biểu đồ:\\\\' +
                   '- Tại Quý II, doanh thu Cửa hàng A là $%s$ tỉ đồng nhỏ hơn Cửa hàng B ($%s$ tỉ đồng).\\\\' +
                   '- Tại Quý III, doanh thu Cửa hàng A tăng lên $%s$ tỉ đồng lớn hơn Cửa hàng B ($%s$ tỉ đồng).\\\\' +
                   'Do đó, hai đường biểu diễn cắt nhau trong khoảng giữa Quý II và Quý III. Tại giao điểm này doanh thu hai cửa hàng bằng nhau, và từ sau thời điểm đó Cửa hàng A vượt lên dẫn trước Cửa hàng B.\\\\' +
                   'Vậy chọn phương án: %s.'
                   ) % (a_vals[1], b_vals[1], a_vals[2], b_vals[2], da)

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
