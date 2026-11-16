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


def bt_dang11_p2_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        configs = [
            (2, 1, 1, 5, 3, 4, -14),
            (3, 2, 1, 8, 2, 3, -9)
        ]
        a1, b1, a2, b2, x_cmp, x_eq, x_neg = random.choice(configs)
        A_cmp_in = a1 * x_cmp + b1
        B_cmp_in = a2 * x_cmp + b2
        A_eq_in = a1 * x_eq + b1
        A_neg_in = a1 * x_neg + b1
        B_neg_in = a2 * x_neg + b2
        A_neg_val = round(A_neg_in / abs(A_neg_in) * (abs(A_neg_in)**(1/3)))
        B_neg_val = round(B_neg_in / abs(B_neg_in) * (abs(B_neg_in)**(1/3)))
        diff_neg = A_neg_val - B_neg_val

        noidungcauhoi = ('Cho hai căn thức $A(x) = \\sqrt[3]{%sx + %s}$ và $B(x) = \\sqrt[3]{x + %s}$. Xét tính đúng sai của các khẳng định sau:' % (a1, b1, b2))

        nb_da_1_d = '\\True Tại $x = %s$, giá trị của $A(%s)$ nhỏ hơn giá trị của $B(%s)$.' % (x_cmp, x_cmp, x_cmp)
        nb_da_1_s = 'Tại $x = %s$, giá trị của $A(%s)$ lớn hơn giá trị của $B(%s)$.' % (x_cmp, x_cmp, x_cmp)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Ta có $A(%s) = \\sqrt[3]{%s}$ và $B(%s) = \\sqrt[3]{%s}$. Vì $%s < %s$ nên $A(%s) < B(%s)$.' % (x_cmp, A_cmp_in, x_cmp, B_cmp_in, A_cmp_in, B_cmp_in, x_cmp, x_cmp))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Có duy nhất một giá trị của $x$ để $A(x) = B(x)$.'
        th_da_1_s = 'Có hai giá trị phân biệt của $x$ để $A(x) = B(x)$.'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Ta có $A(x) = B(x) \\Leftrightarrow \\sqrt[3]{%sx + %s} = \\sqrt[3]{x + %s} \\Leftrightarrow %sx + %s = x + %s \\Leftrightarrow x = %s$ (duy nhất).' % (a1, b1, b2, a1, b1, b2, x_eq))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Khi $x = %s$, giá trị của $A(%s)$ và $B(%s)$ đều bằng $\\sqrt[3]{%s}$.' % (x_eq, x_eq, x_eq, A_eq_in)
        vd_da_1_s = 'Khi $x = %s$, tổng $A(%s) + B(%s)$ là một số nguyên.' % (x_eq, x_eq, x_eq)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Thay $x = %s$, ta được $A(%s) = B(%s) = \\sqrt[3]{%s}$ (là số vô tỉ nên tổng của chúng không phải số nguyên).' % (x_eq, x_eq, x_eq, A_eq_in))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Khi $x = %s$, giá trị của biểu thức $A(%s) - B(%s)$ bằng $%s$.' % (x_neg, x_neg, x_neg, diff_neg)
        vdc_da_1_s = 'Khi $x = %s$, giá trị của biểu thức $A(%s) - B(%s)$ bằng $%s$.' % (x_neg, x_neg, x_neg, A_neg_val + B_neg_val)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Ta có $A(%s) = \\sqrt[3]{%s} = %s$ và $B(%s) = \\sqrt[3]{%s} = %s$. \\\\ Do đó $A(%s) - B(%s) = %s - (%s) = %s$.' % (x_neg, A_neg_in, A_neg_val, x_neg, B_neg_in, B_neg_val, x_neg, x_neg, A_neg_val, B_neg_val, diff_neg))
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

        combined_nb = list(zip([nb_da_1], list_nb_2))
        combined_th = list(zip([th_da_1], list_th_2))
        combined_vd = list(zip([vd_da_1], list_vd_2))
        combined_vdc = list(zip([vdc_da_1], list_vdc_2))

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
