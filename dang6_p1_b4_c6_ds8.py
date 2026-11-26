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




def bt_dang6_p1_b4_c6_ds8(self):
    # Dạng 6: Nhân hai phân thức có tử và mẫu là các đơn thức
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        y_sym, z_sym = sp.symbols('y z')
        k1 = random.choice([2, 3, 5, 7])
        k2 = random.choice([2, 3, 4, 5])
        m1 = random.choice([2, 3, 4])
        m2 = random.choice([2, 3, 5])
        
        c1 = k1 * random.choice([1, 2])
        d1 = m1 * random.choice([1, 2])
        c2 = m2 * random.choice([1, 2])
        d2 = k2 * random.choice([1, 2])
        
        dau1 = random.choice([1, -1])
        dau2 = random.choice([1, -1])
        
        p_x1 = random.randint(2, 4)
        p_y1 = random.randint(1, 2)
        p_z1 = random.randint(1, 2)
        
        p_z2 = random.randint(2, 4)
        p_x2 = random.randint(1, 2)
        p_y2 = random.randint(2, 4)
        
        tu1 = dau1 * c1 * (x**p_x1) * (y_sym**p_y1)
        mau1 = d1 * (z_sym**p_z1)
        tu2 = dau2 * c2 * (z_sym**p_z2)
        mau2 = d2 * (x**p_x2) * (y_sym**p_y2)
        
        kq = sp.simplify((tu1 / mau1) * (tu2 / mau2))
        
        s = [
            latex(-kq),
            latex(sp.simplify(kq * x)),
            latex(sp.simplify(kq / y_sym)),
            latex(sp.simplify(-kq * z_sym)),
            latex(sp.simplify(kq * Rational(1, 2)))
        ]
        s = list(dict.fromkeys([item for item in s if item != latex(kq)]))
        
        du = ['$%s$' % latex(kq)]
        da = random.choice(du)
        
        das1 = '$' + random.choice(s) + '$'
        s.remove(das1[1:-1])
        das2 = '$' + random.choice(s) + '$'
        s.remove(das2[1:-1])
        das3 = '$' + random.choice(s) + '$'
        
        str_pt1 = '\\frac{%s}{%s}' % (latex(tu1), latex(mau1))
        str_pt2 = '\\left(%s\\right)' % ('\\frac{%s}{%s}' % (latex(tu2), latex(mau2))) if dau2 < 0 else '\\frac{%s}{%s}' % (latex(tu2), latex(mau2))
        
        noidungcauhoi = ("""Kết quả rút gọn của phép nhân $%s \\cdot %s$ (với các biến đều khác $0$) là"""
                         % (str_pt1, str_pt2))
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Ta có:\\\\
        $$%s \\cdot %s = \\frac{(%s) \\cdot (%s)}{(%s) \\cdot (%s)} = %s.$$"""
                   % (str_pt1, str_pt2, latex(tu1), latex(tu2), latex(mau1), latex(mau2), latex(kq)))
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
