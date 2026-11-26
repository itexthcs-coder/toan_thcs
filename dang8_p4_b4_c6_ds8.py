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




def bt_dang8_p4_b4_c6_ds8(self):
    # Dạng 8: Tìm x từ các đẳng thức chứa phép nhân, chia phân thức
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([1, 2, 3])
        k = random.choice([2, 3, 4])
        x_a = b + k
        while abs(x_a) == a:
            k += 1
            x_a = b + k
            
        c = random.choice([1, 2, 3])
        vp_b = random.choice([2, 3, 4])
        # (1/(x-c) - 2c/(x^2-c^2)) : (x-c)/(x+c) = (x+c - 2c)/(x^2-c^2) * (x+c)/(x-c) = 1/(x-c) = vp_b => x = c + 1/vp_b
        # Chọn vp_b = 1 để nghiệm nguyên đẹp: 1/(x - c) = 1 => x = c + 1
        x_b = c + 1
        
        noidungcauhoi = ("""Tìm $x$, biết: \\\\
        a) $\\frac{x^2 - %sx + %s}{x^2 - %s} \\cdot \\frac{x + %s}{x - %s} = \\frac{%s}{x - %s}$ (với $x \\neq %s, x \\neq \\pm %s$). \\\\
        b) $\\left(\\frac{1}{x - %s} - \\frac{%s}{x^2 - %s}\\right) : \\frac{x - %s}{x + %s} = 1$ (với $x \\neq \\pm %s$)."""
                         % (2*a, a**2, a**2, a, a, k, b, b, a, c, 2*c, c**2, c, c, c))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Với $x \\neq %s$ và $x \\neq \\pm %s$, rút gọn vế trái ta được:\\\\
        $$\\frac{(x - %s)^2}{(x - %s)(x + %s)} \\cdot \\frac{x + %s}{x - %s} = 1.$$\\\\
        Phương trình trở thành:\\\\
        $$\\frac{%s}{x - %s} = 1 \\Leftrightarrow x - %s = %s \\Leftrightarrow x = %s \\text{ (thỏa mãn điều kiện)}.$$ \n
        \\item Với $x \\neq \\pm %s$, rút gọn vế trái ta được:\\\\
        $$\\frac{x + %s - %s}{(x - %s)(x + %s)} \\cdot \\frac{x + %s}{x - %s} = \\frac{x - %s}{(x - %s)(x + %s)} \\cdot \\frac{x + %s}{x - %s} = \\frac{1}{x - %s}.$$\\\\
        Phương trình trở thành:\\\\
        $$\\frac{1}{x - %s} = 1 \\Leftrightarrow x - %s = 1 \\Leftrightarrow x = %s \\text{ (thỏa mãn điều kiện)}.$$ \n
        \\end{enumEX} \n"""
                   % (b, a, a, a, a, a, a, k, b, b, k, x_a,
                      c, c, 2*c, c, c, c, c, c, c, c, c, c, c, c, c, x_b))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
