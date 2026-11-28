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


def bt_dang1_p4_b1_c9_hh8(self):
    # Dạng 1: Tính độ dài đoạn thẳng chưa biết qua chuỗi tam giác đồng dạng liên tiếp (tính chất bắc cầu)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k1_num, k1_den = random.choice([(2, 3), (3, 4), (3, 5), (4, 5)])
        k2_num, k2_den = random.choice([(1, 2), (1, 3), (2, 3)])
        
        mult = random.choice([2, 3, 4])
        AB = k1_den * k2_den * mult
        AM = k1_num * k2_den * mult
        AP = k1_num * k2_num * mult
        
        AC = AB + random.choice([3, 6, 9])
        BC = random.choice([3, 4, 5]) * k1_den * k2_den
        
        MN = BC * k1_num // k1_den
        PQ = MN * k2_num // k2_den
        
        k_num = k1_num * k2_num
        k_den = k1_den * k2_den
        g = math.gcd(k_num, k_den)
        k_num //= g
        k_den //= g
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (A) at (1.5,3.5);\n'
            '\\coordinate (M) at ($(A)!0.65!(B)$);\n'
            '\\coordinate (N) at ($(A)!0.65!(C)$);\n'
            '\\coordinate (P) at ($(A)!0.3!(B)$);\n'
            '\\coordinate (Q) at ($(A)!0.3!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (P)--(Q);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (P) circle (1pt) node[left] {$P$};\n'
            '\\fill (Q) circle (1pt) node[right] {$Q$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$, $BC = %s\\text{ cm}$. '
            'Lấy điểm $M$ trên cạnh $AB$ sao cho $AM = %s\\text{ cm}$, qua $M$ kẻ đường thẳng song song với $BC$ cắt $AC$ tại $N$. '
            'Tiếp tục lấy điểm $P$ trên đoạn $AM$ sao cho $AP = %s\\text{ cm}$, qua $P$ kẻ đường thẳng song song với $MN$ cắt $AN$ tại $Q$.\\\n'
            'a) Tìm tỉ số đồng dạng của $\\Delta APQ$ với $\\Delta ABC$.\\\n'
            'b) Tính độ dài đoạn thẳng $PQ$.\\\n%s'
            % (AB, AC, BC, AM, AP, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\Delta ABC$ có $MN // BC$ ($M \\in AB$, $N \\in AC$) nên $\\Delta AMN \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k_1 = \\dfrac{AM}{AB} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.\\\n'
            'Xét $\\Delta AMN$ có $PQ // MN$ ($P \\in AM$, $Q \\in AN$) nên $\\Delta APQ \\backsim \\Delta AMN$ theo tỉ số đồng dạng $k_2 = \\dfrac{AP}{AM} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.\\\n'
            'Theo tính chất bắc cầu, ta có $\\Delta APQ \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = k_1 \\cdot k_2 = \\dfrac{%s}{%s} \\cdot \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.\n'
            '\\item Vì $\\Delta APQ \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$ nên $\\dfrac{PQ}{BC} = \\dfrac{%s}{%s}$.\\\n'
            'Suy ra $PQ = \\dfrac{%s}{%s} \\cdot BC = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (AM, AB, k1_num, k1_den, AP, AM, k2_num, k2_den, k1_num, k1_den, k2_num, k2_den, k_num, k_den,
               k_num, k_den, k_num, k_den, k_num, k_den, k_num, k_den, BC, PQ)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
