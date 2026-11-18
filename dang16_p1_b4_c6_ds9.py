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


def bt_dang16_p1_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        l_val = random.choice([10, 12, 15])
        w_val = random.choice([6, 7, 8])
        h_val = random.choice([2, 3, 4])
        pct = random.choice([10, 20, 25])

        v_cu = l_val * w_val * h_val
        v_moi = int(v_cu * (100 - pct) / 100)
        v_giam = v_cu - v_moi

        # Các đáp án trắc nghiệm
        du = ['$%s(%s - x)(%s - x) = %s$' % (h_val, l_val, w_val, v_moi)]
        da = random.choice(du)
        s = [
            '$%s(%s - x)(%s - x) = %s$' % (h_val, l_val, w_val, v_giam),
            '$(%s - x)(%s - x) = %s$' % (l_val, w_val, v_moi),
            '$%s(%s + x)(%s + x) = %s$' % (h_val, l_val, w_val, v_moi),
            '$%s(%s - x)(%s - x) = %s$' % (h_val, l_val, w_val, v_cu)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Hình vẽ minh họa TikZ
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4,0);
\\coordinate (C) at (5.2,0.8);
\\coordinate (D) at (1.2,0.8);
\\coordinate (A1) at (0,1.2);
\\coordinate (B1) at (4,1.2);
\\coordinate (C1) at (5.2,2.0);
\\coordinate (D1) at (1.2,2.0);
\\draw[line width=1pt] (A)--(B)--(C)--(C1)--(B1)--(A1)--cycle (B)--(B1) (A1)--(D1)--(C1);
\\draw[line width=1pt, dashed] (A)--(D)--(C) (D)--(D1);
\\fill (A) circle (1pt);
\\fill (B) circle (1pt);
\\fill (C) circle (1pt);
\\fill (D) circle (1pt);
\\node[below] at (2,0) {$%s\\text{ cm}$};
\\node[below right] at (4.6,0.4) {$%s\\text{ cm}$};
\\node[right] at (5.2,1.4) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}''' % (l_val, w_val, h_val))

        # Câu hỏi
        noidungcauhoi = ('''Một thanh sô cô la dạng hình hộp chữ nhật có chiều dài $%s\\text{ cm}$, chiều rộng $%s\\text{ cm}$ và độ dày $%s\\text{ cm}$. Để giảm $%s\\%%$ thể tích thanh sô cô la mà vẫn giữ nguyên độ dày $%s\\text{ cm}$, nhà sản xuất giảm cả chiều dài và chiều rộng đi cùng một đoạn $x\\text{ (cm)}$ ($0 < x < %s$). Phương trình tìm $x$ là'''
                         % (l_val, w_val, h_val, pct, h_val, w_val))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''%s
Thể tích thanh sô cô la ban đầu là: $%s \\cdot %s \\cdot %s = %s\\text{ (cm}^3\\text{)}$.\\\\
Sau khi giảm $%s\\%%$, thể tích thanh sô cô la mới là: $%s \\cdot (100\\%% - %s\\%%) = %s\\text{ (cm}^3\\text{)}$.\\\\
Chiều dài và chiều rộng mới lần lượt là $%s - x\\text{ (cm)}$ và $%s - x\\text{ (cm)}$, độ dày giữ nguyên là $%s\\text{ cm}$ nên ta có phương trình:
$$%s(%s - x)(%s - x) = %s.$$'''
                   % (hinhve, l_val, w_val, h_val, v_cu, pct, v_cu, pct, v_moi, l_val, w_val, h_val, h_val, l_val, w_val, v_moi))
    
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
