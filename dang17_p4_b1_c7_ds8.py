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

def bt_dang17_p4_b1_c7_ds8(self):
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
    # Bài 17: Ứng dụng trong Tài chính – Chia vốn đầu tư vào hai kênh sinh lời khác nhau
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cfg = random.choice([
            (400, Fraction(6, 100), Fraction(85, 1000), 29, 200, 200),
            (500, Fraction(6, 100), Fraction(8, 100), 36, 200, 300),
            (600, Fraction(5, 100), Fraction(75, 1000), 40, 200, 400),
            (300, Fraction(5, 100), Fraction(8, 100), 21, 100, 200)
        ])
        tong_von, r1, r2, tong_lai, von1, von2 = cfg
        r1_pt = fmt_dec(r1 * 100)
        r2_pt = fmt_dec(r2 * 100)

        noidungcauhoi = ('''Bác Hùng có tổng cộng $%s$ triệu đồng và chia thành hai khoản để đầu tư trong $1$ năm:\\
    - Khoản thứ nhất gửi tiết kiệm ngân hàng với lãi suất $%s\\%%$/năm.\\
    - Khoản thứ hai đầu tư vào trái phiếu doanh nghiệp với lãi suất $%s\\%%$/năm.\\
    Sau đúng $1$ năm, tổng số tiền lãi bác Hùng thu được từ cả hai khoản đầu tư là $%s$ triệu đồng. Hỏi bác Hùng đã đầu tư bao nhiêu triệu đồng vào mỗi khoản?'''
                         % (tong_von, r1_pt, r2_pt, tong_lai))

        loigiai = ('''Gọi $x$ (triệu đồng) là số tiền bác Hùng gửi tiết kiệm ngân hàng ở khoản thứ nhất ($0 < x < %s$).\\
    Số tiền bác Hùng đầu tư vào trái phiếu doanh nghiệp ở khoản thứ hai là $%s - x$ (triệu đồng).\\
    Sau $1$ năm, tiền lãi thu được từ khoản thứ nhất là $%sx$ (triệu đồng) và tiền lãi thu được từ khoản thứ hai là $%s(%s - x)$ (triệu đồng).\\
    Vì tổng số tiền lãi thu được là $%s$ triệu đồng nên ta có phương trình:\\
    $%sx + %s(%s - x) = %s$\\
    $%sx + %s - %sx = %s$\\
    $-%sx = %s - %s$\\
    $-%sx = -%s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện).\\
    Vậy bác Hùng đã đầu tư $%s$ triệu đồng vào tiết kiệm ngân hàng và $%s - %s = %s$ triệu đồng vào trái phiếu doanh nghiệp.'''
                   % (tong_von, tong_von,
                      fmt_dec(r1), fmt_dec(r2), tong_von,
                      tong_lai,
                      fmt_dec(r1), fmt_dec(r2), tong_von, tong_lai,
                      fmt_dec(r1), fmt_dec(r2 * tong_von), fmt_dec(r2), tong_lai,
                      fmt_dec(r2 - r1), tong_lai, fmt_dec(r2 * tong_von),
                      fmt_dec(r2 - r1), fmt_dec(r2 * tong_von - tong_lai), von1,
                      von1, tong_von, von1, von2))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
