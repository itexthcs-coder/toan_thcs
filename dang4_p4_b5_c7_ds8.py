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

def bt_dang4_p4_b5_c7_ds8(self):
    # Dạng 4: Chứng minh hai đường thẳng vuông góc và nhận xét tích hai hệ số góc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([2, 3, 4])
        # d1: y = (1/p)x + 1 => cat Ox tai A(-p; 0)
        # d2: y = -p*x + 1 => cat Ox tai B(1/p; 0)
        # Giao diem I(0; 1)
        xA = -p
        xB = Fraction(1, p)
        OA2 = p * p
        OB2 = Fraction(1, p * p)
        AB2 = Fraction(p * p + 1, p) ** 2
        IA2 = OA2 + 1
        IB2 = OB2 + 1
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3.5,0) -- (2.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1.5) -- (0,3) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-3.2,-0.6) -- (2.2,2.1) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-0.8,2.6) -- (1.2,-1.4) node[right] {$(d_2)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,1) circle (1pt) node[above right] {$I$};\n'
            '\\fill (-2,0) circle (1pt) node[above left] {$A$};\n'
            '\\fill (0.5,0) circle (1pt) node[below left] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $(d_1): y = \\frac{1}{%s}x + 1$ và đường thẳng $(d_2): y = -%sx + 1$.\\\n'
            'a) Xác định tọa độ giao điểm $I$ của $(d_1)$ và $(d_2)$, cùng các giao điểm $A, B$ lần lượt của $(d_1), (d_2)$ với trục $Ox$.\\\n'
            'b) Chứng minh rằng $\\triangle IAB$ vuông tại $I$, từ đó rút ra nhận xét về tích hai hệ số góc của hai đường thẳng vuông góc.'
            % (p, p)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Hai đường thẳng $(d_1)$ và $(d_2)$ có cùng tung độ gốc là $b = 1$ và hệ số góc khác nhau ($\\frac{1}{%s} \\neq -%s$) nên chúng cắt nhau tại điểm $I(0; 1)$ trên trục tung.\\\n'
            'Cho $y = 0$ trong phương trình $(d_1)$, ta được $\\frac{1}{%s}x + 1 = 0 \\Leftrightarrow x = -%s$, suy ra $A(-%s; 0)$.\\\n'
            'Cho $y = 0$ trong phương trình $(d_2)$, ta được $-%sx + 1 = 0 \\Leftrightarrow x = \\frac{1}{%s}$, suy ra $B\\left(\\frac{1}{%s}; 0\\right)$.\n'
            '\\item Trên mặt phẳng tọa độ $Oxy$, ta có $OI = 1$, $OA = |-%s| = %s$, $OB = \\frac{1}{%s}$.\\\n'
            'Vì $A$ và $B$ nằm về hai phía của gốc tọa độ $O$ trên trục $Ox$ nên $AB = OA + OB = %s + \\frac{1}{%s} = \\frac{%s}{%s}$, suy ra $AB^2 = \\frac{%s}{%s}$.\\\n'
            'Áp dụng định lí Pythagore cho hai tam giác vuông $OIA$ và $OIB$ vuông tại $O$, ta có:\\\n'
            '$IA^2 = OI^2 + OA^2 = 1^2 + %s^2 = %s$;\\\n'
            '$IB^2 = OI^2 + OB^2 = 1^2 + \\left(\\frac{1}{%s}\\right)^2 = \\frac{%s}{%s}$.\\\n'
            'Ta thấy: $IA^2 + IB^2 = %s + \\frac{%s}{%s} = \\frac{%s}{%s} = AB^2$.\\\n'
            'Theo định lí Pythagore đảo, tam giác $IAB$ vuông tại $I$, tức là $(d_1) \\perp (d_2)$.\\\n'
            'Nhận xét: Tích hai hệ số góc của hai đường thẳng vuông góc bằng $-1$ (thật vậy, $\\frac{1}{%s} \\cdot (-%s) = -1$).%s\n'
            '\\end{enumEX}'
            % (p, p, p, p, p, p, p, p, p, p, p, p, p, p*p+1, p, (p*p+1)**2, p*p,
               p, p*p+1, p, p*p+1, p*p, p*p+1, p*p+1, p*p, (p*p+1)**2, p*p, p, p, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
