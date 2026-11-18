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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang8_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m6, m7, m8, m9, m10 = 4, 9, 12, 7, 3
        n = 35
        f6 = str((Decimal(m6*100)/Decimal(n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        f7 = str((Decimal(m7*100)/Decimal(n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        f8 = str((Decimal(m8*100)/Decimal(n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        f9 = str((Decimal(m9*100)/Decimal(n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        f10 = str((Decimal(m10*100)/Decimal(n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinh_dt = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt, ->] (0,0) -- (6.0,0) node[right] {Điểm};\n'
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.2) node[above] {Số học sinh};\n'
            '\\foreach \\y/\\lbl in {1/4, 2/8, 3/12} {\n'
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (5.5,\\y);\n'
            '    \\node[left] at (0,\\y) {$\\lbl$};\n'
            '}\n'
            '\\foreach \\x/\\lbl in {1/6, 2/7, 3/8, 4/9, 5/10} {\n'
            '    \\node[below] at (\\x,0) {$\\lbl$};\n'
            '}\n'
            '\\draw[line width=1pt] (1,1.0) -- (2,2.25) -- (3,3.0) -- (4,1.75) -- (5,0.75);\n'
            '\\fill (1,1.0) circle (1pt) node[above left] {$4$};\n'
            '\\fill (2,2.25) circle (1pt) node[above left] {$9$};\n'
            '\\fill (3,3.0) circle (1pt) node[above] {$12$};\n'
            '\\fill (4,1.75) circle (1pt) node[above right] {$7$};\n'
            '\\fill (5,0.75) circle (1pt) node[above right] {$3$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Biểu đồ tần số dạng đoạn thẳng dưới đây ghi lại điểm kiểm tra $15$ phút môn Tiếng Anh của $35$ học sinh lớp 9G:%s'
            'a) Lập bảng tần số tương đối của dãy điểm số trên (làm tròn các kết quả đến hàng phần mười).\\\\ '
            'b) Tính tỉ lệ học sinh đạt điểm từ $8$ trở lên.'
        ) % (hinh_dt)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Cỡ mẫu $n = 35$. Tần số tương đối các mức điểm $6; 7; 8; 9; 10$ làm tròn đến hàng phần mười lần lượt là: $%s\\%%; %s\\%%; %s\\%%; %s\\%%; %s\\%%$.\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|c|}\n'
            '\\hline\n'
            'Điểm & $6$ & $7$ & $8$ & $9$ & $10$ \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Tỉ lệ học sinh đạt điểm từ $8$ trở lên là: $%s\\%% + %s\\%% + %s\\%% = 62,9\\%%$.\n'
            '\\end{enumEX}'
        ) % (f6, f7, f8, f9, f10, f6, f7, f8, f9, f10, f8, f9, f10)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
