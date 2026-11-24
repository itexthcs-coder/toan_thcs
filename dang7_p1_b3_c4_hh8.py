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

def bt_dang7_p1_b3_c4_hh8(self):
    # Dạng 7: Nhận biết song song qua góc đồng vị và tính đoạn thẳng theo định lí Thalès
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([2, 3, 4])
        m = random.choice([1.5, 2, 2.5, 3])
        am = k * 2
        mb = k * 3
        an = m * 2
        nc = m * 3
        
        s_am = fmt_num(am)
        s_mb = fmt_num(mb)
        s_an = fmt_num(an)
        s_nc = fmt_num(nc)
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (1.8,3.2);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.5,0);\n'
            '\\coordinate (M) at ($(A)!0.4!(B)$);\n'
            '\\coordinate (N) at ($(A)!0.4!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\node[above left] at ($(A)!0.5!(M)$) {$%s$};\n'
            '\\node[left] at ($(M)!0.5!(B)$) {$%s$};\n'
            '\\node[above right] at ($(A)!0.5!(N)$) {$%s$};\n'
            '\\node[right] at ($(N)!0.5!(C)$) {$x$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (s_am, s_mb, s_an)
        
        da = '$%s$' % s_nc
        s_vals = set()
        s_vals.add(fmt_num(round(an * am / mb, 2)))
        s_vals.add(fmt_num(nc + 1.5))
        s_vals.add(fmt_num(nc + 2.5))
        s_vals.add(fmt_num(abs(nc - 1.5) if abs(nc - 1.5) != nc else nc + 1))
        s_vals.discard(fmt_num(s_nc))
        extra_step = 1
        while len(s_vals) < 4:
            cand = fmt_num(extra_step * 5 + 3)
            if '$' + cand + '$' != da and '$' + cand + '\\text{ cm}$' != da:
                s_vals.add(cand)
            extra_step += 1
        s = ['$%s$' % v for v in s_vals]
        
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = (
            'Cho tam giác $ABC$, lấy điểm $M \\in AB$ và $N \\in AC$ sao cho $\\widehat{AMN} = \\widehat{ABC}$. Biết $AM = %s$, $MB = %s$, $AN = %s$ và $NC = x$ như hình vẽ. Độ dài $x$ bằng:\n%s'
            % (s_am, s_mb, s_an, hinh_ve)
        )
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = (
            'Ta có $\\widehat{AMN} = \\widehat{ABC}$ (giả thiết), mà hai góc này ở vị trí đồng vị nên $MN // BC$ (dấu hiệu nhận biết hai đường thẳng song song).\\'
            'Áp dụng định lí Thalès trong tam giác $ABC$ có $MN // BC$, ta có:\\'
            '$\\frac{AM}{MB} = \\frac{AN}{NC}$ hay $\\frac{%s}{%s} = \\frac{%s}{x}$.\\'
            'Suy ra $x = \\frac{%s \\cdot %s}{%s} = %s$.'
            % (s_am, s_mb, s_an, s_mb, s_an, s_am, s_nc)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
