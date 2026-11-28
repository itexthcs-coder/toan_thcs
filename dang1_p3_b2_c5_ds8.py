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


def bt_dang1_p3_b2_c5_ds8(self):
    # Dạng 1 (Vận dụng): Tính số biểu tượng tối thiểu khi chuyển bảng sang biểu đồ tranh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gcd_val = random.choice([120, 140, 150, 180])
        m1, m2, m3 = random.sample([2, 3, 4, 5, 7], 3)
        a, b, c = gcd_val * m1, gcd_val * m2, gcd_val * m3
        tong_bt = m1 + m2 + m3
        kq_str = str(tong_bt)
        
        noidungcauhoi = ("""Một kho nông sản xuất đi ba loại hạt giống được thống kê trong bảng sau:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|}
        \\hline
        \\textbf{Loại hạt giống} & Lúa giống & Ngô giống & Đậu tương \\\\
        \\hline
        \\textbf{Khối lượng (kg)} & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Nếu dùng biểu đồ tranh để biểu diễn bảng số liệu này sao cho không phải chia nhỏ bất kì biểu tượng nào và tổng số biểu tượng vẽ ra là ít nhất, thì tổng số biểu tượng cần vẽ cho cả ba loại hạt giống là bao nhiêu?"""
                         % (a, b, c))
        
        loigiai = ("""Để không phải chia nhỏ bất kì biểu tượng nào thì giá trị quy ước của mỗi biểu tượng phải là ước chung của $%s$, $%s$ và $%s$.\\\\
        Để tổng số biểu tượng vẽ ra là ít nhất, giá trị quy ước của mỗi biểu tượng phải lớn nhất, tức là bằng ước chung lớn nhất:
        $$\\text{ƯCLN}(%s, %s, %s) = %s \\text{ (kg)}.$$
        Khi đó số biểu tượng cần vẽ cho lúa giống, ngô giống và đậu tương lần lượt là: $\\dfrac{%s}{%s} = %s$; $\\dfrac{%s}{%s} = %s$; $\\dfrac{%s}{%s} = %s$.\\\\
        Tổng số biểu tượng cần vẽ là: $%s + %s + %s = %s$ (biểu tượng)."""
                   % (a, b, c, a, b, c, gcd_val, a, gcd_val, m1, b, gcd_val, m2, c, gcd_val, m3, m1, m2, m3, tong_bt))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
