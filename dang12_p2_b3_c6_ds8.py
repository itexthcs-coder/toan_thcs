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
def bt_dang12_p2_b3_c6_ds8(self):
    # Dạng 12: Tìm điều kiện hoặc giá trị của biến từ kết quả phép cộng/trừ phân thức
    # A = (m + 1)/(x - 1) - m/(x + 1) = (x + 2m + 1)/(x^2 - 1)
    m = random.choice([2, 3, 4, 5])
    m1 = m + 1
    c = 2 * m + 1
    # A = 1 <=> x + c = x^2 - 1 <=> x^2 - x - (c + 1) = 0
    # Với m = 2 => c = 5 => x^2 - x - 6 = 0 => (x - 3)(x + 2) = 0 (2 nghiệm: 3 và -2)
    # Với m = 3 => c = 7 => x^2 - x - 8 = 0 (Delta = 33 > 0, nghiệm vô tỉ khác +-1)
    # Chọn m = 2 hoặc m = 5 (c = 11 => x^2 - x - 12 = 0 => (x - 4)(x + 3) = 0) để nghiệm nguyên đẹp!
    m, m1, c, r1, r2 = random.choice([(2, 3, 5, 3, -2), (5, 6, 11, 4, -3)])
    
    noidungcauhoi = ('Cho biểu thức $A = \\dfrac{%s}{x - 1} - \\dfrac{%s}{x + 1}$ (với $x \\neq \\pm 1$). Xét tính đúng, sai của các khẳng định sau:' % (m1, m))
    
    list_nb_da_1 = [
        '\\True Rút gọn biểu thức ta được $A = \\dfrac{x + %s}{x^2 - 1}$' % c,
        'Rút gọn biểu thức ta được $A = \\dfrac{x - 1}{x^2 - 1}$'
    ]
    loigiai_nb_1 = ('Ta có: $A = \\dfrac{%s(x + 1) - %s(x - 1)}{x^2 - 1} = \\dfrac{%sx + %s - %sx + %s}{x^2 - 1} = \\dfrac{x + %s}{x^2 - 1}$.' % (m1, m, m1, m1, m, m, c))
    
    list_th_da_1 = [
        '\\True Để $A = 0$ thì giá trị của $x$ bằng $-%s$' % c,
        'Để $A = 0$ thì giá trị của $x$ bằng $%s$' % c
    ]
    loigiai_th_1 = ('Ta có $A = 0 \\Leftrightarrow x + %s = 0 \\Leftrightarrow x = -%s$ (thỏa mãn điều kiện $x \\neq \\pm 1$).' % (c, c))
    
    list_vd_da_1 = [
        '\\True Với $x = %s$, giá trị của $A$ bằng $1$' % r1,
        'Với $x = %s$, giá trị của $A$ bằng $-1$' % r1
    ]
    loigiai_vd_1 = ('Thay $x = %s$ vào $A$, ta được $A = \\dfrac{%s + %s}{%s^2 - 1} = \\dfrac{%s}{%s} = 1$.' % (r1, r1, c, r1, r1 + c, r1 ** 2 - 1))
    
    list_vdc_da_1 = [
        '\\True Có đúng hai giá trị của $x$ thỏa mãn $A = 1$, đó là $x = %s$ và $x = %s$' % (r1, r2),
        'Chỉ có duy nhất một giá trị của $x$ thỏa mãn $A = 1$'
    ]
    loigiai_vdc_1 = ('Ta có $A = 1 \\Leftrightarrow x + %s = x^2 - 1 \\Leftrightarrow x^2 - x - %s = 0 \\Leftrightarrow (x - %s)(x + %s) = 0$, tìm được $x = %s$ hoặc $x = %s$ (cả hai đều thỏa mãn $x \\neq \\pm 1$).' % (c, c + 1, r1, abs(r2), r1, r2))
    
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
