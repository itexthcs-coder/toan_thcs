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

def bt_dang18_p1_b2_c8_ds8(self):
    # Dạng 18: Tình huống giao thông - đèn tín hiệu hoạt động theo chu kì (có hình vẽ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        t_xanh = random.choice([25, 30, 35, 40])
        t_vang = random.choice([3, 4, 5])
        t_do = random.choice([15, 20, 25])
        chu_ki = t_xanh + t_vang + t_do
        
        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (0.8,2.2);\n"
            "\\draw[line width=1pt] (0.4,0) -- (0.4,-0.8);\n"
            "\\draw[line width=1pt] (0.1,-0.8) -- (0.7,-0.8);\n"
            "\\draw[line width=1pt] (0.4,1.8) circle (0.22cm);\n"
            "\\draw[line width=1pt] (0.4,1.1) circle (0.22cm);\n"
            "\\fill (0.4,0.4) circle (0.22cm);\n"
            "\\node[right] at (0.85,1.8) {Đỏ: $%s$s};\n"
            "\\node[right] at (0.85,1.1) {Vàng: $%s$s};\n"
            "\\node[right] at (0.85,0.4) {Xanh: $%s$s};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
            % (t_do, t_vang, t_xanh)
        )
        
        da = '$%s$' % fmt_frac(t_xanh, chu_ki)
        
        candidates = [
            fmt_frac(t_do, chu_ki),
            fmt_frac(t_vang, chu_ki),
            fmt_frac(t_xanh + t_vang, chu_ki),
            fmt_frac(1, 3),
            fmt_frac(1, 2)
        ]
        s = []
        for c in candidates:
            cs = '$%s$' % c
            if cs != da and cs not in s:
                s.append(cs)
                
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = (
            'Một cột đèn giao thông tại ngã tư hoạt động theo chu kì $%s$ giây, trong đó đèn xanh sáng $%s$ giây, đèn vàng sáng $%s$ giây và đèn đỏ sáng $%s$ giây (như hình vẽ). Một người đi xe máy tới ngã tư một cách ngẫu nhiên. Xác suất để người đó gặp đèn xanh là\n%s'
            % (chu_ki, t_xanh, t_vang, t_do, hinh_ve)
        )
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = (
            'Mỗi chu kì đèn giao thông kéo dài $%s$ giây (ứng với $%s$ khoảng thời gian $1$ giây đồng khả năng).\\\\ '
            'Đèn xanh sáng trong $%s$ giây nên số kết quả thuận lợi cho biến cố ``Người đó gặp đèn xanh" là $%s$.\\\\ '
            'Vậy xác suất để người đó gặp đèn xanh là $\\dfrac{%s}{%s} = %s$.'
            % (chu_ki, chu_ki, t_xanh, t_xanh, t_xanh, chu_ki, fmt_frac(t_xanh, chu_ki))
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
