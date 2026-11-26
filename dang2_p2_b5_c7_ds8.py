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

def bt_dang2_p2_b5_c7_ds8(self):
    # Dạng 2: So sánh độ lớn góc tạo bởi đường thẳng và trục Ox
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k1 = random.choice([2, 3, 4, 5])
        a1 = Fraction(1, k1)
        a2 = random.choice([2, 3])
        a3 = a2 + random.choice([2, 3, 4])
        a4 = -random.choice([3, 4, 5, 6])

        b1 = random.randint(1, 6)
        b2 = -random.randint(1, 6)
        b3 = -random.randint(2, 8)
        b4 = random.randint(1, 5)

        d1_str = fmt_line(a1, b1)
        d2_str = fmt_line(a2, b2)
        d3_str = fmt_line(a3, b3)
        d4_str = fmt_line(a4, b4)

        nb_da_1_d = '\\True Cả ba góc $\\alpha_1, \\alpha_2, \\alpha_3$ đều là góc nhọn'
        nb_da_1_s = 'Trong ba góc $\\alpha_1, \\alpha_2, \\alpha_3$ có đúng một góc tù'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Các đường thẳng $(d_1), (d_2), (d_3)$ có hệ số góc lần lượt là $a_1 = %s > 0$, $a_2 = %d > 0$, $a_3 = %d > 0$ nên cả ba góc $\\alpha_1, \\alpha_2, \\alpha_3$ đều là góc nhọn.'''
                        % (fmt_num(a1), a2, a3))

        th_da_1_d = '\\True Vì $0 < %s < %d < %d$ nên $\\alpha_1 < \\alpha_2 < \\alpha_3$' % (fmt_num(a1), a2, a3)
        th_da_1_s = 'Vì $0 < %s < %d < %d$ nên $\\alpha_1 > \\alpha_2 > \\alpha_3$' % (fmt_num(a1), a2, a3)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Khi hệ số góc dương, hệ số góc càng lớn thì góc tạo bởi đường thẳng và trục $Ox$ càng lớn. Vì $0 < %s < %d < %d$ nên $\\alpha_1 < \\alpha_2 < \\alpha_3$.'''
                        % (fmt_num(a1), a2, a3))

        vd_da_1_d = '\\True Đường thẳng $(d_3)$ có độ dốc lớn hơn đường thẳng $(d_2)$'
        vd_da_1_s = 'Đường thẳng $(d_1)$ có độ dốc lớn hơn đường thẳng $(d_2)$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Hệ số góc của $(d_3)$ là $%d$ lớn hơn hệ số góc của $(d_2)$ là $%d$ nên $(d_3)$ dốc hơn $(d_2)$.'''
                        % (a3, a2))

        vdc_da_1_d = '\\True Nếu thêm đường thẳng $(d_4): y = %s$ tạo với trục $Ox$ góc $\\alpha_4$ thì $\\alpha_4$ là góc lớn nhất trong bốn góc' % d4_str
        vdc_da_1_s = 'Nếu thêm đường thẳng $(d_4): y = %s$ tạo với trục $Ox$ góc $\\alpha_4$ thì $\\alpha_4$ là góc nhỏ nhất trong bốn góc' % d4_str
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Đường thẳng $(d_4): y = %s$ có hệ số góc $a_4 = %d < 0$ nên $\\alpha_4$ là góc tù ($90^\\circ < \\alpha_4 < 180^\\circ$), trong khi $\\alpha_1, \\alpha_2, \\alpha_3$ đều là góc nhọn (nhỏ hơn $90^\\circ$). Do đó $\\alpha_4$ lớn nhất trong bốn góc.'''
                         % (d4_str, a4))

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
        noidungcauhoi = ('''Trên cùng mặt phẳng tọa độ $Oxy$, xét ba đường thẳng $(d_1): y = %s$, $(d_2): y = %s$ và $(d_3): y = %s$. Gọi $\\alpha_1, \\alpha_2, \\alpha_3$ lần lượt là góc tạo bởi $(d_1), (d_2), (d_3)$ với trục $Ox$. \\ %s'''
                         % (d1_str, d2_str, d3_str, tikz_fig))

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
