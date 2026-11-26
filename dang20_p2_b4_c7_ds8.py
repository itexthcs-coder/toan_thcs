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


def fmt_vn(val):
    if isinstance(val, Decimal):
        s = str(val)
    elif isinstance(val, float):
        s = str(round(val, 6))
        if s.endswith('.0'):
            s = s[:-2]
    else:
        s = str(val)
    return s.replace('.', ',')


def fmt_frac_tex(fr):
    if fr.denominator == 1:
        return str(fr.numerator)
    if fr.numerator < 0:
        return '-\\frac{%s}{%s}' % (abs(fr.numerator), fr.denominator)
    return '\\frac{%s}{%s}' % (fr.numerator, fr.denominator)


def fmt_linear_tex(a_fr, b_fr, var='x'):
    # Định dạng ax + b với a_fr, b_fr là Fraction
    parts = []
    if a_fr != 0:
        if a_fr == 1:
            parts.append(var)
        elif a_fr == -1:
            parts.append('-%s' % var)
        else:
            parts.append('%s%s' % (fmt_frac_tex(a_fr), var))
    if b_fr != 0:
        if not parts:
            parts.append(fmt_frac_tex(b_fr))
        else:
            if b_fr > 0:
                parts.append('+ %s' % fmt_frac_tex(b_fr))
            else:
                parts.append('- %s' % fmt_frac_tex(abs(b_fr)))
    if not parts:
        return '0'
    return ' '.join(parts)


def bt_dang20_p2_b4_c7_ds8(self):
    # Dạng 20 (Thực tế 5): Lượng xăng còn lại y = tank - rate_per_km * x
    tank = random.choice([45, 50, 60])
    lit_per_100 = random.choice([5, 6, 8])
    rate_dec = Decimal(lit_per_100) / Decimal('100')
    rate_str = fmt_vn(rate_dec)

    x_check = 250
    y_check_dec = Decimal(tank) - rate_dec * Decimal(x_check)
    y_check_str = fmt_vn(y_check_dec)

    # Cảnh báo còn lại y_warn lít (chọn y_warn sao cho (tank - y_warn) chia hết cho rate_dec)
    x_warn = random.choice([600, 700, 750])
    y_warn_dec = Decimal(tank) - rate_dec * Decimal(x_warn)
    while y_warn_dec <= 0:
        x_warn -= 100
        y_warn_dec = Decimal(tank) - rate_dec * Decimal(x_warn)
    y_warn_str = fmt_vn(y_warn_dec)

    tikz_fig = (
        '\\begin{center}\\begin{tikzpicture}[scale=0.55, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\draw[->, line width=1pt] (-0.5,0) -- (5.5,0) node[below] {$x$ (km)};'
        '\\draw[->, line width=1pt] (0,-0.5) -- (0,4.5) node[left] {$y$ (lít)};'
        '\\coordinate (O) at (0,0);'
        '\\coordinate (A) at (0,3.5);'
        '\\coordinate (B) at (4.5,0);'
        '\\draw[line width=1pt] (A) -- (B);'
        '\\fill (O) circle (1pt) node[below left] {$O$};'
        '\\fill (A) circle (1pt) node[left] {$%s$};'
        '\\fill (B) circle (1pt) node[below] {$x_{\\max}$};'
        '\\end{tikzpicture}\\end{center}'
        % tank
    )

    noidungcauhoi = (
        '''Bình xăng của một chiếc ô tô có dung tích tối đa $%s\\text{ lít}$. Khi bắt đầu chuyến đi đường dài, bình xăng được đổ đầy. Biết rằng cứ đi được $100\\text{ km}$ thì xe tiêu thụ hết $%s\\text{ lít}$ xăng. Gọi $y$ (lít) là lượng xăng còn lại trong bình sau khi xe đi được quãng đường $x$ (km). Xét tính đúng sai của các khẳng định sau:'''
        % (tank, lit_per_100)
    )

    # Ý a
    nb_da_1_d = '\\True Trung bình mỗi kilômét xe tiêu thụ hết $%s\\text{ lít}$ xăng' % rate_str
    nb_da_1_s = 'Trung bình mỗi kilômét xe tiêu thụ hết $%s\\text{ lít}$ xăng' % lit_per_100
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        '''Đi $100\\text{ km}$ tiêu thụ hết $%s\\text{ lít}$ xăng nên mỗi kilômét xe tiêu thụ lượng xăng là: $\\dfrac{%s}{100} = %s$ (lít).'''
        % (lit_per_100, lit_per_100, rate_str)
    )
    list_nb_2 = [loigiai_nb_1]

    # Ý b
    th_da_1_d = '\\True Công thức tính lượng xăng còn lại $y$ theo quãng đường $x$ là $y = %s - %sx$' % (tank, rate_str)
    th_da_1_s = 'Công thức tính lượng xăng còn lại $y$ theo quãng đường $x$ là $y = %s + %sx$' % (tank, rate_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        '''Sau khi đi $x$ (km), lượng xăng đã tiêu thụ là $%sx$ (lít). Do đó lượng xăng còn lại trong bình là $y = %s - %sx$ (lít).'''
        % (rate_str, tank, rate_str)
    )
    list_th_2 = [loigiai_th_1]

    # Ý c
    vd_da_1_d = '\\True Sau khi xe đi được $%s\\text{ km}$, trong bình còn lại $%s\\text{ lít}$ xăng' % (x_check, y_check_str)
    vd_da_1_s = 'Sau khi xe đi được $%s\\text{ km}$, trong bình còn lại $%s\\text{ lít}$ xăng' % (x_check, fmt_vn(rate_dec * Decimal(x_check)))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        '''Thay $x = %s$ vào công thức ta được: $y = %s - %s \\cdot %s = %s - %s = %s$ (lít).%s'''
        % (x_check, tank, rate_str, x_check, tank, fmt_vn(rate_dec * Decimal(x_check)), y_check_str, tikz_fig)
    )
    list_vd_2 = [loigiai_vd_1]

    # Ý d
    vdc_da_1_d = '\\True Khi đèn báo nhiên liệu bật sáng (lúc trong bình chỉ còn lại $%s\\text{ lít}$ xăng), ô tô đã đi được quãng đường dài $%s\\text{ km}$' % (y_warn_str, x_warn)
    vdc_da_1_s = 'Khi đèn báo nhiên liệu bật sáng (lúc trong bình chỉ còn lại $%s\\text{ lít}$ xăng), ô tô đã đi được quãng đường dài $%s\\text{ km}$' % (y_warn_str, x_warn + 50)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        '''Thay $y = %s$ vào công thức hàm số ta có: $%s - %sx = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (km).'''
        % (y_warn_str, tank, rate_str, y_warn_str, rate_str, fmt_vn(Decimal(tank) - y_warn_dec), x_warn)
    )
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
