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


def bt_dang6_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (6, 8, 10, 216),
            (8, 6, 10, 288),
            (3, 4, 5, 216),
            (4, 3, 5, 288)
        ]
        r_val, h_val, l_val, goc_deg = random.choice(cau_hinh)
        bc_val = 2 * r_val
        sxq_pi = r_val * l_val
        v_pi = ((r_val ** 2) * h_val) // 3

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ cân tại $A$ có cạnh bên $AB = AC = %s\\text{ cm}$ và cạnh đáy $BC = %s\\text{ cm}$. Quay tam giác $ABC$ một vòng quanh đường cao $AH$ cố định để tạo thành một hình nón (như hình vẽ). \\\\
a) Tính chiều cao, diện tích xung quanh và thể tích của hình nón tạo thành. \\\\
b) Nếu cắt mặt xung quanh của hình nón này theo đường sinh $AB$ rồi trải phẳng ra thành một hình quạt tròn thì góc ở tâm của hình quạt tròn đó có số đo bằng bao nhiêu độ?
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.8);
\\coordinate (H) at (0,0);
\\coordinate (B) at (-1.5,0);
\\coordinate (C) at (1.5,0);
\\draw[line width=1pt] (A)--(B) (A)--(C);
\\draw[line width=1pt] (-1.5,0) arc (180:360:1.5 and 0.35);
\\draw[line width=1pt, dashed] (1.5,0) arc (0:180:1.5 and 0.35);
\\draw[line width=1pt, dashed] (A)--(H) (B)--(C);
\\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (l_val, bc_val))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Hình nón tạo thành có bán kính đáy $r = BH = \\frac{BC}{2} = \\frac{%s}{2} = %s\\text{ (cm)}$ và độ dài đường sinh $l = AB = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore trong tam giác $ABH$ vuông tại $H$, chiều cao của hình nón là:
$$h = AH = \\sqrt{AB^2 - BH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Diện tích xung quanh của hình nón là: $S_{xq} = \\pi r l = \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Thể tích của hình nón là: $V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.
\\item Hình quạt tròn khai triển mặt xung quanh có bán kính bằng đường sinh $l = %s\\text{ cm}$ và độ dài cung bằng chu vi đáy $2\\pi r = %s\\pi\\text{ cm}$. \\\\
Gọi $n^\\circ$ là số đo góc ở tâm của hình quạt tròn đó ($0 < n < 360$), ta có:
$$\\frac{\\pi \\cdot %s \\cdot n}{180} = %s\\pi \\Rightarrow n = \\frac{%s \\cdot 180}{%s} = %s.$$
Vậy góc ở tâm của hình quạt tròn đó có số đo bằng $%s^\\circ$.
\\end{enumEX}'''
                   % (bc_val, r_val, l_val, l_val, r_val, h_val, r_val, l_val, sxq_pi,
                      r_val, h_val, v_pi, l_val, bc_val, l_val, bc_val, bc_val, l_val, goc_deg, goc_deg))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
