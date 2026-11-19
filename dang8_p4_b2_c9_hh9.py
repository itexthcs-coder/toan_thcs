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

def bt_dang8_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'D', 'E', 'F'), ('M', 'N', 'P', 'H', 'K', 'Q')]
        A, B, C, D, E, F = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,2.2);
\\coordinate (C) at (3.2,0);
\\coordinate (I) at (0.76,0.76);
\\coordinate (D) at (1.28,1.32);
\\coordinate (E) at (0.76,0);
\\coordinate (F) at (0,0.76);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.76);
\\draw[line width=1pt, dashed] (I)--(E) (I)--(F);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (I) circle (1pt) node[above right] {$I$};
\\fill (A) circle (1pt) node[below left] {$%(A)s$};
\\fill (B) circle (1pt) node[above left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[above right] {$%(D)s$};
\\fill (E) circle (1pt) node[below] {$%(E)s$};
\\fill (F) circle (1pt) node[left] {$%(F)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ vuông tại $%(A)s$ ngoại tiếp đường tròn $(I; r)$. Gọi $%(D)s, %(E)s, %(F)s$ lần lượt là các tiếp điểm của $(I)$ trên các cạnh $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $r = \\frac{%(A)s%(B)s + %(A)s%(C)s - %(B)s%(C)s}{2}$.
\\item Chứng minh rằng diện tích tam giác $%(A)s%(B)s%(C)s$ bằng tích độ dài hai đoạn thẳng $%(B)s%(D)s \\cdot %(C)s%(D)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tứ giác $%(A)s%(F)sI%(E)s$ có $\\widehat{%(A)s} = \\widehat{%(A)s%(F)sI} = \\widehat{%(A)s%(E)sI} = 90^\\circ$ và $I%(F)s = I%(E)s = r$ nên $%(A)s%(F)sI%(E)s$ là hình vuông cạnh $r$, suy ra $%(A)s%(E)s = %(A)s%(F)s = r$.\\\\
Theo tính chất hai tiếp tuyến cắt nhau, ta có $%(B)s%(D)s = %(B)s%(F)s$ và $%(C)s%(D)s = %(C)s%(E)s$.\\\\
Do đó:
$$%(A)s%(B)s + %(A)s%(C)s - %(B)s%(C)s = (%(A)s%(F)s + %(B)s%(F)s) + (%(A)s%(E)s + %(C)s%(E)s) - (%(B)s%(D)s + %(C)s%(D)s) = %(A)s%(F)s + %(A)s%(E)s = 2r.$$
Suy ra $r = \\frac{%(A)s%(B)s + %(A)s%(C)s - %(B)s%(C)s}{2}$.
\\item Ta có $%(B)s%(D)s = %(B)s%(F)s = %(A)s%(B)s - r$ và $%(C)s%(D)s = %(C)s%(E)s = %(A)s%(C)s - r$.\\\\
Xét tích:
$$%(B)s%(D)s \\cdot %(C)s%(D)s = (%(A)s%(B)s - r)(%(A)s%(C)s - r) = %(A)s%(B)s \\cdot %(A)s%(C)s - r(%(A)s%(B)s + %(A)s%(C)s) + r^2.$$
Thay $r = \\frac{%(A)s%(B)s + %(A)s%(C)s - %(B)s%(C)s}{2}$ và sử dụng định lí Pythagore $%(B)s%(C)s^2 = %(A)s%(B)s^2 + %(A)s%(C)s^2$, ta biến đổi được:
$$%(B)s%(D)s \\cdot %(C)s%(D)s = \\frac{1}{2}%(A)s%(B)s \\cdot %(A)s%(C)s = S_{%(A)s%(B)s%(C)s}.$$
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
