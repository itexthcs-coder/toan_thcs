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


def bt_dang11_p2_b1_c1_ds8(self):
    # Dạng 11: Tìm điều kiện tham số số mũ nguyên dương để hai đơn thức đồng dạng
    n0 = randint(4, 7)
    y_mu = randint(2, 5)
    m0 = y_mu + 1
    bac_dd = n0 + y_mu
    tu = random.choice([3, 5, 7])
    mau = random.choice([2, 4])
    b_hs = random.choice([-4, -3, -2])
    hs_tong = Rational(tu, mau) + b_hs

    noidungcauhoi = ('Cho hai đơn thức $A = \\frac{%s}{%s}x^{n}y^{%s}$ và $B = %sx^{%s}y^{m-1}$ (với $m, n$ là các số nguyên dương, $m > 1$).'
                     % (tu, mau, y_mu, b_hs, n0))

    nb_da_1_d = '\\True Để hai đơn thức $A$ và $B$ đồng dạng thì $n = %s$ và $m = %s$.' % (n0, m0)
    nb_da_1_s = 'Để hai đơn thức $A$ và $B$ đồng dạng thì $n = %s$ và $m = %s$.' % (n0, y_mu)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Để $A$ và $B$ đồng dạng thì phần biến phải giống nhau, tức là $n = %s$ và $m - 1 = %s \\Rightarrow m = %s$.'
                    % (n0, y_mu, m0))

    th_da_1_d = '\\True Khi $A$ và $B$ đồng dạng, bậc của mỗi đơn thức bằng $%s$.' % bac_dd
    th_da_1_s = 'Khi $A$ và $B$ đồng dạng, bậc của mỗi đơn thức bằng $%s$.' % (n0 + m0)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Khi $n = %s$ và $m = %s$, phần biến của mỗi đơn thức là $x^{%s}y^{%s}$ nên bậc bằng $%s + %s = %s$.'
                    % (n0, m0, n0, y_mu, n0, y_mu, bac_dd))

    vd_da_1_d = '\\True Khi $A$ và $B$ đồng dạng, tổng $A + B$ có hệ số bằng $%s$.' % latex(hs_tong)
    vd_da_1_s = 'Khi $A$ và $B$ đồng dạng, tổng $A + B$ có hệ số bằng $%s$.' % latex(Rational(tu, mau) - b_hs)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Khi $A$ và $B$ đồng dạng, hệ số của $A + B$ là $\\frac{%s}{%s} + (%s) = %s$.'
                    % (tu, mau, b_hs, latex(hs_tong)))

    vdc_da_1_d = '\\True Nếu $n = %s$ và $m = %s$ thì $A$ và $B$ không đồng dạng dù có cùng bậc.' % (n0 - 1, m0 + 1)
    vdc_da_1_s = 'Nếu $n = %s$ và $m = %s$ thì $A$ và $B$ vẫn đồng dạng vì có cùng bậc.' % (n0 - 1, m0 + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Với $n = %s$ và $m = %s$, đơn thức $A$ có phần biến $x^{%s}y^{%s}$ còn $B$ có phần biến $x^{%s}y^{%s}$. Hai phần biến khác nhau nên $A$ và $B$ không đồng dạng.'
                     % (n0 - 1, m0 + 1, n0 - 1, y_mu, n0, y_mu + 1))

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
