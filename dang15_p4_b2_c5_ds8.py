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


def bt_dang15_p4_b2_c5_ds8(self):
    # Dạng 15 (Tự luận - Vận dụng): Đọc biểu đồ đoạn thẳng và tính tốc độ tăng trưởng kinh tế
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        def fmt_vn(val):
            s = f"{val:.1f}".replace(".", ",")
            return s[:-2] if s.endswith(",0") else s
            
        k = Decimal(str(random.choice([1, 2])))
        y21 = Decimal('40') * k
        y22 = Decimal('48') * k
        y23 = Decimal('45.6') * k
        y24 = Decimal('57') * k
        y25 = Decimal('68.4') * k
        tb_inc = (y25 - y21) / Decimal('4')
        
        tikz_q = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.6) node[above] {Doanh thu (tỉ đồng)};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Năm};
        \\coordinate (A) at (0.8,0.6);
        \\coordinate (B) at (2.0,1.1);
        \\coordinate (C) at (3.2,0.95);
        \\coordinate (D) at (4.4,1.65);
        \\coordinate (E) at (5.6,2.3);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(E);
        \\fill (A) circle (1pt) node[above left] {$%s$};
        \\fill (B) circle (1pt) node[above] {$%s$};
        \\fill (C) circle (1pt) node[below] {$%s$};
        \\fill (D) circle (1pt) node[above left] {$%s$};
        \\fill (E) circle (1pt) node[above] {$%s$};
        \\node[below] at (0.8,0) {$2021$};
        \\node[below] at (2.0,0) {$2022$};
        \\node[below] at (3.2,0) {$2023$};
        \\node[below] at (4.4,0) {$2024$};
        \\node[below] at (5.6,0) {$2025$};
        \\end{tikzpicture}
        \\end{center}""" % (fmt_vn(y21), fmt_vn(y22), fmt_vn(y23), fmt_vn(y24), fmt_vn(y25)))
        
        noidungcauhoi = ("""Biểu đồ đoạn thẳng dưới đây cho biết doanh thu xuất khẩu thủy sản của một doanh nghiệp qua các năm từ $2021$ đến $2025$:%sa) Lập bảng thống kê doanh thu xuất khẩu thủy sản của doanh nghiệp từ năm $2021$ đến năm $2025$.\\\\
        b) Tính tỉ lệ phần trăm tăng trưởng doanh thu của năm $2022$ so với năm $2021$, và tỉ lệ phần trăm sụt giảm doanh thu của năm $2023$ so với năm $2022$.\\\\
        c) Tính mức tăng doanh thu trung bình mỗi năm trong giai đoạn từ năm $2021$ đến năm $2025$.""" % tikz_q)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Bảng thống kê doanh thu xuất khẩu thủy sản từ năm $2021$ đến năm $2025$:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        \\textbf{Năm} & $2021$ & $2022$ & $2023$ & $2024$ & $2025$ \\\\
        \\hline
        \\textbf{Doanh thu (tỉ đồng)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        \\item Tỉ lệ phần trăm tăng trưởng doanh thu năm $2022$ so với năm $2021$ là:
        $$\\dfrac{%s - %s}{%s} \\cdot 100\\%% = 20\\%%.$$
        Tỉ lệ phần trăm sụt giảm doanh thu năm $2023$ so với năm $2022$ là:
        $$\\dfrac{%s - %s}{%s} \\cdot 100\\%% = 5\\%%.$$
        \\item Mức tăng doanh thu trung bình mỗi năm trong giai đoạn $2021 - 2025$ là:
        $$\\dfrac{%s - %s}{4} = %s \\text{ (tỉ đồng/năm)}.$$
        \\end{enumEX}""" % (fmt_vn(y21), fmt_vn(y22), fmt_vn(y23), fmt_vn(y24), fmt_vn(y25),
                          fmt_vn(y22), fmt_vn(y21), fmt_vn(y21),
                          fmt_vn(y22), fmt_vn(y23), fmt_vn(y22),
                          fmt_vn(y25), fmt_vn(y21), fmt_vn(tb_inc)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
