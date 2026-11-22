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


def bt_dang17_p1_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        goc_A = random.choice([50, 60, 70, 80])
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
            ('M', 'N', 'P', 'Q', 'I', 'J', 'K', 'L')
        ])
        A, B, C, D, E, F, G, H = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,1.6);
\\coordinate (B) at (-2.4,0);
\\coordinate (C) at (0,-1.6);
\\coordinate (D) at (2.4,0);
\\coordinate (E) at (-1.2,0.8);
\\coordinate (F) at (-1.2,-0.8);
\\coordinate (G) at (1.2,-0.8);
\\coordinate (H) at (1.2,0.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (E)--(F)--(G)--(H)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (C) circle (1pt) node[below] {$%s$};
\\fill (D) circle (1pt) node[right] {$%s$};
\\fill (E) circle (1pt) node[above left] {$%s$};
\\fill (F) circle (1pt) node[below left] {$%s$};
\\fill (G) circle (1pt) node[below right] {$%s$};
\\fill (H) circle (1pt) node[above right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, E, F, G, H))

        # Các đáp án trắc nghiệm
        du = ['Hình chữ nhật']
        da = random.choice(du)
        s = [
            'Hình thoi',
            'Hình vuông',
            'Hình thang cân',
            'Hình bình hành có hai đường chéo vuông góc'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình thoi $%s%s%s%s$ có $\\widehat{%s} = %s^\\circ$. Gọi $%s, %s, %s, %s$ lần lượt là trung điểm của các cạnh $%s%s, %s%s, %s%s, %s%s$. Tứ giác $%s%s%s%s$ là hình gì?%s'''
                         % (A, B, C, D, A, goc_A, E, F, G, H, A, B, B, C, C, D, D, A, E, F, G, H, hinh_ve))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Tương tự tính chất đường trung bình của tam giác:\\\\
Ta có $%s%s // %s%s$ và $%s%s = \\dfrac{1}{2}%s%s$; $%s%s // %s%s$ và $%s%s = \\dfrac{1}{2}%s%s$.\\\\
Suy ra $%s%s // %s%s$ và $%s%s = %s%s$, do đó $%s%s%s%s$ là hình bình hành.\\\\
Mặt khác $%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s // %s%s$.\\\\
Vì $%s%s%s%s$ là hình thoi nên hai đường chéo $%s%s \\perp %s%s$.\\\\
Từ $%s%s // %s%s$, $%s%s // %s%s$ và $%s%s \\perp %s%s$ suy ra $%s%s \\perp %s%s$, tức là $\\widehat{%s%s%s} = 90^\\circ$.\\\\
Hình bình hành $%s%s%s%s$ có một góc vuông nên là hình chữ nhật.'''
                   % (E, F, A, C, E, F, A, C, G, H, A, C, G, H, A, C,
                      E, F, G, H, E, F, G, H, E, F, G, H,
                      F, G, B, C, D, F, G, B, D,
                      A, B, C, D, A, C, B, D,
                      E, F, A, C, F, G, B, D, A, C, B, D, E, F, F, G, E, F, G,
                      E, F, G, H))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
