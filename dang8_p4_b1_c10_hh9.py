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


def bt_dang8_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (100, 18, 5),
            (120, 18, 6),
            (150, 12, 5),
            (144, 15, 6)
        ]
        goc_deg, l_val, r_val = random.choice(cau_hinh)
        c_day = 2 * r_val
        h_sq = l_val ** 2 - r_val ** 2
        h_sym = sqrt(h_sq)
        v_exact = Rational(1, 3) * (r_val ** 2) * h_sym
        v_val = (Decimal(str(float(v_exact))) * Decimal('3.14')).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(v_val)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cắt một hình quạt tròn tâm $S$, bán kính $SA = %s\\text{ cm}$ có số đo cung bằng $%s^\\circ$. Cuộn hình quạt tròn đó lại sao cho hai bán kính $SA$ và $SB$ trùng khít nhau để tạo thành mặt xung quanh của một hình nón đỉnh $S$ (như hình vẽ). \\\\
a) Tính bán kính đáy của hình nón tạo thành. \\\\
b) Tính chiều cao và thể tích của hình nón đó (làm tròn thể tích đến hàng đơn vị, lấy $\\pi \\approx 3,14$).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S1) at (0,2.2);
\\coordinate (A1) at (-1.2,0.4);
\\coordinate (B1) at (1.2,0.4);
\\draw[line width=1pt] (S1)--(A1) arc (-123:-57:2.16) -- cycle;
\\draw[->, line width=1pt] (1.8,1.2)--(3,1.2);
\\coordinate (S2) at (5.1,2.5);
\\coordinate (O2) at (5.1,0.2);
\\coordinate (A2) at (4.1,0.2);
\\coordinate (B2) at (6.1,0.2);
\\draw[line width=1pt] (S2)--(A2) (S2)--(B2);
\\draw[line width=1pt] (4.1,0.2) arc (180:360:1 and 0.25);
\\draw[line width=1pt, dashed] (6.1,0.2) arc (0:180:1 and 0.25);
\\draw[line width=1pt, dashed] (S2)--(O2)--(B2);
\\fill (S1) circle (1pt) node[above] {$S$};
\\fill (A1) circle (1pt) node[left] {$A$};
\\fill (B1) circle (1pt) node[right] {$B$};
\\fill (S2) circle (1pt) node[above] {$S$};
\\fill (O2) circle (1pt) node[below] {$O$};
\\end{tikzpicture}
\\end{center}'''
                         % (l_val, goc_deg))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Độ dài đường sinh của hình nón tạo thành là $l = SA = %s\\text{ cm}$. \\\\
Chu vi đáy của hình nón bằng độ dài cung $AB$ của hình quạt tròn:
$$C = \\frac{\\pi \\cdot %s \\cdot %s}{180} = %s\\pi\\text{ (cm)}.$$
Bán kính đáy của hình nón tạo thành là:
$$2\\pi r = %s\\pi \\Rightarrow r = \\frac{%s\\pi}{2\\pi} = %s\\text{ (cm)}.$$
\\item Áp dụng định lí Pythagore, chiều cao của hình nón là:
$$h = \\sqrt{l^2 - r^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s\\text{ (cm)}.$$
Thể tích của hình nón đó là:
$$V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s \\approx %s\\text{ (cm}^3\\text{)}.$$
\\end{enumEX}'''
                   % (l_val, l_val, goc_deg, c_day, c_day, c_day, r_val,
                      l_val, r_val, h_sq, latex(h_sym), r_val, latex(h_sym), kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
