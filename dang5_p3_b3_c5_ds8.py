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

def bt_dang5_p3_b3_c5_ds8(self):
    # Dạng 5: Tìm số liệu bị che khuất trên biểu đồ cột kép khi biết tổng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cam_x = random.randint(135, 160)
        cam_s = random.randint(170, 195)
        buoi_x = random.randint(110, 130)
        buoi_s = random.randint(145, 175)
        tong = cam_x + cam_s + buoi_x + buoi_s
        kq_str = str(buoi_s)
        
        y_cx = round(cam_x / 50.0, 2)
        y_bx = round(buoi_x / 50.0, 2)
        y_cs = round(cam_s / 50.0, 2)
        y_bs = round(buoi_s / 50.0, 2)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.4,0) node[below] {Trang trại};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Số cây};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.8,0) rectangle (1.5,%s); \\node[above] at (1.15,%s) {$%s$};\n' % (y_cx, y_cx, cam_x) +
            '\\draw[line width=1pt, fill=black!45] (1.5,0) rectangle (2.2,%s); \\node[above] at (1.85,%s) {$%s$};\n' % (y_bx, y_bx, buoi_x) +
            '\\node[below] at (1.5,0) {Trang trại Xanh};\n' +
            '\\draw[line width=1pt, fill=black!15] (3.0,0) rectangle (3.7,%s); \\node[above] at (3.35,%s) {$%s$};\n' % (y_cs, y_cs, cam_s) +
            '\\draw[line width=1pt, fill=black!45] (3.7,0) rectangle (4.4,%s); \\node[above] at (4.05,%s) {$x$};\n' % (y_bs, y_bs) +
            '\\node[below] at (3.7,0) {Trang trại Sạch};\n' +
            '\\draw[line width=1pt, fill=black!15] (5.5,3.2) rectangle (5.9,3.5) node[right, yshift=-4pt] {Cây cam};\n' +
            '\\draw[line width=1pt, fill=black!45] (5.5,2.4) rectangle (5.9,2.7) node[right, yshift=-4pt] {Cây bưởi};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây biểu diễn số lượng cây ăn quả (cây) được trồng tại hai trang trại Xanh và Sạch gồm hai loại: Cây cam và Cây bưởi (trong đó số cây bưởi ở trang trại Sạch kí hiệu là $x$). Biết tổng số cây ăn quả của cả hai trang trại là $%s$ cây:\n' % tong +
                         tikz_code + '\n' +
                         'Tìm giá trị của $x$.')
        
        tong_3 = cam_x + buoi_x + cam_s
        loigiai = ('Tổng số cây đã biết trên biểu đồ là:\\\\' +
                   '$$%s + %s + %s = %s \\text{ (cây)}.$$\\\\' +
                   'Vì tổng số cây của cả hai trang trại là $%s$ cây nên giá trị của $x$ là:\\\\' +
                   '$$x = %s - %s = %s \\text{ (cây)}.$$'
                   ) % (cam_x, buoi_x, cam_s, tong_3, tong, tong, tong_3, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
