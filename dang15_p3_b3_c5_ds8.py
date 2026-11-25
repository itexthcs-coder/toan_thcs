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

def bt_dang15_p3_b3_c5_ds8(self):
    # Dạng 15: Tính toán từ biểu đồ đoạn thẳng biểu diễn tốc độ gió theo mùa (Liên môn Địa lí)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # 3 tháng đạt ngưỡng >= 9,0 m/s, 3 tháng dưới 9,0 m/s -> trung bình 3 tháng đạt chuẩn < 10 (tối đa 4 ký tự)
        w1, w2, w3, tb_dec = random.choice([
            (Decimal('10.4'), Decimal('9.8'), Decimal('9.2'), Decimal('9.8')),
            (Decimal('10.2'), Decimal('9.6'), Decimal('9.0'), Decimal('9.6')),
            (Decimal('10.5'), Decimal('9.7'), Decimal('9.2'), Decimal('9.8')),
            (Decimal('10.1'), Decimal('9.5'), Decimal('9.2'), Decimal('9.6'))
        ])
        w4, w5, w6 = Decimal('8.2'), Decimal('7.4'), Decimal('7.8')
        kq_str = str(tb_dec).replace('.', ',')
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        vals = [w1, w2, w3, w4, w5, w6]
        vs = [fmt_vn(x) for x in vals]
        ys = [round(float(x) / 3.0, 2) for x in vals]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.8,0) node[below] {Tháng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.0) node[left] {Tốc độ gió ($\\text{m/s}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (P1) at (1.0,%s); \\coordinate (P2) at (2.0,%s); \\coordinate (P3) at (3.0,%s);\n' % (ys[0], ys[1], ys[2]) +
            '\\coordinate (P4) at (4.0,%s); \\coordinate (P5) at (5.0,%s); \\coordinate (P6) at (6.0,%s);\n' % (ys[3], ys[4], ys[5]) +
            '\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5)--(P6);\n' +
            '\\fill (P1) circle (1pt) node[above] {$%s$};\n' % vs[0] +
            '\\fill (P2) circle (1pt) node[above] {$%s$};\n' % vs[1] +
            '\\fill (P3) circle (1pt) node[above] {$%s$};\n' % vs[2] +
            '\\fill (P4) circle (1pt) node[above] {$%s$};\n' % vs[3] +
            '\\fill (P5) circle (1pt) node[below] {$%s$};\n' % vs[4] +
            '\\fill (P6) circle (1pt) node[above] {$%s$};\n' % vs[5] +
            '\\node[below] at (1.0,0) {$1$}; \\node[below] at (2.0,0) {$2$}; \\node[below] at (3.0,0) {$3$};\n' +
            '\\node[below] at (4.0,0) {$4$}; \\node[below] at (5.0,0) {$5$}; \\node[below] at (6.0,0) {$6$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây biểu diễn tốc độ gió trung bình tháng (đơn vị: $\\text{m/s}$) tại một trạm điện gió ven biển trong $6$ tháng đầu năm:\n' +
                         tikz_code + '\n' +
                         'Biết tua-bin điện gió chỉ phát điện hiệu quả khi tốc độ gió trung bình tháng đạt từ $9,0\\text{ m/s}$ trở lên. Tính tốc độ gió trung bình của các tháng đạt ngưỡng phát điện hiệu quả trong giai đoạn trên (đơn vị: $\\text{m/s}$).')
        
        tong_w = w1 + w2 + w3
        loigiai = ('Các tháng có tốc độ gió trung bình đạt từ $9,0\\text{ m/s}$ trở lên gồm: Tháng $1$ ($%s\\text{ m/s}$), Tháng $2$ ($%s\\text{ m/s}$) và Tháng $3$ ($%s\\text{ m/s}$).\\\\' +
                   'Tốc độ gió trung bình của $3$ tháng này là:\\\\' +
                   '$$\\dfrac{%s + %s + %s}{3} = \\dfrac{%s}{3} = %s \\text{ (m/s)}.$$'
                   ) % (vs[0], vs[1], vs[2], vs[0], vs[1], vs[2], fmt_vn(tong_w), kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
