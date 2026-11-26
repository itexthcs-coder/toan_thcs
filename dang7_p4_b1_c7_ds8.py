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

def bt_dang7_p4_b1_c7_ds8(self):
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
    # Bài 7: Giải phương trình bậc nhất bằng phương pháp tách hạng tử cộng thêm hằng số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m_base = random.choice([2007, 2010, 2015, 2020])
        x0 = random.choice([-2026, -2025, -2024, -2027])
        # (x + a1)/m_base + (x + a2)/(m_base+1) = (x + a3)/(m_base+2) + (x + a4)/(m_base+3)
        # Cộng 1 vào mỗi phân thức => (x - x0)/m_i = 0 => a_i + m_i = -x0 => a_i = -x0 - m_i
        a1 = -x0 - m_base
        a2 = -x0 - (m_base + 1)
        a3 = -x0 - (m_base + 2)
        a4 = -x0 - (m_base + 3)
        abs_x0 = abs(x0)

        pt_str = '\\frac{x + %s}{%s} + \\frac{x + %s}{%s} = \\frac{x + %s}{%s} + \\frac{x + %s}{%s}' % (
            a1, m_base, a2, m_base + 1, a3, m_base + 2, a4, m_base + 3
        )
        noidungcauhoi = ('''Giải phương trình sau:\\
    $%s$.''' % pt_str)

        loigiai = ('''Cộng mỗi phân thức ở cả hai vế của phương trình với $1$, ta được:\\
    $\\left(\\frac{x + %s}{%s} + 1\\right) + \\left(\\frac{x + %s}{%s} + 1\\right) = \\left(\\frac{x + %s}{%s} + 1\\right) + \\left(\\frac{x + %s}{%s} + 1\\right)$\\
    $\\frac{x + %s}{%s} + \\frac{x + %s}{%s} - \\frac{x + %s}{%s} - \\frac{x + %s}{%s} = 0$\\
    $(x + %s)\\left(\\frac{1}{%s} + \\frac{1}{%s} - \\frac{1}{%s} - \\frac{1}{%s}\\right) = 0$.\\
    Vì $\\frac{1}{%s} > \\frac{1}{%s}$ và $\\frac{1}{%s} > \\frac{1}{%s}$ nên $\\frac{1}{%s} + \\frac{1}{%s} - \\frac{1}{%s} - \\frac{1}{%s} > 0$.\\
    Do đó $x + %s = 0 \\Leftrightarrow x = %s$.\\
    Vậy tập nghiệm của phương trình là $S = \\{%s\\}$.'''
                   % (a1, m_base, a2, m_base + 1, a3, m_base + 2, a4, m_base + 3,
                      abs_x0, m_base, abs_x0, m_base + 1, abs_x0, m_base + 2, abs_x0, m_base + 3,
                      abs_x0, m_base, m_base + 1, m_base + 2, m_base + 3,
                      m_base, m_base + 2, m_base + 1, m_base + 3,
                      m_base, m_base + 1, m_base + 2, m_base + 3,
                      abs_x0, x0, x0))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
