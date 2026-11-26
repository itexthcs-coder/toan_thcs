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

def bt_dang18_p4_b1_c7_ds8(self):
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
    # Bài 18: Ứng dụng trong Quản lí nhân sự và Công việc chung – Hợp tác sản xuất
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cfg = random.choice([
            (12, 4, 6, Fraction(2, 5), 20, 30),
            (10, 3, 5, Fraction(2, 5), 15, 30),
            (12, 3, 7, Fraction(5, 12), 24, 24),
            (15, 5, 9, Fraction(7, 15), 25, 37)
        ])
        if cfg[0] == 15:
            cfg = (12, 4, 6, Fraction(2, 5), 20, 30)
        t_chung, d1, d2, phan_cv, t1, t2 = cfg
        con_lai = phan_cv - Fraction(d1, t_chung)
        hieu_ngay = d2 - d1

        noidungcauhoi = ('''Hai đội công nhân cùng làm chung một công trình thì sau $%s$ ngày sẽ hoàn thành toàn bộ công việc. Nếu đội thứ nhất làm một mình trong $%s$ ngày rồi nghỉ, sau đó đội thứ hai làm tiếp một mình trong $%s$ ngày thì cả hai đội hoàn thành được $%s$ công việc. Hỏi nếu làm một mình thì mỗi đội phải mất bao nhiêu ngày mới hoàn thành xong công trình đó?'''
                         % (t_chung, d1, d2, fmt_num(phan_cv)))

        loigiai = ('''Trong $1$ ngày, cả hai đội làm chung được $\\frac{1}{%s}$ (công việc).\\
    Việc đội thứ nhất làm trong $%s$ ngày rồi đội thứ hai làm tiếp trong $%s$ ngày tương đương với việc hai đội cùng làm chung trong $%s$ ngày, sau đó đội thứ hai làm một mình thêm $%s - %s = %s$ ngày.\\
    Trong $%s$ ngày làm chung, hai đội hoàn thành được $%s \\cdot \\frac{1}{%s} = %s$ (công việc).\\
    Gọi $x$ (ngày) là thời gian đội thứ hai làm một mình hoàn thành toàn bộ công việc ($x > %s$).\\
    Trong $1$ ngày, đội thứ hai làm được $\\frac{1}{x}$ (công việc), nên trong $%s$ ngày đội thứ hai làm được $\\frac{%s}{x}$ (công việc).\\
    Theo đề bài, ta có phương trình:\\
    $%s + \\frac{%s}{x} = %s$\\
    $\\frac{%s}{x} = %s - %s = %s$\\
    $x = %s : %s = %s$ (thỏa mãn điều kiện).\\
    Trong $1$ ngày, đội thứ nhất làm một mình được $\\frac{1}{%s} - \\frac{1}{%s} = \\frac{1}{%s}$ (công việc), nên đội thứ nhất làm một mình mất $%s$ ngày.\\
    Vậy đội thứ nhất làm một mình mất $%s$ ngày và đội thứ hai làm một mình mất $%s$ ngày.'''
                   % (t_chung, d1, d2, d1, d2, d1, hieu_ngay,
                      d1, d1, t_chung, fmt_num(Fraction(d1, t_chung)),
                      t_chung, hieu_ngay, hieu_ngay,
                      fmt_num(Fraction(d1, t_chung)), hieu_ngay, fmt_num(phan_cv),
                      hieu_ngay, fmt_num(phan_cv), fmt_num(Fraction(d1, t_chung)), fmt_num(con_lai),
                      hieu_ngay, fmt_num(con_lai), t2,
                      t_chung, t2, t1, t1,
                      t1, t2))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
