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

def bt_dang16_p4_b3_c5_ds8(self):
    # Dạng 16: Phân tích hiệu quả kinh doanh theo quý qua biểu đồ cột kép doanh thu - chi phí
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        dt = [680, 620, 850, 790]
        cp = [540, 510, 640, 610]
        ln = [dt[i] - cp[i] for i in range(4)] # [140, 110, 210, 180]
        ty_suat = (Decimal(ln[2] * 100) / Decimal(dt[2])).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) # 24.71
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (7.8,0) node[below] {Quý};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Triệu đồng};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.5,0) rectangle (1.1,3.4); \\node[above] at (0.8,3.4) {$680$};\n' +
            '\\draw[line width=1pt, fill=black!45] (1.1,0) rectangle (1.7,2.7); \\node[above] at (1.4,2.7) {$540$};\n' +
            '\\node[below] at (1.1,0) {Quý I};\n' +
            '\\draw[line width=1pt, fill=black!15] (2.3,0) rectangle (2.9,3.1); \\node[above] at (2.6,3.1) {$620$};\n' +
            '\\draw[line width=1pt, fill=black!45] (2.9,0) rectangle (3.5,2.55); \\node[above] at (3.2,2.55) {$510$};\n' +
            '\\node[below] at (2.9,0) {Quý II};\n' +
            '\\draw[line width=1pt, fill=black!15] (4.1,0) rectangle (4.7,4.25); \\node[above] at (4.4,4.25) {$850$};\n' +
            '\\draw[line width=1pt, fill=black!45] (4.7,0) rectangle (5.3,3.2); \\node[above] at (5.0,3.2) {$640$};\n' +
            '\\node[below] at (4.7,0) {Quý III};\n' +
            '\\draw[line width=1pt, fill=black!15] (5.9,0) rectangle (6.5,3.95); \\node[above] at (6.2,3.95) {$790$};\n' +
            '\\draw[line width=1pt, fill=black!45] (6.5,0) rectangle (7.1,3.05); \\node[above] at (6.8,3.05) {$610$};\n' +
            '\\node[below] at (6.5,0) {Quý IV};\n' +
            '\\draw[line width=1pt, fill=black!15] (7.6,3.2) rectangle (8.0,3.5) node[right, yshift=-4pt] {Doanh thu};\n' +
            '\\draw[line width=1pt, fill=black!45] (7.6,2.4) rectangle (8.0,2.7) node[right, yshift=-4pt] {Chi phí};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây ghi lại doanh thu và tổng chi phí vận hành (đơn vị: triệu đồng) của một cửa hàng sách trong $4$ quý năm $2025$:\n' +
                         tikz_code + '\n' +
                         'a) Tính lợi nhuận ($\\text{Doanh thu} - \\text{Chi phí}$) và tỉ suất lợi nhuận trên doanh thu ($\\dfrac{\\text{Lợi nhuận}}{\\text{Doanh thu}} \\cdot 100\\%%$) của cửa hàng trong Quý III (làm tròn tỉ suất lợi nhuận đến chữ số thập phân thứ hai).\\\n' +
                         'b) Nhận xét xu hướng biến động doanh thu và lợi nhuận của cửa hàng qua $4$ quý; giải thích vì sao Quý III lại có doanh thu và lợi nhuận cao nhất trong năm đối với ngành kinh doanh sách.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Trong Quý III, lợi nhuận của cửa hàng sách đạt:\\\\' +
                   '$$850 - 640 = 210 \\text{ (triệu đồng)}.$$\\\\' +
                   'Tỉ suất lợi nhuận trên doanh thu của cửa hàng trong Quý III là:\\\\' +
                   '$$\\dfrac{210}{850} \\cdot 100\\%% \\approx %s\\%%.$$\n' +
                   '\\item Lợi nhuận các quý lần lượt là: Quý I đạt $140$ triệu đồng; Quý II giảm xuống $110$ triệu đồng; Quý III tăng vọt lên đỉnh điểm $210$ triệu đồng và Quý IV giảm nhẹ còn $180$ triệu đồng.\\\\' +
                   'Giải thích: Quý III (từ tháng $7$ đến tháng $9$) trùng với dịp chuẩn bị khai giảng năm học mới nên nhu cầu mua sắm sách giáo khoa, sách tham khảo và đồ dùng học tập của học sinh tăng đột biến, giúp doanh thu và lợi nhuận đạt mức cao nhất năm.\n' +
                   '\\end{enumEX}'
                   ) % (fmt_vn(ty_suat))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
