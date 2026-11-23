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


def bt_dang2_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # (x + a)/he = (x + b)/kf => kf*(x+a) = he*(x+b) => (kf - he)*x = he*b - kf*a
        he = random.choice([4, 6])
        kf = he + 4
        a = random.randint(1, 3)
        b = a + 3
        x_val = Rational(he * b - kf * a, kf - he)
        if x_val.is_Integer:
            kq_str = str(int(x_val))
        else:
            kq_str = str(float(x_val)).replace('.', ',')

        noidungcauhoi = ("""Cho $\\Delta DEF$ có $HK // EF$ ($H \\in DE$, $K \\in DF$) như hình vẽ bên dưới. Biết $DH = x + %s$, $HE = %s$, $DK = x + %s$ và $KF = %s$ (với $x > 0$ và các kích thước có cùng đơn vị đo). Giá trị của $x$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (1.5,3);
\\coordinate (E) at (0,0);
\\coordinate (F) at (4.5,0);
\\coordinate (H) at ($(D)!0.45!(E)$);
\\coordinate (K) at ($(D)!0.45!(F)$);
\\draw[line width=1pt] (D)--(E)--(F)--cycle (H)--(K);
\\fill (D) circle (1pt) node[above] {$D$};
\\fill (E) circle (1pt) node[below left] {$E$};
\\fill (F) circle (1pt) node[below right] {$F$};
\\fill (H) circle (1pt) node[left] {$H$};
\\fill (K) circle (1pt) node[right] {$K$};
\\path (D)--(H) node[midway, left] {$x + %s$};
\\path (H)--(E) node[midway, left] {$%s$};
\\path (D)--(K) node[midway, right] {$x + %s$};
\\path (K)--(F) node[midway, right] {$%s$};
\\end{tikzpicture}
\\end{center}"""
                         % (a, he, b, kf, a, he, b, kf))

        loigiai = ("""Xét $\\Delta DEF$ có $HK // EF$ ($H \\in DE$, $K \\in DF$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{DH}{HE} = \\dfrac{DK}{KF}$ \\\\
Thay các biểu thức độ dài vào tỉ lệ thức trên, ta được: \\\\
$\\dfrac{x + %s}{%s} = \\dfrac{x + %s}{%s} \\Rightarrow %s(x + %s) = %s(x + %s)$ \\\\
$\\Leftrightarrow %s x + %s = %s x + %s \\Leftrightarrow %s x = %s \\Leftrightarrow x = %s$ (thỏa mãn $x > 0$). \\\\
Vậy $x = %s$."""
                   % (a, he, b, kf, kf, a, he, b,
                      kf, kf * a, he, he * b, kf - he, he * b - kf * a, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
