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


def bt_dang12_p4_b4_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (8, 12, 4, 48, 5, 24),
            (6, 12, 4, 0, 1, 4),
            (10, 15, 6, 0, 1, 6),
            (12, 24, 8, 0, 1, 8),
            (9, 18, 6, 0, 1, 6),
            (12, 20, 7, 30, 2, 15)
        ])
        t1, t2, gio_chung, phut_chung, tu_chung, mau_chung = bo_so
        chenh = t2 - t1

        a_pt = tu_chung
        b_pt = tu_chung * chenh - 2 * mau_chung
        c_pt = -mau_chung * chenh

        g = math.gcd(abs(a_pt), math.gcd(abs(b_pt), abs(c_pt)))
        a_pt //= g
        b_pt //= g
        c_pt //= g

        delta = b_pt**2 - 4 * a_pt * c_pt
        can_delta = int(math.isqrt(delta))
        nghiem_1 = Rational(-b_pt - can_delta, 2 * a_pt)

        if phut_chung > 0:
            tg_str = f"{gio_chung}\\text{{ giờ }}{phut_chung}\\text{{ phút}}"
        else:
            tg_str = f"{gio_chung}\\text{{ giờ}}"

        noidungcauhoi = ('''Hai dây chuyền đóng gói tự động cùng hoạt động thì hoàn thành một lô hàng xuất khẩu trong $%s$. Nếu cho từng dây chuyền hoạt động riêng lẻ thì dây chuyền thứ nhất hoàn thành lô hàng nhanh hơn dây chuyền thứ hai là $%s$ giờ. \\\\
a) Tính thời gian dây chuyền thứ nhất hoạt động một mình để hoàn thành xong lô hàng. \\\\
b) Tính thời gian dây chuyền thứ hai hoạt động một mình để hoàn thành xong lô hàng.'''
                         %(tg_str, latex(chenh)))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đổi $%s = \\frac{%s}{%s}$ giờ. Trong $1$ giờ, cả hai dây chuyền cùng làm được $\\frac{%s}{%s}$ lô hàng. \\\\
Gọi $x$ (giờ) là thời gian dây chuyền thứ nhất làm một mình xong lô hàng. Điều kiện: $x > 0$. \\\\
Thời gian dây chuyền thứ hai làm một mình xong lô hàng là $x + %s$ (giờ). \\\\
Trong $1$ giờ, dây chuyền thứ nhất làm được $\\frac{1}{x}$ lô hàng và dây chuyền thứ hai làm được $\\frac{1}{x + %s}$ lô hàng. \\\\
Theo đề bài, ta có phương trình: \\\\
$\\frac{1}{x} + \\frac{1}{x + %s} = \\frac{%s}{%s}$. \\\\
Quy đồng mẫu hai vế và khử mẫu, ta được phương trình bậc hai: \\\\
$%s = 0$. \\\\
Ta có: $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = %s$ (loại); \\quad $x_2 = %s$ (thoả mãn điều kiện). \\\\
Vậy dây chuyền thứ nhất làm một mình thì mất $%s$ giờ để hoàn thành lô hàng.
\\item Thời gian dây chuyền thứ hai làm một mình để hoàn thành xong lô hàng là: $%s + %s = %s$ (giờ).
\\end{enumEX}'''
                   %(tg_str, latex(mau_chung), latex(tu_chung), latex(tu_chung), latex(mau_chung),
                     latex(chenh), latex(chenh), latex(chenh), latex(tu_chung), latex(mau_chung),
                     latex(a_pt * x**2 + b_pt * x + c_pt),
                     latex(b_pt), latex(a_pt), latex(c_pt), latex(delta), latex(can_delta),
                     latex(nghiem_1), latex(t1), latex(t1),
                     latex(t1), latex(chenh), latex(t2)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
