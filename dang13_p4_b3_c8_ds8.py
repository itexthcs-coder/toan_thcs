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


def bt_dang13_p4_b3_c8_ds8(self):
    # Dạng 13: Thống kê lượt mượn sách thư viện theo thể loại (Văn hóa – Giáo dục)
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
        n_luot = random.choice([500, 600])
        if n_luot == 500:
            s_tk, s_vh, s_kh, s_bao = 210, 165, 95, 30
            n_t11 = random.choice([700, 720, 750, 800])
        else:
            s_tk, s_vh, s_kh, s_bao = 252, 198, 114, 36
            n_t11 = random.choice([750, 800, 850, 900])
            
        khong_vh = n_luot - s_vh
        p_kvh = Decimal(khong_vh) / Decimal(n_luot)
        p_kvh_str = fmt_dec(p_kvh)
        p_kvh_pct = fmt_dec(p_kvh * 100)
        
        p_kh = Decimal(s_kh) / Decimal(n_luot)
        p_bao = Decimal(s_bao) / Decimal(n_luot)
        p_kh_str = fmt_dec(p_kh)
        p_bao_str = fmt_dec(p_bao)
        
        dd_kh = round_int(Decimal(n_t11) * p_kh)
        dd_bao = round_int(Decimal(n_t11) * p_bao)
        chenh_lech = dd_kh - dd_bao
        
        noidungcauhoi = ('''Thư viện một trường THCS thống kê số lượt học sinh mượn sách trong tháng $10$ theo các thể loại: Sách tham khảo ($%s$ lượt), Truyện văn học ($%s$ lượt), Sách khoa học – kĩ thuật ($%s$ lượt) và Báo – tạp chí ($%s$ lượt).\\
a) Tính xác suất thực nghiệm của biến cố $S$: "Học sinh đến thư viện mượn sách không thuộc nhóm truyện văn học".\\
b) Trong tháng $11$ nhân dịp Ngày Nhà giáo Việt Nam, thư viện dự kiến đón $%s$ lượt mượn sách. Dự đoán số lượt mượn Sách khoa học – kĩ thuật sẽ nhiều hơn số lượt mượn Báo – tạp chí khoảng bao nhiêu lượt?'''
                         % (s_tk, s_vh, s_kh, s_bao, fmt_int(n_t11)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tổng số lượt học sinh mượn sách trong tháng $10$ là: $%s + %s + %s + %s = %s$ (lượt).\\
Số lượt mượn sách không thuộc nhóm truyện văn học là: $%s - %s = %s$ (lượt).\\
Vậy xác suất thực nghiệm của biến cố $S$ là $\\dfrac{%s}{%s} = %s = %s\\%%$.
\\item Xác suất một lượt mượn là Sách khoa học – kĩ thuật được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Xác suất một lượt mượn là Báo – tạp chí được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Trong tháng $11$ với $%s$ lượt mượn sách:\\
- Số lượt mượn Sách khoa học – kĩ thuật dự đoán là: $%s \\cdot %s \\approx %s$ (lượt).\\
- Số lượt mượn Báo – tạp chí dự đoán là: $%s \\cdot %s \\approx %s$ (lượt).\\
Vậy số lượt mượn Sách khoa học – kĩ thuật dự đoán nhiều hơn số lượt mượn Báo – tạp chí khoảng: $%s - %s = %s$ (lượt).
\\end{enumEX}'''
                   % (s_tk, s_vh, s_kh, s_bao, n_luot,
                      n_luot, s_vh, khong_vh,
                      khong_vh, n_luot, p_kvh_str, p_kvh_pct,
                      s_kh, n_luot, p_kh_str,
                      s_bao, n_luot, p_bao_str,
                      fmt_int(n_t11),
                      fmt_int(n_t11), p_kh_str, dd_kh,
                      fmt_int(n_t11), p_bao_str, dd_bao,
                      dd_kh, dd_bao, chenh_lech))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
