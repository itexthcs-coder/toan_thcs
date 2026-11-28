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

def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        dec = (Decimal(val.numerator) / Decimal(val.denominator)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        s = format(dec.normalize(), 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')
    s = str(val)
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')
def bt_dang18_p3_b1_c9_hh8(self):
    # Dạng 18 (Thực tế): Ứng dụng tam giác đồng dạng trong thiết kế thang chữ A
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (Fraction(7, 5), Fraction(3, 5)),
            (Fraction(3, 2), Fraction(2, 5)),
            (Fraction(8, 5), Fraction(1, 2)),
            (Fraction(9, 5), Fraction(2, 3)),
            (Fraction(6, 5), Fraction(3, 4)),
            (Fraction(5, 4), Fraction(3, 5)),
            (Fraction(8, 5), Fraction(3, 4)),
            (Fraction(3, 2), Fraction(3, 5)),
        ]
        bc_val, r_val = random.choice(cases)
        mn_val = bc_val * r_val
        bc_s = fmt_num(bc_val)
        r_tex = '\\frac{%s}{%s}' % (r_val.numerator, r_val.denominator)
        kq_str = fmt_num(mn_val)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (1.5,3.0);\n'
            ' \\coordinate (B) at (0,0);\n'
            ' \\coordinate (C) at (3.0,0);\n'
            ' \\coordinate (M) at ($(A)!0.6!(B)$);\n'
            ' \\coordinate (N) at ($(A)!0.6!(C)$);\n'
            ' \\draw[line width=1pt] (B)--(A)--(C) (M)--(N);\n'
            ' \\draw[line width=1pt, dashed] (B)--(C);\n'
            ' \\fill (A) circle (1pt) node[above] {$A$};\n'
            ' \\fill (B) circle (1pt) node[below left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (M) circle (1pt) node[left] {$M$};\n'
            ' \\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Một chiếc thang chữ A khi mở ra tạo thành một tam giác cân có khoảng cách giữa hai chân thang chạm đất là $%s\\text{ m}$. Người ta gắn một thanh giằng ngang song song với mặt đất tại vị trí cách đỉnh thang một khoảng bằng $%s$ chiều dài cạnh bên của thang. Tính chiều dài thanh giằng ngang đó (đơn vị: mét).\\\\
%s''' % (bc_s, r_tex, tikz_code)
        )

        loigiai = (
            '''Mô hình hóa chiếc thang chữ A thành $\\Delta ABC$ cân tại $A$ với $BC = %s\\text{ m}$ là khoảng cách giữa hai chân thang và $MN$ là thanh giằng ngang ($M \\in AB, N \\in AC$).\\\\
Theo đề bài, thanh giằng ngang song song với mặt đất nên $MN // BC$ và vị trí gắn cách đỉnh thang một khoảng bằng $%s$ cạnh bên nên $\\frac{AM}{AB} = %s$.\\\\
Xét $\\Delta ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$), theo định lí về hai tam giác đồng dạng ta có $\\Delta AMN \\backsim \\Delta ABC$.\\\\
Suy ra tỉ số các cạnh tương ứng là:\\\\
$\\frac{MN}{BC} = \\frac{AM}{AB} = %s$.\\\\
Thay $BC = %s\\text{ m}$ vào hệ thức trên, ta được:\\\\
$MN = %s \\cdot %s = %s\\text{ (m)}$.\\\\
Vậy chiều dài thanh giằng ngang đó là $%s\\text{ m}$.''' % (
                bc_s, r_tex, r_tex,
                r_tex, bc_s, r_tex, bc_s, kq_str, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
