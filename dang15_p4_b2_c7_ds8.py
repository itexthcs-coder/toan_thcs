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


def bt_dang15_p4_b2_c7_ds8(self):
    # Dạng 15: Giải bài toán cấu tạo số tự nhiên có ba chữ số
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Số có 3 chữ số: 100*a + x (với x là số có 2 chữ số, 10 <= x <= 99)
        # Chuyển chữ số a xuống hàng đơn vị -> 10*x + a
        # Hiệu: (100*a + x) - (10*x + a) = 99*a - 9*x = 9(11*a - x)
        a = random.randint(3, 8)
        x_val = random.randint(12, min(95, 11 * a - 12))
        hieu = 99 * a - 9 * x_val
        so_bd = 100 * a + x_val
        
        noidungcauhoi = ('''Tìm một số tự nhiên có ba chữ số, biết chữ số hàng trăm là $%s$. Nếu chuyển chữ số $%s$ này xuống vị trí hàng đơn vị (giữ nguyên thứ tự hai chữ số còn lại) thì ta được một số mới nhỏ hơn số ban đầu là $%s$ đơn vị.'''
                         % (a, a, hieu))
        
        loigiai = ('''Gọi số tự nhiên có hai chữ số tạo bởi chữ số hàng chục và chữ số hàng đơn vị của số ban đầu là $x$ (điều kiện: $x \\in \\mathbb{N}$, $0 \\le x \\le 99$). \\\\
Khi đó số tự nhiên ban đầu là: $\\overline{%sx} = %s + x$. \\\\
Sau khi chuyển chữ số $%s$ xuống vị trí hàng đơn vị, ta được số mới là: $\\overline{x%s} = 10x + %s$. \\\\
Theo đề bài, số mới nhỏ hơn số ban đầu là $%s$ đơn vị nên ta có phương trình: \\\\
$(%s + x) - (10x + %s) = %s$ \\\\
$\\Leftrightarrow %s - 9x = %s$ \\\\
$\\Leftrightarrow 9x = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy số tự nhiên có ba chữ số ban đầu cần tìm là $%s$.'''
                   % (a, 100 * a,
                      a, a, a,
                      hieu,
                      100 * a, a, hieu,
                      99 * a, hieu,
                      99 * a - hieu, x_val,
                      so_bd))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
