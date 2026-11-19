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


def bt_dang13_p3_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_pythagore = [(6, 8, 10), (8, 15, 17), (5, 12, 13), (9, 12, 15), (7, 24, 25), (12, 16, 20)]
        r_10, hm_10, om_10 = random.choice(bo_pythagore)
        r_val = Rational(r_10, 10)
        hm_val = Rational(hm_10, 10)
        om_val = Rational(om_10, 10)
        
        r_str = str(Decimal(float(r_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        hm_str = str(Decimal(float(hm_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        om_str = str(Decimal(float(om_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        r2_str = str(Decimal(float(r_val**2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        hm2_str = str(Decimal(float(hm_val**2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        kq_str = om_str

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,1.5);
\\coordinate (H) at (0,0);
\\coordinate (M) at (2.8,0);
\\draw[line width=1pt] (-2,0)--(4,0);
\\draw[line width=1pt] (O) circle (1.5);
\\draw[line width=1pt, dashed] (O)--(H) (O)--(M);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (M) circle (1pt) node[below] {$M$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một xe lu làm đường có bánh lăn hình trụ bán kính $R = %s\\text{ m}$. Khi xe lu đứng yên trên mặt đường phẳng nằm ngang, một viên đá nhỏ nằm trên mặt đường cách điểm tiếp xúc giữa bánh xe và mặt đường một khoảng $%s\\text{ m}$. Tính khoảng cách từ tâm trục bánh xe lu đến viên đá đó (đơn vị: mét).'''
                         %(r_str, hm_str))
        
        # Nội dung lời giải
        loigiai = ('''%s
Gọi $O$ là tâm trục bánh xe lu, $H$ là điểm tiếp xúc giữa bánh xe và mặt đường, $M$ là vị trí viên đá trên mặt đường. \\\\
Vì mặt đường tiếp xúc với bánh xe tại $H$ nên mặt đường là tiếp tuyến của đường tròn $(O; R)$ tại $H$, suy ra $OH \\perp HM$ tại $H$ với $OH = %s\\text{ m}$ và $HM = %s\\text{ m}$. \\\\
Áp dụng định lí Pythagore vào tam giác $OHM$ vuông tại $H$, ta có: \\\\
$OM = \\sqrt{OH^2 + HM^2} = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s + %s} = %s\\text{ (m)}$.'''
                   %(hinhve, r_str, hm_str, r_str, hm_str, r2_str, hm2_str, om_str))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
