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


def bt_dang3_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([15, 20, 25, 30])
        b = a + random.choice([5, 10, 15])
        x_ans = random.choice([2, 3, 4, 5])
        S_anh = a * b
        S_tong = (a + 2 * x_ans) * (b + 2 * x_ans)
        S_vien = S_tong - S_anh
        he_so_b = 2 * (a + b)
        b_prime = a + b
        delta_p = b_prime**2 + 4 * S_vien
        sqrt_dp = int(math.isqrt(delta_p))
        x1 = (-b_prime - sqrt_dp) // 4
        x2 = (-b_prime + sqrt_dp) // 4

        tikz = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3);
    \\coordinate (B) at (4.5,3);
    \\coordinate (C) at (4.5,0);
    \\coordinate (D) at (0,0);
    \\coordinate (M) at (0.6,2.4);
    \\coordinate (N) at (3.9,2.4);
    \\coordinate (P) at (3.9,0.6);
    \\coordinate (Q) at (0.6,0.6);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt] (M)--(N)--(P)--(Q)--cycle;
    \\draw[line width=1pt, dashed] (0,1.5)--(0.6,1.5) (3.9,1.5)--(4.5,1.5) (2.25,2.4)--(2.25,3) (2.25,0)--(2.25,0.6);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\fill (N) circle (1pt) node[below left] {$N$};
    \\fill (P) circle (1pt) node[above left] {$P$};
    \\fill (Q) circle (1pt) node[above right] {$Q$};
    \\node[above] at (0.3,1.5) {$x$};
    \\node[above] at (4.2,1.5) {$x$};
    \\node[right] at (2.25,2.7) {$x$};
    \\node[right] at (2.25,0.3) {$x$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một bức ảnh hình chữ nhật kích thước $%s\\text{ cm} \\times %s\\text{ cm}$ được đặt trong một khung gỗ có bề rộng viền khung đều nhau ở cả bốn cạnh. Biết diện tích phần viền gỗ xung quanh bức ảnh bằng $%s\\text{ cm}^2$. Tính bề rộng của viền khung gỗ (đơn vị: cm).'''
                         % (str(a), str(b), str(S_vien)))

        loigiai = ('''%s\\\\
                   Gọi bề rộng của viền khung gỗ là $x$ (cm). Điều kiện: $x > 0$.\\\\
                   Khi đó, chiều rộng và chiều dài của cả khung tranh lần lượt là $2x + %s$ (cm) và $2x + %s$ (cm).\\\\
                   Diện tích của bức ảnh là $%s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.\\\\
                   Diện tích của cả khung tranh là $(2x + %s)(2x + %s)\\text{ (cm}^2\\text{)}$.\\\\
                   Vì diện tích phần viền gỗ bằng $%s\\text{ cm}^2$ nên ta có phương trình:\\\\
                   $(2x + %s)(2x + %s) - %s = %s$\\\\
                   $4x^2 + %sx + %s - %s = %s$\\\\
                   $4x^2 + %sx - %s = 0$.\\\\
                   Ta có: $\\Delta' = %s^2 - 4 \\cdot (-%s) = %s$; $\\sqrt{\\Delta'} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-%s - %s}{4} = %s$ (loại); $x_2 = \\dfrac{-%s + %s}{4} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy bề rộng của viền khung gỗ là $%s\\text{ cm}$.'''
                   % (tikz, str(a), str(b), str(a), str(b), str(S_anh),
                      str(a), str(b), str(S_vien), str(a), str(b), str(S_anh), str(S_vien),
                      str(he_so_b), str(S_anh), str(S_anh), str(S_vien),
                      str(he_so_b), str(S_vien), str(b_prime), str(S_vien), str(delta_p), str(sqrt_dp),
                      str(b_prime), str(sqrt_dp), str(x1), str(b_prime), str(sqrt_dp), str(x2), str(x_ans)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(x_ans))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
