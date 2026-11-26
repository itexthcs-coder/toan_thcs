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




def bt_dang20_p4_b4_c6_ds8(self):
    # Dạng 20: Bài toán hình học thực tế – Thiết kế khu vườn hình chữ nhật (có hình vẽ minh họa TikZ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3])
        b = random.choice([3, 4, 5])
        while a == b:
            b = random.choice([3, 4, 5])
        x0 = a + random.choice([2, 3])
        
        tu_S = sp.expand((x + b)*(x + a))
        mau_S = sp.expand(x + a)
        tu_R = sp.expand(x + b)
        mau_R = sp.expand(x**2 - a**2)
        
        # D = S / R = (x+b)(x+a)/(x+a) : (x+b)/((x-a)(x+a)) = (x-a)(x+a) = x^2 - a^2
        # Tỉ số D / R = (x^2 - a^2) : (x+b)/(x^2 - a^2) = (x^2 - a^2)^2 / (x + b)
        # Chọn x0 sao cho (x0^2 - a^2)^2 chia hết cho (x0 + b) hoặc tính chính xác phân số/số nguyên:
        cd_x0 = x0**2 - a**2
        cr_x0 = Rational(x0 + b, x0**2 - a**2)
        ti_so_x0 = Rational(cd_x0**2, x0 + b)
        chu_vi_x0 = 2 * (cd_x0 + cr_x0)
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.85]\n'
            '\\draw[thick, fill=teal!10] (0,0) rectangle (5.4,2.5);\n'
            '\\node[below] at (2.7,0) {Chiều dài $D$};\n'
            '\\node[right] at (5.4,1.25) {$R = \\frac{%s}{%s}\\text{ (m)}$};\n'
            '\\node at (2.7,1.25) {$S = \\frac{%s}{%s}\\text{ (m}^2\\text{)}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        ) % (latex(tu_R), latex(mau_R), latex(tu_S), latex(mau_S))
        
        noidungcauhoi = ("""Một mảnh đất hình chữ nhật có diện tích được biểu diễn bởi phân thức $S = \\frac{%s}{%s}\\text{ (m}^2\\text{)}$ và chiều rộng là $R = \\frac{%s}{%s}\\text{ (m)}$ với $x > %s$.
%s \\\\
        a) Viết phân thức rút gọn biểu thị chiều dài $D$ của mảnh đất theo biến $x$. \\\\
        b) Viết phân thức rút gọn biểu thị tỉ số giữa chiều dài và chiều rộng của mảnh đất, sau đó tính tỉ số này khi $x = %s$. \\\\
        c) Tính chu vi của mảnh đất khi $x = %s$."""
                         % (latex(tu_S), latex(mau_S), latex(tu_R), latex(mau_R), a, hinh_ve, x0, x0))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Chiều dài $D$ của mảnh đất hình chữ nhật là:\\\\
        $$D = S : R = \\frac{%s}{%s} : \\frac{%s}{%s} = \\frac{(x + %s)(x + %s)}{x + %s} \\cdot \\frac{(x - %s)(x + %s)}{x + %s} = (x - %s)(x + %s) = x^2 - %s\\text{ (m)}.$$ \n
        \\item Tỉ số giữa chiều dài và chiều rộng của mảnh đất là:\\\\
        $$\\frac{D}{R} = (x^2 - %s) : \\frac{x + %s}{x^2 - %s} = (x^2 - %s) \\cdot \\frac{x^2 - %s}{x + %s} = \\frac{(x^2 - %s)^2}{x + %s}.$$\\\\
        Khi $x = %s$, tỉ số này bằng $\\frac{(%s^2 - %s)^2}{%s + %s} = %s$. \n
        \\item Khi $x = %s$, mảnh đất có chiều dài $D = %s^2 - %s = %s\\text{ (m)}$ và chiều rộng $R = \\frac{%s + %s}{%s^2 - %s} = %s\\text{ (m)}$.\\\\
        Vậy chu vi của mảnh đất khi $x = %s$ là:\\\\
        $$2 \\cdot \\left(%s + %s\\right) = %s\\text{ (m)}.$$ \n
        \\end{enumEX} \n"""
                   % (latex(tu_S), latex(mau_S), latex(tu_R), latex(mau_R),
                      b, a, a, a, a, b, a, a, a**2,
                      a**2, b, a**2, a**2, a**2, b, a**2, b,
                      x0, x0, a**2, x0, b, latex(ti_so_x0),
                      x0, x0, a**2, cd_x0, x0, b, x0, a**2, latex(cr_x0),
                      x0, cd_x0, latex(cr_x0), latex(chu_vi_x0)))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
