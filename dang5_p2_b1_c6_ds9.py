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


def bt_dang5_p2_b1_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    x_sample = random.randint(6, 12)
    s_sample = x_sample ** 2
    k_mult = random.choice([3, 4, 5])
    k_sq = k_mult ** 2

    tikz_code = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (2.5,0);\n'
        '\\coordinate (C) at (2.5,2.5);\n'
        '\\coordinate (D) at (0,2.5);\n'
        '\\draw[line width=1pt] (A) -- (B) -- (C) -- (D) -- cycle;\n'
        '\\fill (A) circle (1pt) node[below left] {$A$};\n'
        '\\fill (B) circle (1pt) node[below right] {$B$};\n'
        '\\fill (C) circle (1pt) node[above right] {$C$};\n'
        '\\fill (D) circle (1pt) node[above left] {$D$};\n'
        '\\node[below] at (1.25,0) {$x\\text{ (m)}$};\n'
        '\\node[left] at (0,1.25) {$x\\text{ (m)}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một mảnh vườn hình vuông $ABCD$ có độ dài cạnh là $x$ (mét) ($x > 0$). Gọi $S$ ($\\text{m}^2$) là diện tích của mảnh vườn đó.%s' % (tikz_code)
    )

    nb_da_1_d = '\\True Công thức biểu thị $S$ theo $x$ là $S = x^2$, đây là hàm số dạng $y = ax^2$ với hệ số $a = 1$'
    nb_da_1_s = 'Công thức biểu thị $S$ theo $x$ là $S = 4x$, đây là hàm số bậc nhất'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Diện tích hình vuông cạnh $x$ được tính theo công thức $S = x^2$, có dạng $y = ax^2$ với $a = 1 \\ne 0$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Nếu diện tích mảnh vườn là $%s\\text{ m}^2$ thì độ dài cạnh vườn là $%s\\text{ m}$' % (fmt_num(s_sample), fmt_num(x_sample))
    th_da_1_s = 'Nếu diện tích mảnh vườn là $%s\\text{ m}^2$ thì độ dài cạnh vườn là $%s\\text{ m}$' % (fmt_num(s_sample), fmt_num(s_sample // 4))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay $S = %s$ vào công thức $S = x^2$ ta được: $x^2 = %s$. \\\\ Vì $x > 0$ nên suy ra $x = %s\\text{ (m)}$.' % (fmt_num(s_sample), fmt_num(s_sample), fmt_num(x_sample))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu tăng độ dài cạnh $x$ lên $%s$ lần thì diện tích $S$ tăng lên $%s$ lần' % (fmt_num(k_mult), fmt_num(k_sq))
    vd_da_1_s = 'Nếu tăng độ dài cạnh $x$ lên $%s$ lần thì diện tích $S$ tăng lên $%s$ lần' % (fmt_num(k_mult), fmt_num(2 * k_mult))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Khi tăng độ dài cạnh lên $%s$ lần, cạnh mới là $%sx$. \\\\ Diện tích mới của mảnh vườn là $S\\prime = (%sx)^2 = %sx^2 = %sS$. Vậy diện tích tăng lên $%s$ lần.' % (fmt_num(k_mult), fmt_num(k_mult), fmt_num(k_mult), fmt_num(k_sq), fmt_num(k_sq), fmt_num(k_sq))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khi độ dài cạnh $x$ giảm đi một nửa thì diện tích $S$ chỉ bằng $\\frac{1}{4}$ diện tích ban đầu'
    vdc_da_1_s = 'Khi độ dài cạnh $x$ giảm đi một nửa thì diện tích $S$ bằng $\\frac{1}{2}$ diện tích ban đầu'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Khi độ dài cạnh giảm đi một nửa, cạnh mới là $\\frac{x}{2}$. \\\\ Diện tích mới là $S\\prime = \\left(\\frac{x}{2}\\right)^2 = \\frac{1}{4}x^2 = \\frac{1}{4}S$. Vậy diện tích mới bằng $\\frac{1}{4}$ diện tích ban đầu.'
    )
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
