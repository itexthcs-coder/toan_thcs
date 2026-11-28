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

def bt_dang10_p4_b5_c7_ds8(self):
    # Dạng 10: Chứng minh ba điểm thẳng hàng bằng hệ số góc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, -2, -3])
        b = random.choice([-1, 1, 2])
        xA = -1
        xB = 2
        xC = 4
        yA = a * xA + b
        yB = a * xB + b
        yC = a * xC + b
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1.2,-1.8) -- (2.8,3.2) node[right] {$(d)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (-0.6,-1.05) circle (1pt) node[left] {$A$};\n'
            '\\fill (1.2,1.2) circle (1pt) node[above left] {$B$};\n'
            '\\fill (2.2,2.45) circle (1pt) node[above left] {$C$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(%s; %s)$, $B(%s; %s)$ và $C(%s; %s)$. Bằng cách lập phương trình đường thẳng đi qua hai điểm và sử dụng khái niệm hệ số góc, hãy chứng minh ba điểm $A, B, C$ thẳng hàng.'
            % (xA, yA, xB, yB, xC, yC)
        )
        
        loigiai = (
            'Gọi phương trình đường thẳng $AB$ là $y = ax + b$ ($a \\neq 0$ do $x_A \\neq x_B$ và $y_A \\neq y_B$).\\\n'
            'Vì đường thẳng $AB$ đi qua $A(%s; %s)$ và $B(%s; %s)$ nên ta có hệ phương trình:\\\n'
            '$\\begin{cases} %sa + b = %s \\\\ %sa + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} 3a = %s \\\\ b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$.\\\n'
            'Suy ra đường thẳng $AB$ có phương trình $y = %s$ với hệ số góc $a_1 = %s$.\\\n'
            'Tương tự, gọi phương trình đường thẳng $BC$ là $y = a\\prime x + b\\prime$. Thay tọa độ $B(%s; %s)$ và $C(%s; %s)$ vào, ta tìm được hệ số góc $a_2 = \\frac{%s - %s}{%s - %s} = %s$.\\\n'
            'Hai đường thẳng $AB$ và $BC$ có cùng hệ số góc ($a_1 = a_2 = %s$) và có chung điểm $B$ nên hai đường thẳng $AB$ và $BC$ trùng nhau.\\\n'
            'Vậy ba điểm $A, B, C$ thẳng hàng.%s'
            % (xA, yA, xB, yB, xA, yA, xB, yB, yB - yA, b, a, b,
               fmt_dt(a, b), a, xB, yB, xC, yC, yC, yB, xC, xB, a, a, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
