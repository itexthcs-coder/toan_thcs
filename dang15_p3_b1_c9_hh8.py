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
def bt_dang15_p3_b1_c9_hh8(self):
    # Dạng 15: Kết hợp định lí Pythagore và hai tam giác đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        pyth_triples = [
            (3, 4, 5),
            (6, 8, 10),
            (5, 12, 13),
            (8, 15, 17),
            (9, 12, 15),
            (12, 16, 20),
        ]
        ab, ac, bc = random.choice(pyth_triples)
        k = random.choice([2, 3, 4])
        k_sq = k * k
        np_val = bc * k
        kq_str = str(np_val)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (0,0);\n'
            ' \\coordinate (B) at (0,1.4);\n'
            ' \\coordinate (C) at (1.9,0);\n'
            ' \\coordinate (M) at (3.4,0);\n'
            ' \\coordinate (N) at (3.4,2.2);\n'
            ' \\coordinate (P) at (6.4,0);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N)--(P)--cycle;\n'
            ' \\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0) (3.4,0.2)--(3.6,0.2)--(3.6,0);\n'
            ' \\fill (A) circle (1pt) node[below left] {$A$};\n'
            ' \\fill (B) circle (1pt) node[above left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (M) circle (1pt) node[below left] {$M$};\n'
            ' \\fill (N) circle (1pt) node[above left] {$N$};\n'
            ' \\fill (P) circle (1pt) node[below right] {$P$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho $\\Delta ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Tam giác $MNP$ đồng dạng với $\\Delta ABC$ và có diện tích gấp $%s$ lần diện tích $\\Delta ABC$. Tính độ dài cạnh huyền $NP$ của $\\Delta MNP$ (đơn vị: cm).\\\\
%s''' % (ab, ac, k_sq, tikz_code)
        )

        loigiai = (
            '''Áp dụng định lí Pythagore vào $\\Delta ABC$ vuông tại $A$, ta có:\\\\
$BC^2 = AB^2 + AC^2 = %s^2 + %s^2 = %s + %s = %s \\Rightarrow BC = %s\\text{ (cm)}$.\\\\
Gọi $k$ là tỉ số đồng dạng của $\\Delta MNP$ và $\\Delta ABC$ ($k > 0$).\\\\
Vì $\\Delta MNP \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k$ nên $\\frac{MN}{AB} = \\frac{MP}{AC} = \\frac{NP}{BC} = k$, hay $MN = k \\cdot AB$ và $MP = k \\cdot AC$.\\\\
Mặt khác $\\Delta MNP$ vuông tại $M$ (do $\\hat{M} = \\hat{A} = 90^\\circ$) nên tỉ số diện tích của hai tam giác là:\\\\
$\\frac{S_{\\Delta MNP}}{S_{\\Delta ABC}} = \\frac{\\frac{1}{2} MN \\cdot MP}{\\frac{1}{2} AB \\cdot AC} = \\frac{MN}{AB} \\cdot \\frac{MP}{AC} = k^2$.\\\\
Theo đề bài, diện tích $\\Delta MNP$ gấp $%s$ lần diện tích $\\Delta ABC$ nên $k^2 = %s \\Rightarrow k = %s$ (vì $k > 0$).\\\\
Vậy độ dài cạnh huyền $NP$ của $\\Delta MNP$ là:\\\\
$NP = k \\cdot BC = %s \\cdot %s = %s\\text{ (cm)}$.''' % (
                ab, ac, ab*ab, ac*ac, bc*bc, bc,
                k_sq, k_sq, k,
                k, bc, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
