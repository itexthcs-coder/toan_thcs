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


def bt_dang8_p4_b3_c8_ds8(self):
    # Dạng 8: Phân tích tỉ lệ lỗi sản phẩm theo ca sản xuất (Quản lí vận hành)
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
        n_tot = random.choice([800, 1000])
        if n_tot == 800:
            n_sang = random.choice([440, 450, 480])
            n_chieu = n_tot - n_sang
            loi_sang = random.choice([16, 18, 20])
            loi_chieu = random.choice([21, 24, 25])
            n_don = random.choice([12000, 14000, 16000])
        else:
            n_sang = random.choice([550, 560, 600])
            n_chieu = n_tot - n_sang
            loi_sang = random.choice([22, 24, 25])
            loi_chieu = random.choice([27, 28, 30])
            n_don = random.choice([15000, 18000, 20000])
        
        tong_loi = loi_sang + loi_chieu
        dat_chuan = n_tot - tong_loi
        p_chuan = Decimal(dat_chuan) / Decimal(n_tot)
        p_chuan_str = fmt_dec(p_chuan)
        p_chuan_pct = fmt_dec(p_chuan * 100)
        
        p_loi_chieu = Decimal(loi_chieu) / Decimal(n_tot)
        p_loi_chieu_str = fmt_dec(p_loi_chieu)
        du_doan_loi_chieu = round_int(Decimal(n_don) * p_loi_chieu)
        
        noidungcauhoi = ('''Một xưởng may theo dõi $%s$ chiếc áo sơ mi được sản xuất trong ngày, trong đó ca sáng may được $%s$ chiếc và ca chiều may được phần còn lại. Qua kiểm tra, người ta thấy có $%s$ chiếc áo của ca sáng bị lỗi đường may và $%s$ chiếc áo của ca chiều bị lỗi đường may.\\
a) Chọn ngẫu nhiên một chiếc áo trong lô hàng $%s$ chiếc đó, ước lượng xác suất của biến cố $K$: "Chiếc áo được chọn đạt chuẩn (không bị lỗi đường may)".\\
b) Trong tháng tới, xưởng dự kiến nhận đơn hàng $%s$ chiếc áo với tỉ lệ phân bổ sản lượng giữa ca sáng và ca chiều không đổi. Hãy dự đoán số áo bị lỗi đường may của riêng ca chiều trong đơn hàng này.'''
                         % (fmt_int(n_tot), fmt_int(n_sang), loi_sang, loi_chieu,
                            fmt_int(n_tot), fmt_int(n_don)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tổng số chiếc áo bị lỗi đường may trong cả ngày là: $%s + %s = %s$ (chiếc).\\
Số chiếc áo đạt chuẩn (không bị lỗi đường may) là: $%s - %s = %s$ (chiếc).\\
Xác suất thực nghiệm của biến cố $K$ là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vậy xác suất của biến cố $K$ được ước lượng là $%s$ (hay $%s\\%%$).
\\item Trong $%s$ chiếc áo được theo dõi, có $%s$ chiếc áo của ca chiều bị lỗi đường may.\\
Xác suất để một chiếc áo bất kì trong đơn hàng thuộc ca chiều và bị lỗi đường may được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Với đơn hàng $%s$ chiếc áo, số áo bị lỗi đường may của riêng ca chiều được dự đoán là: $%s \\cdot %s = %s$ (chiếc).
\\end{enumEX}'''
                   % (loi_sang, loi_chieu, tong_loi,
                      fmt_int(n_tot), tong_loi, fmt_int(dat_chuan),
                      fmt_int(dat_chuan), fmt_int(n_tot), p_chuan_str, p_chuan_pct,
                      p_chuan_str, p_chuan_pct,
                      fmt_int(n_tot), loi_chieu,
                      loi_chieu, fmt_int(n_tot), p_loi_chieu_str,
                      fmt_int(n_don), fmt_int(n_don), p_loi_chieu_str, fmt_int(du_doan_loi_chieu)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
