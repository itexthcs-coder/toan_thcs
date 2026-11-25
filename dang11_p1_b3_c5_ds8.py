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

def bt_dang11_p1_b3_c5_ds8(self):
    # Dạng 11: Phát hiện sự phóng đại chênh lệch do gốc trục đứng khác 0
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        g0 = random.choice([200, 400, 500, 800])
        d1 = random.choice([10, 15, 20])
        k = random.choice([2, 3, 4])
        v1 = g0 + d1
        v2 = g0 + k * d1
        
        da = 'người vẽ đã đặt gốc trục đứng bắt đầu tại $%s$ thay vì $0$' % g0
        s_pool = [
            'doanh số tháng $11$ thực sự cao gấp $%s$ lần doanh số tháng $10$' % k,
            'chiều rộng của cột tháng $11$ được vẽ lớn hơn cột tháng $10$',
            'trục ngang không ghi đúng thứ tự thời gian của các tháng'
        ]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        # Vẽ biểu đồ cột gốc g0 -> chiều cao cột 1 là 1.0, cột 2 là k * 1.0
        h1 = 1.0
        h2 = float(k)
        ymax = h2 + 0.8
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Tháng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,%s) node[left] {Số chiếc};\n' % ymax +
            '\\node[left] at (0,0) {$%s$};\n' % g0 +
            '\\draw[line width=1pt, dashed] (0,1) -- (4.2,1);\n' +
            '\\node[left] at (0,1) {$%s$};\n' % v1 +
            '\\draw[line width=1pt, dashed] (0,%s) -- (4.2,%s);\n' % (h2, h2) +
            '\\node[left] at (0,%s) {$%s$};\n' % (h2, v2) +
            '\\draw[line width=1pt, fill=black!15] (0.8,0) rectangle (1.8,1.0);\n' +
            '\\node[above] at (1.3,1.0) {$%s$};\n' % v1 +
            '\\node[below] at (1.3,0) {Tháng $10$};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,0) rectangle (3.6,%s);\n' % h2 +
            '\\node[above] at (3.1,%s) {$%s$};\n' % (h2, v2) +
            '\\node[below] at (3.1,0) {Tháng $11$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một cửa hàng quảng cáo doanh số bán điện thoại tháng $10$ là $%s$ chiếc và tháng $11$ là $%s$ chiếc bằng biểu đồ cột sau:\n' % (v1, v2) +
                         tikz_code + '\n' +
                         'Nhìn vào biểu đồ, cột tháng $11$ cao gấp $%s$ lần cột tháng $10$. Nguyên nhân của hiện tượng này là do' % k)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Trên thực tế, tỉ số doanh số giữa tháng $11$ và tháng $10$ là $\\dfrac{%s}{%s} \\neq %s$.\\\\' +
                   'Tuy nhiên, do người vẽ đặt gốc của trục đứng tại $%s$ (khác $0$) nên chiều cao cột tháng $10$ tỉ lệ với $%s - %s = %s$ và chiều cao cột tháng $11$ tỉ lệ với $%s - %s = %s$, làm cột tháng $11$ cao gấp $%s$ lần cột tháng $10$.\\\\' +
                   'Vậy nguyên nhân là do %s.'
                   ) % (v2, v1, k, g0, v1, g0, d1, v2, g0, k * d1, k, da)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
