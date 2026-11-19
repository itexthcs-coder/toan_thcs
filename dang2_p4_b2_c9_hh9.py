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

def bt_dang2_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'D', 'M'), ('P', 'Q', 'R', 'E', 'K'), ('X', 'Y', 'Z', 'H', 'N')]
        A, B, C, D, M = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (115:1.6);
\\coordinate (B) at (210:1.6);
\\coordinate (C) at (-30:1.6);
\\coordinate (M) at (-90:1.6);
\\coordinate (D) at (-0.28,-0.8);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(M) (B)--(M) (O)--(M);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (M) circle (1pt) node[below] {$%(M)s$};
\\fill (D) circle (1pt) node[above left] {$%(D)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'M': M, 'D': D})

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ nhọn nội tiếp đường tròn $(O)$. Tia phân giác của góc $\\widehat{%(B)s%(A)s%(C)s}$ cắt cạnh $%(B)s%(C)s$ tại $%(D)s$ và cắt đường tròn $(O)$ tại điểm thứ hai là $%(M)s$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng $O%(M)s \\perp %(B)s%(C)s$.
\\item Chứng minh rằng $%(M)s%(B)s^2 = %(M)s%(D)s \\cdot %(M)s%(A)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'M': M, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $%(A)s%(M)s$ là tia phân giác của góc $\\widehat{%(B)s%(A)s%(C)s}$ nên $\\widehat{%(B)s%(A)s%(M)s} = \\widehat{%(C)s%(A)s%(M)s}$.\\\\
Trong đường tròn $(O)$, hai góc nội tiếp bằng nhau $\\widehat{%(B)s%(A)s%(M)s}$ và $\\widehat{%(C)s%(A)s%(M)s}$ chắn hai cung nhỏ $%(B)s%(M)s$ và $%(C)s%(M)s$ nên hai cung này bằng nhau, suy ra dây $%(M)s%(B)s = %(M)s%(C)s$.\\\\
Lại có $O%(B)s = O%(C)s = R$ nên hai điểm $O$ và $%(M)s$ cùng cách đều hai đầu mút của đoạn thẳng $%(B)s%(C)s$.\\\\
Do đó $O%(M)s$ là đường trung trực của đoạn thẳng $%(B)s%(C)s$, hay $O%(M)s \\perp %(B)s%(C)s$.
\\item Xét đường tròn $(O)$, hai góc nội tiếp $\\widehat{%(M)s%(B)s%(C)s}$ và $\\widehat{%(M)s%(A)s%(C)s}$ cùng chắn cung nhỏ $%(M)s%(C)s$ nên $\\widehat{%(M)s%(B)s%(C)s} = \\widehat{%(M)s%(A)s%(C)s}$. Mà $\\widehat{%(M)s%(A)s%(C)s} = \\widehat{%(B)s%(A)s%(M)s}$ nên $\\widehat{%(M)s%(B)s%(D)s} = \\widehat{%(M)s%(A)s%(B)s}$.\\\\
Xét $\\Delta %(M)s%(B)s%(D)s$ và $\\Delta %(M)s%(A)s%(B)s$ có $\\widehat{%(B)s%(M)s%(D)s}$ chung và $\\widehat{%(M)s%(B)s%(D)s} = \\widehat{%(M)s%(A)s%(B)s}$.\\\\
Suy ra $\\Delta %(M)s%(B)s%(D)s \\backsim \\Delta %(M)s%(A)s%(B)s$ (g.g), do đó $\\frac{%(M)s%(B)s}{%(M)s%(A)s} = \\frac{%(M)s%(D)s}{%(M)s%(B)s} \\Rightarrow %(M)s%(B)s^2 = %(M)s%(D)s \\cdot %(M)s%(A)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'M': M})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
