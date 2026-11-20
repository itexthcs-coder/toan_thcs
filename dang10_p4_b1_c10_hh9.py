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


def bt_dang10_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [
            (3, 4, 5),
            (4, 3, 5),
            (6, 8, 10),
            (5, 12, 13)
        ]
        r_val, h_val, l_val = random.choice(bo_pythagore)
        ac_val = 2 * h_val
        s_ngoai = 2 * r_val * l_val
        v_tong = (2 * (r_val ** 2) * h_val) // 3

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thoi $ABCD$ có cạnh bằng $%s\\text{ cm}$ và đường chéo $AC = %s\\text{ cm}$. Quay hình thoi $ABCD$ một vòng quanh đường chéo $AC$ cố định, ta thu được một khối tròn xoay gồm hai hình nón chung đáy (như hình vẽ). \\\\
a) Tính diện tích toàn bộ mặt ngoài của khối tròn xoay tạo thành. \\\\
b) Tính thể tích của khối tròn xoay đó.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,3.2);
\\coordinate (O) at (0,1.6);
\\coordinate (C) at (0,0);
\\coordinate (B) at (-1.4,1.6);
\\coordinate (D) at (1.4,1.6);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (-1.4,1.6) arc (180:360:1.4 and 0.3);
\\draw[line width=1pt, dashed] (1.4,1.6) arc (0:180:1.4 and 0.3);
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (D) circle (1pt) node[right] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (l_val, ac_val))

        # Nội dung lời giải
        loigiai = ('''Gọi $O$ là giao điểm hai đường chéo $AC$ và $BD$ của hình thoi $ABCD$. \\\\
Theo tính chất hình thoi, $AC \\perp BD$ tại $O$ và $OA = OC = \\frac{AC}{2} = \\frac{%s}{2} = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore trong tam giác $AOB$ vuông tại $O$:
$$OB = \\sqrt{AB^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Khối tròn xoay tạo thành gồm hai hình nón bằng nhau chung đáy có bán kính đáy $r = OB = %s\\text{ cm}$, chiều cao $h = OA = %s\\text{ cm}$ và đường sinh $l = AB = %s\\text{ cm}$.
\\begin{enumEX}[a)]{1}
\\item Diện tích toàn bộ mặt ngoài của khối tròn xoay tạo thành là:
$$S = 2 \\cdot S_{xq} = 2 \\cdot \\pi r l = 2 \\cdot \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\item Thể tích của khối tròn xoay đó là:
$$V = 2 \\cdot \\frac{1}{3}\\pi r^2 h = 2 \\cdot \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\end{enumEX}'''
                   % (ac_val, h_val, l_val, h_val, r_val, r_val, h_val, l_val,
                      r_val, l_val, s_ngoai, r_val, h_val, v_tong))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
