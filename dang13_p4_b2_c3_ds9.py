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


def bt_dang13_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([2, 3, 5])
        m = randint(2, 4)
        n = randint(2, 4)
        p = random.choice([2, 3, 5])
        q = randint(2, 5)
        
        x1 = k * (m ** 2)
        x2 = k * (n ** 2)
        x3 = p * (q ** 2)
        val_X = k * m * n - q
        
        r = random.choice([2, 3, 5, 7])
        a = randint(4, 7)
        b = randint(2, a - 1)
        y1 = r * (a ** 2)
        y2 = b ** 2
        val_Y = r * (a - b)
        
        while val_X <= 0 or val_X == val_Y:
            m += 1
            x1 = k * (m ** 2)
            val_X = k * m * n - q

        X_sq = val_X ** 2
        Y_sq = val_Y ** 2
        comp_sign = ">" if X_sq > Y_sq else "<"

        # Nội dung câu hỏi
        noidungcauhoi = ('''Không sử dụng máy tính cầm tay, hãy so sánh hai số $X = \\sqrt{%s} \\cdot \\sqrt{%s} - \\dfrac{\\sqrt{%s}}{\\sqrt{%s}}$ và $Y = \\sqrt{%s} \\cdot \\sqrt{%s} - \\sqrt{%s} \\cdot \\sqrt{%s}$.'''
                         % (x1, x2, x3, p, y1, r, r, y2))

        # Nội dung lời giải
        loigiai = ('''Rút gọn từng biểu thức bằng quy tắc nhân và chia các căn bậc hai:
        \\begin{align*}
        X &= \\sqrt{%s \\cdot %s} - \\sqrt{\\dfrac{%s}{%s}} = \\sqrt{%s^2} - \\sqrt{%s^2} = %s - %s = %s. \\\\
        Y &= \\sqrt{%s \\cdot %s} - \\sqrt{%s} \\cdot \\sqrt{%s} = \\sqrt{%s^2} - %s\\sqrt{%s} = %s - %s\\sqrt{%s} = %s\\sqrt{%s}.
        \\end{align*}
        Ta có $X = %s = \\sqrt{%s}$ và $Y = %s\\sqrt{%s} = \\sqrt{%s^2 \\cdot %s} = \\sqrt{%s}$.\\\\
        Vì $%s %s %s$ nên $\\sqrt{%s} %s \\sqrt{%s}$, vậy $X %s Y$.'''
                   % (x1, x2, x3, p, k * m * n, q, k * m * n, q, val_X,
                      y1, r, r, y2, r * a, b, r, r * a, b, r, a - b, r,
                      val_X, X_sq, a - b, r, a - b, r, Y_sq,
                      X_sq, comp_sign, Y_sq, X_sq, comp_sign, Y_sq, comp_sign))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
