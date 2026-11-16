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


def bt_dang1_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'a', 'b', 'c'),
            ('M', 'N', 'P', 'm', 'n', 'p'),
            ('D', 'E', 'F', 'd', 'e', 'f')
        ]
        A, B, C, a, b, c = random.choice(bo_dinh)
        goc = random.choice(['\\alpha', '\\beta', '\\varphi'])

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (%s) at (0,0);
    \\coordinate (%s) at (4.0,0);
    \\coordinate (%s) at (0,2.5);
    \\draw[line width=1pt] (%s)--(%s)--(%s)--cycle;
    \\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
    \\draw[line width=1pt] (3.35,0) arc (180:148:0.65);
    \\fill (%s) circle (1pt) node[below left] {$%s$};
    \\fill (%s) circle (1pt) node[below right] {$%s$};
    \\fill (%s) circle (1pt) node[above left] {$%s$};
    \\node[left] at (0,1.25) {$%s$};
    \\node[below] at (2.0,0) {$%s$};
    \\node[above right] at (2.0,1.25) {$%s$};
    \\node at (3.08,0.25) {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (A, B, C, A, B, C, A, A, B, B, C, C, b, c, a, goc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ có $\\widehat{%s} = %s$, $%s%s = %s$, $%s%s = %s$, $%s%s = %s$ (như hình vẽ). \\\\
    a) Viết các tỉ số lượng giác $\\sin %s$, $\\cos %s$, $\\tan %s$, $\\cot %s$ theo $%s, %s, %s$. \\\\
    b) Sử dụng định lí Pythagore, chứng minh rằng $\\sin^2 %s + \\cos^2 %s = 1$ và $1 + \\tan^2 %s = \\dfrac{1}{\\cos^2 %s}$. \\\\
    c) Chứng minh rằng với mọi góc nhọn $%s$, ta luôn có $\\sin %s + \\cos %s > 1$.
    %s''' % (A, B, C, A, B, goc, B, C, a, A, C, b, A, B, c,
             goc, goc, goc, goc, a, b, c,
             goc, goc, goc, goc,
             goc, goc, goc, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $%s%s%s$ vuông tại $%s$, theo định nghĩa tỉ số lượng giác của góc nhọn ta có:\\\\
    $\\sin %s = \\dfrac{%s}{%s}$; $\\cos %s = \\dfrac{%s}{%s}$; $\\tan %s = \\dfrac{%s}{%s}$; $\\cot %s = \\dfrac{%s}{%s}$.
    \\item Áp dụng định lí Pythagore trong tam giác $%s%s%s$ vuông tại $%s$, ta có $%s^2 + %s^2 = %s^2$.\\\\
    Khi đó: $\\sin^2 %s + \\cos^2 %s = \\left(\\dfrac{%s}{%s}\\right)^2 + \\left(\\dfrac{%s}{%s}\\right)^2 = \\dfrac{%s^2 + %s^2}{%s^2} = \\dfrac{%s^2}{%s^2} = 1$.\\\\
    Mặt khác: $1 + \\tan^2 %s = 1 + \\left(\\dfrac{%s}{%s}\\right)^2 = \\dfrac{%s^2 + %s^2}{%s^2} = \\dfrac{%s^2}{%s^2} = \\left(\\dfrac{%s}{%s}\\right)^2 = \\dfrac{1}{\\cos^2 %s}$.
    \\item Trong tam giác $%s%s%s$, theo bất đẳng thức tam giác ta luôn có $%s + %s > %s$.\\\\
    Chia cả hai vế của bất đẳng thức trên cho số dương $%s$, ta được $\\dfrac{%s}{%s} + \\dfrac{%s}{%s} > 1$, hay $\\sin %s + \\cos %s > 1$.
    \\end{enumEX}'''
                   % (A, B, C, A, goc, b, a, goc, c, a, goc, b, c, goc, c, b,
                      A, B, C, A, b, c, a,
                      goc, goc, b, a, c, a, b, c, a, a, a,
                      goc, b, c, c, b, c, a, c, a, c, goc,
                      A, B, C, b, c, a, a, b, a, c, a, goc, goc))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
