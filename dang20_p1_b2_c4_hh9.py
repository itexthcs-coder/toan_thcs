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


def bt_dang20_p1_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ac = random.choice([6, 8, 10, 12, 14, 16])
        goc_b = random.choice([30, 45, 60])
        goc_c = 90 - goc_b

        if goc_b == 30:
            hc_val = Rational(ac, 2)
            cos_str = '\\dfrac{1}{2}'
            s = [
                '$%s\\text{ cm}$' % latex(Rational(ac, 2) * sqrt(3)),
                '$%s\\text{ cm}$' % latex(ac * sqrt(3)),
                '$%s\\text{ cm}$' % latex(Rational(ac, 3) * sqrt(3)),
                '$%s\\text{ cm}$' % latex(Rational(ac, 2) * sqrt(2))
            ]
        elif goc_b == 45:
            hc_val = Rational(ac, 2) * sqrt(2)
            cos_str = '\\dfrac{\\sqrt{2}}{2}'
            s = [
                '$%s\\text{ cm}$' % latex(Rational(ac, 2)),
                '$%s\\text{ cm}$' % latex(ac * sqrt(2)),
                '$%s\\text{ cm}$' % latex(Rational(ac, 2) * sqrt(3)),
                '$%s\\text{ cm}$' % latex(ac)
            ]
        else:
            hc_val = Rational(ac, 2) * sqrt(3)
            cos_str = '\\dfrac{\\sqrt{3}}{2}'
            s = [
                '$%s\\text{ cm}$' % latex(Rational(ac, 2)),
                '$%s\\text{ cm}$' % latex(ac * sqrt(3)),
                '$%s\\text{ cm}$' % latex(Rational(ac, 2) * sqrt(2)),
                '$%s\\text{ cm}$' % latex(Rational(ac, 3) * sqrt(3))
            ]

        # Các đáp án trắc nghiệm
        du = ['$%s\\text{ cm}$' % latex(hc_val)]
        da = random.choice(du)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4.5,0);
    \\coordinate (H) at (3.375,0);
    \\coordinate (A) at (3.375,1.95);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(H);
    \\draw[line width=1pt] (3.375,0.22)--(3.595,0.22)--(3.595,0);
    \\draw[line width=1pt] ($(A)!0.22cm!(B)$)--($(A)!0.22cm!(B)+(A)!0.22cm!(C)-(A)$)--($(A)!0.22cm!(C)$);
    \\draw[line width=1pt] (0.55,0) arc (0:30:0.55);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[above right] at (3.95,0.98) {$%s\\text{ cm}$};
    \\node at (0.95,0.22) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (ac, goc_b))

        # Câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$, đường cao $AH$. Biết $AC = %s\\text{ cm}$ và $\\widehat{B} = %s^\\circ$ (như hình vẽ). Độ dài đoạn thẳng $HC$ bằng
    %s''' % (ac, goc_b, hinhve))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ABC$ vuông tại $A$, ta có $\\widehat{B} + \\widehat{C} = 90^\\circ$.\\\\
    Suy ra $\\widehat{C} = 90^\\circ - %s^\\circ = %s^\\circ$.\\\\
    Xét tam giác $AHC$ vuông tại $H$ có cạnh huyền $AC = %s\\text{ cm}$ và $\\widehat{C} = %s^\\circ$.\\\\
    Theo hệ thức giữa cạnh huyền và cạnh góc vuông (Định lí 1), ta có:\\\\
    $HC = AC \\cdot \\cos C = %s \\cdot \\cos %s^\\circ = %s \\cdot %s = %s\\text{ (cm)}$.\\\\
    Vậy $HC = %s\\text{ cm}$.'''
                   % (goc_b, goc_c, ac, goc_c, ac, goc_c, ac, cos_str, latex(hc_val), latex(hc_val)))

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
