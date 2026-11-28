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

def bt_dang2_p2_b3_c8_ds8(self):
    # Dạng 2: Thống kê thời gian chờ xe buýt (Bảng tần số ghép nhóm)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([50, 60, 80, 100])
        while True:
            f0 = random.randint(5, n // 5)
            f1 = random.randint(15, n // 2)
            f2 = random.randint(10, n // 3)
            f3 = n - f0 - f1 - f2
            if f3 >= 4 and (f0 * 100) % n == 0 and (f2 + f3) * 10 % n == 0 and (f1 + f2 + f3) % f0 != 0:
                break
        pct_a = (f0 * 100) // n
        pct_a_sai = pct_a + 5
        frac_b = fmt_frac(f1 + f2, n)
        frac_b_sai = fmt_frac(f1, n)
        dec_c = fmt_dec(Fraction(f2 + f3, n), 2)
        dec_c_sai = fmt_dec(Fraction(f2, n), 2)
        so_buoi_tu3 = f1 + f2 + f3
        ti_so_d = fmt_dec(Fraction(so_buoi_tu3, f0), 2)

        bang_tex = (
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|}\n'
            '\\hline\n'
            '\\textbf{Thời gian chờ (phút)} & Dưới $3$ & Từ $3$ đến dưới $6$ & Từ $6$ đến dưới $9$ & Từ $9$ trở lên \\\\ \n'
            '\\hline\n'
            '\\textbf{Số buổi} & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (f0, f1, f2, f3)
        )

        noidungcauhoi = (
            'Bạn Minh ghi lại thời gian chờ xe buýt tuyến số $08$ của mình trong $%s$ buổi sáng đi học ở bảng sau:%s'
            'Xét tính đúng sai của các mệnh đề sau:'
            % (n, bang_tex)
        )

        nb_da_1_d = '\\True Xác suất thực nghiệm để Minh chờ xe buýt dưới $3$ phút là $%s\\%%$' % pct_a
        nb_da_1_s = 'Xác suất thực nghiệm để Minh chờ xe buýt dưới $3$ phút là $%s\\%%$' % pct_a_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất thực nghiệm để Minh chờ xe buýt từ $3$ phút đến dưới $9$ phút là $%s$' % frac_b
        th_da_1_s = 'Xác suất thực nghiệm để Minh chờ xe buýt từ $3$ phút đến dưới $9$ phút là $%s$' % frac_b_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất thực nghiệm để Minh chờ xe buýt không dưới $6$ phút là $%s$' % dec_c
        vd_da_1_s = 'Xác suất thực nghiệm để Minh chờ xe buýt không dưới $6$ phút là $%s$' % dec_c_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Khả năng Minh phải chờ xe buýt từ $3$ phút trở lên cao gấp khoảng $%s$ lần khả năng chờ dưới $3$ phút' % ti_so_d
        vdc_da_1_s = 'Khả năng Minh phải chờ xe buýt từ $3$ phút trở lên cao gấp đúng $%s$ lần khả năng chờ dưới $3$ phút' % (so_buoi_tu3 // f0)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Trong $%s$ buổi sáng, có $%s$ buổi Minh chờ xe buýt dưới $3$ phút.\\'
            'Xác suất thực nghiệm của biến cố này là $\\dfrac{%s}{%s} = %s\\%%$.'
            % (n, f0, f0, n, pct_a)
        )
        loigiai_th_1 = (
            'Số buổi Minh chờ xe buýt từ $3$ phút đến dưới $9$ phút là $%s + %s = %s$ (buổi).\\'
            'Xác suất thực nghiệm của biến cố đó là $\\dfrac{%s}{%s} = %s$.'
            % (f1, f2, f1 + f2, f1 + f2, n, frac_b)
        )
        loigiai_vd_1 = (
            'Chờ xe buýt không dưới $6$ phút tức là chờ từ $6$ phút trở lên, gồm $%s + %s = %s$ (buổi).\\'
            'Xác suất thực nghiệm tương ứng là $\\dfrac{%s}{%s} = %s$.'
            % (f2, f3, f2 + f3, f2 + f3, n, dec_c)
        )
        loigiai_vdc_1 = (
            'Số buổi chờ từ $3$ phút trở lên là $%s + %s + %s = %s$ (buổi), xác suất thực nghiệm là $\\dfrac{%s}{%s}$.\\'
            'Tỉ số giữa hai xác suất thực nghiệm là $\\dfrac{%s}{%s} : \\dfrac{%s}{%s} = \\dfrac{%s}{%s} \\approx %s$.'
            % (f1, f2, f3, so_buoi_tu3, so_buoi_tu3, n, so_buoi_tu3, n, f0, n, so_buoi_tu3, f0, ti_so_d)
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
