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

def bt_dang9_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'D', 'E', 'F'), ('M', 'N', 'P', 'H', 'K', 'Q')]
        A, B, C, D, E, F = random.choice(bo_diem)

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
\\draw[line width=1pt] (D)--(E)--(F)--cycle;
\\draw[line width=1pt, dashed] (I)--(E) (I)--(F);
\\fill (I) circle (1pt) node[below] {$I$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[below] {$%(D)s$};
\\fill (E) circle (1pt) node[right] {$%(E)s$};
\\fill (F) circle (1pt) node[left] {$%(F)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ ngoại tiếp đường tròn $(I)$ với các tiếp điểm trên $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$ lần lượt là $%(D)s, %(E)s, %(F)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $\\widehat{%(E)s%(D)s%(F)s} = 90^\\circ - \\frac{\\widehat{%(B)s%(A)s%(C)s}}{2}$.
\\item Chứng minh rằng tam giác $%(D)s%(E)s%(F)s$ luôn là một tam giác nhọn với mọi tam giác $%(A)s%(B)s%(C)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $%(A)s%(B)s, %(A)s%(C)s$ tiếp xúc với đường tròn $(I)$ lần lượt tại $%(F)s, %(E)s$ nên $I%(F)s \\perp %(A)s%(B)s$ và $I%(E)s \\perp %(A)s%(C)s$, suy ra $\\widehat{%(A)s%(F)sI} = \\widehat{%(A)s%(E)sI} = 90^\\circ$.\\\\
Trong tứ giác $%(A)s%(F)sI%(E)s$, tổng bốn góc bằng $360^\\circ$ nên:
$$\\widehat{%(E)sI%(F)s} = 360^\\circ - 90^\\circ - 90^\\circ - \\widehat{%(B)s%(A)s%(C)s} = 180^\\circ - \\widehat{%(B)s%(A)s%(C)s}.$$
Xét đường tròn $(I)$, góc nội tiếp $\\widehat{%(E)s%(D)s%(F)s}$ và góc ở tâm $\\widehat{%(E)sI%(F)s}$ cùng chắn cung nhỏ $%(E)s%(F)s$ nên:
$$\\widehat{%(E)s%(D)s%(F)s} = \\frac{1}{2}\\widehat{%(E)sI%(F)s} = \\frac{180^\\circ - \\widehat{%(B)s%(A)s%(C)s}}{2} = 90^\\circ - \\frac{\\widehat{%(B)s%(A)s%(C)s}}{2}.$$
\\item Chứng minh tương tự câu a), ta cũng có:
$$\\widehat{%(D)s%(E)s%(F)s} = 90^\\circ - \\frac{\\widehat{%(A)s%(B)s%(C)s}}{2} \\quad \\text{và} \\quad \\widehat{%(D)s%(F)s%(E)s} = 90^\\circ - \\frac{\\widehat{%(A)s%(C)s%(B)s}}{2}.$$
Vì ba góc $\\widehat{%(B)s%(A)s%(C)s}, \\widehat{%(A)s%(B)s%(C)s}, \\widehat{%(A)s%(C)s%(B)s}$ của tam giác $%(A)s%(B)s%(C)s$ đều lớn hơn $0^\\circ$ nên cả ba góc $\\widehat{%(E)s%(D)s%(F)s}, \\widehat{%(D)s%(E)s%(F)s}, \\widehat{%(D)s%(F)s%(E)s}$ đều nhỏ hơn $90^\\circ$.\\\\
Vậy tam giác $%(D)s%(E)s%(F)s$ luôn là một tam giác nhọn với mọi tam giác $%(A)s%(B)s%(C)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
