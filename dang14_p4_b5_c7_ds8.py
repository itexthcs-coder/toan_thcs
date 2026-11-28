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

def bt_dang14_p4_b5_c7_ds8(self):
    # Dạng 14: Lập phương trình hai đường thẳng song song để tạo thành hình bình hành
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = random.choice([2, 3])
        a2 = random.choice([-1, -2])
        b0 = random.choice([2, 4]) # A(0; b0)
        # B(-b0/a1; 0), C(-b0/a2; 0)
        # Chon b0 la boi chung cua a1 va |a2|
        b0 = abs(a1 * a2) * random.choice([1, 2])
        xB = -b0 // a1
        xC = -b0 // a2
        # D doi xung A qua trung diem BC: xD = xB + xC - 0, yD = 0 + 0 - b0 = -b0
        xD = xB + xC
        yD = -b0
        b3 = -a2 * xB
        b4 = -a1 * xC
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.75, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,2.8) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1.5,-1) -- (0.5,3) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-0.8,2.8) -- (2.8,-0.8) node[right] {$(d_2)$};\n'
            '\\draw[line width=1pt] (-2.2,1.2) -- (1.8,-2.8) node[right] {$(d_3)$};\n'
            '\\draw[line width=1pt] (0.5,-3) -- (2.6,1.2) node[right] {$(d_4)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,2) circle (1pt) node[above right] {$A$};\n'
            '\\fill (-1,0) circle (1pt) node[above left] {$B$};\n'
            '\\fill (2,0) circle (1pt) node[above right] {$C$};\n'
            '\\fill (1,-2) circle (1pt) node[below right] {$D$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hai đường thẳng $(d_1): y = %s$ và $(d_2): y = %s$.\\\n'
            'a) Xác định tọa độ giao điểm $A$ của $(d_1)$ và $(d_2)$, giao điểm $B$ của $(d_1)$ với trục $Ox$, và giao điểm $C$ của $(d_2)$ với trục $Ox$.\\\n'
            'b) Viết phương trình đường thẳng $(d_3)$ đi qua $B$ và song song với $(d_2)$, và phương trình đường thẳng $(d_4)$ đi qua $C$ và song song với $(d_1)$. Tìm tọa độ giao điểm $D$ của $(d_3)$ và $(d_4)$ để tứ giác $ABDC$ là hình bình hành.'
            % (fmt_dt(a1, b0), fmt_dt(a2, b0))
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau trên trục tung tại $A(0; %s)$.\\\n'
            'Cho $y = 0$ trong $(d_1)$, ta được $%s = 0 \\Leftrightarrow x = %s$, suy ra $B(%s; 0)$.\\\n'
            'Cho $y = 0$ trong $(d_2)$, ta được $%s = 0 \\Leftrightarrow x = %s$, suy ra $C(%s; 0)$.\n'
            '\\item Đường thẳng $(d_3)$ song song với $(d_2)$ nên có dạng $y = %s + b_3$ ($b_3 \\neq %s$). Vì $(d_3)$ đi qua $B(%s; 0)$ nên $0 = %s \\cdot (%s) + b_3 \\Leftrightarrow b_3 = %s$. Vậy $(d_3): y = %s$.\\\n'
            'Đường thẳng $(d_4)$ song song với $(d_1)$ nên có dạng $y = %s + b_4$ ($b_4 \\neq %s$). Vì $(d_4)$ đi qua $C(%s; 0)$ nên $0 = %s \\cdot %s + b_4 \\Leftrightarrow b_4 = %s$. Vậy $(d_4): y = %s$.\\\n'
            'Hoành độ giao điểm $D$ của $(d_3)$ và $(d_4)$ là nghiệm của phương trình: $%s = %s \\Leftrightarrow x = %s$.\\\n'
            'Thay $x = %s$ vào $(d_3)$, ta được $y = %s$. Vậy $D(%s; %s)$ là đỉnh thứ tư của hình bình hành $ABDC$.%s\n'
            '\\end{enumEX}'
            % (b0, fmt_dt(a1, b0), xB, xB, fmt_dt(a2, b0), xC, xC,
               fmt_dt(a2, 0), b0, xB, a2, xB, b3, fmt_dt(a2, b3),
               fmt_dt(a1, 0), b0, xC, a1, xC, b4, fmt_dt(a1, b4),
               fmt_dt(a2, b3), fmt_dt(a1, b4), xD, xD, yD, xD, yD, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
