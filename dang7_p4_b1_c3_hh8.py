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


def bt_dang7_p4_b1_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [('A', 'B', 'C', 'D'), ('M', 'N', 'P', 'Q'), ('E', 'F', 'G', 'H')]
        d1, d2, d3, d4 = random.choice(bo_dinh)
        ten_tg = d1 + d2 + d3 + d4
        g1 = random.randint(95, 115)
        g2 = random.randint(85, 105)
        tong_34 = 360 - (g1 + g2)
        # Chọn k sao cho 5*k = tong_34 nếu chia hết cho 5, nếu không chỉnh g2
        rem = tong_34 % 5
        if rem != 0:
            g2 += rem
            tong_34 = 360 - (g1 + g2)
        k = tong_34 // 5
        g3 = 2 * k
        g4 = 3 * k

        hinh_ve = '''
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (3.2,0);
        \\coordinate (C) at (2.8,2.1);
        \\coordinate (D) at (0.4,2.0);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);
        \\fill (A) circle (1pt) node[below left] {$%s$} node[above right] {$%s^\\circ$};
        \\fill (B) circle (1pt) node[below right] {$%s$} node[above left] {$%s^\\circ$};
        \\fill (C) circle (1pt) node[above right] {$%s$};
        \\fill (D) circle (1pt) node[above left] {$%s$};
        \\end{tikzpicture}
        \\end{center}''' % (d1, g1, d2, g2, d3, d4)

        noidungcauhoi = ('''Cho tứ giác $%s$ có $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$ và $\\dfrac{\\widehat{%s}}{2} = \\dfrac{\\widehat{%s}}{3}$ (như hình vẽ).\\\\
                         a) Tính tổng số đo hai góc $\\widehat{%s} + \\widehat{%s}$.\\\\
                         b) Tính số đo các góc $\\widehat{%s}$ và $\\widehat{%s}$. %s'''
                         % (ten_tg, d1, g1, d2, g2, d3, d4, d3, d4, d3, d4, hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1} \\n
                   \\item Trong tứ giác $%s$, ta có:\\\\
                   $\\widehat{%s} + \\widehat{%s} = 360^\\circ - (\\widehat{%s} + \\widehat{%s}) = 360^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$. \\n
                   \\item Áp dụng tính chất dãy tỉ số bằng nhau, ta có:\\\\
                   $\\dfrac{\\widehat{%s}}{2} = \\dfrac{\\widehat{%s}}{3} = \\dfrac{\\widehat{%s} + \\widehat{%s}}{2 + 3} = \\dfrac{%s^\\circ}{5} = %s^\\circ$.\\\\
                   Suy ra $\\widehat{%s} = 2 \\cdot %s^\\circ = %s^\\circ$ và $\\widehat{%s} = 3 \\cdot %s^\\circ = %s^\\circ$.\\\\
                   Vậy $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$. \\n
                   \\end{enumEX} \\n'''
                   % (ten_tg, d3, d4, d1, d2, g1, g2, tong_34,
                      d3, d4, d3, d4, tong_34, k,
                      d3, k, g3, d4, k, g4, d3, g3, d4, g4))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
