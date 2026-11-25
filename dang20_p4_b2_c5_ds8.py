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


def bt_dang20_p4_b2_c5_ds8(self):
    # Dạng 20 (Tự luận - Vận dụng thực tế): Chuyển đổi toàn diện bảng thống kê sang biểu đồ cột và hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n0, n1, n2, n3 = 4, 12, 16, 8
        tong = 40
        
        tikz_col = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.2) node[above] {Số học sinh};
        \\draw[line width=1pt, ->] (0,0) -- (5.8,0) node[right] {Số sách đọc};
        \\draw[line width=1pt, fill=black!25] (0.5,0) rectangle (1.2,0.4); \\node[above] at (0.85,0.4) {$4$}; \\node[below] at (0.85,0) {$0$ cuốn};
        \\draw[line width=1pt, fill=black!25] (1.7,0) rectangle (2.4,1.2); \\node[above] at (2.05,1.2) {$12$}; \\node[below] at (2.05,0) {$1$ cuốn};
        \\draw[line width=1pt, fill=black!25] (2.9,0) rectangle (3.6,1.6); \\node[above] at (3.25,1.6) {$16$}; \\node[below] at (3.25,0) {$2$ cuốn};
        \\draw[line width=1pt, fill=black!25] (4.1,0) rectangle (4.8,0.8); \\node[above] at (4.45,0.8) {$8$}; \\node[below] at (4.45,0) {$\\ge 3$ cuốn};
        \\end{tikzpicture}
        \\end{center}""" )
        
        tikz_pie = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.5);
        \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (36:1.5) (0,0) -- (144:1.5) (0,0) -- (288:1.5);
        \\node at (18:1.0) {$10\\%$};
        \\node at (90:0.9) {$30\\%$};
        \\node at (216:0.9) {$40\\%$};
        \\node at (324:0.9) {$20\\%$};
        \\node[right] at (1.9, 0.8) {$0$ cuốn: $10\\%$};
        \\node[right] at (1.9, 0.25) {$1$ cuốn: $30\\%$};
        \\node[right] at (1.9, -0.3) {$2$ cuốn: $40\\%$};
        \\node[right] at (1.9, -0.85) {Từ $3$ cuốn trở lên: $20\\%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Nhân dịp ngày Hội Sách, lớp 8A khảo sát số cuốn sách mỗi học sinh đọc được trong tháng $3$ và thu được bảng số liệu sau:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|}
        \\hline
        \\textbf{Số cuốn sách} & $0$ cuốn & $1$ cuốn & $2$ cuốn & Từ $3$ cuốn trở lên \\\\
        \\hline
        \\textbf{Số học sinh} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        a) Vẽ biểu đồ cột biểu diễn số lượng học sinh theo từng nhóm mức độ đọc sách.\\\\
        b) Nếu muốn báo cáo với giáo viên chủ nhiệm tỉ lệ phần trăm học sinh của lớp theo từng nhóm mức độ đọc sách, em sẽ dùng biểu đồ nào? Tính các tỉ lệ phần trăm đó và vẽ biểu đồ tương ứng.\\\\
        c) So sánh số học sinh đọc từ $2$ cuốn sách trở lên với số học sinh đọc dưới $2$ cuốn sách bằng một nhận xét ngắn gọn."""
                         % (n0, n1, n2, n3))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Biểu đồ cột biểu diễn số lượng học sinh theo từng nhóm mức độ đọc sách:%s
        \\item Để báo cáo tỉ lệ phần trăm học sinh theo từng nhóm, ta dùng \\textbf{biểu đồ hình quạt tròn}.\\\\
        Tổng số học sinh lớp 8A là: $4 + 12 + 16 + 8 = %s$ (học sinh).\\\\
        Tỉ lệ phần trăm từng nhóm là: $0$ cuốn chiếm $\\dfrac{4}{40} = 10\\%%$; $1$ cuốn chiếm $\\dfrac{12}{40} = 30\\%%$; $2$ cuốn chiếm $\\dfrac{16}{40} = 40\\%%$; từ $3$ cuốn trở lên chiếm $\\dfrac{8}{40} = 20\\%%$.%s
        \\item Số học sinh đọc từ $2$ cuốn sách trở lên là $16 + 8 = 24$ em (chiếm $60\\%%$ sĩ số lớp), nhiều hơn số học sinh đọc dưới $2$ cuốn ($4 + 12 = 16$ em, chiếm $40\\%%$) là $8$ học sinh.
        \\end{enumEX}""" % (tikz_col, tong, tikz_pie))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
