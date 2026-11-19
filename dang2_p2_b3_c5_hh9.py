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
from PyQt5.QtGui import QTextCursor, QFont
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
from mpl_toolkits.mplot3d import Axes3D








def bt_dang2_p2_b3_c5_hh9(self):
    R_val = random.choice([6, 9, 12])
    sd_np = random.choice([80, 100, 120])
    sd_mn = (360 - sd_np) // 2

    l_np = Rational(sd_np, 180) * R_val * pi
    tong_l = 2 * Rational(sd_mn, 180) * R_val * pi

    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8]
        \\draw (0,0) circle (1.8cm);
        \\coordinate (M) at (90:1.8cm);
        \\coordinate (N) at (230:1.8cm);
        \\coordinate (P) at (310:1.8cm);
        \\draw[thick] (M) -- (N) -- (P) -- cycle;
        \\fill (0,0) circle (1.5pt) node[below] {$O$};
        \\node[above] at (M) {$M$};
        \\node[below left] at (N) {$N$};
        \\node[below right] at (P) {$P$};
    \\end{tikzpicture}
    \\end{center}''')

    noidungcauhoi = ('''Cho đường tròn $(O; %d\\text{ cm})$ và ba điểm $M, N, P$ thuộc đường tròn sao cho tam giác $MNP$ cân tại $M$ và số đo cung nhỏ $\\overset\\frown{NP}$ bằng $%d^\\circ$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s''' % (R_val, sd_np, hinh_ve))

    nb_da_1_d = '\\True Hai cung nhỏ $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ bằng nhau'
    nb_da_1_s = 'Cung nhỏ $\\overset\\frown{MN}$ lớn hơn cung nhỏ $\\overset\\frown{MP}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''Vì tam giác $MNP$ cân tại $M$ nên hai dây $MN = MP$, suy ra hai cung nhỏ $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ bằng nhau.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số đo của mỗi cung nhỏ $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ bằng $%d^\\circ$' % sd_mn
    th_da_1_s = 'Số đo của mỗi cung nhỏ $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ bằng $%d^\\circ$' % (180 - sd_np)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Ta có $\\text{sđ}\\overset\\frown{MN} + \\text{sđ}\\overset\\frown{MP} + \\text{sđ}\\overset\\frown{NP} = 360^\\circ$ mà $\\overset\\frown{MN} = \\overset\\frown{MP}$ nên $\\text{sđ}\\overset\\frown{MN} = \\text{sđ}\\overset\\frown{MP} = \\dfrac{360^\\circ - %d^\\circ}{2} = %d^\\circ$.''' % (sd_np, sd_mn))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Độ dài cung nhỏ $\\overset\\frown{NP}$ bằng $%s\\text{ cm}$' % latex(l_np)
    vd_da_1_s = 'Độ dài cung nhỏ $\\overset\\frown{NP}$ bằng $%s\\text{ cm}$' % latex(l_np + pi)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Độ dài cung nhỏ $\\overset\\frown{NP}$ là $l_{\\overset\\frown{NP}} = \\dfrac{%d}{180}\\pi \\cdot %d = %s\\text{ (cm)}$.''' % (sd_np, R_val, latex(l_np)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tổng độ dài hai cung nhỏ $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ bằng $%s\\text{ cm}$' % latex(tong_l)
    vdc_da_1_s = 'Tổng độ dài hai cung nhỏ $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ bằng $%s\\text{ cm}$' % latex(tong_l // 2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Tổng số đo hai cung $\\overset\\frown{MN}$ và $\\overset\\frown{MP}$ là $2 \\cdot %d^\\circ = %d^\\circ$. \\\\ Tổng độ dài hai cung nhỏ đó là $l = \\dfrac{%d}{180}\\pi \\cdot %d = %s\\text{ (cm)}$.''' % (sd_mn, 2*sd_mn, 2*sd_mn, R_val, latex(tong_l)))
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
