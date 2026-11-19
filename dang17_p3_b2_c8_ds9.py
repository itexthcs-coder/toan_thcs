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


def bt_dang17_p3_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        dk = random.choice([
            ('$a + b > 10$', '$(2, 9); (4, 7); (4, 9); (6, 5); (6, 7); (6, 9); (8, 3); (8, 5); (8, 7); (8, 9)$', 10),
            ('$a + b < 8$', '$(2, 1); (2, 3); (2, 5); (4, 1); (4, 3); (6, 1)$', 6),
            ('$a > b$', '$(2, 1); (4, 1); (4, 3); (6, 1); (6, 3); (6, 5); (8, 1); (8, 3); (8, 5); (8, 7)$', 10)
        ])
        nd_dk, chuoi_tl, so_tl = dk
        xs = Rational(so_tl, 20)
        kq_str = ('%g' % float(xs)).replace('.', ',')

        hinh_ve = '''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.3cm);
\\draw[line width=1pt] (0,-1.3)--(0,1.3);
\\draw[line width=1pt] (-1.3,0)--(1.3,0);
\\draw[line width=1pt, ->] (0,0)--(0,-0.95);
\\fill (0,0) circle (1pt);
\\node at (-0.55,0.55) {$2$};
\\node at (0.55,0.55) {$4$};
\\node at (0.55,-0.55) {$6$};
\\node at (-0.55,-0.55) {$8$};
\\node at (0,-1.7) {Đĩa tròn $A$};

\\draw[line width=1pt] (4,0) circle (1.3cm);
\\draw[line width=1pt] (4,0)--(4,1.3);
\\draw[line width=1pt] (4,0)--(5.24,0.4);
\\draw[line width=1pt] (4,0)--(4.76,-1.05);
\\draw[line width=1pt] (4,0)--(3.24,-1.05);
\\draw[line width=1pt] (4,0)--(2.76,0.4);
\\draw[line width=1pt, ->] (4,0)--(4,-0.95);
\\fill (4,0) circle (1pt);
\\node at (3.4,0.75) {$1$};
\\node at (4.6,0.75) {$3$};
\\node at (4.85,-0.25) {$5$};
\\node at (4,-0.85) {$7$};
\\node at (3.15,-0.25) {$9$};
\\node at (4,-1.7) {Đĩa tròn $B$};
\\end{tikzpicture}
\\end{center}'''

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
Đĩa $A$ $\\backslash$ Đĩa $B$ & $1$ & $3$ & $5$ & $7$ & $9$ \\\\
\\hline
$2$ & $(2, 1)$ & $(2, 3)$ & $(2, 5)$ & $(2, 7)$ & $(2, 9)$ \\\\
\\hline
$4$ & $(4, 1)$ & $(4, 3)$ & $(4, 5)$ & $(4, 7)$ & $(4, 9)$ \\\\
\\hline
$6$ & $(6, 1)$ & $(6, 3)$ & $(6, 5)$ & $(6, 7)$ & $(6, 9)$ \\\\
\\hline
$8$ & $(8, 1)$ & $(8, 3)$ & $(8, 5)$ & $(8, 7)$ & $(8, 9)$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        noidungcauhoi = ('''Đĩa tròn $A$ chia thành $4$ hình quạt bằng nhau ghi số $2; 4; 6; 8$. Đĩa tròn $B$ chia thành $5$ hình quạt bằng nhau ghi số $1; 3; 5; 7; 9$ như hình vẽ. Quay đồng thời cả hai đĩa tròn và ghi lại số ở hình quạt mà mũi tên chỉ vào ($a$ trên đĩa $A$, $b$ trên đĩa $B$). Tính xác suất của biến cố $G$: ``%s''.%s'''
                         % (nd_dk, hinh_ve))

        loigiai = ('''Ta lập bảng liệt kê không gian mẫu $\\Omega$:%s
Không gian mẫu $\\Omega$ gồm $4 \\cdot 5 = 20$ cặp số đồng khả năng nên $n(\\Omega) = 20$.\\\\
Các kết quả thuận lợi cho biến cố $G$ (%s) là: %s, suy ra $n(G) = %s$.\\\\
Vậy xác suất của biến cố $G$ là $P(G) = \\dfrac{%s}{20} = %s$.'''
                   % (bang_mau, nd_dk, chuoi_tl, so_tl, so_tl, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
