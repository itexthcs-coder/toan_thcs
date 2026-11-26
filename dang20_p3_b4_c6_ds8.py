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




def bt_dang20_p3_b4_c6_ds8(self):
    # Dạng 20: Bài toán hình học thực tế – Tỉ số chiều dài và chiều rộng khu đất hình chữ nhật (có hình vẽ TikZ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3])
        b = random.choice([4, 5, 6])
        x0 = a + random.choice([2, 3])
        
        tu_S = sp.expand((x + a)*(x + b))
        mau_S = sp.expand(x + a)
        tu_R = sp.expand(x + a)
        mau_R = sp.expand(x**2 - a**2)
        
        # Chiều dài = S / R = (x+a)(x+b)/(x+a) * (x-a)(x+a)/(x+a) = (x+b)(x-a)
        # Tỉ số dài / rộng = (x+b)(x-a) : (x+a)/(x^2 - a^2) = (x+b)(x-a)^2
        ti_so = (x0 + b) * (x0 - a)**2
        kq_str = str(ti_so)
        
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8]\n'
            '\\draw[thick, fill=blue!8] (0,0) rectangle (5.2,2.4);\n'
            '\\node[below] at (2.6,0) {Chiều dài};\n'
            '\\node[right] at (5.2,1.2) {$\\frac{%s}{%s}\\text{ (m)}$};\n'
            '\\node at (2.6,1.2) {$S = \\frac{%s}{%s}\\text{ (m}^2\\text{)}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        ) % (latex(tu_R), latex(mau_R), latex(tu_S), latex(mau_S))
        
        noidungcauhoi = ("""Một khu đất hình chữ nhật có diện tích được biểu diễn bởi phân thức $\\frac{%s}{%s}\\text{ (m}^2\\text{)}$ và chiều rộng là $\\frac{%s}{%s}\\text{ (m)}$ với $x > %s$.
%sKhi $x = %s$, tỉ số giữa chiều dài và chiều rộng của khu đất đó bằng bao nhiêu?"""
                         % (latex(tu_S), latex(mau_S), latex(tu_R), latex(mau_R), a, hinh_ve, x0))
        
        loigiai = ("""Chiều dài của khu đất hình chữ nhật là:\\\\
        $$\\frac{%s}{%s} : \\frac{%s}{%s} = \\frac{(x + %s)(x + %s)}{x + %s} \\cdot \\frac{(x - %s)(x + %s)}{x + %s} = (x + %s)(x - %s)\\text{ (m)}.$$\\\\
        Tỉ số giữa chiều dài và chiều rộng của khu đất là:\\\\
        $$(x + %s)(x - %s) : \\frac{x + %s}{x^2 - %s} = (x + %s)(x - %s) \\cdot \\frac{(x - %s)(x + %s)}{x + %s} = (x + %s)(x - %s)^2.$$\\\\
        Thay $x = %s$ vào biểu thức tỉ số trên, ta được:\\\\
        $$(%s + %s)(%s - %s)^2 = %s \\cdot %s = %s.$$"""
                   % (latex(tu_S), latex(mau_S), latex(tu_R), latex(mau_R),
                      a, b, a, a, a, a, b, a,
                      b, a, a, a**2, b, a, a, a, a, b, a,
                      x0, x0, b, x0, a, x0 + b, (x0 - a)**2, ti_so))
        
        dapan = '\\shortans[0]{$%s$}\n' % kq_str
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
