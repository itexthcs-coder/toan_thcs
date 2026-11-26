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
def bt_dang1_p2_b3_c6_ds8(self):
    # Dạng 1: Biến đổi tổng hai phân thức khác mẫu có tử là đa thức bậc nhất
    a = random.choice([2, 3, 4])
    b = random.choice([1, 2, 3])
    c = random.choice([2, 3, 4, 5])
    # A = (ax + 1)/(x - b), B = (c - x)/(x + b)
    # Tổng tử = (ax + 1)(x + b) + (c - x)(x - b) = (a - 1)x^2 + (ab + 1 + c + b)x + (b - bc)
    b2 = b ** 2
    coef_x2 = a - 1
    coef_x = a * b + 1 + c + b
    const_term = b - b * c
    
    str_x2 = 'x^2' if coef_x2 == 1 else '%sx^2' % coef_x2
    str_const = '+ %s' % const_term if const_term > 0 else '- %s' % abs(const_term) if const_term < 0 else ''
    tu_tong = '%s + %sx %s' % (str_x2, coef_x, str_const)
    tu_tong_sai = '%s + %sx %s' % (str_x2, coef_x + 2 * b, str_const)
    
    # Giá trị tại x = 0: 1/(-b) + c/b = (c - 1)/b
    gt_0_num = c - 1
    g = math.gcd(gt_0_num, b)
    num_s = gt_0_num // g
    den_s = b // g
    if den_s == 1:
        str_gt0 = '%s' % num_s
        str_gt0_sai = '%s' % (-num_s if num_s != 0 else 1)
    else:
        str_gt0 = '\\dfrac{%s}{%s}' % (num_s, den_s)
        str_gt0_sai = '\\dfrac{%s}{%s}' % (-num_s, den_s)
    
    noidungcauhoi = ('Cho hai phân thức $A = \\dfrac{%sx + 1}{x - %s}$ và $B = \\dfrac{%s - x}{x + %s}$ (với $x \\neq \\pm %s$). Xét tính đúng, sai của các khẳng định sau:' % (a, b, c, b, b))
    
    list_nb_da_1 = [
        '\\True Mẫu thức chung đơn giản nhất của $A$ và $B$ là $x^2 - %s$' % b2,
        'Mẫu thức chung đơn giản nhất của $A$ và $B$ là $x^2 + %s$' % b2
    ]
    loigiai_nb_1 = ('Vì $(x - %s)(x + %s) = x^2 - %s$ nên mẫu thức chung đơn giản nhất của $A$ và $B$ là $x^2 - %s$.' % (b, b, b2, b2))
    
    list_th_da_1 = [
        '\\True Quy đồng mẫu thức của $A$ ta được $\\dfrac{(%sx + 1)(x + %s)}{x^2 - %s}$' % (a, b, b2),
        'Quy đồng mẫu thức của $A$ ta được $\\dfrac{(%sx + 1)(x - %s)}{x^2 - %s}$' % (a, b, b2)
    ]
    loigiai_th_1 = ('Nhân cả tử và mẫu của phân thức $A$ với nhân tử phụ $x + %s$, ta được $A = \\dfrac{(%sx + 1)(x + %s)}{x^2 - %s}$.' % (b, a, b, b2))
    
    list_vd_da_1 = [
        '\\True Tổng $A + B$ bằng $\\dfrac{%s}{x^2 - %s}$' % (tu_tong, b2),
        'Tổng $A + B$ bằng $\\dfrac{%s}{x^2 - %s}$' % (tu_tong_sai, b2)
    ]
    loigiai_vd_1 = ('Ta có: $A + B = \\dfrac{(%sx + 1)(x + %s) + (%s - x)(x - %s)}{x^2 - %s} = \\dfrac{%s}{x^2 - %s}$.' % (a, b, c, b, b2, tu_tong, b2))
    
    list_vdc_da_1 = [
        '\\True Tại $x = 0$, giá trị của tổng $A + B$ bằng $%s$' % str_gt0,
        'Tại $x = 0$, giá trị của tổng $A + B$ bằng $%s$' % str_gt0_sai
    ]
    loigiai_vdc_1 = ('Tại $x = 0$ (thỏa mãn điều kiện $x \\neq \\pm %s$), ta có $A + B = \\dfrac{1}{-%s} + \\dfrac{%s}{%s} = %s$.' % (b, b, c, b, str_gt0))
    
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
            
    combined = list(zip(answers, [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
