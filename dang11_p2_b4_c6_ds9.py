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


def bt_dang11_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            v_nuoc = random.choice([2, 3, 4, 5])
            v_thuc = random.randint(15, 30)
            if v_thuc <= v_nuoc + 5:
                continue
            v_xuoi = v_thuc + v_nuoc
            v_nguoc = v_thuc - v_nuoc
            t_chay = random.choice([4, 5, 6])
            num = t_chay * (v_thuc**2 - v_nuoc**2)
            if num % (2 * v_thuc) == 0:
                s_ab = num // (2 * v_thuc)
                break

        phut_nghi = random.choice([30, 40, 45])
        a_eq = t_chay
        b_eq = 2 * s_ab
        c_eq = t_chay * (v_nuoc**2)
        g = math.gcd(math.gcd(a_eq, b_eq), c_eq)
        a_s, b_s, c_s = a_eq // g, b_eq // g, c_eq // g

        noidungcauhoi = ('''Một ca nô du lịch xuất phát từ bến sông A xuôi dòng đến bến sông B cách nhau $%s\\text{ km}$, nghỉ lại bến B trong $%s\\text{ phút}$ để khách tham quan rồi quay ngược dòng trở về bến A. Tổng thời gian kể từ lúc xuất phát đến khi về tới bến A là $%s\\text{ giờ } %s\\text{ phút}$. Biết vận tốc dòng nước là $%s\\text{ km/h}$. Gọi $x\\text{ (km/h)}$ là vận tốc thực của ca nô.''' % (fmt_num(s_ab), fmt_num(phut_nghi), fmt_num(t_chay), fmt_num(phut_nghi), fmt_num(v_nuoc)))

        nb_da_1_d = '\\True Điều kiện xác định và điều kiện thực tế của ẩn $x$ là $x > %s$' % (fmt_num(v_nuoc))
        nb_da_1_s = 'Điều kiện xác định và điều kiện thực tế của ẩn $x$ là $x > 0$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Để ca nô có thể chạy ngược dòng nước có vận tốc $%s\\text{ km/h}$ thì vận tốc thực của ca nô phải thoả mãn $x > %s$.''' % (fmt_num(v_nuoc), fmt_num(v_nuoc)))

        th_da_1_d = '\\True Tổng thời gian ca nô thực sự chạy trên sông (không tính thời gian nghỉ) là $%s\\text{ giờ}$' % (fmt_num(t_chay))
        th_da_1_s = 'Tổng thời gian ca nô thực sự chạy trên sông (không tính thời gian nghỉ) là $%s\\text{ giờ}$' % (fmt_num(t_chay + 1))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Tổng thời gian cả hành trình là $%s\\text{ giờ } %s\\text{ phút}$, trừ đi $%s\\text{ phút}$ nghỉ tại bến B nên thời gian ca nô thực sự chạy trên sông là $%s\\text{ giờ}$.''' % (fmt_num(t_chay), fmt_num(phut_nghi), fmt_num(phut_nghi), fmt_num(t_chay)))

        a_str = '' if a_s == 1 else fmt_num(a_s)
        vd_da_1_d = '\\True Phương trình biểu thị bài toán sau khi khử mẫu và rút gọn là $%sx^2 - %sx - %s = 0$' % (a_str, fmt_num(b_s), fmt_num(c_s))
        vd_da_1_s = 'Phương trình biểu thị bài toán sau khi khử mẫu và rút gọn là $%sx^2 + %sx - %s = 0$' % (a_str, fmt_num(b_s), fmt_num(c_s))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Vận tốc xuôi dòng là $x + %s\\text{ (km/h)}$, vận tốc ngược dòng là $x - %s\\text{ (km/h)}$. \\\\ Ta có phương trình: $\\frac{%s}{x + %s} + \\frac{%s}{x - %s} = %s$. \\\\ Quy đồng khử mẫu: $%s(x - %s) + %s(x + %s) = %s(x^2 - %s) \\Leftrightarrow %sx^2 - %sx - %s = 0 \\Leftrightarrow %sx^2 - %sx - %s = 0$.''' % (fmt_num(v_nuoc), fmt_num(v_nuoc), fmt_num(s_ab), fmt_num(v_nuoc), fmt_num(s_ab), fmt_num(v_nuoc), fmt_num(t_chay), fmt_num(s_ab), fmt_num(v_nuoc), fmt_num(s_ab), fmt_num(v_nuoc), fmt_num(t_chay), fmt_num(v_nuoc**2), fmt_num(a_eq), fmt_num(b_eq), fmt_num(c_eq), a_str, fmt_num(b_s), fmt_num(c_s)))

        vdc_da_1_d = '\\True Vận tốc của ca nô khi đi ngược dòng từ B về A là $%s\\text{ km/h}$' % (fmt_num(v_nguoc))
        vdc_da_1_s = 'Vận tốc của ca nô khi đi ngược dòng từ B về A là $%s\\text{ km/h}$' % (fmt_num(v_thuc))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        b_half = b_s // 2
        delta_p = b_half**2 + a_s * c_s
        sqrt_dp = int(math.isqrt(delta_p))
        loigiai_vdc_1 = ('''Giải phương trình $%sx^2 - %sx - %s = 0$: \\\\ Ta có $\\Delta' = (-%s)^2 - %s \\cdot (-%s) = %s$, $\\sqrt{\\Delta'} = %s$. \\\\ Nghiệm của phương trình là $x_1 = \\frac{%s + %s}{%s} = %s$ (thoả mãn) và $x_2 = \\frac{%s - %s}{%s} < 0$ (loại). \\\\ Vậy vận tốc thực của ca nô là $%s\\text{ km/h}$, suy ra vận tốc ngược dòng là $%s - %s = %s\\text{ km/h}$.''' % (a_str, fmt_num(b_s), fmt_num(c_s), fmt_num(b_half), fmt_num(a_s), fmt_num(c_s), fmt_num(delta_p), fmt_num(sqrt_dp), fmt_num(b_half), fmt_num(sqrt_dp), fmt_num(a_s), fmt_num(v_thuc), fmt_num(b_half), fmt_num(sqrt_dp), fmt_num(a_s), fmt_num(v_thuc), fmt_num(v_thuc), fmt_num(v_nuoc), fmt_num(v_nguoc)))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb)
    combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th)
    combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd)
    combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc)

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
