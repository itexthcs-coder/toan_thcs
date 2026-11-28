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

def bt_dang16_p4_b5_c7_ds8(self):
    # Dạng 16: Bài toán thực tế về giá cước vận chuyển (song song và giao điểm)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        aA = random.choice([12, 14, 15])
        bA = random.choice([10, 12])
        k = random.choice([2, 3, 4])
        m_ss = aA - k
        bB = bA + random.choice([15, 20, 25])
        m_cat = aA - k - random.choice([3, 5]) # he so goc B la m_cat + k < aA
        aB_cat = m_cat + k
        x_hw = Fraction(bB - bA, aA - aB_cat)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (0,0) -- (4.5,0) node[below] {$x$ (km)};\n'
            '\\draw[->, line width=1pt] (0,0) -- (0,3.8) node[left] {$y$ (nghìn đồng)};\n'
            '\\draw[line width=1pt] (0,0.8) -- (3.8,3.6) node[right] {Hãng A};\n'
            '\\draw[line width=1pt] (0,1.6) -- (4,3.2) node[right] {Hãng B};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (2.37,2.55) circle (1pt) node[above left] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Hai hãng xe công nghệ A và B áp dụng bảng giá cước cho một chuyến đi (với quãng đường $x$ km, $x > 0$) được biểu diễn bởi hai hàm số bậc nhất:\\\n'
            '- Hãng A: $y_A = %sx + %s$ (nghìn đồng)\\\n'
            '- Hãng B: $y_B = (m + %s)x + %s$ (nghìn đồng, với $m > -%s$)\\\n'
            'a) Giải thích ý nghĩa thực tế của hệ số góc trong công thức tính cước của hãng A.\\\n'
            'b) Tìm giá trị của $m$ để tốc độ tăng giá cước theo mỗi ki-lô-mét của hai hãng là bằng nhau (hai đường thẳng biểu diễn song song). Khi đó, đi hãng nào luôn tiết kiệm hơn?\\\n'
            'c) Nếu $m = %s$, hãy tìm quãng đường $x$ để chi phí đi hai hãng là như nhau.'
            % (aA, bA, k, bB, k, m_cat)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Hệ số góc của đường thẳng biểu diễn cước phí hãng A là $a = %s$, cho biết cứ mỗi ki-lô-mét di chuyển thêm thì số tiền cước khách hàng phải trả tăng thêm $%s$ nghìn đồng.\n'
            '\\item Hai đường thẳng biểu diễn cước phí của hai hãng song song với nhau khi và chỉ khi:\\\n'
            '$\\begin{cases} m + %s = %s \\\\ %s \\neq %s \\end{cases} \\Leftrightarrow m = %s$ (thỏa mãn điều kiện $m > -%s$).\\\n'
            'Khi đó, hai hãng có cùng đơn giá mỗi ki-lô-mét là $%s$ nghìn đồng, nhưng giá mở cửa của hãng A ($%s$ nghìn đồng) thấp hơn hãng B ($%s$ nghìn đồng) nên đi hãng A luôn tiết kiệm hơn với mọi quãng đường.\n'
            '\\item Với $m = %s$, công thức cước phí của hãng B là $y_B = %sx + %s$.\\\n'
            'Chi phí đi hai hãng bằng nhau khi $y_A = y_B \\Leftrightarrow %sx + %s = %sx + %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (km).%s\n'
            '\\end{enumEX}'
            % (aA, aA, k, aA, bB, bA, m_ss, k, aA, bA, bB,
               m_cat, aB_cat, bB, aA, bA, aB_cat, bB, aA - aB_cat, bB - bA, fmt_so(x_hw), tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
