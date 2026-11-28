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


def bt_dang16_p1_b1_c9_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        kieu = random.choice(['thang', 'dong_ho_cat'])
        if kieu == 'thang':
            tikz = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                '\\coordinate (A) at (1.8,3.2);\n'
                '\\coordinate (B) at (0,0);\n'
                '\\coordinate (C) at (4,0);\n'
                '\\coordinate (P) at ($(A)!0.32!(B)$);\n'
                '\\coordinate (Q) at ($(A)!0.32!(C)$);\n'
                '\\coordinate (M) at ($(A)!0.65!(B)$);\n'
                '\\coordinate (N) at ($(A)!0.65!(C)$);\n'
                '\\draw[line width=1pt] (A)--(B)--(C)--cycle (P)--(Q) (M)--(N);\n'
                '\\fill (A) circle (1pt) node[above] {$A$};\n'
                '\\fill (B) circle (1pt) node[below left] {$B$};\n'
                '\\fill (C) circle (1pt) node[below right] {$C$};\n'
                '\\fill (P) circle (1pt) node[left] {$P$};\n'
                '\\fill (Q) circle (1pt) node[right] {$Q$};\n'
                '\\fill (M) circle (1pt) node[left] {$M$};\n'
                '\\fill (N) circle (1pt) node[right] {$N$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
            )
            noidungcauhoi = ('Cho $\\Delta ABC$, lấy $M \\in AB, N \\in AC$ sao cho $MN // BC$; tiếp tục lấy $P \\in AM, Q \\in AN$ sao cho $PQ // MN$ ($P$ không trùng $A, M$) như hình vẽ. Trong hình vẽ có tất cả bao nhiêu cặp tam giác phân biệt đồng dạng với nhau?\n' + tikz)
            loigiai = ('Vì $MN // BC$ nên $\\Delta AMN \\backsim \\Delta ABC$.\\\\ '
                       'Vì $PQ // MN$ nên $\\Delta APQ \\backsim \\Delta AMN$.\\\\ '
                       'Theo tính chất bắc cầu, từ $\\Delta APQ \\backsim \\Delta AMN$ và $\\Delta AMN \\backsim \\Delta ABC$ suy ra $\\Delta APQ \\backsim \\Delta ABC$.\\\\ '
                       'Vậy có tất cả $3$ cặp tam giác phân biệt đồng dạng với nhau.')
        else:
            tikz = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                '\\coordinate (A) at (0,2.4);\n'
                '\\coordinate (B) at (0,0);\n'
                '\\coordinate (O) at (2.8,1.2);\n'
                '\\coordinate (C) at ($(A)!0.55!(O)$);\n'
                '\\coordinate (D) at ($(B)!0.55!(O)$);\n'
                '\\coordinate (F) at ($(O)!-0.5!(A)$);\n'
                '\\coordinate (E) at ($(O)!-0.5!(B)$);\n'
                '\\draw[line width=1pt] (A)--(B) (C)--(D) (E)--(F) (A)--(F) (B)--(E);\n'
                '\\fill (A) circle (1pt) node[above left] {$A$};\n'
                '\\fill (B) circle (1pt) node[below left] {$B$};\n'
                '\\fill (C) circle (1pt) node[above] {$C$};\n'
                '\\fill (D) circle (1pt) node[below] {$D$};\n'
                '\\fill (O) circle (1pt) node[below] {$O$};\n'
                '\\fill (E) circle (1pt) node[above right] {$E$};\n'
                '\\fill (F) circle (1pt) node[below right] {$F$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}\n'
            )
            noidungcauhoi = ('Trong hình vẽ dưới đây, các đường thẳng $AB, CD, EF$ đôi một song song với nhau. Có tất cả bao nhiêu cặp tam giác phân biệt đồng dạng với nhau trong hình?\n' + tikz)
            loigiai = ('Vì $CD // AB$ nên $\\Delta OCD \\backsim \\Delta OAB$.\\\\ '
                       'Vì $EF // CD$ nên $\\Delta OFE \\backsim \\Delta OCD$.\\\\ '
                       'Theo tính chất bắc cầu, suy ra $\\Delta OFE \\backsim \\Delta OAB$.\\\\ '
                       'Vậy có tất cả $3$ cặp tam giác phân biệt đồng dạng với nhau.')
        da = '$3$ cặp'
        s = ['$1$ cặp', '$2$ cặp', '$4$ cặp', '$6$ cặp']
        das1, das2, das3 = random.sample(s, 3)
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
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
