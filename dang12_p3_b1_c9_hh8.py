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
def bt_dang12_p3_b1_c9_hh8(self):
    # Dạng 12: Hai đường thẳng song song cắt hai cạnh tam giác tạo thành nhiều lớp đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = 3 * random.randint(4, 15)
        mn = bc // 3
        pq = 2 * mn
        tong = mn + pq
        kq_str = str(tong)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (1.5,3.0);\n'
            ' \\coordinate (B) at (0,0);\n'
            ' \\coordinate (C) at (3.6,0);\n'
            ' \\coordinate (M) at ($(A)!0.333!(B)$);\n'
            ' \\coordinate (P) at ($(A)!0.667!(B)$);\n'
            ' \\coordinate (N) at ($(A)!0.333!(C)$);\n'
            ' \\coordinate (Q) at ($(A)!0.667!(C)$);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (P)--(Q);\n'
            ' \\fill (A) circle (1pt) node[above] {$A$};\n'
            ' \\fill (B) circle (1pt) node[below left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (M) circle (1pt) node[left] {$M$};\n'
            ' \\fill (P) circle (1pt) node[left] {$P$};\n'
            ' \\fill (N) circle (1pt) node[right] {$N$};\n'
            ' \\fill (Q) circle (1pt) node[right] {$Q$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho $\\Delta ABC$ có $BC = %s\\text{ cm}$. Trên cạnh $AB$ lấy hai điểm $M, P$ sao cho $AM = MP = PB$. Qua $M$ và $P$ kẻ các đường thẳng song song với $BC$ cắt $AC$ lần lượt tại $N$ và $Q$. Tính tổng độ dài $MN + PQ$ (đơn vị: cm).\\\\
%s''' % (bc, tikz_code)
        )

        loigiai = (
            '''Vì $AM = MP = PB$ và $M, P$ nằm trên đoạn thẳng $AB$ nên ta có $\\frac{AM}{AB} = \\frac{1}{3}$ và $\\frac{AP}{AB} = \\frac{2}{3}$.\\\\
Xét $\\Delta ABC$ có $MN // BC$ ($M \\in AB, N \\in AC$), theo định lí về hai tam giác đồng dạng ta có $\\Delta AMN \\backsim \\Delta ABC$.\\\\
Suy ra $\\frac{MN}{BC} = \\frac{AM}{AB} = \\frac{1}{3} \\Rightarrow MN = \\frac{1}{3} \\cdot %s = %s\\text{ (cm)}$.\\\\
Tương tự, xét $\\Delta ABC$ có $PQ // BC$ ($P \\in AB, Q \\in AC$), theo định lí về hai tam giác đồng dạng ta có $\\Delta APQ \\backsim \\Delta ABC$.\\\\
Suy ra $\\frac{PQ}{BC} = \\frac{AP}{AB} = \\frac{2}{3} \\Rightarrow PQ = \\frac{2}{3} \\cdot %s = %s\\text{ (cm)}$.\\\\
Vậy tổng độ dài hai đoạn thẳng là:\\\\
$MN + PQ = %s + %s = %s\\text{ (cm)}$.''' % (
                bc, mn, bc, pq, mn, pq, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
