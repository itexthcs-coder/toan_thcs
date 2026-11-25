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


def bt_dang11_p3_b2_c5_ds8(self):
    # Dạng 11 (Vận dụng): Đọc biểu đồ đoạn thẳng thập phân và tính giá trị trung bình cả năm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d = Decimal(str(random.choice([0.0, 0.5, 1.0, 1.5])))
        q1 = Decimal('16.5') + d
        q2 = Decimal('24.8') + d
        q3 = Decimal('26.2') + d
        q4 = Decimal('18.5') + d
        tong = q1 + q2 + q3 + q4
        tb = (tong / Decimal('4')).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(tb).replace(".", ",")
        
        def fmt_vn(val):
            return f"{val:.1f}".replace(".", ",")
            
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.6) node[above] {Nhiệt độ ($^\\circ$C)};
        \\draw[line width=1pt, ->] (0,0) -- (5.6,0) node[right] {Quý};
        \\coordinate (A) at (0.9,0.6);
        \\coordinate (B) at (2.2,1.8);
        \\coordinate (C) at (3.5,2.1);
        \\coordinate (D) at (4.8,0.9);
        \\draw[line width=1pt] (A)--(B)--(C)--(D);
        \\fill (A) circle (1pt) node[above] {$%s$};
        \\fill (B) circle (1pt) node[above left] {$%s$};
        \\fill (C) circle (1pt) node[above] {$%s$};
        \\fill (D) circle (1pt) node[above right] {$%s$};
        \\node[below] at (0.9,0) {Quý I};
        \\node[below] at (2.2,0) {Quý II};
        \\node[below] at (3.5,0) {Quý III};
        \\node[below] at (4.8,0) {Quý IV};
        \\end{tikzpicture}
        \\end{center}""" % (fmt_vn(q1), fmt_vn(q2), fmt_vn(q3), fmt_vn(q4)))
        
        noidungcauhoi = ("""Biểu đồ đoạn thẳng dưới đây ghi lại nhiệt độ trung bình của một vùng núi qua $4$ quý trong năm $2025$:%sTính nhiệt độ trung bình cả năm $2025$ của vùng núi đó (đơn vị: $^\\circ$C)."""
                         % tikz_code)
        
        loigiai = ("""Nhiệt độ trung bình cả năm $2025$ của vùng núi đó là:
        $$\\dfrac{%s + %s + %s + %s}{4} = \\dfrac{%s}{4} = %s \\text{ ($^\\circ$C)}.$$"""
                   % (fmt_vn(q1), fmt_vn(q2), fmt_vn(q3), fmt_vn(q4), fmt_vn(tong), kq_str))

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
