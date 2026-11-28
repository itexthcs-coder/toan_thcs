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

def bt_dang11_p4_b5_c7_ds8(self):
    # Dạng 11: Viết phương trình đường thẳng song song và tính khoảng cách từ gốc tọa độ O
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ba = random.choice([(3, 4), (4, 3), (5, 12), (12, 5)])
        p, q = bo_ba # he so goc -p/q, cat Ox tai (q, 0), Oy tai (0, p)
        b_cho = random.choice([2, 5, 7])
        if b_cho == p:
            b_cho += 2
        c_huyen = int(math.hypot(p, q))
        OH = Fraction(p * q, c_huyen)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-1,0) -- (4.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1) -- (0,3.8) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-0.6,3.45) -- (4.4,-0.3) node[right] {$(d)$};\n'
            '\\draw[line width=1pt, dashed] (0,0) -- (1.44,1.92);\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (4,0) circle (1pt) node[below] {$P$};\n'
            '\\fill (0,3) circle (1pt) node[left] {$Q$};\n'
            '\\fill (1.44,1.92) circle (1pt) node[above right] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho đường thẳng $(d)$ song song với đường thẳng $y = -\\frac{%s}{%s}x + %s$ và đi qua điểm $P(%s; 0)$.\\\n'
            'a) Viết phương trình đường thẳng $(d)$.\\\n'
            'b) Tính độ dài đường cao $OH$ hạ từ gốc tọa độ $O$ xuống đường thẳng $(d)$.'
            % (p, q, b_cho, q)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì đường thẳng $(d)$ song song với đường thẳng $y = -\\frac{%s}{%s}x + %s$ nên phương trình của $(d)$ có dạng:\\\n'
            '$y = -\\frac{%s}{%s}x + b$ (với $b \\neq %s$).\\\n'
            'Vì $(d)$ đi qua điểm $P(%s; 0)$ nên thay $x = %s, y = 0$ vào phương trình trên ta được:\\\n'
            '$0 = -\\frac{%s}{%s} \\cdot %s + b \\Leftrightarrow b = %s$ (thỏa mãn $b \\neq %s$).\\\n'
            'Vậy phương trình đường thẳng $(d)$ là $y = -\\frac{%s}{%s}x + %s$.\n'
            '\\item Gọi $Q$ là giao điểm của $(d)$ với trục tung $Oy$, ta có $Q(0; %s)$.\\\n'
            'Tam giác $OPQ$ vuông tại $O$ có $OP = %s$, $OQ = %s$.\\\n'
            'Áp dụng định lí Pythagore trong tam giác vuông $OPQ$, ta tính được độ dài cạnh huyền $PQ$:\\\n'
            '$PQ = \\sqrt{OP^2 + OQ^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s$.\\\n'
            'Diện tích tam giác vuông $OPQ$ được tính theo hai cách: $S_{\\triangle OPQ} = \\frac{1}{2} OP \\cdot OQ = \\frac{1}{2} OH \\cdot PQ$.\\\n'
            'Suy ra $OH = \\frac{OP \\cdot OQ}{PQ} = \\frac{%s \\cdot %s}{%s} = %s$ (đơn vị độ dài).%s\n'
            '\\end{enumEX}'
            % (p, q, b_cho, p, q, b_cho, q, q, p, q, q, p, b_cho, p, q, p,
               p, q, p, q, p, q*q + p*p, c_huyen, q, p, c_huyen, fmt_so(OH), tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
