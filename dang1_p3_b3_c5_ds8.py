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

def bt_dang1_p3_b3_c5_ds8(self):
    # Dạng 1: Tính chênh lệch thực tế giữa hai khu vực kinh tế từ biểu đồ hình quạt tròn và tổng GDP
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        gdp = random.choice([400, 450, 500, 600])
        p_dv, p_cn, p_nn, p_th = random.choice([
            (Decimal('42.5'), Decimal('36.5'), Decimal('12.2'), Decimal('8.8')),
            (Decimal('43.0'), Decimal('35.0'), Decimal('13.0'), Decimal('9.0')),
            (Decimal('44.2'), Decimal('36.2'), Decimal('11.4'), Decimal('8.2')),
            (Decimal('41.5'), Decimal('37.5'), Decimal('12.5'), Decimal('8.5'))
        ])
        diff_p = p_dv - p_cn
        kq_dec = (Decimal(gdp) * diff_p / Decimal(100)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(int(kq_dec))
        
        def fmt_vn(d):
            return str(d).rstrip('0').rstrip('.').replace('.', ',')
            
        a1 = round(float(p_dv) * 3.6, 1)
        a2 = round(float(p_dv + p_cn) * 3.6, 1)
        a3 = round(float(p_dv + p_cn + p_nn) * 3.6, 1)
        m0 = round(a1 / 2.0, 1)
        m1 = round((a1 + a2) / 2.0, 1)
        m2 = round((a2 + a3) / 2.0, 1)
        m3 = round((a3 + 360.0) / 2.0, 1)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:%s:1.9) -- cycle;\n' % a1 +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (%s:1.9) arc (%s:%s:1.9) -- cycle;\n' % (a1, a1, a2) +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (%s:1.9) arc (%s:%s:1.9) -- cycle;\n' % (a2, a2, a3) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (%s:1.9) arc (%s:360:1.9) -- cycle;\n' % (a3, a3) +
            '\\node at (%s:1.2) {$%s\\%%$};\n' % (m0, fmt_vn(p_dv)) +
            '\\node at (%s:1.25) {$%s\\%%$};\n' % (m1, fmt_vn(p_cn)) +
            '\\node at (%s:1.35) {$%s\\%%$};\n' % (m2, fmt_vn(p_nn)) +
            '\\node at (%s:1.45) {$%s\\%%$};\n' % (m3, fmt_vn(p_th)) +
            '\\draw[line width=1pt, fill=black!10] (2.6,1.2) rectangle (3.0,1.5) node[right, yshift=-4pt] {Dịch vụ};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.6,0.4) rectangle (3.0,0.7) node[right, yshift=-4pt] {Công nghiệp và xây dựng};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.6,-0.4) rectangle (3.0,-0.1) node[right, yshift=-4pt] {Nông, lâm, thủy sản};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-1.2) rectangle (3.0,-0.9) node[right, yshift=-4pt] {Thuế sản phẩm trừ trợ cấp};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây thống kê cơ cấu đóng góp vào tổng sản phẩm quốc nội (GDP) của một quốc gia năm $2025$:\n' +
                         tikz_code + '\n' +
                         'Biết tổng GDP của quốc gia đó năm $2025$ đạt $%s$ tỉ USD. Hỏi giá trị đóng góp của khu vực Dịch vụ nhiều hơn khu vực Công nghiệp và xây dựng bao nhiêu tỉ USD?' % gdp)
        
        loigiai = ('Từ biểu đồ hình quạt tròn, tỉ trọng đóng góp của khu vực Dịch vụ là $%s\\%%$ và của khu vực Công nghiệp và xây dựng là $%s\\%%$.\\\\' +
                   'Tỉ trọng đóng góp của khu vực Dịch vụ nhiều hơn khu vực Công nghiệp và xây dựng là:\\\\' +
                   '$$%s\\%% - %s\\%% = %s\\%%.$$\\\\' +
                   'Giá trị đóng góp của khu vực Dịch vụ nhiều hơn khu vực Công nghiệp và xây dựng là:\\\\' +
                   '$$%s \\cdot %s\\%% = %s \\text{ (tỉ USD)}.$$'
                   ) % (fmt_vn(p_dv), fmt_vn(p_cn), fmt_vn(p_dv), fmt_vn(p_cn), fmt_vn(diff_p), gdp, fmt_vn(diff_p), kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
