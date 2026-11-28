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


def bt_dang3_p4_b1_c9_hh8(self):
    # Dạng 3: Tìm độ dài cạnh của tam giác khi biết hiệu và tổng độ dài hai cạnh tương ứng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        p = random.choice([2, 3, 4])
        q = random.choice([5, 7, 9])
        while math.gcd(p, q) != 1:
            q = random.choice([5, 7, 9])
        
        m1 = random.choice([2, 3, 4])
        MP = p * m1
        DF = q * m1
        hieu = DF - MP
        
        m2 = random.choice([3, 4, 5])
        MN = p * m2
        DE = q * m2
        tong = DE + MN
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (N) at (0,0);\n'
            '\\coordinate (P) at (2.4,0);\n'
            '\\coordinate (M) at (0.8,1.8);\n'
            '\\coordinate (E) at (3.5,0);\n'
            '\\coordinate (F) at (7.5,0);\n'
            '\\coordinate (D) at (4.83,3);\n'
            '\\draw[line width=1pt] (M)--(N)--(P)--cycle (D)--(E)--(F)--cycle;\n'
            '\\fill (M) circle (1pt) node[above] {$M$};\n'
            '\\fill (N) circle (1pt) node[left] {$N$};\n'
            '\\fill (P) circle (1pt) node[right] {$P$};\n'
            '\\fill (D) circle (1pt) node[above] {$D$};\n'
            '\\fill (E) circle (1pt) node[left] {$E$};\n'
            '\\fill (F) circle (1pt) node[right] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta MNP \\backsim \\Delta DEF$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$. '
            'Biết rằng $DF - MP = %s\\text{ cm}$ và $DE + MN = %s\\text{ cm}$. '
            'Tính độ dài các cạnh $MP$, $DF$, $MN$, $DE$.\\\n%s'
            % (p, q, hieu, tong, tikz)
        )
        
        loigiai = (
            'Vì $\\Delta MNP \\backsim \\Delta DEF$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$ nên ta có tỉ số các cạnh tương ứng:\\\n'
            '$\\dfrac{MN}{DE} = \\dfrac{MP}{DF} = \\dfrac{%s}{%s}$.\\\n'
            '- Từ $\\dfrac{MP}{DF} = \\dfrac{%s}{%s}$, áp dụng tính chất của dãy tỉ số bằng nhau ta có:\\\n'
            '$\\dfrac{MP}{%s} = \\dfrac{DF}{%s} = \\dfrac{DF - MP}{%s - %s} = \\dfrac{%s}{%s} = %s$.\\\n'
            'Suy ra $MP = %s \\cdot %s = %s\\text{ (cm)}$ và $DF = %s \\cdot %s = %s\\text{ (cm)}$.\\\n'
            '- Từ $\\dfrac{MN}{DE} = \\dfrac{%s}{%s}$, áp dụng tính chất của dãy tỉ số bằng nhau ta có:\\\n'
            '$\\dfrac{MN}{%s} = \\dfrac{DE}{%s} = \\dfrac{DE + MN}{%s + %s} = \\dfrac{%s}{%s} = %s$.\\\n'
            'Suy ra $MN = %s \\cdot %s = %s\\text{ (cm)}$ và $DE = %s \\cdot %s = %s\\text{ (cm)}$.'
            % (p, q, p, q,
               p, q, p, q, q, p, hieu, q - p, m1, p, m1, MP, q, m1, DF,
               p, q, p, q, q, p, tong, q + p, m2, p, m2, MN, q, m2, DE)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
