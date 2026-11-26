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




def bt_dang13_p2_b4_c6_ds8(self):
    # Dạng 13: Biến đổi biểu thức hỗn hợp chứa dấu ngoặc (Bài 6.42c SGK)
    a = random.choice([2, 3])
    
    tu_nhan = sp.expand(x**2 - a**2)
    mau_nhan = sp.expand(4*x**2 - 1)
    tu_chia = sp.expand(2*x + 1)
    mau_chia = sp.expand(x * (2*x - 1))
    
    nb_da_1_d = '\\True Hiệu $\\frac{%s}{x + %s} - \\frac{%s}{1 - x}$ rút gọn bằng $\\frac{-%s(2x + 1)}{(x + %s)(1 - x)}$.' % (a, a, a, a, a)
    nb_da_1_s = 'Hiệu $\\frac{%s}{x + %s} - \\frac{%s}{1 - x}$ rút gọn bằng $\\frac{%s}{(x + %s)(1 - x)}$.' % (a, a, a, a, a)
    loigiai_nb_1 = """Ta có $\\frac{%s}{x + %s} - \\frac{%s}{1 - x} = \\frac{%s(1 - x) - %s(x + %s)}{(x + %s)(1 - x)} = \\frac{-%s(2x + 1)}{(x + %s)(1 - x)}$.""" % (
        a, a, a, a, a, a, a, a, a
    )
    
    th_da_1_d = '\\True Tích $\\left(\\frac{%s}{x + %s} - \\frac{%s}{1 - x}\\right) \\cdot \\frac{%s}{%s}$ bằng $\\frac{-%s(x - %s)}{(1 - x)(2x - 1)}$.' % (a, a, a, latex(tu_nhan), latex(mau_nhan), a, a)
    th_da_1_s = 'Tích $\\left(\\frac{%s}{x + %s} - \\frac{%s}{1 - x}\\right) \\cdot \\frac{%s}{%s}$ bằng $\\frac{%s(x - %s)}{(1 - x)(2x + 1)}$.' % (a, a, a, latex(tu_nhan), latex(mau_nhan), a, a)
    loigiai_th_1 = """Ta có $\\frac{-%s(2x + 1)}{(x + %s)(1 - x)} \\cdot \\frac{(x - %s)(x + %s)}{(2x - 1)(2x + 1)} = \\frac{-%s(x - %s)}{(1 - x)(2x - 1)}$.""" % (
        a, a, a, a, a, a
    )
    
    vd_da_1_d = '\\True Sau khi rút gọn, $L = \\frac{-%sx(x - %s)}{(1 - x)(2x + 1)}$.' % (a, a)
    vd_da_1_s = 'Sau khi rút gọn, $L = \\frac{-%s(x - %s)}{x(1 - x)(2x + 1)}$.' % (a, a)
    loigiai_vd_1 = """Ta có $L = \\frac{-%s(x - %s)}{(1 - x)(2x - 1)} \\cdot \\frac{x(2x - 1)}{2x + 1} = \\frac{-%sx(x - %s)}{(1 - x)(2x + 1)}$.""" % (a, a, a, a)
    
    vdc_da_1_d = '\\True Tại $x = %s$, biểu thức $L$ nhận giá trị bằng $0$.' % a
    vdc_da_1_s = 'Giá trị của biểu thức $L$ không phụ thuộc vào biến $x$.'
    loigiai_vdc_1 = """Thay $x = %s$ (thỏa mãn điều kiện xác định) vào $L = \\frac{-%sx(x - %s)}{(1 - x)(2x + 1)}$, ta được $L = 0$.""" % (a, a, a)
    
    while True:
        nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
        th_da_1 = random.choice([th_da_1_d, th_da_1_s])
        vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
        vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= sum('\\True' in ans for ans in answers) <= 3:
            break
            
    noidungcauhoi = ("""Cho biểu thức $L = \\left(\\frac{%s}{x + %s} - \\frac{%s}{1 - x}\\right) \\cdot \\frac{%s}{%s} : \\frac{%s}{%s}$ (với các mẫu thức và phân thức chia đều khác $0$). Xét tính đúng sai của các khẳng định sau:"""
                     % (a, a, a, latex(tu_nhan), latex(mau_nhan), latex(tu_chia), latex(mau_chia)))
                     
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
