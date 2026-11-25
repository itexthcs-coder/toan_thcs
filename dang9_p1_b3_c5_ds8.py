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

def bt_dang9_p1_b3_c5_ds8(self):
    # Dạng 9: Đọc dữ liệu so sánh trên biểu đồ cột kép
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        subjects = ['Toán', 'Ngữ văn', 'Tiếng Anh']
        idx_eq = random.randint(0, 2)
        val_eq = random.randint(14, 18)
        
        t1 = [0, 0, 0]
        t2 = [0, 0, 0]
        for i in range(3):
            if i == idx_eq:
                t1[i] = val_eq
                t2[i] = val_eq
            else:
                v1 = random.randint(8, 17)
                v2 = random.choice([x for x in range(8, 18) if x != v1])
                t1[i] = v1
                t2[i] = v2
                
        da = 'Môn %s' % subjects[idx_eq]
        s_pool = ['Môn %s' % subjects[i] for i in range(3) if i != idx_eq]
        s_pool.append('Không có môn nào')
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        # Tỉ lệ trục đứng 20 -> 4 cm (chia 5)
        y1 = [round(v / 5.0, 2) for v in t1]
        y2 = [round(v / 5.0, 2) for v in t2]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.8,0) node[below] {Môn học};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Số điểm tốt};\n' +
            '\\foreach \\y/\\lbl in {1/5, 2/10, 3/15, 4/20}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (6.2,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            # Toán
            '\\draw[line width=1pt, fill=black!15] (0.6,0) rectangle (1.2,%s);\n' % y1[0] +
            '\\node[above] at (0.9,%s) {$%s$};\n' % (y1[0], t1[0]) +
            '\\draw[line width=1pt, fill=black!45] (1.2,0) rectangle (1.8,%s);\n' % y2[0] +
            '\\node[above] at (1.5,%s) {$%s$};\n' % (y2[0], t2[0]) +
            '\\node[below] at (1.2,0) {Toán};\n' +
            # Ngữ văn
            '\\draw[line width=1pt, fill=black!15] (2.6,0) rectangle (3.2,%s);\n' % y1[1] +
            '\\node[above] at (2.9,%s) {$%s$};\n' % (y1[1], t1[1]) +
            '\\draw[line width=1pt, fill=black!45] (3.2,0) rectangle (3.8,%s);\n' % y2[1] +
            '\\node[above] at (3.5,%s) {$%s$};\n' % (y2[1], t2[1]) +
            '\\node[below] at (3.2,0) {Ngữ văn};\n' +
            # Tiếng Anh
            '\\draw[line width=1pt, fill=black!15] (4.6,0) rectangle (5.2,%s);\n' % y1[2] +
            '\\node[above] at (4.9,%s) {$%s$};\n' % (y1[2], t1[2]) +
            '\\draw[line width=1pt, fill=black!45] (5.2,0) rectangle (5.8,%s);\n' % y2[2] +
            '\\node[above] at (5.5,%s) {$%s$};\n' % (y2[2], t2[2]) +
            '\\node[below] at (5.2,0) {Tiếng Anh};\n' +
            # Chú thích
            '\\draw[line width=1pt, fill=black!15] (6.5,3.2) rectangle (6.9,3.5) node[right, yshift=-4pt] {Tổ $1$};\n' +
            '\\draw[line width=1pt, fill=black!45] (6.5,2.4) rectangle (6.9,2.7) node[right, yshift=-4pt] {Tổ $2$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây biểu diễn số điểm tốt (điểm $9$, điểm $10$) trong học kì I của Tổ $1$ và Tổ $2$:\n' +
                         tikz_code + '\n' +
                         'Môn học nào hai tổ đạt được số điểm tốt bằng nhau?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Quan sát biểu đồ cột kép, số điểm tốt của hai tổ ở từng môn là:\\\\' +
                   '- Môn Toán: Tổ $1$ đạt $%s$ điểm, Tổ $2$ đạt $%s$ điểm;\\\\' +
                   '- Môn Ngữ văn: Tổ $1$ đạt $%s$ điểm, Tổ $2$ đạt $%s$ điểm;\\\\' +
                   '- Môn Tiếng Anh: Tổ $1$ đạt $%s$ điểm, Tổ $2$ đạt $%s$ điểm.\\\\' +
                   'Hai cột của Tổ $1$ và Tổ $2$ bằng nhau tại %s (cùng đạt $%s$ điểm tốt).\\\\' +
                   'Vậy chọn phương án: %s.'
                   ) % (t1[0], t2[0], t1[1], t2[1], t1[2], t2[2], da.lower(), val_eq, da)

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
