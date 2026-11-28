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

def bt_dang17_p4_b5_c7_ds8(self):
    # Dạng 17: Bài toán thực tế về lượng nước trong hai bể (hệ số góc âm và dương)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v1 = random.choice([40, 50, 60])
        v2 = random.choice([20, 30, 40])
        t_giao = random.choice([8, 10, 12, 15])
        b1 = random.choice([300, 400, 500])
        b2 = b1 + (v1 + v2) * t_giao
        y_giao = b1 + v1 * t_giao
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (0,0) -- (4.5,0) node[below] {$x$ (phút)};\n'
            '\\draw[->, line width=1pt] (0,0) -- (0,3.8) node[left] {$y$ (lít)};\n'
            '\\draw[line width=1pt] (0,0.8) -- (3.8,3.2) node[right] {Bể 1};\n'
            '\\draw[line width=1pt] (0,3.3) -- (4,0.9) node[right] {Bể 2};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (2.03,2.08) circle (1pt) node[above] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Hai bể nước hình hộp chữ nhật có chiều cao bằng nhau. Bể thứ nhất ban đầu chứa $%s$ lít nước và đang được bơm thêm nước với tốc độ $%s$ lít/phút. Bể thứ hai ban đầu chứa $%s$ lít nước nhưng đang bị rò rỉ nước chảy ra ngoài với tốc độ $%s$ lít/phút. Gọi $y$ (lít) là lượng nước trong mỗi bể sau $x$ (phút).\\\n'
            'a) Viết công thức hàm số biểu thị lượng nước $y_1, y_2$ của hai bể theo thời gian $x$. Nhận xét về dấu của hệ số góc của hai đường thẳng này và liên hệ với trạng thái tăng hoặc giảm của lượng nước.\\\n'
            'b) Hỏi sau bao nhiêu phút thì lượng nước ở hai bể bằng nhau? Khi đó mỗi bể có bao nhiêu lít nước?'
            % (b1, v1, b2, v2)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Sau $x$ phút, lượng nước bơm thêm vào bể thứ nhất là $%sx$ (lít) nên lượng nước trong bể thứ nhất là: $y_1 = %sx + %s$.\\\n'
            'Sau $x$ phút, lượng nước chảy ra khỏi bể thứ hai là $%sx$ (lít) nên lượng nước còn lại trong bể thứ hai là: $y_2 = -%sx + %s$.\\\n'
            'Nhận xét: Đường thẳng biểu diễn $y_1$ có hệ số góc dương ($a_1 = %s > 0$), đồ thị đi lên từ trái sang phải, ứng với trạng thái lượng nước trong bể đang tăng lên. Đường thẳng biểu diễn $y_2$ có hệ số góc âm ($a_2 = -%s < 0$), đồ thị đi xuống từ trái sang phải, ứng với trạng thái lượng nước trong bể đang giảm đi.\n'
            '\\item Lượng nước ở hai bể bằng nhau khi $y_1 = y_2 \\Leftrightarrow %sx + %s = -%sx + %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (phút).\\\n'
            'Khi đó, lượng nước trong mỗi bể là: $y = %s \\cdot %s + %s = %s$ (lít).%s\n'
            '\\end{enumEX}'
            % (v1, v1, b1, v2, v2, b2, v1, v2,
               v1, b1, v2, b2, v1 + v2, b2 - b1, t_giao, v1, t_giao, b1, y_giao, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
