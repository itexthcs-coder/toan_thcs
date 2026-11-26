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

def bt_dang3_p2_b1_c7_ds8(self):
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

    def fmt_money(n):
        return '{:,}'.format(int(n)).replace(',', '\\,')

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

    def fmt_lin_var(a, b, var='m'):
        fa = Fraction(a).limit_denominator()
        fb = Fraction(b).limit_denominator()
        if fa == 0:
            return fmt_const(fb, is_first=True)
        if fa < 0:
            sign = '-'
        else:
            sign = ''
        abs_f = abs(fa)
        if abs_f == 1:
            part_a = sign + var
        else:
            part_a = '%s%s%s' % (sign, abs_f.numerator, var)
        part_b = fmt_const(fb, is_first=False)
        if part_b == '':
            return part_a
        return '%s %s' % (part_a, part_b)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    # Dạng 3: Đánh giá các bước biến đổi sử dụng quy tắc chuyển vế và quy tắc nhân
    a1 = random.choice([4, 5, 6])
    a2 = random.choice([2, 3])
    x0 = random.choice([3, 4, 5, 6, 7])
    b1 = random.choice([-9, -7, -5, -3])
    b2 = (a1 - a2) * x0 + b1
    pt_goc = '%s = %s' % (fmt_lin(a1, b1), fmt_lin(a2, b2))

    noidungcauhoi = ('''Cho phương trình $%s$. Xét tính đúng, sai của các khẳng định sau:''' % pt_goc)

    # a
    nb_da_1_d = '\\True Chuyển hạng tử $%sx$ từ vế phải sang vế trái và $%s$ từ vế trái sang vế phải, ta được $%sx - %sx = %s + %s$' % (a2, b1, a1, a2, b2, abs(b1))
    nb_da_1_s = 'Chuyển hạng tử $%sx$ từ vế phải sang vế trái và $%s$ từ vế trái sang vế phải, ta được $%sx + %sx = %s - %s$' % (a2, b1, a1, a2, b2, abs(b1))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Áp dụng quy tắc chuyển vế (chuyển vế thì đổi dấu), ta được $%sx - %sx = %s + %s$.''' % (a1, a2, b2, abs(b1)))
    list_nb_2 = [loigiai_nb_1]

    # b
    diff_a = a1 - a2
    sum_b = b2 + abs(b1)
    th_da_1_d = '\\True Thu gọn hai vế của phương trình sau khi chuyển vế, ta được $%sx = %s$' % (diff_a, sum_b)
    th_da_1_s = 'Thu gọn hai vế của phương trình sau khi chuyển vế, ta được $%sx = %s$' % (a1 + a2, sum_b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Thu gọn hai vế của $%sx - %sx = %s + %s$, ta được $(%s - %s)x = %s \\Leftrightarrow %sx = %s$.'''
                    % (a1, a2, b2, abs(b1), a1, a2, sum_b, diff_a, sum_b))
    list_th_2 = [loigiai_th_1]

    # c
    vd_da_1_d = '\\True Chia cả hai vế của phương trình $%sx = %s$ cho $%s$, ta tìm được nghiệm duy nhất là $x = %s$' % (diff_a, sum_b, diff_a, x0)
    vd_da_1_s = 'Chia cả hai vế của phương trình $%sx = %s$ cho $%s$, ta tìm được nghiệm duy nhất là $x = %s$' % (diff_a, sum_b, diff_a, x0 + 1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Chia cả hai vế của phương trình $%sx = %s$ cho $%s$, ta được $x = %s : %s = %s$.'''
                    % (diff_a, sum_b, diff_a, sum_b, diff_a, x0))
    list_vd_2 = [loigiai_vd_1]

    # d
    pt_nhan_am1_dung = '%s = %s' % (fmt_lin(-a1, -b1), fmt_lin(-a2, -b2))
    pt_nhan_am1_sai = '%s = %s' % (fmt_lin(-a1, -b1), fmt_lin(-a2, b2))
    vdc_da_1_d = '\\True Nếu nhân cả hai vế của phương trình ban đầu với $-1$, ta được phương trình $%s$' % pt_nhan_am1_dung
    vdc_da_1_s = 'Nếu nhân cả hai vế của phương trình ban đầu với $-1$, ta được phương trình $%s$' % pt_nhan_am1_sai
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi nhân cả hai vế của phương trình $%s$ với $-1$, ta phải đổi dấu tất cả các hạng tử ở cả hai vế, được $%s$.'''
                     % (pt_goc, pt_nhan_am1_dung))
    list_vdc_2 = [loigiai_vdc_1]

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n'
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
