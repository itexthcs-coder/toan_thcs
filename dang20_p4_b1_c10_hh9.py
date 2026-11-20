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


def bt_dang20_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (4, 10, 3, 8, 24, Decimal('1.5'), Decimal('11.5'), 15),
            (5, 8, 3, 15, 45, Decimal('1.8'), Decimal('9.8'), 14),
            (6, 9, 3, 12, 36, Decimal('1'), Decimal('10'), 15)
        ]
        r_coc, h_nuoc_bd, r_non, h_non, v_non_pi, delta_h, h_sau, h_coc = random.choice(cau_hinh)

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        delta_h_s = fmt(delta_h)
        h_sau_s = fmt(h_sau)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một cốc đong hình trụ có bán kính đáy trong lòng cốc là $R = %s\\text{ cm}$ đang chứa nước đến độ cao $%s\\text{ cm}$. Người ta thả chìm hoàn toàn vào cốc một quả dọi bằng đồng có dạng một khối nón đặc với bán kính đáy $r = %s\\text{ cm}$ và chiều cao $h_{\\text{nón}} = %s\\text{ cm}$ (như hình vẽ). \\\\
a) Tính thể tích của quả dọi hình nón. \\\\
b) Hỏi mực nước trong cốc dâng lên đến độ cao bao nhiêu centimet (biết chiều cao của cốc là $%s\\text{ cm}$ nên nước không tràn ra ngoài)?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.6) ellipse (1.2 and 0.28);
\\draw[line width=1pt] (-1.2,0) arc (180:360:1.2 and 0.28);
\\draw[line width=1pt, dashed] (1.2,0) arc (0:180:1.2 and 0.28);
\\draw[line width=1pt] (-1.2,0)--(-1.2,2.6) (1.2,0)--(1.2,2.6);
\\draw[line width=1pt, dashed] (0,1.4) ellipse (1.2 and 0.28);
\\draw[line width=1pt] (0,1.9) ellipse (1.2 and 0.28);
\\draw[line width=1pt] (0,1.1)--(-0.5,0.15) (0,1.1)--(0.5,0.15);
\\draw[line width=1pt] (0,0.15) ellipse (0.5 and 0.12);
\\end{tikzpicture}
\\end{center}'''
                         % (r_coc, h_nuoc_bd, r_non, h_non, h_coc))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích của quả dọi hình nón là:
$$V_{\\text{nón}} = \\frac{1}{3}\\pi r^2 h_{\\text{nón}} = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Phần nước dâng thêm trong cốc có dạng hình trụ bán kính đáy $R = %s\\text{ cm}$, chiều cao $\\Delta h$ và có thể tích bằng thể tích quả dọi hình nón:
$$\\pi R^2 \\cdot \\Delta h = V_{\\text{nón}} \\Rightarrow \\pi \\cdot %s^2 \\cdot \\Delta h = %s\\pi \\Rightarrow %s \\cdot \\Delta h = %s \\Rightarrow \\Delta h = %s\\text{ (cm)}.$$
Vậy mực nước trong cốc dâng lên đến độ cao là:
$$%s + %s = %s\\text{ (cm)}.$$
\\end{enumEX}'''
                   % (r_non, h_non, v_non_pi, r_coc, r_coc, v_non_pi, r_coc ** 2, v_non_pi, delta_h_s,
                      h_nuoc_bd, delta_h_s, h_sau_s))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
