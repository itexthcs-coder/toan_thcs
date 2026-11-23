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


def bt_dang7_p1_b1_c4_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.randint(2, 4)
        b = random.randint(a + 2, 7)
        k1 = random.randint(2, 4)
        k2 = random.randint(2, 5)
        while k1 == k2:
            k2 = random.randint(2, 5)
        ma = a * k1
        mn = b * k1
        mb = a * k2
        mp = b * k2

        # Các đáp án trắc nghiệm
        du = ['$%s\\text{ cm}$' % (mp)]
        da = random.choice(du)
        s = ['$%s\\text{ cm}$' % (mp - mb),
             '$%s\\text{ cm}$' % (mp + 2),
             '$%s\\text{ cm}$' % (mn - ma + mb),
             '$%s\\text{ cm}$' % (mp + 4),
             '$%s\\text{ cm}$' % (mp - 2)]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho $\\Delta MNP$ có $AB // NP$ ($A \\in MN$, $B \\in MP$) như hình vẽ bên dưới. Biết $MA = %s\\text{ cm}$, $MN = %s\\text{ cm}$, $MB = %s\\text{ cm}$. Độ dài đoạn thẳng $MP$ bằng
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (M) at (1.5,3);
\\coordinate (N) at (0,0);
\\coordinate (P) at (4.5,0);
\\coordinate (A) at ($(M)!0.42!(N)$);
\\coordinate (B) at ($(M)!0.42!(P)$);
\\draw[line width=1pt] (M)--(N)--(P)--cycle (A)--(B);
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below left] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\end{tikzpicture}
\\end{center}'''
                         % (ma, mn, mb))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Xét $\\Delta MNP$ có $AB // NP$ ($A \\in MN$, $B \\in MP$), theo định lí Thalès trong tam giác ta có:\\\\
$\\dfrac{MA}{MN} = \\dfrac{MB}{MP}$.\\\\
Thay $MA = %s\\text{ cm}$, $MN = %s\\text{ cm}$, $MB = %s\\text{ cm}$ vào tỉ lệ thức trên, ta được:\\\\
$\\dfrac{%s}{%s} = \\dfrac{%s}{MP} \\Rightarrow MP = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\\
Vậy độ dài đoạn thẳng $MP$ bằng $%s\\text{ cm}$.'''
                   % (ma, mn, mb, ma, mn, mb, mn, mb, ma, mp, mp))

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
