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


def bt_dang1_p4_b2_c8_ds8(self):
    # Dạng 1: Tìm số phần tử ban đầu qua bài toán thêm bớt hai đối tượng (lập phương trình)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            tong_bd = random.choice([20, 24, 25, 28, 30, 32, 35, 36])
            den_bd = random.randint(6, tong_bd - 6)
            trang_bd = tong_bd - den_bd
            bot_trang = random.randint(2, trang_bd - 2)
            them_den = random.randint(2, 8)
            tong_sau = tong_bd - bot_trang + them_den
            den_sau = den_bd + them_den
            if tong_sau > 0 and 0 < den_sau < tong_sau:
                f = frac(den_sau, tong_sau)
                if f.denominator <= 10:
                    break

        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)
        vt_hs = f.denominator
        vt_const = them_den * f.denominator
        vp_const = f.numerator * tong_sau

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (3.6,1.6);\n'
            '\\draw[line width=1pt] (0,1.6) -- (-0.4,2.1) (3.6,1.6) -- (4.0,2.1);\n'
            '\\node at (1.8,1.0) {Thùng hàng: $%s$ áo};\n'
            '\\node at (1.8,0.45) {Trắng và Đen};\n'
            '\\draw[->, line width=1pt] (4.3,1.1) -- (5.5,1.1) node[above, midway] {$-%s$ trắng};\n'
            '\\draw[->, line width=1pt] (4.3,0.4) -- (5.5,0.4) node[below, midway] {$+%s$ đen};\n'
            '\\draw[line width=1pt] (5.8,0) rectangle (9.6,1.6);\n'
            '\\node at (7.7,1.0) {Sau thay đổi: $%s$ áo};\n'
            '\\node at (7.7,0.45) {$P(\\text{Đen}) = %s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (tong_bd, bot_trang, them_den, tong_sau, xs_str)

        noidungcauhoi = (
            'Một thùng hàng có $%s$ chiếc áo gồm hai màu trắng và đen. Người quản lý lấy ra $%s$ chiếc áo trắng và bỏ thêm vào $%s$ chiếc áo đen. '
            'Sau đó, một nhân viên lấy ngẫu nhiên một chiếc áo từ thùng thì thấy xác suất lấy được áo đen là $%s$. '
            'Hỏi lúc đầu trong thùng có bao nhiêu chiếc áo mỗi loại?%s'
        ) % (tong_bd, bot_trang, them_den, xs_str, tikz_img)

        loigiai = (
            'Gọi số chiếc áo đen lúc đầu trong thùng là $x$ (chiếc, điều kiện: $x \\in \\mathbb{N}^*$, $x < %s$).\\\\\n'
            'Khi đó, số chiếc áo trắng lúc đầu trong thùng là $%s - x$ (chiếc).\\\\\n'
            'Sau khi lấy ra $%s$ chiếc áo trắng và bỏ thêm vào $%s$ chiếc áo đen:\\\\\n'
            '- Số chiếc áo đen trong thùng lúc sau là $x + %s$ (chiếc).\\\\\n'
            '- Tổng số chiếc áo trong thùng lúc sau là $%s - %s + %s = %s$ (chiếc).\\\\\n'
            'Vì lấy ngẫu nhiên một chiếc áo từ thùng nên các kết quả có thể là đồng khả năng.\\\\\n'
            'Theo đề bài, xác suất lấy được chiếc áo đen lúc sau là $%s$, nên ta có phương trình:\\\\\n'
            '$\\frac{x + %s}{%s} = %s$\\\\\n'
            '$%s(x + %s) = %s \\cdot %s$\\\\\n'
            '$%sx + %s = %s$\\\\\n'
            '$%sx = %s$\\\\\n'
            '$x = %s$ (thỏa mãn điều kiện).\\\\\n'
            'Vậy lúc đầu trong thùng có $%s$ chiếc áo đen và $%s - %s = %s$ chiếc áo trắng.'
        ) % (
            tong_bd, tong_bd, bot_trang, them_den, them_den,
            tong_bd, bot_trang, them_den, tong_sau,
            xs_str, them_den, tong_sau, xs_str,
            vt_hs, them_den, f.numerator, tong_sau,
            vt_hs, vt_const, vp_const,
            vt_hs, vp_const - vt_const,
            den_bd, den_bd, tong_bd, den_bd, trang_bd
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
