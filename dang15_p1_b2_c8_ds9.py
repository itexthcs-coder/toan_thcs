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


def bt_dang15_p1_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        dk = random.choice([
            ('là một số lẻ', [(1, 1), (1, 3), (3, 1), (3, 3)], 4),
            ('là một số chẵn', [(1, 2), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 2), (3, 4)], 8),
            ('bằng $6$', [(2, 3), (3, 2)], 2),
            ('nhỏ hơn $4$', [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)], 5)
        ])
        nd_dk, ds_tl, so_tl = dk
        xs = Rational(so_tl, 12)
        da_str = '$\\dfrac{%s}{%s}$' % (xs.p, xs.q)
        chuoi_tl = '; '.join(['$(%s, %s)$' % (x, y) for x, y in ds_tl])

        du = [da_str]
        da = random.choice(du)
        tat_ca = ['$\\dfrac{1}{6}$', '$\\dfrac{1}{4}$', '$\\dfrac{1}{3}$', '$\\dfrac{5}{12}$', '$\\dfrac{1}{2}$', '$\\dfrac{2}{3}$']
        tat_ca.remove(da_str)
        das1 = random.choice(tat_ca)
        tat_ca.remove(das1)
        das2 = random.choice(tat_ca)
        tat_ca.remove(das2)
        das3 = random.choice(tat_ca)

        hinh_ve = '''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.3cm);
\\draw[line width=1pt] (0,0)--(0,1.3);
\\draw[line width=1pt] (0,0)--(1.12,-0.65);
\\draw[line width=1pt] (0,0)--(-1.12,-0.65);
\\draw[line width=1pt, ->] (0,0)--(0,-0.95);
\\fill (0,0) circle (1pt);
\\node at (-0.65,0.45) {$1$};
\\node at (0.65,0.45) {$2$};
\\node at (0,-0.75) {$3$};
\\node at (0,-1.7) {Tấm bìa $A$};

\\draw[line width=1pt] (4,0) circle (1.3cm);
\\draw[line width=1pt] (3.08,0.92)--(4.92,-0.92);
\\draw[line width=1pt] (3.08,-0.92)--(4.92,0.92);
\\draw[line width=1pt, ->] (4,0)--(4,-0.95);
\\fill (4,0) circle (1pt);
\\node at (4,0.8) {$1$};
\\node at (4.8,0) {$2$};
\\node at (4,-0.8) {$3$};
\\node at (3.2,0) {$4$};
\\node at (4,-1.7) {Tấm bìa $B$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Tấm bìa $A$ hình tròn chia thành $3$ hình quạt bằng nhau ghi số $1; 2; 3$. Tấm bìa $B$ hình tròn chia thành $4$ hình quạt bằng nhau ghi số $1; 2; 3; 4$ như hình vẽ. Quay đồng thời cả hai tấm bìa. Xác suất để tích hai số ở hai mũi tên chỉ vào %s bằng%s'''
                         % (nd_dk, hinh_ve))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Tấm bìa $A$ $\\backslash$ Tấm bìa $B$ & $1$ & $2$ & $3$ & $4$ \\\\
\\hline
$1$ & $(1, 1)$ & $(1, 2)$ & $(1, 3)$ & $(1, 4)$ \\\\
\\hline
$2$ & $(2, 1)$ & $(2, 2)$ & $(2, 3)$ & $(2, 4)$ \\\\
\\hline
$3$ & $(3, 1)$ & $(3, 2)$ & $(3, 3)$ & $(3, 4)$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        loigiai = ('''Ta lập bảng liệt kê các kết quả có thể của phép thử:%s
Không gian mẫu $\\Omega$ gồm $12$ kết quả đồng khả năng nên $n(\\Omega) = 12$.\\\\
Gọi $E$ là biến cố ``Tích hai số ở hai mũi tên chỉ vào %s''.\\\\
Các kết quả thuận lợi cho biến cố $E$ là: %s. Suy ra $n(E) = %s$.\\\\
Vậy xác suất cần tìm là $P(E) = \\dfrac{n(E)}{n(\\Omega)} = \\dfrac{%s}{%s}$.'''
                   % (bang_mau, nd_dk, chuoi_tl, so_tl, xs.p, xs.q))

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
