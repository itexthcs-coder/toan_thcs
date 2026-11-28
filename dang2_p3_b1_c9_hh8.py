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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D

def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        dec = (Decimal(val.numerator) / Decimal(val.denominator)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        s = format(dec.normalize(), 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')
    s = str(val)
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')
def bt_dang2_p3_b1_c9_hh8(self):
    # Dạng 2: Tìm chu vi tam giác qua tỉ số đồng dạng và hiệu hai chu vi
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k_choices = [Fraction(1, 2), Fraction(2, 5), Fraction(3, 5), Fraction(3, 4), Fraction(4, 5), Fraction(3, 10), Fraction(7, 10)]
        k = random.choice(k_choices)
        k_str = fmt_num(k)
        num_diff = k.denominator - k.numerator
        hieu = num_diff * random.randint(2, 9)
        c_lon = int(hieu * k.denominator // num_diff)
        c_nho = c_lon - hieu
        kq_str = str(c_nho)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (1.0,2.2);\n'
            ' \\coordinate (B) at (0,0);\n'
            ' \\coordinate (C) at (2.8,0);\n'
            ' \\coordinate (A1) at (4.6,1.4);\n'
            ' \\coordinate (B1) at (4.0,0);\n'
            ' \\coordinate (C1) at (5.7,0);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--cycle (A1)--(B1)--(C1)--cycle;\n'
            ' \\fill (A) circle (1pt) node[above] {$A$};\n'
            ' \\fill (B) circle (1pt) node[below left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (A1) circle (1pt) node[above] {$A\'$};\n'
            ' \\fill (B1) circle (1pt) node[below left] {$B\'$};\n'
            ' \\fill (C1) circle (1pt) node[below right] {$C\'$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho $\\Delta A'B'C' \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = %s$. Biết hiệu chu vi của $\\Delta ABC$ và $\\Delta A'B'C'$ là $%s\\text{ cm}$. Tính chu vi của $\\Delta A'B'C'$ (đơn vị: cm).\\\\
%s''' % (k_str, hieu, tikz_code)
        )

        loigiai = (
            '''Gọi chu vi của $\\Delta A'B'C'$ và $\\Delta ABC$ lần lượt là $C'$ và $C$ ($C' > 0, C > 0$).\\\\
Vì $\\Delta A'B'C' \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = %s$ nên ta có:\\\\
$\\frac{A'B'}{AB} = \\frac{B'C'}{BC} = \\frac{A'C'}{AC} = %s$.\\\\
Áp dụng tính chất của dãy tỉ số bằng nhau, ta có:\\\\
$\\frac{A'B'}{AB} = \\frac{B'C'}{BC} = \\frac{A'C'}{AC} = \\frac{A'B' + B'C' + A'C'}{AB + BC + AC} = \\frac{C'}{C} = %s \\Rightarrow C' = %s C$.\\\\
Theo đề bài, hiệu chu vi của $\\Delta ABC$ và $\\Delta A'B'C'$ là $%s\\text{ cm}$ nên:\\\\
$C - C' = %s \\Leftrightarrow C - %s C = %s \\Leftrightarrow %s C = %s \\Leftrightarrow C = %s\\text{ (cm)}$.\\\\
Suy ra chu vi của $\\Delta A'B'C'$ là $C' = %s - %s = %s\\text{ (cm)}$.''' % (
                k_str, k_str, k_str, k_str,
                hieu, hieu, k_str, hieu, fmt_num(1 - k), hieu, c_lon,
                c_lon, hieu, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
