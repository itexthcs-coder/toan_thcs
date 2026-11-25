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


def bt_dang7_p1_b2_c5_ds8(self):
    # Dạng 7 (Nhận biết): Đọc điểm nút và mức giảm mạnh nhất trên biểu đồ đoạn thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        t2 = random.randint(27, 29)
        t3 = t2 + random.randint(1, 2)
        t4 = t3 + random.randint(2, 3)
        drop_max = random.randint(3, 4)
        t5 = t4 - drop_max
        t6 = t5 - 1
        
        y2 = (t2 - 25) * 0.25
        y3 = (t3 - 25) * 0.25
        y4 = (t4 - 25) * 0.25
        y5 = (t5 - 25) * 0.25
        y6 = (t6 - 25) * 0.25
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,3.0) node[above] {Nhiệt độ ($^\\circ$C)};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Ngày};
        \\draw[line width=1pt, dashed] (0,1.25) -- (5.8,1.25);
        \\draw[line width=1pt, dashed] (0,2.5) -- (5.8,2.5);
        \\node[left] at (0,0) {$25$};
        \\node[left] at (0,1.25) {$30$};
        \\node[left] at (0,2.5) {$35$};
        \\coordinate (A) at (0.8,%.2f);
        \\coordinate (B) at (2.0,%.2f);
        \\coordinate (C) at (3.2,%.2f);
        \\coordinate (D) at (4.4,%.2f);
        \\coordinate (E) at (5.6,%.2f);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(E);
        \\fill (A) circle (1pt) node[above] {$%s$};
        \\fill (B) circle (1pt) node[above] {$%s$};
        \\fill (C) circle (1pt) node[above] {$%s$};
        \\fill (D) circle (1pt) node[above right] {$%s$};
        \\fill (E) circle (1pt) node[right] {$%s$};
        \\node[below] at (0.8,0) {Thứ 2};
        \\node[below] at (2.0,0) {Thứ 3};
        \\node[below] at (3.2,0) {Thứ 4};
        \\node[below] at (4.4,0) {Thứ 5};
        \\node[below] at (5.6,0) {Thứ 6};
        \\end{tikzpicture}
        \\end{center}""" % (y2, y3, y4, y5, y6, t2, t3, t4, t5, t6))
        
        du = ['Từ Thứ Tư sang Thứ Năm']
        da = random.choice(du)
        s = [
            'Từ Thứ Năm sang Thứ Sáu',
            'Từ Thứ Hai sang Thứ Ba',
            'Từ Thứ Ba sang Thứ Tư'
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Biểu đồ đoạn thẳng dưới đây ghi lại nhiệt độ lúc $12$ giờ trưa các ngày từ Thứ Hai đến Thứ Sáu trong tuần:%sNhiệt độ lúc $12$ giờ trưa giảm mạnh nhất vào khoảng thời gian nào?""" % tikz_code)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Quan sát biểu đồ đoạn thẳng, ta thấy:\\\\
    - Từ Thứ Hai sang Thứ Ba: nhiệt độ tăng từ $%s^\\circ\\text{C}$ lên $%s^\\circ\\text{C}$ (tăng $%s^\\circ\\text{C}$).\\\\
    - Từ Thứ Ba sang Thứ Tư: nhiệt độ tăng từ $%s^\\circ\\text{C}$ lên $%s^\\circ\\text{C}$ (tăng $%s^\\circ\\text{C}$).\\\\
    - Từ Thứ Tư sang Thứ Năm: nhiệt độ giảm từ $%s^\\circ\\text{C}$ xuống $%s^\\circ\\text{C}$ (giảm $%s^\\circ\\text{C}$).\\\\
    - Từ Thứ Năm sang Thứ Sáu: nhiệt độ giảm từ $%s^\\circ\\text{C}$ xuống $%s^\\circ\\text{C}$ (giảm $1^\\circ\\text{C}$).\\\\
    Vậy nhiệt độ lúc $12$ giờ trưa giảm mạnh nhất từ Thứ Tư sang Thứ Năm (giảm $%s^\\circ\\text{C}$)."""
                   % (t2, t3, t3 - t2, t3, t4, t4 - t3, t4, t5, drop_max, t5, t6, drop_max))

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
