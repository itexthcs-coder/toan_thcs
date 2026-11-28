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


def bt_dang17_p2_b2_c8_ds8(self):
    # Dạng 17: Tích hợp Đại số – Thay giá trị vào biểu thức / nghiệm của phương trình
    M = [-3, -2, -1, 0, 1, 2, 3, 4]
    tong = len(M)
    r_sq = random.choice([1, 4, 9])
    r_root = int(math.isqrt(r_sq))

    tikz_hinh = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[line width=1pt] (0,0) rectangle (6.6,1.4);\n'
        '\\node at (3.3,0.7) {$M = \\{-3; -2; -1; 0; 1; 2; 3; 4\\}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho tập hợp $M = \\{-3; -2; -1; 0; 1; 2; 3; 4\\}$. Chọn ngẫu nhiên một số $x$ từ tập hợp $M$. Xét tính đúng, sai của các khẳng định sau:\\n%s'
        % (tikz_hinh)
    )

    nghiem_pt = [v for v in M if v**2 - r_sq == 0]
    p_pt = Fraction(len(nghiem_pt), tong)
    p_pt_sai = Fraction(1, tong)
    nb_da_1_d = '\\True Xác suất để số $x$ được chọn là nghiệm của phương trình $x^2 - %s = 0$ bằng $%s$' % (r_sq, fmt_frac(p_pt))
    nb_da_1_s = 'Xác suất để số $x$ được chọn là nghiệm của phương trình $x^2 - %s = 0$ bằng $%s$' % (r_sq, fmt_frac(p_pt_sai))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Phương trình $x^2 - %s = 0 \\Leftrightarrow x = -%s$ hoặc $x = %s$. Cả hai giá trị này đều thuộc tập $M$. \\ Vậy xác suất cần tìm là $\\dfrac{2}{8} = %s$.' % (r_sq, r_root, r_root, fmt_frac(p_pt))
    list_nb_2 = [loigiai_nb_1]

    nghiem_bpt = [v for v in M if 2*v - 1 > 3]
    p_bpt = Fraction(len(nghiem_bpt), tong)
    p_bpt_sai = Fraction(3, tong)
    th_da_1_d = '\\True Xác suất để số $x$ được chọn thỏa mãn bất phương trình $2x - 1 > 3$ bằng $%s$' % (fmt_frac(p_bpt))
    th_da_1_s = 'Xác suất để số $x$ được chọn thỏa mãn bất phương trình $2x - 1 > 3$ bằng $%s$' % (fmt_frac(p_bpt_sai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Ta có $2x - 1 > 3 \\Leftrightarrow 2x > 4 \\Leftrightarrow x > 2$. Trong tập $M$, các giá trị thỏa mãn là $x \\in \\{3; 4\\}$ (gồm $2$ phần tử). \\ Vậy xác suất cần tìm là $\\dfrac{2}{8} = %s$.' % (fmt_frac(p_bpt))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Xác suất để giá trị biểu thức $A = \\dfrac{5}{x + 2}$ nhận giá trị nguyên bằng $\\dfrac{3}{8}$'
    vd_da_1_s = 'Xác suất để giá trị biểu thức $A = \\dfrac{5}{x + 2}$ nhận giá trị nguyên bằng $\\dfrac{1}{2}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Để $A = \\dfrac{5}{x + 2}$ nhận giá trị nguyên thì $x + 2 \\in \\text{Ư}(5) = \\{-5; -1; 1; 5\\} \\Rightarrow x \\in \\{-7; -3; -1; 3\\}$. \\ Giao với tập $M$ ta được $x \\in \\{-3; -1; 3\\}$ (gồm $3$ giá trị). Vậy xác suất cần tìm là $\\dfrac{3}{8}$.'
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Xác suất để $x^2 \\le 4$ bằng $\\dfrac{5}{8}$'
    vdc_da_1_s = 'Xác suất để $x^2 \\le 4$ bằng $\\dfrac{1}{2}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Trong tập $M$, các số thỏa mãn $x^2 \\le 4$ là $-2; -1; 0; 1; 2$ (gồm $5$ phần tử). \\ Vậy xác suất cần tìm là $\\dfrac{5}{8}$.'
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
