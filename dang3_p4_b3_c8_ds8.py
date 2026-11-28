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


def bt_dang3_p4_b3_c8_ds8(self):
    # Dạng 3: Thống kê thời gian giao hàng và dự báo mức phạt hợp đồng
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
        n1 = random.choice([400, 500])
        if n1 == 400:
            c1 = random.choice([80, 84, 92, 96])
            c3 = random.choice([68, 72, 76, 80])
            c4 = random.choice([20, 24, 28, 32])
            c2 = n1 - c1 - c3 - c4
            n2 = random.choice([1200, 1250, 1500, 1600])
        else:
            c1 = random.choice([105, 115, 125, 130])
            c3 = random.choice([85, 90, 95, 100])
            c4 = random.choice([25, 30, 35, 40])
            c2 = n1 - c1 - c3 - c4
            n2 = random.choice([1400, 1600, 1800, 2000])
        
        voucher = random.choice([15000, 20000, 25000, 30000])
        k_tre = c3 + c4
        p_dec = Decimal(k_tre) / Decimal(n1)
        p_str = fmt_dec(p_dec)
        so_don_tre = round_int(Decimal(n2) * p_dec)
        tong_tien = so_don_tre * voucher
        
        noidungcauhoi = ('''Một kho vận theo dõi thời gian giao hàng của $%s$ đơn hàng nội thành trong tuần đầu tiên của tháng và thu được bảng số liệu sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Thời gian giao (phút) & Dưới $20$ & Từ $20$ đến $30$ & Từ $31$ đến $45$ & Trên $45$ \\
\\hline
Số đơn hàng & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
Theo cam kết với khách hàng, mọi đơn hàng giao quá $30$ phút sẽ được tặng mã giảm giá $%s$ đồng. Nếu tuần tiếp theo kho vận xử lý $%s$ đơn hàng nội thành, hãy dự đoán số tiền mã giảm giá mà kho vận phải chi trả.'''
                         % (fmt_int(n1), c1, c2, c3, c4, fmt_int(voucher), fmt_int(n2)))
        
        loigiai = ('''Gọi $E$ là biến cố "Đơn hàng nội thành được giao quá $30$ phút".\\
Trong $%s$ đơn hàng được theo dõi, số đơn hàng giao quá $30$ phút (gồm từ $31$ đến $45$ phút và trên $45$ phút) là: $%s + %s = %s$ (đơn hàng).\\
Xác suất thực nghiệm của biến cố $E$ là $\\dfrac{%s}{%s} = %s$.\\
Do đó, xác suất một đơn hàng giao quá $30$ phút được ước lượng là $P(E) \\approx %s$.\\
Nếu tuần tiếp theo kho vận xử lý $%s$ đơn hàng nội thành, số đơn hàng giao quá $30$ phút được dự đoán là: $%s \\cdot %s = %s$ (đơn hàng).\\
Vậy số tiền mã giảm giá mà kho vận phải chi trả dự đoán là: $%s \\cdot %s = %s$ (đồng).'''
                   % (fmt_int(n1), c3, c4, k_tre,
                      k_tre, fmt_int(n1), p_str, p_str,
                      fmt_int(n2), fmt_int(n2), p_str, fmt_int(so_don_tre),
                      fmt_int(so_don_tre), fmt_int(voucher), fmt_int(tong_tien)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
