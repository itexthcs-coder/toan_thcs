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


def bt_dang8_p3_b5_c7_ds8(self):
    # Dang 8: Tinh he so goc cua duong thang doi xung qua truc hoanh Ox
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_val = random.choice([-4, -3, -2, 2, 3, 4])
        b_val = random.choice([-3, -2, -1, 1, 2, 3])
        x1 = random.choice([-2, -1])
        y1 = a_val * x1 + b_val
        x2 = random.choice([1, 2])
        y2 = a_val * x2 + b_val
        a_sym = -a_val
        b_sym = -b_val
        
        s_bv = '+' if b_val >= 0 else '-'
        s_bs = '+' if b_sym >= 0 else '-'
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,2.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1.5,2.5) -- (2,-2) node[right] {$(d)$};\n'
            '\\draw[line width=1pt, dashed] (-1.5,-2.5) -- (2,2) node[right] {$(d\')$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho đường thẳng $(d): y = ax + b$ đi qua hai điểm $A(%s; %s)$ và $B(%s; %s)$. '
            'Tính hệ số góc của đường thẳng $(d\')$ đối xứng với $(d)$ qua trục hoành $Ox$.\n%s'
            % (x1, y1, x2, y2, tikz)
        )
        
        loigiai = (
            'Vì đường thẳng $(d): y = ax + b$ đi qua hai điểm $A(%s; %s)$ và $B(%s; %s)$ nên ta có hệ phương trình:\\ '
            '$\\begin{cases} (%s)a + b = %s \\\\ (%s)a + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$.\\ '
            'Suy ra phương trình đường thẳng $(d)$ là $y = %sx %s %s$.\\ '
            'Khi lấy đối xứng qua trục hoành $Ox$, mỗi điểm $(x; y) \\in (d)$ biến thành điểm $(x; -y) \\in (d\')$.\\ '
            'Do đó phương trình của đường thẳng $(d\')$ là: $-y = %sx %s %s \\Leftrightarrow y = %sx %s %s$.\\ '
            'Vậy hệ số góc của đường thẳng $(d\')$ là $%s$.'
            % (x1, y1, x2, y2, x1, y1, x2, y2, a_val, b_val, a_val, s_bv, abs(b_val), a_val, s_bv, abs(b_val), a_sym, s_bs, abs(b_sym), a_sym)
        )
        
        dapan = '\\shortans[0]{$%s$}\n' % a_sym

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
