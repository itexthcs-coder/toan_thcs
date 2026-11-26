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

def bt_dang20_p3_b1_c7_ds8(self):
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

    def fmt_ans(val):
        f = Fraction(val).limit_denominator()
        if f.denominator == 1:
            s = str(f.numerator)
            assert -999 < f.numerator < 9999 and len(s) <= 4
            return s
        d = Decimal(f.numerator) / Decimal(f.denominator)
        # Thử làm tròn đến 1 hoặc 2 chữ số thập phân sao cho tối đa 4 ký tự
        for dec_fmt in ['0.1', '0.01']:
            q = d.quantize(Decimal(dec_fmt), rounding=ROUND_HALF_UP)
            s = format(q.normalize(), 'f')
            if '.' in s:
                s = s.rstrip('0').rstrip('.')
            s_comma = s.replace('.', ',')
            if len(s_comma) <= 4:
                return s_comma
        q = d.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_comma = str(q).replace('.', ',')
        return s_comma

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
    # Dạng 20: Ứng dụng trong Hình học thực tế – Mở rộng đáy mảnh đất hình thang vuông
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        day_nho = random.choice([10, 12, 14])
        day_lon = day_nho + random.choice([4, 6, 8])
        chieu_cao = random.choice([8, 10, 12])
        dt_goc = (day_nho + day_lon) * chieu_cao // 2
        x_them = random.choice([3, 4, 5, 6])
        dt_them = x_them * chieu_cao // 2
        kq_str = fmt_ans(x_them)

        tikz_fig = ('\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                    '\\coordinate (D) at (0,0);\n'
                    '\\coordinate (C) at (5,0);\n'
                    '\\coordinate (A) at (0,2.5);\n'
                    '\\coordinate (B) at (3.2,2.5);\n'
                    '\\coordinate (E) at (4.1,2.5);\n'
                    '\\draw[line width=1pt] (D)--(C)--(B)--(A)--cycle;\n'
                    '\\draw[line width=1pt, dashed] (B)--(E)--(C);\n'
                    '\\fill (A) circle (1pt) node[above left] {$A$};\n'
                    '\\fill (B) circle (1pt) node[above] {$B$};\n'
                    '\\fill (E) circle (1pt) node[above right] {$E$};\n'
                    '\\fill (C) circle (1pt) node[below right] {$C$};\n'
                    '\\fill (D) circle (1pt) node[below left] {$D$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}')

        noidungcauhoi = ('''Một mảnh đất hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) có đáy nhỏ $AB = %s\\text{ m}$, đáy lớn $CD = %s\\text{ m}$ và diện tích bằng $%s\\text{ m}^2$. Người ta muốn mở rộng đáy nhỏ $AB$ thêm một đoạn $BE = x\\text{ (m)}$ (giữ nguyên chiều cao $AD$ và đáy lớn $CD$) để diện tích mảnh đất tăng thêm $%s\\text{ m}^2$. Tìm giá trị của $x$.\\
    %s''' % (day_nho, day_lon, dt_goc, dt_them, tikz_fig))

        loigiai = ('''Chiều cao $AD$ của mảnh đất hình thang vuông $ABCD$ là:\\
    $AD = \\frac{2 \\cdot %s}{%s + %s} = \\frac{%s}{%s} = %s\\text{ (m)}$.\\
    Khi mở rộng đáy nhỏ $AB$ thêm $x\\text{ (m)}$, đáy nhỏ mới là $%s + x\\text{ (m)}$ và diện tích mới là $%s + %s = %s\\text{ (m}^2)$.\\
    Ta có phương trình:\\
    $\\frac{[(%s + x) + %s] \\cdot %s}{2} = %s$\\
    $(%s + x) \\cdot %s = %s$\\
    $%s + x = %s \\Leftrightarrow x = %s$.\\
    Vậy $x = %s$.'''
                   % (dt_goc, day_nho, day_lon, 2 * dt_goc, day_nho + day_lon, chieu_cao,
                      day_nho, dt_goc, dt_them, dt_goc + dt_them,
                      day_nho, day_lon, chieu_cao, dt_goc + dt_them,
                      day_nho + day_lon, chieu_cao // 2, dt_goc + dt_them,
                      day_nho + day_lon, (dt_goc + dt_them) // (chieu_cao // 2), kq_str, kq_str))

    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
