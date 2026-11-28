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

def bt_dang9_p4_b5_c7_ds8(self):
    # Dạng 9: Tìm tham số nguyên âm để hai đường thẳng cắt nhau tại điểm có hoành độ nguyên
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        b1 = random.choice([3, 4, 5])
        b2 = random.choice([-1, -2, -3])
        tu = b1 - b2 # x = (b1 - b2)/(m - 1)
        # m nguyen am => m - 1 < -1, m - 1 la uoc am cua tu
        uoc_am = [-d for d in range(2, tu + 1) if tu % d == 0]
        m_list = [u + 1 for u in uoc_am]
        str_m = ', '.join([str(x) for x in m_list])
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3.5,0) -- (2.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-3,-0.5) -- (1.2,3.7) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-2.2,3.4) -- (0.5,-2) node[right] {$(d_2)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (-1.33,1.67) circle (1pt) node[above left] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hai đường thẳng $(d_1): y = x + %s$ và $(d_2): y = mx - %s$ ($m \\neq 0$). Tìm tất cả các giá trị nguyên âm của $m$ để hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau tại một điểm có hoành độ là số nguyên.'
            % (b1, abs(b2))
        )
        
        loigiai = (
            'Để hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau thì hệ số góc của chúng phải khác nhau: $m \\neq 1$ (kết hợp $m \\neq 0$).\\\n'
            'Hoành độ giao điểm của $(d_1)$ và $(d_2)$ là nghiệm của phương trình:\\\n'
            '$x + %s = mx - %s \\Leftrightarrow (m - 1)x = %s \\Leftrightarrow x = \\frac{%s}{m - 1}$.\\\n'
            'Để hoành độ giao điểm $x$ là số nguyên với $m$ nguyên âm thì $m - 1$ phải là ước nguyên của $%s$.\\\n'
            'Mặt khác, vì $m$ là số nguyên âm ($m \\le -1$) nên $m - 1 \\le -2$.\\\n'
            'Các ước nguyên của $%s$ nhỏ hơn hoặc bằng $-2$ là: $%s$.\\\n'
            'Từ đó suy ra các giá trị của $m$ tương ứng là: $m \\in \\{%s\\}$ (đều thỏa mãn điều kiện $m$ nguyên âm và $m \\neq 0, m \\neq 1$).%s'
            % (b1, abs(b2), tu, tu, tu, tu,
               ', '.join([str(u) for u in uoc_am]), str_m, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
