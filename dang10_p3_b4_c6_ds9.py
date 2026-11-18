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


def bt_dang10_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        P = 100
        Q = 120
        k = 2
        x_ans = random.choice([25, 30, 35])
        R = (P - x_ans) * (Q + k * x_ans)
        b_coef = P * k - Q
        c_coef = R - P * Q
        c_half = c_coef // 2
        delta_p = 20**2 - c_half
        sqrt_dp = int(math.isqrt(delta_p))
        x1 = 20 - sqrt_dp
        x2 = 20 + sqrt_dp

        noidungcauhoi = ('''Một rạp chiếu phim bán vé với giá $%s$ nghìn đồng/vé thì trung bình mỗi suất chiếu có $%s$ khán giả. Người quản lý nhận thấy cứ giảm giá vé $5$ nghìn đồng thì số khán giả lại tăng thêm $10$ người. Hỏi cần giảm giá vé bao nhiêu nghìn đồng (chọn mức giảm lớn hơn) để doanh thu mỗi suất chiếu đạt $%s$ nghìn đồng?'''
                         % (str(P), str(Q), str(R)))

        loigiai = ('''Gọi số tiền cần giảm giá mỗi vé là $x$ (nghìn đồng). Điều kiện: $0 < x < %s$.\\\\
                   Khi giảm giá vé $x$ nghìn đồng thì giá vé mới là $%s - x$ (nghìn đồng).\\\\
                   Cứ giảm $5$ nghìn đồng thì tăng $10$ khán giả, tức là giảm $1$ nghìn đồng thì tăng $2$ khán giả. Do đó số khán giả tăng thêm là $2x$ (người), tổng số khán giả lúc này là $%s + 2x$ (người).\\\\
                   Theo đề bài, doanh thu mỗi suất chiếu đạt $%s$ nghìn đồng nên ta có phương trình:\\\\
                   $(%s - x)(%s + 2x) = %s$\\\\
                   $%s + %sx - 2x^2 = %s$\\\\
                   $2x^2 - %sx + %s = 0$ hay $x^2 - 40x + %s = 0$.\\\\
                   Ta có: $\\Delta' = (-20)^2 - 1 \\cdot %s = %s$; $\\sqrt{\\Delta'} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = 20 - %s = %s$ (thỏa mãn điều kiện); $x_2 = 20 + %s = %s$ (thỏa mãn điều kiện).\\\\
                   Chọn mức giảm giá lớn hơn, ta được số tiền cần giảm giá vé là $%s$ nghìn đồng.'''
                   % (str(P), str(P), str(Q), str(R),
                      str(P), str(Q), str(R),
                      str(P * Q), str(b_coef), str(R),
                      str(b_coef), str(c_coef), str(c_half),
                      str(c_half), str(delta_p), str(sqrt_dp),
                      str(sqrt_dp), str(x1), str(sqrt_dp), str(x2), str(x2)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(x2))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
