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

def bt_dang15_p4_b5_c7_ds8(self):
    # Dạng 15: Biện luận số giao điểm bằng cách xét song song với hai nhánh đồ thị hàm số chứa dấu giá trị tuyệt đối
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([1, 2, 3])
        y0 = random.choice([1, 2])
        b_d = y0 + random.choice([1, 2]) # K(0; b_d) nam phia tren dinh (x0; y0) hoac khac
        # Nhanh 1 (x >= x0): y = x - x0 + y0
        # Nhanh 2 (x < x0): y = -x + x0 + y0
        b_n1 = -x0 + y0
        b_n2 = x0 + y0
        # Tai x0, y_d = m*x0 + b_d
        # Khi m = 1: y_d(x0) = x0 + b_d > y0 => cat nhanh 2 tai 1 diem
        # Khi m = -1: y_d(x0) = -x0 + b_d. Neu b_d > x0 + y0 thi cat nhanh 1, neu b_d < x0 + y0 thi vo nghiem
        b_d = x0 + y0 + random.choice([1, 2])
        x_int1 = Fraction(b_n2 - b_d, 2)
        y_int1 = x_int1 + b_d
        x_int2 = Fraction(b_n1 - b_d, -2)
        y_int2 = -x_int2 + b_d
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2,0) -- (4.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-0.5) -- (0,4.2) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1,3.5) -- (1.5,1) -- (4,3.5) node[right] {$(C)$};\n'
            '\\draw[line width=1pt, dashed] (-1.2,1.8) -- (1.2,4.2) node[above] {$m=1$};\n'
            '\\draw[line width=1pt, dashed] (-0.5,3.5) -- (3.2,-0.2) node[right] {$m=-1$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (1.5,1) circle (1pt) node[below] {$I$};\n'
            '\\fill (0,3) circle (1pt) node[left] {$K$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hàm số $y = |x - %s| + %s$ có đồ thị là $(C)$ và đường thẳng $(d): y = mx + %s$ ($m \\neq 0$). Dựa vào sự thay đổi của hệ số góc $m$, hãy xác định giá trị của $m$ để đường thẳng $(d)$ song song với một trong hai nhánh của đồ thị $(C)$. Từ đó tìm tọa độ giao điểm của $(d)$ và $(C)$ trong từng trường hợp đó.'
            % (x0, y0, b_d)
        )
        
        loigiai = (
            'Đồ thị $(C)$ của hàm số $y = |x - %s| + %s$ gồm hai nhánh là hai nửa đường thẳng xuất phát từ đỉnh $I(%s; %s)$:\\\n'
            '- Nhánh phải $(C_1)$ với $x \\ge %s$: $y = %s$ (có hệ số góc $a_1 = 1$).\\\n'
            '- Nhánh trái $(C_2)$ với $x < %s$: $y = %s$ (có hệ số góc $a_2 = -1$).\\\n'
            'Đường thẳng $(d): y = mx + %s$ có hệ số góc là $m$. Do đó $(d)$ song song với một trong hai nhánh của $(C)$ khi $m = 1$ hoặc $m = -1$ (vì tung độ gốc $%s$ khác $%s$ và $%s$).\\\n'
            '- Trường hợp 1: $m = 1$, phương trình $(d)$ là $y = x + %s$. Khi đó $(d)$ song song với nhánh $(C_1)$ nên không cắt $(C_1)$, và cắt nhánh $(C_2)$ tại điểm có hoành độ thỏa mãn:\\\n'
            '$x + %s = %s \\Leftrightarrow 2x = %s \\Leftrightarrow x = %s$ (thỏa mãn $x < %s$). Suy ra giao điểm duy nhất là $M\\left(%s; %s\\right)$.\\\n'
            '- Trường hợp 2: $m = -1$, phương trình $(d)$ là $y = -x + %s$. Khi đó $(d)$ song song với nhánh $(C_2)$ nên không cắt $(C_2)$, và cắt nhánh $(C_1)$ tại điểm có hoành độ thỏa mãn:\\\n'
            '$-x + %s = %s \\Leftrightarrow -2x = %s \\Leftrightarrow x = %s$ (thỏa mãn $x \\ge %s$). Suy ra giao điểm duy nhất là $N\\left(%s; %s\\right)$.%s'
            % (x0, y0, x0, y0, x0, fmt_dt(1, b_n1), x0, fmt_dt(-1, b_n2),
               b_d, b_d, b_n1, b_n2,
               b_d, b_d, fmt_dt(-1, b_n2), b_n2 - b_d, fmt_so(x_int1), x0, fmt_so(x_int1), fmt_so(y_int1),
               b_d, b_d, fmt_dt(1, b_n1), b_n1 - b_d, fmt_so(x_int2), x0, fmt_so(x_int2), fmt_so(y_int2), tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
