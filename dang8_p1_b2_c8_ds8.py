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



def fmt_frac(num, den):
    f = Fraction(num, den)
    if f.denominator == 1:
        return str(f.numerator)
    return "\\dfrac{%s}{%s}" % (f.numerator, f.denominator)

def fmt_list_str(lst):
    return "; ".join(str(x) for x in lst)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_square(n):
    if n < 1:
        return False
    r = math.isqrt(n)
    return r * r == n

def bt_dang8_p1_b2_c8_ds8(self):
    # Dạng 8: Tình huống gieo xúc xắc 6 mặt - biến cố đơn giản (có hình vẽ minh họa)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        mat_chon = random.randint(1, 6)
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (A) at (0,0);\n"
            "\\coordinate (B) at (1.2,0);\n"
            "\\coordinate (C) at (1.2,1.2);\n"
            "\\coordinate (D) at (0,1.2);\n"
            "\\coordinate (E) at (0.5,1.6);\n"
            "\\coordinate (F) at (1.7,1.6);\n"
            "\\coordinate (G) at (1.7,0.4);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (D)--(E)--(F)--(C) (F)--(G)--(B);\n"
            "\\fill (0.6,0.6) circle (1pt);\n"
            "\\fill (0.6,1.4) circle (1pt) (1.1,1.4) circle (1pt);\n"
            "\\fill (1.45,0.6) circle (1pt) (1.45,0.9) circle (1pt) (1.45,1.2) circle (1pt);\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )
        
        da = '$\\dfrac{1}{6}$'
        
        candidates = [
            fmt_frac(mat_chon, 6) if mat_chon != 1 else '$\\dfrac{5}{6}$',
            '$\\dfrac{1}{5}$',
            '$\\dfrac{1}{2}$',
            '$\\dfrac{1}{3}$'
        ]
        s = []
        for c in candidates:
            cs = c if c.startswith('$') else '$%s$' % c
            if cs != da and cs not in s:
                s.append(cs)
                
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = (
            'Gieo một con xúc xắc $6$ mặt cân đối và đồng chất một lần (như hình vẽ). Xác suất của biến cố ``Mặt xuất hiện có số chấm bằng $%s$" là\n%s'
            % (mat_chon, hinh_ve)
        )
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = (
            'Gieo một con xúc xắc cân đối và đồng chất có $6$ kết quả có thể là: $1$ chấm; $2$ chấm; $3$ chấm; $4$ chấm; $5$ chấm; $6$ chấm. Các kết quả này là đồng khả năng.\\\\ '
            'Chỉ có $1$ kết quả thuận lợi cho biến cố ``Mặt xuất hiện có số chấm bằng $%s$" là mặt $%s$ chấm.\\\\ '
            'Vậy xác suất của biến cố đó là $\\dfrac{1}{6}$.'
            % (mat_chon, mat_chon)
        )
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
