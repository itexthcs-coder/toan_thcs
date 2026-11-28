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

def bt_dang13_p4_b5_c7_ds8(self):
    # Dạng 13: Tìm khoảng giá trị hệ số góc m để đường thẳng cắt đoạn thẳng AB
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b0 = random.choice([1, 2])
        xA = random.choice([1, 2])
        xB = xA + random.choice([2, 3])
        mA = random.choice([2, 3])
        mB = random.choice([1, 2])
        if mA == mB:
            mA += 1
        yA = mA * xA + b0
        yB = mB * xB + b0
        m_min = min(mA, mB)
        m_max = max(mA, mB)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-1,0) -- (4.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1) -- (0,4.2) node[left] {$y$};\n'
            '\\draw[line width=1pt] (1,2) -- (3.5,3.2);\n'
            '\\draw[line width=1pt, dashed] (-0.5,0.5) -- (2.2,3.2) node[above] {$(d_A)$};\n'
            '\\draw[line width=1pt, dashed] (-0.5,0.7) -- (4.2,3.6) node[right] {$(d_B)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,1) circle (1pt) node[left] {$K$};\n'
            '\\fill (1,2) circle (1pt) node[above left] {$A$};\n'
            '\\fill (3.5,3.2) circle (1pt) node[below right] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Trong mặt phẳng tọa độ $Oxy$, cho đoạn thẳng $AB$ với $A(%s; %s)$ và $B(%s; %s)$. Cho đường thẳng $(d): y = mx + %s$ ($m \\neq 0$). Tìm khoảng giá trị của tham số $m$ để đường thẳng $(d)$ luôn có điểm chung với đoạn thẳng $AB$.'
            % (xA, yA, xB, yB, b0)
        )
        
        loigiai = (
            'Đường thẳng $(d): y = mx + %s$ luôn đi qua điểm cố định $K(0; %s)$ nằm trên trục tung $Oy$ với mọi giá trị của $m \\neq 0$.\\\n'
            'Khi $m$ thay đổi, đường thẳng $(d)$ quay quanh điểm cố định $K(0; %s)$. Để $(d)$ có điểm chung với đoạn thẳng $AB$, hệ số góc $m$ của $(d)$ phải nằm giữa hai giá trị giới hạn là hệ số góc của đường thẳng $KA$ và đường thẳng $KB$.\\\n'
            '- Đường thẳng $(d)$ đi qua điểm $A(%s; %s)$ khi $%s = m \\cdot %s + %s \\Leftrightarrow m = %s$.\\\n'
            '- Đường thẳng $(d)$ đi qua điểm $B(%s; %s)$ khi $%s = m \\cdot %s + %s \\Leftrightarrow m = %s$.\\\n'
            'Quan sát vị trí các điểm trên mặt phẳng tọa độ, đường thẳng $(d)$ cắt đoạn thẳng $AB$ khi và chỉ khi $%s \\le m \\le %s$ (thỏa mãn điều kiện $m \\neq 0$).%s'
            % (b0, b0, b0, xA, yA, yA, xA, b0, mA,
               xB, yB, yB, xB, b0, mB, m_min, m_max, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
