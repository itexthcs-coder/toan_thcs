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


def bt_dang7_p4_b3_c8_ds8(self):
    # Dạng 7: Thống kê chỉ số chất lượng không khí AQI (Môi trường)
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
        # Quý I năm không nhuận có 31 + 28 + 31 = 90 ngày
        n_q1 = 90
        d_tot = random.choice([18, 20, 24, 27])
        d_tb = random.choice([36, 40, 42, 45])
        d_kem = random.choice([15, 18, 21])
        d_xau = n_q1 - d_tot - d_tb - d_kem
        
        d_anh_huong = d_kem + d_xau
        frac_ah = Fraction(d_anh_huong, n_q1)
        p_ah_str = fmt_dec(Decimal(d_anh_huong) / Decimal(n_q1))
        
        p_tot = Decimal(d_tot) / Decimal(n_q1)
        du_doan_tot = round_int(Decimal(365) * p_tot)
        
        noidungcauhoi = ('''Trạm quan trắc khí tượng ghi nhận chỉ số chất lượng không khí (AQI) vào lúc $8\\text{h}00$ sáng hằng ngày tại một khu đô thị trong quý I của năm không nhuận (gồm tháng $1, 2, 3$) như sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Mức độ AQI & Tốt ($0 - 50$) & Trung bình ($51 - 100$) & Kém ($101 - 150$) & Xấu ($> 150$) \\
\\hline
Số ngày & $%s$ & $%s$ & $%s$ & $?$ \\
\\hline
\\end{tabular}
\\end{center}
a) Xác định số ngày có chỉ số AQI ở mức "Xấu" trong quý I.\\
b) Ước lượng xác suất để vào một buổi sáng bất kì, chất lượng không khí ở mức ảnh hưởng đến sức khỏe (tức là mức "Kém" hoặc "Xấu").\\
c) Dự đoán trong cả năm đó ($365$ ngày), có khoảng bao nhiêu ngày chất lượng không khí ở mức "Tốt"?'''
                         % (d_tot, d_tb, d_kem))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong năm không nhuận, tháng $1$ có $31$ ngày, tháng $2$ có $28$ ngày và tháng $3$ có $31$ ngày.\\
Tổng số ngày trong quý I là: $31 + 28 + 31 = 90$ (ngày).\\
Số ngày có chỉ số AQI ở mức "Xấu" trong quý I là: $90 - (%s + %s + %s) = %s$ (ngày).
\\item Số ngày chất lượng không khí ở mức "Kém" hoặc "Xấu" trong quý I là: $%s + %s = %s$ (ngày).\\
Xác suất thực nghiệm của biến cố "Chất lượng không khí ở mức ảnh hưởng đến sức khỏe" là $\\dfrac{%s}{90} = \\dfrac{%s}{%s} = %s$.\\
Vậy xác suất cần tìm được ước lượng là $%s$.
\\item Xác suất một ngày chất lượng không khí ở mức "Tốt" được ước lượng là $\\dfrac{%s}{90}$.\\
Trong cả năm đó ($365$ ngày), số ngày chất lượng không khí ở mức "Tốt" được dự đoán là: $365 \\cdot \\dfrac{%s}{90} \\approx %s$ (ngày).
\\end{enumEX}'''
                   % (d_tot, d_tb, d_kem, d_xau,
                      d_kem, d_xau, d_anh_huong,
                      d_anh_huong, frac_ah.numerator, frac_ah.denominator, p_ah_str, p_ah_str,
                      d_tot, d_tot, du_doan_tot))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
