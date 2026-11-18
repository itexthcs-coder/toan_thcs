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


def bt_dang17_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v_dong = random.choice([50, 100, 150])
        v_nhom = random.choice([100, 150, 200])
        m_dong = int(Decimal('8.9') * v_dong)
        m_nhom = int(Decimal('2.7') * v_nhom)
        tong_v = v_dong + v_nhom

        a_c = 10 * tong_v
        b_c = 62 * tong_v - 10 * (m_nhom + m_dong)
        c_c = -62 * m_nhom
        g = math.gcd(math.gcd(abs(a_c), abs(b_c)), abs(c_c))
        a_s, b_s, c_s = a_c // g, b_c // g, c_c // g
        delta_val = b_s**2 - 4 * a_s * c_s
        sqrt_d = int(math.isqrt(delta_val))
        x1_frac = Rational(-b_s - sqrt_d, 2 * a_s)

        noidungcauhoi = ('''Một khối đồng nặng $%s\\text{ g}$ và một khối nhôm nặng $%s\\text{ g}$ có tổng thể tích bằng $%s\\text{ cm}^3$. Biết khối lượng riêng của đồng lớn hơn khối lượng riêng của nhôm là $6,2\\text{ g/cm}^3$. Tính khối lượng riêng của nhôm (đơn vị: $\\text{g/cm}^3$).'''
                         % (str(m_dong), str(m_nhom), str(tong_v)))

        loigiai = ('''Gọi khối lượng riêng của nhôm là $x$ ($\\text{g/cm}^3$). Điều kiện: $x > 0$.\\\\
                   Khi đó, khối lượng riêng của đồng là $x + 6,2$ ($\\text{g/cm}^3$).\\\\
                   Thể tích của khối nhôm là $\\dfrac{%s}{x}$ ($\\text{cm}^3$), thể tích của khối đồng là $\\dfrac{%s}{x + 6,2}$ ($\\text{cm}^3$).\\\\
                   Vì tổng thể tích hai khối kim loại bằng $%s\\text{ cm}^3$ nên ta có phương trình:\\\\
                   $\\dfrac{%s}{x} + \\dfrac{%s}{x + 6,2} = %s$.\\\\
                   Quy đồng mẫu và khử mẫu hai vế của phương trình, ta được:\\\\
                   $%s(x + 6,2) + %sx = %sx(x + 6,2)$\\\\
                   $%sx^2 + (%s)x - %s = 0$ hay $%sx^2 + (%s)x - %s = 0$.\\\\
                   Ta có: $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-(%s) - %s}{%s} = %s$ (loại); $x_2 = \\dfrac{-(%s) + %s}{%s} = 2,7$ (thỏa mãn điều kiện).\\\\
                   Vậy khối lượng riêng của nhôm là $2,7\\text{ g/cm}^3$.'''
                   % (str(m_nhom), str(m_dong), str(tong_v),
                      str(m_nhom), str(m_dong), str(tong_v),
                      str(m_nhom), str(m_dong), str(tong_v),
                      str(a_c), str(b_c), str(abs(c_c)), str(a_s), str(b_s), str(abs(c_s)),
                      str(b_s), str(a_s), str(abs(c_s)), str(delta_val), str(sqrt_d),
                      str(b_s), str(sqrt_d), str(2 * a_s), latex(x1_frac), str(b_s), str(sqrt_d), str(2 * a_s)))

        dapan = '\\shortans[0]{$2,7$}\n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
