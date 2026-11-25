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


def bt_dang7_p2_b2_c6_ds8(self):
    # Dạng 7: Tìm đa thức thích hợp thay thế cho dấu ? qua nhiều bước biến đổi
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([2, 3, 5])
        while a == b:
            b = random.choice([2, 3, 5])

        noidungcauhoi = ('Xét các đẳng thức phân thức sau (giả thiết các phân thức đều có nghĩa). Xét tính đúng sai của các khẳng định sau:')

        # Ý a
        nb_da_1_d = '\\True Trong đẳng thức $\\dfrac{%sx - y}{%s - x} = \\dfrac{A}{x - %s}$, đa thức $A$ là $y - %sx$' % (a, b, b, a)
        nb_da_1_s = 'Trong đẳng thức $\\dfrac{%sx - y}{%s - x} = \\dfrac{A}{x - %s}$, đa thức $A$ là $%sx - y$' % (a, b, b, a)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Áp dụng quy tắc đổi dấu cả tử và mẫu: $\\dfrac{%sx - y}{%s - x} = \\dfrac{-(%sx - y)}{-(%s - x)} = \\dfrac{y - %sx}{x - %s}$, suy ra $A = y - %sx$.' % (a, b, a, b, a, b, a))
        list_nb_2 = [loigiai_nb_1]

        # Ý b
        tu_b_dung = latex(expand((x + a) * (x + 1)))
        tu_b_sai = latex(expand((x + a) * (x - 1)))
        th_da_1_d = '\\True Trong đẳng thức $\\dfrac{x + %s}{x - 1} = \\dfrac{B}{x^2 - 1}$, đa thức $B$ là $%s$' % (a, tu_b_dung)
        th_da_1_s = 'Trong đẳng thức $\\dfrac{x + %s}{x - 1} = \\dfrac{B}{x^2 - 1}$, đa thức $B$ là $%s$' % (a, tu_b_sai)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Vì $x^2 - 1 = (x - 1)(x + 1)$ nên ta nhân cả tử và mẫu của phân thức vế trái với $(x + 1)$: $B = (x + %s)(x + 1) = %s$.' % (a, tu_b_dung))
        list_th_2 = [loigiai_th_1]

        # Ý c
        vd_da_1_d = '\\True Trong đẳng thức $\\dfrac{x^2 - %sx}{x^2 - %s} = \\dfrac{x}{C}$, đa thức $C$ là $x + %s$' % (b, b**2, b)
        vd_da_1_s = 'Trong đẳng thức $\\dfrac{x^2 - %sx}{x^2 - %s} = \\dfrac{x}{C}$, đa thức $C$ là $x - %s$' % (b, b**2, b)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Ta có $\\dfrac{x^2 - %sx}{x^2 - %s} = \\dfrac{x(x - %s)}{(x - %s)(x + %s)} = \\dfrac{x}{x + %s}$, suy ra $C = x + %s$.' % (b, b**2, b, b, b, b, b))
        list_vd_2 = [loigiai_vd_1]

        # Ý d
        vdc_da_1_d = '\\True Trong đẳng thức $\\dfrac{x^3 - 1}{x^2 - 1} = \\dfrac{D}{x + 1}$, đa thức $D$ là $x^2 + x + 1$'
        vdc_da_1_s = 'Trong đẳng thức $\\dfrac{x^3 - 1}{x^2 - 1} = \\dfrac{D}{x + 1}$, đa thức $D$ là $x^2 - x + 1$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Ta có $\\dfrac{x^3 - 1}{x^2 - 1} = \\dfrac{(x - 1)(x^2 + x + 1)}{(x - 1)(x + 1)} = \\dfrac{x^2 + x + 1}{x + 1}$, suy ra $D = x^2 + x + 1$.')
        list_vdc_2 = [loigiai_vdc_1]

        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
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

    # Xuất câu hỏi trắc nghiệm đúng sai
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
