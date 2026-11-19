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


def bt_dang1_p4_b2_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        ten = random.choice(['Hùng', 'Nam', 'Tuấn', 'Khoa'])
        hinh_ve = '''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) circle (1.5cm);
\\draw[line width=1pt] (-1.06,1.06)--(1.06,-1.06);
\\draw[line width=1pt] (-1.06,-1.06)--(1.06,1.06);
\\draw[line width=1pt, ->] (0,0)--(0,-1.1);
\\fill (0,0) circle (1pt);
\\node at (0,0.9) {$2$};
\\node at (0.9,0) {$4$};
\\node at (0,-0.9) {$6$};
\\node at (-0.9,0) {$8$};
\\end{tikzpicture}
\\end{center}'''

        bang_mau = '''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Lần 1 $\\backslash$ Lần 2 & $2$ & $4$ & $6$ & $8$ \\\\
\\hline
$2$ & $(2, 2)$ & $(2, 4)$ & $(2, 6)$ & $(2, 8)$ \\\\
\\hline
$4$ & $(4, 2)$ & $(4, 4)$ & $(4, 6)$ & $(4, 8)$ \\\\
\\hline
$6$ & $(6, 2)$ & $(6, 4)$ & $(6, 6)$ & $(6, 8)$ \\\\
\\hline
$8$ & $(8, 2)$ & $(8, 4)$ & $(8, 6)$ & $(8, 8)$ \\\\
\\hline
\\end{tabular}
\\end{center}'''

        noidungcauhoi = ('''Một tấm bìa cứng hình tròn được chia làm $4$ hình quạt bằng nhau, đánh số $2; 4; 6; 8$ và được gắn vào trục quay có mũi tên ở tâm như hình vẽ. Bạn %s quay tấm bìa hai lần liên tiếp, quan sát và ghi lại số của hình quạt mà mũi tên chỉ vào.%s
a) Mô tả không gian mẫu của phép thử.\\\\
b) Tính xác suất của biến cố $A$: ``Tổng hai số ghi trên hai hình quạt ở hai lần quay bằng $10$''.\\\\
c) Tính xác suất của biến cố $B$: ``Số ghi ở lần quay thứ hai gấp đôi số ghi ở lần quay thứ nhất''.'''
                         % (ten, hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Kết quả của phép thử là một cặp số $(a, b)$, trong đó $a$ và $b$ tương ứng là số ghi trên hình quạt mà mũi tên chỉ vào ở lần quay thứ nhất và lần quay thứ hai. Ta lập bảng liệt kê không gian mẫu:%s
Không gian mẫu $\\Omega$ gồm $16$ phần tử đồng khả năng:\\\\
$\\Omega = \\{(2, 2); (2, 4); (2, 6); (2, 8); (4, 2); (4, 4); (4, 6); (4, 8); (6, 2); (6, 4); (6, 6); (6, 8); (8, 2); (8, 4); (8, 6); (8, 8)\\}$.
\\item Các kết quả thuận lợi cho biến cố $A$ ($a + b = 10$) là $(2, 8); (4, 6); (6, 4); (8, 2)$, suy ra $n(A) = 4$.\\\\
Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{n(A)}{n(\\Omega)} = \\dfrac{4}{16} = \\dfrac{1}{4}$.
\\item Các kết quả thuận lợi cho biến cố $B$ ($b = 2a$) là $(2, 4); (4, 8)$, suy ra $n(B) = 2$.\\\\
Vậy xác suất của biến cố $B$ là $P(B) = \\dfrac{n(B)}{n(\\Omega)} = \\dfrac{2}{16} = \\dfrac{1}{8}$.
\\end{enumEX}''' % (bang_mau))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
