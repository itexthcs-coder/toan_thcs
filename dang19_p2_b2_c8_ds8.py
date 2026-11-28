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


def bt_dang19_p2_b2_c8_ds8(self):
    # Dạng 19: Tích hợp Hình học phẳng – Đếm hình tam giác trên hình vẽ
    n_base = random.choice([4, 5])
    tong_tg = n_base * (n_base - 1) // 2

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (M) at (2.5,2.5);\n'
        '\\coordinate (A) at (0.5,0);\n'
        '\\coordinate (B) at (1.8,0);\n'
        '\\coordinate (C) at (3.2,0);\n'
        '\\coordinate (D) at (4.5,0);\n'
        '\\draw[line width=1pt] (0,0)--(5,0) (M)--(A) (M)--(B) (M)--(C) (M)--(D);\n'
        '\\fill (M) circle (1pt) node[above] {$M$};\n'
        '\\fill (A) circle (1pt) node[below] {$A$};\n'
        '\\fill (B) circle (1pt) node[below] {$B$};\n'
        '\\fill (C) circle (1pt) node[below] {$C$};\n'
        '\\fill (D) circle (1pt) node[below] {$D$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    if n_base == 4:
        pts_str = 'A, B, C, D'
        giai_tong = 'Các tam giác được tạo thành gồm: $MAB, MAC, MAD, MBC, MBD, MCD$ (tổng cộng $6$ tam giác).'
        so_ma = 3
        giai_ma = 'Các tam giác chứa cạnh $MA$ là $MAB, MAC, MAD$ (gồm $3$ tam giác).'
        so_no_d = 3
        giai_no_d = 'Các tam giác không chứa điểm $D$ là $MAB, MAC, MBC$ (gồm $3$ tam giác).'
    else:
        pts_str = 'A, B, C, D, E'
        giai_tong = 'Số đoạn thẳng đáy chọn từ $5$ điểm thẳng hàng là $\\dfrac{5 \\cdot 4}{2} = 10$ đoạn, tương ứng tạo thành $10$ tam giác có đỉnh $M$.'
        so_ma = 4
        giai_ma = 'Các tam giác chứa cạnh $MA$ là $MAB, MAC, MAD, MAE$ (gồm $4$ tam giác).'
        so_no_d = 6
        giai_no_d = 'Bỏ điểm $D$, còn $4$ điểm trên đường thẳng $d$ tạo thành $\\dfrac{4 \\cdot 3}{2} = 6$ tam giác không chứa điểm $D$.'

    noidungcauhoi = (
        'Trên một đường thẳng $d$ lấy $%s$ điểm phân biệt $%s$ và lấy một điểm $M$ nằm ngoài đường thẳng $d$. Nối $M$ với từng điểm trên đường thẳng $d$. Chọn ngẫu nhiên một tam giác có các đỉnh là $3$ trong các điểm đã cho. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (n_base, pts_str, tikz_hinh)
    )

    nb_da_1_d = '\\True Có tất cả $%s$ tam giác được tạo thành và khả năng chọn mỗi tam giác là như nhau' % (tong_tg)
    nb_da_1_s = 'Có tất cả $%s$ tam giác được tạo thành và khả năng chọn mỗi tam giác là như nhau' % (tong_tg + 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = giai_tong
    list_nb_2 = [loigiai_nb_1]

    p_ma = Fraction(so_ma, tong_tg)
    p_ma_sai = Fraction(1, tong_tg)
    th_da_1_d = '\\True Xác suất để tam giác được chọn có chứa cạnh $MA$ bằng $%s$' % (fmt_frac(p_ma))
    th_da_1_s = 'Xác suất để tam giác được chọn có chứa cạnh $MA$ bằng $%s$' % (fmt_frac(p_ma_sai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = '%s \\ Vậy xác suất cần tìm là $\\dfrac{%s}{%s} = %s$.' % (giai_ma, so_ma, tong_tg, fmt_frac(p_ma))
    list_th_2 = [loigiai_th_1]

    p_bc = Fraction(1, tong_tg)
    p_bc_sai = Fraction(2, tong_tg)
    vd_da_1_d = '\\True Xác suất để tam giác được chọn có đáy là đoạn thẳng $BC$ bằng $%s$' % (fmt_frac(p_bc))
    vd_da_1_s = 'Xác suất để tam giác được chọn có đáy là đoạn thẳng $BC$ bằng $%s$' % (fmt_frac(p_bc_sai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Chỉ có duy nhất một tam giác có đáy là đoạn thẳng $BC$, đó là $\\triangle MBC$. \\ Vậy xác suất cần tìm là $%s$.' % (fmt_frac(p_bc))
    list_vd_2 = [loigiai_vd_1]

    p_no_d = Fraction(so_no_d, tong_tg)
    p_no_d_sai = Fraction(so_no_d + 1, tong_tg)
    vdc_da_1_d = '\\True Xác suất để tam giác được chọn không chứa điểm $D$ bằng $%s$' % (fmt_frac(p_no_d))
    vdc_da_1_s = 'Xác suất để tam giác được chọn không chứa điểm $D$ bằng $%s$' % (fmt_frac(p_no_d_sai))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = '%s \\ Vậy xác suất cần tìm là $\\dfrac{%s}{%s} = %s$.' % (giai_no_d, so_no_d, tong_tg, fmt_frac(p_no_d))
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
