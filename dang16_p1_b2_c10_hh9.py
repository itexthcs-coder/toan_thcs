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


def bt_dang16_p1_b2_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        R = random.choice([3, 4, 5])
        d = 2 * R
        h = 3 * d
        V_tru = Decimal(str(math.pi * (R**2) * h)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        V_bong = Decimal(str(3 * (4 / 3) * math.pi * (R**3))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        V_trong = V_tru - V_bong

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-1,0) arc (180:360:1cm and 0.3cm);
\\draw[line width=1pt, dashed] (1,0) arc (0:180:1cm and 0.3cm);
\\draw[line width=1pt] (0,6) ellipse (1cm and 0.3cm);
\\draw[line width=1pt] (-1,0)--(-1,6) (1,0)--(1,6);
\\draw[line width=1pt] (0,1) circle (1cm);
\\draw[line width=1pt] (0,3) circle (1cm);
\\draw[line width=1pt] (0,5) circle (1cm);
\\end{tikzpicture}
\\end{center}''')

        du = ['$%s\\text{ cm}^3$' % (V_trong)]
        da = random.choice(du)
        s = [
            '$%s\\text{ cm}^3$' % (V_tru),
            '$%s\\text{ cm}^3$' % (V_bong),
            '$%s\\text{ cm}^3$' % (V_trong + Decimal('50')),
            '$%s\\text{ cm}^3$' % (V_trong - Decimal('40'))
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Một hộp đựng bóng tennis có dạng hình trụ chứa vừa khít ba quả bóng tennis xếp theo chiều dọc. Các quả bóng tennis có dạng hình cầu, đường kính $%s\\text{ cm}$. Thể tích bên trong hộp đựng bóng không bị chiếm bởi ba quả bóng tennis là (bỏ qua bề dày của vỏ hộp, làm tròn kết quả đến hàng đơn vị của $\\text{cm}^3$)%s'''
                         % (d, hinh_ve))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Chiều cao hộp đựng bóng hình trụ là: $h = %s \\cdot 3 = %s\\text{ (cm)}$.\\\\
Bán kính đáy hộp đựng bóng hình trụ là: $R = %s : 2 = %s\\text{ (cm)}$.\\\\
Thể tích hộp đựng bóng hình trụ là:
$$V = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s \\approx %s\\text{ (cm}^3\\text{)}.$$
Thể tích của ba quả bóng tennis có dạng hình cầu là:
$$V' = 3 \\cdot \\left(\\dfrac{4}{3}\\pi R^3\\right) = 3 \\cdot \\left(\\dfrac{4}{3}\\pi \\cdot %s^3\\right) \\approx %s\\text{ (cm}^3\\text{)}.$$
Thể tích bên trong hộp đựng bóng không bị chiếm bởi ba quả bóng tennis là:
$$V'' = V - V' \\approx %s - %s = %s\\text{ (cm}^3\\text{)}.$$'''
                   % (d, h, d, R, R, h, V_tru, R, V_bong, V_tru, V_bong, V_trong))
    
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
