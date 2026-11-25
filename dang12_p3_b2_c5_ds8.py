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


def bt_dang12_p3_b2_c5_ds8(self):
    # Dạng 12 (Vận dụng): Đọc biểu đồ cột kép và tính tổng doanh thu theo đơn giá
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t7_th, t7_vip = 120, 40
        cn_th, cn_vip = 150, 50
        p_th = random.choice([70, 80, 90])
        p_vip = random.choice([140, 150, 160])
        
        tong_th = t7_th + cn_th
        tong_vip = t7_vip + cn_vip
        tong_nghin = tong_th * p_th + tong_vip * p_vip
        tong_trieu = (Decimal(str(tong_nghin)) / Decimal('1000')).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(tong_trieu).replace(".", ",")
        if kq_str.endswith(",0"):
            kq_str = kq_str[:-2]
            
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số vé};
        \\draw[line width=1pt, ->] (0,0) -- (5.0,0) node[right] {Ngày};
        \\draw[line width=1pt, fill=black!35] (0.7,0) rectangle (1.3,1.5) (2.7,0) rectangle (3.3,1.9);
        \\draw[line width=1pt, fill=white] (1.3,0) rectangle (1.9,0.5) (3.3,0) rectangle (3.9,0.65);
        \\node[above] at (1.0,1.5) {$120$}; \\node[above] at (1.6,0.5) {$40$};
        \\node[above] at (3.0,1.9) {$150$}; \\node[above] at (3.6,0.65) {$50$};
        \\node[below] at (1.3,0) {Thứ Bảy}; \\node[below] at (3.3,0) {Chủ nhật};
        \\draw[line width=1pt, fill=black!35] (4.8,1.7) rectangle (5.1,2.0); \\node[right] at (5.1,1.85) {Vé thường};
        \\draw[line width=1pt, fill=white] (4.8,1.2) rectangle (5.1,1.5); \\node[right] at (5.1,1.35) {Vé VIP};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Biểu đồ cột kép dưới đây biểu diễn số lượng vé thường và vé VIP bán được trong hai ngày Thứ Bảy và Chủ nhật tại một rạp chiếu phim:%sBiết giá mỗi vé thường là $%s$ nghìn đồng và giá mỗi vé VIP là $%s$ nghìn đồng. Hỏi tổng doanh thu của rạp trong hai ngày cuối tuần là bao nhiêu triệu đồng?"""
                         % (tikz_code, p_th, p_vip))
        
        loigiai = ("""Tổng số vé thường bán được trong hai ngày là: $120 + 150 = 270$ (vé).\\\\
        Tổng số vé VIP bán được trong hai ngày là: $40 + 50 = 90$ (vé).\\\\
        Tổng doanh thu của rạp trong hai ngày cuối tuần là:
        $$270 \\cdot %s + 90 \\cdot %s = %s \\text{ (nghìn đồng)} = %s \\text{ (triệu đồng)}.$$"""
                   % (p_th, p_vip, tong_nghin, kq_str))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
