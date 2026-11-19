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

def bt_dang6_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'D', 'E'), ('M', 'P', 'Q', 'H', 'K')]
        A, B, C, D, E = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (B) at (-1.5,0);
\\coordinate (C) at (1.5,0);
\\coordinate (A) at (120:1.5);
\\coordinate (D) at (-1.5,0.866);
\\coordinate (E) at (1.5,2.598);
\\draw[line width=1pt] (O) circle (1.5);
\\draw[line width=1pt] (B)--(C) (B)--(D) (C)--(E) (D)--(E);
\\draw[line width=1pt] (D)--(O)--(E) (O)--(A);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[left] {$%(D)s$};
\\fill (E) circle (1pt) node[right] {$%(E)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E})

        noidungcauhoi = ('''Cho đường tròn $(O)$ đường kính $%(B)s%(C)s = 2R$. Lấy điểm $%(A)s$ nằm trên đường tròn $(O)$ sao cho $%(A)s%(B)s < %(A)s%(C)s$. Tiếp tuyến của đường tròn $(O)$ tại $%(A)s$ cắt các tiếp tuyến tại $%(B)s$ và $%(C)s$ của $(O)$ lần lượt tại $%(D)s$ và $%(E)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng tam giác $%(D)sO%(E)s$ vuông tại $O$ và xác định bán kính đường tròn ngoại tiếp tam giác $%(D)sO%(E)s$ theo $%(D)s%(E)s$.
\\item Chứng minh rằng $%(B)s%(D)s \\cdot %(C)s%(E)s = R^2$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Theo tính chất hai tiếp tuyến cắt nhau của đường tròn $(O)$, ta có $O%(D)s$ là tia phân giác của góc $\\widehat{%(B)sO%(A)s}$ và $O%(E)s$ là tia phân giác của góc $\\widehat{%(A)sO%(C)s}$.\\\\
Vì hai góc $\\widehat{%(B)sO%(A)s}$ và $\\widehat{%(A)sO%(C)s}$ kề bù nên:
$$\\widehat{%(D)sO%(E)s} = \\frac{1}{2}(\\widehat{%(B)sO%(A)s} + \\widehat{%(A)sO%(C)s}) = \\frac{180^\\circ}{2} = 90^\\circ.$$
Vậy tam giác $%(D)sO%(E)s$ vuông tại $O$. Do đó đường tròn ngoại tiếp tam giác $%(D)sO%(E)s$ có tâm là trung điểm của cạnh huyền $%(D)s%(E)s$ và bán kính bằng $\\frac{%(D)s%(E)s}{2}$.
\\item Xét tam giác $%(D)sO%(E)s$ vuông tại $O$ có $O%(A)s \\perp %(D)s%(E)s$ (tính chất tiếp tuyến tại $%(A)s$).\\\\
Áp dụng hệ thức lượng trong tam giác vuông $%(D)sO%(E)s$ (hoặc $\\Delta %(D)sO%(A)s \\backsim \\Delta O%(E)s%(A)s$), ta có:
$$O%(A)s^2 = %(A)s%(D)s \\cdot %(A)s%(E)s.$$
Theo tính chất hai tiếp tuyến cắt nhau, ta có $%(A)s%(D)s = %(B)s%(D)s$ và $%(A)s%(E)s = %(C)s%(E)s$.\\\\
Lại có $O%(A)s = R$, do đó suy ra $%(B)s%(D)s \\cdot %(C)s%(E)s = R^2$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
