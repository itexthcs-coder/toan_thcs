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

def bt_dang20_p1_b3_c4_hh8(self):
    # Dạng 20: Tính độ dài đoạn thẳng dựa vào tính chất đường phân giác ngoài
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        p = random.choice([2, 3])
        q = random.choice([3, 4, 5])
        while p >= q or math.gcd(p, q) != 1:
            p = random.choice([2, 3])
            q = random.choice([3, 4, 5])
        k = random.choice([2, 3])
        m = random.choice([3, 4, 5])
        
        ab = p * k
        ac = q * k
        bc = (q - p) * m
        d1b = p * m
        d1c = q * m
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (3.2,2.2);\n'
            '\\coordinate (B) at (2.8,0);\n'
            '\\coordinate (C) at (6.2,0);\n'
            '\\coordinate (X) at (0.8,3.96);\n'
            '\\coordinate (D1) at (0,0);\n'
            '\\draw[line width=1pt] (D1)--(C) (X)--(C) (A)--(B) (D1)--(A);\n'
            '\\fill (A) circle (1pt) node[above right] {$A$};\n'
            '\\fill (B) circle (1pt) node[below] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D1) circle (1pt) node[above left] {$D\'$};\n'
            '\\node[below left] at (X) {$x$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        da = '$%s\\text{ cm}$' % d1b
        s_vals = set()
        s_vals.add(fmt_num(d1c))
        s_vals.add(fmt_num(d1b + 3))
        s_vals.add(fmt_num(abs(d1b - 2)) if abs(d1b - 2) != d1b else d1b + 4)
        s_vals.add(fmt_num(bc * 2))
        s_vals.discard(fmt_num(d1b))
        extra_step = 1
        while len(s_vals) < 4:
            cand = fmt_num(extra_step * 5 + 3)
            if '$' + cand + '$' != da and '$' + cand + '\\text{ cm}$' != da:
                s_vals.add(cand)
            extra_step += 1
        s = ['$%s\\text{ cm}$' % fmt_num(v) for v in s_vals]
        
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = (
            'Cho tam giác $ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$, $BC = %s\\text{ cm}$. Tia phân giác của góc ngoài $BAx$ tại đỉnh $A$ cắt đường thẳng $BC$ tại $D\'$ ($B$ nằm giữa $D\'$ và $C$). Độ dài đoạn thẳng $D\'B$ bằng:\n%s'
            % (ab, ac, bc, hinh_ve)
        )
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = (
            'Vì $AD\'$ là đường phân giác ngoài tại đỉnh $A$ của tam giác $ABC$ nên theo tính chất đường phân giác ngoài, ta có:\\'
            '$\\frac{D\'B}{D\'C} = \\frac{AB}{AC} = \\frac{%s}{%s} = \\frac{%s}{%s}$.\\'
            'Vì điểm $B$ nằm giữa hai điểm $D\'$ và $C$ nên $D\'C = D\'B + BC = D\'B + %s$.\\'
            'Thay vào tỉ lệ thức ta được $\\frac{D\'B}{D\'B + %s} = \\frac{%s}{%s}$.\\'
            'Suy ra $%s \\cdot D\'B = %s(D\'B + %s) \\Leftrightarrow %s \\cdot D\'B = %s \\cdot D\'B + %s \\Leftrightarrow %s \\cdot D\'B = %s \\Leftrightarrow D\'B = %s\\text{ cm}$.'
            % (ab, ac, p, q, bc, bc, p, q, q, p, bc, q, p, p * bc, q - p, p * bc, d1b)
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
