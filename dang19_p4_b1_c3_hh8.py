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


def bt_dang19_p4_b1_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [('A', 'B', 'C', 'D'), ('M', 'N', 'P', 'Q'), ('E', 'F', 'G', 'H')]
        d1, d2, d3, d4 = random.choice(bo_dinh)
        ten_tg = d1 + d2 + d3 + d4
        gn1 = random.randint(70, 90)
        gn2 = random.randint(80, 100)
        gn3 = random.randint(85, 105)
        gn4 = 360 - (gn1 + gn2 + gn3)
        gt1 = 180 - gn1
        gt2 = 180 - gn2
        gt3 = 180 - gn3
        gt4 = 180 - gn4

        hinh_ve = '''
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0.8,0.8);
        \\coordinate (B) at (3.2,0.8);
        \\coordinate (C) at (2.8,2.5);
        \\coordinate (D) at (1.0,2.4);
        \\draw[line width=1pt] (0,0.8)--(B)--(3.2,0) (B)--(C)--(3.6,2.5) (C)--(D)--(1.0,3.2) (D)--(A)--(0.8,0);
        \\fill (A) circle (1pt) node[above right] {$%s$};
        \\fill (B) circle (1pt) node[above left] {$%s$};
        \\fill (C) circle (1pt) node[below left] {$%s$};
        \\fill (D) circle (1pt) node[below right] {$%s$};
        \\end{tikzpicture}
        \\end{center}''' % (d1, d2, d3, d4)

        noidungcauhoi = ('''Cho tứ giác $%s$ có các góc ngoài tại bốn đỉnh $%s, %s, %s, %s$ (mỗi đỉnh lấy một góc ngoài kề bù với góc trong, như hình vẽ). Biết ba góc ngoài tại $%s, %s, %s$ lần lượt bằng $%s^\\circ$, $%s^\\circ$, $%s^\\circ$.\\\\
                         a) Tính số đo góc ngoài thứ tư tại đỉnh $%s$.\\\\
                         b) Tính số đo cả bốn góc trong của tứ giác $%s$. %s'''
                         % (ten_tg, d1, d2, d3, d4, d1, d2, d3, gn1, gn2, gn3, d4, ten_tg, hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1} \\n
                   \\item Tổng số đo bốn góc ngoài của một tứ giác bằng $360^\\circ$ nên góc ngoài tại đỉnh $%s$ bằng:\\\\
                   $360^\\circ - (%s^\\circ + %s^\\circ + %s^\\circ) = 360^\\circ - %s^\\circ = %s^\\circ$. \\n
                   \\item Vì góc trong và góc ngoài tại mỗi đỉnh kề bù nhau nên:\\\\
                   $\\widehat{%s} = 180^\\circ - %s^\\circ = %s^\\circ$; $\\widehat{%s} = 180^\\circ - %s^\\circ = %s^\\circ$; $\\widehat{%s} = 180^\\circ - %s^\\circ = %s^\\circ$; $\\widehat{%s} = 180^\\circ - %s^\\circ = %s^\\circ$.\\\\
                   Vậy $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$, $\\widehat{%s} = %s^\\circ$. \\n
                   \\end{enumEX} \\n'''
                   % (d4, gn1, gn2, gn3, gn1+gn2+gn3, gn4,
                      d1, gn1, gt1, d2, gn2, gt2, d3, gn3, gt3, d4, gn4, gt4,
                      d1, gt1, d2, gt2, d3, gt3, d4, gt4))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
