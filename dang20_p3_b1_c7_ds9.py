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


def bt_dang20_p3_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        f1 = random.choice([6, 7, 8])
        f2 = 22 - f1
        f3 = 16
        f4 = 8
        f5 = 4
        ho_tro = f1 + f2
        pct = ho_tro * 100 // 50
        kq_str = str(pct)
        y1 = round(f1 * 0.2, 2)
        y2 = round(f2 * 0.2, 2)
        y3 = round(f3 * 0.2, 2)
        y4 = round(f4 * 0.2, 2)
        y5 = round(f5 * 0.2, 2)
        # Nội dung câu hỏi
        noidungcauhoi = ('''Đa giác tần số dưới đây biểu diễn mức tiêu thụ điện năng hàng tháng (đơn vị: trăm $\\text{kWh}$) của $50$ hộ gia đình trong một khu dân cư. Nhà nước có chính sách hỗ trợ giá điện cho các hộ tiêu thụ không quá $200\\text{ kWh}$/tháng (tức mức $1$ hoặc $2$ trăm $\\text{kWh}$):
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Điện năng (trăm $\\text{kWh}$)};
\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Số hộ};
\\foreach \\y/\\lbl in {1/5, 2/10, 3/15}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\coordinate (A) at (1,%s);
\\coordinate (B) at (2,%s);
\\coordinate (C) at (3,%s);
\\coordinate (D) at (4,%s);
\\coordinate (E) at (5,%s);
\\draw[line width=1pt] (A) -- (B) -- (C) -- (D) -- (E);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[above] {$%s$};
\\fill (C) circle (1pt) node[above] {$16$};
\\fill (D) circle (1pt) node[above] {$8$};
\\fill (E) circle (1pt) node[above] {$4$};
\\node[below] at (1,0) {$1$};
\\node[below] at (2,0) {$2$};
\\node[below] at (3,0) {$3$};
\\node[below] at (4,0) {$4$};
\\node[below] at (5,0) {$5$};
\\end{tikzpicture}
\\end{center}
Hỏi số hộ được hỗ trợ giá điện chiếm bao nhiêu phần trăm tổng số hộ trong khu dân cư?''' % (y1, y2, y3, y4, y5, f1, f2))
        
        # Nội dung lời giải
        loigiai = ('''Số hộ gia đình tiêu thụ không quá $200\\text{ kWh}$/tháng gồm mức $1$ trăm $\\text{kWh}$ ($%s$ hộ) và mức $2$ trăm $\\text{kWh}$ ($%s$ hộ).\\\\
Tổng số hộ được hỗ trợ giá điện là: $%s + %s = %s$ (hộ).\\\\
Tỉ lệ phần trăm số hộ được hỗ trợ giá điện là: $\\dfrac{%s}{50} \\cdot 100\\%% = %s\\%%$.\\\\
Vậy kết quả là $%s$.''' % (f1, f2, f1, f2, ho_tro, ho_tro, pct, pct))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
        # Xuất câu hỏi
        content = ('\\begin{minipage}{\\textwidth} \n' +
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n' +
                   str(dapan) +
                   '\\loigiai{ \n' +
                   str(loigiai) + '}\n' +
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content
