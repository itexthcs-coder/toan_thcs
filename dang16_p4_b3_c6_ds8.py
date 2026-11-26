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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D
def bt_dang16_p4_b3_c6_ds8(self):
    # Dạng 16: Bài toán chuyển động đường bộ gồm ba giai đoạn (có vẽ hình minh họa sơ đồ hành trình)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_chuan = [
            (30, 120, 35, 20, 45, '2,5', '\\dfrac{2}{3} + \\dfrac{3}{2} + \\dfrac{1}{3}'),
            (36, 140, 34, 24, 36, '3,4', '1 + 2 + 0,4'),
            (45, 160, 35, 30, 45, '3,5', '1 + 2 + 0,5')
        ]
        s1, s2, dv, nghi_phut, x_val, kq_str, phep_tinh = random.choice(bo_chuan)
        g_nghi = math.gcd(nghi_phut, 60)
        nghi_tu = nghi_phut // g_nghi
        nghi_mau = 60 // g_nghi
        
        tikz_hinh = ('\\begin{center}\n'
                     '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                     '\\coordinate (A) at (0,0);\n'
                     '\\coordinate (M) at (2.8,0);\n'
                     '\\coordinate (B) at (7.5,0);\n'
                     '\\draw[line width=1pt] (A)--(M)--(B);\n'
                     '\\fill (A) circle (1pt) node[below] {$A$};\n'
                     '\\fill (M) circle (1pt) node[below] {$M$ (Nghỉ $%s$ phút)};\n'
                     '\\fill (B) circle (1pt) node[below] {$B$};\n'
                     '\\node[above] at (1.4,0.1) {$%s\\text{ km}$, $v = x$};\n'
                     '\\node[above] at (5.15,0.1) {$%s\\text{ km}$, $v = x + %s$};\n'
                     '\\end{tikzpicture}\n'
                     '\\end{center}' % (nghi_phut, s1, s2, dv))
        
        noidungcauhoi = ('Một xe khách đi từ thành phố $A$ đến thành phố $B$. Chặng đầu dài $%s\\text{ km}$, xe chạy trong nội thành với vận tốc $x\\text{ (km/h)}$ ($x > 0$). Chặng thứ hai dài $%s\\text{ km}$ trên đường cao tốc, xe tăng vận tốc thêm $%s\\text{ km/h}$. Giữa hai chặng xe dừng nghỉ $%s$ phút (minh họa như hình vẽ).\\'
                         '%s\\'
                         'a) Viết các phân thức biểu thị thời gian xe chạy trên chặng đầu và thời gian xe chạy trên đường cao tốc.\\'
                         'b) Viết biểu thức biểu thị tổng thời gian xe đi từ thành phố $A$ đến thành phố $B$ (kể cả thời gian nghỉ) và tính tổng thời gian đó khi $x = %s\\text{ km/h}$.'
                         % (s1, s2, dv, nghi_phut, tikz_hinh, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Thời gian xe chạy trên chặng đầu là $\\dfrac{%s}{x}$ (giờ).\\'
                   'Vận tốc xe chạy trên đường cao tốc là $x + %s\\text{ (km/h)}$, nên thời gian xe chạy trên đường cao tốc là $\\dfrac{%s}{x + %s}$ (giờ).\n'
                   '\\item Đổi $%s$ phút $= \\dfrac{%s}{%s}$ giờ.\\'
                   'Biểu thức biểu thị tổng thời gian xe đi từ thành phố $A$ đến thành phố $B$ (kể cả thời gian nghỉ) là:\\'
                   '$$T = \\dfrac{%s}{x} + \\dfrac{%s}{x + %s} + \\dfrac{%s}{%s}\\text{ (giờ)}.$$\\'
                   'Khi $x = %s\\text{ km/h}$, tổng thời gian xe đi là:\\'
                   '$$T = \\dfrac{%s}{%s} + \\dfrac{%s}{%s + %s} + \\dfrac{%s}{%s} = %s = %s\\text{ (giờ)}.$$\n'
                   '\\end{enumEX} \n'
                   % (s1, dv, s2, dv, nghi_phut, nghi_tu, nghi_mau, s1, s2, dv, nghi_tu, nghi_mau,
                      x_val, s1, x_val, s2, x_val, dv, nghi_tu, nghi_mau, phep_tinh, kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
