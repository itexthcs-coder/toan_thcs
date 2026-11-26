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

def bt_dang14_p2_b5_c7_ds8(self):
    # Dạng 14: Xác định đa giác tạo bởi các đường thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b = random.choice([2, 3, 4, 5])
        chu_vi = 4 * b

        nb_da_1_d = '\\True Các cặp đường thẳng $(d_1)$ và $(d_2)$; $(d_3)$ và $(d_4)$ từng đôi một song song với nhau'
        nb_da_1_s = 'Bốn đường thẳng đã cho đôi một cắt nhau tạo thành sáu giao điểm phân biệt'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $(d_1)$ và $(d_2)$ cùng có hệ số góc $a = 1$ (tung độ gốc $%d \\neq -%d$) nên $(d_1) // (d_2)$; $(d_3)$ và $(d_4)$ cùng có hệ số góc $a = -1$ (tung độ gốc $%d \\neq -%d$) nên $(d_3) // (d_4)$.'''
                        % (b, b, b, b))

        th_da_1_d = '\\True Các đỉnh của tứ giác tạo bởi bốn đường thẳng trên đều nằm trên hai trục tọa độ $Ox$ và $Oy$'
        th_da_1_s = 'Không có đỉnh nào của tứ giác tạo bởi bốn đường thẳng trên nằm trên trục $Ox$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Tìm giao điểm của các cặp đường thẳng cắt nhau ta được bốn đỉnh: $A(%d; 0)$, $B(0; %d)$, $C(-%d; 0)$, $D(0; -%d)$, đều nằm trên hai trục $Ox$ và $Oy$.'''
                        % (b, b, b, b))

        vd_da_1_d = '\\True Tứ giác tạo bởi giao điểm của bốn đường thẳng trên là một hình vuông'
        vd_da_1_s = 'Tứ giác tạo bởi giao điểm của bốn đường thẳng trên là một hình bình hành nhưng không phải hình chữ nhật'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Tứ giác $ABCD$ có hai đường chéo $AC = %d$ và $BD = %d$ bằng nhau, vuông góc với nhau và cắt nhau tại trung điểm $O$ của mỗi đường nên $ABCD$ là hình vuông.'''
                        % (2 * b, 2 * b))

        vdc_da_1_d = '\\True Chu vi của tứ giác tạo bởi bốn đường thẳng trên bằng $%d\\sqrt{2}$ đơn vị độ dài' % chu_vi
        vdc_da_1_s = 'Diện tích của tứ giác tạo bởi bốn đường thẳng trên bằng $%d$ đơn vị diện tích' % (b * b)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Mỗi cạnh của hình vuông $ABCD$ có độ dài $AB = \\sqrt{OA^2 + OB^2} = \\sqrt{%d^2 + %d^2} = %d\\sqrt{2}$. Do đó chu vi hình vuông bằng $4 \\cdot %d\\sqrt{2} = %d\\sqrt{2}$ (đơn vị độ dài).'''
                         % (b, b, b, b, chu_vi))

        tikz_fig = '''\\begin{center}
\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (2,0);
\\coordinate (B) at (0,2);
\\coordinate (C) at (-2,0);
\\coordinate (D) at (0,-2);
\\draw[line width=1pt, ->] (-3.2,0)--(3.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-3)--(0,3.2) node[left] {$y$};
\\draw[line width=1pt] (-2.7,-0.7)--(0.7,2.7) node[above] {$(d_1)$};
\\draw[line width=1pt] (-0.7,-2.7)--(2.7,0.7) node[right] {$(d_2)$};
\\draw[line width=1pt] (-0.7,2.7)--(2.7,-0.7) node[right] {$(d_3)$};
\\draw[line width=1pt] (-2.7,0.7)--(0.7,-2.7) node[below] {$(d_4)$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below right] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below left] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\end{tikzpicture}
\\end{center}'''
        noidungcauhoi = ('''Cho bốn đường thẳng: $(d_1): y = x + %d$; $(d_2): y = x - %d$; $(d_3): y = -x + %d$; $(d_4): y = -x - %d$. \\ %s'''
                         % (b, b, b, b, tikz_fig))

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
