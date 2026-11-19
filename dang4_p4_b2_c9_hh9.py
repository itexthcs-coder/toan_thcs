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

def bt_dang4_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C', 'H', 'M', 'D'), ('P', 'Q', 'R', 'K', 'N', 'E')]
        A, B, C, H, M, D = random.choice(bo_diem)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (105:1.6);
\\coordinate (B) at (215:1.6);
\\coordinate (C) at (-35:1.6);
\\coordinate (D) at (-75:1.6);
\\coordinate (H) at (-0.15,0.65);
\\coordinate (M) at (0,-0.918);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(D) (A)--(H) (O)--(M);
\\draw[line width=1pt, dashed] (B)--(H)--(D)--(C)--(H);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above] {$%(A)s$};
\\fill (B) circle (1pt) node[below left] {$%(B)s$};
\\fill (C) circle (1pt) node[below right] {$%(C)s$};
\\fill (D) circle (1pt) node[below] {$%(D)s$};
\\fill (H) circle (1pt) node[left] {$%(H)s$};
\\fill (M) circle (1pt) node[below] {$%(M)s$};
\\end{tikzpicture}
\\end{center}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'H': H, 'M': M})

        noidungcauhoi = ('''Cho tam giác nhọn $%(A)s%(B)s%(C)s$ nội tiếp đường tròn $(O)$. Gọi $%(H)s$ là trực tâm của tam giác $%(A)s%(B)s%(C)s$ và $%(M)s$ là trung điểm của cạnh $%(B)s%(C)s$. Kẻ đường kính $%(A)s%(D)s$ của đường tròn $(O)$.%(hv)s
\\begin{enumEX}[a)]{1}
\\item Chứng minh rằng ba điểm $%(H)s, %(M)s, %(D)s$ thẳng hàng.
\\item Chứng minh rằng $%(A)s%(H)s = 2O%(M)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'M': M, 'D': D, 'hv': hinh_ve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét đường tròn $(O)$ đường kính $%(A)s%(D)s$, ta có $\\widehat{%(A)s%(B)s%(D)s} = 90^\\circ$ và $\\widehat{%(A)s%(C)s%(D)s} = 90^\\circ$ (các góc nội tiếp chắn nửa đường tròn).\\\\
Suy ra $%(D)s%(B)s \\perp %(A)s%(B)s$ và $%(D)s%(C)s \\perp %(A)s%(C)s$.\\\\
Mặt khác, $%(H)s$ là trực tâm của tam giác $%(A)s%(B)s%(C)s$ nên $%(C)s%(H)s \\perp %(A)s%(B)s$ và $%(B)s%(H)s \\perp %(A)s%(C)s$.\\\\
Do đó $%(B)s%(H)s // %(D)s%(C)s$ và $%(C)s%(H)s // %(D)s%(B)s$, suy ra tứ giác $%(B)s%(H)s%(C)s%(D)s$ là hình bình hành.\\\\
Vì $%(M)s$ là trung điểm của đường chéo $%(B)s%(C)s$ nên $%(M)s$ cũng là trung điểm của đường chéo $%(H)s%(D)s$. Vậy ba điểm $%(H)s, %(M)s, %(D)s$ thẳng hàng.
\\item Xét tam giác $%(A)s%(H)s%(D)s$ có $O$ là trung điểm của $%(A)s%(D)s$ (tâm đường tròn đường kính $%(A)s%(D)s$) và $%(M)s$ là trung điểm của $%(H)s%(D)s$ (theo câu a).\\\\
Suy ra $O%(M)s$ là đường trung bình của tam giác $%(A)s%(H)s%(D)s$, do đó $O%(M)s = \\frac{1}{2}%(A)s%(H)s$ hay $%(A)s%(H)s = 2O%(M)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'H': H, 'M': M, 'D': D})

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
