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

def bt_dang2_p4_b5_c7_ds8(self):
    # Dạng 2: Chứng minh họ đường thẳng đi qua điểm cố định và tìm điều kiện song song
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([1, 2, 3, -1, -2])
        y0 = random.choice([1, 2, 3, 4, 5])
        # y = (2m - 1)x - 2*x0*m + (x0 + y0)
        c_m = -2 * x0
        c_const = x0 + y0
        str_cm = '+ %sm' % c_m if c_m > 0 else '- %sm' % abs(c_m)
        str_cc = '+ %s' % c_const if c_const > 0 else '- %s' % abs(c_const)
        
        a_song = random.choice([3, 5, 7, -3, -5])
        xA = random.choice([1, 2])
        yA = random.choice([-2, -1, 1])
        xB = xA + 2
        yB = yA + 2 * a_song
        # 2m - 1 = a_song => m = (a_song + 1)/2
        m_val = (a_song + 1) // 2
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2,0) -- (4,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1,-1.5) -- (3.5,3) node[right] {$(d_m)$};\n'
            '\\draw[line width=1pt] (-0.5,-1.5) -- (3.5,2.5) node[right] {$AB$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (1.5,1) circle (1pt) node[above left] {$M$};\n'
            '\\fill (1,0) circle (1pt) node[below right] {$A$};\n'
            '\\fill (2.5,1.5) circle (1pt) node[below right] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho họ đường thẳng $(d_m): y = (2m - 1)x %s %s$ (với $m \\neq \\frac{1}{2}$).\\\n'
            'a) Chứng minh rằng với mọi giá trị của $m \\neq \\frac{1}{2}$, đường thẳng $(d_m)$ luôn đi qua một điểm cố định $M(x_0; y_0)$.\\\n'
            'b) Tìm $m$ để đường thẳng $(d_m)$ song song với đường thẳng đi qua hai điểm $A(%s; %s)$ và $B(%s; %s)$.'
            % (str_cm, str_cc, xA, yA, xB, yB)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Giả sử điểm cố định mà $(d_m)$ luôn đi qua là $M(x_0; y_0)$. Khi đó tọa độ của $M$ thỏa mãn phương trình của $(d_m)$ với mọi $m \\neq \\frac{1}{2}$:\\\n'
            '$y_0 = (2m - 1)x_0 %s %s \\Leftrightarrow (2x_0 %s)m + (-x_0 %s - y_0) = 0$ đúng với mọi $m \\neq \\frac{1}{2}$.\\\n'
            'Điều này xảy ra khi và chỉ khi $\\begin{cases} 2x_0 %s = 0 \\\\ -x_0 %s - y_0 = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x_0 = %s \\\\ y_0 = %s \\end{cases}$.\\\n'
            'Vậy họ đường thẳng $(d_m)$ luôn đi qua điểm cố định $M(%s; %s)$.\n'
            '\\item Gọi phương trình đường thẳng đi qua hai điểm $A(%s; %s)$ và $B(%s; %s)$ là $y = ax + b$ ($a \\neq 0$).\\\n'
            'Thay tọa độ điểm $A$ và $B$ vào phương trình ta được hệ: $\\begin{cases} %sa + b = %s \\\\ %sa + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$.\\\n'
            'Suy ra đường thẳng $AB$ có phương trình là $y = %s$.\\\n'
            'Để $(d_m)$ song song với đường thẳng $AB$ thì $\\begin{cases} 2m - 1 = %s \\\\ %sm %s \\neq %s \\end{cases} \\Leftrightarrow m = %s$ (thỏa mãn điều kiện $m \\neq \\frac{1}{2}$ và tung độ gốc khác nhau).%s\n'
            '\\end{enumEX}'
            % (str_cm, str_cc, str_cm.replace('m', ''), str_cc, str_cm.replace('m', ''), str_cc, x0, y0, x0, y0,
               xA, yA, xB, yB, xA, yA, xB, yB, a_song, yA - a_song * xA, fmt_dt(a_song, yA - a_song * xA),
               a_song, c_m, str_cc, yA - a_song * xA, m_val, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
