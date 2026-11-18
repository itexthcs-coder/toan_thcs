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


def bt_dang1_p2_b4_c6_ds9(self):
    def fmt_num(val):
        if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
            return str(int(val))
        return str(val).replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        w = random.randint(10, 25)
        diff_dim = random.randint(4, 15)
        l = w + diff_dim
        area = w * l
        chu_vi = 2 * (w + l)

        noidungcauhoi = ('''Một trường THCS dự định cải tạo một mảnh đất hình chữ nhật để làm vườn sinh học có diện tích $%s\\text{ m}^2$. Theo thiết kế, chiều dài của khu vườn lớn hơn chiều rộng là $%s\\text{ m}$. Gọi $x\\text{ (m)}$ là chiều rộng của khu vườn.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4.5,0);
\\coordinate (C) at (4.5,2.5);
\\coordinate (D) at (0,2.5);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\node at (2.25,-0.35) {$x + %s\\text{ (m)}$};
\\node[left] at (-0.1,1.25) {$x\\text{ (m)}$};
\\end{tikzpicture}
\\end{center}''' % (fmt_num(area), fmt_num(diff_dim), fmt_num(diff_dim)))

        nb_da_1_d = '\\True Điều kiện thích hợp của ẩn $x$ là $x > 0$'
        nb_da_1_s = 'Điều kiện thích hợp của ẩn $x$ là $x > %s$' % (fmt_num(diff_dim))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì $x$ là chiều rộng của mảnh đất hình chữ nhật nên điều kiện thích hợp của ẩn $x$ là $x > 0$.''')

        th_da_1_d = '\\True Chiều dài của khu vườn được biểu thị theo $x$ là $x + %s\\text{ (m)}$' % (fmt_num(diff_dim))
        th_da_1_s = 'Chiều dài của khu vườn được biểu thị theo $x$ là $x - %s\\text{ (m)}$' % (fmt_num(diff_dim))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Do chiều dài của khu vườn lớn hơn chiều rộng là $%s\\text{ m}$ nên chiều dài của khu vườn là $x + %s\\text{ (m)}$.''' % (fmt_num(diff_dim), fmt_num(diff_dim)))

        vd_da_1_d = '\\True Phương trình lập được từ giả thiết của bài toán là $x^2 + %sx - %s = 0$' % (fmt_num(diff_dim), fmt_num(area))
        vd_da_1_s = 'Phương trình lập được từ giả thiết của bài toán là $x^2 - %sx - %s = 0$' % (fmt_num(diff_dim), fmt_num(area))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Diện tích khu vườn hình chữ nhật bằng $%s\\text{ m}^2$ nên ta có phương trình: $x(x + %s) = %s$ hay $x^2 + %sx - %s = 0$.''' % (fmt_num(area), fmt_num(diff_dim), fmt_num(area), fmt_num(diff_dim), fmt_num(area)))

        vdc_da_1_d = '\\True Chu vi của vườn sinh học sau khi hoàn thành là $%s\\text{ m}$' % (fmt_num(chu_vi))
        vdc_da_1_s = 'Chu vi của vườn sinh học sau khi hoàn thành là $%s\\text{ m}$' % (fmt_num(chu_vi + 10))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        delta = diff_dim**2 + 4 * area
        sqrt_delta = int(math.isqrt(delta))
        loigiai_vdc_1 = ('''Giải phương trình $x^2 + %sx - %s = 0$: \\\\ Ta có $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\ Phương trình có hai nghiệm phân biệt: $x_1 = \\frac{-%s - %s}{2} = -%s$ (loại); $x_2 = \\frac{-%s + %s}{2} = %s$ (thoả mãn điều kiện). \\\\ Vậy chiều rộng khu vườn là $%s\\text{ m}$, chiều dài là $%s + %s = %s\\text{ m}$. \\\\ Chu vi của vườn sinh học là $2 \\cdot (%s + %s) = %s\\text{ m}$.''' % (fmt_num(diff_dim), fmt_num(area), fmt_num(diff_dim), fmt_num(area), fmt_num(delta), fmt_num(sqrt_delta), fmt_num(diff_dim), fmt_num(sqrt_delta), fmt_num(l), fmt_num(diff_dim), fmt_num(sqrt_delta), fmt_num(w), fmt_num(w), fmt_num(w), fmt_num(diff_dim), fmt_num(l), fmt_num(w), fmt_num(l), fmt_num(chu_vi)))

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
