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

def fmt_dec(val, places=2):
    d = Decimal(str(val)).quantize(Decimal('1.' + '0'*places) if places > 0 else Decimal('1'), rounding=ROUND_HALF_UP)
    s = format(d, 'f')
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')

def fmt_frac(num, den):
    f = Fraction(num, den)
    if f.denominator == 1:
        return str(f.numerator)
    return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang6_p2_b3_c8_ds8(self):
    # Dạng 6: Trò chơi vòng quay may mắn (Kết hợp Số học và hình vẽ TikZ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([20, 24, 30])
        if n == 20:
            d1, d2 = 4, 5
            boichinh = [20]
            uoc_list = [1, 2, 4, 5, 10, 20]
            snt_list = [2, 3, 5, 7, 11, 13, 17, 19]
            scp_list = [1, 4, 9, 16]
        elif n == 24:
            d1, d2 = 3, 4
            boichinh = [12, 24]
            uoc_list = [1, 2, 3, 4, 6, 8, 12, 24]
            snt_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
            scp_list = [1, 4, 9, 16]
        else:
            d1, d2 = 3, 5
            boichinh = [15, 30]
            uoc_list = [1, 2, 3, 5, 6, 10, 15, 30]
            snt_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            scp_list = [1, 4, 9, 16, 25]

        p_a = fmt_frac(len(boichinh), n)
        p_a_sai = fmt_frac(len(boichinh) + 1, n)
        p_b = fmt_frac(len(uoc_list), n)
        p_b_sai = fmt_frac(len(uoc_list) - 1, n)
        p_c = fmt_frac(len(snt_list), n)
        p_c_sai = fmt_frac(len(snt_list) + 1, n)
        p_d = fmt_frac(len(scp_list), n)
        p_d_sai = fmt_frac(len(scp_list) + 1, n)

        tikz_tex = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) circle (1.8cm);\n'
            '\\foreach \\i in {1,...,12} {\n'
            '  \\draw[line width=1pt] (0,0) -- ({30*\\i}:1.8cm);\n'
            '}\n'
            '\\fill (0,0) circle (1pt);\n'
            '\\draw[line width=1pt, ->] (0,2.3) -- (0,1.85);\n'
            '\\node[above] at (0,2.3) {Kim chỉ};\n'
            '\\node[below] at (0,-1.95) {Vòng quay đánh số từ $1$ đến $%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % n
        )

        noidungcauhoi = (
            'Một vòng quay được chia thành $%s$ hình quạt bằng nhau, đánh số từ $1$ đến $%s$. Quay vòng quay một lần và quan sát số ở ô kim chỉ vào.%s'
            'Xét tính đúng sai của các mệnh đề sau:'
            % (n, n, tikz_tex)
        )

        nb_da_1_d = '\\True Xác suất của biến cố "Kim chỉ vào ô ghi số chia hết cho cả $%s$ và $%s$" là $%s$' % (d1, d2, p_a)
        nb_da_1_s = 'Xác suất của biến cố "Kim chỉ vào ô ghi số chia hết cho cả $%s$ và $%s$" là $%s$' % (d1, d2, p_a_sai)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất của biến cố "Kim chỉ vào ô ghi số là ước của $%s$" là $%s$' % (n, p_b)
        th_da_1_s = 'Xác suất của biến cố "Kim chỉ vào ô ghi số là ước của $%s$" là $%s$' % (n, p_b_sai)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất của biến cố "Kim chỉ vào ô ghi số nguyên tố" bằng $%s$' % p_c
        vd_da_1_s = 'Xác suất của biến cố "Kim chỉ vào ô ghi số nguyên tố" bằng $%s$' % p_c_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Xác suất của biến cố "Kim chỉ vào ô ghi số chính phương" là $%s$' % p_d
        vdc_da_1_s = 'Xác suất của biến cố "Kim chỉ vào ô ghi số chính phương" là $%s$' % p_d_sai
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Các số từ $1$ đến $%s$ chia hết cho cả $%s$ và $%s$ là: $\\{%s\\}$ (gồm $%s$ số).\\'
            'Xác suất của biến cố này là $\\dfrac{%s}{%s} = %s$.'
            % (n, d1, d2, '; '.join(map(str, boichinh)), len(boichinh), len(boichinh), n, p_a)
        )
        loigiai_th_1 = (
            'Tập hợp các ước dương của $%s$ là $\\{%s\\}$ (gồm $%s$ số).\\'
            'Xác suất của biến cố đó là $\\dfrac{%s}{%s} = %s$.'
            % (n, '; '.join(map(str, uoc_list)), len(uoc_list), len(uoc_list), n, p_b)
        )
        loigiai_vd_1 = (
            'Các số nguyên tố từ $1$ đến $%s$ là $\\{%s\\}$ (gồm $%s$ số).\\'
            'Xác suất của biến cố đó là $\\dfrac{%s}{%s} = %s$.'
            % (n, '; '.join(map(str, snt_list)), len(snt_list), len(snt_list), n, p_c)
        )
        loigiai_vdc_1 = (
            'Các số chính phương từ $1$ đến $%s$ là $\\{%s\\}$ (gồm $%s$ số).\\'
            'Xác suất của biến cố đó là $\\dfrac{%s}{%s} = %s$.'
            % (n, '; '.join(map(str, scp_list)), len(scp_list), len(scp_list), n, p_d)
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
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
