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


def bt_dang2_p4_b2_c8_ds8(self):
    # Dạng 2: Tìm tham số trong dãy số tự nhiên liên tiếp thỏa mãn điều kiện chia hết
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d = random.choice([3, 4, 5, 6])
        k = random.choice([3, 4, 5])
        n = d * k
        xs_str = '\\frac{1}{%s}' % d
        boi_list = [str(d * i) for i in range(1, k + 1)]
        boi_str = '; '.join(boi_list)
        gioi_han_duoi = d * (k - 1)
        gioi_han_tren = d * (k + 1)

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\foreach \\i/\\txt in {0/$1$, 1.3/$2$, 2.6/$3$, 3.9/$\\dots$, 5.2/$n$}{\n'
            '  \\draw[line width=1pt] (\\i,0) rectangle (\\i+1.0,1.3);\n'
            '  \\node at (\\i+0.5,0.65) {\\txt};\n'
            '}\n'
            '\\node at (3.1,-0.45) {Hộp gồm $n$ tấm thẻ ($%s < n < %s$)};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (gioi_han_duoi, gioi_han_tren)

        noidungcauhoi = (
            'Viết các số tự nhiên liên tiếp từ $1$ đến $n$ ($%s < n < %s$) lên $n$ tấm thẻ giống hệt nhau rồi bỏ vào hộp. '
            'Rút ngẫu nhiên một tấm thẻ từ hộp. Biết rằng xác suất để rút được tấm thẻ ghi số chia hết cho $%s$ là $%s$. '
            'Tìm giá trị của $n$.%s'
        ) % (gioi_han_duoi, gioi_han_tren, d, xs_str, tikz_img)

        loigiai = (
            'Từ $1$ đến $n$ có $n$ số tự nhiên nên khi rút ngẫu nhiên một tấm thẻ từ hộp thì có $n$ kết quả có thể. '
            'Vì các tấm thẻ giống hệt nhau nên $n$ kết quả có thể này là đồng khả năng.\\\\\n'
            'Vì $%s < n < %s$, các số tự nhiên từ $1$ đến $n$ chia hết cho $%s$ là: $%s$.\\\\\n'
            'Do đó, có $%s$ kết quả thuận lợi cho biến cố rút được tấm thẻ ghi số chia hết cho $%s$.\\\\\n'
            'Xác suất để rút được tấm thẻ ghi số chia hết cho $%s$ là $\\frac{%s}{n}$.\\\\\n'
            'Theo đề bài, ta có: $\\frac{%s}{n} = %s$, suy ra $n = %s \\cdot %s = %s$ (thỏa mãn điều kiện $%s < n < %s$).\\\\\n'
            'Vậy $n = %s$.'
        ) % (
            gioi_han_duoi, gioi_han_tren, d, boi_str,
            k, d, d, k,
            k, xs_str, k, d, n, gioi_han_duoi, gioi_han_tren,
            n
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
