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




def bt_dang14_p4_b4_c6_ds8(self):
    # Dạng 14: Bài toán phối hợp rút gọn tổng dây chuyền kết hợp phép nhân phân thức
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        d = random.choice([2, 3])
        x0 = random.choice([2025, 2026, 2027])
        
        # Tổng 3 số hạng: 1/(x(x+d)) + 1/((x+d)(x+2d)) + 1/((x+2d)(x+3d)) = 1/d * (1/x - 1/(x+3d)) = 3 / (x(x+3d))
        # Nhân với (x^2 + 3dx) / 3 => R = 1!
        # Hoặc nhân với (x^2 + 3dx) / 3 * (x - 1) => R = x - 1, tại x0 thì R = x0 - 1
        
        noidungcauhoi = ("""Cho biểu thức $R = \\left(\\frac{1}{x(x + %s)} + \\frac{1}{(x + %s)(x + %s)} + \\frac{1}{(x + %s)(x + %s)}\\right) \\cdot \\frac{(x^2 + %sx)(x - 1)}{3}$ với $x \\notin \\{0; -%s; -%s; -%s\\}$. \\\\
        a) Chứng minh rằng $\\frac{1}{x(x + %s)} = \\frac{1}{%s}\\left(\\frac{1}{x} - \\frac{1}{x + %s}\\right)$, từ đó rút gọn biểu thức $R$. \\\\
        b) Tính giá trị của $R$ tại $x = %s$."""
                         % (d, d, 2*d, 2*d, 3*d, 3*d, d, 2*d, 3*d, d, d, d, x0))
        
        loigiai = ("""\\begin{enumEX}[a)]{1} \n
        \\item Ta có:\\\\
        $$\\frac{1}{%s}\\left(\\frac{1}{x} - \\frac{1}{x + %s}\\right) = \\frac{1}{%s} \\cdot \\frac{x + %s - x}{x(x + %s)} = \\frac{1}{x(x + %s)}.$$\\\\
        Áp dụng công thức trên cho từng phân thức trong ngoặc, ta được:\\\\
        $$\\frac{1}{x(x + %s)} + \\frac{1}{(x + %s)(x + %s)} + \\frac{1}{(x + %s)(x + %s)} = \\frac{1}{%s}\\left(\\frac{1}{x} - \\frac{1}{x + %s} + \\frac{1}{x + %s} - \\frac{1}{x + %s} + \\frac{1}{x + %s} - \\frac{1}{x + %s}\\right)$$\\\\
        $$= \\frac{1}{%s}\\left(\\frac{1}{x} - \\frac{1}{x + %s}\\right) = \\frac{1}{%s} \\cdot \\frac{%s}{x(x + %s)} = \\frac{3}{x(x + %s)}.$$\\\\
        Khi đó:\\\\
        $$R = \\frac{3}{x(x + %s)} \\cdot \\frac{x(x + %s)(x - 1)}{3} = x - 1.$$ \n
        \\item Thay $x = %s$ (thỏa mãn điều kiện xác định) vào biểu thức rút gọn của $R$, ta được:\\\\
        $$R = %s - 1 = %s.$$ \n
        \\end{enumEX} \n"""
                   % (d, d, d, d, d, d,
                      d, d, 2*d, 2*d, 3*d, d, d, d, 2*d, 2*d, 3*d,
                      d, 3*d, d, 3*d, 3*d, 3*d,
                      3*d, 3*d, x0, x0, x0 - 1))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
