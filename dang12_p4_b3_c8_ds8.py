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


def bt_dang12_p4_b3_c8_ds8(self):
    # Dạng 12: Bài toán tính toán chi phí bảo hành sản phẩm (Kinh tế – Tài chính)
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
        n_kt = random.choice([400, 500])
        if n_kt == 400:
            loi_nhe = random.choice([16, 20, 24])
            loi_nang = random.choice([8, 12])
            n_lo = random.choice([6000, 8000, 10000])
        else:
            loi_nhe = random.choice([20, 25, 30])
            loi_nang = random.choice([10, 15])
            n_lo = random.choice([7000, 8000, 9000])
            
        tot = n_kt - loi_nhe - loi_nang
        gia_sua = random.choice([75000, 80000, 90000])
        gia_doi = random.choice([320000, 350000, 400000])
        
        tong_loi = loi_nhe + loi_nang
        p_loi = Decimal(tong_loi) / Decimal(n_kt)
        p_loi_str = fmt_dec(p_loi)
        p_loi_pct = fmt_dec(p_loi * 100)
        
        p_nhe = Decimal(loi_nhe) / Decimal(n_kt)
        p_nang = Decimal(loi_nang) / Decimal(n_kt)
        p_nhe_str = fmt_dec(p_nhe)
        p_nang_str = fmt_dec(p_nang)
        
        dd_nhe = round_int(Decimal(n_lo) * p_nhe)
        dd_nang = round_int(Decimal(n_lo) * p_nang)
        tong_chi_phi = dd_nhe * gia_sua + dd_nang * gia_doi
        
        noidungcauhoi = ('''Một hãng sản xuất tai nghe không dây kiểm tra ngẫu nhiên $%s$ sản phẩm xuất xưởng và nhận thấy: có $%s$ chiếc hoạt động hoàn hảo, $%s$ chiếc bị lỗi nhẹ ở hộp sạc (chi phí sửa chữa bảo hành là $%s$ đồng/chiếc) và $%s$ chiếc bị lỗi hỏng mạch âm thanh phải đổi mới hoàn toàn (chi phí đổi mới là $%s$ đồng/chiếc).\\
a) Ước lượng xác suất để một chiếc tai nghe bất kì của hãng bị lỗi (bao gồm cả lỗi nhẹ và lỗi nặng).\\
b) Nếu hãng bán ra thị trường một lô hàng gồm $%s$ chiếc tai nghe, hãy dự đoán tổng số tiền mà hãng phải dự trù cho việc sửa chữa và đổi mới bảo hành của lô hàng này.'''
                         % (fmt_int(n_kt), fmt_int(tot), loi_nhe, fmt_int(gia_sua),
                            loi_nang, fmt_int(gia_doi), fmt_int(n_lo)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $%s$ sản phẩm kiểm tra, tổng số chiếc tai nghe bị lỗi là: $%s + %s = %s$ (chiếc).\\
Xác suất thực nghiệm để một chiếc tai nghe bị lỗi là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vậy xác suất một chiếc tai nghe bất kì bị lỗi được ước lượng là $%s$ (hay $%s\\%%$).
\\item Xác suất một chiếc tai nghe bị lỗi nhẹ ở hộp sạc được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Xác suất một chiếc tai nghe bị lỗi hỏng mạch âm thanh được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Trong lô hàng $%s$ chiếc tai nghe:\\
- Số chiếc bị lỗi nhẹ dự đoán là: $%s \\cdot %s = %s$ (chiếc).\\
- Số chiếc bị lỗi nặng phải đổi mới dự đoán là: $%s \\cdot %s = %s$ (chiếc).\\
Vậy tổng số tiền bảo hành mà hãng phải dự trù là: $%s \\cdot %s + %s \\cdot %s = %s$ (đồng).
\\end{enumEX}'''
                   % (fmt_int(n_kt), loi_nhe, loi_nang, tong_loi,
                      tong_loi, fmt_int(n_kt), p_loi_str, p_loi_pct,
                      p_loi_str, p_loi_pct,
                      loi_nhe, fmt_int(n_kt), p_nhe_str,
                      loi_nang, fmt_int(n_kt), p_nang_str,
                      fmt_int(n_lo),
                      fmt_int(n_lo), p_nhe_str, fmt_int(dd_nhe),
                      fmt_int(n_lo), p_nang_str, fmt_int(dd_nang),
                      fmt_int(dd_nhe), fmt_int(gia_sua), fmt_int(dd_nang), fmt_int(gia_doi), fmt_int(tong_chi_phi)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
