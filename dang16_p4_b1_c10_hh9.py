# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""

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


def bt_dang16_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (Decimal('1.6'), Decimal('2.5'), 75, 25),
            (Decimal('2.0'), Decimal('2.5'), 80, 314),
            (Decimal('1.6'), Decimal('2.0'), 75, 20)
        ]
        d_val, h_val, phan_tram, luu_luong = random.choice(cau_hinh)
        r_val = d_val / Decimal('2')
        v_pi = (r_val ** 2) * h_val
        v_m3 = v_pi * Decimal('3.14')
        v_lit = v_m3 * Decimal('1000')
        phan_tram_thieu = 100 - phan_tram
        v_can_bom = (v_lit * Decimal(str(phan_tram_thieu))) / Decimal('100')
        thoi_gian = (v_can_bom / Decimal(str(luu_luong))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        d_s = fmt(d_val)
        r_s = fmt(r_val)
        h_s = fmt(h_val)
        v_pi_s = fmt(v_pi)
        v_m3_s = fmt(v_m3)
        v_lit_s = fmt(v_lit)
        v_can_s = fmt(v_can_bom)
        tg_s = fmt(thoi_gian)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bể chứa nước ngầm của một gia đình có dạng hình trụ đặt thẳng đứng với đường kính trong lòng bể là $%s\\text{ m}$ và chiều cao trong lòng bể là $%s\\text{ m}$ (như hình vẽ). \\\\
a) Hỏi bể chứa được tối đa bao nhiêu lít nước (lấy $\\pi \\approx 3,14$ và $1\\text{ m}^3 = 1000\\text{ lít}$)? \\\\
b) Hiện tại trong bể đang chứa lượng nước bằng $%s\\%%$ dung tích của bể. Gia đình bật máy bơm cấp nước vào bể với lưu lượng $%s\\text{ lít/phút}$. Hỏi sau bao nhiêu phút thì nước đầy bể?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.4) ellipse (1.3 and 0.3);
\\draw[line width=1pt] (-1.3,0) arc (180:360:1.3 and 0.3);
\\draw[line width=1pt, dashed] (1.3,0) arc (0:180:1.3 and 0.3);
\\draw[line width=1pt] (-1.3,0)--(-1.3,2.4) (1.3,0)--(1.3,2.4);
\\draw[line width=1pt, dashed] (-1.3,0)--(1.3,0);
\\node[below] at (0,-0.3) {$%s\\text{ m}$};
\\node[right] at (1.3,1.2) {$%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}'''
                         % (d_s, h_s, phan_tram, luu_luong, d_s, h_s))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính đáy trong lòng bể là: $R = \\frac{%s}{2} = %s\\text{ (m)}$. \\\\
Thể tích tối đa của bể nước là:
$$V = \\pi R^2 h = \\pi \\cdot (%s)^2 \\cdot %s = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (m}^3\\text{)} = %s\\text{ (lít)}.$$
\\item Lượng nước cần bơm thêm để đầy bể chiếm $100\\%% - %s\\%% = %s\\%%$ dung tích bể, tương ứng với:
$$%s \\cdot %s\\%% = %s\\text{ (lít)}.$$
Thời gian để máy bơm bơm đầy bể là:
$$%s : %s = %s\\text{ (phút)}.$$
\\end{enumEX}'''
                   % (d_s, r_s, r_s, h_s, v_pi_s, v_pi_s, v_m3_s, v_lit_s,
                      phan_tram, phan_tram_thieu, v_lit_s, phan_tram_thieu, v_can_s,
                      v_can_s, luu_luong, tg_s))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
