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


def bt_dang19_p4_b2_c8_ds8(self):
    # Dạng 19: Bài toán thêm đồng thời một số lượng phần tử chưa biết vào cả hai loại
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            xanh_bd = random.choice([6, 8, 9, 10, 12])
            vang_bd = random.choice([10, 12, 14, 15, 16])
            he_so = random.choice([2, 3])
            x_them = random.randint(2, 6)
            v_them = he_so * x_them
            tong_sau = xanh_bd + vang_bd + x_them + v_them
            xanh_sau = xanh_bd + x_them
            f = frac(xanh_sau, tong_sau)
            if f.denominator <= 30 and f.numerator != f.denominator:
                break

        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)
        tong_bd = xanh_bd + vang_bd
        he_so_tong = 1 + he_so
        ten_gap = 'gấp đôi' if he_so == 2 else 'gấp ba'

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (3.4,1.5);\n'
            '\\node at (1.7,1.0) {Bình ban đầu};\n'
            '\\node at (1.7,0.45) {$%s$ xanh, $%s$ vàng};\n'
            '\\draw[->, line width=1pt] (3.7,0.75) -- (5.5,0.75) node[above, midway] {$+x$ xanh} node[below, midway] {$+%sx$ vàng};\n'
            '\\draw[line width=1pt] (5.8,0) rectangle (9.2,1.5);\n'
            '\\node at (7.5,1.0) {Bình lúc sau};\n'
            '\\node at (7.5,0.45) {$P(\\text{Xanh}) = %s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (xanh_bd, vang_bd, he_so, xs_str)

        noidungcauhoi = (
            'Một bình đựng $%s$ viên bi xanh và $%s$ viên bi vàng (các viên bi có cùng kích thước và khối lượng). '
            'Người ta bỏ thêm vào bình một số viên bi xanh và một số viên bi vàng sao cho số viên bi vàng bỏ thêm %s số viên bi xanh bỏ thêm. '
            'Sau khi bỏ thêm, lấy ngẫu nhiên một viên bi từ bình thì xác suất lấy được viên bi xanh là $%s$. '
            'Hỏi người ta đã bỏ thêm vào bình bao nhiêu viên bi mỗi loại?%s'
        ) % (xanh_bd, vang_bd, ten_gap, xs_str, tikz_img)

        loigiai = (
            'Gọi số viên bi xanh bỏ thêm vào bình là $x$ (viên, điều kiện: $x \\in \\mathbb{N}^*$).\\\\\n'
            'Khi đó, số viên bi vàng bỏ thêm vào bình là $%sx$ (viên).\\\\\n'
            'Sau khi bỏ thêm:\\\\\n'
            '- Số viên bi xanh trong bình là $%s + x$ (viên).\\\\\n'
            '- Tổng số viên bi trong bình là $%s + %s + x + %sx = %s + %sx$ (viên).\\\\\n'
            'Vì lấy ngẫu nhiên một viên bi từ bình nên các kết quả có thể là đồng khả năng.\\\\\n'
            'Theo đề bài, xác suất lấy được viên bi xanh lúc sau là $%s$ nên ta có phương trình:\\\\\n'
            '$\\frac{%s + x}{%s + %sx} = %s$\\\\\n'
            '$%s(%s + x) = %s(%s + %sx)$\\\\\n'
            '$%s + %sx = %s + %sx$\\\\\n'
            '$%sx = %s$\\\\\n'
            '$x = %s$ (thỏa mãn điều kiện).\\\\\n'
            'Suy ra số viên bi vàng bỏ thêm vào bình là $%s \\cdot %s = %s$ (viên).\\\\\n'
            'Vậy người ta đã bỏ thêm vào bình $%s$ viên bi xanh và $%s$ viên bi vàng.'
        ) % (
            he_so, xanh_bd,
            xanh_bd, vang_bd, he_so, tong_bd, he_so_tong,
            xs_str,
            xanh_bd, tong_bd, he_so_tong, xs_str,
            f.denominator, xanh_bd, f.numerator, tong_bd, he_so_tong,
            f.denominator * xanh_bd, f.denominator, f.numerator * tong_bd, f.numerator * he_so_tong,
            f.denominator - f.numerator * he_so_tong, f.numerator * tong_bd - f.denominator * xanh_bd,
            x_them,
            he_so, x_them, v_them,
            x_them, v_them
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
