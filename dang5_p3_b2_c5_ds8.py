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


def bt_dang5_p3_b2_c5_ds8(self):
    # Dạng 5 (Vận dụng): Tính mức tăng trung bình hằng năm trên biểu đồ đoạn thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        y1 = random.choice([2200, 2450, 2600])
        inc_avg = random.choice([300, 350, 400])
        y5 = y1 + 4 * inc_avg
        y2 = y1 + inc_avg - 80
        y3 = y1 + 2 * inc_avg - 50
        y4 = y1 + 3 * inc_avg - 20
        kq_str = str(inc_avg)
        
        s1 = f"{y1:,}".replace(",", "\\,")
        s2 = f"{y2:,}".replace(",", "\\,")
        s3 = f"{y3:,}".replace(",", "\\,")
        s4 = f"{y4:,}".replace(",", "\\,")
        s5 = f"{y5:,}".replace(",", "\\,")
        s_diff = f"{(y5 - y1):,}".replace(",", "\\,")
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.8) node[above] {Số sách};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Năm};
        \\coordinate (A) at (0.8,0.5);
        \\coordinate (B) at (2.0,0.9);
        \\coordinate (C) at (3.2,1.4);
        \\coordinate (D) at (4.4,1.9);
        \\coordinate (E) at (5.6,2.4);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(E);
        \\fill (A) circle (1pt) node[above left] {$%s$};
        \\fill (B) circle (1pt) node[above left] {$%s$};
        \\fill (C) circle (1pt) node[above left] {$%s$};
        \\fill (D) circle (1pt) node[above left] {$%s$};
        \\fill (E) circle (1pt) node[above] {$%s$};
        \\node[below] at (0.8,0) {$2021$};
        \\node[below] at (2.0,0) {$2022$};
        \\node[below] at (3.2,0) {$2023$};
        \\node[below] at (4.4,0) {$2024$};
        \\node[below] at (5.6,0) {$2025$};
        \\end{tikzpicture}
        \\end{center}""" % (s1, s2, s3, s4, s5))
        
        noidungcauhoi = ("""Biểu đồ đoạn thẳng dưới đây ghi lại số lượng sách trong thư viện của một trường THCS qua các năm từ $2021$ đến $2025$:%sTrung bình mỗi năm từ năm $2021$ đến năm $2025$, thư viện có thêm bao nhiêu cuốn sách?"""
                         % tikz_code)
        
        loigiai = ("""Quan sát biểu đồ đoạn thẳng, số sách năm $2021$ là $%s$ cuốn và năm $2025$ là $%s$ cuốn.\\\\
        Tổng số sách tăng thêm sau $4$ năm (từ năm $2021$ đến năm $2025$) là:
        $$%s - %s = %s \\text{ (cuốn)}.$$
        Trung bình mỗi năm thư viện có thêm số cuốn sách là:
        $$\\dfrac{%s}{4} = %s \\text{ (cuốn)}.$$"""
                   % (s1, s5, s5, s1, s_diff, s_diff, inc_avg))

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
