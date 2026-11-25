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

def bt_dang10_p2_b3_c5_ds8(self):
    # Dạng 10: Phân tích bảng thống kê kết hợp biểu đồ cột về thời gian tự học của học sinh
    # Tổng 40 HS: n1 (dưới 60p), n2 (60-<90p), n3 (90-<120p), n4 (>=120p)
    n1, n2, n3, n4 = random.choice([
        (6, 14, 12, 8),
        (8, 12, 16, 4),
        (4, 16, 8, 12)
    ])
    tong = n1 + n2 + n3 + n4
    p_ge90 = int((n3 + n4) * 100 // tong)
    p_n1 = int(n1 * 100 // tong)
    
    hs = [round(v / 4.0, 2) for v in [n1, n2, n3, n4]]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (7.6,0) node[below] {Mức thời gian};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.8) node[left] {Số học sinh};\n' +
        '\\foreach \\y/\\lbl in {1/4, 2/8, 3/12, 4/16}{\n' +
        '    \\draw[line width=1pt, dashed] (0,\\y) -- (7.2,\\y);\n' +
        '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
        '}\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!20] (0.5,0) rectangle (1.5,%s); \\node[above] at (1.0,%s) {$%s$}; \\node[below] at (1.0,0) {$<60\\text{p}$};\n' % (hs[0], hs[0], n1) +
        '\\draw[line width=1pt, fill=black!20] (2.2,0) rectangle (3.2,%s); \\node[above] at (2.7,%s) {$%s$}; \\node[below] at (2.7,0) {$60-<90\\text{p}$};\n' % (hs[1], hs[1], n2) +
        '\\draw[line width=1pt, fill=black!20] (3.9,0) rectangle (4.9,%s); \\node[above] at (4.4,%s) {$%s$}; \\node[below] at (4.4,0) {$90-<120\\text{p}$};\n' % (hs[2], hs[2], n3) +
        '\\draw[line width=1pt, fill=black!20] (5.6,0) rectangle (6.6,%s); \\node[above] at (6.1,%s) {$%s$}; \\node[below] at (6.1,0) {$\\ge 120\\text{p}$};\n' % (hs[3], hs[3], n4) +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột dưới đây thống kê thời gian tự học ở nhà mỗi ngày (tính theo phút) của toàn bộ $%s$ học sinh lớp $8\\text{D}$:\n' % tong +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Nhóm học sinh tự học dưới $60$ phút mỗi ngày có số lượng ít nhất trong lớp ($%s$ học sinh)' % n1 if n1 < n4 else '\\True Nhóm học sinh tự học từ $120$ phút trở lên mỗi ngày có số lượng ít nhất trong lớp ($%s$ học sinh)' % n4
    nb_da_1_s = 'Nhóm học sinh tự học từ $60$ đến dưới $90$ phút mỗi ngày có số lượng ít nhất trong lớp'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Số học sinh ở bốn mức lần lượt là $%s; %s; %s; %s$, do đó giá trị nhỏ nhất là $%s$ học sinh.' % (n1, n2, n3, n4, min(n1, n4)))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Có đúng $%s\\%%$ số học sinh của lớp dành từ $90$ phút trở lên mỗi ngày để tự học' % p_ge90
    th_da_1_s = 'Có $70\\%%$ số học sinh của lớp dành từ $90$ phút trở lên mỗi ngày để tự học'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Số học sinh tự học từ $90$ phút trở lên là $%s + %s = %s$ (học sinh), chiếm tỉ lệ $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (n3, n4, n3 + n4, n3 + n4, tong, p_ge90))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Số học sinh tự học dưới $60$ phút bằng một nửa số học sinh tự học từ $90$ đến dưới $120$ phút'
    vd_da_1_s = 'Số học sinh tự học dưới $60$ phút bằng số học sinh tự học từ $60$ đến dưới $90$ phút'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Ta có số học sinh tự học dưới $60$ phút là $%s$ em, bằng một nửa của $%s$ em ở nhóm từ $90$ đến dưới $120$ phút ($%s = \\dfrac{%s}{2}$).' % (n1, n3, n1, n3))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Nếu chuyển dữ liệu sang biểu đồ hình quạt tròn thì nhóm tự học dưới $60$ phút chiếm $%s\\%%$' % p_n1
    vdc_da_1_s = 'Nếu chuyển dữ liệu sang biểu đồ hình quạt tròn thì nhóm tự học dưới $60$ phút chiếm $%s\\%%$' % (p_n1 + 10)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tỉ lệ phần trăm của nhóm tự học dưới $60$ phút là $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (n1, tong, p_n1))
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
