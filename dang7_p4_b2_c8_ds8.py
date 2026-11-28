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


def bt_dang7_p4_b2_c8_ds8(self):
    # Dạng 7: Bài toán chuyển phần tử giữa hai hộp để cân bằng xác suất
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xanh1 = random.choice([8, 10, 12, 14])
        do1 = random.randint(2, xanh1 - 4)
        chuyen = xanh1 - do1
        do2 = chuyen + random.randint(2, 6)
        xanh2 = random.randint(3, 8)
        tong1_bd = xanh1 + do1

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (2.8,1.5);\n'
            '\\node at (1.4,1.0) {Hộp 1};\n'
            '\\node at (1.4,0.45) {$%s$ xanh, $%s$ đỏ};\n'
            '\\draw[line width=1pt] (4.8,0) rectangle (7.6,1.5);\n'
            '\\node at (6.2,1.0) {Hộp 2};\n'
            '\\node at (6.2,0.45) {$%s$ xanh, $%s$ đỏ};\n'
            '\\draw[->, line width=1pt] (4.8,0.75) -- (2.8,0.75) node[above, midway] {Chuyển $x$ bi đỏ};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (xanh1, do1, xanh2, do2)

        noidungcauhoi = (
            'Hộp thứ nhất chứa $%s$ viên bi xanh và $%s$ viên bi đỏ. Hộp thứ hai chứa $%s$ viên bi xanh và $%s$ viên bi đỏ (các viên bi có cùng kích thước và khối lượng). '
            'Cần chuyển bao nhiêu viên bi đỏ từ hộp thứ hai sang hộp thứ nhất để khi lấy ngẫu nhiên một viên bi từ hộp thứ nhất, xác suất lấy được viên bi đỏ bằng $\\frac{1}{2}$?%s'
        ) % (xanh1, do1, xanh2, do2, tikz_img)

        loigiai = (
            'Gọi số viên bi đỏ cần chuyển từ hộp thứ hai sang hộp thứ nhất là $x$ (viên, điều kiện: $x \\in \\mathbb{N}^*$, $x \\le %s$).\\\\\n'
            'Sau khi chuyển $x$ viên bi đỏ sang hộp thứ nhất:\\\\\n'
            '- Số viên bi đỏ ở hộp thứ nhất là $%s + x$ (viên).\\\\\n'
            '- Tổng số viên bi ở hộp thứ nhất là $%s + %s + x = %s + x$ (viên).\\\\\n'
            'Vì lấy ngẫu nhiên một viên bi từ hộp thứ nhất nên các kết quả có thể là đồng khả năng.\\\\\n'
            'Để xác suất lấy được viên bi đỏ từ hộp thứ nhất bằng $\\frac{1}{2}$, ta có phương trình:\\\\\n'
            '$\\frac{%s + x}{%s + x} = \\frac{1}{2}$\\\\\n'
            '$2(%s + x) = %s + x$\\\\\n'
            '$%s + 2x = %s + x$\\\\\n'
            '$2x - x = %s - %s$\\\\\n'
            '$x = %s$ (thỏa mãn điều kiện).\\\\\n'
            'Vậy cần chuyển $%s$ viên bi đỏ từ hộp thứ hai sang hộp thứ nhất.'
        ) % (
            do2, do1, xanh1, do1, tong1_bd,
            do1, tong1_bd,
            do1, tong1_bd,
            2 * do1, tong1_bd,
            tong1_bd, 2 * do1,
            chuyen, chuyen
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
