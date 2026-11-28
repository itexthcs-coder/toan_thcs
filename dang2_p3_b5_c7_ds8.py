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


def bt_dang2_p3_b5_c7_ds8(self):
    # Dang 2: Tim tong cac gia tri nguyen cua tham so de hai duong thang cat nhau
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([1, 4, 9])
        sqrt_p = int(math.sqrt(p))
        k = random.choice([2, 3, 4])
        a2 = k**2 - p
        N = random.choice([4, 5, 6])
        b1 = random.choice([10, 15, 20])
        b2 = random.choice([-5, -3, -2, 2, 3])
        sign_b2 = '+' if b2 > 0 else '-'
        abs_b2 = abs(b2)
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,3) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-2,-1.5) -- (2.5,2.5) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-2,2.5) -- (2.5,-1.5) node[right] {$(d_2)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0.25,0.5) circle (1pt) node[above] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Tìm tổng tất cả các giá trị nguyên của tham số $m$ thuộc đoạn $[-%s; %s]$ để đường thẳng '
            '$(d_1): y = (m^2 - %s)x + %s$ cắt đường thẳng $(d_2): y = %sx %s %s$.\n%s'
            % (N, N, p, b1, a2, sign_b2, abs_b2, tikz)
        )
        
        loigiai = (
            'Để $(d_1)$ là đồ thị của hàm số bậc nhất thì hệ số góc của $(d_1)$ phải khác $0$, tức là: $m^2 - %s \\neq 0 \\Leftrightarrow m \\neq \\pm %s$.\\ '
            'Để đường thẳng $(d_1)$ cắt đường thẳng $(d_2)$ thì hai hệ số góc phải khác nhau: $m^2 - %s \\neq %s \\Leftrightarrow m^2 \\neq %s \\Leftrightarrow m \\neq \\pm %s$.\\ '
            'Vì $m$ là số nguyên thuộc đoạn $[-%s; %s]$ nên các giá trị của $m$ thỏa mãn điều kiện trên gồm các số đối nhau từng đôi một (ngoại trừ các giá trị $\\pm %s$ và $\\pm %s$ bị loại).\\ '
            'Do tính chất đối xứng qua số $0$, tổng tất cả các giá trị nguyên của $m$ thỏa mãn bài toán bằng $0$.'
            % (p, sqrt_p, p, a2, k**2, k, N, N, sqrt_p, k)
        )
        
        dapan = '\\shortans[0]{$0$}\n'

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
