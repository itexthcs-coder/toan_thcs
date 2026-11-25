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

def bt_dang4_p3_b3_c5_ds8(self):
    # Dạng 4: Tính độ giảm nhiệt độ trung bình mỗi giờ trên biểu đồ đoạn thẳng có mốc thời gian không đều
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t0 = Decimal('8.4')
        t1, t2, step_dec = random.choice([
            (Decimal('6.2'), Decimal('-3.8'), Decimal('-2.5')),
            (Decimal('5.8'), Decimal('-4.2'), Decimal('-2.5')),
            (Decimal('7.0'), Decimal('-3.4'), Decimal('-2.6')),
            (Decimal('6.4'), Decimal('-4.8'), Decimal('-2.8'))
        ])
        kq_str = str(step_dec).replace('.', ',')
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[below] {Giờ};\n' +
            '\\draw[line width=1pt, ->] (0,-1.5) -- (0,3.2) node[left] {Nhiệt độ ($^\\circ\\text{C}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (P0) at (1.0,2.5);\n' +
            '\\coordinate (P1) at (2.2,1.8);\n' +
            '\\coordinate (P2) at (4.6,-1.1);\n' +
            '\\draw[line width=1pt] (P0)--(P1)--(P2);\n' +
            '\\fill (P0) circle (1pt) node[above] {$%s$};\n' % fmt_vn(t0) +
            '\\fill (P1) circle (1pt) node[above right] {$%s$};\n' % fmt_vn(t1) +
            '\\fill (P2) circle (1pt) node[below] {$%s$};\n' % fmt_vn(t2) +
            '\\node[below] at (1.0,0) {$6\\text{h}00$};\n' +
            '\\node[below] at (2.2,0) {$7\\text{h}00$};\n' +
            '\\node[above] at (4.6,0) {$11\\text{h}00$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Trên biểu đồ đoạn thẳng theo dõi nhiệt độ trong một kho lạnh bảo quản vắc-xin: lúc $6\\text{h}00$ nhiệt độ là $%s^\\circ\\text{C}$; lúc $7\\text{h}00$ nhiệt độ là $%s^\\circ\\text{C}$; lúc $11\\text{h}00$ nhiệt độ là $%s^\\circ\\text{C}$:\n' % (fmt_vn(t0), fmt_vn(t1), fmt_vn(t2)) +
                         tikz_code + '\n' +
                         'Hỏi trong khoảng thời gian từ $7\\text{h}00$ đến $11\\text{h}00$, trung bình mỗi giờ nhiệt độ trong kho lạnh thay đổi bao nhiêu độ C? (Ghi dấu $-$ nếu nhiệt độ giảm).')
        
        diff_t = t2 - t1
        loigiai = ('Khoảng thời gian từ $7\\text{h}00$ đến $11\\text{h}00$ là: $11 - 7 = 4$ (giờ).\\\\' +
                   'Độ biến thiên nhiệt độ trong $4$ giờ này là: $%s - %s = %s$ ($^\\circ\\text{C}$).\\\\' +
                   'Trung bình mỗi giờ nhiệt độ trong kho lạnh thay đổi là:\\\\' +
                   '$$\\dfrac{%s}{4} = %s \\text{ (}^\\circ\\text{C/giờ)}.$$'
                   ) % (fmt_vn(t2), fmt_vn(t1), fmt_vn(diff_t), fmt_vn(diff_t), kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
