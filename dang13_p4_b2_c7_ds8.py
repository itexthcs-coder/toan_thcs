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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang13_p4_b2_c7_ds8(self):
    # Dạng 13: Giải bài toán tìm hai số nguyên dương qua tỉ số
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cases = [
            (3, 5, 12, 5, 7, 6),   # 18 và 30 -> +12 -> 30/42 = 5/7
            (2, 3, 10, 3, 4, 10),  # 20 và 30 -> +10 -> 30/40 = 3/4
            (3, 4, 15, 4, 5, 15),  # 45 và 60 -> +15 -> 60/75 = 4/5
            (2, 5, 14, 1, 2, 14),  # 28 và 70 -> +14 -> 42/84 = 1/2
            (4, 7, 18, 2, 3, 6)    # 24 và 42 -> +18 -> 42/60 = 7/10 (wait: (24+18)/(42+18)=42/60=7/10)
        ]
        clean_cases = [
            (3, 5, 12, 5, 7, 6),
            (2, 3, 10, 3, 4, 10),
            (3, 4, 15, 4, 5, 15),
            (2, 5, 14, 1, 2, 14),
            (4, 7, 18, 7, 10, 6)
        ]
        a, b, them, c, d, x_val = random.choice(clean_cases)
        so1 = a * x_val
        so2 = b * x_val
        
        noidungcauhoi = ('''Cho hai số nguyên dương có tỉ số bằng $\\frac{%s}{%s}$. Nếu cùng thêm $%s$ đơn vị vào cả hai số thì được hai số mới có tỉ số bằng $\\frac{%s}{%s}$. Tìm hai số nguyên dương ban đầu.'''
                         % (a, b, them, c, d))
        
        loigiai = ('''Gọi hai số nguyên dương ban đầu lần lượt là $%sx$ và $%sx$ (điều kiện: $x \\in \\mathbb{N}^*$). \\\\
Sau khi cùng thêm $%s$ đơn vị vào cả hai số, ta được hai số mới là $%sx + %s$ và $%sx + %s$. \\\\
Theo đề bài, tỉ số của hai số mới bằng $\\frac{%s}{%s}$ nên ta có phương trình: \\\\
$\\frac{%sx + %s}{%sx + %s} = \\frac{%s}{%s}$ \\\\
$\\Leftrightarrow %s(%sx + %s) = %s(%sx + %s)$ \\\\
$\\Leftrightarrow %sx + %s = %sx + %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy hai số nguyên dương ban đầu lần lượt là $%s \\cdot %s = %s$ và $%s \\cdot %s = %s$.'''
                   % (a, b,
                      them, a, them, b, them,
                      c, d,
                      a, them, b, them, c, d,
                      d, a, them, c, b, them,
                      d*a, d*them, c*b, c*them,
                      c*b - d*a, d*them - c*them, x_val,
                      a, x_val, so1, b, x_val, so2))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
