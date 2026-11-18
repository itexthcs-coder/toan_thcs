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


def bt_dang17_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (3, 8, 200, 80),
            (4, 6, 150, 100),
            (5, 8, 160, 100),
            (2, 5, 250, 120)
        ]
        d1, d2, v1, v2 = random.choice(bo_so)
        m1 = d1 * v1
        m2 = d2 * v2
        dv = v1 - v2
        dd = d2 - d1

        a_eq = dv
        b_eq = dv * dd + m2 - m1
        c_eq = m1 * dd
        g = math.gcd(math.gcd(abs(a_eq), abs(b_eq)), abs(c_eq))
        a_s, b_s, c_s = a_eq // g, b_eq // g, c_eq // g
        a_str = '' if a_s == 1 else fmt_num(a_s)

        noidungcauhoi = ('''Trong phòng thí nghiệm luyện kim có hai thỏi hợp kim khác loại: thỏi thứ nhất nặng $%s\\text{ g}$, thỏi thứ hai nặng $%s\\text{ g}$. Biết rằng thể tích của thỏi thứ nhất lớn hơn thể tích của thỏi thứ hai là $%s\\text{ cm}^3$, còn khối lượng riêng của thỏi thứ nhất nhỏ hơn khối lượng riêng của thỏi thứ hai là $%s\\text{ g/cm}^3$. Gọi $x\\text{ (g/cm}^3\\text{)}$ là khối lượng riêng của thỏi thứ nhất ($x > 0$).''' % (fmt_num(m1), fmt_num(m2), fmt_num(dv), fmt_num(dd)))

        nb_da_1_d = '\\True Thể tích của thỏi hợp kim thứ hai là $\\frac{%s}{x + %s}\\text{ (cm}^3\\text{)}$' % (fmt_num(m2), fmt_num(dd))
        nb_da_1_s = 'Thể tích của thỏi hợp kim thứ hai là $\\frac{%s}{x - %s}\\text{ (cm}^3\\text{)}$' % (fmt_num(m2), fmt_num(dd))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Khối lượng riêng của thỏi thứ hai là $x + %s\\text{ (g/cm}^3\\text{)}$ nên thể tích của thỏi thứ hai là $\\frac{%s}{x + %s}\\text{ (cm}^3\\text{)}$.''' % (fmt_num(dd), fmt_num(m2), fmt_num(dd)))

        th_da_1_d = '\\True Phương trình lập được từ mối quan hệ thể tích hai thỏi là $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$' % (fmt_num(m1), fmt_num(m2), fmt_num(dd), fmt_num(dv))
        th_da_1_s = 'Phương trình lập được từ mối quan hệ thể tích hai thỏi là $\\frac{%s}{x + %s} - \\frac{%s}{x} = %s$' % (fmt_num(m2), fmt_num(dd), fmt_num(m1), fmt_num(dv))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thể tích thỏi thứ nhất là $\\frac{%s}{x}\\text{ (cm}^3\\text{)}$, thể tích thỏi thứ hai là $\\frac{%s}{x + %s}\\text{ (cm}^3\\text{)}$. \\\\ Ta có phương trình: $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$.''' % (fmt_num(m1), fmt_num(m2), fmt_num(dd), fmt_num(m1), fmt_num(m2), fmt_num(dd), fmt_num(dv)))

        vd_da_1_d = '\\True Sau khi quy đồng khử mẫu và thu gọn, ta được phương trình $%sx^2 + %sx - %s = 0$' % (a_str, fmt_num(b_s), fmt_num(c_s))
        vd_da_1_s = 'Sau khi quy đồng khử mẫu và thu gọn, ta được phương trình $%sx^2 - %sx - %s = 0$' % (a_str, fmt_num(b_s), fmt_num(c_s))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Nhân cả hai vế của phương trình $\\frac{%s}{x} - \\frac{%s}{x + %s} = %s$ với $x(x + %s)$: \\\\ $%s(x + %s) - %sx = %sx(x + %s) \\Leftrightarrow %sx^2 + %sx - %s = 0 \\Leftrightarrow %sx^2 + %sx - %s = 0$.''' % (fmt_num(m1), fmt_num(m2), fmt_num(dd), fmt_num(dv), fmt_num(dd), fmt_num(m1), fmt_num(dd), fmt_num(m2), fmt_num(dv), fmt_num(dd), fmt_num(a_eq), fmt_num(b_eq), fmt_num(c_eq), a_str, fmt_num(b_s), fmt_num(c_s)))

        vdc_da_1_d = '\\True Khối lượng riêng của thỏi hợp kim thứ hai là $%s\\text{ g/cm}^3$' % (fmt_num(d2))
        vdc_da_1_s = 'Khối lượng riêng của thỏi hợp kim thứ hai là $%s\\text{ g/cm}^3$' % (fmt_num(d1))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Giải phương trình bậc hai $%sx^2 + %sx - %s = 0$, ta tìm được nghiệm dương duy nhất là $x = %s\\text{ (g/cm}^3\\text{)}$. \\\\ Vậy khối lượng riêng của thỏi thứ nhất là $%s\\text{ g/cm}^3$ và của thỏi thứ hai là $%s + %s = %s\\text{ g/cm}^3$.''' % (a_str, fmt_num(b_s), fmt_num(c_s), fmt_num(d1), fmt_num(d1), fmt_num(d1), fmt_num(dd), fmt_num(d2)))

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
