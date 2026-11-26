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

def bt_dang6_p1_b1_c7_ds8(self):
    def fmt_num(val):
        f = Fraction(val).limit_denominator()
        if f.denominator == 1:
            return str(f.numerator)
        if f.numerator < 0:
            return '-\\frac{%s}{%s}' % (abs(f.numerator), f.denominator)
        return '\\frac{%s}{%s}' % (f.numerator, f.denominator)

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

    def pick_distractors(correct_str, candidates, fallback_gen):
        pool = []
        for item in candidates:
            if item != correct_str and item not in pool:
                pool.append(item)
        k = 1
        while len(pool) < 3:
            cand = fallback_gen(k)
            k += 1
            if cand != correct_str and cand not in pool:
                pool.append(cand)
        d1 = random.choice(pool); pool.remove(d1)
        d2 = random.choice(pool); pool.remove(d2)
        d3 = random.choice(pool)
        return d1, d2, d3
    # Dạng 6: Nhận biết phương trình không nhận giá trị cho trước làm nghiệm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([-3, -2, -1, 1, 2, 3])
        a1 = random.choice([2, 3, 4])
        pt_d1 = '%s = 0' % fmt_lin(a1, -a1 * x0)

        a2 = random.choice([2, 3, 4])
        c2 = random.choice([1, 2, 3])
        d2 = (a2 + 1) * x0 + c2
        pt_d2 = '%s = %s' % (fmt_lin(a2, c2), '%s - x' % d2)

        a3 = random.choice([2, 3, 5])
        pt_d3 = '%s = %s' % (fmt_lin(-2, (a3 + 2) * x0), fmt_term_x(a3, True))

        a4 = random.choice([2, 3, 4])
        b4 = random.choice([1, 2, 3])
        vp4 = a4 * x0 + b4 + random.choice([2, 3, 4])
        pt_sai = '%s = %s' % (fmt_lin(a4, b4), vp4)

        du = ['$%s$' % pt_sai]
        da = random.choice(du)
        s = ['$%s$' % pt_d1, '$%s$' % pt_d2, '$%s$' % pt_d3]
        das1 = random.choice(s); s.remove(das1)
        das2 = random.choice(s); s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Số $x = %s$ \\textbf{không} phải là nghiệm của phương trình nào sau đây?''' % x0)
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        vt_val = a4 * x0 + b4
        loigiai = ('''Thay $x = %s$ vào hai vế của phương trình $%s$, ta có:\\
    Vế trái: $%s \\cdot %s %s = %s$.\\
    Vế phải: $%s$.\\
    Vì $%s \\neq %s$ nên giá trị của hai vế không bằng nhau tại $x = %s$.\\
    Do đó, $x = %s$ không phải là nghiệm của phương trình $%s$.'''
                   % (x0, pt_sai, a4, fmt_paren(x0), fmt_const(b4, False), vt_val, vp4, vt_val, vp4, x0, x0, pt_sai))

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
