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

def fmt_so(val):
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val < 0:
            return '-\\frac{%s}{%s}' % (abs(val.numerator), val.denominator)
        return '\\frac{%s}{%s}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        s = ('%g' % val).replace('.', ',')
        return s
    return str(val)

def fmt_dt(a, b):
    if a == 1:
        sa = 'x'
    elif a == -1:
        sa = '-x'
    else:
        sa = '%sx' % fmt_so(a)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_so(b))
    else:
        return '%s - %s' % (sa, fmt_so(abs(b)))

def bt_dang3_p4_b5_c7_ds8(self):
    # Dạng 3: Tìm tham số để ba đường thẳng đồng quy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x_int = random.choice([1, 2, 3, -1, -2])
        y_int = random.choice([1, 2, 3, 4, 5])
        a1 = random.choice([2, 3])
        b1 = y_int - a1 * x_int
        a2 = random.choice([-1, -2])
        b2 = y_int - a2 * x_int
        
        # d3: y = (k - 2)x + k + c3
        # Tai x_int: y_int = (k - 2)*x_int + k + c3 = k*(x_int + 1) - 2*x_int + c3
        k_dung = random.choice([3, 4, 5, -1, -2])
        if k_dung == 2 or k_dung - 2 == a1 or k_dung - 2 == a2:
            k_dung = 6
        c3 = y_int - (k_dung - 2) * x_int - k_dung
        str_c3 = '+ %s' % c3 if c3 > 0 else ('- %s' % abs(c3) if c3 < 0 else '')
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2,0) -- (4,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,4) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-0.5,-1.5) -- (3,3.5) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-1,3.5) -- (3.5,-1) node[right] {$(d_2)$};\n'
            '\\draw[line width=1pt] (-1.5,0.5) -- (3.5,2.5) node[right] {$(d_3)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (1.43,1.26) circle (1pt) node[above left] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Tìm giá trị của tham số $k$ để ba đường thẳng sau cùng đi qua một điểm (đồng quy):\\\n'
            '$(d_1): y = %s$; $\\quad (d_2): y = %s$; $\\quad (d_3): y = (k - 2)x + k %s$ (với $k \\neq 2$).'
            % (fmt_dt(a1, b1), fmt_dt(a2, b2), str_c3)
        )
        
        loigiai = (
            'Vì hệ số góc của $(d_1)$ là $a_1 = %s$ và của $(d_2)$ là $a_2 = %s$ ($a_1 \\neq a_2$) nên hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau.\\\n'
            'Hoành độ giao điểm $I$ của $(d_1)$ và $(d_2)$ là nghiệm của phương trình:\\\n'
            '$%s = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$.\\\n'
            'Thay $x = %s$ vào phương trình đường thẳng $(d_1)$ ta được: $y = %s \\cdot (%s) %s = %s$.\\\n'
            'Vậy tọa độ giao điểm của $(d_1)$ và $(d_2)$ là $I(%s; %s)$.\\\n'
            'Để ba đường thẳng $(d_1), (d_2), (d_3)$ đồng quy thì đường thẳng $(d_3)$ phải đi qua điểm $I(%s; %s)$ và không trùng với $(d_1), (d_2)$.\\\n'
            'Thay $x = %s, y = %s$ vào phương trình $(d_3)$ ta được:\\\n'
            '$%s = (k - 2) \\cdot (%s) + k %s \\Leftrightarrow %sk = %s \\Leftrightarrow k = %s$ (thỏa mãn $k \\neq 2$ và $k - 2 = %s$ khác $a_1, a_2$).\\\n'
            'Vậy giá trị cần tìm là $k = %s$.%s'
            % (a1, a2, fmt_dt(a1, b1), fmt_dt(a2, b2), a1 - a2, b2 - b1, x_int,
               x_int, a1, x_int, '+ %s' % b1 if b1 >= 0 else '- %s' % abs(b1), y_int,
               x_int, y_int, x_int, y_int, x_int, y_int,
               y_int, x_int, str_c3, x_int + 1, y_int + 2 * x_int - c3, k_dung, k_dung - 2, k_dung, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
