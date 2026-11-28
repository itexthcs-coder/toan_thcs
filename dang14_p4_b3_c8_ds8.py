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


def bt_dang14_p4_b3_c8_ds8(self):
    # Dạng 14: Đánh giá độ chính xác của thiết bị đo lường (Kĩ thuật – Công nghiệp)
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
        n_goi = random.choice([200, 250])
        if n_goi == 200:
            g1, g2, g3, g4, g5 = 6, 34, 118, 38, 4
            n_ca = random.choice([4000, 4500, 5000])
        else:
            g1, g2, g3, g4, g5 = 8, 42, 145, 48, 7
            n_ca = random.choice([4500, 5000, 6000])
            
        khong_chuan = g1 + g5
        p_kc = Decimal(khong_chuan) / Decimal(n_goi)
        p_kc_str = fmt_dec(p_kc)
        p_kc_pct = fmt_dec(p_kc * 100)
        
        thieu_hut = g1 + g2
        p_th = Decimal(thieu_hut) / Decimal(n_goi)
        p_th_str = fmt_dec(p_th)
        du_doan_th = round_int(Decimal(n_ca) * p_th)
        
        noidungcauhoi = ('''Một dây chuyền đóng gói tự động cài đặt định mức mỗi gói cà phê nặng $500\\text{ g}$. Nhân viên kĩ thuật cân kiểm tra ngẫu nhiên $%s$ gói cà phê và ghi lại sai số so với định mức chuẩn trong bảng sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|c|}
\\hline
Khối lượng thực tế ($\\text{g}$) & Dưới $495$ & Từ $495$ đến $499$ & Đúng $500$ & Từ $501$ đến $505$ & Trên $505$ \\
\\hline
Số gói & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
Theo tiêu chuẩn chất lượng, gói cà phê đạt chuẩn khi khối lượng nằm trong khoảng từ $495\\text{ g}$ đến $505\\text{ g}$.\\
a) Ước lượng xác suất một gói cà phê đóng gói bởi dây chuyền này không đạt tiêu chuẩn chất lượng.\\
b) Trong một ca làm việc đóng gói được $%s$ gói cà phê, dự đoán có khoảng bao nhiêu gói bị thiếu hụt khối lượng (nhỏ hơn $500\\text{ g}$)?'''
                         % (n_goi, g1, g2, g3, g4, g5, fmt_int(n_ca)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Các gói cà phê không đạt tiêu chuẩn chất lượng có khối lượng dưới $495\\text{ g}$ hoặc trên $505\\text{ g}$.\\
Số gói không đạt tiêu chuẩn trong $%s$ gói kiểm tra là: $%s + %s = %s$ (gói).\\
Xác suất thực nghiệm của biến cố "Gói cà phê không đạt tiêu chuẩn chất lượng" là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vậy xác suất cần tìm được ước lượng là $%s$ (hay $%s\\%%$).
\\item Số gói bị thiếu hụt khối lượng (nhỏ hơn $500\\text{ g}$) trong $%s$ gói kiểm tra là: $%s + %s = %s$ (gói).\\
Xác suất một gói cà phê bị thiếu hụt khối lượng được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Trong một ca làm việc đóng gói $%s$ gói cà phê, số gói bị thiếu hụt khối lượng được dự đoán là: $%s \\cdot %s = %s$ (gói).
\\end{enumEX}'''
                   % (n_goi, g1, g5, khong_chuan,
                      khong_chuan, n_goi, p_kc_str, p_kc_pct,
                      p_kc_str, p_kc_pct,
                      n_goi, g1, g2, thieu_hut,
                      thieu_hut, n_goi, p_th_str,
                      fmt_int(n_ca), fmt_int(n_ca), p_th_str, fmt_int(du_doan_th)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
