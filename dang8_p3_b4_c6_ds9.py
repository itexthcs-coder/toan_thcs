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


def bt_dang8_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_cay = [(20, 4, 120, 1), (15, 5, 120, 2), (24, 6, 120, 1), (30, 6, 180, 1), (16, 4, 160, 2)]
        n_dd, them_nguoi, tong_cay, giam_cay = random.choice(bo_cay)
        c_val = (tong_cay * them_nguoi) // giam_cay
        delta_val = them_nguoi**2 + 4 * c_val
        sqrt_d = int(math.isqrt(delta_val))
        x1 = (-them_nguoi - sqrt_d) // 2
        x2 = (-them_nguoi + sqrt_d) // 2

        noidungcauhoi = ('''Một chi đoàn thanh niên dự định trồng $%s$ cây xanh. Đến ngày thực hiện, do có thêm $%s$ đoàn viên tham gia nên mỗi người trồng ít hơn dự định $%s$ cây. Tính số đoàn viên dự định tham gia ban đầu.'''
                         % (str(tong_cay), str(them_nguoi), str(giam_cay)))

        loigiai = ('''Gọi số đoàn viên dự định tham gia ban đầu là $x$ (người). Điều kiện: $x \\in \\mathbb{N}^*$.\\\\
                   Theo dự định, mỗi đoàn viên phải trồng $\\dfrac{%s}{x}$ (cây).\\\\
                   Thực tế có $x + %s$ đoàn viên tham gia nên mỗi đoàn viên trồng $\\dfrac{%s}{x + %s}$ (cây).\\\\
                   Vì thực tế mỗi người trồng ít hơn dự định $%s$ cây nên ta có phương trình:\\\\
                   $\\dfrac{%s}{x} - \\dfrac{%s}{x + %s} = %s$.\\\\
                   Quy đồng mẫu và khử mẫu hai vế của phương trình, ta được:\\\\
                   $%s(x + %s) - %sx = %sx(x + %s)$\\\\
                   $%sx^2 + %sx - %s = 0$ hay $x^2 + %sx - %s = 0$.\\\\
                   Ta có: $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (-%s) = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{-%s - %s}{2} = %s$ (loại); $x_2 = \\dfrac{-%s + %s}{2} = %s$ (thỏa mãn điều kiện).\\\\
                   Vậy số đoàn viên dự định tham gia ban đầu là $%s$ người.'''
                   % (str(tong_cay), str(them_nguoi), str(tong_cay), str(them_nguoi), str(giam_cay),
                      str(tong_cay), str(tong_cay), str(them_nguoi), str(giam_cay),
                      str(tong_cay), str(them_nguoi), str(tong_cay), str(giam_cay), str(them_nguoi),
                      str(giam_cay), str(giam_cay * them_nguoi), str(tong_cay * them_nguoi), str(them_nguoi), str(c_val),
                      str(them_nguoi), str(c_val), str(delta_val), str(sqrt_d),
                      str(them_nguoi), str(sqrt_d), str(x1), str(them_nguoi), str(sqrt_d), str(x2), str(n_dd)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(n_dd))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
