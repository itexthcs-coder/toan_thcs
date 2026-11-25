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


def bt_dang19_p3_b1_c6_ds8(self):
    # Dạng 19: Bài toán Vật lí - Điện trở tương đương của hai điện trở mắc song song
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (6, 6, 4),    # R1=6, R2=12 => 72/18 = 4
            (9, 6, 4),    # R1=6, R2=15 => 90/21 (lẻ) -> đổi: (6, 3, 2): R1=3, R2=9 => 27/12=2,25
            (10, 15, 6),  # R1=15, R2=25 -> đổi: (15, 10, 6): R1=10, R2=25 -> đổi: (5, 15, 3,75)
            (12, 6, 4)    # R1=6, R2=18 => 108/24 = 4,5
        ]
        scenarios = [
            (6, 6, '4'),     # 6 * 12 / 18 = 4
            (3, 6, '2'),     # 3 * 6 / 9 = 2
            (12, 6, '4,5'),  # 6 * 18 / 24 = 4,5
            (10, 10, '5')    # 10 * 20 / 30 -> 200/30 lẻ -> đổi (10, 15, '6'): 15*25/40 -> đổi (6, 3, '2'): 3*9/12=2,25
        ]
        scenarios = [
            (6, 6, '4'),
            (3, 6, '2'),
            (12, 6, '4,5'),
            (10, 15, '6')
        ]
        # Kiểm tra R1=15, R2=25 -> 375/40 = 9,375; đổi R1=10, R2=15 -> 150/25 = 6 -> diff = 5, x = 10
        scenarios = [
            (6, 6, '4'),
            (3, 6, '2'),
            (12, 6, '4,5'),
            (5, 10, '6')
        ]
        diff_r, x_val, ans_str = random.choice(scenarios)
        r2_val = x_val + diff_r
        tu_val = x_val * r2_val
        mau_val = x_val + r2_val
        
        noidungcauhoi = ('Trong mạch điện gồm hai điện trở $R_1$ và $R_2$ mắc song song, điện trở tương đương $R_{\\text{tđ}}$ của đoạn mạch được tính theo công thức $R_{\\text{tđ}} = \\dfrac{R_1 \\cdot R_2}{R_1 + R_2}\\text{ (}\\Omega\\text{)}$. Biết điện trở $R_1 = x\\text{ (}\\Omega\\text{)}$ ($x > 0$) và điện trở $R_2$ lớn hơn điện trở $R_1$ là $%s\\text{ }\\Omega$. Khi $x = %s\\text{ }\\Omega$, điện trở tương đương $R_{\\text{tđ}}$ của đoạn mạch bằng bao nhiêu Ôm?'
                         % (diff_r, x_val))
        
        loigiai = ('Ta có $R_2 = x + %s\\text{ (}\\Omega\\text{)}$, phân thức biểu thị điện trở tương đương của đoạn mạch là:\\\n'
                   '$R_{\\text{tđ}} = \\dfrac{x(x + %s)}{x + x + %s} = \\dfrac{x(x + %s)}{2x + %s}\\text{ (}\\Omega\\text{)}$.\\\n'
                   'Thay $x = %s$ vào phân thức trên, ta được:\\\n'
                   '$R_{\\text{tđ}} = \\dfrac{%s \\cdot (%s + %s)}{2 \\cdot %s + %s} = \\dfrac{%s}{%s} = %s\\text{ (}\\Omega\\text{)}$.'
                   % (diff_r, diff_r, diff_r, diff_r, diff_r, x_val, x_val, x_val, diff_r, x_val, diff_r, tu_val, mau_val, ans_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % ans_str

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
