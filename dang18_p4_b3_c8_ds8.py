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


def bt_dang18_p4_b3_c8_ds8(self):
    # Dạng 18: Thí nghiệm rút hai thẻ đồng thời và xét tính chẵn/lẻ, bội số của tích
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
        bo_the = random.choice([
            [2, 3, 5, 6, 7, 9],
            [2, 3, 4, 5, 7, 9],
            [1, 2, 3, 5, 6, 7],
            [2, 3, 5, 7, 8, 9]
        ])
        cap_list = []
        tich_set = []
        for i in range(len(bo_the)):
            for j in range(i + 1, len(bo_the)):
                a, b = bo_the[i], bo_the[j]
                p = a * b
                cap_list.append((a, b, p))
                if p not in tich_set:
                    tich_set.append(p)
        tich_set.sort()
        total_cap = len(cap_list) # 15
        
        cap_le = [(a, b, p) for (a, b, p) in cap_list if p % 2 == 1]
        cap_boi6 = [(a, b, p) for (a, b, p) in cap_list if p % 6 == 0]
        
        frac_d = Fraction(len(cap_le), total_cap)
        frac_f = Fraction(len(cap_boi6), total_cap)
        
        str_the = "; ".join(str(x) for x in bo_the)
        str_tich = "; ".join(str(x) for x in tich_set)
        str_cap_le = ", ".join("(%s; %s)" % (a, b) for (a, b, p) in cap_le)
        str_cap_boi6 = ", ".join("(%s; %s)" % (a, b) for (a, b, p) in cap_boi6)
        
        noidungcauhoi = ('''Một hộp kín đựng $6$ tấm thẻ giống hệt nhau được đánh số $%s$. Bạn Lan lấy ngẫu nhiên đồng thời $2$ tấm thẻ từ trong hộp và tính tích của hai số ghi trên hai tấm thẻ đó.\\
a) Liệt kê tất cả các giá trị có thể của tích hai số nhận được.\\
b) Tính xác suất của biến cố $D$: "Tích hai số ghi trên hai tấm thẻ là một số lẻ".\\
c) Tính xác suất của biến cố $F$: "Tích hai số ghi trên hai tấm thẻ là một bội của $6$".'''
                         % str_the)
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khi lấy ngẫu nhiên đồng thời $2$ tấm thẻ trong $6$ tấm thẻ đã cho, có tất cả $%s$ cặp thẻ đồng khả năng.\\
Tính tích của từng cặp số và sắp xếp theo thứ tự tăng dần, tất cả các giá trị có thể của tích hai số nhận được là: $%s$.
\\item Tích của hai số là một số lẻ khi và chỉ khi cả hai số được chọn đều là số lẻ.\\
Có $%s$ cặp thẻ thuận lợi cho biến cố $D$ là: $%s$.\\
Vậy xác suất của biến cố $D$ là $P(D) = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\item Có $%s$ cặp thẻ có tích là một bội của $6$ (thuận lợi cho biến cố $F$) là: $%s$.\\
Vậy xác suất của biến cố $F$ là $P(F) = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\end{enumEX}'''
                   % (total_cap, str_tich,
                      len(cap_le), str_cap_le, len(cap_le), total_cap, frac_d.numerator, frac_d.denominator,
                      len(cap_boi6), str_cap_boi6, len(cap_boi6), total_cap, frac_f.numerator, frac_f.denominator))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
