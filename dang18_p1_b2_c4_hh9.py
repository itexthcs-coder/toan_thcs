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


def bt_dang18_p1_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab = random.randint(8, 18)
        goc = random.choice([40, 48, 50, 55, 62, 65])
        rad = math.radians(goc)

        ah_val = ab * math.sin(rad)
        ah_str = str(Decimal(str(ah_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        s_vals = [
            str(Decimal(str(ab * math.cos(rad))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
            str(Decimal(str(ab * math.tan(rad))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
            str(Decimal(str(ab / math.sin(rad))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ','),
            str(Decimal(str(2 * ab * math.cos(rad))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        ]
        s = ['$' + v + '\\text{ cm}$' for v in set(s_vals) if v != ah_str]

        # Các đáp án trắc nghiệm
        du = ['$' + ah_str + '\\text{ cm}$']
        da = random.choice(du)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4,0);
    \\coordinate (H) at (2,0);
    \\coordinate (A) at (2,2.4);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(H);
    \\draw[line width=1pt] (2,0.22)--(2.22,0.22)--(2.22,0);
    \\draw[line width=1pt] (0.5,0) arc (0:50:0.5);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[above left] at (1,1.2) {$%s\\text{ cm}$};
    \\node at (0.85,0.25) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (ab, goc))

        # Câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ cân tại $A$ có cạnh bên $AB = %s\\text{ cm}$ và góc ở đáy $\\widehat{B} = %s^\\circ$ (như hình vẽ). Độ dài đường cao $AH$ (làm tròn đến chữ số thập phân thứ nhất) là
    %s''' % (ab, goc, hinhve))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ABH$ vuông tại $H$, cạnh $AH$ là cạnh góc vuông đối diện với góc $B$ và $AB$ là cạnh huyền.\\\\
    Theo hệ thức giữa cạnh huyền và cạnh góc vuông (Định lí 1), ta có:\\\\
    $AH = AB \\cdot \\sin B = %s \\cdot \\sin %s^\\circ \\approx %s\\text{ (cm)}$.\\\\
    Vậy độ dài đường cao $AH$ xấp xỉ bằng $%s\\text{ cm}$.'''
                   % (ab, goc, ah_str, ah_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
