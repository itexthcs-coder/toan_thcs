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

def bt_dang4_p3_b4_c7_ds8(self):
    # Dạng 4: Tính diện tích tam giác tạo bởi đồ thị hàm số bậc nhất và hai trục tọa độ
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        x0 = random.choice([-6, -4, -2, 2, 4, 6])
        b = -a * x0
        area = abs(x0 * b) // 2
        kq_str = str(area)

        dau_b = '+' if b > 0 else '-'
        px = 2.2 if x0 > 0 else -2.2
        py = 2.2 if b > 0 else -2.2
        pos_q = 'below' if b > 0 else 'above'
        pos_p = 'left' if x0 > 0 else 'right'

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.2,0) -- (3.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-3.2) -- (0,3.2) node[left] {$y$};
\\coordinate (O) at (0,0);
\\coordinate (Q) at (%s,0);
\\coordinate (P) at (0,%s);
\\draw[line width=1pt] ($(P)!-0.3!(Q)$) -- ($(Q)!-0.3!(P)$);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (Q) circle (1pt) node[%s] {$Q$};
\\fill (P) circle (1pt) node[%s] {$P$};
\\end{tikzpicture}
\\end{center}''' % (px, py, pos_q, pos_p))

        noidungcauhoi = ('''Tính diện tích của tam giác tạo bởi đồ thị hàm số $y = %sx %s %s$ với hai trục tọa độ $Ox$ và $Oy$ (đơn vị đo trên các trục là $\\text{cm}$).%s'''
                         % (a, dau_b, abs(b), tikz_code))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

        loigiai = ('''Xác định giao điểm của đồ thị hàm số $y = %sx %s %s$ với hai trục tọa độ:\\\\
- Cho $x = 0$ thì $y = %s$, ta được giao điểm với trục tung $Oy$ là $P(0; %s)$. Suy ra $OP = |%s| = %s\\text{ (cm)}$.\\\\
- Cho $y = 0$ thì $%sx %s %s = 0 \\Leftrightarrow x = %s$, ta được giao điểm với trục hoành $Ox$ là $Q(%s; 0)$. Suy ra $OQ = |%s| = %s\\text{ (cm)}$.\\\\
Tam giác $OPQ$ vuông tại gốc tọa độ $O$ nên diện tích của tam giác $OPQ$ là:\\\\
$S_{\\triangle OPQ} = \\dfrac{1}{2} \\cdot OP \\cdot OQ = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.'''
                   % (a, dau_b, abs(b),
                      b, b, b, abs(b),
                      a, dau_b, abs(b), x0, x0, x0, abs(x0),
                      abs(b), abs(x0), kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
