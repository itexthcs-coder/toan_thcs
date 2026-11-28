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


def bt_dang13_p2_b2_c8_ds8(self):
    # Dạng 13: Bài toán ngược – Bớt đi đối tượng và cho trước xác suất mới
    tong_sau = random.choice([20, 25, 30])
    bot = random.choice([4, 5, 6])
    tong_dau = tong_sau + bot
    xanh_sau = random.choice([i for i in range(6, tong_sau - 4) if Fraction(i, tong_sau).denominator in [4, 5, 6, 10]])
    xanh_dau = xanh_sau + bot
    trang_dau = tong_dau - xanh_dau
    p_xanh_sau = Fraction(xanh_sau, tong_sau)

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) rectangle (6.6,1.4);\n'
        '\\node at (3.3,0.7) {Bình ban đầu: $%s$ bi $\\longrightarrow$ Lấy ra $%s$ bi xanh};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (tong_dau, bot)

    noidungcauhoi = (
        'Một bình chứa $%s$ viên bi gồm bi xanh và bi trắng cùng kích thước. Người ta lấy ra khỏi bình $%s$ viên bi xanh. Khi lấy ngẫu nhiên $1$ viên bi trong số bi còn lại trong bình, xác suất lấy được viên bi xanh là $%s$. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (tong_dau, bot, fmt_frac(p_xanh_sau), tikz_hinh)
    )

    nb_da_1_d = '\\True Số viên bi còn lại trong bình sau khi lấy ra $%s$ viên là $%s$ viên' % (bot, tong_sau)
    nb_da_1_s = 'Số viên bi còn lại trong bình sau khi lấy ra $%s$ viên là $%s$ viên' % (bot, tong_dau)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Sau khi lấy ra $%s$ viên bi, số viên bi còn lại trong bình là $%s - %s = %s$ (viên).' % (bot, tong_dau, bot, tong_sau)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số viên bi xanh còn lại trong bình là $%s$ viên' % (xanh_sau)
    th_da_1_s = 'Số viên bi xanh còn lại trong bình là $%s$ viên' % (xanh_dau)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Gọi $y$ là số viên bi xanh còn lại trong bình ($y \\in \\mathbb{N}^*$). Ta có $\\dfrac{y}{%s} = %s \\Rightarrow y = %s \\cdot %s = %s$ (viên).' % (tong_sau, fmt_frac(p_xanh_sau), tong_sau, fmt_frac(p_xanh_sau), xanh_sau)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Ban đầu trong bình có $%s$ viên bi trắng' % (trang_dau)
    vd_da_1_s = 'Ban đầu trong bình có $%s$ viên bi trắng' % (xanh_dau)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Số viên bi xanh ban đầu là $%s + %s = %s$ (viên). \\ Vậy số viên bi trắng ban đầu trong bình là $%s - %s = %s$ (viên).' % (xanh_sau, bot, xanh_dau, tong_dau, xanh_dau, trang_dau)
    list_vd_2 = [loigiai_vd_1]

    p_trang_dau = Fraction(trang_dau, tong_dau)
    p_trang_dau_sai = Fraction(trang_dau, tong_sau)
    vdc_da_1_d = '\\True Ban đầu, xác suất lấy ngẫu nhiên được viên bi trắng là $%s$' % (fmt_frac(p_trang_dau))
    vdc_da_1_s = 'Ban đầu, xác suất lấy ngẫu nhiên được viên bi trắng là $%s$' % (fmt_frac(p_trang_dau_sai))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Ban đầu trong bình có $%s$ viên bi trắng trên tổng số $%s$ viên bi nên xác suất lấy được viên bi trắng là $\\dfrac{%s}{%s} = %s$.' % (trang_dau, tong_dau, trang_dau, tong_dau, fmt_frac(p_trang_dau))
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
