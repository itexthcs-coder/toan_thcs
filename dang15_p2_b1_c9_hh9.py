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


def bt_dang15_p2_b1_c9_hh9(self):
    bo_ti_le = [
        (2, 3, 4, 9),
        (3, 4, 5, 12),
        (1, 2, 3, 6)
    ]
    a_r, b_r, c_r, tong_r = random.choice(bo_ti_le)
    cung_AB = (360 // tong_r) * a_r
    cung_BC = (360 // tong_r) * b_r
    cung_CA = (360 // tong_r) * c_r
    goc_C = cung_AB // 2
    goc_A = cung_BC // 2
    goc_B = cung_CA // 2
    loai_tg = 'nhọn' if goc_B < 90 else 'vuông'

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (A) at (110:2);\n'
        '\\coordinate (B) at (210:2);\n'
        '\\coordinate (C) at (330:2);\n'
        '\\draw[line width=1pt] (O) circle (2cm);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n'
        '\\fill (O) circle (1pt) node[below] {$O$};\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho ba điểm $A, B, C$ nằm trên đường tròn $(O)$ sao cho $\\text{sđ}\\overset\\frown{AB} : \\text{sđ}\\overset\\frown{BC} : \\text{sđ}\\overset\\frown{CA} = %s : %s : %s$ (các cung đều là cung nhỏ) như hình vẽ.\n%s'
        % (a_r, b_r, c_r, hinh_ve)
    )

    nb_da_1_d = '\\True Số đo cung nhỏ $AB$ bằng $%s^\\circ$' % (cung_AB)
    nb_da_1_s = 'Số đo cung nhỏ $AB$ bằng $%s^\\circ$' % (cung_AB // 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Vì tổng số đo ba cung nhỏ $AB, BC, CA$ bằng $360^\\circ$ nên $\\text{sđ}\\overset\\frown{AB} = \\dfrac{%s}{%s + %s + %s} \\cdot 360^\\circ = %s^\\circ$.' % (a_r, a_r, b_r, c_r, cung_AB)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số đo góc nội tiếp $\\widehat{ABC}$ bằng $%s^\\circ$' % (goc_B)
    th_da_1_s = 'Số đo góc nội tiếp $\\widehat{ABC}$ bằng $%s^\\circ$' % (cung_CA)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Ta có $\\text{sđ}\\overset\\frown{CA} = \\dfrac{%s}{%s} \\cdot 360^\\circ = %s^\\circ$. Góc nội tiếp $\\widehat{ABC}$ chắn cung nhỏ $CA$ nên $\\widehat{ABC} = \\dfrac{1}{2}\\text{sđ}\\overset\\frown{CA} = %s^\\circ$.' % (c_r, tong_r, cung_CA, goc_B)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Góc lớn nhất của tam giác $ABC$ có số đo bằng $%s^\\circ$' % (goc_B)
    vd_da_1_s = 'Góc lớn nhất của tam giác $ABC$ có số đo bằng $%s^\\circ$' % (goc_B + 10)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Tương tự, ta tính được $\\widehat{ACB} = \\dfrac{1}{2}\\text{sđ}\\overset\\frown{AB} = %s^\\circ$ và $\\widehat{BAC} = \\dfrac{1}{2}\\text{sđ}\\overset\\frown{BC} = %s^\\circ$. Vậy góc lớn nhất của $\\triangle ABC$ là $\\widehat{ABC} = %s^\\circ$.' % (goc_C, goc_A, goc_B)
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tam giác $ABC$ là tam giác %s' % (loai_tg)
    vdc_da_1_s = 'Tam giác $ABC$ là tam giác tù'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Ba góc của $\\triangle ABC$ có số đo lần lượt là $%s^\\circ, %s^\\circ, %s^\\circ$ nên $\\triangle ABC$ là tam giác %s.' % (goc_A, goc_B, goc_C, loai_tg)
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
