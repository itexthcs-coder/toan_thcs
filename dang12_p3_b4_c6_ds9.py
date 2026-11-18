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


def bt_dang12_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_voi = [(8, 4), (6, 3), (10, 5), (12, 4), (6, 6)]
        t1, diff = random.choice(bo_voi)
        t2 = t1 + diff
        t_chung = Rational(t1 * t2, t1 + t2)
        gio = t_chung.p // t_chung.q
        phut = int((t_chung - gio) * 60)
        tu = t_chung.p
        mau = t_chung.q
        a_c = mau
        b_c = mau * diff - 2 * tu
        c_c = -tu * diff
        delta_val = b_c**2 - 4 * a_c * c_c
        sqrt_d = int(math.isqrt(delta_val))
        x1_frac = Rational(-b_c - sqrt_d, 2 * a_c)
        x2_val = (-b_c + sqrt_d) // (2 * a_c)

        noidungcauhoi = ('''Hai vòi nước cùng chảy vào một bể không có nước thì sau $%s$ giờ $%s$ phút đầy bể. Nếu mở riêng từng vòi thì vòi thứ nhất chảy đầy bể nhanh hơn vòi thứ hai là $%s$ giờ. Hỏi nếu mở riêng vòi thứ nhất thì sau bao nhiêu giờ sẽ đầy bể?'''
                         % (str(gio), str(phut), str(diff)))

        loigiai = ('''Đổi $%s$ giờ $%s$ phút $= %s$ giờ.\\\\
                   Gọi thời gian vòi thứ nhất chảy riêng đầy bể là $x$ (giờ). Điều kiện: $x > 0$.\\\\
                   Khi đó, thời gian vòi thứ hai chảy riêng đầy bể là $x + %s$ (giờ).\\\\
                   Trong $1$ giờ, vòi thứ nhất chảy được $\\dfrac{1}{x}$ (bể), vòi thứ hai chảy được $\\dfrac{1}{x + %s}$ (bể), và cả hai vòi cùng chảy được $%s$ (bể).\\\\
                   Theo đề bài, ta có phương trình:\\\\
                   $\\dfrac{1}{x} + \\dfrac{1}{x + %s} = %s$.\\\\
                   Quy đồng mẫu và khử mẫu hai vế của phương trình, ta được:\\\\
                   $%s(x + %s) + %sx = %sx(x + %s)$\\\\
                   $%sx^2 + (%s)x - %s = 0$.\\\\
                   Ta có: $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-(%s) - %s}{%s} = %s$ (loại); $x_2 = \\dfrac{-(%s) + %s}{%s} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy nếu mở riêng vòi thứ nhất thì sau $%s$ giờ sẽ đầy bể.'''
                   % (str(gio), str(phut), latex(t_chung), str(diff), str(diff), latex(Rational(mau, tu)),
                      str(diff), latex(Rational(mau, tu)),
                      str(tu), str(diff), str(tu), str(mau), str(diff),
                      str(a_c), str(b_c), str(abs(c_c)),
                      str(b_c), str(a_c), str(abs(c_c)), str(delta_val), str(sqrt_d),
                      str(b_c), str(sqrt_d), str(2 * a_c), latex(x1_frac), str(b_c), str(sqrt_d), str(2 * a_c), str(x2_val), str(t1)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(t1))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
