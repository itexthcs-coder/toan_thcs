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


def bt_dang19_p3_b2_c10_hh9(self):
    d = random.choice([6, 8, 10])
    L_tong = random.choice([18, 20, 22, 24])
    R = d / 2
    h_tru = L_tong - d
    # V = pi * R^2 * h_tru + 4/3 * pi * R^3
    V_exact = math.pi * (R**2) * h_tru + (4 / 3) * math.pi * (R**3)
    V_round = Decimal(str(V_exact)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    kq_str = str(V_round)

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-1.8,0.7)--(1.8,0.7) (-1.8,-0.7)--(1.8,-0.7);
\\draw[line width=1pt] (-1.8,0.7) arc (90:270:0.7cm);
\\draw[line width=1pt] (1.8,-0.7) arc (-90:90:0.7cm);
\\draw[line width=1pt, dashed] (-1.8,0.7)--(-1.8,-0.7) (1.8,0.7)--(1.8,-0.7);
\\draw[<->, line width=1pt] (-2.5,-1.1)--(2.5,-1.1) node[midway, below] {$%s\\text{ mm}$};
\\draw[<->, line width=1pt] (2.8,-0.7)--(2.8,0.7) node[midway, right] {$%s\\text{ mm}$};
\\end{tikzpicture}
\\end{center}''' % (L_tong, d))

    noidungcauhoi = ('''Một viên thuốc con nhộng có dạng gồm một phần thân hình trụ ở giữa và hai đầu là hai nửa hình cầu có cùng đường kính với đáy hình trụ. Biết tổng chiều dài của cả viên thuốc là $%s\\text{ mm}$ và đường kính thân viên thuốc là $%s\\text{ mm}$ (bỏ qua độ dày vỏ thuốc). Tính thể tích phần thuốc chứa bên trong viên con nhộng đó (làm tròn kết quả đến hàng đơn vị của $\\text{mm}^3$).%s'''
                     % (L_tong, d, hinh_ve))

    loigiai = ('''Bán kính của hai nửa hình cầu (cũng là bán kính đáy phần thân hình trụ) là: $R = \\dfrac{%s}{2} = %s\\text{ (mm)}$.\\\nChiều dài phần thân hình trụ ở giữa là: $h = %s - 2R = %s - %s = %s\\text{ (mm)}$.\\\nHai nửa hình cầu ở hai đầu ghép lại thành một hình cầu có bán kính $R = %s\\text{ mm}$.\\\nThể tích của viên thuốc con nhộng là:
$$V = V_{\\text{trụ}} + V_{\\text{cầu}} = \\pi R^2 h + \\dfrac{4}{3}\\pi R^3 = \\pi \\cdot %s^2 \\cdot %s + \\dfrac{4}{3}\\pi \\cdot %s^3 \\approx %s\\text{ (mm}^3\\text{)}.$$'''
               % (d, int(R), L_tong, L_tong, d, int(h_tru), int(R), int(R), int(h_tru), int(R), kq_str))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
