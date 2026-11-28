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

def bt_dang5_p4_b5_c7_ds8(self):
    # Dạng 5: Lập phương trình đường thẳng khi biết hệ số góc và diện tích tam giác tạo với hai trục tọa độ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([-2, -3, -4])
        k = random.choice([2, 3, 4])
        b = abs(a) * k # b > 0, xA = b / |a| = k
        S = Fraction(k * b, 2)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-1.5,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1.5) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-0.8,3.2) -- (2.5,-1.2) node[right] {$(d)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,2.13) circle (1pt) node[left] {$B$};\n'
            '\\fill (1.6,0) circle (1pt) node[below left] {$A$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Viết phương trình đường thẳng $(d)$ có hệ số góc $a = %s$, biết rằng $(d)$ cắt trục $Ox$ tại $A$, cắt trục $Oy$ tại $B$ sao cho tam giác $OAB$ có diện tích bằng $%s$ (đơn vị diện tích) và tung độ điểm $B$ dương.'
            % (a, fmt_so(S))
        )
        
        loigiai = (
            'Đường thẳng $(d)$ có hệ số góc $a = %s$ nên phương trình của $(d)$ có dạng: $y = %sx + b$ ($b > 0$ do tung độ điểm $B$ dương).\\\n'
            'Giao điểm $B$ của $(d)$ với trục tung $Oy$ có tọa độ $B(0; b)$, suy ra $OB = |b| = b$ (vì $b > 0$).\\\n'
            'Cho $y = 0$, ta được $%sx + b = 0 \\Leftrightarrow x = \\frac{b}{%s}$. Vậy giao điểm $A$ của $(d)$ với trục hoành $Ox$ có tọa độ $A\\left(\\frac{b}{%s}; 0\\right)$, suy ra $OA = \\left|\\frac{b}{%s}\\right| = \\frac{b}{%s}$.\\\n'
            'Vì tam giác $OAB$ vuông tại $O$ nên diện tích của nó là:\\\n'
            '$S_{\\triangle OAB} = \\frac{1}{2} \\cdot OA \\cdot OB = \\frac{1}{2} \\cdot \\frac{b}{%s} \\cdot b = \\frac{b^2}{%s}$.\\\n'
            'Theo đề bài, $S_{\\triangle OAB} = %s$ nên $\\frac{b^2}{%s} = %s \\Leftrightarrow b^2 = %s$.\\\n'
            'Vì $b > 0$ nên ta tìm được $b = %s$.\\\n'
            'Vậy phương trình đường thẳng $(d)$ cần tìm là $y = %sx + %s$.%s'
            % (a, a, a, abs(a), abs(a), abs(a), abs(a), abs(a), 2 * abs(a),
               fmt_so(S), 2 * abs(a), fmt_so(S), b * b, b, a, b, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
