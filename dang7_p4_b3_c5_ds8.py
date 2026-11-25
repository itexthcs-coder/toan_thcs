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

def bt_dang7_p4_b3_c5_ds8(self):
    # Dạng 7: Kết hợp biểu đồ hình quạt tròn và biểu đồ cột để phân tích cơ cấu nhân sự doanh nghiệp
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong_ns = random.choice([1000, 1200, 1400])
        p_kt, p_kd, p_hc = 55, 30, 15
        ns_kt = int(tong_ns * p_kt // 100)
        ns_kd = int(tong_ns * p_kd // 100)
        ns_hc = int(tong_ns * p_hc // 100)
        
        r_kt, r_kd, r_hc = 92, 85, 70
        dh_kt = int(ns_kt * r_kt // 100)
        dh_kd = int(ns_kd * r_kd // 100)
        dh_hc = int(ns_hc * r_hc // 100)
        tong_dh = dh_kt + dh_kd + dh_hc
        
        pct_dh = (Decimal(tong_dh * 100) / Decimal(tong_ns)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        pct_dh_str = str(pct_dh).rstrip('0').rstrip('.').replace('.', ',')
        
        def fmt_int(n):
            return f"{n:,}".replace(",", "\\,")
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.6) arc (0:198:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=black!35] (0,0) -- (198:1.6) arc (198:306:1.6) -- cycle;\n' +
            '\\draw[line width=1pt, fill=white] (0,0) -- (306:1.6) arc (306:360:1.6) -- cycle;\n' +
            '\\node at (99:0.95) {$55\\%%$};\n' +
            '\\node at (252:1.0) {$30\\%%$};\n' +
            '\\node at (333:1.15) {$15\\%%$};\n' +
            '\\node[below] at (0,-1.8) {Cơ cấu nhân sự};\n' +
            '\\begin{scope}[xshift=4.2cm, yshift=-1.4cm]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.5,0) node[below] {Khối};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[left] {Tỉ lệ ĐH ($\\%%$)};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.5,0) rectangle (1.3,2.76); \\node[above] at (0.9,2.76) {$92\\%%$}; \\node[below] at (0.9,0) {KT};\n' +
            '\\draw[line width=1pt, fill=black!35] (1.8,0) rectangle (2.6,2.55); \\node[above] at (2.2,2.55) {$85\\%%$}; \\node[below] at (2.2,0) {KD};\n' +
            '\\draw[line width=1pt, fill=white] (3.1,0) rectangle (3.9,2.10); \\node[above] at (3.5,2.10) {$70\\%%$}; \\node[below] at (3.5,0) {HC};\n' +
            '\\end{scope}\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một tập đoàn công nghệ có tổng cộng $%s$ nhân sự làm việc tại ba khối: Kĩ thuật (KT), Kinh doanh (KD) và Hành chính (HC). Biểu đồ hình quạt tròn biểu diễn cơ cấu nhân sự các khối và biểu đồ cột biểu diễn tỉ lệ nhân sự có trình độ từ Đại học trở lên ở từng khối:\n' % fmt_int(tong_ns) +
                         tikz_code + '\n' +
                         'a) Tính số lượng nhân sự của từng khối trong tập đoàn.\\\n' +
                         'b) Tính tổng số nhân sự có trình độ từ Đại học trở lên của toàn tập đoàn và cho biết nhóm này chiếm bao nhiêu phần trăm tổng số nhân sự toàn tập đoàn.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Số lượng nhân sự của từng khối trong tập đoàn là:\\\\' +
                   '- Khối Kĩ thuật: $%s \\cdot 55\\%% = %s$ (người).\\\\' +
                   '- Khối Kinh doanh: $%s \\cdot 30\\%% = %s$ (người).\\\\' +
                   '- Khối Hành chính: $%s \\cdot 15\\%% = %s$ (người).\n' +
                   '\\item Số nhân sự có trình độ từ Đại học trở lên ở từng khối là:\\\\' +
                   '- Khối Kĩ thuật: $%s \\cdot 92\\%% = %s$ (người).\\\\' +
                   '- Khối Kinh doanh: $%s \\cdot 85\\%% = %s$ (người).\\\\' +
                   '- Khối Hành chính: $%s \\cdot 70\\%% = %s$ (người).\\\\' +
                   'Tổng số nhân sự có trình độ từ Đại học trở lên của toàn tập đoàn là:\\\\' +
                   '$$%s + %s + %s = %s \\text{ (người)}.$$\\\\' +
                   'Tỉ lệ phần trăm so với toàn tập đoàn là: $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.\n' +
                   '\\end{enumEX}'
                   ) % (fmt_int(tong_ns), ns_kt, fmt_int(tong_ns), ns_kd, fmt_int(tong_ns), ns_hc,
                        ns_kt, dh_kt, ns_kd, dh_kd, ns_hc, dh_hc,
                        dh_kt, dh_kd, dh_hc, fmt_int(tong_dh), fmt_int(tong_dh), fmt_int(tong_ns), pct_dh_str)

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
