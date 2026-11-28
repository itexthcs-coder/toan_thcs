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


def bt_dang9_p4_b2_c8_ds8(self):
    # Dạng 9: Bài toán chọn ngẫu nhiên có điều kiện ràng buộc về tỉ số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            a, b = random.choice([(2, 3), (3, 4), (2, 5), (3, 5)])
            c, d = random.choice([(3, 5), (2, 5), (3, 4), (4, 5)])
            tu = b * c
            mau = a * d
            g = math.gcd(tu, mau)
            tu //= g
            mau //= g
            if tu != mau:
                k = random.choice([2, 3])
                hs7 = tu * k
                hs8 = mau * k
                tong = hs7 + hs8
                break

        f = frac(hs8, tong)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (6.6,1.2);\n'
            '\\draw[line width=1pt] (3.1,0) -- (3.1,1.2);\n'
            '\\node at (1.55,0.6) {Khối 7 ($x$ HS)};\n'
            '\\node at (4.85,0.6) {Khối 8 ($%s - x$ HS)};\n'
            '\\node at (3.3,-0.4) {Câu lạc bộ cờ vua: $%s$ thành viên};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (tong, tong)

        noidungcauhoi = (
            'Trong một câu lạc bộ cờ vua có $%s$ thành viên gồm học sinh khối 7 và khối 8. '
            'Biết rằng $\\frac{%s}{%s}$ số học sinh khối 7 bằng $\\frac{%s}{%s}$ số học sinh khối 8. '
            'Chọn ngẫu nhiên một thành viên của câu lạc bộ làm đội trưởng. Tính xác suất để người được chọn là học sinh khối 8.%s'
        ) % (tong, a, b, c, d, tikz_img)

        loigiai = (
            'Gọi số học sinh khối 7 trong câu lạc bộ là $x$ (học sinh, điều kiện: $x \\in \\mathbb{N}^*$, $x < %s$).\\\\\n'
            'Khi đó, số học sinh khối 8 trong câu lạc bộ là $%s - x$ (học sinh).\\\\\n'
            'Theo đề bài, $\\frac{%s}{%s}$ số học sinh khối 7 bằng $\\frac{%s}{%s}$ số học sinh khối 8 nên ta có phương trình:\\\\\n'
            '$\\frac{%s}{%s}x = \\frac{%s}{%s}(%s - x)$\\\\\n'
            '$%s \\cdot %s x = %s \\cdot %s(%s - x)$\\\\\n'
            '$%sx = %s(%s - x)$\\\\\n'
            '$%sx = %s - %sx$\\\\\n'
            '$%sx = %s$\\\\\n'
            '$x = %s$ (thỏa mãn điều kiện).\\\\\n'
            'Suy ra số học sinh khối 8 là $%s - %s = %s$ (học sinh).\\\\\n'
            'Khi chọn ngẫu nhiên một thành viên trong $%s$ thành viên của câu lạc bộ thì có $%s$ kết quả có thể và các kết quả này là đồng khả năng.\\\\\n'
            'Do có $%s$ kết quả thuận lợi nên xác suất để người được chọn là học sinh khối 8 là: $P = \\frac{%s}{%s} = %s$.'
        ) % (
            tong, tong,
            a, b, c, d,
            a, b, c, d, tong,
            a, d, b, c, tong,
            a * d, b * c, tong,
            a * d, b * c * tong, b * c,
            a * d + b * c, b * c * tong,
            hs7,
            tong, hs7, hs8,
            tong, tong,
            hs8, hs8, tong, xs_str
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
