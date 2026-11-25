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


def bt_dang18_p2_b1_c6_ds8(self):
    # Dạng 18: Mô hình hóa bài toán hình học thực tế (kích thước mảnh vườn hình chữ nhật)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (240, 12, 10), # r=12 -> d=20 != 12; r=10 -> d=24, P=68
            (180, 12, 9),  # r=12 -> d=15 != 12; r=9 -> d=20, P=58
            (300, 15, 10)  # r=15 -> d=20 != 15; r=10 -> d=30, P=80
        ]
        S_vuon, r1, r2 = random.choice(scenarios)
        d1 = S_vuon // r1
        d2 = S_vuon // r2
        chu_vi = 2 * (r2 + d2)
        
        tikz_hinh = ('\\begin{center}\n'
                     '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                     '\\coordinate (A) at (0,0);\n'
                     '\\coordinate (B) at (4.2,0);\n'
                     '\\coordinate (C) at (4.2,2.2);\n'
                     '\\coordinate (D) at (0,2.2);\n'
                     '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
                     '\\fill (A) circle (1pt) node[below left] {$A$};\n'
                     '\\fill (B) circle (1pt) node[below right] {$B$};\n'
                     '\\fill (C) circle (1pt) node[above right] {$C$};\n'
                     '\\fill (D) circle (1pt) node[above left] {$D$};\n'
                     '\\node[below] at (2.1,0) {$\\dfrac{%s}{x}\\text{ (m)}$};\n'
                     '\\node[left] at (0,1.1) {$x\\text{ (m)}$};\n'
                     '\\node at (2.1,1.1) {$S = %s\\text{ m}^2$};\n'
                     '\\end{tikzpicture}\n'
                     '\\end{center}' % (S_vuon, S_vuon))
        
        noidungcauhoi = ('Bác An có một mảnh vườn hình chữ nhật $ABCD$ với diện tích là $%s\\text{ m}^2$. Gọi chiều rộng của mảnh vườn là $x\\text{ (m)}$ ($x > 0$). Xét tính đúng sai của các khẳng định sau:\n%s'
                         % (S_vuon, tikz_hinh))
        
        nb_da_1_d = '\\True Phân thức biểu thị chiều dài của mảnh vườn theo $x$ là $\\dfrac{%s}{x}\\text{ (m)}$' % S_vuon
        nb_da_1_s = 'Phân thức biểu thị chiều dài của mảnh vườn theo $x$ là $\\dfrac{x}{%s}\\text{ (m)}$' % S_vuon
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Vì diện tích hình chữ nhật bằng chiều dài nhân chiều rộng nên chiều dài mảnh vườn là $\\dfrac{%s}{x}\\text{ (m)}$.' % S_vuon
        loigiai_nb_s = 'Sai. Chiều dài bằng diện tích chia cho chiều rộng: $\\dfrac{%s}{x}\\text{ (m)}$.' % S_vuon
        
        th_da_1_d = '\\True Phân thức biểu thị tỉ số giữa chiều rộng và chiều dài của mảnh vườn là $\\dfrac{x^2}{%s}$' % S_vuon
        th_da_1_s = 'Phân thức biểu thị tỉ số giữa chiều rộng và chiều dài của mảnh vườn là $\\dfrac{%s}{x^2}$' % S_vuon
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Tỉ số giữa chiều rộng và chiều dài là $x : \\dfrac{%s}{x} = x \\cdot \\dfrac{x}{%s} = \\dfrac{x^2}{%s}$.' % (S_vuon, S_vuon, S_vuon)
        loigiai_th_s = 'Sai. $\\dfrac{%s}{x^2}$ là tỉ số giữa chiều dài và chiều rộng; tỉ số giữa chiều rộng và chiều dài là $\\dfrac{x^2}{%s}$.' % (S_vuon, S_vuon)
        
        vd_da_1_d = '\\True Nếu chiều rộng của mảnh vườn là $%s\\text{ m}$ thì chiều dài mảnh vườn bằng $%s\\text{ m}$' % (r1, d1)
        vd_da_1_s = 'Nếu chiều rộng của mảnh vườn là $%s\\text{ m}$ thì mảnh vườn đó có dạng hình vuông' % r1
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Thay $x = %s$ vào phân thức $\\dfrac{%s}{x}$, ta được chiều dài mảnh vườn là $\\dfrac{%s}{%s} = %s\\text{ (m)}$.' % (r1, S_vuon, S_vuon, r1, d1)
        loigiai_vd_s = 'Sai. Khi chiều rộng là $%s\\text{ m}$ thì chiều dài là $\\dfrac{%s}{%s} = %s\\text{ m} \\neq %s\\text{ m}$, nên mảnh vườn không phải hình vuông.' % (r1, S_vuon, r1, d1, r1)
        
        vdc_da_1_d = '\\True Nếu chiều rộng của mảnh vườn là $%s\\text{ m}$ thì chu vi của mảnh vườn là $%s\\text{ m}$' % (r2, chu_vi)
        vdc_da_1_s = 'Nếu chiều rộng của mảnh vườn là $%s\\text{ m}$ thì chu vi của mảnh vườn là $%s\\text{ m}$' % (r2, r2 + d2)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Với $x = %s\\text{ m}$, chiều dài là $\\dfrac{%s}{%s} = %s\\text{ m}$. Chu vi mảnh vườn là $2 \\cdot (%s + %s) = %s\\text{ (m)}$.' % (r2, S_vuon, r2, d2, r2, d2, chu_vi)
        loigiai_vdc_s = 'Sai. $%s\\text{ m}$ mới chỉ là nửa chu vi; chu vi mảnh vườn là $2 \\cdot (%s + %s) = %s\\text{ (m)}$.' % (r2 + d2, r2, d2, chu_vi)
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
