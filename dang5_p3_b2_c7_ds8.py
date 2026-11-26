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


def bt_dang5_p3_b2_c7_ds8(self):
    # Dạng 5: Giải bài toán bằng cách lập phương trình - Dạng tìm phân số
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cases = [
            (11, 3, 4, 3, 4),
            (9, 2, 3, 2, 3),
            (13, 4, 2, 4, 5),
            (10, 5, 1, 3, 4),
            (15, 3, 5, 5, 6)
        ]
        d, a, b, p, q = random.choice(cases)
        x_val = (p * (d - b) - q * a) // (q - p)
        mau_val = x_val + d
        tong = x_val + mau_val
        kq_str = str(tong)
        
        noidungcauhoi = ('''Một phân số có tử số bé hơn mẫu số là $%s$ đơn vị. Nếu tăng tử số thêm $%s$ đơn vị và giảm mẫu số đi $%s$ đơn vị thì được một phân số mới có giá trị bằng $\\frac{%s}{%s}$. Tính tổng của tử số và mẫu số của phân số ban đầu.'''
                         % (d, a, b, p, q))
        
        loigiai = ('''Gọi tử số của phân số ban đầu là $x$ ($x \\in \\mathbb{Z}$, $x \\neq %s$). \\\\
Vì tử số bé hơn mẫu số là $%s$ đơn vị nên mẫu số của phân số ban đầu là $x + %s$. \\\\
Sau khi tăng tử số thêm $%s$ đơn vị và giảm mẫu số đi $%s$ đơn vị, ta được phân số mới là $\\frac{x + %s}{x + %s}$. \\\\
Theo đề bài, ta có phương trình: \\\\
$\\frac{x + %s}{x + %s} = \\frac{%s}{%s}$ \\\\
$\\Leftrightarrow %s(x + %s) = %s(x + %s)$ \\\\
$\\Leftrightarrow %sx + %s = %sx + %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Do đó tử số ban đầu là $%s$ và mẫu số ban đầu là $%s + %s = %s$. \\\\
Vậy tổng của tử số và mẫu số của phân số ban đầu là $%s + %s = %s$.'''
                   % (b - d, d, d, a, b, a, d - b,
                      a, d - b, p, q,
                      q, a, p, d - b,
                      q, q*a, p, p*(d - b),
                      q - p, p*(d - b) - q*a, x_val,
                      x_val, x_val, d, mau_val,
                      x_val, mau_val, tong))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
