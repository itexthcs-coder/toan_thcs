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

def fmt_so(val):
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val < 0:
            return '-\\frac{%s}{%s}' % (abs(val.numerator), val.denominator)
        return '\\frac{%s}{%s}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        s = ('%g' % val).replace('.', ',')
        return s
    return str(val)

def fmt_dt(a, b):
    if a == 1:
        sa = 'x'
    elif a == -1:
        sa = '-x'
    else:
        sa = '%sx' % fmt_so(a)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_so(b))
    else:
        return '%s - %s' % (sa, fmt_so(abs(b)))

def bt_dang6_p4_b5_c7_ds8(self):
    # Dạng 6: Tìm hai tham số m, n để hai đường thẳng song song, trùng nhau, cắt nhau trên trục tung
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # (2m + 3)x - n + 1 và (c - m)x + 2n - d
        # 2m + 3 = c - m => 3m = c - 3
        m_val = random.choice([1, 2, -1])
        c = 3 * m_val + 3
        # -n + 1 = 2n - d => 3n = d + 1
        n_val = random.choice([2, 3, 4])
        d = 3 * n_val - 1
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1.5) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1.2,-1) -- (2.5,2.7) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-1.2,2.8) -- (2.5,-0.9) node[right] {$(d_2)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,1.2) circle (1pt) node[above right] {$K$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hai hàm số bậc nhất $y = (2m + 3)x - n + 1$ và $y = (%s - m)x + 2n - %s$ (với $m \\neq -\\frac{3}{2}$ và $m \\neq %s$). Tìm các giá trị của $m$ và $n$ để đồ thị của hai hàm số trên:\\\n'
            'a) Song song với nhau.\\\n'
            'b) Trùng nhau.\\\n'
            'c) Cắt nhau tại một điểm nằm trên trục tung.'
            % (c, d, c)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Đồ thị của hai hàm số đã cho song song với nhau khi và chỉ khi:\\\n'
            '$\\begin{cases} 2m + 3 = %s - m \\\\ -n + 1 \\neq 2n - %s \\end{cases} \\Leftrightarrow \\begin{cases} 3m = %s \\\\ 3n \\neq %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\\\ n \\neq %s \\end{cases}$ (thỏa mãn điều kiện $m \\neq -\\frac{3}{2}$ và $m \\neq %s$).\n'
            '\\item Đồ thị của hai hàm số đã cho trùng nhau khi và chỉ khi:\\\n'
            '$\\begin{cases} 2m + 3 = %s - m \\\\ -n + 1 = 2n - %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\\\ n = %s \\end{cases}$ (thỏa mãn điều kiện).\n'
            '\\item Hai đường thẳng cắt nhau tại một điểm nằm trên trục tung khi và chỉ khi hệ số góc của chúng khác nhau và tung độ gốc của chúng bằng nhau:\\\n'
            '$\\begin{cases} 2m + 3 \\neq %s - m \\\\ -n + 1 = 2n - %s \\end{cases} \\Leftrightarrow \\begin{cases} m \\neq %s \\\\ n = %s \\end{cases}$ (kết hợp điều kiện $m \\neq -\\frac{3}{2}$ và $m \\neq %s$).%s\n'
            '\\end{enumEX}'
            % (c, d, c - 3, d + 1, m_val, n_val, c,
               c, d, m_val, n_val,
               c, d, m_val, n_val, c, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
