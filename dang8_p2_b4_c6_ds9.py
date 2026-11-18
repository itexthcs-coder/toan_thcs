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


def bt_dang8_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_coef = Decimal('0.04')
        b_coef = Decimal('0.8')
        v_real = random.choice([30, 40, 50, 60])
        d_val = a_coef * (Decimal(v_real) ** 2) + b_coef * Decimal(v_real)
        c_norm = int(d_val * Decimal(25))
        v_limit = v_real + 10

        noidungcauhoi = ('''Các kỹ sư giao thông sử dụng công thức $d = 0,04v^2 + 0,8v$ để ước tính khoảng cách an toàn tối thiểu $d\\text{ (mét)}$ mà một ô tô đi được kể từ lúc người lái đạp phanh cho đến khi xe dừng hẳn trên mặt đường khô ráo, với $v\\text{ (km/h)}$ là tốc độ của xe lúc bắt đầu đạp phanh ($v > 0$). Một chiếc ô tô để lại vết phanh dài $%s\\text{ m}$ trên đường trước khi dừng lại.''' % (fmt_num(d_val)))

        nb_da_1_d = '\\True Để tìm tốc độ của ô tô lúc đạp phanh, ta giải phương trình $0,04v^2 + 0,8v - %s = 0$' % (fmt_num(d_val))
        nb_da_1_s = 'Để tìm tốc độ của ô tô lúc đạp phanh, ta giải phương trình $0,04v^2 + 0,8v + %s = 0$' % (fmt_num(d_val))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thay $d = %s$ vào công thức $d = 0,04v^2 + 0,8v$, ta được phương trình $0,04v^2 + 0,8v - %s = 0$.''' % (fmt_num(d_val), fmt_num(d_val)))

        th_da_1_d = '\\True Phương trình trên tương đương với $v^2 + 20v - %s = 0$' % (fmt_num(c_norm))
        th_da_1_s = 'Phương trình trên tương đương với $v^2 + 2v - %s = 0$' % (fmt_num(c_norm))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Nhân cả hai vế của phương trình $0,04v^2 + 0,8v - %s = 0$ với $25$, ta được phương trình tương đương: $v^2 + 20v - %s = 0$.''' % (fmt_num(d_val), fmt_num(c_norm)))

        vd_da_1_d = '\\True Tốc độ của chiếc ô tô lúc bắt đầu đạp phanh là $%s\\text{ km/h}$' % (fmt_num(v_real))
        vd_da_1_s = 'Tốc độ của chiếc ô tô lúc bắt đầu đạp phanh là $%s\\text{ km/h}$' % (fmt_num(v_real + 20))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        delta_p = 100 + c_norm
        sqrt_dp = int(math.isqrt(delta_p))
        loigiai_vd_1 = ('''Giải phương trình $v^2 + 20v - %s = 0$: \\\\ Ta có $\\Delta' = 10^2 - 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta'} = %s$. \\\\ Nghiệm của phương trình là $v_1 = -10 + %s = %s$ (thoả mãn) và $v_2 = -10 - %s = -%s$ (loại). \\\\ Vậy tốc độ của xe lúc bắt đầu đạp phanh là $%s\\text{ km/h}$.''' % (fmt_num(c_norm), fmt_num(c_norm), fmt_num(delta_p), fmt_num(sqrt_dp), fmt_num(sqrt_dp), fmt_num(v_real), fmt_num(sqrt_dp), fmt_num(v_real + 20), fmt_num(v_real)))

        vdc_da_1_d = '\\True Nếu đoạn đường này có biển báo giới hạn tốc độ tối đa là $%s\\text{ km/h}$ thì tài xế không vi phạm lỗi chạy quá tốc độ' % (fmt_num(v_limit))
        vdc_da_1_s = 'Nếu đoạn đường này có biển báo giới hạn tốc độ tối đa là $%s\\text{ km/h}$ thì tài xế đã vi phạm lỗi chạy quá tốc độ' % (fmt_num(v_limit))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Vì tốc độ của ô tô lúc đạp phanh là $%s\\text{ km/h} < %s\\text{ km/h}$ nên tài xế không vi phạm lỗi chạy quá tốc độ.''' % (fmt_num(v_real), fmt_num(v_limit)))

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
