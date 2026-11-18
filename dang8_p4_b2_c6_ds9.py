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


def bt_dang8_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m = randint(2, 5)
        p = randint(1, 4)
        q = p + 2*(m + 1)
        k = p + q - 2*m
        
        b_pt = p - q
        c_pt = p + q - k
        delta = b_pt**2 - 8*c_pt
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Giải phương trình chứa ẩn ở mẫu sau: \\\\
                         $\\dfrac{x + %s}{x - 1} + \\dfrac{x - %s}{x + 1} = \\dfrac{%s}{x^2 - 1}$.'''
                         %(latex(p), latex(q), latex(k)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Điều kiện xác định của phương trình: $x \\neq 1$ và $x \\neq -1$. \\\\
                   Quy đồng mẫu thức hai vế của phương trình với mẫu thức chung là $x^2 - 1 = (x - 1)(x + 1)$, ta được: \\\\
                   $\\dfrac{(x + %s)(x + 1) + (x - %s)(x - 1)}{x^2 - 1} = \\dfrac{%s}{x^2 - 1}$ \\\\
                   Suy ra: \\\\
                   $(x + %s)(x + 1) + (x - %s)(x - 1) = %s$ \\\\
                   $\\Leftrightarrow x^2 + %sx + %s + x^2 - %sx + %s = %s$ \\\\
                   $\\Leftrightarrow 2x^2 %s %sx + %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = 2$, $b = %s$, $c = %s$. \\\\
                   Ta có biệt thức $\\Delta = (%s)^2 - 4 \\cdot 2 \\cdot %s = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{-(%s) + \\sqrt{%s}}{2 \\cdot 2} = %s$ (thỏa mãn điều kiện xác định); \\\\
                   $x_2 = \\dfrac{-(%s) - \\sqrt{%s}}{2 \\cdot 2} = 1$ (không thỏa mãn điều kiện xác định nên loại). \\\\
                   Vậy phương trình đã cho có nghiệm duy nhất là $x = %s$.'''
                   %(latex(p), latex(q), latex(k),
                     latex(p), latex(q), latex(k),
                     latex(p + 1), latex(p), latex(q + 1), latex(q), latex(k),
                     "-" if b_pt < 0 else "+", latex(abs(b_pt)), latex(c_pt),
                     latex(b_pt), latex(c_pt),
                     latex(b_pt), latex(c_pt), latex(delta),
                     latex(b_pt), latex(delta), latex(m),
                     latex(b_pt), latex(delta),
                     latex(m)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
