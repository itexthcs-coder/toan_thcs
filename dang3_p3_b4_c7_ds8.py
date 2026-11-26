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

def bt_dang3_p3_b4_c7_ds8(self):
    # Dạng 3: Xác định hệ số a, b của hàm số bậc nhất khi biết giao điểm với hai trục tọa độ
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        x_int = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        b = -a * x_int
        P_val = a**2 + b**2
        kq_str = str(P_val)

        px = 2.0 if x_int > 0 else -2.0
        py = 2.0 if b > 0 else -2.0
        pos_q = 'below' if b > 0 else 'above'
        pos_p = 'left' if x_int > 0 else 'right'

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.2,0) -- (3.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-3.2) -- (0,3.2) node[left] {$y$};
\\coordinate (O) at (0,0);
\\coordinate (Q) at (%s,0);
\\coordinate (P) at (0,%s);
\\draw[line width=1pt] ($(P)!-0.35!(Q)$) -- ($(Q)!-0.35!(P)$);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (Q) circle (1pt) node[%s] {$%s$};
\\fill (P) circle (1pt) node[%s] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (px, py, pos_q, x_int, pos_p, b))

        noidungcauhoi = ('''Biết đồ thị hàm số bậc nhất $y = ax + b$ ($a \\neq 0$) cắt trục tung tại điểm có tung độ bằng $%s$ và cắt trục hoành tại điểm có hoành độ bằng $%s$ (như hình vẽ minh họa). Tính giá trị của biểu thức $P = a^2 + b^2$.%s'''
                         % (b, x_int, tikz_code))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

        loigiai = ('''Vì đồ thị hàm số $y = ax + b$ cắt trục tung $Oy$ tại điểm có tung độ bằng $%s$ nên điểm $P(0; %s)$ thuộc đồ thị hàm số.\\\\
Thay $x = 0$ và $y = %s$ vào công thức hàm số, ta được: $%s = a \\cdot 0 + b \\Rightarrow b = %s$.\\\\
Vì đồ thị hàm số cắt trục hoành $Ox$ tại điểm có hoành độ bằng $%s$ nên điểm $Q(%s; 0)$ thuộc đồ thị hàm số.\\\\
Thay $x = %s$, $y = 0$ và $b = %s$ vào công thức hàm số, ta được:\\\\
$0 = a \\cdot (%s) + (%s) \\Leftrightarrow a = %s$ (thỏa mãn $a \\neq 0$).\\\\
Khi đó $P = a^2 + b^2 = (%s)^2 + (%s)^2 = %s + %s = %s$.'''
                   % (b, b, b, b, b, x_int, x_int, x_int, b, x_int, b, a, a, b, a**2, b**2, kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
