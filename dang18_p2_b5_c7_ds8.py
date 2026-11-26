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

def bt_dang18_p2_b5_c7_ds8(self):
    # Dạng 18 (Thực tế): Bài toán điểm hòa vốn trong kinh doanh quán cà phê
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cost_var = random.choice([10, 12])
        price = cost_var + random.choice([15, 20])
        diff = price - cost_var
        x_even = random.choice([300, 400, 500])
        cost_fix = diff * x_even
        cost_fix_tr = Fraction(cost_fix, 1000)

        nb_da_1_d = '\\True Hàm số biểu diễn tổng chi phí là $y_1 = %dx + %d$ và tổng doanh thu là $y_2 = %dx$' % (cost_var, cost_fix, price)
        nb_da_1_s = 'Hàm số biểu diễn tổng chi phí là $y_1 = %dx + %d$ và tổng doanh thu là $y_2 = %dx$' % (cost_fix, cost_var, price)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Tổng chi phí gồm chi phí cố định $%d$ nghìn đồng và chi phí biến đổi $%dx$ nghìn đồng nên $y_1 = %dx + %d$; tổng doanh thu là $y_2 = %dx$.'''
                        % (cost_fix, cost_var, cost_var, cost_fix, price))

        th_da_1_d = '\\True Hệ số góc của đường doanh thu lớn hơn hệ số góc của đường chi phí, chứng tỏ càng bán nhiều ly thì doanh thu tăng nhanh hơn chi phí'
        th_da_1_s = 'Hệ số góc của đường doanh thu nhỏ hơn hệ số góc của đường chi phí'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Đường doanh thu có hệ số góc $a_2 = %d$ lớn hơn hệ số góc $a_1 = %d$ của đường chi phí nên doanh thu tăng nhanh hơn chi phí.'''
                        % (price, cost_var))

        vd_da_1_d = '\\True Đồ thị của hai hàm số $y_1$ và $y_2$ cắt nhau vì có hai hệ số góc khác nhau'
        vd_da_1_s = 'Đồ thị của hai hàm số $y_1$ và $y_2$ song song với nhau'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vì $a_1 = %d \\neq a_2 = %d$ nên hai đường thẳng biểu diễn $y_1$ và $y_2$ cắt nhau.'''
                        % (cost_var, price))

        vdc_da_1_d = '\\True Để đạt điểm hòa vốn (doanh thu bằng chi phí), quán cần bán đúng $%d$ ly cà phê trong tháng' % x_even
        vdc_da_1_s = 'Để đạt điểm hòa vốn (doanh thu bằng chi phí), quán cần bán đúng $%d$ ly cà phê trong tháng' % (x_even + 100)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Hoành độ giao điểm của hai đường thẳng thỏa mãn $%dx = %dx + %d \\Leftrightarrow %dx = %d \\Leftrightarrow x = %d$ (ly).'''
                         % (price, cost_var, cost_fix, diff, cost_fix, x_even))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (I) at (1.2,1.8);
\\draw[line width=1pt, ->] (-2.5,0)--(3.8,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-1.5)--(0,3.8) node[left] {$y$};
\\draw[line width=1pt] (-1.2,-0.6)--(2.6,3.2) node[right] {$(d_1)$};
\\draw[line width=1pt] (-0.8,3.2)--(3.2,0.4) node[right] {$(d_2)$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (I) circle (1pt) node[above] {$I$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Một bạn trẻ khởi nghiệp mở quầy cà phê mang đi với chi phí cố định là $%s$ triệu đồng/tháng và chi phí nguyên vật liệu cho mỗi ly cà phê là $%d\\,000$ đồng. Giá bán mỗi ly cà phê là $%d\\,000$ đồng. Gọi $x$ (ly) là số ly cà phê bán được trong tháng ($x \\in \\mathbb{N}^*$), $y_1$ (nghìn đồng) là tổng chi phí và $y_2$ (nghìn đồng) là tổng doanh thu. \\ %s'''
                         % (fmt_num(cost_fix_tr), cost_var, price, tikz_fig))

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
                break

        combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
        combined_th = list(zip([th_da_1], [loigiai_th_1]))
        combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
        combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
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
