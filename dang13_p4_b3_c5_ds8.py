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

def bt_dang13_p4_b3_c5_ds8(self):
    # Dạng 13: Phân tích biểu đồ cột kép về kết quả học tập của học sinh khối 8
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        s_a, s_b, s_c, s_d = 40, 42, 38, 40
        g_a, t_a = 14, 18 # 32/40 = 80%
        g_b, t_b = 12, 21 # 33/42 = 78.57%
        g_c, t_c = 15, 16 # 31/38 = 81.58%
        g_d, t_d = 11, 19 # 30/40 = 75%
        
        tong_g = g_a + g_b + g_c + g_d # 52
        tong_t = t_a + t_b + t_c + t_d # 74
        thuong_g = 150000
        thuong_t = 100000
        tong_tien = tong_g * thuong_g + tong_t * thuong_t
        
        def fmt_int(n):
            return f"{n:,}".replace(",", "\\,")
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (7.8,0) node[below] {Lớp};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số học sinh};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.5,0) rectangle (1.1,2.3); \\node[above] at (0.8,2.3) {$14$};\n' +
            '\\draw[line width=1pt, fill=black!45] (1.1,0) rectangle (1.7,3.0); \\node[above] at (1.4,3.0) {$18$};\n' +
            '\\node[below] at (1.1,0) {$8\\text{A}$};\n' +
            '\\draw[line width=1pt, fill=black!15] (2.3,0) rectangle (2.9,2.0); \\node[above] at (2.6,2.0) {$12$};\n' +
            '\\draw[line width=1pt, fill=black!45] (2.9,0) rectangle (3.5,3.5); \\node[above] at (3.2,3.5) {$21$};\n' +
            '\\node[below] at (2.9,0) {$8\\text{B}$};\n' +
            '\\draw[line width=1pt, fill=black!15] (4.1,0) rectangle (4.7,2.5); \\node[above] at (4.4,2.5) {$15$};\n' +
            '\\draw[line width=1pt, fill=black!45] (4.7,0) rectangle (5.3,2.7); \\node[above] at (5.0,2.7) {$16$};\n' +
            '\\node[below] at (4.7,0) {$8\\text{C}$};\n' +
            '\\draw[line width=1pt, fill=black!15] (5.9,0) rectangle (6.5,1.8); \\node[above] at (6.2,1.8) {$11$};\n' +
            '\\draw[line width=1pt, fill=black!45] (6.5,0) rectangle (7.1,3.2); \\node[above] at (6.8,3.2) {$19$};\n' +
            '\\node[below] at (6.5,0) {$8\\text{D}$};\n' +
            '\\draw[line width=1pt, fill=black!15] (7.6,3.2) rectangle (8.0,3.5) node[right, yshift=-4pt] {HS Giỏi};\n' +
            '\\draw[line width=1pt, fill=black!45] (7.6,2.4) rectangle (8.0,2.7) node[right, yshift=-4pt] {HS Tiên tiến};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây biểu diễn số học sinh đạt danh hiệu Học sinh Giỏi và Học sinh Tiên tiến của bốn lớp khối $8$ (sĩ số các lớp lần lượt là $8\\text{A}: 40$ em; $8\\text{B}: 42$ em; $8\\text{C}: 38$ em; $8\\text{D}: 40$ em):\n' +
                         tikz_code + '\n' +
                         'a) Tính tỉ lệ phần trăm học sinh đạt danh hiệu (bao gồm cả Giỏi và Tiên tiến) trên tổng sĩ số của từng lớp (làm tròn đến chữ số thập phân thứ hai). Lớp nào có tỉ lệ học sinh đạt danh hiệu cao nhất?\\\n' +
                         'b) Nhà trường dự định khen thưởng $150\\,000$ đồng cho mỗi Học sinh Giỏi và $100\\,000$ đồng cho mỗi Học sinh Tiên tiến. Tính tổng kinh phí khen thưởng dành cho cả khối $8$.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Tỉ lệ phần trăm học sinh đạt danh hiệu của từng lớp là:\\\\' +
                   '- Lớp $8\\text{A}$: $\\dfrac{14 + 18}{40} \\cdot 100\\%% = \\dfrac{32}{40} \\cdot 100\\%% = 80\\%%$.\\\\' +
                   '- Lớp $8\\text{B}$: $\\dfrac{12 + 21}{42} \\cdot 100\\%% = \\dfrac{33}{42} \\cdot 100\\%% \\approx 78,57\\%%$.\\\\' +
                   '- Lớp $8\\text{C}$: $\\dfrac{15 + 16}{38} \\cdot 100\\%% = \\dfrac{31}{38} \\cdot 100\\%% \\approx 81,58\\%%$.\\\\' +
                   '- Lớp $8\\text{D}$: $\\dfrac{11 + 19}{40} \\cdot 100\\%% = \\dfrac{30}{40} \\cdot 100\\%% = 75\\%%$.\\\\' +
                   'Vậy lớp $8\\text{C}$ có tỉ lệ học sinh đạt danh hiệu cao nhất ($81,58\\%%$).\n' +
                   '\\item Tổng số Học sinh Giỏi toàn khối là: $14 + 12 + 15 + 11 = %s$ (học sinh).\\\\' +
                   'Tổng số Học sinh Tiên tiến toàn khối là: $18 + 21 + 16 + 19 = %s$ (học sinh).\\\\' +
                   'Tổng kinh phí khen thưởng dành cho cả khối $8$ là:\\\\' +
                   '$$%s \\cdot 150\\,000 + %s \\cdot 100\\,000 = 7\\,800\\,000 + 7\\,400\\,000 = %s \\text{ (đồng)}.$$\n' +
                   '\\end{enumEX}'
                   ) % (tong_g, tong_t, tong_g, tong_t, fmt_int(tong_tien))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
