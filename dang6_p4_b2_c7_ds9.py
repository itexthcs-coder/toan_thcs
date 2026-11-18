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
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang6_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        he_so = random.choice([1, 2])
        m1, m2, m3, m4 = 60*he_so, 90*he_so, 120*he_so, 30*he_so
        tong = 300*he_so

        hinh_cot = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Tuần};\n'
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.5) node[above] {Số sách};\n'
            '\\foreach \\y/\\lbl in {1/%s, 2/%s, 3/%s} {\n'
            '    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);\n'
            '    \\node[left] at (0,\\y) {$\\lbl$};\n'
            '}\n'
            '\\draw[line width=1pt] (0.7,0) rectangle (1.3,1.5); \\node[above] at (1.0,1.5) {$%s$}; \\node[below] at (1.0,0) {Tuần 1};\n'
            '\\draw[line width=1pt] (2.2,0) rectangle (2.8,2.25); \\node[above] at (2.5,2.25) {$%s$}; \\node[below] at (2.5,0) {Tuần 2};\n'
            '\\draw[line width=1pt] (3.7,0) rectangle (4.3,3.0); \\node[above] at (4.0,3.0) {$%s$}; \\node[below] at (4.0,0) {Tuần 3};\n'
            '\\draw[line width=1pt] (5.2,0) rectangle (5.8,0.75); \\node[above] at (5.5,0.75) {$%s$}; \\node[below] at (5.5,0) {Tuần 4};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (40*he_so, 80*he_so, 120*he_so, m1, m2, m3, m4)

        noidungcauhoi = (
            'Biểu đồ cột dưới đây thống kê số lượng sách quyên góp của học sinh khối 9 theo từng tuần trong tháng 11:%s'
            'a) Lập bảng tần số và bảng tần số tương đối biểu diễn số sách quyên góp qua từng tuần.\\\\ '
            'b) Số sách quyên góp trong hai tuần giữa (Tuần 2 và Tuần 3) chiếm bao nhiêu phần trăm tổng số sách cả tháng?'
        ) % (hinh_cot)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Tổng số sách quyên góp được trong tháng 11 là $n = %s + %s + %s + %s = %s$ (quyển).\\\\ '
            'Tần số tương đối của Tuần 1, 2, 3, 4 lần lượt là $20\\%%; 30\\%%; 40\\%%; 10\\%%$.\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|}\n'
            '\\hline\n'
            'Thời gian & Tuần 1 & Tuần 2 & Tuần 3 & Tuần 4 \\\\ \n'
            '\\hline\n'
            'Số sách (quyển) & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $20\\%%$ & $30\\%%$ & $40\\%%$ & $10\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Số sách quyên góp trong hai tuần giữa chiếm tỉ lệ: $30\\%% + 40\\%% = 70\\%%$.\n'
            '\\end{enumEX}'
        ) % (m1, m2, m3, m4, tong, m1, m2, m3, m4)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
