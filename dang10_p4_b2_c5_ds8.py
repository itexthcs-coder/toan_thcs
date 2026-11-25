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


def bt_dang10_p4_b2_c5_ds8(self):
    # Dạng 10 (Tự luận - Vận dụng): Chuyển đổi biểu đồ tranh có nửa biểu tượng sang bảng và tính tỉ trọng phần trăm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        unit = random.choice([20, 30, 40])
        half_u = unit // 2
        w1 = 3 * unit + half_u
        w2 = 4 * unit
        w3 = 2 * unit + half_u
        w4 = 5 * unit
        tong = w1 + w2 + w3 + w4
        pct_w4 = (Decimal(str(w4 * 100)) / Decimal(str(tong))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_pct_w4 = str(pct_w4).replace(".", ",")
        
        tikz_q = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (-1.2, 0.2) rectangle (5.2, 3.4);
        \\draw[line width=1pt] (0.4, 0.2) -- (0.4, 3.4);
        \\draw[line width=1pt] (-1.2, 2.6) -- (5.2, 2.6);
        \\draw[line width=1pt] (-1.2, 1.8) -- (5.2, 1.8);
        \\draw[line width=1pt] (-1.2, 1.0) -- (5.2, 1.0);
        \\node at (-0.4, 3.0) {Tuần 1};
        \\node at (-0.4, 2.2) {Tuần 2};
        \\node at (-0.4, 1.4) {Tuần 3};
        \\node at (-0.4, 0.6) {Tuần 4};
        \\draw[line width=1pt] (0.9,2.8) rectangle (1.3,3.2) (1.6,2.8) rectangle (2.0,3.2) (2.3,2.8) rectangle (2.7,3.2) (3.0,2.8) rectangle (3.2,3.2);
        \\draw[line width=1pt] (0.9,2.0) rectangle (1.3,2.4) (1.6,2.0) rectangle (2.0,2.4) (2.3,2.0) rectangle (2.7,2.4) (3.0,2.0) rectangle (3.4,2.4);
        \\draw[line width=1pt] (0.9,1.2) rectangle (1.3,1.6) (1.6,1.2) rectangle (2.0,1.6) (2.3,1.2) rectangle (2.5,1.6);
        \\draw[line width=1pt] (0.9,0.4) rectangle (1.3,0.8) (1.6,0.4) rectangle (2.0,0.8) (2.3,0.4) rectangle (2.7,0.8) (3.0,0.4) rectangle (3.4,0.8) (3.7,0.4) rectangle (4.1,0.8);
        \\draw[line width=1pt] (0.2,-0.45) rectangle (0.6,-0.05);
        \\node[right] at (0.7,-0.25) {$= %s$ chiếc;};
        \\draw[line width=1pt] (2.8,-0.45) rectangle (3.0,-0.05);
        \\node[right] at (3.1,-0.25) {$= %s$ chiếc};
        \\end{tikzpicture}
        \\end{center}""" % (unit, half_u))
        
        noidungcauhoi = ("""Biểu đồ tranh dưới đây thống kê số lượng máy tính bảng bán được của một siêu thị điện máy trong $4$ tuần của tháng $12$:%sa) Lập bảng thống kê số lượng máy tính bảng bán được trong từng tuần.\\\\
        b) Nếu biểu diễn dữ liệu của cả $4$ tuần bằng biểu đồ hình quạt tròn thì doanh số Tuần 4 chiếm bao nhiêu phần trăm tổng doanh số cả tháng (làm tròn kết quả đến chữ số thập phân thứ nhất)?""" % tikz_q)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Số lượng máy tính bảng bán được trong từng tuần là:\\\\
        - Tuần 1: $3 \\cdot %s + %s = %s$ (chiếc).\\\\
        - Tuần 2: $4 \\cdot %s = %s$ (chiếc).\\\\
        - Tuần 3: $2 \\cdot %s + %s = %s$ (chiếc).\\\\
        - Tuần 4: $5 \\cdot %s = %s$ (chiếc).\\\\
        Bảng thống kê số lượng máy tính bảng bán được:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Tuần} & Tuần $1$ & Tuần $2$ & Tuần $3$ & Tuần $4$ \\\\
        \\hline
        \\textbf{Số lượng (chiếc)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        \\item Tổng số máy tính bảng bán được trong cả tháng là: $%s + %s + %s + %s = %s$ (chiếc).\\\\
        Tỉ lệ phần trăm doanh số Tuần 4 chiếm so với cả tháng là:
        $$\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%.$$
        \\end{enumEX}""" % (unit, half_u, w1, unit, w2, unit, half_u, w3, unit, w4, w1, w2, w3, w4, w1, w2, w3, w4, tong, w4, tong, s_pct_w4))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
