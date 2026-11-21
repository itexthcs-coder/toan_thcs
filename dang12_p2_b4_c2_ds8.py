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


def bt_dang12_p2_b4_c2_ds8(self):
    y = symbols('y')
    a = random.randint(2, 4)
    b = random.randint(2, 5)
    # H = x^2 - a^2*y^2 + b*x + a*b*y = (x + a*y)(x - a*y + b)
    da_thuc = x**2 - (a**2)*(y**2) + b*x + a*b*y
    nt1 = x + a*y
    nt2 = x - a*y + b
    
    noidungcauhoi = ('''Cho biểu thức $H = %s$.''' % (latex(da_thuc)))
    
    nb_da_1_d = '\\True Phân tích $H$ thành nhân tử ta được $H = (%s)(%s)$' % (latex(nt1), latex(nt2))
    nb_da_1_s = 'Phân tích $H$ thành nhân tử ta được $H = (%s)(%s)$' % (latex(x - a*y), latex(x + a*y + b))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['''Ta có $H = (x^2 - %sy^2) + (%sx + %sy) = (%s)(%s) + %s(%s) = (%s)(%s)$.'''
                 % (a**2, b, a*b, latex(x - a*y), latex(nt1), b, latex(nt1), latex(nt1), latex(nt2))]
    
    val_tong = 100
    val_hieu = random.randint(5, 12)
    kq_th = val_tong * (val_hieu + b)
    th_da_1_d = '\\True Nếu $%s = %s$ và $%s = %s$ thì giá trị của $H$ bằng $%s$' % (latex(nt1), val_tong, latex(x - a*y), val_hieu, kq_th)
    th_da_1_s = 'Nếu $%s = %s$ và $%s = %s$ thì giá trị của $H$ bằng $%s$' % (latex(nt1), val_tong, latex(x - a*y), val_hieu, val_tong * val_hieu)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['''Thay $%s = %s$ và $%s = %s$, ta được $H = %s \\cdot (%s + %s) = %s$.'''
                 % (latex(nt1), val_tong, latex(x - a*y), val_hieu, val_tong, val_hieu, b, kq_th)]
    
    y_val = -1000
    x_val = -a * y_val
    vd_da_1_d = '\\True Khi $x = %s$ và $y = %s$ thì giá trị của biểu thức $H$ bằng $0$' % (x_val, y_val)
    vd_da_1_s = 'Khi $x = %s$ và $y = %s$ thì giá trị của biểu thức $H$ bằng $%s$' % (x_val, y_val, b)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['''Khi $x = %s$ và $y = %s$ thì $%s = %s + %s \\cdot (%s) = 0$, nên $H = 0$.'''
                 % (x_val, y_val, latex(nt1), x_val, a, y_val)]
    
    vdc_da_1_d = '\\True Có vô số cặp số $(x; y)$ thỏa mãn $H = 0$'
    vdc_da_1_s = 'Chỉ có duy nhất một cặp số $(x; y)$ thỏa mãn $H = 0$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['''Với mọi $y \\in \\mathbb{R}$, chọn $x = -%sy$ thì $%s = 0$ nên $H = 0$. Vậy có vô số cặp $(x; y)$ thỏa mãn.''' % (a, latex(nt1))]

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
