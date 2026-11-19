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

def bt_dang14_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'D', 'E', 'F', 'K'), ('M', 'N', 'P', 'H', 'Q', 'R', 'T')]
        A, B, C, D, E, F, K = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.8,0);
\\coordinate (I) at (1.53,0.88);
\\coordinate (D) at (1.53,0);
\\coordinate (E) at (2.37,1.33);
\\coordinate (F) at (0.74,1.54);
\\coordinate (K) at (1.96,0.68);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.88);
\\draw[line width=1pt] (A)--(K) (D)--(E) (I)--(C) (I)--(E);
\\fill (I) circle (1pt) node[left] {$I$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[below] {$%(D)s$};
\\fill (E) circle (1pt) node[above right] {$%(E)s$};
\\fill (K) circle (1pt) node[right] {$%(K)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'K': K})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ ($%(A)s%(B)s < %(A)s%(C)s$) ngoại tiếp đường tròn $(I)$. Gọi $%(D)s, %(E)s, %(F)s$ lần lượt là tiếp điểm của $(I)$ trên các cạnh $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$. Tia phân giác của góc $\\widehat{%(B)s%(A)s%(C)s}$ cắt đường thẳng $%(D)s%(E)s$ tại $%(K)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng bốn điểm $%(A)s, I, %(K)s, %(C)s$ cùng nằm trên một đường tròn.
\\item Chứng minh rằng $\\widehat{%(A)s%(K)s%(C)s} = 90^\\circ$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'K': K, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Theo tính chất hai tiếp tuyến cắt nhau của đường tròn $(I)$, ta có $%(C)s%(D)s = %(C)s%(E)s$ nên tam giác $%(C)s%(D)s%(E)s$ cân tại $%(C)s$, suy ra $\\widehat{%(C)s%(E)s%(D)s} = \\frac{180^\\circ - \\widehat{%(C)s}}{2} = 90^\\circ - \\frac{\\widehat{%(C)s}}{2}$.\\\\
Vì $I$ là tâm đường tròn nội tiếp tam giác $%(A)s%(B)s%(C)s$ nên $%(A)sI, %(C)sI$ là phân giác của $\\widehat{%(A)s}$ và $\\widehat{%(C)s}$.\\\\
Xét tam giác $%(A)sI%(C)s$, góc ngoài tại đỉnh $I$ là:
$$\\widehat{%(C)sI%(K)s} = \\widehat{I%(A)s%(C)s} + \\widehat{I%(C)s%(A)s} = \\frac{\\widehat{%(A)s} + \\widehat{%(C)s}}{2} = \\frac{180^\\circ - \\widehat{%(B)s}}{2} = 90^\\circ - \\frac{\\widehat{%(B)s}}{2}.$$
(Hoặc xét $\\widehat{%(B)sI%(C)s} = 90^\\circ + \\frac{\\widehat{%(A)s}}{2}$, suy ra góc kề bù $\\widehat{%(C)sI%(K)s} = 90^\\circ - \\frac{\\widehat{%(A)s}}{2}$; tương tự $\\widehat{%(A)sI%(K)s} = 90^\\circ - \\frac{\\widehat{%(C)s}}{2} = \\widehat{%(A)s%(C)s%(K)s}$).\\\\
Hai đỉnh $I$ và $%(C)s$ cùng nhìn đoạn thẳng $%(A)s%(K)s$ dưới hai góc bằng nhau ($\\widehat{%(A)sI%(K)s} = \\widehat{%(A)s%(C)s%(K)s}$) nên tứ giác $%(A)sI%(K)s%(C)s$ nội tiếp, tức là bốn điểm $%(A)s, I, %(K)s, %(C)s$ cùng nằm trên một đường tròn.
\\item Vì tứ giác $%(A)sI%(K)s%(C)s$ nội tiếp đường tròn nên tổng hai góc đối bằng $180^\\circ$:
$$\\widehat{%(A)s%(K)s%(C)s} + \\widehat{%(A)s%(E)sI} = 180^\\circ.$$
Mà $%(A)s%(C)s$ là tiếp tuyến của đường tròn $(I)$ tại $%(E)s$ nên $I%(E)s \\perp %(A)s%(C)s$, tức là $\\widehat{%(A)s%(E)sI} = 90^\\circ$.\\\\
Vậy $\\widehat{%(A)s%(K)s%(C)s} = 180^\\circ - 90^\\circ = 90^\\circ$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'K': K})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
