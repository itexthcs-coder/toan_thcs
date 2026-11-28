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

def bt_dang1_p2_b3_c8_ds8(self):
    # Dạng 1: Thống kê số lượng sách mượn tại thư viện trường (Bảng tần số rời rạc)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        vals = [10, 12, 15, 18, 20, 25]
        while True:
            freqs = [random.randint(3, 15) for _ in range(6)]
            n = sum(freqs)
            if n in [40, 50, 60, 80, 100]:
                break
        f0, f1, f2, f3, f4, f5 = freqs
        p_a = fmt_dec(Fraction(f2, n), 4)
        p_a_sai = fmt_dec(Fraction(f2 + 2, n), 4)
        so_ngay_b = f3 + f4 + f5
        so_ngay_b_sai = f2 + f3 + f4 + f5
        p_c_tex = fmt_frac(f0 + f1, n)
        p_c_sai_tex = fmt_frac(f0 + f1 + f2, n)
        p_d_val = Fraction(so_ngay_b, n)
        nguong_d = Decimal(str(float(p_d_val) - 0.03)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        nguong_d_str = fmt_dec(nguong_d, 2)

        bang_tex = (
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|c|c|}\n'
            '\\hline\n'
            '\\textbf{Số lượt mượn/ngày} & $10$ & $12$ & $15$ & $18$ & $20$ & $25$ \\\\ \n'
            '\\hline\n'
            '\\textbf{Số ngày} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (f0, f1, f2, f3, f4, f5)
        )

        noidungcauhoi = (
            'Thư viện trường THCS Bình Minh theo dõi số lượt học sinh mượn sách tham khảo trong $%s$ ngày hoạt động và ghi lại kết quả ở bảng sau:%s'
            'Xét tính đúng sai của các khẳng định sau:'
            % (n, bang_tex)
        )

        nb_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Trong một ngày có đúng $15$ lượt mượn sách" là $%s$' % p_a
        nb_da_1_s = 'Xác suất thực nghiệm của biến cố "Trong một ngày có đúng $15$ lượt mượn sách" là $%s$' % p_a_sai
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Có $%s$ ngày thư viện ghi nhận số lượt mượn sách nhiều hơn $15$ lượt' % so_ngay_b
        th_da_1_s = 'Có $%s$ ngày thư viện ghi nhận số lượt mượn sách nhiều hơn $15$ lượt' % so_ngay_b_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Trong một ngày có không quá $12$ lượt mượn sách" là $%s$' % p_c_tex
        vd_da_1_s = 'Xác suất thực nghiệm của biến cố "Trong một ngày có không quá $12$ lượt mượn sách" là $%s$' % p_c_sai_tex
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Xác suất thực nghiệm của biến cố "Trong một ngày có ít nhất $18$ lượt mượn sách" lớn hơn $%s$' % nguong_d_str
        vdc_da_1_s = 'Xác suất thực nghiệm của biến cố "Trong một ngày có ít nhất $18$ lượt mượn sách" nhỏ hơn $%s$' % nguong_d_str
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Trong $%s$ ngày theo dõi, có $%s$ ngày có đúng $15$ lượt mượn sách.\\'
            'Vậy xác suất thực nghiệm của biến cố "Trong một ngày có đúng $15$ lượt mượn sách" là $\\dfrac{%s}{%s} = %s$.'
            % (n, f2, f2, n, p_a)
        )
        loigiai_th_1 = (
            'Số lượt mượn sách nhiều hơn $15$ lượt ứng với các giá trị $18; 20; 25$.\\'
            'Do đó, số ngày ghi nhận nhiều hơn $15$ lượt mượn sách là $%s + %s + %s = %s$ (ngày).'
            % (f3, f4, f5, so_ngay_b)
        )
        loigiai_vd_1 = (
            'Số ngày có không quá $12$ lượt mượn sách (gồm $10$ lượt và $12$ lượt) là $%s + %s = %s$ (ngày).\\'
            'Xác suất thực nghiệm của biến cố đó là $\\dfrac{%s}{%s} = %s$.'
            % (f0, f1, f0 + f1, f0 + f1, n, p_c_tex)
        )
        loigiai_vdc_1 = (
            'Số ngày có ít nhất $18$ lượt mượn sách (gồm $18; 20; 25$ lượt) là $%s + %s + %s = %s$ (ngày).\\'
            'Xác suất thực nghiệm của biến cố đó là $\\dfrac{%s}{%s} = %s > %s$.'
            % (f3, f4, f5, so_ngay_b, so_ngay_b, n, fmt_dec(p_d_val, 4), nguong_d_str)
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
