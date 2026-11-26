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


def bt_dang11_p4_b2_c7_ds8(self):
    # Dạng 11: Tìm tham số nguyên để phương trình bậc nhất có nghiệm nguyên dương
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.randint(2, 4)
        k = random.choice([4, 6])
        # (m + a)x - 3m + 1 = a*x + (1 + k) => m*x = 3m + k => x = 3 + k/m
        c_rhs = 1 + k
        
        # Tính các ước của k và kiểm tra x = 3 + k/m > 0
        uoc_list = []
        for u in range(-k, k + 1):
            if u != 0 and k % u == 0:
                uoc_list.append(u)
                
        nhan_list = []
        dong_giai = []
        for u in uoc_list:
            x_u = 3 + k // u
            if x_u > 0:
                nhan_list.append(str(u))
                dong_giai.append('- Với $m = %s \\Rightarrow x = 3 + \\frac{%s}{%s} = %s > 0$ (nhận).' % (u, k, u, x_u))
            else:
                dong_giai.append('- Với $m = %s \\Rightarrow x = 3 + \\frac{%s}{%s} = %s \\le 0$ (loại).' % (u, k, u, x_u))
                
        chi_tiet_uoc = ' \\\\\n'.join(dong_giai)
        tap_uoc_str = '; '.join([str(u) for u in uoc_list])
        tap_nhan_str = '; '.join(nhan_list)
        
        noidungcauhoi = ('''Tìm tất cả các giá trị nguyên của tham số $m$ để phương trình $(m + %s)x - 3m + 1 = %sx + %s$ có nghiệm duy nhất là một số nguyên dương.'''
                         % (a, a, c_rhs))
        
        loigiai = ('''Biến đổi phương trình đã cho về dạng cơ bản: \\\\
$(m + %s)x - 3m + 1 = %sx + %s$ \\\\
$\\Leftrightarrow (m + %s - %s)x = 3m + %s - 1$ \\\\
$\\Leftrightarrow mx = 3m + %s$. \\\\
Để phương trình có nghiệm duy nhất thì $m \\neq 0$. Khi đó nghiệm duy nhất của phương trình là: \\\\
$x = \\frac{3m + %s}{m} = 3 + \\frac{%s}{m}$. \\\\
Vì $m \\in \\mathbb{Z}$ nên để $x$ là số nguyên thì $\\frac{%s}{m} \\in \\mathbb{Z}$, suy ra $m \\in \\text{Ư}(%s) = \\{%s\\}$. \\\\
Kiểm tra điều kiện nghiệm nguyên dương ($x > 0$): \\\\
%s \\\\
Vậy các giá trị nguyên của tham số $m$ thỏa mãn yêu cầu bài toán là $m \\in \\{%s\\}$.'''
                   % (a, a, c_rhs,
                      a, a, c_rhs,
                      k,
                      k, k,
                      k, k, tap_uoc_str,
                      chi_tiet_uoc,
                      tap_nhan_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
