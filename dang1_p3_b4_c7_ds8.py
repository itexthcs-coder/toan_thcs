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

def bt_dang1_p3_b4_c7_ds8(self):
    # Dạng 1: Tìm tham số m để đồ thị hàm số bậc nhất đi qua một điểm cho trước
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            k = random.choice([2, 3, 4])
            c = random.choice([i for i in range(-6, 7) if i != 0])
            x0 = random.choice([2, 3, 4, 5])
            p = random.choice([i for i in range(-5, 6) if i != 0])
            q = random.choice([i for i in range(-8, 9) if i != 0])
            denom = k * x0 + p
            if denom in [2, 4, 5, 10, -2, -4, -5, -10]:
                num = random.choice([i for i in range(-25, 26) if i != 0 and i % denom != 0])
                m_val = Fraction(num, denom)
                if -9 < float(m_val) < 9 and c + k * m_val != 0:
                    y0_frac = (k * m_val + c) * x0 + p * m_val + q
                    if y0_frac.denominator == 1:
                        y0 = int(y0_frac)
                        break

        number = Decimal(str(float(m_val)))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        dau_c = '+' if c > 0 else '-'
        dau_p = '+' if p > 0 else '-'
        dau_q = '+' if q > 0 else '-'
        str_p = 'm' if abs(p) == 1 else '%sm' % abs(p)

        hs_str = '(%sm %s %s)x %s %s %s %s' % (k, dau_c, abs(c), dau_p, str_p, dau_q, abs(q))
        const_part = c * x0 + q
        dau_const = '+' if const_part >= 0 else '-'

        noidungcauhoi = ('''Cho hàm số bậc nhất $y = %s$. Tìm giá trị của tham số $m$ để đồ thị hàm số đi qua điểm $A(%s; %s)$ (kết quả viết dưới dạng số thập phân).'''
                         % (hs_str, x0, y0))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

        loigiai = ('''Vì đồ thị hàm số $y = %s$ đi qua điểm $A(%s; %s)$ nên thay $x = %s$ và $y = %s$ vào công thức hàm số, ta được:\\\\
$%s = (%sm %s %s) \\cdot %s %s %s %s %s$\\\\
$\\Leftrightarrow %s = %sm %s %s$\\\\
$\\Leftrightarrow %sm = %s$\\\\
$\\Leftrightarrow m = \\dfrac{%s}{%s} = %s$ (thỏa mãn điều kiện hệ số $a = %sm %s %s \\neq 0$).\\\\
Vậy giá trị cần tìm là $m = %s$.'''
                   % (hs_str, x0, y0, x0, y0,
                      y0, k, dau_c, abs(c), x0, dau_p, str_p, dau_q, abs(q),
                      y0, denom, dau_const, abs(const_part),
                      denom, num,
                      num, denom, kq_str, k, dau_c, abs(c),
                      kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
