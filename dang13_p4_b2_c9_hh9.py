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

def bt_dang13_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'M', 'N'), ('P', 'Q', 'R', 'E', 'F')]
        A, B, C, M, N = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (G) at (0,0);
\\coordinate (A) at (90:1.6);
\\coordinate (B) at (210:1.6);
\\coordinate (C) at (-30:1.6);
\\coordinate (M) at (-0.85,0.13);
\\coordinate (N) at (0.65,0.47);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (M)--(N);
\\draw[line width=1pt, dashed] (A)--(G);
\\fill (G) circle (1pt) node[below] {$G$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (M) circle (1pt) node[left] {$%(M)s$};
\\fill (N) circle (1pt) node[right] {$%(N)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'M': M, 'N': N})

        noidungcauhoi = ('''Cho tam giác đều $%(A)s%(B)s%(C)s$ cạnh $a$ có tâm đường tròn nội tiếp là $G$. Một đường thẳng $d$ đi qua $G$ cắt hai cạnh $%(A)s%(B)s, %(A)s%(C)s$ lần lượt tại $%(M)s$ và $%(N)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $\\frac{1}{%(A)s%(M)s} + \\frac{1}{%(A)s%(N)s} = \\frac{3}{a}$.
\\item Tìm vị trí của đường thẳng $d$ để diện tích tam giác $%(A)s%(M)s%(N)s$ đạt giá trị nhỏ nhất và tính giá trị nhỏ nhất đó theo $a$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'M': M, 'N': N, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì tam giác $%(A)s%(B)s%(C)s$ đều nên tâm đường tròn nội tiếp $G$ trùng với trọng tâm của tam giác.\\\\
Kẻ đường cao $%(A)sH$ của tam giác đều $%(A)s%(B)s%(C)s$, ta có $%(A)sH = \\frac{a\\sqrt{3}}{2}$ và $%(A)sG = \\frac{2}{3}%(A)sH = \\frac{a\\sqrt{3}}{3}$, $\\widehat{G%(A)s%(M)s} = \\widehat{G%(A)s%(N)s} = 30^\\circ$.\\\\
Ta có $S_{%(A)s%(M)s%(N)s} = S_{%(A)sG%(M)s} + S_{%(A)sG%(N)s}$, hay:
$$\\frac{1}{2}%(A)s%(M)s \\cdot %(A)s%(N)s \\sin 60^\\circ = \\frac{1}{2}%(A)s%(M)s \\cdot %(A)sG \\sin 30^\\circ + \\frac{1}{2}%(A)s%(N)s \\cdot %(A)sG \\sin 30^\\circ.$$
Thay $\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$, $\\sin 30^\\circ = \\frac{1}{2}$ và $%(A)sG = \\frac{a\\sqrt{3}}{3}$, ta được:
$$\\frac{\\sqrt{3}}{4}%(A)s%(M)s \\cdot %(A)s%(N)s = \\frac{1}{4} \\cdot \\frac{a\\sqrt{3}}{3}(%(A)s%(M)s + %(A)s%(N)s) \\Leftrightarrow 3%(A)s%(M)s \\cdot %(A)s%(N)s = a(%(A)s%(M)s + %(A)s%(N)s).$$
Chia cả hai vế cho $a \\cdot %(A)s%(M)s \\cdot %(A)s%(N)s$, ta được $\\frac{1}{%(A)s%(M)s} + \\frac{1}{%(A)s%(N)s} = \\frac{3}{a}$.
\\item Áp dụng bất đẳng thức Cauchy (AM-GM) cho hai số dương $\\frac{1}{%(A)s%(M)s}$ và $\\frac{1}{%(A)s%(N)s}$:
$$\\frac{3}{a} = \\frac{1}{%(A)s%(M)s} + \\frac{1}{%(A)s%(N)s} \\ge \\frac{2}{\\sqrt{%(A)s%(M)s \\cdot %(A)s%(N)s}} \\Rightarrow \\sqrt{%(A)s%(M)s \\cdot %(A)s%(N)s} \\ge \\frac{2a}{3} \\Rightarrow %(A)s%(M)s \\cdot %(A)s%(N)s \\ge \\frac{4a^2}{9}.$$
Diện tích tam giác $%(A)s%(M)s%(N)s$ là $S_{%(A)s%(M)s%(N)s} = \\frac{%(A)s%(M)s \\cdot %(A)s%(N)s \\sqrt{3}}{4} \\ge \\frac{4a^2}{9} \\cdot \\frac{\\sqrt{3}}{4} = \\frac{a^2\\sqrt{3}}{9}$.\\\\
Dấu bằng xảy ra khi và chỉ khi $%(A)s%(M)s = %(A)s%(N)s = \\frac{2a}{3}$, tức là đường thẳng $d$ đi qua $G$ và song song với cạnh $%(B)s%(C)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'M': M, 'N': N})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
