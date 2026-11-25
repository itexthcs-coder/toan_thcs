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

def bt_dang19_p2_b3_c5_ds8(self):
    # Dạng 19: Phân tích bài toán kinh tế hộ gia đình kết hợp biểu đồ cột kép thu - chi
    thu = [45, 42, 48, 55]
    chi = [36, 32, 35, 41]
    tk = [thu[i] - chi[i] for i in range(4)] # [9, 10, 13, 14]
    tong_thu = sum(thu) # 190
    tong_tk = sum(tk) # 46
    
    pct_tk = (Decimal(tong_tk * 100) / Decimal(tong_thu)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) # 24.21
    pct_tk_str = str(pct_tk).replace('.', ',')
    
    ht = [round(v / 15.0, 2) for v in thu]
    hc = [round(v / 15.0, 2) for v in chi]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (7.8,0) node[below] {Quý};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Triệu đồng};\n' +
        '\\foreach \\y/\\lbl in {1/15, 2/30, 3/45, 4/60}{\n' +
        '    \\draw[line width=1pt, dashed] (0,\\y) -- (7.4,\\y);\n' +
        '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
        '}\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!15] (0.5,0) rectangle (1.1,%s); \\node[above] at (0.8,%s) {$45$};\n' % (ht[0], ht[0]) +
        '\\draw[line width=1pt, fill=black!45] (1.1,0) rectangle (1.7,%s); \\node[above] at (1.4,%s) {$36$};\n' % (hc[0], hc[0]) +
        '\\node[below] at (1.1,0) {Quý I};\n' +
        '\\draw[line width=1pt, fill=black!15] (2.3,0) rectangle (2.9,%s); \\node[above] at (2.6,%s) {$42$};\n' % (ht[1], ht[1]) +
        '\\draw[line width=1pt, fill=black!45] (2.9,0) rectangle (3.5,%s); \\node[above] at (3.2,%s) {$32$};\n' % (hc[1], hc[1]) +
        '\\node[below] at (2.9,0) {Quý II};\n' +
        '\\draw[line width=1pt, fill=black!15] (4.1,0) rectangle (4.7,%s); \\node[above] at (4.4,%s) {$48$};\n' % (ht[2], ht[2]) +
        '\\draw[line width=1pt, fill=black!45] (4.7,0) rectangle (5.3,%s); \\node[above] at (5.0,%s) {$35$};\n' % (hc[2], hc[2]) +
        '\\node[below] at (4.7,0) {Quý III};\n' +
        '\\draw[line width=1pt, fill=black!15] (5.9,0) rectangle (6.5,%s); \\node[above] at (6.2,%s) {$55$};\n' % (ht[3], ht[3]) +
        '\\draw[line width=1pt, fill=black!45] (6.5,0) rectangle (7.1,%s); \\node[above] at (6.8,%s) {$41$};\n' % (hc[3], hc[3]) +
        '\\node[below] at (6.5,0) {Quý IV};\n' +
        '\\draw[line width=1pt, fill=black!15] (7.6,3.2) rectangle (8.0,3.5) node[right, yshift=-4pt] {Thu nhập};\n' +
        '\\draw[line width=1pt, fill=black!45] (7.6,2.4) rectangle (8.0,2.7) node[right, yshift=-4pt] {Chi tiêu};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột kép dưới đây ghi lại tổng thu nhập và tổng chi tiêu (đơn vị: triệu đồng) của một gia đình trong $4$ quý của năm $2025$ (biết Tiền tiết kiệm = Thu nhập $-$ Chi tiêu):\n' +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Trong cả $4$ quý, gia đình đó đều có khoản tiền tiết kiệm dương'
    nb_da_1_s = 'Có ít nhất một quý trong năm gia đình đó bị chi tiêu vượt quá thu nhập'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Ở tất cả các quý, cột Thu nhập đều cao hơn cột Chi tiêu (tiết kiệm các quý lần lượt là $9; 10; 13; 14$ triệu đồng đều lớn hơn $0$).' )
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Quý IV là quý gia đình tiết kiệm được nhiều tiền nhất ($14$ triệu đồng)'
    th_da_1_s = 'Quý III là quý gia đình tiết kiệm được nhiều tiền nhất ($13$ triệu đồng)'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Tiền tiết kiệm từng quý: Quý I là $45 - 36 = 9$; Quý II là $42 - 32 = 10$; Quý III là $48 - 35 = 13$; Quý IV là $55 - 41 = 14$ (triệu đồng). Nhiều nhất là Quý IV.' )
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Tổng số tiền gia đình tiết kiệm được trong cả năm $2025$ là $46$ triệu đồng'
    vd_da_1_s = 'Tổng số tiền gia đình tiết kiệm được trong cả năm $2025$ là $42$ triệu đồng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Tổng số tiền tiết kiệm cả năm là $9 + 10 + 13 + 14 = 46$ (triệu đồng).' )
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Tỉ lệ tiền tiết kiệm so với tổng thu nhập cả năm của gia đình đạt khoảng $%s\\%%$ (dưới $25\\%%$)' % pct_tk_str
    vdc_da_1_s = 'Tỉ lệ tiền tiết kiệm so với tổng thu nhập cả năm của gia đình đạt trên $25\\%%$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng thu nhập cả năm là $45 + 42 + 48 + 55 = 190$ (triệu đồng). Tỉ lệ tiết kiệm là $\\dfrac{46}{190} \\cdot 100\\%% \\approx 24,21\\%% < 25\\%%$.' )
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
