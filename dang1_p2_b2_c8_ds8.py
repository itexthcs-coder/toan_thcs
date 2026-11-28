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


def bt_dang1_p2_b2_c8_ds8(self):
    # Dạng 1: Gieo xúc xắc đồng chất – Kết hợp tính chất chia hết và số nguyên tố
    k = random.choice([2, 3])
    m = random.choice([4, 5])
    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (1.5,0);\n'
        '\\coordinate (C) at (1.5,1.5);\n'
        '\\coordinate (D) at (0,1.5);\n'
        '\\coordinate (E) at (0.6,2.0);\n'
        '\\coordinate (F) at (2.1,2.0);\n'
        '\\coordinate (G) at (2.1,0.5);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (D)--(E)--(F)--(C) (F)--(G)--(B);\n'
        '\\fill (0.75,0.75) circle (1pt);\n'
        '\\fill (0.4,1.1) circle (1pt) (1.1,0.4) circle (1pt);\n'
        '\\fill (1.05,1.75) circle (1pt);\n'
        '\\fill (1.8,1.25) circle (1pt);\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )
    noidungcauhoi = (
        'Gieo một con xúc xắc cân đối và đồng chất có $6$ mặt (đánh số từ $1$ đến $6$) một lần. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (tikz_hinh)
    )

    nb_da_1_d = '\\True Có $6$ kết quả có thể xảy ra và các kết quả này là đồng khả năng'
    nb_da_1_s = 'Có $6$ kết quả có thể xảy ra nhưng các kết quả này không đồng khả năng'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Gieo một con xúc xắc cân đối và đồng chất có $6$ mặt nên có $6$ kết quả có thể xảy ra là $1; 2; 3; 4; 5; 6$ và các kết quả này là đồng khả năng.'
    list_nb_2 = [loigiai_nb_1]

    p_nt = Fraction(3, 6)
    p_nt_sai = Fraction(4, 6)
    th_da_1_d = '\\True Xác suất của biến cố "Mặt xuất hiện có số chấm là số nguyên tố" bằng $%s$' % (fmt_frac(p_nt))
    th_da_1_s = 'Xác suất của biến cố "Mặt xuất hiện có số chấm là số nguyên tố" bằng $%s$' % (fmt_frac(p_nt_sai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Các kết quả thuận lợi cho biến cố "Mặt xuất hiện có số chấm là số nguyên tố" là $2; 3; 5$ (gồm $3$ kết quả). \\ Vậy xác suất của biến cố đó là $\\dfrac{3}{6} = %s$.' % (fmt_frac(p_nt))
    list_th_2 = [loigiai_th_1]

    thuan_loi_k = [i for i in range(1, 7) if i % k == 0]
    p_k = Fraction(len(thuan_loi_k), 6)
    p_k_sai = Fraction(1, 6) if p_k != Fraction(1, 6) else Fraction(1, 2)
    ds_k_str = '; '.join(str(i) for i in thuan_loi_k)
    vd_da_1_d = '\\True Xác suất của biến cố "Mặt xuất hiện có số chấm chia hết cho $%s$" bằng $%s$' % (k, fmt_frac(p_k))
    vd_da_1_s = 'Xác suất của biến cố "Mặt xuất hiện có số chấm chia hết cho $%s$" bằng $%s$' % (k, fmt_frac(p_k_sai))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Các kết quả thuận lợi cho biến cố "Mặt xuất hiện có số chấm chia hết cho $%s$" là $%s$ (gồm $%s$ kết quả). \\ Vậy xác suất của biến cố đó là $\\dfrac{%s}{6} = %s$.' % (k, ds_k_str, len(thuan_loi_k), len(thuan_loi_k), fmt_frac(p_k))
    list_vd_2 = [loigiai_vd_1]

    thuan_loi_m = [i for i in range(1, 7) if i < m]
    p_m = Fraction(len(thuan_loi_m), 6)
    ds_m_str = '; '.join(str(i) for i in thuan_loi_m)
    vdc_da_1_d = '\\True Xác suất của biến cố "Mặt xuất hiện có số chấm nhỏ hơn $%s$" bằng $%s$' % (m, fmt_frac(p_m))
    vdc_da_1_s = 'Xác suất của biến cố "Mặt xuất hiện có số chấm nhỏ hơn $%s$" bằng $\\dfrac{1}{2}$' % (m)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Các kết quả thuận lợi cho biến cố "Mặt xuất hiện có số chấm nhỏ hơn $%s$" là $%s$ (gồm $%s$ kết quả). \\ Vậy xác suất của biến cố đó là $\\dfrac{%s}{6} = %s$.' % (m, ds_m_str, len(thuan_loi_m), len(thuan_loi_m), fmt_frac(p_m))
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
