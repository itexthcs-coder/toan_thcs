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

def bt_dang13_p2_b5_c7_ds8(self):
    # Dạng 13: Khoảng cách từ gốc tọa độ đến đường thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        b_val = 4 * k
        m1 = 2 + 4 * k
        m2 = 2 + 3 * k

        nb_da_1_d = '\\True Khi $m = %d$, khoảng cách từ gốc tọa độ $O$ đến giao điểm của $(d)$ với trục $Ox$ bằng $1$' % m1
        nb_da_1_s = 'Khi $m = %d$, khoảng cách từ gốc tọa độ $O$ đến giao điểm của $(d)$ với trục $Ox$ bằng $%d$' % (m1, b_val)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Khi $m = %d$, đường thẳng $(d)$ có phương trình $y = %dx + %d$, cắt trục $Ox$ tại $A(-1; 0)$ nên $OA = |-1| = 1$.'''
                        % (m1, b_val, b_val))

        th_da_1_d = '\\True Khi $m = %d$, diện tích tam giác tạo bởi $(d)$ và hai trục tọa độ bằng $%d$' % (m1, 2 * k)
        th_da_1_s = 'Khi $m = %d$, diện tích tam giác tạo bởi $(d)$ và hai trục tọa độ bằng $%d$' % (m1, b_val)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Giao điểm của $(d)$ với hai trục tọa độ là $A(-1; 0)$ và $B(0; %d)$. Diện tích tam giác $OAB$ là $S = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot 1 \\cdot %d = %d$.'''
                        % (b_val, b_val, 2 * k))

        vd_da_1_d = '\\True Khi $m = %d$, độ dài đường cao kẻ từ $O$ đến đường thẳng $(d)$ bằng $\\frac{%d}{\\sqrt{10}}$' % (m2, b_val)
        vd_da_1_s = 'Khi $m = %d$, độ dài đường cao kẻ từ $O$ đến đường thẳng $(d)$ bằng $\\frac{%d}{5}$' % (m2, 3 * b_val)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Khi $m = %d$, $(d): y = %dx + %d$ cắt $Ox, Oy$ tại $A(-\\frac{4}{3}; 0)$ và $B(0; %d)$. Khi đó $OA = \\frac{4}{3}$, $OB = %d$, $AB = \\sqrt{\\frac{16}{9} + %d} = \\frac{%d\\sqrt{10}}{3}$. Đường cao $OH = \\frac{OA \\cdot OB}{AB} = \\frac{%d}{\\sqrt{10}}$.'''
                        % (m2, 3 * k, b_val, b_val, b_val, b_val * b_val, b_val, b_val))

        vdc_da_1_d = '\\True Tồn tại hai giá trị của $m$ để khoảng cách từ gốc tọa độ $O$ đến đường thẳng $(d)$ bằng $\\frac{%d}{\\sqrt{5}}$' % b_val
        vdc_da_1_s = 'Chỉ có duy nhất một giá trị của $m$ để khoảng cách từ gốc tọa độ $O$ đến đường thẳng $(d)$ bằng $\\frac{%d}{\\sqrt{5}}$' % b_val
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Đường thẳng $(d)$ cắt $Ox, Oy$ tại $A(-\\frac{%d}{m-2}; 0)$ và $B(0; %d)$. Ta có $\\frac{1}{OH^2} = \\frac{1}{OA^2} + \\frac{1}{OB^2} = \\frac{(m-2)^2}{%d} + \\frac{1}{%d} = \\frac{5}{%d} \\Leftrightarrow (m-2)^2 = 4 \\Leftrightarrow m = 4$ hoặc $m = 0$ (cả hai đều khác $2$).'''
                         % (b_val, b_val, b_val * b_val, b_val * b_val, b_val * b_val))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (3,0);
\\coordinate (B) at (0,2.5);
\\draw[line width=1pt, ->] (-1.5,0)--(4.2,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-1.2)--(0,3.5) node[left] {$y$};
\\draw[line width=1pt] (-0.8,3.17)--(3.8,-0.67) node[right] {$(d)$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Cho đường thẳng $(d): y = (m - 2)x + %d$ (với $m \\neq 2$). \\ %s''' % (b_val, tikz_fig))

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
