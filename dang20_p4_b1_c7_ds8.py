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

def bt_dang20_p4_b1_c7_ds8(self):
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
    # Bài 20: Ứng dụng trong Hình học thực tế – Khu vườn hình chữ nhật có lối đi bên trong
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Chu vi = 2*nua_cv, lối đi rộng d => mỗi chiều giảm 2d
        # Diện tích giảm = x*(nua_cv - x) - (x - 2d)*(nua_cv - x - 2d) = 2d*nua_cv - 4d^2 (không phụ thuộc x!)
        # Để bài toán lập được phương trình bậc nhất xác định duy nhất x, cho chiều dài gấp k lần chiều rộng hoặc hơn chiều rộng h mét:
        # Cụ thể: diện tích đất trồng hoa bằng tỉ số hoặc kém diện tích ban đầu một lượng gắn với x:
        # Đặt: chiều dài hơn chiều rộng h (m), sau khi làm lối đi rộng d (m) xung quanh bên trong thì diện tích trồng hoa là S_hoa (m^2)
        # x*(x + h) - (x - 2d)*(x + h - 2d) = S_giam  => 4d*x + 2d*h - 4d^2 = S_giam (phương trình bậc nhất ẩn x!)
        d = Fraction(3, 2)  # 1,5 m => 2d = 3 m
        h = random.choice([4, 6, 8, 10])
        rong = random.choice([12, 14, 16, 18, 20])
        dai = rong + h
        dt_goc = rong * dai
        dt_hoa = (rong - 3) * (dai - 3)
        dt_giam = dt_goc - dt_hoa

        tikz_fig = ('\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                    '\\coordinate (A) at (0,0);\n'
                    '\\coordinate (B) at (5,0);\n'
                    '\\coordinate (C) at (5,3);\n'
                    '\\coordinate (D) at (0,3);\n'
                    '\\coordinate (E) at (0.6,0.6);\n'
                    '\\coordinate (F) at (4.4,0.6);\n'
                    '\\coordinate (G) at (4.4,2.4);\n'
                    '\\coordinate (H) at (0.6,2.4);\n'
                    '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
                    '\\draw[line width=1pt, dashed] (E)--(F)--(G)--(H)--cycle;\n'
                    '\\fill (A) circle (1pt) node[below left] {$A$};\n'
                    '\\fill (B) circle (1pt) node[below right] {$B$};\n'
                    '\\fill (C) circle (1pt) node[above right] {$C$};\n'
                    '\\fill (D) circle (1pt) node[above left] {$D$};\n'
                    '\\node at (2.5,1.5) {Đất trồng hoa};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}')

        noidungcauhoi = ('''Một khu vườn hình chữ nhật $ABCD$ có chiều dài hơn chiều rộng $%s\\text{ m}$. Người ta làm một lối đi xung quanh bên trong khu vườn có bề rộng đều bằng $1,5\\text{ m}$ (như hình vẽ), phần đất còn lại ở giữa dùng để trồng hoa có diện tích nhỏ hơn diện tích toàn bộ khu vườn là $%s\\text{ m}^2$. Tính chiều dài và chiều rộng ban đầu của khu vườn.\\
    %s''' % (h, dt_giam, tikz_fig))

        loigiai = ('''Gọi $x\\text{ (m)}$ là chiều rộng ban đầu của khu vườn ($x > 3$).\\
    Chiều dài ban đầu của khu vườn là $x + %s\\text{ (m)}$ và diện tích toàn bộ khu vườn là $x(x + %s)\\text{ (m}^2)$.\\
    Vì lối đi xung quanh bên trong rộng $1,5\\text{ m}$ nên phần đất trồng hoa hình chữ nhật có chiều rộng là $x - 2 \\cdot 1,5 = x - 3\\text{ (m)}$ và chiều dài là $(x + %s) - 3 = x + %s\\text{ (m)}$.\\
    Diện tích phần đất trồng hoa là $(x - 3)(x + %s)\\text{ (m}^2)$.\\
    Theo đề bài, diện tích trồng hoa nhỏ hơn diện tích toàn bộ khu vườn là $%s\\text{ m}^2$ nên ta có phương trình:\\
    $x(x + %s) - (x - 3)(x + %s) = %s$\\
    $(x^2 + %sx) - (x^2 + %sx - %s) = %s$\\
    $x^2 + %sx - x^2 - %sx + %s = %s$\\
    $6x + %s = %s$\\
    $6x = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện).\\
    Vậy chiều rộng ban đầu của khu vườn là $%s\\text{ m}$ và chiều dài ban đầu là $%s + %s = %s\\text{ (m)}$.'''
                   % (h, h,
                      h, h - 3,
                      h - 3, dt_giam,
                      h, h - 3, dt_giam,
                      h, h - 6, 3 * (h - 3), dt_giam,
                      h, h - 6, 3 * (h - 3), dt_giam,
                      3 * (h - 3), dt_giam,
                      dt_giam - 3 * (h - 3), rong,
                      rong, rong, h, dai))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
