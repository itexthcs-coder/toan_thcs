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


def bt_dang9_p4_b3_c8_ds8(self):
    # Dạng 9: Thống kê điểm rèn luyện và xét học bổng (Giáo dục)
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
        n_ks = random.choice([120, 150, 160])
        if n_ks == 120:
            s1, s2, s3, s4 = 12, 36, 48, 24
            n_khoa = random.choice([850, 900, 960])
        elif n_ks == 150:
            s1, s2, s3, s4 = 15, 45, 60, 30
            n_khoa = random.choice([850, 950, 1050])
        else:
            s1, s2, s3, s4 = 16, 48, 64, 32
            n_khoa = random.choice([880, 920, 1000])
            
        sv_hb = s3 + s4
        p_hb = Decimal(sv_hb) / Decimal(n_ks)
        p_hb_str = fmt_dec(p_hb)
        p_hb_pct = fmt_dec(p_hb * 100)
        
        sv_duoi_90 = s1 + s2 + s3
        p_duoi_90 = Decimal(sv_duoi_90) / Decimal(n_ks)
        p_duoi_90_str = fmt_dec(p_duoi_90)
        du_doan_duoi_90 = round_int(Decimal(n_khoa) * p_duoi_90)
        
        noidungcauhoi = ('''Kết quả đánh giá điểm rèn luyện cuối học kì I của $%s$ sinh viên khoa Kinh tế được cho trong bảng tần số ghép nhóm sau:\\
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Khoảng điểm & $[50; 65)$ & $[65; 80)$ & $[80; 90)$ & $[90; 100]$ \\
\\hline
Số sinh viên & $%s$ & $%s$ & $%s$ & $%s$ \\
\\hline
\\end{tabular}
\\end{center}
Theo quy chế, sinh viên đạt từ $80$ điểm trở lên mới đủ điều kiện xét học bổng khuyến khích.\\
a) Chọn ngẫu nhiên một sinh viên trong nhóm khảo sát, tính xác suất thực nghiệm của biến cố $H$: "Sinh viên được chọn đủ điều kiện xét học bổng".\\
b) Toàn khoa Kinh tế có $%s$ sinh viên. Hãy dự đoán có khoảng bao nhiêu sinh viên của toàn khoa không đạt loại Xuất sắc (dưới $90$ điểm)?'''
                         % (n_ks, s1, s2, s3, s4, fmt_int(n_khoa)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Số sinh viên đạt từ $80$ điểm trở lên trong nhóm khảo sát là: $%s + %s = %s$ (sinh viên).\\
Vậy xác suất thực nghiệm của biến cố $H$ là $\\dfrac{%s}{%s} = %s = %s\\%%$.
\\item Số sinh viên đạt dưới $90$ điểm trong nhóm khảo sát là: $%s + %s + %s = %s$ (sinh viên) (hoặc $%s - %s = %s$).\\
Xác suất một sinh viên của khoa không đạt loại Xuất sắc được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Với toàn khoa có $%s$ sinh viên, số sinh viên không đạt loại Xuất sắc được dự đoán là: $%s \\cdot %s = %s$ (sinh viên).
\\end{enumEX}'''
                   % (s3, s4, sv_hb,
                      sv_hb, n_ks, p_hb_str, p_hb_pct,
                      s1, s2, s3, sv_duoi_90, n_ks, s4, sv_duoi_90,
                      sv_duoi_90, n_ks, p_duoi_90_str,
                      fmt_int(n_khoa), fmt_int(n_khoa), p_duoi_90_str, fmt_int(du_doan_duoi_90)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
