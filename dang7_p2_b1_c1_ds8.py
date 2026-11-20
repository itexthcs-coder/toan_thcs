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


def bt_dang7_p2_b1_c1_ds8(self):
    # Dạng 7: Sắp xếp các đơn thức thành từng nhóm đồng dạng và tính tổng, hiệu từng nhóm
    k = randint(2, 5)
    c3 = k + 1
    m = randint(3, 5)
    hs1_dec = random.choice(['0,5', '0,25', '1,5'])
    hs2_dec = random.choice(['2,75', '3,25', '4,5'])
    hieu_dec = str(float(Rational(hs2_dec.replace(',', '.')) - Rational(hs1_dec.replace(',', '.')))).replace('.', ',')
    if hieu_dec.endswith(',0'):
        hieu_dec = hieu_dec[:-2]

    noidungcauhoi = ('Cho các đơn thức: $\\frac{5}{3}x^{2}y$; $-xy^{2}$; $%sx^{%s}$; $-%sxy^{2}$; $%sx^{%s}$; $-\\frac{1}{4}x^{2}y$; $%sxy^{2}$.'
                     % (hs1_dec, m, k, hs2_dec, m, c3))

    nb_da_1_d = '\\True Khi sắp xếp thành các nhóm đơn thức đồng dạng, ta chia được thành $3$ nhóm.'
    nb_da_1_s = 'Khi sắp xếp thành các nhóm đơn thức đồng dạng, ta chia được thành $4$ nhóm.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Ta chia được thành $3$ nhóm đơn thức đồng dạng:\\\\\n'
                    '- Nhóm 1 (phần biến $x^{2}y$): $\\frac{5}{3}x^{2}y$ và $-\\frac{1}{4}x^{2}y$.\\\\\n'
                    '- Nhóm 2 (phần biến $xy^{2}$): $-xy^{2}$; $-%sxy^{2}$ và $%sxy^{2}$.\\\\\n'
                    '- Nhóm 3 (phần biến $x^{%s}$): $%sx^{%s}$ và $%sx^{%s}$.'
                    % (k, c3, m, hs1_dec, m, hs2_dec, m))

    th_da_1_d = '\\True Nhóm các đơn thức đồng dạng có phần biến $xy^{2}$ gồm $3$ đơn thức.'
    th_da_1_s = 'Nhóm các đơn thức đồng dạng có phần biến $xy^{2}$ gồm $2$ đơn thức.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Nhóm có phần biến $xy^{2}$ gồm $3$ đơn thức là: $-xy^{2}$; $-%sxy^{2}$ và $%sxy^{2}$.'
                    % (k, c3))

    vd_da_1_d = '\\True Tổng của các đơn thức trong nhóm có phần biến $xy^{2}$ bằng $0$.'
    vd_da_1_s = 'Tổng của các đơn thức trong nhóm có phần biến $xy^{2}$ bằng $xy^{2}$.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Tổng của ba đơn thức đồng dạng trong nhóm có phần biến $xy^{2}$ là:\n'
                    '\\begin{align*}\n'
                    '-xy^{2} + (-%sxy^{2}) + %sxy^{2} = (-1 - %s + %s)xy^{2} = 0 \\cdot xy^{2} = 0.\n'
                    '\\end{align*}'
                    % (k, c3, k, c3))

    vdc_da_1_d = '\\True Hiệu của hai đơn thức $%sx^{%s}$ và $%sx^{%s}$ là $%sx^{%s}$.' % (hs2_dec, m, hs1_dec, m, hieu_dec, m)
    vdc_da_1_s = 'Hiệu của hai đơn thức $%sx^{%s}$ và $%sx^{%s}$ là $%s$.' % (hs2_dec, m, hs1_dec, m, hieu_dec)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Ta có: $%sx^{%s} - %sx^{%s} = (%s - %s)x^{%s} = %sx^{%s}$.'
                     % (hs2_dec, m, hs1_dec, m, hs2_dec, hs1_dec, m, hieu_dec, m))

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
