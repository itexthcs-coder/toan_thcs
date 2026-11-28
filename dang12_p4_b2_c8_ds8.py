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


def bt_dang12_p4_b2_c8_ds8(self):
    # Dạng 12: Xác suất kết hợp điều kiện tạo thành ba cạnh của một tam giác
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        lengths = random.choice([
            [2, 3, 4, 5, 6],
            [2, 4, 5, 7, 9],
            [3, 4, 5, 7, 8],
            [2, 3, 5, 6, 8]
        ])
        all_triples = []
        valid_triples = []
        n = len(lengths)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = lengths[i], lengths[j], lengths[k]
                    all_triples.append((a, b, c))
                    if a + b > c:
                        valid_triples.append((a, b, c))

        tong_kq = len(all_triples)
        so_tl = len(valid_triples)
        f = frac(so_tl, tong_kq)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)

        len_str = '; '.join(['%s\\text{ cm}' % x for x in lengths])
        all_str = '; '.join(['(%s; %s; %s)' % t for t in all_triples])
        val_str = '; '.join(['(%s; %s; %s)' % t for t in valid_triples])

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,1.2) -- (1.2,1.2) node[right] {$%s\\text{ cm}$};\n'
            '\\draw[line width=1pt] (0,0.9) -- (1.8,0.9) node[right] {$%s\\text{ cm}$};\n'
            '\\draw[line width=1pt] (0,0.6) -- (2.4,0.6) node[right] {$%s\\text{ cm}$};\n'
            '\\draw[line width=1pt] (0,0.3) -- (3.0,0.3) node[right] {$%s\\text{ cm}$};\n'
            '\\draw[line width=1pt] (0,0.0) -- (3.6,0.0) node[right] {$%s\\text{ cm}$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (lengths[0], lengths[1], lengths[2], lengths[3], lengths[4])

        noidungcauhoi = (
            'Có $5$ thanh gỗ thẳng có độ dài lần lượt là $%s$. '
            'Lấy ngẫu nhiên đồng thời $3$ thanh gỗ từ $5$ thanh gỗ trên. Tính xác suất để $3$ thanh gỗ lấy ra có thể ghép thành một tam giác.%s'
        ) % (len_str, tikz_img)

        loigiai = (
            'Các bộ ba độ dài của $3$ thanh gỗ có thể lấy ra từ $5$ thanh gỗ đã cho là:\\\\\n'
            '$%s$.\\\\\n'
            'Có tất cả $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Ba đoạn thẳng ghép thành một tam giác khi và chỉ khi tổng độ dài hai đoạn thẳng bất kì lớn hơn độ dài đoạn thẳng còn lại (hay tổng hai cạnh nhỏ hơn lớn hơn cạnh lớn nhất).\\\\\n'
            'Kiểm tra các bộ ba trên, các bộ ba thỏa mãn bất đẳng thức tam giác là:\\\\\n'
            '$%s$.\\\\\n'
            'Do đó, có $%s$ kết quả thuận lợi cho biến cố $3$ thanh gỗ lấy ra ghép thành một tam giác.\\\\\n'
            'Vậy xác suất cần tìm là: $P = \\frac{%s}{%s} = %s$.'
        ) % (all_str, tong_kq, val_str, so_tl, so_tl, tong_kq, xs_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
