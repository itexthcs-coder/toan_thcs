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

def bt_dang15_p4_b1_c7_ds8(self):
    def fmt_num(val):
        f = Fraction(val).limit_denominator()
        if f.denominator == 1:
            return str(f.numerator)
        if f.numerator < 0:
            return '-\\frac{%s}{%s}' % (abs(f.numerator), f.denominator)
        return '\\frac{%s}{%s}' % (f.numerator, f.denominator)

    def fmt_dec(val):
        f = Fraction(val).limit_denominator()
        if f.denominator == 1:
            return str(f.numerator)
        d = Decimal(f.numerator) / Decimal(f.denominator)
        s = format(d.normalize(), 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    def fmt_paren(val):
        f = Fraction(val).limit_denominator()
        s = fmt_num(f)
        if f < 0:
            return '(%s)' % s
        return s

    def fmt_term_x(coef, is_first=True):
        f = Fraction(coef).limit_denominator()
        if f == 0:
            return ''
        if f < 0:
            sign = '-' if is_first else '- '
        else:
            sign = '' if is_first else '+ '
        abs_f = abs(f)
        if abs_f == 1:
            mag = 'x'
        elif abs_f.denominator == 1:
            mag = '%sx' % abs_f.numerator
        else:
            mag = '\\frac{%s}{%s}x' % (abs_f.numerator, abs_f.denominator)
        return sign + mag

    def fmt_const(val, is_first=False):
        f = Fraction(val).limit_denominator()
        if f == 0:
            return '' if not is_first else '0'
        if f < 0:
            sign = '-' if is_first else '- '
        else:
            sign = '' if is_first else '+ '
        abs_f = abs(f)
        if abs_f.denominator == 1:
            mag = str(abs_f.numerator)
        else:
            mag = '\\frac{%s}{%s}' % (abs_f.numerator, abs_f.denominator)
        return sign + mag

    def fmt_lin(a, b):
        fa = Fraction(a).limit_denominator()
        fb = Fraction(b).limit_denominator()
        if fa == 0:
            return fmt_const(fb, is_first=True)
        part_a = fmt_term_x(fa, is_first=True)
        part_b = fmt_const(fb, is_first=False)
        if part_b == '':
            return part_a
        return '%s %s' % (part_a, part_b)
    # Bài 15: Lập phương trình bậc nhất từ điều kiện giá trị biểu thức đại số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # A = (5x - a)/4 - (x + b)/3 ; B = (2x - c)/6 + d/2
        # MTC = 12: 12A = 3(5x - a) - 4(x + b) = 11x - 3a - 4b
        #           12B = 2(2x - c) + 6d = 4x - 2c + 6d
        a = random.choice([1, 3, 5])
        b = random.choice([1, 2, 4])
        c = random.choice([1, 3, 5])
        d = random.choice([1, 3, 5])
        k = random.choice([1, 2, 3])

        const_a = -3 * a - 4 * b
        const_b = -2 * c + 6 * d
        # a) A = B => 11x + const_a = 4x + const_b => 7x = const_b - const_a
        xa = Fraction(const_b - const_a, 7)
        # b) A - B = k => 11x + const_a - (4x + const_b) = 12k => 7x = 12k + const_b - const_a
        xb = Fraction(12 * k + const_b - const_a, 7)

        noidungcauhoi = ('''Cho hai biểu thức $A = \\frac{5x - %s}{4} - \\frac{x + %s}{3}$ và $B = \\frac{2x - %s}{6} + \\frac{%s}{2}$.\\
    a) Tìm giá trị của $x$ để hai biểu thức $A$ và $B$ có giá trị bằng nhau.\\
    b) Tìm giá trị của $x$ để giá trị của biểu thức $A$ lớn hơn giá trị của biểu thức $B$ là $%s$ đơn vị.'''
                         % (a, b, c, d, k))

        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Để hai biểu thức $A$ và $B$ có giá trị bằng nhau thì $A = B$, tức là:\\
    $\\frac{5x - %s}{4} - \\frac{x + %s}{3} = \\frac{2x - %s}{6} + \\frac{%s}{2}$.\\
    Quy đồng mẫu hai vế với mẫu thức chung bằng $12$ rồi khử mẫu, ta được:\\
    $3(5x - %s) - 4(x + %s) = 2(2x - %s) + 6 \\cdot %s$\\
    $15x - %s - 4x - %s = 4x - %s + %s$\\
    $11x %s = 4x %s$\\
    $7x = %s \\Leftrightarrow x = %s$.\\
    Vậy $x = %s$.
    \\item Để giá trị của $A$ lớn hơn giá trị của $B$ là $%s$ đơn vị thì $A - B = %s$, tức là:\\
    $\\frac{5x - %s}{4} - \\frac{x + %s}{3} - \\left(\\frac{2x - %s}{6} + \\frac{%s}{2}\\right) = %s$.\\
    Nhân cả hai vế với $12$ để khử mẫu, ta được:\\
    $3(5x - %s) - 4(x + %s) - 2(2x - %s) - 6 \\cdot %s = %s$\\
    $(11x %s) - (4x %s) = %s$\\
    $7x %s = %s \\Leftrightarrow 7x = %s \\Leftrightarrow x = %s$.\\
    Vậy $x = %s$.
    \\end{enumEX}'''
                   % (a, b, c, d,
                      a, b, c, d,
                      3 * a, 4 * b, 2 * c, 6 * d,
                      fmt_const(const_a, False), fmt_const(const_b, False),
                      const_b - const_a, fmt_num(xa), fmt_num(xa),
                      k, k,
                      a, b, c, d, k,
                      a, b, c, d, 12 * k,
                      fmt_const(const_a, False), fmt_const(const_b, False), 12 * k,
                      fmt_const(const_a - const_b, False), 12 * k, 12 * k + const_b - const_a, fmt_num(xb), fmt_num(xb)))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
