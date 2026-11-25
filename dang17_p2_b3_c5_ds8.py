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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang17_p2_b3_c5_ds8(self):
    # Dạng 17: Bài toán tìm số liệu ẩn trên biểu đồ khi biết giá trị trung bình cộng
    tb = random.choice([70, 75, 80])
    tong = 4 * tb
    s_a = tb - 7
    s_b = tb - 1
    s_d = tb + 7
    s_c = tong - (s_a + s_b + s_d) # tb + 1
    
    pct_d = (Decimal(s_d * 100) / Decimal(tong)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    pct_d_str = str(pct_d).replace('.', ',')
    
    hs = [round(v / 25.0, 2) for v in [s_a, s_b, s_c, s_d]]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (7.4,0) node[below] {Lớp};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số sách (cuốn)};\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!20] (0.6,0) rectangle (1.5,%s); \\node[above] at (1.05,%s) {$%s$}; \\node[below] at (1.05,0) {$8\\text{A}$};\n' % (hs[0], hs[0], s_a) +
        '\\draw[line width=1pt, fill=black!20] (2.2,0) rectangle (3.1,%s); \\node[above] at (2.65,%s) {$%s$}; \\node[below] at (2.65,0) {$8\\text{B}$};\n' % (hs[1], hs[1], s_b) +
        '\\draw[line width=1pt, fill=black!20] (3.8,0) rectangle (4.7,%s); \\node[above] at (4.25,%s) {$x$}; \\node[below] at (4.25,0) {$8\\text{C}$};\n' % (hs[2], hs[2]) +
        '\\draw[line width=1pt, fill=black!20] (5.4,0) rectangle (6.3,%s); \\node[above] at (5.85,%s) {$%s$}; \\node[below] at (5.85,0) {$8\\text{D}$};\n' % (hs[3], hs[3], s_d) +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột dưới đây biểu diễn số cuốn sách quyên góp được của $4$ lớp khối $8$ trong phong trào "Tủ sách yêu thương" (trong đó số sách của lớp $8\\text{C}$ kí hiệu là $x$). Biết trung bình mỗi lớp quyên góp được $%s$ cuốn sách:\n' % tb +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Tổng số sách cả $4$ lớp quyên góp được là $%s$ cuốn' % tong
    nb_da_1_s = 'Tổng số sách cả $4$ lớp quyên góp được là $%s$ cuốn' % (tong - 20)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Vì trung bình mỗi lớp quyên góp được $%s$ cuốn nên tổng số sách của $4$ lớp là $%s \\cdot 4 = %s$ (cuốn).' % (tb, tb, tong))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Lớp $8\\text{C}$ quyên góp được $x = %s$ cuốn sách' % s_c
    th_da_1_s = 'Lớp $8\\text{C}$ quyên góp được $x = %s$ cuốn sách' % (s_c - 4)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Ta có $x = %s - (%s + %s + %s) = %s - %s = %s$ (cuốn).' % (tong, s_a, s_b, s_d, tong, s_a + s_b + s_d, s_c))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Có đúng $2$ lớp quyên góp được số sách vượt mức trung bình của cả khối'
    vd_da_1_s = 'Có $3$ lớp quyên góp được số sách vượt mức trung bình của cả khối'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('So với mức trung bình $%s$ cuốn, có $2$ lớp vượt mức là lớp $8\\text{C}$ ($%s$ cuốn) và lớp $8\\text{D}$ ($%s$ cuốn).' % (tb, s_c, s_d))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Số sách của lớp $8\\text{D}$ chiếm khoảng $%s\\%%$ tổng số sách quyên góp của cả $4$ lớp' % pct_d_str
    vdc_da_1_s = 'Số sách của lớp $8\\text{D}$ chiếm đúng $30\\%%$ tổng số sách quyên góp của cả $4$ lớp'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tỉ lệ số sách của lớp $8\\text{D}$ so với cả khối là $\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%$.' % (s_d, tong, pct_d_str))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
