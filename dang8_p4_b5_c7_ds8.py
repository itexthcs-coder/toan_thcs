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

def bt_dang8_p4_b5_c7_ds8(self):
    # Dạng 8: Đường thẳng đối xứng qua trục tung Oy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, 4, 5])
        b = random.choice([-2, -3, -4, 2, 3])
        xM = Fraction(-b, a)
        xM_prime = Fraction(b, a)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (2.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,2.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-0.3,-2.2) -- (1.8,2) node[right] {$(d)$};\n'
            '\\draw[line width=1pt] (0.3,-2.2) -- (-1.8,2) node[left] {$(d\\prime)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,-1.6) circle (1pt) node[below right] {$N$};\n'
            '\\fill (0.8,0) circle (1pt) node[below right] {$M$};\n'
            '\\fill (-0.8,0) circle (1pt) node[below left] {$M\\prime$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho đường thẳng $(d): y = %s$.\\\n'
            'a) Tìm tọa độ các giao điểm $M, N$ của $(d)$ lần lượt với trục $Ox$ và trục $Oy$.\\\n'
            'b) Viết phương trình đường thẳng $(d\\prime)$ đối xứng với đường thẳng $(d)$ qua trục tung $Oy$. Nêu nhận xét về mối quan hệ giữa hệ số góc của $(d)$ và $(d\\prime)$.'
            % (fmt_dt(a, b))
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Cho $y = 0$, ta được $%s = 0 \\Leftrightarrow x = %s$, suy ra giao điểm với trục $Ox$ là $M\\left(%s; 0\\right)$.\\\n'
            'Cho $x = 0$, ta được $y = %s$, suy ra giao điểm với trục $Oy$ là $N(0; %s)$.\n'
            '\\item Vì $(d\\prime)$ đối xứng với $(d)$ qua trục tung $Oy$ nên $(d\\prime)$ đi qua điểm $N(0; %s)$ nằm trên trục $Oy$ và đi qua điểm $M\\prime\\left(%s; 0\\right)$ là điểm đối xứng của $M$ qua trục $Oy$.\\\n'
            'Gọi phương trình đường thẳng $(d\\prime)$ là $y = a\\prime x + b\\prime$ ($a\\prime \\neq 0$).\\\n'
            'Vì $(d\\prime)$ đi qua $N(0; %s)$ nên $b\\prime = %s$.\\\n'
            'Thay tọa độ $M\\prime\\left(%s; 0\\right)$ vào $y = a\\prime x %s$, ta được: $a\\prime \\cdot \\left(%s\\right) %s = 0 \\Leftrightarrow a\\prime = -%s$.\\\n'
            'Vậy phương trình đường thẳng $(d\\prime)$ là $y = %s$.\\\n'
            'Nhận xét: Hai đường thẳng đối xứng nhau qua trục tung $Oy$ có hệ số góc là hai số đối nhau ($%s$ và $-%s$).%s\n'
            '\\end{enumEX}'
            % (fmt_dt(a, b), fmt_so(xM), fmt_so(xM), b, b,
               b, fmt_so(xM_prime), b, b, fmt_so(xM_prime),
               '+ %s' % b if b >= 0 else '- %s' % abs(b), fmt_so(xM_prime),
               '+ %s' % b if b >= 0 else '- %s' % abs(b), a, fmt_dt(-a, b), a, a, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
