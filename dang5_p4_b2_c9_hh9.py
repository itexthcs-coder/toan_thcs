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

def bt_dang5_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'H', 'M', 'N'), ('D', 'E', 'F', 'K', 'P', 'Q')]
        A, B, C, H, M, N = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,2.4);
\\coordinate (C) at (3.2,0);
\\coordinate (H) at (1.152,1.536);
\\coordinate (M) at (0,1.536);
\\coordinate (N) at (1.152,0);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(H) (M)--(H)--(N) (M)--(N);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[below left] {$%(A)s$};
\\fill (B) circle (1pt) node[above left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (H) circle (1pt) node[above right] {$%(H)s$};
\\fill (M) circle (1pt) node[left] {$%(M)s$};
\\fill (N) circle (1pt) node[below] {$%(N)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'M': M, 'N': N})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ vuông tại $%(A)s$ có đường cao $%(A)s%(H)s$ ($%(H)s \\in %(B)s%(C)s$). Gọi $%(M)s, %(N)s$ lần lượt là hình chiếu vuông góc của $%(H)s$ trên các cạnh $%(A)s%(B)s$ và $%(A)s%(C)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Xác định tâm và bán kính đường tròn ngoại tiếp tam giác $%(A)s%(M)s%(N)s$.
\\item Chứng minh rằng bốn điểm $%(B)s, %(M)s, %(N)s, %(C)s$ cùng nằm trên một đường tròn.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'M': M, 'N': N, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì tam giác $%(A)s%(M)s%(N)s$ vuông tại $%(A)s$ nên đường tròn ngoại tiếp tam giác $%(A)s%(M)s%(N)s$ có tâm là trung điểm của cạnh huyền $%(M)s%(N)s$ và bán kính bằng $\\frac{%(M)s%(N)s}{2}$.\\\\
Mặt khác, tứ giác $%(A)s%(M)s%(H)s%(N)s$ có $\\widehat{%(A)s} = \\widehat{%(A)s%(M)s%(H)s} = \\widehat{%(A)s%(N)s%(H)s} = 90^\\circ$ nên $%(A)s%(M)s%(H)s%(N)s$ là hình chữ nhật, suy ra $%(M)s%(N)s = %(A)s%(H)s$.\\\\
Vậy đường tròn ngoại tiếp tam giác $%(A)s%(M)s%(N)s$ có tâm là trung điểm của $%(M)s%(N)s$ (hoặc giao điểm của $%(M)s%(N)s$ và $%(A)s%(H)s$) và bán kính bằng $\\frac{%(M)s%(N)s}{2} = \\frac{%(A)s%(H)s}{2}$.
\\item Vì $%(A)s%(M)s%(H)s%(N)s$ là hình chữ nhật nên $\\widehat{%(A)s%(N)s%(M)s} = \\widehat{%(A)s%(H)s%(M)s}$.\\\\
Mà $\\widehat{%(A)s%(H)s%(M)s} = \\widehat{%(A)s%(B)s%(C)s}$ (cùng phụ với $\\widehat{%(B)s%(H)s%(M)s}$) nên $\\widehat{%(A)s%(N)s%(M)s} = \\widehat{%(A)s%(B)s%(C)s}$.\\\\
Xét $\\Delta %(A)s%(N)s%(M)s$ và $\\Delta %(A)s%(B)s%(C)s$ có $\\widehat{%(A)s}$ chung và $\\widehat{%(A)s%(N)s%(M)s} = \\widehat{%(A)s%(B)s%(C)s}$ nên $\\Delta %(A)s%(N)s%(M)s \\backsim \\Delta %(A)s%(B)s%(C)s$ (g.g), suy ra $\\widehat{%(A)s%(M)s%(N)s} = \\widehat{%(A)s%(C)s%(B)s}$.\\\\
Do đó $\\widehat{%(B)s%(M)s%(N)s} + \\widehat{%(B)s%(C)s%(A)s} = 180^\\circ - \\widehat{%(A)s%(M)s%(N)s} + \\widehat{%(A)s%(C)s%(B)s} = 180^\\circ$, suy ra tứ giác $%(B)s%(M)s%(N)s%(C)s$ nội tiếp. Vậy bốn điểm $%(B)s, %(M)s, %(N)s, %(C)s$ cùng nằm trên một đường tròn.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'M': M, 'N': N})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
