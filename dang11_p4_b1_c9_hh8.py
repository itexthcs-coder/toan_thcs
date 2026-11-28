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


def bt_dang11_p4_b1_c9_hh8(self):
    # Dạng 11: Tìm điều kiện của tam giác ban đầu để tam giác đồng dạng là tam giác vuông cân
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        p = random.choice([2, 3, 4])
        q = random.choice([3, 5, 7])
        while math.gcd(p, q) != 1:
            q = random.choice([3, 5, 7])
        
        m = random.choice([2, 3, 4])
        A1B1 = q * m
        AB = p * m
        
        S1_val = Fraction(A1B1 ** 2, 2)
        if S1_val.denominator == 1:
            str_S1 = str(S1_val.numerator)
        else:
            str_S1 = str(S1_val.numerator // 2) + ',5'
            
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (2,0);\n'
            '\\coordinate (C) at (0,2);\n'
            '\\coordinate (A1) at (3.5,0);\n'
            '\\coordinate (B1) at (6.5,0);\n'
            '\\coordinate (C1) at (3.5,3);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A1)--(B1)--(C1)--cycle;\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (A1) circle (1pt) node[below left] {$A^{\\prime}$};\n'
            '\\fill (B1) circle (1pt) node[below right] {$B^{\\prime}$};\n'
            '\\fill (C1) circle (1pt) node[above left] {$C^{\\prime}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC \\backsim \\Delta A^{\\prime}B^{\\prime}C^{\\prime}$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$. '
            'Biết $\\Delta A^{\\prime}B^{\\prime}C^{\\prime}$ vuông tại $A^{\\prime}$, có $A^{\\prime}B^{\\prime} = %s\\text{ cm}$ và diện tích bằng $%s\\text{ cm}^2$.\\\n'
            'a) Chứng minh $\\Delta ABC$ là tam giác vuông cân.\\\n'
            'b) Tính độ dài cạnh $AB$ và cạnh huyền $BC$.\\\n%s'
            % (p, q, A1B1, str_S1, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $\\Delta A^{\\prime}B^{\\prime}C^{\\prime}$ vuông tại $A^{\\prime}$ nên diện tích của nó là $S_{\\Delta A^{\\prime}B^{\\prime}C^{\\prime}} = \\dfrac{1}{2} A^{\\prime}B^{\\prime} \\cdot A^{\\prime}C^{\\prime}$.\\\n'
            'Suy ra $A^{\\prime}C^{\\prime} = \\dfrac{2 S_{\\Delta A^{\\prime}B^{\\prime}C^{\\prime}}}{A^{\\prime}B^{\\prime}} = \\dfrac{2 \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\n'
            'Ta thấy $A^{\\prime}B^{\\prime} = A^{\\prime}C^{\\prime} = %s\\text{ cm}$ và $\\widehat{A^{\\prime}} = 90^\\circ$ nên $\\Delta A^{\\prime}B^{\\prime}C^{\\prime}$ vuông cân tại $A^{\\prime}$.\\\n'
            'Vì $\\Delta ABC \\backsim \\Delta A^{\\prime}B^{\\prime}C^{\\prime}$ nên $\\widehat{A} = \\widehat{A^{\\prime}} = 90^\\circ$ và $\\dfrac{AB}{A^{\\prime}B^{\\prime}} = \\dfrac{AC}{A^{\\prime}C^{\\prime}}$.\\\n'
            'Mà $A^{\\prime}B^{\\prime} = A^{\\prime}C^{\\prime}$ nên $AB = AC$. Vậy $\\Delta ABC$ vuông cân tại $A$.\n'
            '\\item Vì $\\Delta ABC \\backsim \\Delta A^{\\prime}B^{\\prime}C^{\\prime}$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$ nên:\\\n'
            '$AB = \\dfrac{%s}{%s} \\cdot A^{\\prime}B^{\\prime} = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$, suy ra $AC = %s\\text{ cm}$.\\\n'
            'Áp dụng định lí Pythagore trong $\\Delta ABC$ vuông tại $A$, ta có:\\\n'
            '$BC^2 = AB^2 + AC^2 = %s^2 + %s^2 = %s \\Rightarrow BC = %s\\sqrt{2}\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (str_S1, A1B1, A1B1, A1B1,
               p, q, p, q, p, q, A1B1, AB, AB,
               AB, AB, 2 * (AB ** 2), AB)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
