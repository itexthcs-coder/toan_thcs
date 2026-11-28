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


def bt_dang11_p4_b2_c8_ds8(self):
    # Dạng 11: Xác suất liên quan đến bất phương trình bậc nhất một ẩn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        N = random.choice([6, 7, 8, 9])
        a = random.choice([2, 3])
        k = random.randint(-2, 3)
        b = random.choice([-3, -2, -1, 1, 2, 3])
        c = a * k + b

        dau_b = '+' if b > 0 else '-'
        abs_b = abs(b)
        bpt_str = '%sm %s %s > %s' % (a, dau_b, abs_b, c)

        vals = list(range(-N, N + 1))
        tong_kq = len(vals)
        fav = [m for m in vals if m > k]
        so_tl = len(fav)
        f = frac(so_tl, tong_kq)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)
        fav_str = '; '.join([str(x) for x in fav])

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3.2,0) -- (3.2,0) node[below] {$m$};\n'
            '\\draw[line width=1pt] (-2.5,0.1) -- (-2.5,-0.1) node[below] {$-%s$};\n'
            '\\draw[line width=1pt] (0,0.1) -- (0,-0.1) node[below] {$0$};\n'
            '\\draw[line width=1pt] (2.5,0.1) -- (2.5,-0.1) node[below] {$%s$};\n'
            '\\node at (0,0.55) {Hộp gồm $%s$ quả cầu ghi số nguyên từ $-%s$ đến $%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (N, N, tong_kq, N, N)

        noidungcauhoi = (
            'Một hộp kín đựng $%s$ quả cầu giống hệt nhau được ghi các số nguyên từ $-%s$ đến $%s$. '
            'Lấy ngẫu nhiên một quả cầu trong hộp. Gọi $m$ là số ghi trên quả cầu lấy được. '
            'Tính xác suất của biến cố $B$: ``Giá trị của $m$ là nghiệm của bất phương trình $%s$\'\'.%s'
        ) % (tong_kq, N, N, bpt_str, tikz_img)

        loigiai = (
            'Hộp có $%s$ quả cầu giống hệt nhau nên khi lấy ngẫu nhiên một quả cầu thì có $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Giải bất phương trình $%s$:\\\\\n'
            '$%sm > %s %s %s$\\\\\n'
            '$%sm > %s$\\\\\n'
            '$m > %s$.\\\\\n'
            'Trong các số nguyên từ $-%s$ đến $%s$, các giá trị của $m$ thỏa mãn $m > %s$ là: $%s$.\\\\\n'
            'Do đó, có $%s$ kết quả thuận lợi cho biến cố $B$.\\\\\n'
            'Vậy xác suất của biến cố $B$ là: $P(B) = \\frac{%s}{%s} = %s$.'
        ) % (
            tong_kq, tong_kq,
            bpt_str,
            a, c, ('-' if b > 0 else '+'), abs_b,
            a, c - b,
            k,
            N, N, k, fav_str,
            so_tl,
            so_tl, tong_kq, xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
