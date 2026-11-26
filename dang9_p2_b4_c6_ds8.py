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




def bt_dang9_p2_b4_c6_ds8(self):
    # Dạng 9: Tách phân thức thành hiệu hai phân thức để rút gọn tổng dây chuyền (VD1 Luyện tập chung SGK)
    n_terms = random.choice([3, 4])
    k_chia = n_terms * 2
    
    if n_terms == 3:
        bieu_thuc_F = '\\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)} + \\frac{1}{(x + 2)(x + 3)}'
        day_so = '\\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\frac{1}{3 \\cdot 4}'
        dk_x = 'x \\notin \\{0; -1; -2; -3\\}'
    else:
        bieu_thuc_F = '\\frac{1}{x(x + 1)} + \\frac{1}{(x + 1)(x + 2)} + \\frac{1}{(x + 2)(x + 3)} + \\frac{1}{(x + 3)(x + 4)}'
        day_so = '\\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\frac{1}{3 \\cdot 4} + \\frac{1}{4 \\cdot 5}'
        dk_x = 'x \\notin \\{0; -1; -2; -3; -4\\}'
        
    gt_day_so = Rational(n_terms, n_terms + 1)
    
    nb_da_1_d = '\\True Với mỗi số tự nhiên $k$, ta luôn có $\\frac{1}{(x + k)(x + k + 1)} = \\frac{1}{x + k} - \\frac{1}{x + k + 1}$.'
    nb_da_1_s = 'Với mỗi số tự nhiên $k$, ta luôn có $\\frac{1}{(x + k)(x + k + 1)} = \\frac{1}{x + k} + \\frac{1}{x + k + 1}$.'
    loigiai_nb_1 = """Ta có $\\frac{1}{x + k} - \\frac{1}{x + k + 1} = \\frac{(x + k + 1) - (x + k)}{(x + k)(x + k + 1)} = \\frac{1}{(x + k)(x + k + 1)}$."""
    
    th_da_1_d = '\\True Biểu thức $F$ rút gọn bằng $\\frac{%s}{x(x + %s)}$.' % (n_terms, n_terms)
    th_da_1_s = 'Biểu thức $F$ rút gọn bằng $\\frac{1}{x(x + %s)}$.' % n_terms
    loigiai_th_1 = """Áp dụng công thức tách trên và triệt tiêu các số hạng đối nhau, ta được $F = \\frac{1}{x} - \\frac{1}{x + %s} = \\frac{%s}{x(x + %s)}$.""" % (n_terms, n_terms, n_terms)
    
    vd_da_1_d = '\\True Giá trị của tổng $%s$ bằng $%s$.' % (day_so, latex(gt_day_so))
    vd_da_1_s = 'Giá trị của tổng $%s$ bằng $\\frac{1}{%s}$.' % (day_so, n_terms + 1)
    loigiai_vd_1 = """Thay $x = 1$ vào biểu thức rút gọn của $F$, ta được giá trị của tổng bằng $\\frac{%s}{1 \\cdot (1 + %s)} = %s$.""" % (n_terms, n_terms, latex(gt_day_so))
    
    vdc_da_1_d = '\\True Thương của phép chia $F : \\frac{%s}{x^2 + %sx}$ bằng $\\frac{1}{2}$.' % (k_chia, n_terms)
    vdc_da_1_s = 'Thương của phép chia $F : \\frac{%s}{x^2 + %sx}$ bằng $2$.' % (k_chia, n_terms)
    loigiai_vdc_1 = """Ta có $F : \\frac{%s}{x(x + %s)} = \\frac{%s}{x(x + %s)} \\cdot \\frac{x(x + %s)}{%s} = \\frac{%s}{%s} = \\frac{1}{2}$.""" % (
        k_chia, n_terms, n_terms, n_terms, n_terms, k_chia, n_terms, k_chia
    )
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho biểu thức $F = %s$ với $%s$. Xét tính đúng sai của các khẳng định sau:"""
                     % (bieu_thuc_F, dk_x))
                     
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(nb_da_1) + '}\n' +
               '{' + str(th_da_1) + '}\n' +
               '{' + str(vd_da_1) + '}\n' +
               '{' + str(vdc_da_1) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(loigiai_nb_1) + '\n' +
               '\\item ' + str(loigiai_th_1) + '\n' +
               '\\item ' + str(loigiai_vd_1) + '\n' +
               '\\item ' + str(loigiai_vdc_1) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
