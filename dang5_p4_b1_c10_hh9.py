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


def bt_dang5_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [
            (5, 12, 13),
            (3, 4, 5),
            (6, 8, 10),
            (8, 15, 17),
            (9, 12, 15)
        ]
        r_val, h_val, l_val = random.choice(bo_pythagore)
        v_tru = (r_val ** 2) * h_val
        v_non = v_tru // 3
        v_con = v_tru - v_non
        sxq_tru = 2 * r_val * h_val
        s_day = r_val ** 2
        sxq_non = r_val * l_val
        s_tong = sxq_tru + s_day + sxq_non

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khối gỗ đặc dạng hình trụ có bán kính đáy $R = %s\\text{ cm}$ và chiều cao $h = %s\\text{ cm}$. Người ta khoét đi một phần gỗ có dạng hình nón có chung đáy dưới và đỉnh trùng với tâm của đáy trên hình trụ (như hình vẽ). \\\\
a) Tính thể tích phần gỗ còn lại. \\\\
b) Tính tổng diện tích bề mặt của vật thể còn lại sau khi khoét (bao gồm mặt ngoài hình trụ, mặt đáy trên và mặt xung quanh của phần nón bị khoét).
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S) at (0,2.6);
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.5,0);
\\coordinate (B) at (1.5,0);
\\draw[line width=1pt] (0,2.6) ellipse (1.5 and 0.35);
\\draw[line width=1pt] (-1.5,0) arc (180:360:1.5 and 0.35);
\\draw[line width=1pt, dashed] (1.5,0) arc (0:180:1.5 and 0.35);
\\draw[line width=1pt] (-1.5,0)--(-1.5,2.6) (1.5,0)--(1.5,2.6);
\\draw[line width=1pt, dashed] (S)--(A) (S)--(B) (S)--(O)--(B);
\\fill (S) circle (1pt) node[above] {$S$};
\\fill (O) circle (1pt) node[below] {$O$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_val, h_val))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích của khối gỗ hình trụ ban đầu là:
$$V_{\\text{trụ}} = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Thể tích phần gỗ hình nón bị khoét đi là:
$$V_{\\text{nón}} = \\frac{1}{3}\\pi R^2 h = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Thể tích phần gỗ còn lại là:
$$V = V_{\\text{trụ}} - V_{\\text{nón}} = %s\\pi - %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Độ dài đường sinh của phần hình nón bị khoét là:
$$l = \\sqrt{R^2 + h^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}.$$
Tổng diện tích bề mặt của vật thể còn lại sau khi khoét là:
$$S = S_{xq\\text{ (trụ)}} + S_{\\text{đáy trên}} + S_{xq\\text{ (nón)}} = 2\\pi R h + \\pi R^2 + \\pi R l = 2\\pi \\cdot %s \\cdot %s + \\pi \\cdot %s^2 + \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (r_val, h_val, v_tru, r_val, h_val, v_non, v_tru, v_non, v_con,
                      r_val, h_val, l_val, r_val, h_val, r_val, r_val, l_val, s_tong))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
