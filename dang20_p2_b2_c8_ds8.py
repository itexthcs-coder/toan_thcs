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


def bt_dang20_p2_b2_c8_ds8(self):
    # Dạng 20: Bài toán thực tế về mã khóa / mật khẩu số đơn giản
    mode = random.choice([1, 2])
    if mode == 1:
        dk_chuc = 'số lẻ'
        dk_dv = 'số chia hết cho $3$'
        so_chuc = 5
        so_dv = 4
        so_ma = 20
        giai_ma = 'Chữ số hàng chục là số lẻ có $5$ cách chọn ($1; 3; 5; 7; 9$). Chữ số hàng đơn vị chia hết cho $3$ có $4$ cách chọn ($0; 3; 6; 9$). Do đó có $5 \\cdot 4 = 20$ mã số thỏa mãn.'
    else:
        dk_chuc = 'số chẵn'
        dk_dv = 'số chia hết cho $4$'
        so_chuc = 5
        so_dv = 3
        so_ma = 15
        giai_ma = 'Chữ số hàng chục là số chẵn có $5$ cách chọn ($0; 2; 4; 6; 8$). Chữ số hàng đơn vị chia hết cho $4$ có $3$ cách chọn ($0; 4; 8$). Do đó có $5 \\cdot 3 = 15$ mã số thỏa mãn.'

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) rectangle (3.6,1.6);\n'
        '\\draw[line width=1pt] (1.8,0)--(1.8,1.6);\n'
        '\\node at (0.9,0.8) {$0 \\div 9$};\n'
        '\\node at (2.7,0.8) {$0 \\div 9$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một chiếc vali có khóa số gồm $2$ vòng xoay độc lập, mỗi vòng có các chữ số từ $0$ đến $9$. Bạn Hà đặt mật khẩu là một dãy gồm hai chữ số mà chữ số hàng chục là %s và chữ số hàng đơn vị là %s. Một người lạ thử xoay ngẫu nhiên $1$ mã gồm hai chữ số (từ $00$ đến $99$). Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (dk_chuc, dk_dv, tikz_hinh)
    )

    nb_da_1_d = '\\True Có tất cả $100$ mã số có thể tạo thành trên khóa vali'
    nb_da_1_s = 'Có tất cả $90$ mã số có thể tạo thành trên khóa vali'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Từ $00$ đến $99$ có $99 - 0 + 1 = 100$ mã số có thể tạo thành và khả năng xoay được mỗi mã số là đồng khả năng.'
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Có $%s$ mã số thỏa mãn quy luật đặt mật khẩu của bạn Hà' % (so_ma)
    th_da_1_s = 'Có $%s$ mã số thỏa mãn quy luật đặt mật khẩu của bạn Hà' % (so_chuc + so_dv)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = giai_ma
    list_th_2 = [loigiai_th_1]

    p_quy_luat = Fraction(so_ma, 100)
    p_quy_luat_sai = Fraction(so_ma + 5, 100)
    vd_da_1_d = '\\True Xác suất để người lạ xoay trúng một mã số thỏa mãn quy luật đặt mật khẩu của Hà là $%s$' % (fmt_frac(p_quy_luat))
    vd_da_1_s = 'Xác suất để người lạ xoay trúng một mã số thỏa mãn quy luật đặt mật khẩu của Hà là $%s$' % (fmt_frac(p_quy_luat_sai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Xác suất để người lạ xoay trúng một mã số thỏa mãn quy luật đặt mật khẩu của Hà là $\\dfrac{%s}{100} = %s$.' % (so_ma, fmt_frac(p_quy_luat))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Xác suất để người lạ xoay đúng chính xác mật khẩu của Hà ngay lần đầu tiên là $\\dfrac{1}{100}$'
    vdc_da_1_s = 'Xác suất để người lạ xoay đúng chính xác mật khẩu của Hà ngay lần đầu tiên là $%s$' % (fmt_frac(p_quy_luat))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Mật khẩu của Hà là một mã số cố định duy nhất trong tổng số $100$ mã số có thể nên xác suất để người lạ xoay đúng ngay lần đầu tiên là $\\dfrac{1}{100}$.'
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
