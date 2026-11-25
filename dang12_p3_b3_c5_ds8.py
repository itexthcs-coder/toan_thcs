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

def bt_dang12_p3_b3_c5_ds8(self):
    # Dạng 12: Tính độ lệch thực tế so với chỉ tiêu kế hoạch trên biểu đồ đoạn thẳng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        chi_tieu = random.choice([120, 125, 130])
        q1 = chi_tieu - random.randint(6, 10)
        q2 = chi_tieu + random.randint(1, 4)
        q3 = chi_tieu - random.randint(12, 18)
        q4 = chi_tieu + random.randint(8, 12)
        
        tong_tt = q1 + q2 + q3 + q4
        tong_kh = chi_tieu * 4
        lech = tong_tt - tong_kh
        kq_str = str(lech)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.6,0) node[below] {Quý};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Sản lượng (nghìn tấn)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (Q1) at (1.0,2.2);\n' +
            '\\coordinate (Q2) at (2.2,2.7);\n' +
            '\\coordinate (Q3) at (3.4,1.8);\n' +
            '\\coordinate (Q4) at (4.6,3.2);\n' +
            '\\draw[line width=1pt] (Q1)--(Q2)--(Q3)--(Q4);\n' +
            '\\fill (Q1) circle (1pt) node[above] {$%s$};\n' % q1 +
            '\\fill (Q2) circle (1pt) node[above] {$%s$};\n' % q2 +
            '\\fill (Q3) circle (1pt) node[below] {$%s$};\n' % q3 +
            '\\fill (Q4) circle (1pt) node[above] {$%s$};\n' % q4 +
            '\\node[below] at (1.0,0) {Quý I};\n' +
            '\\node[below] at (2.2,0) {Quý II};\n' +
            '\\node[below] at (3.4,0) {Quý III};\n' +
            '\\node[below] at (4.6,0) {Quý IV};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây ghi lại sản lượng khai thác than thực tế (đơn vị: nghìn tấn) của một mỏ khoáng sản trong $4$ quý:\n' +
                         tikz_code + '\n' +
                         'Biết chỉ tiêu kế hoạch đặt ra cho mỗi quý là $%s$ nghìn tấn. Tính tổng mức chênh lệch thực tế so với kế hoạch của cả năm (lấy tổng sản lượng thực tế trừ đi tổng sản lượng kế hoạch, đơn vị: nghìn tấn).' % chi_tieu)
        
        loigiai = ('Tổng sản lượng khai thác thực tế trong cả $4$ quý là:\\\\' +
                   '$$%s + %s + %s + %s = %s \\text{ (nghìn tấn)}.$$\\\\' +
                   'Tổng chỉ tiêu kế hoạch của cả năm là: $%s \\cdot 4 = %s$ (nghìn tấn).\\\\' +
                   'Tổng mức chênh lệch thực tế so với kế hoạch của cả năm là:\\\\' +
                   '$$%s - %s = %s \\text{ (nghìn tấn)}.$$'
                   ) % (q1, q2, q3, q4, tong_tt, chi_tieu, tong_kh, tong_tt, tong_kh, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
