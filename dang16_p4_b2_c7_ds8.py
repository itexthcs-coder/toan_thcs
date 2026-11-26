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
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang16_p4_b2_c7_ds8(self):
    # Dạng 16: Ứng dụng - Bài toán chuyển động đường thủy tính độ dài quãng đường
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v_thuc = random.choice([20, 22, 24, 26, 28])
        v_nuoc = random.choice([2, 3, 4])
        v_xuoi = v_thuc + v_nuoc
        v_nguoc = v_thuc - v_nuoc
        # Chọn quãng đường S là bội đẹp của gcd để thời gian lẻ nửa giờ hoặc phần tư giờ
        # t = S/v_xuoi + S/v_nguoc = S * (2*v_thuc) / (v_xuoi * v_nguoc)
        # Đặt S = k * (v_xuoi * v_nguoc) / gcd(2*v_thuc, v_xuoi*v_nguoc) / 2
        g = math.gcd(2 * v_thuc, v_xuoi * v_nguoc)
        base_S = (v_xuoi * v_nguoc) // g
        S = base_S if base_S >= 30 else base_S * 2
        t_frac = Rational(S, v_xuoi) + Rational(S, v_nguoc)
        # Đảm bảo t_frac có mẫu là 1, 2, hoặc 4 để đổi ra giờ và phút đẹp
        while t_frac.q not in [1, 2, 4]:
            v_thuc = random.choice([20, 22, 24, 25, 26, 28, 30])
            v_nuoc = random.choice([2, 3, 4, 5])
            v_xuoi = v_thuc + v_nuoc
            v_nguoc = v_thuc - v_nuoc
            g = math.gcd(2 * v_thuc, v_xuoi * v_nguoc)
            base_S = (v_xuoi * v_nguoc) // g
            S = base_S if base_S >= 35 else base_S * 2
            t_frac = Rational(S, v_xuoi) + Rational(S, v_nguoc)
            
        gio = t_frac.p // t_frac.q
        phut = ((t_frac.p % t_frac.q) * 60) // t_frac.q
        thoi_gian_str = '%s giờ %s phút' % (gio, phut) if phut > 0 else '%s giờ' % gio
        
        bcnn = math.lcm(v_xuoi, v_nguoc)
        m1 = bcnn // v_xuoi
        m2 = bcnn // v_nguoc
        vp = int(t_frac * bcnn)
        
        noidungcauhoi = ('''Một ca nô chạy xuôi dòng từ bến $A$ đến bến $B$ rồi lập tức quay ngược dòng từ bến $B$ trở về bến $A$ mất tổng cộng $%s$. Biết vận tốc thực của ca nô khi nước yên lặng là $%s\\text{ km/h}$ và vận tốc dòng nước là $%s\\text{ km/h}$. Tính độ dài quãng đường sông $AB$.'''
                         % (thoi_gian_str, v_thuc, v_nuoc))
        
        loigiai = ('''Đổi $%s = %s\\text{ (giờ)}$. \\\\
Gọi độ dài quãng đường sông $AB$ là $x\\text{ (km)}$ (điều kiện: $x > 0$). \\\\
- Vận tốc của ca nô khi chạy xuôi dòng là: $%s + %s = %s\\text{ (km/h)}$. \\\\
- Vận tốc của ca nô khi chạy ngược dòng là: $%s - %s = %s\\text{ (km/h)}$. \\\\
- Thời gian ca nô chạy xuôi dòng từ $A$ đến $B$ là $\\frac{x}{%s}\\text{ (giờ)}$ và thời gian ca nô chạy ngược dòng từ $B$ về $A$ là $\\frac{x}{%s}\\text{ (giờ)}$. \\\\
Vì tổng thời gian cả đi và về là $%s$ giờ nên ta có phương trình: \\\\
$\\frac{x}{%s} + \\frac{x}{%s} = %s$. \\\\
Quy đồng mẫu thức hai vế với mẫu chung là $%s$, ta được: \\\\
$%sx + %sx = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy độ dài quãng đường sông $AB$ là $%s\\text{ km}$.'''
                   % (thoi_gian_str, latex(t_frac),
                      v_thuc, v_nuoc, v_xuoi,
                      v_thuc, v_nuoc, v_nguoc,
                      v_xuoi, v_nguoc,
                      latex(t_frac),
                      v_xuoi, v_nguoc, latex(t_frac),
                      bcnn,
                      m1, m2, vp, m1 + m2, vp, S,
                      S))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
