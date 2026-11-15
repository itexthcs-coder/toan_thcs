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


def bt_dang7_p4_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        n = randint(2, 5)
        tu_1 = n * (n + 1) + 1
        mau_1 = n * (n + 1)
        
        p = randint(2, 5)
        tu_2 = mau_1 ** 2
        mau_2 = p ** 2
        
        a_dec = random.choice([12, 15, 18, 24, 25])
        b_dec = random.choice([2, 3, 4, 5])
        num_a = Rational(a_dec ** 2, 100)
        num_b = Rational(b_dec ** 2, 100)
        
        val_1 = Rational(tu_1, p)
        val_2 = Rational(a_dec, b_dec)
        ans = val_1 + val_2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Tính giá trị của biểu thức: $K = \\sqrt{1 + \\dfrac{1}{%s^2} + \\dfrac{1}{%s^2}} \\cdot \\sqrt{\\dfrac{%s}{%s}} + \\dfrac{\\sqrt{%s}}{\\sqrt{%s}}$.'''
                         % (n, n + 1, tu_2, mau_2, float(num_a), float(num_b)))

        # Nội dung lời giải
        loigiai = ('''Ta có:
        $$1 + \\dfrac{1}{%s^2} + \\dfrac{1}{%s^2} = \\dfrac{%s^2 \\cdot %s^2 + %s^2 + %s^2}{%s^2 \\cdot %s^2} = \\dfrac{(%s)^2}{(%s)^2}.$$
        Mặt khác $\\dfrac{%s}{%s} = \\dfrac{%s}{%s} = %s$. Do đó:
        \\begin{align*}
        K &= \\sqrt{\\dfrac{(%s)^2}{(%s)^2}} \\cdot \\sqrt{\\dfrac{%s^2}{%s^2}} + \\sqrt{%s} \\\\
        &= \\dfrac{%s}{%s} \\cdot \\dfrac{%s}{%s} + %s \\\\
        &= %s + %s = %s.
        \\end{align*}'''
                   % (n, n + 1, n, n + 1, n + 1, n, n, n + 1, tu_1, mau_1,
                      float(num_a), float(num_b), a_dec ** 2, b_dec ** 2, latex(Rational(a_dec ** 2, b_dec ** 2)),
                      tu_1, mau_1, mau_1, p, latex(Rational(a_dec ** 2, b_dec ** 2)),
                      tu_1, mau_1, mau_1, p, latex(val_2),
                      latex(val_1), latex(val_2), latex(ans)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
