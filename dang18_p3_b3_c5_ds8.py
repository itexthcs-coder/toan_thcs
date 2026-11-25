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

def bt_dang18_p3_b3_c5_ds8(self):
    # Dạng 18: Bài toán lập bảng thống kê từ biểu đồ cột và tìm tỉ số phần trăm đạt chuẩn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Tổng 200 HS
        n1, n2, n3, n4 = random.choice([
            (18, 42, 84, 56),
            (16, 44, 80, 60),
            (20, 50, 78, 52),
            (14, 36, 90, 60)
        ])
        tong = n1 + n2 + n3 + n4 # 200
        dat_kg = n3 + n4
        pct = int(dat_kg * 100 // tong)
        kq_str = str(pct)
        
        hs = [round(v / 25.0, 2) for v in [n1, n2, n3, n4]]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (7.6,0) node[below] {Mức điểm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số học sinh};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!20] (0.5,0) rectangle (1.5,%s); \\node[above] at (1.0,%s) {$%s$}; \\node[below] at (1.0,0) {$<5$};\n' % (hs[0], hs[0], n1) +
            '\\draw[line width=1pt, fill=black!20] (2.2,0) rectangle (3.2,%s); \\node[above] at (2.7,%s) {$%s$}; \\node[below] at (2.7,0) {$5-<6,5$};\n' % (hs[1], hs[1], n2) +
            '\\draw[line width=1pt, fill=black!20] (3.9,0) rectangle (4.9,%s); \\node[above] at (4.4,%s) {$%s$}; \\node[below] at (4.4,0) {$6,5-<8$};\n' % (hs[2], hs[2], n3) +
            '\\draw[line width=1pt, fill=black!20] (5.6,0) rectangle (6.6,%s); \\node[above] at (6.1,%s) {$%s$}; \\node[below] at (6.1,0) {$8-10$};\n' % (hs[3], hs[3], n4) +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột dưới đây thống kê kết quả kiểm tra môn Toán giữa học kì II của khối $8$ một trường THCS theo bốn mức điểm:\n' +
                         tikz_code + '\n' +
                         'Hỏi tỉ lệ học sinh đạt điểm khá và giỏi (từ $6,5$ điểm trở lên) chiếm bao nhiêu phần trăm tổng số học sinh toàn khối?')
        
        loigiai = ('Tổng số học sinh toàn khối $8$ tham gia kiểm tra là:\\\\' +
                   '$$%s + %s + %s + %s = %s \\text{ (học sinh)}.$$\\\\' +
                   'Số học sinh đạt từ $6,5$ điểm trở lên là: $%s + %s = %s$ (học sinh).\\\\' +
                   'Tỉ lệ phần trăm học sinh đạt điểm khá và giỏi là:\\\\' +
                   '$$\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$'
                   ) % (n1, n2, n3, n4, tong, n3, n4, dat_kg, dat_kg, tong, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
