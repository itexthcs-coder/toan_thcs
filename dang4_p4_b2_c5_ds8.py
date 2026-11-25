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


def bt_dang4_p4_b2_c5_ds8(self):
    # Dạng 4 (Tự luận - Vận dụng): Biện luận loại trừ biểu đồ cho dữ liệu thập phân không theo thời gian
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        def fmt_vn(val):
            return f"{val:.2f}".replace(".", ",")
        d = Decimal(str(random.choice([0.00, 0.10, 0.20])))
        s1 = Decimal('7.45') + d
        s2 = Decimal('8.12') + d
        s3 = Decimal('6.85') + d
        s4 = Decimal('7.90') + d
        s5 = Decimal('8.34') + d
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Điểm TB};
        \\draw[line width=1pt, ->] (0,0) -- (6.5,0) node[right] {Lớp};
        \\draw[line width=1pt, fill=black!25] (0.5,0) rectangle (1.1,1.3); \\node[above] at (0.8,1.3) {$%s$}; \\node[below] at (0.8,0) {8A};
        \\draw[line width=1pt, fill=black!25] (1.6,0) rectangle (2.2,1.7); \\node[above] at (1.9,1.7) {$%s$}; \\node[below] at (1.9,0) {8B};
        \\draw[line width=1pt, fill=black!25] (2.7,0) rectangle (3.3,1.1); \\node[above] at (3.0,1.1) {$%s$}; \\node[below] at (3.0,0) {8C};
        \\draw[line width=1pt, fill=black!25] (3.8,0) rectangle (4.4,1.5); \\node[above] at (4.1,1.5) {$%s$}; \\node[below] at (4.1,0) {8D};
        \\draw[line width=1pt, fill=black!25] (4.9,0) rectangle (5.5,1.9); \\node[above] at (5.2,1.9) {$%s$}; \\node[below] at (5.2,0) {8E};
        \\end{tikzpicture}
        \\end{center}""" % (fmt_vn(s1), fmt_vn(s2), fmt_vn(s3), fmt_vn(s4), fmt_vn(s5)))
        
        noidungcauhoi = ("""Bảng thống kê điểm thi môn Khoa học tự nhiên trung bình của năm lớp khối 8 trong kì thi khảo sát chất lượng như sau:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        \\textbf{Lớp} & 8A & 8B & 8C & 8D & 8E \\\\
        \\hline
        \\textbf{Điểm trung bình} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Hãy giải thích vì sao \textbf{không} dùng biểu đồ tranh, \textbf{không} dùng biểu đồ đoạn thẳng, \textbf{không} dùng biểu đồ hình quạt tròn cho bảng số liệu này, từ đó lựa chọn và vẽ biểu đồ phù hợp nhất."""
                         % (fmt_vn(s1), fmt_vn(s2), fmt_vn(s3), fmt_vn(s4), fmt_vn(s5)))
        
        loigiai = ("""- \textbf{Không dùng biểu đồ tranh} vì các số liệu điểm trung bình ($%s; %s; %s; %s; %s$) đều là số thập phân lẻ đến hai chữ số sau dấu phẩy.\\\\
        - \textbf{Không dùng biểu đồ đoạn thẳng} vì trục ngang biểu diễn tên các lớp độc lập khác nhau, không phải là các mốc thời gian liên tục.\\\\
        - \textbf{Không dùng biểu đồ hình quạt tròn} vì đây là giá trị điểm trung bình của từng lớp chứ không phải cơ cấu tỉ lệ phần trăm các phần trong một tổng thể.\\\\
        - Vậy \textbf{biểu đồ cột} là lựa chọn phù hợp nhất:%s"""
                   % (fmt_vn(s1), fmt_vn(s2), fmt_vn(s3), fmt_vn(s4), fmt_vn(s5), tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
