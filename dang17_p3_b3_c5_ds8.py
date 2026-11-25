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

def bt_dang17_p3_b3_c5_ds8(self):
    # Dạng 17: Tính hệ số góc (tốc độ biến thiên) của đoạn thẳng trên biểu đồ quãng đường - thời gian
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        v_tb = random.choice([52, 54, 56, 58, 60])
        s1 = random.choice([60, 72, 84])
        # dt = 2,5 giờ -> ds = 2,5 * v_tb
        ds = int(Decimal(v_tb) * Decimal('2.5'))
        s2 = s1 + ds
        kq_str = str(v_tb)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[below] {Thời gian (giờ)};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.0) node[left] {Quãng đường ($\\text{km}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (O) at (0,0);\n' +
            '\\coordinate (A) at (1.5,1.2);\n' +
            '\\coordinate (B) at (4.0,3.4);\n' +
            '\\draw[line width=1pt] (O)--(A)--(B);\n' +
            '\\draw[line width=1pt, dashed] (1.5,0) -- (A) -- (0,1.2);\n' +
            '\\draw[line width=1pt, dashed] (4.0,0) -- (B) -- (0,3.4);\n' +
            '\\fill (A) circle (1pt) (B) circle (1pt);\n' +
            '\\node[below] at (1.5,0) {$1,5$};\n' +
            '\\node[below] at (4.0,0) {$4,0$};\n' +
            '\\node[left] at (0,1.2) {$%s$};\n' % s1 +
            '\\node[left] at (0,3.4) {$%s$};\n' % s2 +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một tàu hỏa chuyển động thẳng trên đường ray được ghi lại bằng biểu đồ đoạn thẳng quãng đường – thời gian như hình vẽ dưới đây:\n' +
                         tikz_code + '\n' +
                         'Tính vận tốc trung bình của tàu hỏa trong khoảng thời gian từ $1,5$ giờ đến $4,0$ giờ (đơn vị: $\\text{km/h}$).')
        
        loigiai = ('Quãng đường tàu hỏa đi được trong khoảng thời gian từ $1,5$ giờ đến $4,0$ giờ là: $%s - %s = %s\\text{ (km)}$.\\\\' +
                   'Thời gian tàu hỏa di chuyển trong chặng này là: $4,0 - 1,5 = 2,5$ (giờ).\\\\' +
                   'Vận tốc trung bình của tàu hỏa trong khoảng thời gian này là:\\\\' +
                   '$$\\dfrac{%s}{2,5} = %s \\text{ (km/h)}.$$'
                   ) % (s2, s1, ds, ds, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
