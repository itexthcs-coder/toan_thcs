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


def bt_dang20_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_chuan = [
            (24, 16, 4),
            (30, 20, 5),
            (18, 12, 3),
            (12, 8, 2)
        ]
        dai_ho, rong_ho, x_val = random.choice(bo_chuan)

        s_ho = dai_ho * rong_ho
        s_tong = 2 * s_ho
        b_eq = 2 * (dai_ho + rong_ho)
        c_eq = s_ho

        noidungcauhoi = ('''Một khu nghỉ dưỡng xây dựng một bể bơi hình chữ nhật có kích thước dài $%s\\text{ m}$, rộng $%s\\text{ m}$. Xung quanh bể bơi, người ta lát gạch làm một lối đi có bề rộng không đổi là $x\\text{ (m)}$ ($x > 0$). Biết rằng diện tích phần lối đi lát gạch bằng đúng diện tích mặt nước của bể bơi.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4.6,0);
\\coordinate (C) at (4.6,2.8);
\\coordinate (D) at (0,2.8);
\\coordinate (A1) at (0.6,0.5);
\\coordinate (B1) at (4.0,0.5);
\\coordinate (C1) at (4.0,2.3);
\\coordinate (D1) at (0.6,2.3);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (A1)--(B1)--(C1)--(D1)--cycle;
\\draw[line width=1pt, <->] (0,1.4)--(0.6,1.4) node[midway, above] {$x$};
\\node at (2.3,1.4) {Bể bơi ($%s\\text{ m} \\times %s\\text{ m}$)};
\\end{tikzpicture}
\\end{center}''' % (fmt_num(dai_ho), fmt_num(rong_ho), fmt_num(dai_ho), fmt_num(rong_ho)))

        nb_da_1_d = '\\True Chiều dài và chiều rộng của hình chữ nhật lớn (bao gồm cả bể bơi và lối đi) lần lượt là $%s + 2x\\text{ (m)}$ và $%s + 2x\\text{ (m)}$' % (fmt_num(dai_ho), fmt_num(rong_ho))
        nb_da_1_s = 'Chiều dài và chiều rộng của hình chữ nhật lớn (bao gồm cả bể bơi và lối đi) lần lượt là $%s + x\\text{ (m)}$ và $%s + x\\text{ (m)}$' % (fmt_num(dai_ho), fmt_num(rong_ho))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì lối đi bao quanh cả $4$ phía của bể bơi nên mỗi chiều của hình chữ nhật lớn tăng thêm $2x\\text{ (m)}$, do đó chiều dài là $%s + 2x\\text{ (m)}$ và chiều rộng là $%s + 2x\\text{ (m)}$.''' % (fmt_num(dai_ho), fmt_num(rong_ho)))

        th_da_1_d = '\\True Tổng diện tích của cả bể bơi và lối đi là $%s\\text{ m}^2$' % (fmt_num(s_tong))
        th_da_1_s = 'Tổng diện tích của cả bể bơi và lối đi là $%s\\text{ m}^2$' % (fmt_num(s_ho))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Diện tích mặt nước của bể bơi là $%s \\cdot %s = %s\\text{ (m}^2\\text{)}$. Vì diện tích lối đi bằng diện tích bể bơi nên tổng diện tích là $%s + %s = %s\\text{ (m}^2\\text{)}$.''' % (fmt_num(dai_ho), fmt_num(rong_ho), fmt_num(s_ho), fmt_num(s_ho), fmt_num(s_ho), fmt_num(s_tong)))

        vd_da_1_d = '\\True Phương trình tìm bề rộng $x$ của lối đi là $4x^2 + %sx - %s = 0$' % (fmt_num(b_eq), fmt_num(c_eq))
        vd_da_1_s = 'Phương trình tìm bề rộng $x$ của lối đi là $x^2 + %sx - %s = 0$' % (fmt_num(dai_ho + rong_ho), fmt_num(c_eq))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Ta có phương trình diện tích: $(%s + 2x)(%s + 2x) = %s \\Leftrightarrow %s + %sx + 4x^2 = %s \\Leftrightarrow 4x^2 + %sx - %s = 0$.''' % (fmt_num(dai_ho), fmt_num(rong_ho), fmt_num(s_tong), fmt_num(s_ho), fmt_num(b_eq), fmt_num(s_tong), fmt_num(b_eq), fmt_num(c_eq)))

        vdc_da_1_d = '\\True Bề rộng của lối đi xung quanh bể bơi là $%s\\text{ m}$' % (fmt_num(x_val))
        vdc_da_1_s = 'Bề rộng của lối đi xung quanh bể bơi là $%s\\text{ m}$' % (fmt_num(x_val + 1))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        b_half = b_eq // 2
        delta_p = b_half**2 + 4 * c_eq
        sqrt_dp = int(math.isqrt(delta_p))
        loigiai_vdc_1 = ('''Giải phương trình $4x^2 + %sx - %s = 0$: \\\\ Ta có $\\Delta' = %s^2 - 4 \\cdot (-%s) = %s$, $\\sqrt{\\Delta'} = %s$. \\\\ Nghiệm dương của phương trình là $x = \\frac{-%s + %s}{4} = %s$ (thoả mãn). \\\\ Vậy bề rộng của lối đi xung quanh bể bơi là $%s\\text{ m}$.''' % (fmt_num(b_eq), fmt_num(c_eq), fmt_num(b_half), fmt_num(c_eq), fmt_num(delta_p), fmt_num(sqrt_dp), fmt_num(b_half), fmt_num(sqrt_dp), fmt_num(x_val), fmt_num(x_val)))

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
