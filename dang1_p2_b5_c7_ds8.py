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


def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def fmt_num(val):
    if isinstance(val, int):
        return str(val)
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val.numerator < 0:
            return '-\\frac{%d}{%d}' % (-val.numerator, val.denominator)
        return '\\frac{%d}{%d}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val)

def fmt_line(a, b, var='x'):
    if a == 1:
        sa = var
    elif a == -1:
        sa = '-' + var
    else:
        sa = '%s%s' % (fmt_num(a), var)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_num(b))
    else:
        return '%s - %s' % (sa, fmt_num(-b))

def bt_dang1_p2_b5_c7_ds8(self):
    # Dạng 1: Biến đổi dạng hàm số và xác định hệ số góc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            a_coef = random.choice([i for i in range(-8, 9) if i != 0])
            b_coef = random.choice([i for i in range(-8, 9) if i not in [0, 1, -1]])
            c_coef = random.choice([i for i in range(-15, 16) if i != 0])
            if math.gcd(abs(a_coef), abs(b_coef)) == 1 and math.gcd(abs(c_coef), abs(b_coef)) == 1:
                break

        slope = Fraction(-a_coef, b_coef)
        intercept = Fraction(c_coef, b_coef)
        str_rhs = fmt_line(slope, intercept)

        sign_b = '+' if b_coef > 0 else '-'
        sign_c = '+' if -c_coef > 0 else '-'
        str_ax = 'x' if a_coef == 1 else ('-x' if a_coef == -1 else '%dx' % a_coef)
        pt_tq = '%s %s %dy %s %d = 0' % (str_ax, sign_b, abs(b_coef), sign_c, abs(c_coef))

        # Mệnh đề 1 (Thông hiểu)
        nb_da_1_d = '\\True Đường thẳng $(d)$ là đồ thị của hàm số bậc nhất $y = %s$' % str_rhs
        nb_da_1_s = 'Đường thẳng $(d)$ là đồ thị của hàm số bậc nhất $y = %s$' % fmt_line(-slope, intercept)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $%s \\Leftrightarrow %dy = %s \\Leftrightarrow y = %s$. \\
Vậy đường thẳng $(d)$ là đồ thị của hàm số bậc nhất $y = %s$.'''
                        % (pt_tq, b_coef, fmt_line(-a_coef, c_coef), str_rhs, str_rhs))

        # Mệnh đề 2 (Thông hiểu)
        th_da_1_d = '\\True Hệ số góc của đường thẳng $(d)$ bằng $%s$' % fmt_num(slope)
        th_da_1_s = 'Hệ số góc của đường thẳng $(d)$ bằng $%d$' % a_coef
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Từ phương trình $y = %s$, hệ số góc của đường thẳng $(d)$ là $a = %s$.'''
                        % (str_rhs, fmt_num(slope)))

        # Mệnh đề 3 (Thông hiểu)
        if slope > 0:
            vd_da_1_d = '\\True Góc tạo bởi đường thẳng $(d)$ và tia $Ox$ là góc nhọn'
            vd_da_1_s = 'Góc tạo bởi đường thẳng $(d)$ và tia $Ox$ là góc tù'
            loigiai_vd_1 = ('''Vì hệ số góc $a = %s > 0$ nên góc tạo bởi đường thẳng $(d)$ và tia $Ox$ là góc nhọn.''' % fmt_num(slope))
            tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.5,0);
\\coordinate (T) at (1.5,3);
\\draw[line width=1pt, ->] (-3,0)--(3.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-1.5)--(0,4) node[left] {$y$};
\\draw[line width=1pt] (-2.2,-0.7)--(2.2,3.7) node[right] {$y=ax+b$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (T) circle (1pt) node[left] {$T$};
\\end{tikzpicture}
\\end{center}'''
        else:
            vd_da_1_d = '\\True Góc tạo bởi đường thẳng $(d)$ và tia $Ox$ là góc tù'
            vd_da_1_s = 'Góc tạo bởi đường thẳng $(d)$ và tia $Ox$ là góc nhọn'
            loigiai_vd_1 = ('''Vì hệ số góc $a = %s < 0$ nên góc tạo bởi đường thẳng $(d)$ và tia $Ox$ là góc tù.''' % fmt_num(slope))
            tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (2,0);
\\coordinate (T) at (0.5,2.25);
\\draw[line width=1pt, ->] (-2,0)--(4,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-1.5)--(0,3.8) node[left] {$y$};
\\draw[line width=1pt] (-0.5,3.75)--(3,-1.5) node[right] {$y=ax+b$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (T) circle (1pt) node[right] {$T$};
\\end{tikzpicture}
\\end{center}'''
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        # Mệnh đề 4 (Vận dụng)
        if slope > 0:
            vdc_da_1_d = '\\True Đường thẳng $(d)$ đi lên từ trái sang phải trên mặt phẳng tọa độ $Oxy$'
            vdc_da_1_s = 'Đường thẳng $(d)$ đi xuống từ trái sang phải trên mặt phẳng tọa độ $Oxy$'
            loigiai_vdc_1 = ('''Do hệ số góc $a = %s > 0$ nên đồ thị hàm số $y = %s$ đi lên từ trái sang phải trên mặt phẳng tọa độ $Oxy$.'''
                             % (fmt_num(slope), str_rhs))
        else:
            vdc_da_1_d = '\\True Đường thẳng $(d)$ đi xuống từ trái sang phải trên mặt phẳng tọa độ $Oxy$'
            vdc_da_1_s = 'Đường thẳng $(d)$ đi lên từ trái sang phải trên mặt phẳng tọa độ $Oxy$'
            loigiai_vdc_1 = ('''Do hệ số góc $a = %s < 0$ nên đồ thị hàm số $y = %s$ đi xuống từ trái sang phải trên mặt phẳng tọa độ $Oxy$.'''
                             % (fmt_num(slope), str_rhs))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        noidungcauhoi = ('''Cho đường thẳng $(d)$ có phương trình $%s$. \\ %s''' % (pt_tq, tikz_fig))

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
                break

        list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
        list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
        list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
        list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

        combined_nb = list(zip(list_nb_1, list_nb_2))
        combined_th = list(zip(list_th_1, list_th_2))
        combined_vd = list(zip(list_vd_1, list_vd_2))
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))

        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

        content = ('\\begin{minipage}{\\textwidth} \n'
                   '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                   '\\choiceTFn \n'
                   '{' + str(shuffled_answers_nb[0]) + '}\n'
                   '{' + str(shuffled_answers_th[0]) + '}\n'
                   '{' + str(shuffled_answers_vd[0]) + '}\n'
                   '{' + str(shuffled_answers_vdc[0]) + '}\n'
                   '\\loigiai{ \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                   '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                   '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                   '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                   '\\end{enumEX}} \n'
                   '\\end{ex}\n \\end{minipage}\n\n')
        return content
