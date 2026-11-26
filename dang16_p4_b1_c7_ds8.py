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

def bt_dang16_p4_b1_c7_ds8(self):
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
    # Bài 16: Ứng dụng trong Vật lí – Chuyển động đường bộ có thay đổi vận tốc giữa chặng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t_du_dinh = random.choice([4, 6])
        giam_v = random.choice([10, 12, 15])
        muon_phut = random.choice([30, 45])
        t_muon = Fraction(muon_phut, 60)
        # Nửa đầu đi mất t_du_dinh/2 giờ; nửa sau đi chậm hơn thời gian dự định t_muon giờ
        # => (S/2)/(v - giam_v) - (S/2)/v = t_muon, với S = t_du_dinh * v
        # (t_du_dinh/2)*v / (v - giam_v) - t_du_dinh/2 = t_muon
        # (t_du_dinh/2) * giam_v / (v - giam_v) = t_muon
        # Chọn số sao cho v nguyên đẹp
        cfg = random.choice([
            (4, 10, 30, 50, 200),
            (4, 15, 30, 75, 300),
            (6, 10, 45, 50, 300),
            (4, 12, 30, 60, 240)
        ])
        t_du_dinh, giam_v, muon_phut, v_dd, quang_duong = cfg
        t_muon = Fraction(muon_phut, 60)
        t_nua = t_du_dinh // 2

        tikz_fig = ('\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                    '\\coordinate (A) at (0,0);\n'
                    '\\coordinate (M) at (3,0);\n'
                    '\\coordinate (B) at (6,0);\n'
                    '\\draw[line width=1pt] (A)--(B);\n'
                    '\\draw[line width=1pt, ->] (0.5,0.3)--(2.5,0.3) node[midway, above] {$v$};\n'
                    '\\draw[line width=1pt, ->] (3.5,0.3)--(5.5,0.3) node[midway, above] {$v - %s$};\n'
                    '\\fill (A) circle (1pt) node[below] {$A$};\n'
                    '\\fill (M) circle (1pt) node[below] {$M$};\n'
                    '\\fill (B) circle (1pt) node[below] {$B$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}' % giam_v)

        noidungcauhoi = ('''Một người đi xe máy từ địa điểm $A$ đến địa điểm $B$ dự định mất $%s$ giờ. Trong nửa đầu quãng đường $AB$, người đó đi với vận tốc dự định. Đến nửa sau quãng đường, do đường trơn nên người đó giảm vận tốc đi $%s\\text{ km/h}$ so với vận tốc dự định, vì vậy người đó đến $B$ muộn hơn dự định $%s$ phút. Tính độ dài quãng đường $AB$ và vận tốc dự định ban đầu của người đi xe máy.\\
    %s''' % (t_du_dinh, giam_v, muon_phut, tikz_fig))

        loigiai = ('''Đổi $%s$ phút $= %s$ giờ.\\
    Gọi $x\\text{ (km/h)}$ là vận tốc dự định ban đầu của người đi xe máy ($x > %s$).\\
    Độ dài quãng đường $AB$ theo dự định là $%sx\\text{ (km)}$, nên mỗi nửa quãng đường dài $%sx\\text{ (km)}$.\\
    Thời gian người đó đi nửa đầu quãng đường là $\\frac{%sx}{x} = %s$ (giờ).\\
    Vận tốc của người đó trên nửa sau quãng đường là $x - %s\\text{ (km/h)}$, nên thời gian đi nửa sau quãng đường là $\\frac{%sx}{x - %s}$ (giờ).\\
    Vì người đó đến $B$ muộn hơn dự định $%s$ giờ (tức là tổng thời gian thực tế là $%s + %s = %s$ giờ) nên ta có phương trình:\\
    $%s + \\frac{%sx}{x - %s} = %s$\\
    $\\frac{%sx}{x - %s} = %s$\\
    $%sx = %s(x - %s)$\\
    $%sx = %sx - %s$\\
    $%sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện).\\
    Vậy vận tốc dự định ban đầu là $%s\\text{ km/h}$ và độ dài quãng đường $AB$ là $%s \\cdot %s = %s\\text{ (km)}$.'''
                   % (muon_phut, fmt_num(t_muon), giam_v,
                      t_du_dinh, t_nua,
                      t_nua, t_nua,
                      giam_v, t_nua, giam_v,
                      fmt_num(t_muon), t_du_dinh, fmt_num(t_muon), fmt_num(t_du_dinh + t_muon),
                      t_nua, t_nua, giam_v, fmt_num(t_du_dinh + t_muon),
                      t_nua, giam_v, fmt_num(t_nua + t_muon),
                      t_nua, fmt_num(t_nua + t_muon), giam_v,
                      t_nua, fmt_num(t_nua + t_muon), fmt_num((t_nua + t_muon) * giam_v),
                      fmt_num(t_muon), fmt_num((t_nua + t_muon) * giam_v), v_dd,
                      v_dd, t_du_dinh, v_dd, quang_duong))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
