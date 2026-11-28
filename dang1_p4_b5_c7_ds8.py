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

def bt_dang1_p4_b5_c7_ds8(self):
    # Dạng 1: Tìm tham số để hai đường thẳng song song và tính khoảng cách giao điểm trên trục Oy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4])
        a2 = k * k - 1
        m_dung = -k
        c1 = random.choice([i for i in range(-5, 6) if i != 0])
        b2 = k + c1 + random.choice([2, 3, 4, 5])
        y_A = m_dung + c1
        kc = abs(y_A - b2)
        
        str_c1 = '+ %s' % c1 if c1 > 0 else '- %s' % abs(c1)
        str_b2 = '+ %s' % b2 if b2 > 0 else '- %s' % abs(b2)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1.2,-2) -- (1.8,2.5) node[right] {$(d_2)$};\n'
            '\\draw[line width=1pt] (-0.2,-2) -- (2.5,2.05) node[right] {$(d_1)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,1.2) circle (1pt) node[left] {$B$};\n'
            '\\fill (0,-1.7) circle (1pt) node[left] {$A$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hai đường thẳng $(d_1): y = (m^2 - 1)x + m %s$ và $(d_2): y = %sx %s$ (với $m \\neq \\pm 1$). Tìm giá trị của tham số $m$ để $(d_1)$ và $(d_2)$ song song với nhau. Với giá trị $m$ vừa tìm được, hãy tính khoảng cách giữa giao điểm $A$ của $(d_1)$ với trục $Oy$ và giao điểm $B$ của $(d_2)$ với trục $Oy$.'
            % (str_c1, a2, str_b2)
        )
        
        loigiai = (
            'Hai đường thẳng $(d_1): y = (m^2 - 1)x + m %s$ và $(d_2): y = %sx %s$ song song với nhau khi và chỉ khi:\\\n'
            '$\\begin{cases} m^2 - 1 = %s \\\\ m %s \\neq %s \\end{cases} \\Leftrightarrow \\begin{cases} m^2 = %s \\\\ m \\neq %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\text{ hoặc } m = %s \\\\ m \\neq %s \\end{cases} \\Leftrightarrow m = %s$ (thỏa mãn điều kiện $m \\neq \\pm 1$).\\\n'
            'Với $m = %s$, phương trình đường thẳng $(d_1)$ là $y = %sx %s$.\\\n'
            'Giao điểm $A$ của $(d_1)$ với trục $Oy$ có tọa độ $A(0; %s)$.\\\n'
            'Giao điểm $B$ của $(d_2)$ với trục $Oy$ có tọa độ $B(0; %s)$.\\\n'
            'Vì hai điểm $A$ và $B$ cùng nằm trên trục tung $Oy$ nên khoảng cách giữa chúng là:\\\n'
            '$AB = |%s - (%s)| = %s$ (đơn vị độ dài).%s'
            % (str_c1, a2, str_b2, a2, str_c1, b2, k*k, b2 - c1, k, -k, b2 - c1, m_dung,
               m_dung, a2, '+ %s' % y_A if y_A > 0 else '- %s' % abs(y_A),
               y_A, b2, y_A, b2, kc, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
