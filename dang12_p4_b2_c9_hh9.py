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

def bt_dang12_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'E', 'F'), ('M', 'N', 'P', 'H', 'K')]
        A, B, C, E, F = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.4,0);
\\coordinate (I) at (1.56,0.92);
\\coordinate (E) at (2.43,1.27);
\\coordinate (F) at (0.76,1.27);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.92);
\\draw[line width=1pt] (B)--(E) (C)--(F);
\\fill (I) circle (1pt) node[below] {$I$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (E) circle (1pt) node[right] {$%(E)s$};
\\fill (F) circle (1pt) node[left] {$%(F)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'E': E, 'F': F})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ có $\\widehat{%(B)s%(A)s%(C)s} = 60^\\circ$ và $I$ là tâm đường tròn nội tiếp tam giác $%(A)s%(B)s%(C)s$. Các tia $%(B)sI, %(C)sI$ lần lượt cắt các cạnh $%(A)s%(C)s, %(A)s%(B)s$ tại $%(E)s$ và $%(F)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Tính số đo góc $\\widehat{%(B)sI%(C)s}$.
\\item Chứng minh rằng $I%(E)s = I%(F)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'E': E, 'F': F, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $%(A)s%(B)s%(C)s$ có tổng ba góc bằng $180^\\circ$ nên:
$$\\widehat{%(A)s%(B)s%(C)s} + \\widehat{%(A)s%(C)s%(B)s} = 180^\\circ - \\widehat{%(B)s%(A)s%(C)s} = 180^\\circ - 60^\\circ = 120^\\circ.$$
Vì $I$ là tâm đường tròn nội tiếp tam giác $%(A)s%(B)s%(C)s$ nên $%(B)sI, %(C)sI$ là các tia phân giác của $\\widehat{%(A)s%(B)s%(C)s}$ và $\\widehat{%(A)s%(C)s%(B)s}$.\\\\
Suy ra $\\widehat{I%(B)s%(C)s} + \\widehat{I%(C)s%(B)s} = \\frac{\\widehat{%(A)s%(B)s%(C)s} + \\widehat{%(A)s%(C)s%(B)s}}{2} = \\frac{120^\\circ}{2} = 60^\\circ$.\\\\
Xét tam giác $I%(B)s%(C)s$, ta có $\\widehat{%(B)sI%(C)s} = 180^\\circ - (\\widehat{I%(B)s%(C)s} + \\widehat{I%(C)s%(B)s}) = 180^\\circ - 60^\\circ = 120^\\circ$.
\\item Kẻ tia phân giác $ID$ của góc $\\widehat{%(B)sI%(C)s}$ ($D \\in %(B)s%(C)s$). Khi đó $\\widehat{%(B)sID} = \\widehat{%(C)sID} = \\frac{120^\\circ}{2} = 60^\\circ$.\\\\
Lại có $\\widehat{%(B)sI%(F)s} = \\widehat{%(C)sI%(E)s} = 180^\\circ - 120^\\circ = 60^\\circ$ (hai góc kề bù với $\\widehat{%(B)sI%(C)s}$).\\\\
Xét $\\Delta %(B)sI%(F)s$ và $\\Delta %(B)sID$ có $\\widehat{I%(B)s%(F)s} = \\widehat{I%(B)sD}$, $%(B)sI$ chung, $\\widehat{%(B)sI%(F)s} = \\widehat{%(B)sID} = 60^\\circ$ nên $\\Delta %(B)sI%(F)s = \\Delta %(B)sID$ (g.c.g), suy ra $I%(F)s = ID$.\\\\
Chứng minh tương tự, $\\Delta %(C)sI%(E)s = \\Delta %(C)sID$ (g.c.g), suy ra $I%(E)s = ID$.\\\\
Vậy $I%(E)s = I%(F)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'E': E, 'F': F})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
