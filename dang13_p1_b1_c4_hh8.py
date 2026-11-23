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


def bt_dang13_p1_b1_c4_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        def fmt_num(val):
            if val.is_Integer:
                return str(int(val))
            fval = float(val)
            return str(fval).replace('.', ',')

        pe = random.choice([4, 6, 8])
        pf = random.choice([5, 6, 9])
        fq_dec = random.choice([2.5, 3.5, 4.5])
        pq = Rational(pf) + Rational(str(fq_dec))
        y_val = Rational(pe * pq, pf)

        fq_str = str(fq_dec).replace('.', ',')
        y_str = fmt_num(y_val)
        eh_val = y_val - pe
        eh_str = fmt_num(eh_val)

        s_pool = [eh_str, fmt_num(y_val + 2), fmt_num(y_val - Rational(3, 2)), fmt_num(Rational(pe) + Rational(str(fq_dec))), fmt_num(y_val + Rational(7, 2))]
        s = list(set(['$%s$' % (v) for v in s_pool if v != y_str]))

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (y_str)]
        da = random.choice(du)
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Tìm độ dài $y$ trong hình vẽ bên dưới (các số chỉ kích thước trên hình có cùng đơn vị đo).
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (H) at (0,0);
\\coordinate (P) at (0,3.2);
\\coordinate (Q) at (4,0);
\\coordinate (E) at (0,1.6);
\\coordinate (F) at (2,1.6);
\\draw[line width=1pt] (P)--(H)--(Q)--cycle (E)--(F);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (0,1.85)--(0.25,1.85)--(0.25,1.6);
\\draw[<->, line width=1pt] (-0.7,0)--(-0.7,3.2) node[midway, left] {$y$};
\\fill (P) circle (1pt) node[above] {$P$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (Q) circle (1pt) node[below right] {$Q$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (F) circle (1pt) node[right] {$F$};
\\path (P)--(E) node[midway, left] {$%s$};
\\path (P)--(F) node[midway, right] {$%s$};
\\path (F)--(Q) node[midway, right] {$%s$};
\\end{tikzpicture}
\\end{center}'''
                         % (pe, pf, fq_str))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Ta có $EF \\perp PH$ và $HQ \\perp PH$ nên $EF // HQ$ (từ vuông góc đến song song).\\\\
Độ dài đoạn thẳng $PQ$ là: $PQ = PF + FQ = %s + %s = %s$.\\\\
Xét $\\Delta PHQ$ có $EF // HQ$ ($E \\in PH$, $F \\in PQ$), theo định lí Thalès trong tam giác ta có:\\\\
$\\dfrac{PE}{PH} = \\dfrac{PF}{PQ}$.\\\\
Thay số vào tỉ lệ thức trên, ta được:\\\\
$\\dfrac{%s}{y} = \\dfrac{%s}{%s} \\Rightarrow y = \\dfrac{%s \\cdot %s}{%s} = %s$.\\\\
Vậy $y = %s$.'''
                   % (pf, fq_str, fmt_num(pq), pe, pf, fmt_num(pq), pe, fmt_num(pq), pf, y_str, y_str))

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
