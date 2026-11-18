# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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


def bt_dang12_p4_b1_c8_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Dạng 12: Bài toán lai đậu Hà Lan tích hợp Sinh học (Vận dụng SGK)
        bang_1 = ('''\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
\\text{Màu hạt / Dạng hạt} & $BB$ & $Bb$ & $bB$ & $bb$ \\\\
\\hline
$AA$ & $(AA, BB)$ & $(AA, Bb)$ & $(AA, bB)$ & $(AA, bb)$ \\\\
\\hline
$Aa$ & $(Aa, BB)$ & $(Aa, Bb)$ & $(Aa, bB)$ & $(Aa, bb)$ \\\\
\\hline
\\end{tabular}
\\end{center}''')
        bang_2 = ('''\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
\\text{Màu hạt / Dạng hạt} & $BB$ & $Bb$ \\\\
\\hline
$AA$ & $(AA, BB)$ & $(AA, Bb)$ \\\\
\\hline
$Aa$ & $(Aa, BB)$ & $(Aa, Bb)$ \\\\
\\hline
$aA$ & $(aA, BB)$ & $(aA, Bb)$ \\\\
\\hline
$aa$ & $(aa, BB)$ & $(aa, Bb)$ \\\\
\\hline
\\end{tabular}
\\end{center}''')
        truong_hop = [
            ('(AA, Bb)', '(Aa, Bb)', 'AA; Aa', 'BB; Bb; bB; bb', 8, bang_1),
            ('(Aa, BB)', '(Aa, Bb)', 'AA; Aa; aA; aa', 'BB; Bb', 8, bang_2)
        ]
        bo, me, gen_mau, gen_dang, ans, bang_sinh = random.choice(truong_hop)
        noidungcauhoi = ('''Ở đậu Hà Lan, màu hạt do cặp allele $A, a$ quy định (vàng trội hoàn toàn so với xanh) và hình dạng hạt do cặp allele $B, b$ quy định (trơn trội hoàn toàn so với nhăn). Khi lai hai cây đậu Hà Lan, cây con lấy ngẫu nhiên một gene từ cây bố và một gene từ cây mẹ ở mỗi tính trạng để hình thành cặp gene. Xét phép thử cho lai cây bố có kiểu gene $%s$ với cây mẹ có kiểu gene $%s$.\\\\
a) Liệt kê các tổ hợp kiểu gene có thể có về màu hạt và về hình dạng hạt của cây con.\\\\
b) Lập bảng mô tả không gian mẫu $\\Omega$ của phép lai trên và cho biết không gian mẫu có bao nhiêu phần tử.'''
                         % (bo, me))
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khi cây con lấy ngẫu nhiên một gene từ bố và một gene từ mẹ:\\\\
- Về màu hạt, các kiểu gene có thể có của cây con là: $%s$.\\\\
- Về hình dạng hạt, các kiểu gene có thể có của cây con là: $%s$.
\\item Lập bảng hai chiều liệt kê tất cả các tổ hợp kiểu gene của cây con:\\\\
%s
Vậy không gian mẫu $\\Omega$ gồm $%s$ phần tử như trong bảng trên.
\\end{enumEX}'''
                   % (gen_mau, gen_dang, bang_sinh, ans))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
