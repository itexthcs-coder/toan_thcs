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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang5_p4_b3_c4_hh8(self):
    # Dạng 5: Khai thác tính chất đường phân giác kết hợp đường cao trong tam giác vuông
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'H', 'D', 'E'),
            ('M', 'N', 'P', 'H', 'K', 'I')
        ]
        A, B, C, H, D, E = random.choice(bo_dinh)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (1.5,2.5);\n'
            '\\coordinate (%s) at (0,0);\n'
            '\\coordinate (%s) at (4.5,0);\n'
            '\\coordinate (%s) at (1.5,0);\n'
            '\\coordinate (%s) at (2.8,1.42);\n'
            '\\coordinate (%s) at (1.5,0.76);\n'
            '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s);\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, H, D, E, A, B, C, A, H, B, D, A, A, B, B, C, C, H, H, D, D, E, E)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ vuông tại $%s$ ($%s%s < %s%s$), đường cao $%s%s$ ($%s \\in %s%s$). Tia phân giác của góc $%s%s%s$ cắt $%s%s$ tại $%s$ và cắt $%s%s$ tại $%s$.\\\\\n'
            'a) Chứng minh $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$ và $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\\n'
            'b) Chứng minh tam giác $%s%s%s$ cân tại $%s$, từ đó suy ra $%s%s = %s%s$.\n%s'
            % (A, B, C, A, A, B, A, C, A, H, H, B, C, A, B, C, A, H, E, A, C, D, E, H, E, A, B, H, B, A, D, A, D, C, B, A, B, C, A, E, D, A, A, E, A, D, hinh_ve)
        )

        p1 = (
            '\\item Trong tam giác $%s%s%s$ có $%s%s$ là tia phân giác của góc $%s%s%s$ ($%s \\in %s%s$) nên theo tính chất đường phân giác, ta có: $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\'
            % (A, B, H, B, E, A, B, H, E, A, H, E, H, E, A, B, H, B, A)
        )
        p2 = (
            'Trong tam giác $%s%s%s$ có $%s%s$ là tia phân giác của góc $%s%s%s$ ($%s \\in %s%s$) nên theo tính chất đường phân giác, ta có: $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$ (điều phải chứng minh). \n'
            % (A, B, C, B, D, A, B, C, D, A, C, D, A, D, C, B, A, B, C)
        )
        p3 = (
            '\\item Ta có $\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$ (do tam giác $%s%s%s$ vuông tại $%s$) và $\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$ (do tam giác $%s%s%s$ vuông tại $%s$).\\\\'
            % (A, D, B, A, B, D, A, B, C, A, H, E, B, H, B, E, B, H, E, H)
        )
        p4 = (
            'Mà $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (do $%s%s$ là tia phân giác của góc $%s%s%s$) nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\'
            % (A, B, D, H, B, E, B, D, A, B, C, A, D, B, H, E, B)
        )
        p5 = (
            'Lại có $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc đối đỉnh), suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s}$. Vậy tam giác $%s%s%s$ cân tại $%s$, suy ra $%s%s = %s%s$ (điều phải chứng minh). \n'
            % (H, E, B, A, E, D, A, D, E, A, E, D, A, E, D, A, A, E, A, D)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + p5 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
