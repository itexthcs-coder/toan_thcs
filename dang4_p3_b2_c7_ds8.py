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


def bt_dang4_p3_b2_c7_ds8(self):
    # Dạng 4: Giải bài toán bằng cách lập phương trình - Dạng cấu tạo số tự nhiên
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        nice_cases = [
            (1, 5, 4, 17, 5),
            (2, 4, 2, 7, 4),
            (1, 8, 7, 9, 2),
            (2, 7, 5, 8, 3),
            (3, 6, 3, 7, 4),
            (4, 8, 4, 7, 4)
        ]
        chuc, donvi, hieu, tu, mau = random.choice(nice_cases)
        so_bd = 10 * chuc + donvi
        kq_str = str(so_bd)
        
        noidungcauhoi = ('''Tìm một số tự nhiên có hai chữ số, biết rằng chữ số hàng đơn vị lớn hơn chữ số hàng chục là $%s$ đơn vị và nếu đổi chỗ hai chữ số cho nhau thì được số mới bằng $\\frac{%s}{%s}$ số ban đầu.'''
                         % (hieu, tu, mau))
        
        loigiai = ('''Gọi chữ số hàng chục của số tự nhiên cần tìm là $x$ ($x \\in \\mathbb{N}^*$, $1 \\le x \\le %s$). \\\\
Khi đó chữ số hàng đơn vị là $x + %s$. \\\\
Số tự nhiên ban đầu là: $\\overline{x(x+%s)} = 10x + x + %s = 11x + %s$. \\\\
Nếu đổi chỗ hai chữ số cho nhau thì được số mới là: $10(x + %s) + x = 11x + %s$. \\\\
Theo đề bài, số mới bằng $\\frac{%s}{%s}$ số ban đầu nên ta có phương trình: \\\\
$11x + %s = \\frac{%s}{%s}(11x + %s)$ \\\\
$\\Leftrightarrow %s(11x + %s) = %s(11x + %s)$ \\\\
$\\Leftrightarrow %sx + %s = %sx + %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy số tự nhiên ban đầu cần tìm là $%s$.'''
                   % (9 - hieu, hieu, hieu, hieu, hieu,
                      hieu, 10*hieu,
                      tu, mau,
                      10*hieu, tu, mau, hieu,
                      mau, 10*hieu, tu, hieu,
                      11*mau, 10*hieu*mau, 11*tu, tu*hieu,
                      11*(tu - mau), 10*hieu*mau - tu*hieu, chuc,
                      so_bd))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
