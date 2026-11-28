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


def bt_dang15_p4_b3_c8_ds8(self):
    # Dạng 15: Kết hợp tính chất số học của số có ba chữ số với xác suất cổ điển
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
        tap_cfg = random.choice([
            ([1, 2, 3, 4, 5], 300, 5),
            ([1, 2, 3, 4, 5], 400, 5),
            ([1, 2, 3, 4, 6], 400, 2)
        ])
        digits, gioi_han, chia_het_a = tap_cfg
        # Tạo tất cả các số có 3 chữ số khác nhau từ digits
        all_nums = []
        for a in digits:
            for b in digits:
                if b == a: continue
                for c in digits:
                    if c == a or c == b: continue
                    all_nums.append(100*a + 10*b + c)
        total_n = len(all_nums) # 60
        
        list_a = [num for num in all_nums if num % chia_het_a == 0]
        list_b = [num for num in all_nums if num < gioi_han and num % 3 == 0]
        
        frac_a = Fraction(len(list_a), total_n)
        frac_b = Fraction(len(list_b), total_n)
        
        str_digits = "; ".join(str(d) for d in digits)
        str_list_b = "; ".join(str(num) for num in list_b)
        
        if chia_het_a == 5:
            dk_a = "chữ số hàng đơn vị bằng $5$"
            so_cach_c = 1
        else:
            dk_a = "chữ số hàng đơn vị là số chẵn ($2; 4; 6$)"
            so_cach_c = 3
            
        noidungcauhoi = ('''Viết ngẫu nhiên một số tự nhiên có ba chữ số khác nhau được lập từ tập hợp các chữ số $\\{%s\\}$.\\
a) Tính tổng số kết quả có thể xảy ra của phép thử trên.\\
b) Tính xác suất của biến cố $A$: "Số được viết là một số chia hết cho $%s$".\\
c) Tính xác suất của biến cố $B$: "Số được viết là một số nhỏ hơn $%s$ và chia hết cho $3$".'''
                         % (str_digits, chia_het_a, gioi_han))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi số tự nhiên có ba chữ số khác nhau cần lập là $\\overline{abc}$ với $a, b, c \\in \\{%s\\}$ đôi một khác nhau.\\
- Có $5$ cách chọn chữ số hàng trăm $a$.\\
- Sau khi chọn $a$, còn $4$ cách chọn chữ số hàng chục $b$ ($b \\neq a$).\\
- Sau khi chọn $a$ và $b$, còn $3$ cách chọn chữ số hàng đơn vị $c$ ($c \\neq a, c \\neq b$).\\
Vậy tổng số kết quả có thể xảy ra (số các số lập được) là: $5 \\cdot 4 \\cdot 3 = %s$ (số). Các kết quả này là đồng khả năng.
\\item Để số $\\overline{abc}$ chia hết cho $%s$ thì %s, nên có $%s$ cách chọn $c$.\\
Sau khi chọn $c$, còn $4$ cách chọn $a$ và $3$ cách chọn $b$.\\
Số kết quả thuận lợi cho biến cố $A$ là: $%s \\cdot 4 \\cdot 3 = %s$.\\
Vậy xác suất của biến cố $A$ là $P(A) = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\item Một số chia hết cho $3$ khi và chỉ khi tổng các chữ số của nó chia hết cho $3$.\\
Liệt kê các số có ba chữ số khác nhau lập từ tập $\\{%s\\}$ nhỏ hơn $%s$ và có tổng các chữ số chia hết cho $3$, ta được $%s$ số là: $%s$.\\
Vậy xác suất của biến cố $B$ là $P(B) = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\end{enumEX}'''
                   % (str_digits, total_n,
                      chia_het_a, dk_a, so_cach_c, so_cach_c, len(list_a),
                      len(list_a), total_n, frac_a.numerator, frac_a.denominator,
                      str_digits, gioi_han, len(list_b), str_list_b,
                      len(list_b), total_n, frac_b.numerator, frac_b.denominator))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
