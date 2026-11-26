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

def bt_dang16_p2_b1_c7_ds8(self):
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
    # Dạng 16: Ứng dụng trong Quản lí chi tiêu và Mua sắm thông minh
    gia_vo_goc = random.choice([10000, 12000, 15000])
    giam_pt = random.choice([10, 20])
    gia_vo_sau = gia_vo_goc * (100 - giam_pt) // 100
    gia_but = random.choice([4000, 5000, 6000])
    so_but = random.choice([5, 6, 8, 10])
    tien_but = gia_but * so_but
    so_vo = random.choice([8, 9, 10, 11])
    du_tien = random.choice([1000, 2000, 3000])
    tong_tien = tien_but + so_vo * gia_vo_sau + du_tien

    noidungcauhoi = ('''Một cửa hàng văn phòng phẩm niêm yết giá một quyển vở là $%s$ đồng và một chiếc bút bi là $%s$ đồng. Nhân dịp khai giảng, cửa hàng giảm giá $%s\\%%$ cho mỗi quyển vở nhưng giữ nguyên giá bút bi. Bạn Minh mang theo $%s$ đồng để mua $%s$ chiếc bút bi và $x$ quyển vở ($x \\in \\mathbb{N}^*$) sao cho vừa đủ hết số tiền mang theo. Xét tính đúng, sai của các khẳng định sau:'''
                     % (fmt_money(gia_vo_goc), fmt_money(gia_but), giam_pt, fmt_money(tong_tien), so_but))

    # a
    nb_da_1_d = '\\True Giá của mỗi quyển vở sau khi được giảm $%s\\%%$ là $%s$ đồng' % (giam_pt, fmt_money(gia_vo_sau))
    nb_da_1_s = 'Giá của mỗi quyển vở sau khi được giảm $%s\\%%$ là $%s$ đồng' % (giam_pt, fmt_money(gia_vo_goc - giam_pt * 100))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Giá mỗi quyển vở sau khi giảm $%s\\%%$ là: $%s \\cdot (100\\%% - %s\\%%) = %s$ (đồng).'''
                    % (giam_pt, fmt_money(gia_vo_goc), giam_pt, fmt_money(gia_vo_sau)))
    list_nb_2 = [loigiai_nb_1]

    # b
    th_da_1_d = '\\True Số tiền bạn Minh dùng để mua $%s$ chiếc bút bi là $%s$ đồng' % (so_but, fmt_money(tien_but))
    th_da_1_s = 'Số tiền bạn Minh dùng để mua $%s$ chiếc bút bi là $%s$ đồng' % (so_but, fmt_money(tien_but + gia_but))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Số tiền mua $%s$ chiếc bút bi là: $%s \\cdot %s = %s$ (đồng).'''
                    % (so_but, so_but, fmt_money(gia_but), fmt_money(tien_but)))
    list_th_2 = [loigiai_th_1]

    # c
    pt_dung = '%sx + %s = %s' % (fmt_money(gia_vo_sau), fmt_money(tien_but), fmt_money(tong_tien))
    pt_sai = '%sx + %s = %s' % (fmt_money(gia_vo_goc), fmt_money(tien_but), fmt_money(tong_tien))
    vd_da_1_d = '\\True Phương trình biểu thị tổng số tiền mua vở và bút của Minh bằng $%s$ đồng là $%s$' % (fmt_money(tong_tien), pt_dung)
    vd_da_1_s = 'Phương trình biểu thị tổng số tiền mua vở và bút của Minh bằng $%s$ đồng là $%s$' % (fmt_money(tong_tien), pt_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Tổng số tiền mua $x$ quyển vở (giá $%s$ đồng/quyển) và $%s$ chiếc bút bi là $%s$ đồng, nên ta có phương trình $%s$.'''
                    % (fmt_money(gia_vo_sau), so_but, fmt_money(tong_tien), pt_dung))
    list_vd_2 = [loigiai_vd_1]

    # d
    vdc_da_1_d = '\\True Bạn Minh có thể mua được nhiều nhất $%s$ quyển vở và còn dư lại $%s$ đồng' % (so_vo, fmt_money(du_tien))
    vdc_da_1_s = 'Bạn Minh có thể mua được nhiều nhất $%s$ quyển vở và vừa hết tiền' % (so_vo + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Giải phương trình $%s \\Leftrightarrow %sx = %s \\Leftrightarrow x = \\frac{%s}{%s} = %s$ dư $%s$. Vậy bạn Minh mua được nhiều nhất $%s$ quyển vở và còn dư $%s$ đồng.'''
                     % (pt_dung, fmt_money(gia_vo_sau), fmt_money(tong_tien - tien_but), fmt_money(tong_tien - tien_but), fmt_money(gia_vo_sau), so_vo, fmt_money(du_tien), so_vo, fmt_money(du_tien)))
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
