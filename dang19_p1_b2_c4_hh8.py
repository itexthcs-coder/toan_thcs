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
    return str(val).replace('.', ',')

def bt_dang19_p1_b2_c4_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_diem = random.choice([
            ('A', 'B', 'C', 'D', 'E', 'F'),
            ('M', 'N', 'P', 'H', 'I', 'K')
        ])
        A, B, C, D, E, F = bo_diem
        bo_pyth = random.choice([(6, 8, 10), (12, 16, 20), (10, 24, 26), (16, 30, 34)])
        ab, ac, bc = bo_pyth
        de = ac // 2
        ef = ab // 2
        tong = de + ef
    
        du = ['$%s\\text{ cm}$' % fmt_num(tong)]
        da = random.choice(du)
        s = [
            '$%s\\text{ cm}$' % fmt_num(ab + ac),
            '$%s\\text{ cm}$' % fmt_num(bc),
            '$%s\\text{ cm}$' % fmt_num(bc // 2 + 1),
            '$%s\\text{ cm}$' % fmt_num(tong + 2),
            '$%s\\text{ cm}$' % fmt_num(tong - 2)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (0,3);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (4,3);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s)--(%s);
\\draw[line width=1pt] (0,2.7)--(0.3,2.7)--(0.3,3);
\\fill (%s) circle (1pt) node[above left] {$%s$};
\\fill (%s) circle (1pt) node[below left] {$%s$};
\\fill (%s) circle (1pt) node[above right] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[below right] {$%s$};
\\fill (%s) circle (1pt) node[above] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, A, B, E, B, C, F, A, C, A, B, C, D, E, F, A, A, B, B, C, C, D, D, E, E, F, F))
    
        noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ có $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$ (như hình vẽ). Tổng độ dài $%s%s + %s%s$ bằng%s''' % (A, B, C, A, A, B, fmt_num(ab), A, C, fmt_num(ac), D, E, F, A, B, B, C, C, A, D, E, E, F, hinhve))
    
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        loigiai = ('''Xét tam giác $%s%s%s$ có $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$.\\
Do đó, $%s%s$ và $%s%s$ là các đường trung bình của tam giác $%s%s%s$.\\
Theo tính chất đường trung bình của tam giác, ta có:\\
$%s%s = \\dfrac{1}{2}%s%s = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$;\\
$%s%s = \\dfrac{1}{2}%s%s = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.\\
Vậy tổng độ dài $%s%s + %s%s = %s + %s = %s\\text{ cm}$.''' % (A, B, C, D, E, F, A, B, B, C, C, A, D, E, E, F, A, B, C, D, E, A, C, fmt_num(ac), fmt_num(de), E, F, A, B, fmt_num(ab), fmt_num(ef), D, E, E, F, fmt_num(de), fmt_num(ef), fmt_num(tong)))
    
    # Xuất câu trắc nghiệm
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
