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


def bt_dang4_p4_b2_c8_ds8(self):
    # Dạng 4: Bài toán gieo hai con xúc xắc cân đối (tính tổng số chấm)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        sub_type = random.choice(['nguyen_to', 'chia_het_3', 'lon_hon_8'])
        pairs = []
        if sub_type == 'nguyen_to':
            dk_text = 'Tổng số chấm xuất hiện trên hai con xúc xắc là một số nguyên tố'
            primes = {2, 3, 5, 7, 11}
            for i in range(1, 7):
                for j in range(1, 7):
                    if (i + j) in primes:
                        pairs.append((i, j))
            giai_thich_dk = 'Các số nguyên tố có thể là tổng số chấm của hai con xúc xắc (từ $2$ đến $12$) là: $2; 3; 5; 7; 11$.'
        elif sub_type == 'chia_het_3':
            dk_text = 'Tổng số chấm xuất hiện trên hai con xúc xắc chia hết cho $3$'
            for i in range(1, 7):
                for j in range(1, 7):
                    if (i + j) % 3 == 0:
                        pairs.append((i, j))
            giai_thich_dk = 'Các số chia hết cho $3$ có thể là tổng số chấm của hai con xúc xắc (từ $2$ đến $12$) là: $3; 6; 9; 12$.'
        else:
            dk_text = 'Tổng số chấm xuất hiện trên hai con xúc xắc lớn hơn $8$'
            for i in range(1, 7):
                for j in range(1, 7):
                    if (i + j) > 8:
                        pairs.append((i, j))
            giai_thich_dk = 'Các giá trị tổng số chấm lớn hơn $8$ (từ $2$ đến $12$) là: $9; 10; 11; 12$.'

        so_tl = len(pairs)
        f = frac(so_tl, 36)
        xs_str = '\\frac{%s}{%s}' % (f.numerator, f.denominator)
        pairs_str = '; '.join(['(%s; %s)' % (a, b) for a, b in pairs])

        tikz_img = (
            '\\\\\n'
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (1.4,1.4);\n'
            '\\draw[line width=1pt] (1.4,1.4) -- (1.9,1.9) -- (0.5,1.9) -- (0,1.4);\n'
            '\\draw[line width=1pt] (1.4,0) -- (1.9,0.5) -- (1.9,1.9);\n'
            '\\fill (0.7,0.7) circle (1.5pt);\n'
            '\\node at (0.7,-0.45) {Xúc xắc 1};\n'
            '\\begin{scope}[xshift=3.2cm]\n'
            '\\draw[line width=1pt] (0,0) rectangle (1.4,1.4);\n'
            '\\draw[line width=1pt] (1.4,1.4) -- (1.9,1.9) -- (0.5,1.9) -- (0,1.4);\n'
            '\\draw[line width=1pt] (1.4,0) -- (1.9,0.5) -- (1.9,1.9);\n'
            '\\fill (0.4,0.4) circle (1.5pt) (1.0,1.0) circle (1.5pt);\n'
            '\\node at (0.7,-0.45) {Xúc xắc 2};\n'
            '\\end{scope}\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Gieo đồng thời hai con xúc xắc cân đối, đồng chất (một con màu xanh, một con màu đỏ) và quan sát số chấm xuất hiện trên mặt của mỗi con. '
            'Tính xác suất của biến cố $A$: ``%s\'\'.%s'
        ) % (dk_text, tikz_img)

        loigiai = (
            'Mỗi con xúc xắc có $6$ mặt được đánh số chấm từ $1$ đến $6$. Khi gieo đồng thời hai con xúc xắc cân đối, đồng chất, '
            'mỗi kết quả có thể là một cặp số $(a; b)$, trong đó $a$ là số chấm trên con xúc xắc màu xanh và $b$ là số chấm trên con xúc xắc màu đỏ ($a, b \\in \\{1; 2; 3; 4; 5; 6\\}$).\\\\\n'
            'Tổng số kết quả có thể là $6 \\cdot 6 = 36$ kết quả và các kết quả này là đồng khả năng.\\\\\n'
            '%s\\\\\n'
            'Các kết quả thuận lợi cho biến cố $A$ là: $%s$.\\\\\n'
            'Như vậy, có $%s$ kết quả thuận lợi cho biến cố $A$.\\\\\n'
            'Vậy xác suất của biến cố $A$ là: $P(A) = \\frac{%s}{36} = %s$.'
        ) % (giai_thich_dk, pairs_str, so_tl, so_tl, xs_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
