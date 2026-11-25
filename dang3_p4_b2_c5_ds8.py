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


def bt_dang3_p4_b2_c5_ds8(self):
    # Dạng 3 (Tự luận - Vận dụng): Chuyển đổi biểu đồ đoạn thẳng sang biểu đồ cột và biện luận chuỗi thời gian dài
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d = random.choice([0, 10, 20])
        t1, t2, t3, t4 = 210 + d, 195 + d, 230 + d, 265 + d
        
        tikz_q = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Điện năng (kWh)};
        \\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[right] {Tháng};
        \\coordinate (A) at (0.9,0.9);
        \\coordinate (B) at (2.2,0.6);
        \\coordinate (C) at (3.5,1.4);
        \\coordinate (D) at (4.8,2.1);
        \\draw[line width=1pt] (A)--(B)--(C)--(D);
        \\fill (A) circle (1pt) node[above] {$%s$};
        \\fill (B) circle (1pt) node[below] {$%s$};
        \\fill (C) circle (1pt) node[above] {$%s$};
        \\fill (D) circle (1pt) node[above] {$%s$};
        \\node[below] at (0.9,0) {Tháng 1};
        \\node[below] at (2.2,0) {Tháng 2};
        \\node[below] at (3.5,0) {Tháng 3};
        \\node[below] at (4.8,0) {Tháng 4};
        \\end{tikzpicture}
        \\end{center}""" % (t1, t2, t3, t4))
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Điện năng (kWh)};
        \\draw[line width=1pt, ->] (0,0) -- (5.6,0) node[right] {Tháng};
        \\draw[line width=1pt, fill=black!25] (0.6,0) rectangle (1.3,1.4); \\node[above] at (0.95,1.4) {$%s$}; \\node[below] at (0.95,0) {Tháng 1};
        \\draw[line width=1pt, fill=black!25] (1.8,0) rectangle (2.5,1.3); \\node[above] at (2.15,1.3) {$%s$}; \\node[below] at (2.15,0) {Tháng 2};
        \\draw[line width=1pt, fill=black!25] (3.0,0) rectangle (3.7,1.6); \\node[above] at (3.35,1.6) {$%s$}; \\node[below] at (3.35,0) {Tháng 3};
        \\draw[line width=1pt, fill=black!25] (4.2,0) rectangle (4.9,1.9); \\node[above] at (4.55,1.9) {$%s$}; \\node[below] at (4.55,0) {Tháng 4};
        \\end{tikzpicture}
        \\end{center}""" % (t1, t2, t3, t4))
        
        noidungcauhoi = ("""Cho biểu đồ đoạn thẳng ghi lại lượng điện tiêu thụ (đơn vị: $\\text{kWh}$) của gia đình cô Lan trong $4$ tháng đầu năm $2026$:%sa) Lập bảng thống kê biểu diễn dữ liệu trên và vẽ biểu đồ cột thay thế cho biểu đồ đoạn thẳng.\\\\
        b) Nếu cô Lan thu thập hóa đơn tiền điện hằng tháng liên tục trong suốt $5$ năm (từ năm $2021$ đến năm $2025$, gồm $60$ tháng), thì có nên dùng biểu đồ cột để biểu diễn dữ liệu đó không? Tại sao?""" % tikz_q)
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Bảng thống kê lượng điện tiêu thụ trong $4$ tháng đầu năm $2026$:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Tháng} & Tháng $1$ & Tháng $2$ & Tháng $3$ & Tháng $4$ \\\\
        \\hline
        \\textbf{Lượng điện (kWh)} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Biểu đồ cột thay thế cho biểu đồ đoạn thẳng:%s
        \\item \textbf{Không nên} dùng biểu đồ cột để biểu diễn dữ liệu liên tục trong $5$ năm ($60$ tháng), vì số lượng thời điểm quan sát quá nhiều; nếu vẽ $60$ cột đứng cạnh nhau sẽ rất dày đặc, rối mắt và khó nhận ra xu hướng biến động theo thời gian. Khi đó nên dùng \textbf{biểu đồ đoạn thẳng}.
        \\end{enumEX}""" % (t1, t2, t3, t4, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
