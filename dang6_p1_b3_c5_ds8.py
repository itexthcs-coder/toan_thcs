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

def bt_dang6_p1_b3_c5_ds8(self):
    # Dạng 6: Đọc số liệu trực tiếp trên biểu đồ cột
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        days = ['Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']
        vals = random.sample([140, 180, 220, 260, 310, 350, 390, 420], 4)
        
        idx_max = vals.index(max(vals))
        da = days[idx_max]
        
        s_pool = [days[i] for i in range(4) if i != idx_max]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        # Tọa độ cột tỉ lệ với 500 -> chiều cao max ~ 4.2 cm
        h0 = round(vals[0] / 100.0, 2)
        h1 = round(vals[1] / 100.0, 2)
        h2 = round(vals[2] / 100.0, 2)
        h3 = round(vals[3] / 100.0, 2)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (7.2,0) node[below] {Ngày};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,5.2) node[left] {Số vé};\n' +
            '\\foreach \\y/\\lbl in {1/100, 2/200, 3/300, 4/400, 5/500}{\n' +
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (6.8,\\y);\n' +
            '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
            '}\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!20] (0.6,0) rectangle (1.4,%s);\n' % h0 +
            '\\node[above] at (1.0,%s) {$%s$};\n' % (h0, vals[0]) +
            '\\node[below] at (1.0,0) {Thứ Năm};\n' +
            '\\draw[line width=1pt, fill=black!20] (2.2,0) rectangle (3.0,%s);\n' % h1 +
            '\\node[above] at (2.6,%s) {$%s$};\n' % (h1, vals[1]) +
            '\\node[below] at (2.6,0) {Thứ Sáu};\n' +
            '\\draw[line width=1pt, fill=black!20] (3.8,0) rectangle (4.6,%s);\n' % h2 +
            '\\node[above] at (4.2,%s) {$%s$};\n' % (h2, vals[2]) +
            '\\node[below] at (4.2,0) {Thứ Bảy};\n' +
            '\\draw[line width=1pt, fill=black!20] (5.4,0) rectangle (6.2,%s);\n' % h3 +
            '\\node[above] at (5.8,%s) {$%s$};\n' % (h3, vals[3]) +
            '\\node[below] at (5.8,0) {Chủ Nhật};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột dưới đây cho biết số lượng vé xem phim bán được tại một rạp chiếu phim trong $4$ ngày cuối tuần:\n' +
                         tikz_code + '\n' +
                         'Dựa vào biểu đồ, ngày nào rạp chiếu phim bán được nhiều vé nhất?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Quan sát biểu đồ cột, số lượng vé bán được trong từng ngày lần lượt là:\\\\' +
                   '- Thứ Năm: $%s$ vé;\\\\' +
                   '- Thứ Sáu: $%s$ vé;\\\\' +
                   '- Thứ Bảy: $%s$ vé;\\\\' +
                   '- Chủ Nhật: $%s$ vé.\\\\' +
                   'Cột cao nhất ứng với %s ($%s$ vé). Vậy %s rạp chiếu phim bán được nhiều vé nhất.'
                   ) % (vals[0], vals[1], vals[2], vals[3], da, vals[idx_max], da)

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
