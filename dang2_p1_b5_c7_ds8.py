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


def bt_dang2_p1_b5_c7_ds8(self):
    def fmt_num(val):
        if isinstance(val, Fraction):
            if val.denominator == 1:
                return str(val.numerator)
            if val.numerator < 0:
                return '-\\dfrac{%s}{%s}' % (abs(val.numerator), val.denominator)
            return '\\dfrac{%s}{%s}' % (val.numerator, val.denominator)
        if isinstance(val, float):
            s_val = ('%g' % val).replace('.', ',')
            return s_val
        return str(val)

    def fmt_line(a_val, b_val):
        # Định dạng y = ax + b với a_val, b_val là int hoặc Fraction
        if isinstance(a_val, Fraction) and a_val.denominator != 1:
            if a_val.numerator < 0:
                str_a = '-\\dfrac{%s}{%s}x' % (abs(a_val.numerator), a_val.denominator)
            else:
                str_a = '\\dfrac{%s}{%s}x' % (a_val.numerator, a_val.denominator)
        else:
            ai = int(a_val)
            if ai == 1:
                str_a = 'x'
            elif ai == -1:
                str_a = '-x'
            else:
                str_a = '%sx' % ai

        if b_val == 0:
            return 'y = %s' % str_a
        if isinstance(b_val, Fraction) and b_val.denominator != 1:
            if b_val.numerator < 0:
                str_b = '- \\dfrac{%s}{%s}' % (abs(b_val.numerator), b_val.denominator)
            else:
                str_b = '+ \\dfrac{%s}{%s}' % (b_val.numerator, b_val.denominator)
        else:
            bi = int(b_val)
            if bi > 0:
                str_b = '+ %s' % bi
            else:
                str_b = '- %s' % abs(bi)
        return 'y = %s %s' % (str_a, str_b)

    # Dạng 2: Nhận diện hệ số góc khi thứ tự các hạng tử bị đảo ngược (y = b + ax)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tu = random.choice([i for i in range(-7, 8) if i != 0])
        mau = random.choice([2, 3, 4, 5])
        while math.gcd(abs(tu), mau) != 1:
            tu = random.choice([i for i in range(-7, 8) if i != 0])
        a_frac = Fraction(tu, mau)
        b = random.choice([i for i in range(-9, 10) if i != 0])
        if a_frac > 0:
            pt = 'y = %s + %sx' % (b, fmt_num(a_frac))
        else:
            pt = 'y = %s - %sx' % (b, fmt_num(abs(a_frac)))

        da = '$%s$' % fmt_num(a_frac)
        s_pool = [Fraction(b, 1), -a_frac, Fraction(-b, 1), Fraction(mau, tu) if tu != 0 else Fraction(1, 2)]
        s_unique = []
        for item in s_pool:
            if item != a_frac and item not in s_unique:
                s_unique.append(item)
        while len(s_unique) < 3:
            cand = a_frac + len(s_unique) + 1
            if cand != a_frac and cand not in s_unique:
                s_unique.append(cand)
        das1, das2, das3 = ['$%s$' % fmt_num(x) for x in s_unique[:3]]

        noidungcauhoi = ('Đường thẳng $%s$ có hệ số góc bằng bao nhiêu?' % pt)
        da_d = ('\\True ' + str(da))
        list_1 = [da_d, das1, das2, das3]
        random.shuffle(list_1)

        pt_chuan = fmt_line(a_frac, b)
        loigiai = ('Ta viết lại phương trình đường thẳng dưới dạng $y = ax + b$: $%s$.\\\\'
                   'Khi đó hệ số của $x$ là $a = %s$.\\\\'
                   'Vậy hệ số góc của đường thẳng đã cho bằng $%s$.' % (pt_chuan, fmt_num(a_frac), fmt_num(a_frac)))

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
