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


def bt_dang17_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (30, 40, 50, Decimal('0.72')),
            (15, 20, 25, Decimal('0.75')),
            (30, 40, 50, Decimal('0.80'))
        ]
        r_cm, h_cm, l_cm, klr = random.choice(cau_hinh)
        c_cm = Decimal('2') * Decimal('3.14') * Decimal(str(r_cm))
        sxq_cm2 = Decimal('3.14') * Decimal(str(r_cm)) * Decimal(str(l_cm))
        r_dm = Decimal(str(r_cm)) / Decimal('10')
        h_dm = Decimal(str(h_cm)) / Decimal('10')
        v_pi_dm3 = ((r_dm ** 2) * h_dm) / Decimal('3')
        v_dm3 = (v_pi_dm3 * Decimal('3.14')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        khoi_luong = (v_dm3 * klr).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        c_s = fmt(c_cm)
        sxq_s = fmt(sxq_cm2)
        r_dm_s = fmt(r_dm)
        h_dm_s = fmt(h_dm)
        v_pi_s = fmt(v_pi_dm3)
        v_dm3_s = fmt(v_dm3)
        klr_s = fmt(klr)
        kl_s = fmt(khoi_luong)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một chiếc phễu thu gom hạt nông sản có dạng hình nón với chu vi miệng phễu là $%s\\text{ cm}$ và độ dài đường sinh là $%s\\text{ cm}$ (lấy $\\pi \\approx 3,14$, xem hình vẽ). \\\\
a) Tính diện tích tôn cần dùng để làm mặt xung quanh chiếc phễu đó (coi phần mép hàn không đáng kể). \\\\
b) Khi đổ đầy hạt ngô vào phễu (hạt ngô san phẳng ngang miệng phễu), biết khối lượng riêng của hạt ngô là $%s\\text{ kg/dm}^3$. Hỏi chiếc phễu khi đầy chứa được bao nhiêu kilôgam hạt ngô (làm tròn kết quả đến hàng phần mười)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.4) ellipse (1.5 and 0.35);
\\draw[line width=1pt] (-1.5,2.4)--(0,0)--(1.5,2.4);
\\draw[line width=1pt, dashed] (0,2.4)--(0,0) (0,2.4)--(1.5,2.4);
\\end{tikzpicture}
\\end{center}'''
                         % (c_s, l_cm, klr_s))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính miệng phễu hình nón là: $r \\approx \\frac{%s}{2 \\cdot 3,14} = %s\\text{ (cm)} = %s\\text{ (dm)}$. \\\\
Diện tích tôn cần dùng để làm mặt xung quanh chiếc phễu là:
$$S_{xq} = \\pi r l \\approx 3,14 \\cdot %s \\cdot %s = %s\\text{ (cm}^2\\text{)}.$$
\\item Chiều cao của chiếc phễu là: $h = \\sqrt{l^2 - r^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)} = %s\\text{ (dm)}$. \\\\
Thể tích của chiếc phễu là:
$$V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\cdot (%s)^2 \\cdot %s = %s\\pi \\approx %s \\cdot 3,14 = %s\\text{ (dm}^3\\text{)}.$$
Khối lượng hạt ngô khi chứa đầy phễu là:
$$m = %s \\cdot %s \\approx %s\\text{ (kg)}.$$
\\end{enumEX}'''
                   % (c_s, r_cm, r_dm_s, r_cm, l_cm, sxq_s,
                      l_cm, r_cm, h_cm, h_dm_s, r_dm_s, h_dm_s, v_pi_s, v_pi_s, v_dm3_s,
                      v_dm3_s, klr_s, kl_s))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
