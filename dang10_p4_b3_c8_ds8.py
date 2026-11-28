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


def bt_dang10_p4_b3_c8_ds8(self):
    # Dạng 10: Dự báo lượng khách đặt bàn và chuẩn bị nguyên liệu (Nhà hàng – Khách sạn)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        def fmt_int(n):
            return '{:,}'.format(int(n)).replace(',', '\\,')
        
        def fmt_dec(val, places=None):
            if places is not None:
                d = Decimal(str(val)).quantize(Decimal(places), rounding=ROUND_HALF_UP)
                s = format(d, 'f')
            else:
                s = str(val)
            return s.replace('.', ',')
        
        def round_int(val):
            return int(Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        
        def round_ten(val):
            return int(Decimal(str(val)).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
        n_tuan = random.choice([20, 25, 30])
        if n_tuan == 20:
            t1, t2, t3, t4 = 2, 6, 9, 3
            n_tuan_sau = random.choice([15, 25, 30])
        elif n_tuan == 25:
            t1, t2, t3, t4 = 3, 7, 11, 4
            n_tuan_sau = random.choice([15, 20, 30])
        else:
            t1, t2, t3, t4 = 4, 8, 13, 5
            n_tuan_sau = random.choice([15, 20, 25])
            
        t_it_21 = t3 + t4
        p_it_21 = Decimal(t_it_21) / Decimal(n_tuan)
        p_it_21_str = fmt_dec(p_it_21)
        p_it_21_pct = fmt_dec(p_it_21 * 100)
        
        t_15_25 = t2 + t3
        p_15_25 = Decimal(t_15_25) / Decimal(n_tuan)
        p_15_25_str = fmt_dec(p_15_25)
        du_doan_toi = round_int(Decimal(n_tuan_sau) * p_15_25)
        
        noidungcauhoi = ('''Quản lí một nhà hàng hải sản thống kê số lượng bàn khách đặt trước vào các tối cuối tuần trong $%s$ tuần liên tiếp thu được kết quả: có $%s$ tuần đặt dưới $15$ bàn, $%s$ tuần đặt từ $15$ đến $20$ bàn, $%s$ tuần đặt từ $21$ đến $25$ bàn và $%s$ tuần đặt trên $25$ bàn.\\
a) Ước lượng xác suất để vào một tối cuối tuần bất kì, nhà hàng nhận được ít nhất $21$ bàn đặt trước.\\
b) Trong $%s$ tuần tiếp theo, dự đoán có khoảng bao nhiêu tối cuối tuần nhà hàng có số bàn đặt trước từ $15$ đến $25$ bàn?'''
                         % (n_tuan, t1, t2, t3, t4, n_tuan_sau))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $%s$ tuần thống kê, số tuần nhà hàng nhận được ít nhất $21$ bàn đặt trước (từ $21$ đến $25$ bàn hoặc trên $25$ bàn) là: $%s + %s = %s$ (tuần).\\
Xác suất thực nghiệm của biến cố "Nhà hàng nhận được ít nhất $21$ bàn đặt trước" là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vậy xác suất cần tìm được ước lượng là $%s$ (hay $%s\\%%$).
\\item Số tuần nhà hàng có số bàn đặt trước từ $15$ đến $25$ bàn trong thời gian thống kê là: $%s + %s = %s$ (tuần).\\
Xác suất để một tối cuối tuần nhà hàng có từ $15$ đến $25$ bàn đặt trước được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Trong $%s$ tuần tiếp theo, số tối cuối tuần nhà hàng có số bàn đặt trước từ $15$ đến $25$ bàn được dự đoán là: $%s \\cdot %s \\approx %s$ (tối).
\\end{enumEX}'''
                   % (n_tuan, t3, t4, t_it_21,
                      t_it_21, n_tuan, p_it_21_str, p_it_21_pct,
                      p_it_21_str, p_it_21_pct,
                      t2, t3, t_15_25,
                      t_15_25, n_tuan, p_15_25_str,
                      n_tuan_sau, n_tuan_sau, p_15_25_str, du_doan_toi))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
