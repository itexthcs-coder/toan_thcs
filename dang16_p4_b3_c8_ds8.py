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


def bt_dang16_p4_b3_c8_ds8(self):
    # Dạng 16: Thực nghiệm quay vòng quay may mắn và bài toán xác suất ngược (Tìm ẩn số)
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
        n_quay = random.choice([100, 110, 120])
        f1 = random.choice([12, 13, 14])
        f2 = random.choice([13, 14, 15]) # số nguyên tố (x)
        f3 = random.choice([11, 12, 13]) # số nguyên tố
        f4 = random.choice([14, 15, 16])
        f5 = random.choice([12, 13, 14]) # số nguyên tố
        f6 = random.choice([13, 14, 15])
        f8 = random.choice([12, 13, 14])
        f7 = n_quay - (f1 + f2 + f3 + f4 + f5 + f6 + f8) # y (không nguyên tố nếu 7? Chú ý 7 là số nguyên tố!)
        # Chọn ẩn x ở số 2 (nguyên tố) và y ở số 6 (hợp số) để xác định duy nhất x, y!
        # Đề bài: bảng có 1..8, ẩn x ở ô số 2, ẩn y ở ô số 6!
        f7_val = random.choice([12, 13, 14])
        f2_val = random.choice([13, 14, 15])
        f6_val = n_quay - (f1 + f2_val + f3 + f4 + f5 + f7_val + f8)
        
        k_nt = f2_val + f3 + f5 + f7_val # các số nguyên tố: 2, 3, 5, 7
        k_uoc8 = f1 + f2_val + f4 + f8   # các ước của 8: 1, 2, 4, 8
        n_tiep = n_quay * 2
        du_doan_uoc8 = round_int(Decimal(n_tiep) * Decimal(k_uoc8) / Decimal(n_quay))
        
        noidungcauhoi = ('''Một đĩa tròn được chia thành $8$ hình quạt bằng nhau có ghi các số từ $1$ đến $8$. Bạn Nam thực hiện quay mũi tên trên đĩa tròn đó $n$ lần và ghi lại kết quả số lần mũi tên chỉ vào các số như sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|c|c|c|c|}
\\hline
Số trên đĩa & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ & $7$ & $8$ \\
\\hline
Số lần xuất hiện & $%s$ & $x$ & $%s$ & $%s$ & $%s$ & $y$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
Biết rằng bạn Nam đã quay tổng cộng $%s$ lần và xác suất thực nghiệm của biến cố "Mũi tên chỉ vào số nguyên tố" bằng $\\dfrac{%s}{%s}$.\\
a) Tìm các giá trị $x$ và $y$.\\
b) Nếu bạn Nam tiếp tục quay thêm $%s$ lần nữa, hãy dự đoán số lần mũi tên chỉ vào số là ước của $8$.'''
                         % (f1, f3, f4, f5, f7_val, f8,
                            n_quay, k_nt, n_quay, n_tiep))
        
        tong_6_so = f1 + f3 + f4 + f5 + f7_val + f8
        tong_xy = n_quay - tong_6_so
        tong_nt_biet = f3 + f5 + f7_val
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì bạn Nam đã quay tổng cộng $%s$ lần nên ta có:\\
$%s + x + %s + %s + %s + y + %s + %s = %s \\Leftrightarrow x + y + %s = %s \\Leftrightarrow x + y = %s$.\\
Trên đĩa tròn từ $1$ đến $8$, các số nguyên tố là $2; 3; 5; 7$.\\
Số lần mũi tên chỉ vào số nguyên tố là: $x + %s + %s + %s = x + %s$.\\
Vì xác suất thực nghiệm của biến cố "Mũi tên chỉ vào số nguyên tố" bằng $\\dfrac{%s}{%s}$ trong $%s$ lần quay nên số lần biến cố này xảy ra là $%s$.\\
Suy ra $x + %s = %s \\Leftrightarrow x = %s$.\\
Thay $x = %s$ vào $x + y = %s$, ta được $y = %s - %s = %s$.\\
Vậy $x = %s$ và $y = %s$.
\\item Các số trên đĩa là ước của $8$ gồm: $1; 2; 4; 8$.\\
Số lần mũi tên chỉ vào ước của $8$ trong $%s$ lần quay đầu là: $%s + %s + %s + %s = %s$ (lần).\\
Xác suất mũi tên chỉ vào số là ước của $8$ được ước lượng là $\\dfrac{%s}{%s}$.\\
Nếu bạn Nam tiếp tục quay thêm $%s$ lần nữa, số lần mũi tên chỉ vào số là ước của $8$ được dự đoán là: $%s \\cdot \\dfrac{%s}{%s} = %s$ (lần).
\\end{enumEX}'''
                   % (n_quay, f1, f3, f4, f5, f7_val, f8, n_quay, tong_6_so, n_quay, tong_xy,
                      f3, f5, f7_val, tong_nt_biet,
                      k_nt, n_quay, n_quay, k_nt,
                      tong_nt_biet, k_nt, f2_val,
                      f2_val, tong_xy, tong_xy, f2_val, f6_val,
                      f2_val, f6_val,
                      n_quay, f1, f2_val, f4, f8, k_uoc8,
                      k_uoc8, n_quay, n_tiep, n_tiep, k_uoc8, n_quay, du_doan_uoc8))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
