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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang19_p1_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        R = random.randint(2, 7)
        he_so = random.choice([2, 3])
        om = he_so * R
        ma_sq = om ** 2 - R ** 2
        ma_val = sqrt(ma_sq)
    
        # Các đáp án trắc nghiệm
        du = ['$%s\\text{ cm}$' % latex(ma_val)]
        da = random.choice(du)
        s_exprs = [
            Rational(R),
            Rational(om),
            sqrt(om ** 2 + R ** 2),
            Rational(om - R)
        ]
        s = ['$%s\\text{ cm}$' % latex(e) for e in s_exprs if e != ma_val]
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Từ điểm $M$ nằm ngoài đường tròn $(O; %s\\text{ cm})$ sao cho $OM = %s\\text{ cm}$, kẻ hai tiếp tuyến $MA, MB$ tới $(O)$ ($A, B$ là các tiếp điểm, như hình vẽ). Độ dài đoạn thẳng $MB$ bằng
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M) at (-3.6,0);
\\coordinate (A) at (-0.9,1.5588);
\\coordinate (B) at (-0.9,-1.5588);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (-4.0,-0.2309)--(0.045,2.1044);
\\draw[line width=1pt] (-4.0,0.2309)--(0.045,-2.1044);
\\draw[line width=1pt] (O)--(A) (O)--(B) (M)--(O);
\\draw[line width=1pt] (-0.775,1.3423)--(-0.9915,1.2173)--(-1.1165,1.4338);
\\draw[line width=1pt] (-0.775,-1.3423)--(-0.9915,-1.2173)--(-1.1165,-1.4338);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\end{tikzpicture}
\\end{center}'''
                         % (R, om))
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Tam giác $OAM$ có $\\widehat{OAM} = 90^\\circ$ (do $MA$ tiếp xúc với đường tròn $(O)$ tại $A$) và $OA = R = %s\\text{ cm}$, $OM = %s\\text{ cm}$.\\\\
Áp dụng định lí Pythagore vào tam giác $OAM$ vuông tại $A$, ta có:
\\begin{align*}
AM^2 + OA^2 &= OM^2 \\\\
AM^2 &= OM^2 - OA^2 = %s^2 - %s^2 = %s \\\\
AM &= \\sqrt{%s} = %s\\text{ (cm)}.
\\end{align*}
Theo Định lí $2$ (tính chất của hai tiếp tuyến cắt nhau), ta có $MB = MA = %s\\text{ cm}$.'''
                   % (R, om, om, R, ma_sq, ma_sq, latex(ma_val), latex(ma_val)))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
