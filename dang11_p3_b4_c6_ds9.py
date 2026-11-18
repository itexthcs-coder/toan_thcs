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


def bt_dang11_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_cano = [(20, 4, 48, 30), (24, 4, 56, 40), (25, 5, 60, 45), (30, 6, 72, 20), (15, 3, 36, 30)]
        v_thuc, v_nuoc, S, nghi_phut = random.choice(bo_cano)
        t_chay = S // (v_thuc + v_nuoc) + S // (v_thuc - v_nuoc)
        a_coef = t_chay
        c_coef = -t_chay * (v_nuoc**2)
        delta_p = S**2 - a_coef * c_coef
        sqrt_dp = int(math.isqrt(delta_p))
        x1_frac = Rational(S - sqrt_dp, a_coef)
        x2_val = (S + sqrt_dp) // a_coef

        noidungcauhoi = ('''Một ca nô chở hàng đi xuôi dòng từ bến $A$ đến bến $B$ cách nhau $%s\\text{ km}$, dừng lại bốc dỡ hàng hết $%s$ phút rồi quay ngược dòng về $A$. Tổng thời gian kể từ lúc xuất phát đến khi về đến $A$ là $%s$ giờ $%s$ phút. Biết vận tốc dòng nước là $%s\\text{ km/h}$. Tính vận tốc thực của ca nô (đơn vị: km/h).'''
                         % (str(S), str(nghi_phut), str(t_chay), str(nghi_phut), str(v_nuoc)))

        loigiai = ('''Gọi vận tốc thực của ca nô là $x$ (km/h). Vì vận tốc dòng nước là $%s\\text{ km/h}$ nên điều kiện là $x > %s$.\\\\
                   Vận tốc của ca nô khi xuôi dòng là $x + %s$ (km/h), thời gian ca nô đi xuôi dòng là $\\dfrac{%s}{x + %s}$ (giờ).\\\\
                   Vận tốc của ca nô khi ngược dòng là $x - %s$ (km/h), thời gian ca nô đi ngược dòng là $\\dfrac{%s}{x - %s}$ (giờ).\\\\
                   Vì thời gian dừng lại bốc dỡ hàng là $%s$ phút nên tổng thời gian ca nô thực sự di chuyển cả đi và về là $%s$ giờ.\\\\
                   Theo đề bài, ta có phương trình:\\\\
                   $\\dfrac{%s}{x + %s} + \\dfrac{%s}{x - %s} = %s$.\\\\
                   Quy đồng mẫu và khử mẫu hai vế của phương trình, ta được:\\\\
                   $%s(x - %s) + %s(x + %s) = %s(x + %s)(x - %s)$\\\\
                   $%sx = %sx^2 - %s$ hay $%sx^2 - %sx - %s = 0$.\\\\
                   Ta có: $\\Delta' = (-%s)^2 - %s \\cdot (-%s) = %s$; $\\sqrt{\\Delta'} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{%s - %s}{%s} = %s$ (loại); $x_2 = \\dfrac{%s + %s}{%s} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy vận tốc thực của ca nô là $%s\\text{ km/h}$.'''
                   % (str(v_nuoc), str(v_nuoc),
                      str(v_nuoc), str(S), str(v_nuoc),
                      str(v_nuoc), str(S), str(v_nuoc),
                      str(nghi_phut), str(t_chay),
                      str(S), str(v_nuoc), str(S), str(v_nuoc), str(t_chay),
                      str(S), str(v_nuoc), str(S), str(v_nuoc), str(t_chay), str(v_nuoc), str(v_nuoc),
                      str(2 * S), str(a_coef), str(abs(c_coef)), str(a_coef), str(2 * S), str(abs(c_coef)),
                      str(S), str(a_coef), str(abs(c_coef)), str(delta_p), str(sqrt_dp),
                      str(S), str(sqrt_dp), str(a_coef), latex(x1_frac), str(S), str(sqrt_dp), str(a_coef), str(x2_val), str(v_thuc)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(v_thuc))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
