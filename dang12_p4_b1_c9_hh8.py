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


def bt_dang12_p4_b1_c9_hh8(self):
    # Dạng 12: Bài toán đồng dạng qua điều kiện cạnh nhỏ nhất, cạnh lớn nhất
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Chọn các bộ (p, q, m, k_bc) thỏa mãn: p < k_bc < q, p + k_bc > q
        p, q, m, k_bc = random.choice([
            (2, 3, 4, 3),   # AB=8, BC=10? Chờ: AB = p*m, BC = k_bc*m, CA = q*m -> p < k_bc < q!
            (3, 5, 2, 4),   # AB=6, BC=8, CA=10 -> tỉ số 5/3
            (3, 5, 3, 4),   # AB=9, BC=12, CA=15 -> tỉ số 5/3
            (4, 7, 2, 5),   # AB=8, BC=10, CA=14 -> tỉ số 7/4
            (4, 7, 2, 6),   # AB=8, BC=12, CA=14 -> tỉ số 7/4
            (5, 8, 2, 6),   # AB=10, BC=12, CA=16 -> tỉ số 8/5
            (5, 8, 2, 7)    # AB=10, BC=14, CA=16 -> tỉ số 8/5
        ])
        if (p, q, m, k_bc) == (2, 3, 4, 3):
            p, q, m, k_bc = (3, 5, 4, 4)
        AB = p * m
        BC = k_bc * m
        CA = q * m
            
        MN = CA
        NP = k_bc * q
        PM = q * q
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (2.8,0);\n'
            '\\coordinate (A) at (0.6,1.8);\n'
            '\\coordinate (N) at (3.8,0);\n'
            '\\coordinate (P) at (8.2,0);\n'
            '\\coordinate (M) at (4.8,2.8);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N)--(P)--cycle;\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (M) circle (1pt) node[above] {$M$};\n'
            '\\fill (N) circle (1pt) node[left] {$N$};\n'
            '\\fill (P) circle (1pt) node[right] {$P$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC$ có $AB = %s\\text{ cm}$, $BC = %s\\text{ cm}$, $CA = %s\\text{ cm}$. '
            'Biết $\\Delta MNP \\backsim \\Delta ABC$ và cạnh nhỏ nhất của $\\Delta MNP$ có độ dài bằng cạnh lớn nhất của $\\Delta ABC$.\\\n'
            'a) Tìm tỉ số đồng dạng của $\\Delta MNP$ với $\\Delta ABC$.\\\n'
            'b) Tính độ dài các cạnh của $\\Delta MNP$.\\\n%s'
            % (AB, BC, CA, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Trong $\\Delta ABC$, ta có $AB < BC < CA$ (vì $%s < %s < %s$) nên cạnh nhỏ nhất là $AB = %s\\text{ cm}$ và cạnh lớn nhất là $CA = %s\\text{ cm}$.\\\n'
            'Vì $\\Delta MNP \\backsim \\Delta ABC$ nên thứ tự độ dài các cạnh tương ứng cũng được bảo toàn, tức là $MN < NP < PM$.\\\n'
            'Do đó cạnh nhỏ nhất của $\\Delta MNP$ là $MN$. Theo đề bài, $MN = CA = %s\\text{ cm}$.\\\n'
            'Vậy tỉ số đồng dạng của $\\Delta MNP$ với $\\Delta ABC$ là: $k = \\dfrac{MN}{AB} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.\n'
            '\\item Vì $\\Delta MNP \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$ nên:\\\n'
            '- $MN = %s\\text{ cm}$.\\\n'
            '- $NP = \\dfrac{%s}{%s} \\cdot BC = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\\\n'
            '- $PM = \\dfrac{%s}{%s} \\cdot CA = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (AB, BC, CA, AB, CA, CA, CA, AB, q, p,
               q, p, MN, q, p, q, p, BC, NP, q, p, q, p, CA, PM)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
