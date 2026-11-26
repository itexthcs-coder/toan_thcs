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
def bt_dang14_p2_b3_c6_ds8(self):
    # Dạng 14: Thực hiện chuỗi phép cộng phân thức liên tiếp có quy luật (sai phân)
    a = random.choice([1, 2, 3, 4])
    a1 = a + 1
    
    noidungcauhoi = ('Cho biểu thức $C = \\dfrac{1}{(x + %s)(x + %s)} + \\dfrac{1}{(x + %s)(x + %s)}$ (với $x \\neq -%s, -%s, -%s$). Xét tính đúng, sai của các khẳng định sau:' % (a - 1 if a > 1 else 0, a, a, a1, a - 1 if a > 1 else 0, a, a1))
    # Xử lý riêng trường hợp a=1 cho đẹp (x(x+1))
    if a == 1:
        noidungcauhoi = ('Cho biểu thức $C = \\dfrac{1}{x(x + 1)} + \\dfrac{1}{(x + 1)(x + 2)}$ (với $x \\neq 0, -1, -2$). Xét tính đúng, sai của các khẳng định sau:')
        t1_str = '\\dfrac{1}{x(x + 1)} = \\dfrac{1}{x} - \\dfrac{1}{x + 1}'
        t1_sai = '\\dfrac{1}{x(x + 1)} = \\dfrac{1}{x} + \\dfrac{1}{x + 1}'
        t2_str = '\\dfrac{1}{(x + 1)(x + 2)} = \\dfrac{1}{x + 1} - \\dfrac{1}{x + 2}'
        t2_sai = '\\dfrac{1}{(x + 1)(x + 2)} = \\dfrac{1}{x + 2} - \\dfrac{1}{x + 1}'
        rut_gon = '\\dfrac{2}{x(x + 2)}'
        rut_gon_sai = '\\dfrac{1}{x(x + 2)}'
        gt_1 = '\\dfrac{2}{3}'
        gt_1_sai = '\\dfrac{1}{3}'
        lg_a = 'Ta có $\\dfrac{1}{x} - \\dfrac{1}{x + 1} = \\dfrac{(x + 1) - x}{x(x + 1)} = \\dfrac{1}{x(x + 1)}$.'
        lg_b = 'Tương tự, $\\dfrac{1}{x + 1} - \\dfrac{1}{x + 2} = \\dfrac{(x + 2) - (x + 1)}{(x + 1)(x + 2)} = \\dfrac{1}{(x + 1)(x + 2)}$.'
        lg_c = 'Cộng hai biểu thức: $C = \\left(\\dfrac{1}{x} - \\dfrac{1}{x + 1}\\right) + \\left(\\dfrac{1}{x + 1} - \\dfrac{1}{x + 2}\\right) = \\dfrac{1}{x} - \\dfrac{1}{x + 2} = \\dfrac{2}{x(x + 2)}$.'
        lg_d = 'Thay $x = 1$ vào $C$, ta được $C = \\dfrac{2}{1 \\cdot (1 + 2)} = \\dfrac{2}{3}$.'
    else:
        b = a - 1
        t1_str = '\\dfrac{1}{(x + %s)(x + %s)} = \\dfrac{1}{x + %s} - \\dfrac{1}{x + %s}' % (b, a, b, a)
        t1_sai = '\\dfrac{1}{(x + %s)(x + %s)} = \\dfrac{1}{x + %s} + \\dfrac{1}{x + %s}' % (b, a, b, a)
        t2_str = '\\dfrac{1}{(x + %s)(x + %s)} = \\dfrac{1}{x + %s} - \\dfrac{1}{x + %s}' % (a, a1, a, a1)
        t2_sai = '\\dfrac{1}{(x + %s)(x + %s)} = \\dfrac{1}{x + %s} - \\dfrac{1}{x + %s}' % (a, a1, a1, a)
        rut_gon = '\\dfrac{2}{(x + %s)(x + %s)}' % (b, a1)
        rut_gon_sai = '\\dfrac{1}{(x + %s)(x + %s)}' % (b, a1)
        num_1 = 2
        den_1 = (1 + b) * (1 + a1)
        g = math.gcd(num_1, den_1)
        gt_1 = '\\dfrac{%s}{%s}' % (num_1 // g, den_1 // g)
        gt_1_sai = '\\dfrac{1}{%s}' % den_1
        lg_a = 'Ta có $\\dfrac{1}{x + %s} - \\dfrac{1}{x + %s} = \\dfrac{(x + %s) - (x + %s)}{(x + %s)(x + %s)} = \\dfrac{1}{(x + %s)(x + %s)}$.' % (b, a, a, b, b, a, b, a)
        lg_b = 'Tương tự, $\\dfrac{1}{x + %s} - \\dfrac{1}{x + %s} = \\dfrac{(x + %s) - (x + %s)}{(x + %s)(x + %s)} = \\dfrac{1}{(x + %s)(x + %s)}$.' % (a, a1, a1, a, a, a1, a, a1)
        lg_c = 'Cộng hai biểu thức: $C = \\dfrac{1}{x + %s} - \\dfrac{1}{x + %s} = \\dfrac{2}{(x + %s)(x + %s)}$.' % (b, a1, b, a1)
        lg_d = 'Thay $x = 1$ vào $C$, ta được $C = \\dfrac{2}{%s \\cdot %s} = %s$.' % (1 + b, 1 + a1, gt_1)
        
    list_nb_da_1 = ['\\True Ta có $%s$' % t1_str, 'Ta có $%s$' % t1_sai]
    list_th_da_1 = ['\\True Tương tự, $%s$' % t2_str, 'Tương tự, $%s$' % t2_sai]
    list_vd_da_1 = ['\\True Tổng $C$ rút gọn thành $%s$' % rut_gon, 'Tổng $C$ rút gọn thành $%s$' % rut_gon_sai]
    list_vdc_da_1 = ['\\True Tại $x = 1$, giá trị của $C$ bằng $%s$' % gt_1, 'Tại $x = 1$, giá trị của $C$ bằng $%s$' % gt_1_sai]
    
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
            
    combined = list(zip(answers, [lg_a, lg_b, lg_c, lg_d]))
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
