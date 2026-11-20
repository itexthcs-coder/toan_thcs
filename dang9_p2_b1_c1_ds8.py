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


def bt_dang9_p2_b1_c1_ds8(self):
    # Dạng 9: Thu gọn đơn thức ba biến có hệ số thập phân và tính giá trị
    m = randint(2, 3)
    n = randint(1, 2)
    mu_y = 1 + m
    mu_z = 1 + n
    bac = 1 + mu_y + mu_z
    x0 = random.choice([4, 8])
    z0 = 2
    gt_b = int(-Rational(1, 2) * x0 * (Rational(1, 2) ** mu_y) * (z0 ** mu_z))

    noidungcauhoi = ('Cho đơn thức $B = xyz(-0,5)y^{%s}z^{%s}$.' % (m, n))

    nb_da_1_d = '\\True Dạng thu gọn của đơn thức $B$ là $-0,5xy^{%s}z^{%s}$.' % (mu_y, mu_z)
    nb_da_1_s = 'Dạng thu gọn của đơn thức $B$ là $-0,5xy^{%s}z^{%s}$.' % (m, n)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Ta thu gọn đơn thức $B$:\n'
                    '\\begin{align*}\n'
                    'B = xyz(-0,5)y^{%s}z^{%s} = -0,5x(y \\cdot y^{%s})(z \\cdot z^{%s}) = -0,5xy^{%s}z^{%s}.\n'
                    '\\end{align*}'
                    % (m, n, m, n, mu_y, mu_z))

    th_da_1_d = '\\True Bậc của đơn thức $B$ là $%s$.' % bac
    th_da_1_s = 'Bậc của đơn thức $B$ là $%s$.' % (mu_y + mu_z)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Đơn thức thu gọn $-0,5xy^{%s}z^{%s}$ có tổng số mũ của các biến là $1 + %s + %s = %s$ nên bậc của $B$ bằng $%s$.'
                    % (mu_y, mu_z, mu_y, mu_z, bac, bac))

    vd_da_1_d = '\\True Tại $y = 0,5$, giá trị của $y^{%s}$ bằng $\\frac{1}{%s}$.' % (mu_y, 2 ** mu_y)
    vd_da_1_s = 'Tại $y = 0,5$, giá trị của $y^{%s}$ bằng $\\frac{1}{%s}$.' % (mu_y, 2 * mu_y)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Tại $y = 0,5 = \\frac{1}{2}$, ta có $y^{%s} = \\left(\\frac{1}{2}\\right)^{%s} = \\frac{1}{%s}$.'
                    % (mu_y, mu_y, 2 ** mu_y))

    vdc_da_1_d = '\\True Giá trị của đơn thức $B$ tại $x = %s$; $y = 0,5$; $z = %s$ bằng $%s$.' % (x0, z0, gt_b)
    vdc_da_1_s = 'Giá trị của đơn thức $B$ tại $x = %s$; $y = 0,5$; $z = %s$ bằng $%s$.' % (x0, z0, -gt_b)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Thay $x = %s$; $y = 0,5 = \\frac{1}{2}$; $z = %s$ vào $B = -0,5xy^{%s}z^{%s}$, ta được:\n'
                     '\\begin{align*}\n'
                     'B = -\\frac{1}{2} \\cdot %s \\cdot \\frac{1}{%s} \\cdot %s^{%s} = %s.\n'
                     '\\end{align*}'
                     % (x0, z0, mu_y, mu_z, x0, 2 ** mu_y, z0, mu_z, gt_b))

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

    combined = list(zip([nb_da_1, th_da_1, vd_da_1, vdc_da_1],
                        [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers[0]) + '}\n'
               '{' + str(shuffled_answers[1]) + '}\n'
               '{' + str(shuffled_answers[2]) + '}\n'
               '{' + str(shuffled_answers[3]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions[0]) + '\n'
               '\\item ' + str(shuffled_solutions[1]) + '\n'
               '\\item ' + str(shuffled_solutions[2]) + '\n'
               '\\item ' + str(shuffled_solutions[3]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
