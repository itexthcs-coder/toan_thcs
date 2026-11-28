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

def bt_dang12_p4_b5_c7_ds8(self):
    # Dạng 12: Đường thẳng tạo với trục Ox một góc 45 độ hoặc 135 độ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xE = random.choice([1, 2, 3])
        yE = random.choice([4, 5, 6])
        b1 = yE - xE
        
        xF = random.choice([-1, -2, -3])
        yF = random.choice([3, 4, 5])
        b2 = yF + xF
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1) -- (0,3.8) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-2.2,-0.5) -- (2.2,3.9) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-1.2,3.7) -- (3,-0.5) node[right] {$(d_2)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (-1.7,0) circle (1pt) node[below] {$A$};\n'
            '\\fill (0,1.7) circle (1pt) node[left] {$B$};\n'
            '\\fill (2.5,0) circle (1pt) node[below] {$C$};\n'
            '\\fill (0,2.5) circle (1pt) node[right] {$D$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'a) Viết phương trình đường thẳng $(d_1)$ đi qua điểm $E(%s; %s)$ và tạo với tia $Ox$ một góc $45^\\circ$.\\\n'
            'b) Viết phương trình đường thẳng $(d_2)$ đi qua điểm $F(%s; %s)$ và tạo với tia $Ox$ một góc $135^\\circ$.'
            % (xE, yE, xF, yF)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Gọi phương trình đường thẳng $(d_1)$ là $y = ax + b$ ($a \\neq 0$).\\\n'
            'Vì góc tạo bởi $(d_1)$ và tia $Ox$ là $45^\\circ$ (góc nhọn) nên $a > 0$, đường thẳng đi lên từ trái sang phải.\\\n'
            'Gọi $A, B$ lần lượt là giao điểm của $(d_1)$ với trục $Ox$ và trục $Oy$. Khi đó $A\\left(-\\frac{b}{a}; 0\\right)$ và $B(0; b)$.\\\n'
            'Tam giác $OAB$ vuông tại $O$ có $\\widehat{OAB} = 45^\\circ$ nên $\\triangle OAB$ vuông cân tại $O$, suy ra $OA = OB \\Leftrightarrow \\left|-\\frac{b}{a}\\right| = |b| \\Leftrightarrow a = 1$ (vì $a > 0$ và $b \\neq 0$).\\\n'
            'Thay tọa độ điểm $E(%s; %s)$ vào phương trình $y = x + b$, ta được: $%s = %s + b \\Leftrightarrow b = %s$.\\\n'
            'Vậy phương trình đường thẳng $(d_1)$ là $y = %s$.\n'
            '\\item Gọi phương trình đường thẳng $(d_2)$ là $y = a\\prime x + b\\prime$ ($a\\prime \\neq 0$).\\\n'
            'Vì góc tạo bởi $(d_2)$ và tia $Ox$ là $135^\\circ$ (góc tù) nên $a\\prime < 0$, đường thẳng đi xuống từ trái sang phải.\\\n'
            'Gọi $C, D$ lần lượt là giao điểm của $(d_2)$ với trục $Ox$ và trục $Oy$. Khi đó $\\widehat{OCD} = 180^\\circ - 135^\\circ = 45^\\circ$, suy ra $\\triangle OCD$ vuông cân tại $O$.\\\n'
            'Do đó $OC = OD \\Leftrightarrow \\left|-\\frac{b\\prime}{a\\prime}\\right| = |b\\prime| \\Leftrightarrow a\\prime = -1$ (vì $a\\prime < 0$).\\\n'
            'Thay tọa độ điểm $F(%s; %s)$ vào phương trình $y = -x + b\\prime$, ta được: $%s = -(%s) + b\\prime \\Leftrightarrow b\\prime = %s$.\\\n'
            'Vậy phương trình đường thẳng $(d_2)$ là $y = %s$.%s\n'
            '\\end{enumEX}'
            % (xE, yE, yE, xE, b1, fmt_dt(1, b1),
               xF, yF, yF, xF, b2, fmt_dt(-1, b2), tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
