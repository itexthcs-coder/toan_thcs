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


def bt_dang6_p3_b2_c5_ds8(self):
    # Dạng 6 (Vận dụng): Phân tích biểu đồ cột kép để tính tỉ lệ phần trăm chênh lệch tổng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        a1, a2, a3 = 12 * k, 18 * k, 20 * k
        b1, b2, b3 = 15 * k, 14 * k, 11 * k
        tong_a = a1 + a2 + a3
        tong_b = b1 + b2 + b3
        pct = 25
        kq_str = str(pct)
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.6) node[above] {Số giải};
        \\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[right] {Loại giải};
        \\draw[line width=1pt, fill=black!35] (0.6,0) rectangle (1.1,1.2) (2.2,0) rectangle (2.7,1.8) (3.8,0) rectangle (4.3,2.0);
        \\draw[line width=1pt, fill=white] (1.1,0) rectangle (1.6,1.5) (2.7,0) rectangle (3.2,1.4) (4.3,0) rectangle (4.8,1.1);
        \\node[above] at (0.85,1.2) {$%s$}; \\node[above] at (1.35,1.5) {$%s$};
        \\node[above] at (2.45,1.8) {$%s$}; \\node[above] at (2.95,1.4) {$%s$};
        \\node[above] at (4.05,2.0) {$%s$}; \\node[above] at (4.55,1.1) {$%s$};
        \\node[below] at (1.1,0) {Nhất}; \\node[below] at (2.7,0) {Nhì}; \\node[below] at (4.3,0) {Ba};
        \\draw[line width=1pt, fill=black!35] (5.2,1.8) rectangle (5.5,2.1); \\node[right] at (5.5,1.95) {Đội $A$};
        \\draw[line width=1pt, fill=white] (5.2,1.3) rectangle (5.5,1.6); \\node[right] at (5.5,1.45) {Đội $B$};
        \\end{tikzpicture}
        \\end{center}""" % (a1, b1, a2, b2, a3, b3))
        
        noidungcauhoi = ("""Biểu đồ cột kép dưới đây biểu diễn số lượng giải đạt được của hai đội tuyển $A$ và $B$ trong kì thi Học sinh giỏi cấp tỉnh:%sTổng số giải của đội $A$ nhiều hơn tổng số giải của đội $B$ bao nhiêu phần trăm?"""
                         % tikz_code)
        
        loigiai = ("""Quan sát biểu đồ cột kép, ta có:\\\\
        - Tổng số giải của đội $A$ là: $%s + %s + %s = %s$ (giải).\\\\
        - Tổng số giải của đội $B$ là: $%s + %s + %s = %s$ (giải).\\\\
        Tổng số giải của đội $A$ nhiều hơn tổng số giải của đội $B$ số phần trăm là:
        $$\\dfrac{%s - %s}{%s} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$"""
                   % (a1, a2, a3, tong_a, b1, b2, b3, tong_b, tong_a, tong_b, tong_b, tong_a - tong_b, tong_b, pct))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
