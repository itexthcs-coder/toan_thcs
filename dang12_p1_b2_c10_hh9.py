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


def bt_dang12_p1_b2_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        R = randint(8, 15)
        d = 2 * R
        tu, mau = random.choice([(2, 3), (3, 4), (3, 5)])
        V_cau = (4 / 3) * math.pi * (R**3)
        V_nuoc = Decimal(str(V_cau * tu / mau)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        V_cau_round = Decimal(str(V_cau)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        V_wrong2 = Decimal(str(V_cau * (mau - tu) / mau)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-1.3,1.5) arc (140:400:2cm);
\\draw[line width=1pt] (-1.3,1.5) arc (180:360:1.3cm and 0.3cm);
\\draw[line width=1pt, dashed] (1.3,1.5) arc (0:180:1.3cm and 0.3cm);
\\draw[line width=1pt] (-1.95,0.4) arc (180:360:1.95cm and 0.4cm);
\\draw[line width=1pt, dashed] (1.95,0.4) arc (0:180:1.95cm and 0.4cm);
\\end{tikzpicture}
\\end{center}''')

        du = ['$%s\\text{ cm}^3$' % (V_nuoc)]
        da = random.choice(du)
        s = [
            '$%s\\text{ cm}^3$' % (V_cau_round),
            '$%s\\text{ cm}^3$' % (V_wrong2),
            '$%s\\text{ cm}^3$' % (V_nuoc + Decimal('250')),
            '$%s\\text{ cm}^3$' % (V_nuoc - Decimal('180'))
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Bạn Trang có một bể cá có dạng một phần hình cầu với đường kính bằng $%s\\text{ cm}$. Khi nuôi cá, Trang thường đổ vào bể lượng nước có thể tích bằng $\\dfrac{%s}{%s}$ thể tích của hình cầu. Thể tích nước bạn Trang đã đổ vào bể cá là (làm tròn kết quả đến hàng đơn vị của $\\text{cm}^3$)%s'''
                         % (d, tu, mau, hinh_ve))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Bán kính của hình cầu là: $R = %s : 2 = %s\\text{ (cm)}$.\\\\
Thể tích của hình cầu là:
$$V = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = \\dfrac{%s\\pi}{3}\\text{ (cm}^3\\text{)}.$$
Thể tích nước bạn Trang sử dụng để đổ vào bể cá là:
$$V_{\\text{nước}} = \\dfrac{%s}{%s} \\cdot \\dfrac{%s\\pi}{3} \\approx %s\\text{ (cm}^3\\text{)}.$$'''
                   % (d, R, R, 4 * (R**3), tu, mau, 4 * (R**3), V_nuoc))
    
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
