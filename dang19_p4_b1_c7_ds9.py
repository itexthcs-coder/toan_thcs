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


def bt_dang19_p4_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        f0, f1, f2, f3, f4 = 3, 7, 9, 4, 1
        tong_goi = 41
        tb = (Decimal(tong_goi) / Decimal(24)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        tb_str = str(tb).replace('.', ',')
        # Nội dung câu hỏi
        noidungcauhoi = ('''Thống kê số lượng cuộc gọi khẩn cấp tới tổng đài $115$ trong mỗi giờ qua một ngày đêm ($24$ giờ) cho kết quả: $0$ cuộc ($3$ giờ), $1$ cuộc ($7$ giờ), $2$ cuộc ($9$ giờ), $3$ cuộc ($4$ giờ), $4$ cuộc ($1$ giờ).\\\\
a) Lập bảng tần số theo cột dọc và tính số cuộc gọi khẩn cấp trung bình trong một giờ (làm tròn đến chữ số thập phân thứ hai).\\\\
b) Vẽ biểu đồ tần số dạng đoạn thẳng (đa giác tần số) để minh họa sự phân bố trên.''')
        
        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \\
    \\item Lập bảng tần số dọc:\\
    \\begin{center}
    \\begin{tabular}{|c|c|}
    \\hline
    Số cuộc gọi & Tần số (giờ) \\\\
    \\hline
    $0$ & $3$ \\\\
    $1$ & $7$ \\\\
    $2$ & $9$ \\\\
    $3$ & $4$ \\\\
    $4$ & $1$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Tổng số cuộc gọi khẩn cấp trong ngày đêm là: $0 \\cdot 3 + 1 \\cdot 7 + 2 \\cdot 9 + 3 \\cdot 4 + 4 \\cdot 1 = 41$ (cuộc).\\
    Số cuộc gọi trung bình trong một giờ là: $\\dfrac{41}{24} \\approx %s$ (cuộc).\\
    \\item Biểu đồ tần số dạng đoạn thẳng:\\
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Số cuộc gọi};
    \\draw[line width=1pt, ->] (0,0) -- (0,3.6) node[left] {Tần số (giờ)};
    \\foreach \\y/\\lbl in {1.5/5, 3.0/10}{
        \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
        \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
    }
    \\node[below left] at (0,0) {$0$};
    \\coordinate (A) at (1,0.9);
    \\coordinate (B) at (2,2.1);
    \\coordinate (C) at (3,2.7);
    \\coordinate (D) at (4,1.2);
    \\coordinate (E) at (5,0.3);
    \\draw[line width=1pt] (A) -- (B) -- (C) -- (D) -- (E);
    \\fill (A) circle (1pt) node[above] {$3$};
    \\fill (B) circle (1pt) node[above] {$7$};
    \\fill (C) circle (1pt) node[above] {$9$};
    \\fill (D) circle (1pt) node[above] {$4$};
    \\fill (E) circle (1pt) node[above] {$1$};
    \\node[below] at (1,0) {$0$};
    \\node[below] at (2,0) {$1$};
    \\node[below] at (3,0) {$2$};
    \\node[below] at (4,0) {$3$};
    \\node[below] at (5,0) {$4$};
    \\end{tikzpicture}
    \\end{center}
\\end{enumEX}''' % tb_str)
        
        # Xuất câu hỏi tự luận theo cấu trúc @tl
        content = ('\\begin{minipage}{\\textwidth} \n' +
                   '\\begin{ex}\n' +
                   str(noidungcauhoi) + '\n' +
                   '\\loigiai{ \n' +
                   str(loigiai) + '}\n' +
                   '\\end{ex}\n \\end{minipage} \n\n')
        return content
