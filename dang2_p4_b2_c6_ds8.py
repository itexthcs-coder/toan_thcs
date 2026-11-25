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


def bt_dang2_p4_b2_c6_ds8(self):
    # Dạng 2: Tìm đa thức chưa biết trong chuỗi đẳng thức phân thức bằng nhau
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([2, 3, 5])
        while a == b:
            b = random.choice([2, 3, 5])

        tu_goc = latex(x - a)
        mau_goc = latex(x + b)
        mau_1 = latex(expand((x + b)**2))
        tu_2 = latex(x**2 - a**2)
        tu_3 = latex(a - x)

        da_thuc_A = latex(expand((x - a) * (x + b)))
        da_thuc_B = latex(expand((x + b) * (x + a)))
        da_thuc_C = latex(-x - b)

        noidungcauhoi = ('Tìm các đa thức $A, B, C$ thỏa mãn chuỗi đẳng thức sau (giả thiết các phân thức đều có nghĩa):\\\n'
                         '$\\dfrac{%s}{%s} = \\dfrac{A}{%s} = \\dfrac{%s}{B} = \\dfrac{%s}{C}$.'
                         % (tu_goc, mau_goc, mau_1, tu_2, tu_3))

        loigiai = ('\\begin{enumEX}[a)]{1}\n'
                   '\\item Ta có $%s = (%s)^2$. Nhân cả tử và mẫu của phân thức $\\dfrac{%s}{%s}$ với $(%s)$, ta được:\\\n'
                   '$\\dfrac{%s}{%s} = \\dfrac{(%s)(%s)}{(%s)^2} = \\dfrac{%s}{%s}$.\\\n'
                   'Vậy đa thức $A = %s$.\n'
                   '\\item Ta có $%s = (%s)(x + %s)$. Nhân cả tử và mẫu của phân thức $\\dfrac{%s}{%s}$ với $(x + %s)$, ta được:\\\n'
                   '$\\dfrac{%s}{%s} = \\dfrac{(%s)(x + %s)}{(%s)(x + %s)} = \\dfrac{%s}{%s}$.\\\n'
                   'Vậy đa thức $B = %s$.\n'
                   '\\item Áp dụng quy tắc đổi dấu cả tử và mẫu của phân thức $\\dfrac{%s}{%s}$, ta được:\\\n'
                   '$\\dfrac{%s}{%s} = \\dfrac{-(%s)}{-(%s)} = \\dfrac{%s}{%s}$.\\\n'
                   'Vậy đa thức $C = %s$.\n'
                   '\\end{enumEX}'
                   % (mau_1, mau_goc, tu_goc, mau_goc, mau_goc, tu_goc, mau_goc, tu_goc, mau_goc, mau_goc, da_thuc_A, mau_1, da_thuc_A,
                      tu_2, tu_goc, a, tu_goc, mau_goc, a, tu_goc, mau_goc, tu_goc, a, mau_goc, a, tu_2, da_thuc_B, da_thuc_B,
                      tu_goc, mau_goc, tu_goc, mau_goc, tu_goc, mau_goc, tu_3, da_thuc_C, da_thuc_C))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
