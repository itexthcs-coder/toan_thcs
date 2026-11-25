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

def bt_dang1_p2_b3_c5_ds8(self):
    # Dạng 1: Phân tích biểu đồ cột kép về chỉ số chất lượng không khí (AQI) giữa hai đô thị
    x1 = random.randint(138, 150)
    x2 = random.randint(122, 134)
    x3 = random.randint(105, 115)
    x4 = random.randint(80, 90)
    
    y1 = random.randint(92, 102)
    y2 = random.randint(102, 112)
    y3 = x3
    y4 = random.randint(92, 98)
    
    diff1 = x1 - y1
    diff2 = x2 - y2
    
    # Vẽ biểu đồ cột kép TikZ (tỉ lệ 160 -> 4.0 cm)
    hx = [round(v / 40.0, 2) for v in [x1, x2, x3, x4]]
    hy = [round(v / 40.0, 2) for v in [y1, y2, y3, y4]]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (7.8,0) node[below] {Tháng};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Chỉ số AQI};\n' +
        '\\foreach \\y/\\lbl in {1/40, 2/80, 3/120, 4/160}{\n' +
        '    \\draw[line width=1pt, dashed] (0,\\y) -- (7.4,\\y);\n' +
        '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
        '}\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!15] (0.5,0) rectangle (1.1,%s);\n' % hx[0] +
        '\\node[above] at (0.8,%s) {$%s$};\n' % (hx[0], x1) +
        '\\draw[line width=1pt, fill=black!45] (1.1,0) rectangle (1.7,%s);\n' % hy[0] +
        '\\node[above] at (1.4,%s) {$%s$};\n' % (hy[0], y1) +
        '\\node[below] at (1.1,0) {Tháng $1$};\n' +
        '\\draw[line width=1pt, fill=black!15] (2.3,0) rectangle (2.9,%s);\n' % hx[1] +
        '\\node[above] at (2.6,%s) {$%s$};\n' % (hx[1], x2) +
        '\\draw[line width=1pt, fill=black!45] (2.9,0) rectangle (3.5,%s);\n' % hy[1] +
        '\\node[above] at (3.2,%s) {$%s$};\n' % (hy[1], y2) +
        '\\node[below] at (2.9,0) {Tháng $2$};\n' +
        '\\draw[line width=1pt, fill=black!15] (4.1,0) rectangle (4.7,%s);\n' % hx[2] +
        '\\node[above] at (4.4,%s) {$%s$};\n' % (hx[2], x3) +
        '\\draw[line width=1pt, fill=black!45] (4.7,0) rectangle (5.3,%s);\n' % hy[2] +
        '\\node[above] at (5.0,%s) {$%s$};\n' % (hy[2], y3) +
        '\\node[below] at (4.7,0) {Tháng $3$};\n' +
        '\\draw[line width=1pt, fill=black!15] (5.9,0) rectangle (6.5,%s);\n' % hx[3] +
        '\\node[above] at (6.2,%s) {$%s$};\n' % (hx[3], x4) +
        '\\draw[line width=1pt, fill=black!45] (6.5,0) rectangle (7.1,%s);\n' % hy[3] +
        '\\node[above] at (6.8,%s) {$%s$};\n' % (hy[3], y4) +
        '\\node[below] at (6.5,0) {Tháng $4$};\n' +
        '\\draw[line width=1pt, fill=black!15] (7.6,3.2) rectangle (8.0,3.5) node[right, yshift=-4pt] {Thành phố $X$};\n' +
        '\\draw[line width=1pt, fill=black!45] (7.6,2.4) rectangle (8.0,2.7) node[right, yshift=-4pt] {Thành phố $Y$};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột kép dưới đây biểu diễn chỉ số chất lượng không khí trung bình (AQI) trong $4$ tháng đầu năm của hai thành phố $X$ và $Y$:\n' +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # Mệnh đề a (Gốc Sai)
    nb_da_1_d = '\\True Trong cả $4$ tháng, chỉ số AQI của thành phố $X$ không phải lúc nào cũng cao hơn thành phố $Y$'
    nb_da_1_s = 'Trong cả $4$ tháng, chỉ số AQI của thành phố $X$ luôn cao hơn thành phố $Y$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tại Tháng $3$, chỉ số AQI của hai thành phố bằng nhau ($%s = %s$); tại Tháng $4$, chỉ số AQI của thành phố $X$ ($%s$) thấp hơn thành phố $Y$ ($%s$). Do đó, không phải trong cả $4$ tháng chỉ số AQI của thành phố $X$ đều cao hơn thành phố $Y$.' % (x3, y3, x4, y4))
    list_nb_2 = [loigiai_nb_1]
    
    # Mệnh đề b (Gốc Đúng)
    th_da_1_d = '\\True Chỉ số AQI của thành phố $X$ có xu hướng giảm liên tục từ Tháng $1$ đến Tháng $4$'
    th_da_1_s = 'Chỉ số AQI của thành phố $X$ có xu hướng tăng liên tục từ Tháng $1$ đến Tháng $4$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Chỉ số AQI của thành phố $X$ qua các tháng $1, 2, 3, 4$ lần lượt là $%s; %s; %s; %s$, giảm liên tục qua từng tháng.' % (x1, x2, x3, x4))
    list_th_2 = [loigiai_th_1]
    
    # Mệnh đề c (Gốc Đúng)
    vd_da_1_d = '\\True Vào Tháng $3$, chỉ số AQI của hai thành phố đạt mức bằng nhau và cùng bằng $%s$' % x3
    vd_da_1_s = 'Vào Tháng $3$, chỉ số AQI của thành phố $X$ cao hơn thành phố $Y$ là $10$ đơn vị'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Quan sát cặp cột tại Tháng $3$, hai cột có chiều cao bằng nhau và cùng biểu diễn giá trị $%s$.' % x3)
    list_vd_2 = [loigiai_vd_1]
    
    # Mệnh đề d (Gốc Sai)
    vdc_da_1_d = '\\True Mức chênh lệch chỉ số AQI giữa hai thành phố lớn nhất là vào Tháng $1$'
    vdc_da_1_s = 'Mức chênh lệch chỉ số AQI giữa hai thành phố lớn nhất là vào Tháng $2$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Mức chênh lệch chỉ số AQI giữa hai thành phố trong từng tháng lần lượt là: Tháng $1$ là $|%s - %s| = %s$; Tháng $2$ là $|%s - %s| = %s$; Tháng $3$ là $0$; Tháng $4$ là $|%s - %s| = %s$. Vậy mức chênh lệch lớn nhất là vào Tháng $1$ ($%s$ đơn vị).' % (x1, y1, diff1, x2, y2, diff2, x4, y4, abs(x4 - y4), diff1))
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
