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

def bt_dang12_p2_b5_c7_ds8(self):
    # Dạng 12: Điều kiện hai đường thẳng vuông góc qua hệ số góc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = random.choice([2, 4])
        xm = a1
        b1 = -random.choice([2, 4])
        ym = a1 * xm + b1
        a2 = Fraction(-1, a1)
        b2 = ym - a2 * xm
        x_ox = -b2 / a2
        area = Fraction(1, 2) * abs(b2 - b1) * xm

        nb_da_1_d = '\\True Hệ số góc của đường thẳng $(d_2)$ là $a = %s$' % fmt_num(a2)
        nb_da_1_s = 'Hệ số góc của đường thẳng $(d_2)$ là $a = %s$' % fmt_num(-a2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì $(d_1) \\perp (d_2)$ nên tích hai hệ số góc bằng $-1$, tức là $%d \\cdot a = -1 \\Rightarrow a = %s$.'''
                        % (a1, fmt_num(a2)))

        th_da_1_d = '\\True Phương trình của đường thẳng $(d_2)$ là $y = %s$' % fmt_line(a2, b2)
        th_da_1_s = 'Phương trình của đường thẳng $(d_2)$ là $y = %s$' % fmt_line(a2, b2 + 2)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Đường thẳng $(d_2)$ có dạng $y = %sx + b$. Vì $(d_2)$ đi qua $M(%d; %d)$ nên $%d = %s \\cdot %d + b \\Rightarrow b = %s$. Vậy $(d_2): y = %s$.'''
                        % (fmt_num(a2), xm, ym, ym, fmt_num(a2), xm, fmt_num(b2), fmt_line(a2, b2)))

        vd_da_1_d = '\\True Đường thẳng $(d_2)$ cắt trục hoành tại điểm có hoành độ bằng $%s$' % fmt_num(x_ox)
        vd_da_1_s = 'Đường thẳng $(d_2)$ cắt trục hoành tại điểm có hoành độ bằng $%s$' % fmt_num(b2)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Cho $y = 0$ trong phương trình $(d_2)$ ta có $%s = 0 \\Leftrightarrow x = %s$.'''
                        % (fmt_line(a2, b2), fmt_num(x_ox)))

        vdc_da_1_d = '\\True Tam giác tạo bởi $(d_1)$, $(d_2)$ và trục tung có diện tích bằng $%s$ đơn vị diện tích' % fmt_num(area)
        vdc_da_1_s = 'Tam giác tạo bởi $(d_1)$, $(d_2)$ và trục tung có diện tích bằng $%s$ đơn vị diện tích' % fmt_num(area * 2)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Giao điểm của $(d_1)$ và $(d_2)$ với trục tung lần lượt là $P(0; %d)$ và $Q(0; %s)$, suy ra $PQ = |%s - (%d)| = %s$. Giao điểm của $(d_1)$ và $(d_2)$ là $M(%d; %d)$ có khoảng cách đến trục tung là $x_M = %d$. Diện tích tam giác $MPQ$ là $\\frac{1}{2} \\cdot %s \\cdot %d = %s$.'''
                         % (b1, fmt_num(b2), fmt_num(b2), b1, fmt_num(abs(b2 - b1)), xm, ym, xm, fmt_num(abs(b2 - b1)), xm, fmt_num(area)))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M) at (1.5,1.5);
\\draw[line width=1pt, ->] (-2,0)--(4,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-2)--(0,3.5) node[left] {$y$};
\\draw[line width=1pt] (-0.5,-1.5)--(2.5,3) node[right] {$(d_1)$};
\\draw[line width=1pt] (-1.5,3.5)--(3.8,-0.03) node[right] {$(d_2)$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $(d_1): y = %s$ và đường thẳng $(d_2): y = ax + b$ ($a \\neq 0$) đi qua điểm $M(%d; %d)$. Biết rằng $(d_2)$ vuông góc với $(d_1)$ (hai đường thẳng vuông góc khi tích hai hệ số góc bằng $-1$). \\ %s'''
                         % (fmt_line(a1, b1), xm, ym, tikz_fig))

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
