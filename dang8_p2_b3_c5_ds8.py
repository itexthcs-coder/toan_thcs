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

def bt_dang8_p2_b3_c5_ds8(self):
    # Dạng 8: Đọc và phân tích dữ liệu khí hậu (lượng mưa) liên môn Địa lí
    k = random.choice([3, 4])
    m12 = random.choice([150, 160, 180])
    m10 = k * m12
    m7 = random.randint(80, 95)
    m8 = random.randint(110, 130)
    m9 = random.randint(270, 310)
    m11 = random.randint(390, 440)
    
    vals = [m7, m8, m9, m10, m11, m12]
    hs = [round(v / 150.0, 2) for v in vals]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (8.2,0) node[below] {Tháng};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,5.2) node[left] {Lượng mưa ($\\text{mm}$)};\n' +
        '\\foreach \\y/\\lbl in {1/150, 2/300, 3/450, 4/600, 5/750}{\n' +
        '    \\draw[line width=1pt, dashed] (0,\\y) -- (7.8,\\y);\n' +
        '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
        '}\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!25] (0.5,0) rectangle (1.3,%s); \\node[above] at (0.9,%s) {$%s$}; \\node[below] at (0.9,0) {Th.$7$};\n' % (hs[0], hs[0], m7) +
        '\\draw[line width=1pt, fill=black!25] (1.7,0) rectangle (2.5,%s); \\node[above] at (2.1,%s) {$%s$}; \\node[below] at (2.1,0) {Th.$8$};\n' % (hs[1], hs[1], m8) +
        '\\draw[line width=1pt, fill=black!25] (2.9,0) rectangle (3.7,%s); \\node[above] at (3.3,%s) {$%s$}; \\node[below] at (3.3,0) {Th.$9$};\n' % (hs[2], hs[2], m9) +
        '\\draw[line width=1pt, fill=black!25] (4.1,0) rectangle (4.9,%s); \\node[above] at (4.5,%s) {$%s$}; \\node[below] at (4.5,0) {Th.$10$};\n' % (hs[3], hs[3], m10) +
        '\\draw[line width=1pt, fill=black!25] (5.3,0) rectangle (6.1,%s); \\node[above] at (5.7,%s) {$%s$}; \\node[below] at (5.7,0) {Th.$11$};\n' % (hs[4], hs[4], m11) +
        '\\draw[line width=1pt, fill=black!25] (6.5,0) rectangle (7.3,%s); \\node[above] at (6.9,%s) {$%s$}; \\node[below] at (6.9,0) {Th.$12$};\n' % (hs[5], hs[5], m12) +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột dưới đây biểu diễn lượng mưa trung bình tháng (đơn vị: $\\text{mm}$) tại một trạm khí tượng ở miền Trung trong $6$ tháng cuối năm:\n' +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Tháng $10$ là tháng có lượng mưa trung bình cao nhất trong nửa cuối năm ($%s\\text{ mm}$)' % m10
    nb_da_1_s = 'Tháng $11$ là tháng có lượng mưa trung bình cao nhất trong nửa cuối năm'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Cột cao nhất trên biểu đồ thuộc về Tháng $10$ với lượng mưa đạt $%s\\text{ mm}$.' % m10)
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Lượng mưa trung bình của Tháng $10$ cao gấp $%s$ lần lượng mưa trung bình của Tháng $12$' % k
    th_da_1_s = 'Lượng mưa trung bình của Tháng $10$ cao gấp $2$ lần lượng mưa trung bình của Tháng $12$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Ta có tỉ số lượng mưa giữa Tháng $10$ và Tháng $12$ là $\\dfrac{%s}{%s} = %s$ (lần).' % (m10, m12, k))
    list_th_2 = [loigiai_th_1]
    
    # c (Sai)
    vd_da_1_d = '\\True Lượng mưa tại trạm khí tượng này tăng từ Tháng $7$ đến Tháng $10$, sau đó giảm dần đến Tháng $12$'
    vd_da_1_s = 'Từ Tháng $7$ đến Tháng $12$, lượng mưa tại trạm khí tượng này tăng liên tục qua từng tháng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Lượng mưa tăng từ $%s\\text{ mm}$ (Tháng $7$) lên đỉnh điểm $%s\\text{ mm}$ (Tháng $10$), rồi giảm xuống $%s\\text{ mm}$ (Tháng $11$) và $%s\\text{ mm}$ (Tháng $12$).' % (m7, m10, m11, m12))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Có đúng $3$ tháng trong nửa cuối năm có lượng mưa vượt mức $250\\text{ mm}$'
    vdc_da_1_s = 'Có $4$ tháng trong nửa cuối năm có lượng mưa vượt mức $250\\text{ mm}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Các tháng có lượng mưa lớn hơn $250\\text{ mm}$ gồm: Tháng $9$ ($%s\\text{ mm}$), Tháng $10$ ($%s\\text{ mm}$) và Tháng $11$ ($%s\\text{ mm}$), tổng cộng có $3$ tháng.' % (m9, m10, m11))
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
