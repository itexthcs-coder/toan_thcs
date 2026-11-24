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


def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang2_p2_b2_c4_hh8(self):
    A, B, C, D, E, F = random.choice([('A', 'B', 'C', 'D', 'E', 'F'), ('M', 'N', 'P', 'H', 'I', 'K')])
    k = random.choice([2, 3, 4])
    ab, bc, ac = 5 * k, 7 * k, 6 * k
    de = ac // 2
    cv_def = (ab + bc + ac) // 2

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (1.5,3);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (4.5,0);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s)--(%s)--cycle;
\\fill (%s) circle (1pt) node[above] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[below] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, A, B, E, B, C, F, A, C, A, B, C, D, E, F, A, A, B, B, C, C, D, D, E, E, F, F))

    noidungcauhoi = ('''Cho tam giác $%s%s%s$ có ba cạnh $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$ (như hình vẽ).%s''' % (A, B, C, A, B, fmt_num(ab), B, C, fmt_num(bc), A, C, fmt_num(ac), D, E, F, A, B, B, C, C, A, hinhve))

    nb_da_1_d = '\\True Tam giác $%s%s%s$ có ba cạnh đều là các đường trung bình của tam giác $%s%s%s$' % (D, E, F, A, B, C)
    nb_da_1_s = 'Tam giác $%s%s%s$ có ba cạnh đều là các đường trung tuyến của tam giác $%s%s%s$' % (D, E, F, A, B, C)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Vì $%s, %s, %s$ lần lượt là trung điểm của các cạnh $%s%s, %s%s, %s%s$ nên $%s%s, %s%s, %s%s$ là ba đường trung bình của tam giác $%s%s%s$.' % (D, E, F, A, B, B, C, C, A, D, E, E, F, F, D, A, B, C)]

    th_da_1_d = '\\True Độ dài cạnh $%s%s$ bằng $%s\\text{ cm}$' % (D, E, fmt_num(de))
    th_da_1_s = 'Độ dài cạnh $%s%s$ bằng $%s\\text{ cm}$' % (D, E, fmt_num(ab // 2))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Vì $%s%s$ là đường trung bình ứng với cạnh $%s%s$ của tam giác $%s%s%s$ nên $%s%s = \\dfrac{1}{2}%s%s = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.' % (D, E, A, C, A, B, C, D, E, A, C, fmt_num(ac), fmt_num(de))]

    vd_da_1_d = '\\True Chu vi của tam giác $%s%s%s$ bằng $%s\\text{ cm}$' % (D, E, F, fmt_num(cv_def))
    vd_da_1_s = 'Chu vi của tam giác $%s%s%s$ bằng $%s\\text{ cm}$' % (D, E, F, fmt_num(ab + bc + ac))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Ta có $%s%s = \\dfrac{1}{2}%s%s$, $%s%s = \\dfrac{1}{2}%s%s$, $%s%s = \\dfrac{1}{2}%s%s$. Chu vi tam giác $%s%s%s$ là $\\dfrac{1}{2}(%s + %s + %s) = %s\\text{ cm}$.' % (D, E, A, C, E, F, A, B, F, D, B, C, D, E, F, fmt_num(ab), fmt_num(bc), fmt_num(ac), fmt_num(cv_def))]

    vdc_da_1_d = '\\True Tứ giác $%s%s%s%s$ là hình bình hành' % (D, E, C, F)
    vdc_da_1_s = 'Tứ giác $%s%s%s%s$ là hình chữ nhật' % (D, E, C, F)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Ta có $%s%s // %s%s$ và $%s%s = \\dfrac{1}{2}%s%s = %s%s$ (do $%s$ là trung điểm $%s%s$). Tứ giác $%s%s%s%s$ có hai cạnh đối $%s%s$ và $%s%s$ song song và bằng nhau nên là hình bình hành.' % (D, E, A, C, D, E, A, C, F, C, F, A, C, D, E, C, F, D, E, F, C)]

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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
