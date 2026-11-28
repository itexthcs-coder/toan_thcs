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
def bt_dang1_p3_b1_c9_hh8(self):
    # Dạng 1: Tìm độ dài cạnh dựa vào tính chất bắc cầu của ba tam giác đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        pairs = [
            (Fraction(1, 2), Fraction(2, 3)),
            (Fraction(2, 3), Fraction(3, 4)),
            (Fraction(3, 4), Fraction(2, 3)),
            (Fraction(1, 3), Fraction(3, 5)),
            (Fraction(2, 5), Fraction(5, 4)),
            (Fraction(3, 5), Fraction(5, 6)),
            (Fraction(2, 3), Fraction(3, 5)),
            (Fraction(1, 2), Fraction(4, 5)),
        ]
        k1, k2 = random.choice(pairs)
        k = k1 * k2
        mn = k.denominator * random.randint(2, 8)
        ab = int(mn * k)
        
        k1_tex = '\\frac{%s}{%s}' % (k1.numerator, k1.denominator)
        k2_tex = '\\frac{%s}{%s}' % (k2.numerator, k2.denominator)
        k_tex = '\\frac{%s}{%s}' % (k.numerator, k.denominator)
        kq_str = str(ab)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (0.4,1.2);\n'
            ' \\coordinate (B) at (0,0);\n'
            ' \\coordinate (C) at (1.5,0);\n'
            ' \\coordinate (D) at (2.8,1.6);\n'
            ' \\coordinate (E) at (2.2,0);\n'
            ' \\coordinate (F) at (4.2,0);\n'
            ' \\coordinate (M) at (5.7,2.1);\n'
            ' \\coordinate (N) at (5.0,0);\n'
            ' \\coordinate (P) at (7.6,0);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E)--(F)--cycle (M)--(N)--(P)--cycle;\n'
            ' \\fill (A) circle (1pt) node[above] {$A$};\n'
            ' \\fill (B) circle (1pt) node[below left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (D) circle (1pt) node[above] {$D$};\n'
            ' \\fill (E) circle (1pt) node[below left] {$E$};\n'
            ' \\fill (F) circle (1pt) node[below right] {$F$};\n'
            ' \\fill (M) circle (1pt) node[above] {$M$};\n'
            ' \\fill (N) circle (1pt) node[below left] {$N$};\n'
            ' \\fill (P) circle (1pt) node[below right] {$P$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho $\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $k_1 = %s$ và $\\Delta DEF \\backsim \\Delta MNP$ theo tỉ số đồng dạng $k_2 = %s$. Biết $MN = %s\\text{ cm}$, tính độ dài cạnh $AB$ (đơn vị: cm).\\\\
%s''' % (k1_tex, k2_tex, mn, tikz_code)
        )

        loigiai = (
            '''Vì $\\Delta ABC \\backsim \\Delta DEF$ theo tỉ số đồng dạng $k_1 = %s$ và $\\Delta DEF \\backsim \\Delta MNP$ theo tỉ số đồng dạng $k_2 = %s$ nên theo tính chất bắc cầu của hai tam giác đồng dạng ta có $\\Delta ABC \\backsim \\Delta MNP$ theo tỉ số đồng dạng là:\\\\
$k = k_1 \\cdot k_2 = %s \\cdot %s = %s$.\\\\
Do $\\Delta ABC \\backsim \\Delta MNP$ theo tỉ số đồng dạng $k = %s$ nên ta có tỉ số các cạnh tương ứng:\\\\
$\\frac{AB}{MN} = %s \\Rightarrow AB = %s \\cdot MN = %s \\cdot %s = %s\\text{ (cm)}$.\\\\
Vậy độ dài cạnh $AB$ bằng $%s\\text{ cm}$.''' % (
                k1_tex, k2_tex, k1_tex, k2_tex, k_tex,
                k_tex, k_tex, k_tex, k_tex, mn, kq_str, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
