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


def bt_dang5_p4_b3_c8_ds8(self):
    # Dạng 5: Dự báo lượng điện tiêu thụ vượt ngưỡng (Năng lượng)
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
        thang_cfg = random.choice([
            ("tháng $4$", 30),
            ("tháng $6$", 30),
            ("tháng $9$", 30),
            ("tháng $11$", 30)
        ])
        ten_thang, so_ngay = thang_cfg
        d1 = random.choice([3, 6, 9, 12])
        d2 = random.choice([12, 15, 18])
        while d1 + d2 >= so_ngay:
            d2 -= 3
        d3 = so_ngay - d1 - d2
        
        frac_m = Fraction(d3, so_ngay)
        p_m_str = fmt_dec(Decimal(d3) / Decimal(so_ngay))
        
        he_cfg = random.choice([
            ("tháng $7$ và tháng $8$", 62),
            ("tháng $6$ và tháng $7$", 61),
            ("tháng $5$ và tháng $6$", 61)
        ])
        ten_he, ngay_he = he_cfg
        ngay_tu_10 = d2 + d3
        p_tu_10 = Decimal(ngay_tu_10) / Decimal(so_ngay)
        p_tu_10_str = fmt_dec(p_tu_10)
        du_doan_ngay = round_int(Decimal(ngay_he) * p_tu_10)
        
        noidungcauhoi = ('''Gia đình bác Hùng ghi lại mức điện năng tiêu thụ mỗi ngày trong suốt %s ($%s$ ngày) như sau: có $%s$ ngày dùng dưới $10\\text{ kWh}$, $%s$ ngày dùng từ $10$ đến $15\\text{ kWh}$, và những ngày còn lại dùng trên $15\\text{ kWh}$.\\
a) Tính xác suất thực nghiệm của biến cố $M$: "Trong một ngày của %s, gia đình bác Hùng dùng trên $15\\text{ kWh}$ điện".\\
b) Dự đoán trong hai tháng hè là %s (tổng cộng $%s$ ngày), có khoảng bao nhiêu ngày gia đình bác Hùng tiêu thụ điện ở mức từ $10\\text{ kWh}$ trở lên?'''
                         % (ten_thang, so_ngay, d1, d2, ten_thang, ten_he, ngay_he))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Số ngày gia đình bác Hùng dùng trên $15\\text{ kWh}$ điện trong %s là: $%s - (%s + %s) = %s$ (ngày).\\
Vậy xác suất thực nghiệm của biến cố $M$ là $\\dfrac{%s}{%s} = \\dfrac{%s}{%s} = %s$.
\\item Số ngày gia đình bác Hùng dùng từ $10\\text{ kWh}$ trở lên trong %s là: $%s + %s = %s$ (ngày).\\
Xác suất một ngày gia đình bác Hùng tiêu thụ điện từ $10\\text{ kWh}$ trở lên được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Trong hai tháng hè (%s) có $%s$ ngày, số ngày gia đình bác Hùng tiêu thụ điện ở mức từ $10\\text{ kWh}$ trở lên được dự đoán là: $%s \\cdot %s \\approx %s$ (ngày).
\\end{enumEX}'''
                   % (ten_thang, so_ngay, d1, d2, d3,
                      d3, so_ngay, frac_m.numerator, frac_m.denominator, p_m_str,
                      ten_thang, d2, d3, ngay_tu_10,
                      ngay_tu_10, so_ngay, p_tu_10_str,
                      ten_he, ngay_he, ngay_he, p_tu_10_str, du_doan_ngay))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
