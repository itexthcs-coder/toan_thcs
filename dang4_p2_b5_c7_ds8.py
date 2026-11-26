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

def bt_dang4_p2_b5_c7_ds8(self):
    # Dạng 4: Vị trí tương đối của hai đường thẳng chứa tham số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([1, 2, 3])
        q = random.choice([2, 3, 4])
        k_ss = p + q
        b1 = k_ss + random.choice([1, 2, 3])

        nb_da_1_d = '\\True Hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau khi và chỉ khi $k \\neq %d$' % k_ss
        nb_da_1_s = 'Hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau khi và chỉ khi $k = %d$' % k_ss
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau khi $2k - %d \\neq k + %d \\Leftrightarrow k \\neq %d$ (kết hợp với điều kiện $k \\neq \\frac{%d}{2}$ và $k \\neq -%d$).'''
                        % (p, q, k_ss, p, q))

        th_da_1_d = '\\True Khi $k = %d$, hai đường thẳng $(d_1)$ và $(d_2)$ song song với nhau' % k_ss
        th_da_1_s = 'Khi $k = %d$, hai đường thẳng $(d_1)$ và $(d_2)$ trùng nhau' % k_ss
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Khi $k = %d$, ta có $a_1 = 2 \\cdot %d - %d = %d$ và $a_2 = %d + %d = %d$ nên $a_1 = a_2$. Đồng thời tung độ gốc $b_1 = %d \\neq b_2 = %d$ nên $(d_1) // (d_2)$.'''
                        % (k_ss, k_ss, p, 2*k_ss - p, k_ss, q, k_ss + q, b1, k_ss))

        vd_da_1_d = '\\True Không tồn tại giá trị nào của $k$ để hai đường thẳng $(d_1)$ và $(d_2)$ trùng nhau'
        vd_da_1_s = 'Khi $k = %d$, hai đường thẳng $(d_1)$ và $(d_2)$ trùng nhau' % b1
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Hai đường thẳng trùng nhau khi $a_1 = a_2$ (tức $k = %d$) và $b_1 = b_2$ (tức $k = %d$). Vì $%d \\neq %d$ nên không tồn tại giá trị nào của $k$ để $(d_1)$ và $(d_2)$ trùng nhau.'''
                        % (k_ss, b1, k_ss, b1))

        vdc_da_1_d = '\\True Khi $k = 0$, giao điểm của $(d_1)$ và $(d_2)$ không nằm trên trục tung'
        vdc_da_1_s = 'Khi $k = 0$, giao điểm của $(d_1)$ và $(d_2)$ nằm trên trục tung'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        x_g = Fraction(-b1, -p - q)
        y_g = -p * x_g + b1
        loigiai_vdc_1 = ('''Khi $k = 0$, $(d_1): y = -%dx + %d$ và $(d_2): y = %dx$. Hoành độ giao điểm là nghiệm phương trình $-%dx + %d = %dx \\Leftrightarrow x = %s \\neq 0$, tung độ $y = %s$. Vậy giao điểm không nằm trên trục tung.'''
                         % (p, b1, q, p, b1, q, fmt_num(x_g), fmt_num(y_g)))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\draw[line width=1pt, ->] (-3,0)--(3.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-2)--(0,3.8) node[left] {$y$};
\\draw[line width=1pt] (-2.5,-0.5)--(1.5,3.5) node[right] {$(d_1)$};
\\draw[line width=1pt] (-1.5,-1.5)--(2.5,2.5) node[right] {$(d_2)$};
\\fill (O) circle (1pt) node[below right] {$O$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Cho hai đường thẳng $(d_1): y = (2k - %d)x + %d$ và $(d_2): y = (k + %d)x + k$ (với $k \\neq \\frac{%d}{2}$ và $k \\neq -%d$). \\ %s'''
                         % (p, b1, q, p, q, tikz_fig))

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
