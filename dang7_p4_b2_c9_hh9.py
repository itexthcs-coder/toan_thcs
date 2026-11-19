# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang7_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'D', 'E', 'F'), ('M', 'N', 'P', 'H', 'K', 'Q')]
        A, B, C, D, E, F = random.choice(bo_diem)
        k = random.choice([1, 2])
        a = 14 * k
        b = 13 * k
        c = 15 * k
        p = 21 * k
        bd = p - b
        ce = p - c
        af = p - a

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (I) at (1.62,0.9);
\\coordinate (D) at (1.62,0);
\\coordinate (E) at (2.44,1.25);
\\coordinate (F) at (0.84,1.4);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.9);
\\fill (I) circle (1pt) node[below] {$I$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[below] {$%(D)s$};
\\fill (E) circle (1pt) node[right] {$%(E)s$};
\\fill (F) circle (1pt) node[left] {$%(F)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F})

        noidungcauhoi = ('''Cho đường tròn $(I)$ nội tiếp tam giác $%(A)s%(B)s%(C)s$, tiếp xúc với các cạnh $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$ lần lượt tại $%(D)s, %(E)s, %(F)s$. Đặt $%(B)s%(C)s = a$, $%(C)s%(A)s = b$, $%(A)s%(B)s = c$ và $p = \\frac{a + b + c}{2}$ là nửa chu vi tam giác $%(A)s%(B)s%(C)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $%(A)s%(E)s = %(A)s%(F)s = p - a$; $%(B)s%(D)s = %(B)s%(F)s = p - b$; $%(C)s%(D)s = %(C)s%(E)s = p - c$.
\\item Biết $a = %(a)s\\text{ cm}$, $b = %(b)s\\text{ cm}$, $c = %(c)s\\text{ cm}$. Tính độ dài các đoạn thẳng $%(B)s%(D)s, %(C)s%(E)s, %(A)s%(F)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'hv': hinh_ve, 'a': a, 'b': b, 'c': c})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Theo tính chất hai tiếp tuyến cắt nhau của đường tròn $(I)$, ta có:
$$%(A)s%(E)s = %(A)s%(F)s, \\quad %(B)s%(D)s = %(B)s%(F)s, \\quad %(C)s%(D)s = %(C)s%(E)s.$$
Chu vi tam giác $%(A)s%(B)s%(C)s$ là:
$$2p = a + b + c = %(B)s%(C)s + %(C)s%(A)s + %(A)s%(B)s = (%(B)s%(D)s + %(C)s%(D)s) + (%(C)s%(E)s + %(A)s%(E)s) + (%(A)s%(F)s + %(B)s%(F)s) = 2(%(A)s%(E)s + %(B)s%(D)s + %(C)s%(D)s).$$
Suy ra $p = %(A)s%(E)s + %(B)s%(D)s + %(C)s%(D)s$.\\\\
Do đó:
$$%(A)s%(E)s = %(A)s%(F)s = p - (%(B)s%(D)s + %(C)s%(D)s) = p - %(B)s%(C)s = p - a.$$
Chứng minh hoàn toàn tương tự, ta được $%(B)s%(D)s = %(B)s%(F)s = p - b$ và $%(C)s%(D)s = %(C)s%(E)s = p - c$.
\\item Nửa chu vi tam giác $%(A)s%(B)s%(C)s$ là $p = \\frac{%(a)s + %(b)s + %(c)s}{2} = %(p)s\\text{ (cm)}$.\\\\
Áp dụng kết quả câu a), ta có:
$$%(B)s%(D)s = p - b = %(p)s - %(b)s = %(bd)s\\text{ (cm)}; \\quad %(C)s%(E)s = p - c = %(p)s - %(c)s = %(ce)s\\text{ (cm)}; \\quad %(A)s%(F)s = p - a = %(p)s - %(a)s = %(af)s\\text{ (cm)}.$$
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'a': a, 'b': b, 'c': c, 'p': p, 'bd': bd, 'ce': ce, 'af': af})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
