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


def bt_dang4_p2_b1_c1_ds8(self):
    # Dạng 4: Thu gọn đơn thức có hệ số là biểu thức số kết hợp phân số
    mau = random.choice([3, 5, 7])
    k = random.choice([2, 3, 4])
    tong_so = k * mau
    a = randint(1, 3)
    b = 2
    c_dec_val = Rational(tong_so - a, b)
    c_str = str(float(c_dec_val)).replace('.', ',')
    if c_str.endswith(',0'):
        c_str = c_str[:-2]
    m = randint(2, 4)
    n = randint(2, 4)
    mu_y = 1 + n
    bac_kq = m + mu_y

    noidungcauhoi = ('Cho đơn thức $Q = (%s + %s \\cdot %s)x^{%s}y \\cdot \\frac{1}{%s}y^{%s}$.'
                     % (a, b, c_str, m, mau, n))

    nb_da_1_d = '\\True Giá trị của biểu thức số $(%s + %s \\cdot %s)$ bằng $%s$.' % (a, b, c_str, tong_so)
    nb_da_1_s = 'Giá trị của biểu thức số $(%s + %s \\cdot %s)$ bằng $%s$.' % (a, b, c_str, tong_so + 1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Ta tính giá trị phần số trong ngoặc: $%s + %s \\cdot %s = %s + %s = %s$.'
                    % (a, b, c_str, a, tong_so - a, tong_so))

    th_da_1_d = '\\True Đơn thức $Q$ sau khi thu gọn có hệ số bằng $%s$.' % k
    th_da_1_s = 'Đơn thức $Q$ sau khi thu gọn có hệ số bằng $%s$.' % tong_so
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Ta thu gọn đơn thức $Q$:\n'
                    '\\begin{align*}\n'
                    'Q = %sx^{%s}y \\cdot \\frac{1}{%s}y^{%s} = \\left(%s \\cdot \\frac{1}{%s}\\right)x^{%s}(y \\cdot y^{%s}) = %sx^{%s}y^{%s}.\n'
                    '\\end{align*}\n'
                    'Vậy hệ số của đơn thức thu gọn $Q$ bằng $%s$.'
                    % (tong_so, m, mau, n, tong_so, mau, m, n, k, m, mu_y, k))

    vd_da_1_d = '\\True Phần biến của đơn thức thu gọn $Q$ là $x^{%s}y^{%s}$.' % (m, mu_y)
    vd_da_1_s = 'Phần biến của đơn thức thu gọn $Q$ là $x^{%s}y^{%s}$.' % (m, n)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Phần biến của đơn thức thu gọn $Q = %sx^{%s}y^{%s}$ là $x^{%s}y^{%s}$.'
                    % (k, m, mu_y, m, mu_y))

    vdc_da_1_d = '\\True Bậc của đơn thức $Q$ bằng $%s$.' % bac_kq
    vdc_da_1_s = 'Bậc của đơn thức $Q$ bằng $%s$.' % (m + n)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng số mũ của các biến trong đơn thức thu gọn $Q = %sx^{%s}y^{%s}$ là $%s + %s = %s$, nên bậc của $Q$ bằng $%s$.'
                     % (k, m, mu_y, m, mu_y, bac_kq, bac_kq))

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
