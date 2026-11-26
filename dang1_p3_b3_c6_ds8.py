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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D
def bt_dang1_p3_b3_c6_ds8(self):
    # Dạng 1: Tính giá trị biểu thức tổng ba phân thức có mẫu đổi dấu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # A = (4x - a)/(x - k) + (x + b)/(k - x) - (2x - c)/(x - k) = (x + (-a - b + c))/(x - k)
        # Chọn sao cho tử sau rút gọn là (x + m), và x_val - k = 10 hoặc 5 để kết quả là số thập phân hữu hạn <= 4 ký tự
        k = random.choice([2, 3, 4])
        m = random.choice([2, 4, 6, 8])
        a = random.choice([1, 2, 3])
        b = random.choice([3, 4, 5])
        c = m + a + b  # -a - b + c = m
        x_val = k + 10
        
        num = Decimal(x_val + m) / Decimal(10)
        kq = num.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        
        noidungcauhoi = ('Tính giá trị của biểu thức $A = \\dfrac{4x - %s}{x - %s} + \\dfrac{x + %s}{%s - x} - \\dfrac{2x - %s}{x - %s}$ tại $x = %s$.' % (a, k, b, k, c, k, x_val))
        
        loigiai = ('Áp dụng quy tắc đổi dấu, ta viết $\\dfrac{x + %s}{%s - x} = \\dfrac{-(x + %s)}{x - %s}$.\\'
                   'Khi đó:\\'
                   '$$\\begin{aligned}'
                   'A &= \\dfrac{4x - %s}{x - %s} - \\dfrac{x + %s}{x - %s} - \\dfrac{2x - %s}{x - %s} \\\\'
                   '&= \\dfrac{(4x - %s) - (x + %s) - (2x - %s)}{x - %s} \\\\'
                   '&= \\dfrac{4x - %s - x - %s - 2x + %s}{x - %s} = \\dfrac{x + %s}{x - %s}.'
                   '\\end{aligned}$$\\'
                   'Thay $x = %s$ (thỏa mãn $x \\neq %s$) vào biểu thức rút gọn, ta được $A = \\dfrac{%s + %s}{%s - %s} = \\dfrac{%s}{10} = %s$.'
                   % (b, k, b, k, a, k, b, k, c, k, a, b, c, k, a, b, c, k, m, k, x_val, k, x_val, m, x_val, k, x_val + m, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
