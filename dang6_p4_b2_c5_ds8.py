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


def bt_dang6_p4_b2_c5_ds8(self):
    # Dạng 6 (Tự luận - Vận dụng): Chuyển đổi từ biểu đồ hình quạt tròn sang bảng thống kê và biểu đồ cột
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong = random.choice([1200, 1600, 2000])
        v1 = tong * 45 // 100
        v2 = tong * 30 // 100
        v3 = tong * 15 // 100
        v4 = tong * 10 // 100
        
        tikz_q = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.5);
        \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (162:1.5) (0,0) -- (270:1.5) (0,0) -- (324:1.5);
        \\node at (81:0.9) {$45\\%$};
        \\node at (216:0.9) {$30\\%$};
        \\node at (297:0.95) {$15\\%$};
        \\node at (342:1.05) {$10\\%$};
        \\node[right] at (1.9, 0.8) {Sách giáo khoa: $45\\%$};
        \\node[right] at (1.9, 0.25) {Sách tham khảo: $30\\%$};
        \\node[right] at (1.9, -0.3) {Truyện thiếu nhi: $15\\%$};
        \\node[right] at (1.9, -0.85) {Sách kĩ năng sống: $10\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số sách (cuốn)};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Loại sách};
        \\draw[line width=1pt, fill=black!25] (0.5,0) rectangle (1.3,2.0); \\node[above] at (0.9,2.0) {$%s$}; \\node[below] at (0.9,0) {SGK};
        \\draw[line width=1pt, fill=black!25] (1.9,0) rectangle (2.7,1.4); \\node[above] at (2.3,1.4) {$%s$}; \\node[below] at (2.3,0) {STK};
        \\draw[line width=1pt, fill=black!25] (3.3,0) rectangle (4.1,0.8); \\node[above] at (3.7,0.8) {$%s$}; \\node[below] at (3.7,0) {Truyện};
        \\draw[line width=1pt, fill=black!25] (4.7,0) rectangle (5.5,0.5); \\node[above] at (5.1,0.5) {$%s$}; \\node[below] at (5.1,0) {Kĩ năng};
        \\end{tikzpicture}
        \\end{center}""" % (v1, v2, v3, v4))
        
        noidungcauhoi = ("""Biểu đồ hình quạt tròn dưới đây cho biết tỉ lệ các loại sách trong thư viện của một trường học:%sBiết tổng số sách trong thư viện là $%s$ cuốn.\\\\
        a) Lập bảng thống kê cho biết số lượng cụ thể của từng loại sách có trong thư viện.\\\\
        b) Vẽ biểu đồ cột biểu diễn bảng thống kê vừa lập được.""" % (tikz_q, tong))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Số lượng cụ thể của từng loại sách trong thư viện là:\\\\
        - Sách giáo khoa: $%s \\cdot 45\\%% = %s$ (cuốn).\\\\
        - Sách tham khảo: $%s \\cdot 30\\%% = %s$ (cuốn).\\\\
        - Truyện thiếu nhi: $%s \\cdot 15\\%% = %s$ (cuốn).\\\\
        - Sách kĩ năng sống: $%s \\cdot 10\\%% = %s$ (cuốn).\\\\
        Bảng thống kê số lượng các loại sách:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Loại sách} & Sách giáo khoa & Sách tham khảo & Truyện thiếu nhi & Sách kĩ năng sống \\\\
        \\hline
        \\textbf{Số lượng (cuốn)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        \\item Biểu đồ cột biểu diễn số lượng từng loại sách:%s
        \\end{enumEX}""" % (tong, v1, tong, v2, tong, v3, tong, v4, v1, v2, v3, v4, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
