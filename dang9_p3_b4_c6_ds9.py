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


def bt_dang9_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
        a, b, c = random.choice(bo_pythagore)
        diff = b - a
        c_val = (c**2 - diff**2) // 2
        delta_val = diff**2 + 4 * c_val
        sqrt_d = int(math.isqrt(delta_val))
        x1 = (-diff - sqrt_d) // 2
        x2 = (-diff + sqrt_d) // 2

        tikz = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (0,3.2);
    \\coordinate (C) at (2.4,0);
    \\draw[line width=1pt] (0,3.8)--(A)--(3.2,0);
    \\draw[line width=1pt] (B)--(C);
    \\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\node[right] at (1.3,1.7) {$%s\\text{ m}$};
    \\node[below] at (1.2,0) {$x$};
    \\node[left] at (0,1.6) {$x + %s$};
\\end{tikzpicture}
\\end{center}''' % (str(c), str(diff)))

        noidungcauhoi = ('''Một chiếc thang dài $%s\\text{ m}$ dựa vào một bức tường thẳng đứng. Biết khoảng cách từ đỉnh thang đến mặt đất lớn hơn khoảng cách từ chân thang đến chân tường là $%s\\text{ m}$. Tính khoảng cách từ chân thang đến chân tường (đơn vị: mét).'''
                         % (str(c), str(diff)))

        loigiai = ('''%s\\\\
                   Gọi khoảng cách từ chân thang đến chân tường là $x$ (m). Điều kiện: $0 < x < %s$.\\\\
                   Khi đó, khoảng cách từ đỉnh thang đến mặt đất là $x + %s$ (m).\\\\
                   Vì bức tường thẳng đứng vuông góc với mặt đất nên áp dụng định lí Pythagore, ta có phương trình:\\\\
                   $x^2 + (x + %s)^2 = %s^2$\\\\
                   $x^2 + x^2 + %sx + %s = %s$\\\\
                   $2x^2 + %sx - %s = 0$ hay $x^2 + %sx - %s = 0$.\\\\
                   Ta có: $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-%s - %s}{2} = %s$ (loại); $x_2 = \\dfrac{-%s + %s}{2} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy khoảng cách từ chân thang đến chân tường là $%s\\text{ m}$.'''
                   % (tikz, str(c), str(diff), str(diff), str(c),
                      str(2 * diff), str(diff**2), str(c**2),
                      str(2 * diff), str(c**2 - diff**2), str(diff), str(c_val),
                      str(diff), str(c_val), str(delta_val), str(sqrt_d),
                      str(diff), str(sqrt_d), str(x1), str(diff), str(sqrt_d), str(x2), str(a)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(a))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
