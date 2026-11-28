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


def fmt_frac(f):
    if f.denominator == 1:
        return str(f.numerator)
    return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)


def fmt_dec(val, digits=2):
    d = Decimal(str(val)).quantize(Decimal('1.' + '0'*digits) if digits > 0 else Decimal('1'), rounding=ROUND_HALF_UP)
    s = str(d).rstrip('0').rstrip('.') if digits > 0 else str(d)
    if s == '-0':
        s = '0'
    return s.replace('.', ',')


def bt_dang16_p2_b2_c8_ds8(self):
    # Dạng 16: Bài toán thực tế về phân loại dữ liệu từ bảng thống kê
    tong = random.choice([40, 50])
    if tong == 40:
        tot, kha, dat, chua_dat = 12, 18, 8, 2
    else:
        tot, kha, dat, chua_dat = 15, 22, 10, 3

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) rectangle (6.4,1.6);\n'
        '\\draw[line width=1pt] (0,0.8)--(6.4,0.8) (1.6,0)--(1.6,1.6) (3.2,0)--(3.2,1.6) (4.8,0)--(4.8,1.6);\n'
        '\\node at (0.8,1.2) {Tốt}; \\node at (2.4,1.2) {Khá}; \\node at (4.0,1.2) {Đạt}; \\node at (5.6,1.2) {Chưa đạt};\n'
        '\\node at (0.8,0.4) {$%s$}; \\node at (2.4,0.4) {$%s$}; \\node at (4.0,0.4) {$%s$}; \\node at (5.6,0.4) {$%s$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (tot, kha, dat, chua_dat)

    noidungcauhoi = (
        'Bảng thống kê kết quả xếp loại học lực học kì I của lớp 8A được cho ở hình dưới đây. Giáo viên chủ nhiệm chọn ngẫu nhiên $1$ học sinh trong lớp để phỏng vấn. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (tikz_hinh)
    )

    nb_da_1_d = '\\True Lớp 8A có tổng cộng $%s$ học sinh' % (tong)
    nb_da_1_s = 'Lớp 8A có tổng cộng $%s$ học sinh' % (tong + 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Tổng số học sinh của lớp 8A là $%s + %s + %s + %s = %s$ (học sinh).' % (tot, kha, dat, chua_dat, tong)
    list_nb_2 = [loigiai_nb_1]

    p_tot = Fraction(tot, tong)
    pct_tot = int(p_tot * 100)
    th_da_1_d = '\\True Xác suất chọn được học sinh xếp loại Tốt là $%s\\%%$' % (pct_tot)
    th_da_1_s = 'Xác suất chọn được học sinh xếp loại Tốt là $%s\\%%$' % (pct_tot + 5)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Xác suất chọn được học sinh xếp loại Tốt là $\\dfrac{%s}{%s} = %s = %s\\%%$.' % (tot, tong, fmt_frac(p_tot), pct_tot)
    list_th_2 = [loigiai_th_1]

    p_kha_tot = Fraction(tot + kha, tong)
    p_kha_tot_sai = Fraction(kha, tong)
    vd_da_1_d = '\\True Xác suất chọn được học sinh xếp loại từ Khá trở lên bằng $%s$' % (fmt_frac(p_kha_tot))
    vd_da_1_s = 'Xác suất chọn được học sinh xếp loại từ Khá trở lên bằng $%s$' % (fmt_frac(p_kha_tot_sai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Số học sinh xếp loại từ Khá trở lên (gồm Tốt và Khá) là $%s + %s = %s$ (học sinh). \\ Vậy xác suất cần tìm là $\\dfrac{%s}{%s} = %s$.' % (tot, kha, tot + kha, tot + kha, tong, fmt_frac(p_kha_tot))
    list_vd_2 = [loigiai_vd_1]

    p_not_cd = Fraction(tong - chua_dat, tong)
    p_not_cd_dec = fmt_dec(float(p_not_cd), 2)
    p_not_cd_sai = fmt_dec(float(Fraction(chua_dat, tong)), 2)
    vdc_da_1_d = '\\True Xác suất chọn được học sinh không xếp loại Chưa đạt bằng $%s$' % (p_not_cd_dec)
    vdc_da_1_s = 'Xác suất chọn được học sinh không xếp loại Chưa đạt bằng $%s$' % (p_not_cd_sai)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Số học sinh không xếp loại Chưa đạt là $%s - %s = %s$ (học sinh). \\ Vậy xác suất cần tìm là $\\dfrac{%s}{%s} = %s$.' % (tong, chua_dat, tong - chua_dat, tong - chua_dat, tong, p_not_cd_dec)
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
