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


def bt_dang6_p4_b3_c8_ds8(self):
    # Dạng 6: Đánh giá hiệu quả chiến dịch quảng cáo trực tuyến (Marketing số)
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
        n1 = random.choice([4000, 4500, 5000])
        r1 = random.choice([6, 7, 8]) # phần trăm
        k1 = n1 * r1 // 100
        
        n2 = random.choice([6000, 6200, 6400, 6500])
        r2_dec = Decimal(r1) - Decimal('0.5')
        k2 = int(Decimal(n2) * r2_dec / Decimal(100))
        
        p1_str = fmt_dec(Decimal(k1) / Decimal(n1))
        p1_pct = fmt_dec(Decimal(k1) * 100 / Decimal(n1))
        p2_str = fmt_dec(Decimal(k2) / Decimal(n2))
        p2_pct = fmt_dec(Decimal(k2) * 100 / Decimal(n2))
        
        n_moi = random.choice([20000, 25000, 30000, 35000])
        du_doan_click = round_int(Decimal(n_moi) * Decimal(k1) / Decimal(n1))
        
        noidungcauhoi = ('''Một cửa hàng thời trang chạy thử nghiệm hai mẫu quảng cáo video trên mạng xã hội trong cùng một ngày. Mẫu $1$ tiếp cận được $%s$ người xem và có $%s$ lượt nhấp vào liên kết mua hàng. Mẫu $2$ tiếp cận được $%s$ người xem và có $%s$ lượt nhấp vào liên kết.\\
a) Dựa vào xác suất thực nghiệm, hãy cho biết mẫu quảng cáo nào thu hút khách hàng nhấp vào liên kết hiệu quả hơn?\\
b) Nếu cửa hàng chi ngân sách để Mẫu $1$ tiếp cận được $%s$ người xem trong đợt khuyến mãi sắp tới, dự đoán sẽ có khoảng bao nhiêu lượt nhấp vào liên kết?'''
                         % (fmt_int(n1), fmt_int(k1), fmt_int(n2), fmt_int(k2), fmt_int(n_moi)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xác suất thực nghiệm của biến cố "Người xem nhấp vào liên kết của Mẫu $1$" là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Xác suất thực nghiệm của biến cố "Người xem nhấp vào liên kết của Mẫu $2$" là $\\dfrac{%s}{%s} = %s = %s\\%%$.\\
Vì $%s\\%% > %s\\%%$ nên Mẫu $1$ thu hút khách hàng nhấp vào liên kết hiệu quả hơn Mẫu $2$.
\\item Xác suất một người xem nhấp vào liên kết của Mẫu $1$ được ước lượng là $%s$.\\
Nếu Mẫu $1$ tiếp cận được $%s$ người xem trong đợt khuyến mãi sắp tới, số lượt nhấp vào liên kết được dự đoán là: $%s \\cdot %s = %s$ (lượt).
\\end{enumEX}'''
                   % (fmt_int(k1), fmt_int(n1), p1_str, p1_pct,
                      fmt_int(k2), fmt_int(n2), p2_str, p2_pct,
                      p1_pct, p2_pct,
                      p1_str, fmt_int(n_moi), fmt_int(n_moi), p1_str, fmt_int(du_doan_click)))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
