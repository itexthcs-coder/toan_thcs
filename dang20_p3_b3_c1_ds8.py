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


def bt_dang20_p3_b3_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        a = randint(3, 5)
        b = randint(2, 4)
        c1 = randint(15, 22)
        c2 = randint(24, 32)
        tong_hang = c1 + c2
        
        T1 = a*x**2*y - b*x*y**2 + c1
        T2 = b*x*y**2 - a*x**2*y + c2
        
        pts = [(1, -1), (-1, 2), (2, 1), (-2, -1)]
        t1_vals = [int(T1.subs({x: px, y: py})) for px, py in pts]
        t2_dung = [int(T2.subs({x: px, y: py})) for px, py in pts]
        
        t2_hien_thi = list(t2_dung)
        t2_hien_thi[2] += 8
        kq_str = str(t2_dung[2])
        
        noidungcauhoi = ('''Hai cảm biến nhiệt độ $T_1$ và $T_2$ trong một phòng thí nghiệm truyền dữ liệu về máy chủ theo công thức $T_1 = %s$ và $T_2 = %s$. Bảng dưới đây ghi lại giá trị của $T_1$ và $T_2$ tại $4$ thời điểm đo khác nhau:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Thời điểm & Lần 1 & Lần 2 & Lần 3 & Lần 4 \\\\
\\hline
$T_1$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
$T_2$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Biết có duy nhất một lần đo bị nhiễu tín hiệu làm sai lệch giá trị của $T_2$ (trong khi $T_1$ vẫn chính xác). Hỏi giá trị đúng của $T_2$ ở lần đo bị lỗi đó phải là bao nhiêu?'''
                         % (latex(T1), latex(T2),
                            t1_vals[0], t1_vals[1], t1_vals[2], t1_vals[3],
                            t2_hien_thi[0], t2_hien_thi[1], t2_hien_thi[2], t2_hien_thi[3]))
        
        loigiai = ('''Ta có: \\\\
                   $T_1 + T_2 = (%s) + (%s) = %s$ với mọi giá trị của $x$ và $y$. \\\\
                   Kiểm tra các cột dữ liệu: Lần 1 ($%s + %s = %s$), Lần 2 ($%s + %s = %s$), Lần 4 ($%s + %s = %s$), riêng Lần 3 có $%s + %s = %s \\neq %s$. \\\\
                   Vì $T_1 = %s$ chính xác nên giá trị đúng của $T_2$ ở Lần 3 phải là: $%s - %s = %s$.'''
                   % (latex(T1), latex(T2), tong_hang,
                      t1_vals[0], t2_hien_thi[0], tong_hang,
                      t1_vals[1], t2_hien_thi[1], tong_hang,
                      t1_vals[3], t2_hien_thi[3], tong_hang,
                      t1_vals[2], t2_hien_thi[2], t1_vals[2] + t2_hien_thi[2], tong_hang,
                      t1_vals[2], tong_hang, t1_vals[2], kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
