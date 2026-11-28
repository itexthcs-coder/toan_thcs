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


def bt_dang7_p2_b2_c8_ds8(self):
    # Dạng 7: Bốc thăm trúng thưởng tại siêu thị (Biến cố hợp và biến cố đối)
    tong = 100
    g_db = 1
    g_nhat = random.choice([3, 4, 5])
    g_nhi = random.choice([12, 15, 16])
    g_ba = random.choice([25, 30, 32])
    may_man = tong - (g_db + g_nhat + g_nhi + g_ba)

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) rectangle (6.6,1.4);\n'
        '\\node at (3.3,0.7) {Hòm $100$ phiếu: ĐB ($1$), Nhất ($%s$), Nhì ($%s$), Ba ($%s$), KMM};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    ) % (g_nhat, g_nhi, g_ba)

    noidungcauhoi = (
        'Nhân dịp khai trương, một cửa hàng chuẩn bị $100$ phiếu bốc thăm giống nhau gồm: $1$ giải Đặc biệt, $%s$ giải Nhất, $%s$ giải Nhì, $%s$ giải Ba và còn lại là phiếu Chúc bạn may mắn lần sau. Khách hàng đầu tiên bốc ngẫu nhiên $1$ phiếu. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (g_nhat, g_nhi, g_ba, tikz_hinh)
    )

    nb_da_1_d = '\\True Số phiếu Chúc bạn may mắn lần sau là $%s$ phiếu' % (may_man)
    nb_da_1_s = 'Số phiếu Chúc bạn may mắn lần sau là $%s$ phiếu' % (may_man + 5)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Số phiếu Chúc bạn may mắn lần sau là $100 - (1 + %s + %s + %s) = %s$ (phiếu).' % (g_nhat, g_nhi, g_ba, may_man)
    list_nb_2 = [loigiai_nb_1]

    so_trung = g_db + g_nhat + g_nhi + g_ba
    p_trung = Fraction(so_trung, 100)
    p_trung_sai = Fraction(so_trung - 1, 100)
    th_da_1_d = '\\True Xác suất để khách hàng trúng giải (từ giải Ba trở lên) bằng $%s$' % (fmt_frac(p_trung))
    th_da_1_s = 'Xác suất để khách hàng trúng giải (từ giải Ba trở lên) bằng $%s$' % (fmt_frac(p_trung_sai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Tổng số phiếu trúng giải là $1 + %s + %s + %s = %s$ (phiếu). \\ Vậy xác suất để khách hàng trúng giải là $\\dfrac{%s}{100} = %s$.' % (g_nhat, g_nhi, g_ba, so_trung, so_trung, fmt_frac(p_trung))
    list_th_2 = [loigiai_th_1]

    p_12 = Fraction(g_nhat + g_nhi, 100)
    p_12_sai = Fraction(g_nhat + g_nhi + 1, 100)
    vd_da_1_d = '\\True Xác suất để khách hàng trúng giải Nhất hoặc giải Nhì bằng $%s$' % (fmt_frac(p_12))
    vd_da_1_s = 'Xác suất để khách hàng trúng giải Nhất hoặc giải Nhì bằng $%s$' % (fmt_frac(p_12_sai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Số phiếu trúng giải Nhất hoặc giải Nhì là $%s + %s = %s$ (phiếu). \\ Vậy xác suất cần tìm là $\\dfrac{%s}{100} = %s$.' % (g_nhat, g_nhi, g_nhat + g_nhi, g_nhat + g_nhi, fmt_frac(p_12))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Xác suất để khách hàng không trúng giải Đặc biệt là $\\dfrac{99}{100}$'
    vdc_da_1_s = 'Xác suất để khách hàng không trúng giải Đặc biệt là $\\dfrac{1}{100}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Vì chỉ có $1$ phiếu giải Đặc biệt nên có $100 - 1 = 99$ phiếu không phải giải Đặc biệt. \\ Vậy xác suất để khách hàng không trúng giải Đặc biệt là $\\dfrac{99}{100}$.'
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
