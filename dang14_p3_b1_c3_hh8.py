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


def bt_dang14_p3_b1_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [('A', 'B', 'C', 'D', 'I'), ('M', 'N', 'P', 'Q', 'K'), ('E', 'F', 'G', 'H', 'O')]
        d1, d2, d3, d4, giao = random.choice(bo_dinh)
        ten_tg = d1 + d2 + d3 + d4
        g1 = random.choice([90, 100, 110, 120])
        g2 = random.choice([80, 90, 100, 110])
        tong_34 = 360 - (g1 + g2)
        nua_34 = tong_34 // 2
        kq = 180 - nua_34
        kq_str = str(kq)

        hinh_ve = '''
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (3.4,0);
        \\coordinate (C) at (2.8,2.2);
        \\coordinate (D) at (0.4,2);
        \\coordinate (I) at (1.7,1.1);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
        \\draw[line width=1pt, dashed] (C)--(I)--(D);
        \\fill (A) circle (1pt) node[below left] {$%s$} node[above right] {$%s^\\circ$};
        \\fill (B) circle (1pt) node[below right] {$%s$} node[above left] {$%s^\\circ$};
        \\fill (C) circle (1pt) node[above right] {$%s$};
        \\fill (D) circle (1pt) node[above left] {$%s$};
        \\fill (I) circle (1pt) node[below] {$%s$};
        \\end{tikzpicture}
        \\end{center}''' % (d1, g1, d2, g2, d3, d4, giao)

        noidungcauhoi = ('''Cho tứ giác $%s$ có $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$. Các tia phân giác của $\\widehat{%s}$ và $\\widehat{%s}$ cắt nhau tại $%s$ (như hình vẽ). Tính số đo góc $\\widehat{%s%s%s}$ (đơn vị: độ). %s'''
                         % (ten_tg, d1, g1, d2, g2, d3, d4, giao, d3, giao, d4, hinh_ve))

        loigiai = ('''Trong tứ giác $%s$, ta có $\\widehat{%s} + \\widehat{%s} = 360^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.\\\\
                   Trong $\\triangle %s%s%s$, tổng $\\widehat{%s%s%s} + \\widehat{%s%s%s} = \\dfrac{\\widehat{%s} + \\widehat{%s}}{2} = \\dfrac{%s^\\circ}{2} = %s^\\circ$.\\\\
                   Suy ra $\\widehat{%s%s%s} = 180^\\circ - %s^\\circ = %s^\\circ$.\\\\
                   Vậy $\\widehat{%s%s%s} = %s^\\circ$.'''
                   % (ten_tg, d3, d4, g1, g2, tong_34, giao, d3, d4, giao, d3, d4, giao, d4, d3, d3, d4, tong_34, nua_34, d3, giao, d4, nua_34, kq_str, d3, giao, d4, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
