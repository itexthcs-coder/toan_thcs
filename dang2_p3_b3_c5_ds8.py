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

def bt_dang2_p3_b3_c5_ds8(self):
    # Dạng 2: Tìm tỉ lệ phần trăm tăng trưởng năng lượng tái tạo qua hai biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t20, t25, p20, p25 = random.choice([
            (40, 60, 10, 30),
            (50, 80, 10, 25),
            (40, 80, 15, 30),
            (50, 75, 12, 24)
        ])
        s20 = int(t20 * p20 // 100)
        s25 = int(t25 * p25 // 100)
        pct = int((s25 - s20) * 100 // s20)
        kq_str = str(pct)
        
        p_th20 = 100 - 25 - p20
        p_th25 = 100 - 20 - p25
        
        a1_20 = round(p_th20 * 3.6, 1)
        a2_20 = round((p_th20 + 25) * 3.6, 1)
        a1_25 = round(p_th25 * 3.6, 1)
        a2_25 = round((p_th25 + 20) * 3.6, 1)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.6) arc (0:%s:1.6) -- cycle;\n' % a1_20 +
            '\\draw[line width=1pt, fill=black!35] (0,0) -- (%s:1.6) arc (%s:%s:1.6) -- cycle;\n' % (a1_20, a1_20, a2_20) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (%s:1.6) arc (%s:360:1.6) -- cycle;\n' % (a2_20, a2_20) +
            '\\node at (%s:0.95) {$%s\\%%$};\n' % (round(a1_20/2, 1), p_th20) +
            '\\node at (%s:1.05) {$25\\%%$};\n' % (round((a1_20+a2_20)/2, 1)) +
            '\\node at (%s:1.15) {$%s\\%%$};\n' % (round((a2_20+360)/2, 1), p20) +
            '\\node[below] at (0,-1.8) {Năm $2020$ ($%s$ tỉ $\\text{kWh}$)};\n' % t20 +
            '\\begin{scope}[xshift=4.6cm]\n' +
            '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.6) arc (0:%s:1.6) -- cycle;\n' % a1_25 +
            '\\draw[line width=1pt, fill=black!35] (0,0) -- (%s:1.6) arc (%s:%s:1.6) -- cycle;\n' % (a1_25, a1_25, a2_25) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (%s:1.6) arc (%s:360:1.6) -- cycle;\n' % (a2_25, a2_25) +
            '\\node at (%s:0.95) {$%s\\%%$};\n' % (round(a1_25/2, 1), p_th25) +
            '\\node at (%s:1.05) {$20\\%%$};\n' % (round((a1_25+a2_25)/2, 1)) +
            '\\node at (%s:1.1) {$%s\\%%$};\n' % (round((a2_25+360)/2, 1), p25) +
            '\\node[below] at (0,-1.8) {Năm $2025$ ($%s$ tỉ $\\text{kWh}$)};\n' % t25 +
            '\\end{scope}\n' +
            '\\draw[line width=1pt, fill=black!15] (6.8,0.8) rectangle (7.2,1.1) node[right, yshift=-4pt] {Nhiệt điện};\n' +
            '\\draw[line width=1pt, fill=black!35] (6.8,0.0) rectangle (7.2,0.3) node[right, yshift=-4pt] {Thủy điện};\n' +
            '\\draw[line width=1pt, fill=white] (6.8,-0.8) rectangle (7.2,-0.5) node[right, yshift=-4pt] {Mặt trời và gió};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Hai biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu sản lượng điện phát ra của một tập đoàn năng lượng năm $2020$ (tổng sản lượng $%s$ tỉ $\\text{kWh}$) và năm $2025$ (tổng sản lượng $%s$ tỉ $\\text{kWh}$):\n' % (t20, t25) +
                         tikz_code + '\n' +
                         'Hỏi sản lượng điện mặt trời và điện gió năm $2025$ của tập đoàn đó tăng thêm bao nhiêu phần trăm so với năm $2020$?')
        
        loigiai = ('Sản lượng điện mặt trời và điện gió năm $2020$ là: $%s \\cdot %s\\%% = %s$ (tỉ $\\text{kWh}$).\\\\' +
                   'Sản lượng điện mặt trời và điện gió năm $2025$ là: $%s \\cdot %s\\%% = %s$ (tỉ $\\text{kWh}$).\\\\' +
                   'Tỉ lệ phần trăm tăng trưởng của sản lượng điện mặt trời và điện gió năm $2025$ so với năm $2020$ là:\\\\' +
                   '$$\\dfrac{%s - %s}{%s} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$'
                   ) % (t20, p20, s20, t25, p25, s25, s25, s20, s20, s25 - s20, s20, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
