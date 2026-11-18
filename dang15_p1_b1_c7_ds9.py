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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang15_p1_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f1 = random.randint(4, 6)
        f2 = random.randint(8, 11)
        f3 = random.randint(11, 14)
        f4 = random.randint(6, 9)
        f5 = random.randint(2, 4)
        tong = f1 + f2 + f3 + f4 + f5
    
        y1 = round(f1 * 0.25, 2)
        y2 = round(f2 * 0.25, 2)
        y3 = round(f3 * 0.25, 2)
        y4 = round(f4 * 0.25, 2)
        y5 = round(f5 * 0.25, 2)
    
        du = ['$%s$ học sinh' % tong]
        da = random.choice(du)
        s = [
            '$%s$ học sinh' % (tong - f5),
            '$%s$ học sinh' % (tong + 2),
            '$%s$ học sinh' % (tong - 2),
            '$%s$ học sinh' % f3
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        noidungcauhoi = ('''Cho biểu đồ tần số dạng cột dưới đây biểu diễn số cuốn sách mà các bạn học sinh lớp $9C$ đã đọc trong tháng $10$:
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Số cuốn sách};
    \\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số học sinh};
    \\foreach \\y/\\lbl in {0.5/2, 1/4, 1.5/6, 2/8, 2.5/10, 3/12, 3.5/14}{
        \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
        \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
    }
    \\node[below left] at (0,0) {$0$};
    \\draw[line width=1pt] (0.7,0) rectangle (1.3,%s);
    \\node[above] at (1,%s) {$%s$};
    \\node[below] at (1,0) {$1$};
    \\draw[line width=1pt] (1.7,0) rectangle (2.3,%s);
    \\node[above] at (2,%s) {$%s$};
    \\node[below] at (2,0) {$2$};
    \\draw[line width=1pt] (2.7,0) rectangle (3.3,%s);
    \\node[above] at (3,%s) {$%s$};
    \\node[below] at (3,0) {$3$};
    \\draw[line width=1pt] (3.7,0) rectangle (4.3,%s);
    \\node[above] at (4,%s) {$%s$};
    \\node[below] at (4,0) {$4$};
    \\draw[line width=1pt] (4.7,0) rectangle (5.3,%s);
    \\node[above] at (5,%s) {$%s$};
    \\node[below] at (5,0) {$5$};
    \\end{tikzpicture}
    \\end{center}
    Dựa vào biểu đồ, tổng số học sinh của lớp $9C$ tham gia thống kê là bao nhiêu?'''
                         % (y1, y1, f1, y2, y2, f2, y3, y3, f3, y4, y4, f4, y5, y5, f5))
    
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        loigiai = ('''Từ biểu đồ tần số dạng cột, ta xác định được số học sinh đọc $1$, $2$, $3$, $4$, $5$ cuốn sách lần lượt là $%s$, $%s$, $%s$, $%s$, $%s$.\\\\
    Tổng số học sinh của lớp $9C$ tham gia thống kê là:\\\\
    $%s + %s + %s + %s + %s = %s$ (học sinh).'''
                   % (f1, f2, f3, f4, f5, f1, f2, f3, f4, f5, tong))
    
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
