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


def bt_dang6_p3_b2_c6_ds8(self):
    # Dạng 6: Rút gọn hai phân thức cồng kềnh rồi tính tổng hệ số tử thức sau khi quy đồng
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a = random.choice([2, 3])
        k = random.choice([2, 3, 4, 5])

        tu1 = latex(x**2 - a * x)
        mau1 = latex(x**3 - a**3)
        tu2 = latex(k * x + k * a)
        mau2 = latex(x**2 - a**2)
        tam_thuc = latex(expand(x**2 + a * x + a**2))
        mtc = '(x - %s)(%s)' % (a, tam_thuc)

        da_thuc_tu2 = expand(k * (x**2 + a * x + a**2))
        c2 = int(da_thuc_tu2.coeff(x, 2))
        c1 = int(da_thuc_tu2.coeff(x, 1))
        c0 = int(da_thuc_tu2.coeff(x, 0))
        tong_hs = c2 + c1 + c0
        kq_str = str(tong_hs)

        noidungcauhoi = ('Rút gọn hai phân thức $\\dfrac{%s}{%s}$ và $\\dfrac{%s}{%s}$ (với $x \\neq \\pm %s$), sau đó quy đồng mẫu thức hai phân thức nhận được với mẫu thức chung $M = %s$. Khi đó tử thức của phân thức thứ hai có dạng $ax^2 + bx + c$. Tính giá trị của $a + b + c$.' % (tu1, mau1, tu2, mau2, a, mtc))

        loigiai = ('Bước 1: Rút gọn hai phân thức đã cho:\\\n'
                   '- $\\dfrac{%s}{%s} = \\dfrac{x(x - %s)}{(x - %s)(%s)} = \\dfrac{x}{%s}$.\\\n'
                   '- $\\dfrac{%s}{%s} = \\dfrac{%s(x + %s)}{(x - %s)(x + %s)} = \\dfrac{%s}{x - %s}$.\\\n'
                   'Bước 2: Quy đồng với mẫu thức chung $M = %s$, nhân tử phụ của phân thức thứ hai là $%s$.\\\n'
                   'Tử thức của phân thức thứ hai là $%s(%s) = %s$.\\\n'
                   'Suy ra $a = %s, b = %s, c = %s$, nên $a + b + c = %s + %s + %s = %s$.'
                   % (tu1, mau1, a, a, tam_thuc, tam_thuc, tu2, mau2, k, a, a, a, k, a, mtc, tam_thuc, k, tam_thuc, latex(da_thuc_tu2), c2, c1, c0, c2, c1, c0, tong_hs))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
