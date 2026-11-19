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

def bt_dang3_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'M'), ('D', 'E', 'F', 'K'), ('P', 'Q', 'R', 'N')]
        A, B, C, M = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (105:1.6);
\\coordinate (B) at (215:1.6);
\\coordinate (C) at (-35:1.6);
\\coordinate (M) at (-90:1.6);
\\coordinate (I) at (-0.18,-0.32);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(M) (B)--(M)--(C) (B)--(I)--(C);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (M) circle (1pt) node[below] {$%(M)s$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'M': M})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ nội tiếp đường tròn $(O)$. Tia phân giác của góc $\\widehat{%(B)s%(A)s%(C)s}$ cắt đường tròn $(O)$ tại điểm thứ hai là $%(M)s$ ($%(M)s \\neq %(A)s$). Gọi $I$ là tâm đường tròn nội tiếp tam giác $%(A)s%(B)s%(C)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $%(M)s%(B)s = %(M)s%(C)s = %(M)sI$.
\\item Suy ra điểm $%(M)s$ là tâm đường tròn ngoại tiếp tam giác $%(B)sI%(C)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'M': M, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $%(A)s%(M)s$ là tia phân giác của góc $\\widehat{%(B)s%(A)s%(C)s}$ nên $\\widehat{%(B)s%(A)s%(M)s} = \\widehat{%(C)s%(A)s%(M)s}$, suy ra hai cung nhỏ $%(B)s%(M)s$ và $%(C)s%(M)s$ của đường tròn $(O)$ bằng nhau, do đó $%(M)s%(B)s = %(M)s%(C)s$ (1).\\\\
Vì $I$ là tâm đường tròn nội tiếp tam giác $%(A)s%(B)s%(C)s$ nên $%(B)sI$ là tia phân giác của góc $\\widehat{%(A)s%(B)s%(C)s}$, suy ra $\\widehat{I%(B)s%(A)s} = \\widehat{I%(B)s%(C)s}$.\\\\
Xét đường tròn $(O)$, hai góc nội tiếp $\\widehat{%(M)s%(B)s%(C)s}$ và $\\widehat{%(M)s%(A)s%(C)s}$ cùng chắn cung nhỏ $%(M)s%(C)s$ nên $\\widehat{%(M)s%(B)s%(C)s} = \\widehat{%(M)s%(A)s%(C)s} = \\widehat{%(M)s%(A)s%(B)s}$.\\\\
Ta có: $\\widehat{%(M)s%(B)sI} = \\widehat{%(M)s%(B)s%(C)s} + \\widehat{I%(B)s%(C)s} = \\widehat{%(M)s%(A)s%(B)s} + \\widehat{I%(B)s%(A)s} = \\widehat{%(M)sI%(B)s}$ (góc ngoài của $\\Delta %(A)s%(B)sI$).\\\\
Do đó tam giác $%(M)s%(B)sI$ cân tại $%(M)s$, suy ra $%(M)s%(B)s = %(M)sI$ (2).\\\\
Từ (1) và (2) suy ra $%(M)s%(B)s = %(M)s%(C)s = %(M)sI$.
\\item Vì $%(M)s%(B)s = %(M)s%(C)s = %(M)sI$ nên điểm $%(M)s$ cách đều ba đỉnh $%(B)s, I, %(C)s$ của tam giác $%(B)sI%(C)s$. Vậy $%(M)s$ là tâm đường tròn ngoại tiếp tam giác $%(B)sI%(C)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'M': M})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
