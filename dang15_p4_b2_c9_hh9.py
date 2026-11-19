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

def bt_dang15_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (I) at (1.62,0.88);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.88);
\\draw[line width=1pt, dashed] (A)--(I) (B)--(I) (C)--(I);
\\fill (I) circle (1pt) node[above right] {$I$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C})

        noidungcauhoi = ('''Cho tam giác nhọn $%(A)s%(B)s%(C)s$ có diện tích $S$, độ dài ba cạnh $%(B)s%(C)s = a$, $%(C)s%(A)s = b$, $%(A)s%(B)s = c$ và bán kính đường tròn nội tiếp là $r$. Gọi $h_a, h_b, h_c$ lần lượt là độ dài ba đường cao kẻ từ các đỉnh $%(A)s, %(B)s, %(C)s$ của tam giác.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $S = \\frac{a + b + c}{2} \\cdot r$.
\\item Chứng minh rằng $\\frac{1}{h_a} + \\frac{1}{h_b} + \\frac{1}{h_c} = \\frac{1}{r}$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $I$ là tâm đường tròn nội tiếp tam giác $%(A)s%(B)s%(C)s$. Khi đó khoảng cách từ $I$ đến ba cạnh $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$ đều bằng bán kính $r$ của đường tròn nội tiếp.\\\\
Chia tam giác $%(A)s%(B)s%(C)s$ thành ba tam giác $I%(B)s%(C)s$, $I%(C)s%(A)s$ và $I%(A)s%(B)s$, ta có diện tích tam giác $%(A)s%(B)s%(C)s$ là:
$$S = S_{I%(B)s%(C)s} + S_{I%(C)s%(A)s} + S_{I%(A)s%(B)s} = \\frac{1}{2}a \\cdot r + \\frac{1}{2}b \\cdot r + \\frac{1}{2}c \\cdot r = \\frac{a + b + c}{2} \\cdot r.$$
\\item Theo công thức tính diện tích tam giác qua đường cao, ta có:
$$S = \\frac{1}{2}a \\cdot h_a = \\frac{1}{2}b \\cdot h_b = \\frac{1}{2}c \\cdot h_c.$$
Suy ra $\\frac{1}{h_a} = \\frac{a}{2S}$, $\\frac{1}{h_b} = \\frac{b}{2S}$, $\\frac{1}{h_c} = \\frac{c}{2S}$.\\\\
Cộng vế với vế ba đẳng thức trên, ta được:
$$\\frac{1}{h_a} + \\frac{1}{h_b} + \\frac{1}{h_c} = \\frac{a + b + c}{2S}.$$
Từ câu a), ta có $\\frac{a + b + c}{2S} = \\frac{1}{r}$. Vậy $\\frac{1}{h_a} + \\frac{1}{h_b} + \\frac{1}{h_c} = \\frac{1}{r}$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
