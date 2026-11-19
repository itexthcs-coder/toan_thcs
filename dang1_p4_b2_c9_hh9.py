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

def bt_dang1_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'H', 'D'), ('M', 'N', 'P', 'K', 'E'), ('E', 'F', 'G', 'I', 'Q')]
        A, B, C, H, D = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (110:1.6);
\\coordinate (B) at (215:1.6);
\\coordinate (C) at (-35:1.6);
\\coordinate (D) at (-70:1.6);
\\coordinate (H) at (-0.547,-0.918);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(H) (A)--(D) (D)--(C);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[below] {$%(D)s$};
\\fill (H) circle (1pt) node[below] {$%(H)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'H': H})

        noidungcauhoi = ('''Cho tam giác nhọn $%(A)s%(B)s%(C)s$ ($%(A)s%(B)s < %(A)s%(C)s$) nội tiếp đường tròn $(O)$. Kẻ đường cao $%(A)s%(H)s$ của tam giác $%(A)s%(B)s%(C)s$ ($%(H)s \\in %(B)s%(C)s$) và đường kính $%(A)s%(D)s$ của đường tròn $(O)$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $\\Delta %(A)s%(B)s%(H)s \\backsim \\Delta %(A)s%(D)s%(C)s$.
\\item Từ đó suy ra hệ thức $%(A)s%(B)s \\cdot %(A)s%(C)s = 2R \\cdot %(A)s%(H)s$ (với $R$ là bán kính đường tròn $(O)$).
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'D': D, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét đường tròn $(O)$ có $\\widehat{%(A)s%(C)s%(D)s}$ là góc nội tiếp chắn nửa đường tròn đường kính $%(A)s%(D)s$ nên $\\widehat{%(A)s%(C)s%(D)s} = 90^\\circ$.\\\\
Lại có $%(A)s%(H)s \\perp %(B)s%(C)s$ tại $%(H)s$ nên $\\widehat{%(A)s%(H)s%(B)s} = 90^\\circ$.\\\\
Xét $\\Delta %(A)s%(B)s%(H)s$ và $\\Delta %(A)s%(D)s%(C)s$ có:
$$\\widehat{%(A)s%(H)s%(B)s} = \\widehat{%(A)s%(C)s%(D)s} = 90^\\circ,$$
$$\\widehat{%(A)s%(B)s%(H)s} = \\widehat{%(A)s%(D)s%(C)s} \\text{ (hai góc nội tiếp cùng chắn cung nhỏ } %(A)s%(C)s \\text{ của } (O)\\text{)}.$$
Vậy $\\Delta %(A)s%(B)s%(H)s \\backsim \\Delta %(A)s%(D)s%(C)s$ (g.g).
\\item Vì $\\Delta %(A)s%(B)s%(H)s \\backsim \\Delta %(A)s%(D)s%(C)s$ nên ta có tỉ số đồng dạng:
$$\\frac{%(A)s%(B)s}{%(A)s%(D)s} = \\frac{%(A)s%(H)s}{%(A)s%(C)s} \\Rightarrow %(A)s%(B)s \\cdot %(A)s%(C)s = %(A)s%(D)s \\cdot %(A)s%(H)s.$$
Mà $%(A)s%(D)s = 2R$ (đường kính đường tròn $(O)$) nên suy ra $%(A)s%(B)s \\cdot %(A)s%(C)s = 2R \\cdot %(A)s%(H)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'D': D})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
