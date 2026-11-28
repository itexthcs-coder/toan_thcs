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


def bt_dang11_p4_b3_c8_ds8(self):
    # Dạng 11: Thống kê tỉ lệ tiêm chủng và miễn dịch cộng đồng (Y tế dự phòng)
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
        n_tre = random.choice([500, 640, 800])
        if n_tre == 500:
            m3, m2 = 425, 50
            n_quan = random.choice([8000, 9000, 10000])
        elif n_tre == 640:
            m3, m2 = 544, 64
            n_quan = random.choice([8800, 9600, 10400])
        else:
            m3, m2 = 680, 80
            n_quan = random.choice([9200, 10000, 11200])
            
        m1 = n_tre - m3 - m2
        chua_du = n_tre - m3
        p_chua_du = Decimal(chua_du) / Decimal(n_tre)
        p_chua_du_str = fmt_dec(p_chua_du)
        p_chua_du_pct = fmt_dec(p_chua_du * 100)
        
        p_m1 = Decimal(m1) / Decimal(n_tre)
        p_m1_str = fmt_dec(p_m1)
        du_doan_m1 = round_int(Decimal(n_quan) * p_m1)
        
        noidungcauhoi = ('''Trung tâm y tế phường tiến hành rà soát sổ tiêm chủng của $%s$ trẻ em dưới $5$ tuổi trên địa bàn. Kết quả cho thấy có $%s$ trẻ đã tiêm đủ $3$ mũi vắc-xin phòng bệnh viêm não Nhật Bản, $%s$ trẻ mới tiêm $2$ mũi và số còn lại mới tiêm $1$ mũi.\\
a) Chọn ngẫu nhiên một trẻ trong danh sách rà soát, ước lượng xác suất của biến cố $T$: "Trẻ được chọn chưa tiêm đủ $3$ mũi vắc-xin".\\
b) Toàn quận có $%s$ trẻ em trong độ tuổi này. Dự đoán có khoảng bao nhiêu trẻ em toàn quận mới chỉ tiêm $1$ mũi vắc-xin?'''
                         % (fmt_int(n_tre), fmt_int(m3), m2, fmt_int(n_quan)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Số trẻ em chưa tiêm đủ $3$ mũi vắc-xin trong danh sách rà soát là: $%s - %s = %s$ (trẻ).\\
Xác suất thực nghiệm của biến cố $T$ là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vậy xác suất của biến cố $T$ được ước lượng là $%s$ (hay $%s\\%%$).
\\item Số trẻ em mới chỉ tiêm $1$ mũi vắc-xin trong danh sách rà soát là: $%s - (%s + %s) = %s$ (trẻ).\\
Xác suất để một trẻ em trong độ tuổi này mới chỉ tiêm $1$ mũi vắc-xin được ước lượng là $\\dfrac{%s}{%s} = %s$.\\
Với toàn quận có $%s$ trẻ em, số trẻ em mới chỉ tiêm $1$ mũi vắc-xin được dự đoán là: $%s \\cdot %s = %s$ (trẻ).
\\end{enumEX}'''
                   % (fmt_int(n_tre), fmt_int(m3), chua_du,
                      chua_du, fmt_int(n_tre), p_chua_du_str, p_chua_du_pct,
                      p_chua_du_str, p_chua_du_pct,
                      fmt_int(n_tre), fmt_int(m3), m2, m1,
                      m1, fmt_int(n_tre), p_m1_str,
                      fmt_int(n_quan), fmt_int(n_quan), p_m1_str, fmt_int(du_doan_m1)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
