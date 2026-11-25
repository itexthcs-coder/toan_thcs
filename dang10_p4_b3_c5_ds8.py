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

def bt_dang10_p4_b3_c5_ds8(self):
    # Dạng 10: Phân tích biểu đồ đoạn thẳng tiêu thụ điện năng và đề xuất phương án tiết kiệm điện
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d_e = random.choice([0, 200, 400])
        e = [4200 + d_e, 3600 + d_e, 4500 + d_e, 4800 + d_e, 5400 + d_e, 5700 + d_e]
        tong_6t = sum(e)
        tb_6t = int(tong_6t // 6)
        gia_dien = 2200
        dien_tk = int(tong_6t * 15 // 100)
        tien_tk = dien_tk * gia_dien
        
        def fmt_int(n):
            return f"{n:,}".replace(",", "\\,")
            
        ys = [round(v / 1600.0, 2) for v in e]
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (6.8,0) node[below] {Tháng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Điện năng ($\\text{kWh}$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\coordinate (P1) at (1.0,%s); \\coordinate (P2) at (2.0,%s); \\coordinate (P3) at (3.0,%s);\n' % (ys[0], ys[1], ys[2]) +
            '\\coordinate (P4) at (4.0,%s); \\coordinate (P5) at (5.0,%s); \\coordinate (P6) at (6.0,%s);\n' % (ys[3], ys[4], ys[5]) +
            '\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5)--(P6);\n' +
            '\\fill (P1) circle (1pt) node[above] {$%s$};\n' % e[0] +
            '\\fill (P2) circle (1pt) node[below] {$%s$};\n' % e[1] +
            '\\fill (P3) circle (1pt) node[above] {$%s$};\n' % e[2] +
            '\\fill (P4) circle (1pt) node[above] {$%s$};\n' % e[3] +
            '\\fill (P5) circle (1pt) node[above] {$%s$};\n' % e[4] +
            '\\fill (P6) circle (1pt) node[above] {$%s$};\n' % e[5] +
            '\\node[below] at (1.0,0) {$1$}; \\node[below] at (2.0,0) {$2$}; \\node[below] at (3.0,0) {$3$};\n' +
            '\\node[below] at (4.0,0) {$4$}; \\node[below] at (5.0,0) {$5$}; \\node[below] at (6.0,0) {$6$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ đoạn thẳng dưới đây ghi lại sản lượng điện tiêu thụ hàng tháng (đơn vị: $\\text{kWh}$) của một xưởng sản xuất cơ khí nhỏ trong $6$ tháng đầu năm $2025$:\n' +
                         tikz_code + '\n' +
                         'a) Lập bảng thống kê lượng điện tiêu thụ của xưởng trong $6$ tháng đầu năm và tính lượng điện tiêu thụ trung bình mỗi tháng.\\\n' +
                         'b) Biết đơn giá điện sản xuất bình quân là $2\\,200$ đồng/$\\text{kWh}$. Trong $6$ tháng cuối năm, xưởng lắp đặt hệ thống điện mặt trời áp mái giúp giảm $15\\%%$ lượng điện phải mua từ lưới điện so với $6$ tháng đầu năm. Tính số tiền điện xưởng tiết kiệm được trong $6$ tháng cuối năm.')
        
        loigiai = ('\\begin{enumEX}[a)]{1}\n' +
                   '\\item Bảng thống kê lượng điện tiêu thụ của xưởng trong $6$ tháng đầu năm $2025$:\\\\' +
                   '\\begin{center}\n' +
                   '\\begin{tabular}{|l|c|c|c|c|c|c|}\n' +
                   '\\hline\n' +
                   '\\textbf{Tháng} & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ \\\\ \\hline\n' +
                   '\\textbf{Sản lượng ($\\text{kWh}$)} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \\hline\n' % tuple(e) +
                   '\\end{tabular}\n' +
                   '\\end{center}\n' +
                   'Tổng lượng điện tiêu thụ trong $6$ tháng đầu năm là:\\\\' +
                   '$$%s + %s + %s + %s + %s + %s = %s \\text{ (kWh)}.$$\\\\' +
                   'Lượng điện tiêu thụ trung bình mỗi tháng là: $\\dfrac{%s}{6} = %s\\text{ (kWh)}$.\n' +
                   '\\item Lượng điện xưởng tiết kiệm được (không phải mua từ lưới điện) trong $6$ tháng cuối năm là:\\\\' +
                   '$$%s \\cdot 15\\%% = %s \\text{ (kWh)}.$$\\\\' +
                   'Số tiền điện xưởng tiết kiệm được trong $6$ tháng cuối năm là:\\\\' +
                   '$$%s \\cdot 2\\,200 = %s \\text{ (đồng)}.$$\n' +
                   '\\end{enumEX}'
                   ) % (tuple(e) + (fmt_int(tong_6t), fmt_int(tong_6t), fmt_int(tb_6t),
                                    fmt_int(tong_6t), fmt_int(dien_tk), fmt_int(dien_tk), fmt_int(tien_tk)))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
