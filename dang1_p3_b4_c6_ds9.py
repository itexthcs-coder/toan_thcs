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


def bt_dang1_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        w = randint(10, 25)
        diff = randint(4, 15)
        l = w + diff
        S = w * l
        chu_vi = 2 * (w + l)
        delta_val = diff**2 + 4 * S
        sqrt_delta = int(math.isqrt(delta_val))
        x1 = (-diff - sqrt_delta) // 2
        x2 = (-diff + sqrt_delta) // 2

        tikz = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.5);
    \\coordinate (B) at (4.5,2.5);
    \\coordinate (C) at (4.5,0);
    \\coordinate (D) at (0,0);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\node[above] at (2.25,2.5) {$x + %s$ (m)};
    \\node[right] at (4.5,1.25) {$x$ (m)};
\\end{tikzpicture}
\\end{center}''' % (str(diff)))

        noidungcauhoi = ('''Nhà trường dự định quy hoạch một vườn hoa hình chữ nhật có diện tích bằng $%s\\text{ m}^2$. Biết chiều dài lớn hơn chiều rộng $%s\\text{ m}$. Tính chu vi của vườn hoa đó (đơn vị: mét).'''
                         % (str(S), str(diff)))

        loigiai = ('''%s\\\\
                   Gọi chiều rộng của vườn hoa hình chữ nhật là $x$ (m). Điều kiện: $x > 0$.\\\\
                   Khi đó, chiều dài của vườn hoa là $x + %s$ (m).\\\\
                   Theo đề bài, diện tích vườn hoa bằng $%s\\text{ m}^2$ nên ta có phương trình:\\\\
                   $x(x + %s) = %s$ hay $x^2 + %sx - %s = 0$.\\\\
                   Ta có: $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-%s - %s}{2} = %s$ (loại); $x_2 = \\dfrac{-%s + %s}{2} = %s$ (thỏa mãn điều kiện).\\\\
                   Suy ra chiều rộng của vườn hoa là $%s\\text{ m}$ và chiều dài của vườn hoa là $%s + %s = %s\\text{ m}$.\\\\
                   Vậy chu vi của vườn hoa đó là $2 \\cdot (%s + %s) = %s$ (m).'''
                   % (tikz, str(diff), str(S), str(diff), str(S), str(diff), str(S),
                      str(diff), str(S), str(delta_val), str(sqrt_delta),
                      str(diff), str(sqrt_delta), str(x1), str(diff), str(sqrt_delta), str(x2),
                      str(w), str(w), str(diff), str(l), str(w), str(l), str(chu_vi)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(chu_vi))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
