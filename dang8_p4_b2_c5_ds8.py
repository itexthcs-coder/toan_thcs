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


def bt_dang8_p4_b2_c5_ds8(self):
    # Dạng 8 (Tự luận - Vận dụng): Tách dữ liệu thành phần từ biểu đồ cột kép sang biểu đồ cột đơn và tính tỉ lệ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nam6, nu6 = 22, 18
        nam7, nu7 = 25, 20
        nam8, nu8 = 28, 24
        nam9, nu9 = 30, 22
        tong_nu = nu6 + nu7 + nu8 + nu9
        tong_all = (nam6 + nam7 + nam8 + nam9) + tong_nu
        pct_nu = (Decimal(str(tong_nu * 100)) / Decimal(str(tong_all))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_pct_nu = str(pct_nu).replace(".", ",")
        
        tikz_q = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số học sinh};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Khối};
        \\draw[line width=1pt, fill=black!35] (0.5,0) rectangle (0.95,1.4) (1.9,0) rectangle (2.35,1.6) (3.3,0) rectangle (3.75,1.8) (4.7,0) rectangle (5.15,2.0);
        \\draw[line width=1pt, fill=white] (0.95,0) rectangle (1.4,1.1) (2.35,0) rectangle (2.8,1.3) (3.75,0) rectangle (4.2,1.5) (5.15,0) rectangle (5.6,1.4);
        \\node[above] at (0.72,1.4) {$22$}; \\node[above] at (1.18,1.1) {$18$};
        \\node[above] at (2.12,1.6) {$25$}; \\node[above] at (2.58,1.3) {$20$};
        \\node[above] at (3.52,1.8) {$28$}; \\node[above] at (3.98,1.5) {$24$};
        \\node[above] at (4.92,2.0) {$30$}; \\node[above] at (5.38,1.4) {$22$};
        \\node[below] at (0.95,0) {Khối 6}; \\node[below] at (2.35,0) {Khối 7};
        \\node[below] at (3.75,0) {Khối 8}; \\node[below] at (5.15,0) {Khối 9};
        \\draw[line width=1pt, fill=black!35] (6.0,1.7) rectangle (6.3,2.0); \\node[right] at (6.3,1.85) {Nam};
        \\draw[line width=1pt, fill=white] (6.0,1.2) rectangle (6.3,1.5); \\node[right] at (6.3,1.35) {Nữ};
        \\end{tikzpicture}
        \\end{center}""" )
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.4) node[above] {Số học sinh nữ};
        \\draw[line width=1pt, ->] (0,0) -- (5.8,0) node[right] {Khối};
        \\draw[line width=1pt, fill=black!25] (0.5,0) rectangle (1.2,1.2); \\node[above] at (0.85,1.2) {$18$}; \\node[below] at (0.85,0) {Khối 6};
        \\draw[line width=1pt, fill=black!25] (1.7,0) rectangle (2.4,1.35); \\node[above] at (2.05,1.35) {$20$}; \\node[below] at (2.05,0) {Khối 7};
        \\draw[line width=1pt, fill=black!25] (2.9,0) rectangle (3.6,1.6); \\node[above] at (3.25,1.6) {$24$}; \\node[below] at (3.25,0) {Khối 8};
        \\draw[line width=1pt, fill=black!25] (4.1,0) rectangle (4.8,1.45); \\node[above] at (4.45,1.45) {$22$}; \\node[below] at (4.45,0) {Khối 9};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Cho biểu đồ cột kép thống kê số lượng học sinh nam và học sinh nữ tham gia giải chạy việt dã của bốn khối lớp:%sa) Hãy lập bảng thống kê riêng cho số lượng \textbf{học sinh nữ} tham gia giải chạy ở bốn khối và vẽ biểu đồ cột đơn biểu diễn bảng thống kê đó.\\\\
        b) Tính tỉ lệ phần trăm số học sinh nữ tham gia giải chạy so với tổng số học sinh toàn trường tham gia giải (làm tròn kết quả đến chữ số thập phân thứ nhất).""" % tikz_q)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Bảng thống kê số lượng học sinh nữ tham gia giải chạy ở bốn khối:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Khối} & Khối $6$ & Khối $7$ & Khối $8$ & Khối $9$ \\\\
        \\hline
        \\textbf{Số học sinh nữ} & $18$ & $20$ & $24$ & $22$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Biểu đồ cột đơn biểu diễn số lượng học sinh nữ:%s
        \\item Tổng số học sinh nữ tham gia giải chạy là: $18 + 20 + 24 + 22 = %s$ (học sinh).\\\\
        Tổng số học sinh toàn trường tham gia giải chạy là: $(22 + 25 + 28 + 30) + %s = %s$ (học sinh).\\\\
        Tỉ lệ phần trăm số học sinh nữ tham gia giải chạy so với toàn trường là:
        $$\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%.$$
        \\end{enumEX}""" % (tikz_a, tong_nu, tong_nu, tong_all, tong_nu, tong_all, s_pct_nu))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
