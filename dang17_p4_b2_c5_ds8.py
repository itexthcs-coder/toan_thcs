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


def bt_dang17_p4_b2_c5_ds8(self):
    # Dạng 17 (Tự luận - Vận dụng): Suy luận đại số tìm số liệu và dựng biểu đồ cột
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x_val = random.choice([30, 40, 50])
        tt = x_val
        tth = x_val + 24
        kh = 2 * x_val
        ls = 2 * x_val - 16
        tong = tt + tth + kh + ls
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.4) node[above] {Số lượt mượn};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Thể loại};
        \\draw[line width=1pt, fill=black!25] (0.5,0) rectangle (1.3,1.0); \\node[above] at (0.9,1.0) {$%s$}; \\node[below] at (0.9,0) {T.Tranh};
        \\draw[line width=1pt, fill=black!25] (1.9,0) rectangle (2.7,1.5); \\node[above] at (2.3,1.5) {$%s$}; \\node[below] at (2.3,0) {T.Thuyết};
        \\draw[line width=1pt, fill=black!25] (3.3,0) rectangle (4.1,2.0); \\node[above] at (3.7,2.0) {$%s$}; \\node[below] at (3.7,0) {Khoa học};
        \\draw[line width=1pt, fill=black!25] (4.7,0) rectangle (5.5,1.5); \\node[above] at (5.1,1.5) {$%s$}; \\node[below] at (5.1,0) {Lịch sử};
        \\end{tikzpicture}
        \\end{center}""" % (tt, tth, kh, ls))
        
        noidungcauhoi = ("""Một thư viện thống kê số lượt mượn sách trong tuần qua bốn thể loại: Truyện tranh, Tiểu thuyết, Sách khoa học và Sách lịch sử. Biết rằng:\\\\
        - Số lượt mượn Tiểu thuyết nhiều hơn Truyện tranh là $24$ lượt;\\\\
        - Số lượt mượn Sách khoa học gấp đôi số lượt mượn Truyện tranh;\\\\
        - Số lượt mượn Sách lịch sử ít hơn Sách khoa học là $16$ lượt;\\\\
        - Tổng số lượt mượn cả bốn thể loại trong tuần là $%s$ lượt.\\\\
        a) Tìm số lượt mượn của từng thể loại sách và lập bảng thống kê.\\\\
        b) Vẽ biểu đồ cột biểu diễn bảng thống kê vừa tìm được.""" % tong)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Gọi số lượt mượn Truyện tranh là $x$ (lượt, $x \\in \\mathbb{N}^*$).\\\\
        Khi đó số lượt mượn Tiểu thuyết là $x + 24$, Sách khoa học là $2x$ và Sách lịch sử là $2x - 16$.\\\\
        Ta có phương trình:
        $$x + (x + 24) + 2x + (2x - 16) = %s \\Leftrightarrow 6x + 8 = %s \\Leftrightarrow 6x = %s \\Leftrightarrow x = %s.$$
        Suy ra: Truyện tranh có $%s$ lượt; Tiểu thuyết có $%s$ lượt; Sách khoa học có $%s$ lượt; Sách lịch sử có $%s$ lượt.\\\\
        Bảng thống kê số lượt mượn sách trong tuần:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Thể loại} & Truyện tranh & Tiểu thuyết & Sách khoa học & Sách lịch sử \\\\
        \\hline
        \\textbf{Số lượt mượn} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        \\item Biểu đồ cột biểu diễn bảng thống kê trên:%s
        \\end{enumEX}""" % (tong, tong, tong - 8, x_val, tt, tth, kh, ls, tt, tth, kh, ls, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
