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
def bt_dang9_p2_b3_c6_ds8(self):
    # Dạng 9: Cộng, trừ phân thức có mẫu là hằng đẳng thức lập phương
    a = random.choice([1, 2, 3])
    k = random.choice([2, 3, 4])
    a2 = a ** 2
    a3 = a ** 3
    str_ax = 'x' if a == 1 else '%sx' % a
    
    noidungcauhoi = ('Cho biểu thức $K = \\dfrac{x^2 - %s + %s}{x^3 + %s} + \\dfrac{%s}{x + %s}$ (với $x \\neq -%s$). Xét tính đúng, sai của các khẳng định sau:' % (str_ax, a2, a3, k, a, a))
    
    list_nb_da_1 = [
        '\\True Phân tích mẫu thức thứ nhất ta có $x^3 + %s = (x + %s)(x^2 - %s + %s)$' % (a3, a, str_ax, a2),
        'Phân tích mẫu thức thứ nhất ta có $x^3 + %s = (x + %s)(x^2 + %s + %s)$' % (a3, a, str_ax, a2)
    ]
    loigiai_nb_1 = ('Áp dụng hằng đẳng thức tổng hai lập phương: $x^3 + %s^3 = (x + %s)(x^2 - %s + %s)$.' % (a, a, str_ax, a2))
    
    list_th_da_1 = [
        '\\True Mẫu thức chung đơn giản nhất của hai phân thức là $(x + %s)(x^2 - %s + %s)$' % (a, str_ax, a2),
        'Mẫu thức chung đơn giản nhất của hai phân thức là $(x + %s)^2(x^2 - %s + %s)$' % (a, str_ax, a2)
    ]
    loigiai_th_1 = ('Vì $x^3 + %s$ chia hết cho $x + %s$ nên mẫu thức chung là $x^3 + %s = (x + %s)(x^2 - %s + %s)$.' % (a3, a, a3, a, str_ax, a2))
    
    list_vd_da_1 = [
        '\\True Rút gọn phân thức thứ nhất rồi cộng với phân thức thứ hai, ta được $K = \\dfrac{%s}{x + %s}$' % (k + 1, a),
        'Rút gọn biểu thức ta được $K = \\dfrac{%s}{x^2 - %s + %s}$' % (k + 1, str_ax, a2)
    ]
    loigiai_vd_1 = ('Ta có: $\\dfrac{x^2 - %s + %s}{x^3 + %s} = \\dfrac{x^2 - %s + %s}{(x + %s)(x^2 - %s + %s)} = \\dfrac{1}{x + %s}$. Do đó $K = \\dfrac{1}{x + %s} + \\dfrac{%s}{x + %s} = \\dfrac{%s}{x + %s}$.' % (str_ax, a2, a3, str_ax, a2, a, str_ax, a2, a, a, k, a, k + 1, a))
    
    list_vdc_da_1 = [
        '\\True Tại $x = %s$, giá trị của $K$ bằng $1$' % (k + 1 - a),
        'Tại $x = %s$, giá trị của $K$ bằng $0$' % (k + 1 - a)
    ]
    loigiai_vdc_1 = ('Tại $x = %s$ (thỏa mãn $x \\neq -%s$), ta có $K = \\dfrac{%s}{%s + %s} = \\dfrac{%s}{%s} = 1$.' % (k + 1 - a, a, k + 1, k + 1 - a, a, k + 1, k + 1))
    
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
