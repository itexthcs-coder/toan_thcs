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
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang11_p3_b3_c4_hh8(self):
    # Dạng 11: Tính độ dài đoạn thẳng trong tam giác qua hai lần định lí Thalès
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (2, 3, 27, 12),
            (1, 2, 24, 6),
            (1, 3, 36, 4),
            (3, 4, 32, 18),
            (2, 5, 50, 8)
        ]
        p, q, bc, mn = random.choice(bo_so)
        kq_str = fmt_num(mn)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (1.8,3.4);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.6,0);\n'
            '\\coordinate (I) at ($(A)!0.667!(B)$);\n'
            '\\coordinate (K) at ($(A)!0.667!(C)$);\n'
            '\\coordinate (M) at ($(A)!0.444!(C)$);\n'
            '\\coordinate (N) at ($(A)!0.444!(B)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(K) (C)--(I) (I)--(M) (K)--(N) (M)--(N);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (I) circle (1pt) node[left] {$I$};\n'
            '\\fill (K) circle (1pt) node[right] {$K$};\n'
            '\\fill (M) circle (1pt) node[above right] {$M$};\n'
            '\\fill (N) circle (1pt) node[above left] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ có $BC = %s\\text{ cm}$. Lấy điểm $I \\in AB$ sao cho $\\frac{AI}{AB} = \\frac{%s}{%s}$ và điểm $K \\in AC$ sao cho $\\frac{AK}{AC} = \\frac{%s}{%s}$. Kẻ $IM // BK$ ($M \\in AC$), kẻ $KN // CI$ ($N \\in AB$). Tính độ dài đoạn thẳng $MN$ (đơn vị: $\\text{cm}$).\n%s'
            % (bc, p, q, p, q, hinh_ve)
        )

        loigiai = (
            'Xét tam giác $ABK$ có $IM // BK$, theo định lí Thalès ta có: $\\frac{AM}{AK} = \\frac{AI}{AB} = \\frac{%s}{%s} \\Rightarrow \\frac{AM}{AC} = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\'
            'Xét tam giác $AIC$ có $KN // CI$, theo định lí Thalès ta có: $\\frac{AN}{AI} = \\frac{AK}{AC} = \\frac{%s}{%s} \\Rightarrow \\frac{AN}{AB} = \\frac{%s}{%s} \\cdot \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\'
            'Suy ra $\\frac{AN}{AB} = \\frac{AM}{AC} = \\frac{%s}{%s}$, theo định lí Thalès đảo ta có $MN // BC$.\\\\'
            'Theo hệ quả định lí Thalès, ta có $\\frac{MN}{BC} = \\frac{AN}{AB} = \\frac{%s}{%s} \\Rightarrow MN = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}$.'
            % (p, q, p, q, p, q, p * p, q * q, p, q, p, q, p, q, p * p, q * q, p * p, q * q, p * p, q * q, p * p, q * q, bc, kq_str)
        )

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
