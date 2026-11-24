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

def bt_dang4_p4_b3_c4_hh8(self):
    # Dạng 4: Chứng minh hệ thức độ dài trong tam giác có đường phân giác
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'D', 'E'),
            ('M', 'N', 'P', 'D', 'K')
        ]
        A, B, C, D, E = random.choice(bo_dinh)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (1.5,3.2);\n'
            '\\coordinate (%s) at (0,0);\n'
            '\\coordinate (%s) at (4.6,0);\n'
            '\\coordinate (%s) at (1.84,0);\n'
            '\\coordinate (%s) at ($(%s)!0.62!(%s)$);\n'
            '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s);\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, D, E, A, C, A, B, C, A, D, D, E, A, A, B, B, C, C, D, D, E, E)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ ($%s%s < %s%s$), đường phân giác $%s%s$ ($%s \\in %s%s$). Trên cạnh $%s%s$ lấy điểm $%s$ sao cho $%s%s = %s%s$.\\\\\n'
            'a) Chứng minh $\\Delta %s%s%s = \\Delta %s%s%s$, từ đó suy ra $%s%s = %s%s$.\\\\\n'
            'b) Chứng minh rằng $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s - %s%s}$.\n%s'
            % (A, B, C, A, B, A, C, A, D, D, B, C, A, C, E, A, E, A, B, A, B, D, A, E, D, B, D, E, D, B, D, E, C, A, B, A, C, A, B, hinh_ve)
        )

        p1 = (
            '\\item Xét $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có: $%s%s = %s%s$ (giả thiết), $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (do $%s%s$ là tia phân giác của góc $%s%s%s$) và cạnh $%s%s$ chung.\\\\'
            % (A, B, D, A, E, D, A, B, A, E, B, A, D, E, A, D, A, D, B, A, C, A, D)
        )
        p2 = (
            'Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c), do đó $%s%s = %s%s$ (hai cạnh tương ứng). \n'
            % (A, B, D, A, E, D, B, D, E, D)
        )
        p3 = (
            '\\item Trong tam giác $%s%s%s$ có $%s%s$ là đường phân giác của góc $%s$ nên $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\'
            % (A, B, C, A, D, A, B, D, D, C, A, B, A, C)
        )
        p4 = (
            'Mà $%s%s = %s%s$ (chứng minh trên) và $%s%s = %s%s - %s%s = %s%s - %s%s$ (do $%s$ nằm giữa $%s$ và $%s$).\\\\'
            % (B, D, E, D, E, C, A, C, A, E, A, C, A, B, E, A, C)
        )
        p5 = (
            'Thay vào tỉ lệ thức trên ta được $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s - %s%s}$ (điều phải chứng minh). \n'
            % (B, D, E, C, A, B, A, C, A, B)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + p5 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
