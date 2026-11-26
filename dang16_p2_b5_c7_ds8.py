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

def bt_dang16_p2_b5_c7_ds8(self):
    # Dạng 16 (Thực tế): Bài toán cước phí taxi và so sánh gói cước
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gia_km = random.choice([12, 14, 15])
        phi_mo_cua_1 = random.choice([10, 12])
        giam = random.choice([4, 5])
        phi_mo_cua_2 = phi_mo_cua_1 - giam

        gia_km_3 = gia_km - 2
        x_cut = random.choice([4, 5, 6])
        phi_mo_cua_3 = phi_mo_cua_1 + 2 * x_cut

        nb_da_1_d = '\\True Hệ số góc của đường thẳng biểu diễn hai gói cước trên đều bằng $%d$, thể hiện giá cước mỗi ki-lô-mét là $%d\\,000$ đồng' % (gia_km, gia_km)
        nb_da_1_s = 'Hệ số góc của Gói Tiêu chuẩn là $%d$ còn của Gói Tiết kiệm là $%d$' % (phi_mo_cua_1, phi_mo_cua_2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Hai hàm số $y = %dx + %d$ và $y = %dx + %d$ đều có hệ số góc $a = %d$, biểu thị đơn giá $%d\\,000$ đồng/km.'''
                        % (gia_km, phi_mo_cua_1, gia_km, phi_mo_cua_2, gia_km, gia_km))

        th_da_1_d = '\\True Trên cùng hệ trục tọa độ, đồ thị biểu diễn hai gói cước là hai nửa đường thẳng song song với nhau'
        th_da_1_s = 'Trên cùng hệ trục tọa độ, đồ thị biểu diễn hai gói cước là hai đường thẳng cắt nhau'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Vì hai đường thẳng có cùng hệ số góc $a = %d$ và tung độ gốc khác nhau ($%d \\neq %d$) nên song song với nhau.'''
                        % (gia_km, phi_mo_cua_1, phi_mo_cua_2))

        vd_da_1_d = '\\True Ở mọi quãng đường $x > 0$, Gói Tiết kiệm luôn rẻ hơn Gói Tiêu chuẩn $%d\\,000$ đồng' % giam
        vd_da_1_s = 'Quãng đường càng dài thì mức chênh lệch tiền giữa hai gói cước càng lớn'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Hiệu số tiền giữa hai gói là $(%dx + %d) - (%dx + %d) = %d$ (nghìn đồng), luôn không đổi với mọi $x > 0$.'''
                        % (gia_km, phi_mo_cua_1, gia_km, phi_mo_cua_2, giam))

        vdc_da_1_d = '\\True Nếu hãng khác đưa ra Gói Cạnh tranh có công thức $y = %dx + %d$ thì đồ thị gói này cắt đồ thị Gói Tiêu chuẩn tại điểm có hoành độ $x = %d$' % (gia_km_3, phi_mo_cua_3, x_cut)
        vdc_da_1_s = 'Nếu hãng khác đưa ra Gói Cạnh tranh có công thức $y = %dx + %d$ thì đồ thị gói này song song với đồ thị Gói Tiêu chuẩn' % (gia_km_3, phi_mo_cua_3)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Vì hệ số góc $%d \\neq %d$ nên hai đường thẳng cắt nhau. Hoành độ giao điểm thỏa mãn $%dx + %d = %dx + %d \\Leftrightarrow 2x = %d \\Leftrightarrow x = %d$.'''
                         % (gia_km_3, gia_km, gia_km_3, phi_mo_cua_3, gia_km, phi_mo_cua_1, 2 * x_cut, x_cut))

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
        noidungcauhoi = ('''Một hãng taxi công nghệ áp dụng hai gói cước cho hành khách tính theo quãng đường di chuyển $x$ (km, $x > 0$) và tổng số tiền phải trả $y$ (nghìn đồng): \\
\\begin{tabular}{|l|c|c|}
\\hline
\\textbf{Tên gói cước} & \textbf{Gói Tiêu chuẩn} & \textbf{Gói Tiết kiệm} \\
\\hline
\\textbf{Công thức tính cước} & $y = %dx + %d$ & $y = %dx + %d$ \\
\\hline
\\end{tabular} \\ %s'''
                         % (gia_km, phi_mo_cua_1, gia_km, phi_mo_cua_2, tikz_fig))

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
