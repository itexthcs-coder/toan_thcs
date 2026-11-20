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


def bt_dang5_p2_b1_c1_ds8(self):
    # Dạng 5: Thu gọn đơn thức ba biến có hệ số thập phân và số nguyên âm
    a_dec = random.choice(['2,5', '3,5', '4,5', '1,5'])
    a_val = Rational(a_dec.replace(',', '.'))
    b = random.choice([-4, -2])
    hs_kq = int(a_val * b)
    m = randint(2, 4)
    mu_x = m + 1
    mu_y = 2
    tong_xy = mu_x + mu_y
    bac_kq = tong_xy + 1

    noidungcauhoi = ('Cho đơn thức $K = %sx^{%s}y(%s)xyz$.' % (a_dec, m, b))

    nb_da_1_d = '\\True Dạng thu gọn của đơn thức $K$ là $%sx^{%s}y^{2}z$.' % (hs_kq, mu_x)
    nb_da_1_s = 'Dạng thu gọn của đơn thức $K$ là $%sx^{%s}yz$.' % (hs_kq, mu_x)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Ta thu gọn đơn thức $K$ như sau:\n'
                    '\\begin{align*}\n'
                    'K = %sx^{%s}y(%s)xyz = [%s \\cdot (%s)] \\cdot (x^{%s} \\cdot x) \\cdot (y \\cdot y) \\cdot z = %sx^{%s}y^{2}z.\n'
                    '\\end{align*}'
                    % (a_dec, m, b, a_dec, b, m, hs_kq, mu_x))

    th_da_1_d = '\\True Hệ số của đơn thức $K$ là $%s$.' % hs_kq
    th_da_1_s = 'Hệ số của đơn thức $K$ là $%s$.' % abs(hs_kq)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Đơn thức thu gọn $%sx^{%s}y^{2}z$ có hệ số là $%s$.' % (hs_kq, mu_x, hs_kq))

    vd_da_1_d = '\\True Tổng số mũ của biến $x$ và biến $y$ trong đơn thức thu gọn $K$ bằng $%s$.' % tong_xy
    vd_da_1_s = 'Tổng số mũ của biến $x$ và biến $y$ trong đơn thức thu gọn $K$ bằng $%s$.' % bac_kq
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Trong đơn thức thu gọn $%sx^{%s}y^{2}z$, biến $x$ có số mũ $%s$ và biến $y$ có số mũ $2$ nên tổng số mũ của chúng bằng $%s + 2 = %s$.'
                    % (hs_kq, mu_x, mu_x, mu_x, tong_xy))

    vdc_da_1_d = '\\True Bậc của đơn thức $K$ là $%s$.' % bac_kq
    vdc_da_1_s = 'Bậc của đơn thức $K$ là $%s$.' % tong_xy
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng số mũ của các biến $x, y, z$ trong đơn thức thu gọn $%sx^{%s}y^{2}z$ là $%s + 2 + 1 = %s$, nên bậc của $K$ bằng $%s$.'
                     % (hs_kq, mu_x, mu_x, bac_kq, bac_kq))

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
