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

def bt_dang4_p4_b3_c5_ds8(self):
    # Dạng 4: Chuyển đổi dữ liệu từ biểu đồ cột số lượng sang biểu đồ hình quạt tròn (Tính góc ở tâm)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Tổng 300 hoặc 400 HS
        tong, n1, n2, n3, n4 = random.choice([
            (300, 135, 90, 45, 30),
            (400, 180, 120, 60, 40),
            (300, 150, 75, 45, 30),
            (400, 160, 120, 80, 40)
        ])
        p1 = int(n1 * 100 // tong)
        p2 = int(n2 * 100 // tong)
        p3 = int(n3 * 100 // tong)
        p4 = int(n4 * 100 // tong)
        
        g1 = Decimal(p1) * Decimal('3.6')
        g2 = Decimal(p2) * Decimal('3.6')
        g3 = Decimal(p3) * Decimal('3.6')
        g4 = Decimal(p4) * Decimal('3.6')
        
        def fmt_vn(d):
            return str(d).rstrip('0').rstrip('.').replace('.', ',')
            
        hs = [round(v / (tong / 8.0), 2) for v in [n1, n2, n3, n4]]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (7.4,0) node[below] {Màu áo};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số học sinh};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!20] (0.5,0) rectangle (1.5,%s); \\node[above] at (1.0,%s) {$%s$}; \\node[below] at (1.0,0) {Xanh dương};\n' % (hs[0], hs[0], n1) +
            '\\draw[line width=1pt, fill=black!20] (2.2,0) rectangle (3.2,%s); \\node[above] at (2.7,%s) {$%s$}; \\node[below] at (2.7,0) {Trắng kem};\n' % (hs[1], hs[1], n2) +
            '\\draw[line width=1pt, fill=black!20] (3.9,0) rectangle (4.9,%s); \\node[above] at (4.4,%s) {$%s$}; \\node[below] at (4.4,0) {Đỏ đô};\n' % (hs[2], hs[2], n3) +
            '\\draw[line width=1pt, fill=black!20] (5.6,0) rectangle (6.6,%s); \\node[above] at (6.1,%s) {$%s$}; \\node[below] at (6.1,0) {Vàng nhạt};\n' % (hs[3], hs[3], n4) +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột dưới đây thống kê số lượng học sinh khối $8$ của một trường THCS tham gia bình chọn màu áo đồng phục kỉ niệm thành lập trường (mỗi học sinh chỉ được chọn đúng một màu áo):\n' +
                         tikz_code + '\n' +
                         'a) Lập bảng thống kê tỉ lệ phần trăm số học sinh bình chọn cho từng màu áo.\\\n' +
                         'b) Nếu biểu diễn bảng tỉ lệ phần trăm trên bằng biểu đồ hình quạt tròn, hãy tính số đo góc ở tâm của từng hình quạt tương ứng với bốn màu áo đó.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Tổng số học sinh tham gia bình chọn là: $%s + %s + %s + %s = %s$ (học sinh).\\\\' +
                   'Tỉ lệ phần trăm số học sinh bình chọn từng màu áo là:\\\\' +
                   '- Màu xanh dương: $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   '- Màu trắng kem: $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   '- Màu đỏ đô: $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   '- Màu vàng nhạt: $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.\\\\' +
                   'Bảng thống kê tỉ lệ phần trăm:\\\\' +
                   '\\begin{center}\n' +
                   '\\begin{tabular}{|l|c|c|c|c|}\n' +
                   '\\hline\n' +
                   '\\textbf{Màu áo} & Xanh dương & Trắng kem & Đỏ đô & Vàng nhạt \\\\ \\hline\n' +
                   '\\textbf{Tỉ lệ ($\\%%$)} & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\ \\hline\n' +
                   '\\end{tabular}\n' +
                   '\\end{center}\n' +
                   '\\item Số đo góc ở tâm của từng hình quạt trên biểu đồ hình quạt tròn là:\\\\' +
                   '- Màu xanh dương: $360^\\circ \\cdot %s\\%% = %s^\\circ$.\\\\' +
                   '- Màu trắng kem: $360^\\circ \\cdot %s\\%% = %s^\\circ$.\\\\' +
                   '- Màu đỏ đô: $360^\\circ \\cdot %s\\%% = %s^\\circ$.\\\\' +
                   '- Màu vàng nhạt: $360^\\circ \\cdot %s\\%% = %s^\\circ$.\n' +
                   '\\end{enumEX}'
                   ) % (n1, n2, n3, n4, tong,
                        n1, tong, p1, n2, tong, p2, n3, tong, p3, n4, tong, p4,
                        p1, p2, p3, p4,
                        p1, fmt_vn(g1), p2, fmt_vn(g2), p3, fmt_vn(g3), p4, fmt_vn(g4))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
