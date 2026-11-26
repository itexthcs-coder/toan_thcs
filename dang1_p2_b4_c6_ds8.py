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




def bt_dang1_p2_b4_c6_ds8(self):
    # Dạng 1: Phân tích các bước thực hiện phép nhân hai phân thức chứa đa thức bậc nhất và bậc hai
    a = random.randint(2, 5)
    k1 = random.choice([2, 3, 4])
    m = random.choice([2, 3])
    k2 = k1 * m
    
    tu1 = sp.expand(x**2 - a**2)
    mau1 = sp.expand(k1 * (x + a))
    tu2 = sp.expand(k2 * x)
    mau2 = sp.expand(x * (x - a))
    
    nb_da_1_d = '\\True Phân thức thứ nhất sau khi rút gọn bằng $\\frac{%s}{%s}$.' % (latex(x - a), k1)
    nb_da_1_s = 'Phân thức thứ nhất sau khi rút gọn bằng $\\frac{%s}{%s}$.' % (latex(x + a), k1)
    loigiai_nb_1 = """Ta có $\\frac{%s}{%s} = \\frac{(%s)(%s)}{%s(%s)} = \\frac{%s}{%s}$ (với $x \\neq -%s$).""" % (
        latex(tu1), latex(mau1), latex(x - a), latex(x + a), k1, latex(x + a), latex(x - a), k1, a
    )
    
    th_da_1_d = '\\True Phân thức thứ hai sau khi rút gọn bằng $\\frac{%s}{%s}$.' % (k2, latex(x - a))
    th_da_1_s = 'Phân thức thứ hai sau khi rút gọn bằng $\\frac{%s}{%s}$.' % (k2, latex(x + a))
    loigiai_th_1 = """Ta có $\\frac{%s}{%s} = \\frac{%s x}{x(%s)} = \\frac{%s}{%s}$ (với $x \\neq 0, x \\neq %s$).""" % (
        latex(tu2), latex(mau2), k2, latex(x - a), k2, latex(x - a), a
    )
    
    vd_da_1_d = '\\True Kết quả rút gọn của biểu thức $A$ là $%s$.' % m
    vd_da_1_s = 'Kết quả rút gọn của biểu thức $A$ là $%sx$.' % m
    loigiai_vd_1 = """Thực hiện phép nhân hai phân thức đã rút gọn, ta được: $A = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = %s$.""" % (
        latex(x - a), k1, k2, latex(x - a), m
    )
    
    vdc_da_1_d = '\\True Giá trị của biểu thức $A$ không phụ thuộc vào giá trị của biến $x$ (với $x \\neq 0, x \\neq \\pm %s$).' % a
    vdc_da_1_s = 'Giá trị của biểu thức $A$ phụ thuộc vào giá trị của biến $x$.'
    loigiai_vdc_1 = """Vì $A = %s$ là hằng số nên với mọi $x \\neq 0, x \\neq \\pm %s$, giá trị của $A$ luôn bằng $%s$ và không phụ thuộc vào biến $x$.""" % (m, a, m)
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho biểu thức $A = \\frac{%s}{%s} \\cdot \\frac{%s}{%s}$ với $x \\neq 0, x \\neq \\pm %s$. Xét tính đúng sai của các khẳng định sau:"""
                     % (latex(tu1), latex(mau1), latex(tu2), latex(mau2), a))
                     
    combined_nb = [(nb_da_1, loigiai_nb_1)]
    combined_th = [(th_da_1, loigiai_th_1)]
    combined_vd = [(vd_da_1, loigiai_vd_1)]
    combined_vdc = [(vdc_da_1, loigiai_vdc_1)]
    
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
