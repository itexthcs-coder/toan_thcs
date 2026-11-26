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
def bt_dang20_p4_b3_c6_ds8(self):
    # Dạng 20: Bài toán Hình học thực tế – Thiết kế lối đi xung quanh mảnh vườn hình chữ nhật
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo = [
            (360, 6, 4, 18, 26, 14, '\\dfrac{13}{7}'),
            (300, 5, 3, 15, 25, 12, '\\dfrac{25}{12}'),
            (240, 4, 2, 12, 24, 10, '\\dfrac{12}{5}'),
            (400, 8, 4, 20, 28, 16, '\\dfrac{7}{4}')
        ]
        dien_tich, tang_dai, giam_rong, x_val, dai_moi, rong_moi, ti_so_str = random.choice(bo)
        tu_dai_moi = '%s + %sx' % (dien_tich, tang_dai)
        
        tikz_hinh = ('\\begin{center}\n'
                     '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                     '\\coordinate (A) at (0,0);\n'
                     '\\coordinate (B) at (4.5,0);\n'
                     '\\coordinate (C) at (4.5,2.5);\n'
                     '\\coordinate (D) at (0,2.5);\n'
                     '\\coordinate (M) at (0,0.6);\n'
                     '\\coordinate (N) at (5.5,0.6);\n'
                     '\\coordinate (P) at (5.5,2.5);\n'
                     '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
                     '\\draw[line width=1pt, dashed] (M)--(N)--(P)--(C);\n'
                     '\\fill (A) circle (1pt) node[left] {$A$};\n'
                     '\\fill (B) circle (1pt) node[below] {$B$};\n'
                     '\\fill (C) circle (1pt) node[above] {$C$};\n'
                     '\\fill (D) circle (1pt) node[left] {$D$};\n'
                     '\\node[left] at (0,1.25) {$x$};\n'
                     '\\node[below] at (2.25,0) {$\\dfrac{%s}{x}$};\n'
                     '\\node[above] at (5.0,2.5) {$+%s$};\n'
                     '\\node[left] at (0,0.3) {$-%s$};\n'
                     '\\end{tikzpicture}\n'
                     '\\end{center}' % (dien_tich, tang_dai, giam_rong))
        
        noidungcauhoi = ('Một mảnh vườn hình chữ nhật $ABCD$ có diện tích bằng $%s\\text{ m}^2$ và chiều rộng là $x\\text{ (m)}$ ($x > %s$). Người ta mở rộng chiều dài mảnh vườn thêm $%s\\text{ m}$ và thu hẹp chiều rộng đi $%s\\text{ m}$ để làm lối đi, tạo thành một mảnh vườn mới (minh họa như hình vẽ).\\'
                         '%s\\'
                         'a) Viết các phân thức biểu thị chiều dài ban đầu và chiều dài mới (sau khi mở rộng) của mảnh vườn.\\'
                         'b) Viết phân thức biểu thị tỉ số giữa chiều dài mới và chiều rộng mới của mảnh vườn, sau đó tính giá trị của tỉ số đó khi $x = %s$.'
                         % (dien_tich, giam_rong, tang_dai, giam_rong, tikz_hinh, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Chiều dài ban đầu của mảnh vườn là $\\dfrac{%s}{x}\\text{ (m)}$.\\'
                   'Chiều dài mới của mảnh vườn sau khi mở rộng thêm $%s\\text{ m}$ là:\\'
                   '$$\\dfrac{%s}{x} + %s = \\dfrac{%s}{x}\\text{ (m)}.$$\n'
                   '\\item Chiều rộng mới của mảnh vườn sau khi thu hẹp đi $%s\\text{ m}$ là $x - %s\\text{ (m)}$.\\'
                   'Phân thức biểu thị tỉ số giữa chiều dài mới và chiều rộng mới của mảnh vườn là:\\'
                   '$$T = \\dfrac{%s}{x} : (x - %s) = \\dfrac{%s}{x(x - %s)}.$$\\'
                   'Khi $x = %s$, chiều dài mới là $\\dfrac{%s}{%s} + %s = %s\\text{ (m)}$ và chiều rộng mới là $%s - %s = %s\\text{ (m)}$, do đó tỉ số cần tìm là:\\'
                   '$$T = \\dfrac{%s}{%s} = %s.$$\n'
                   '\\end{enumEX} \n'
                   % (dien_tich, tang_dai, dien_tich, tang_dai, tu_dai_moi,
                      giam_rong, giam_rong, tu_dai_moi, giam_rong, tu_dai_moi, giam_rong,
                      x_val, dien_tich, x_val, tang_dai, dai_moi, x_val, giam_rong, rong_moi,
                      dai_moi, rong_moi, ti_so_str))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
