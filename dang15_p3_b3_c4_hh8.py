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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang15_p3_b3_c4_hh8(self):
    # Dạng 15: Tính tổng chu vi của dãy tam giác trung bình lồng nhau
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        c3 = random.choice([12, 14, 16, 18, 20, 24])
        c2 = 2 * c3
        c1 = 4 * c3
        tong = c1 + c2 + c3
        kq_str = fmt_num(tong)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A1) at (1.8,3.4);\n'
            '\\coordinate (B1) at (0,0);\n'
            '\\coordinate (C1) at (4.6,0);\n'
            '\\coordinate (A2) at ($(B1)!0.5!(C1)$);\n'
            '\\coordinate (B2) at ($(A1)!0.5!(C1)$);\n'
            '\\coordinate (C2) at ($(A1)!0.5!(B1)$);\n'
            '\\coordinate (A3) at ($(B2)!0.5!(C2)$);\n'
            '\\coordinate (B3) at ($(A2)!0.5!(C2)$);\n'
            '\\coordinate (C3) at ($(A2)!0.5!(B2)$);\n'
            '\\draw[line width=1pt] (A1)--(B1)--(C1)--cycle (A2)--(B2)--(C2)--cycle (A3)--(B3)--(C3)--cycle;\n'
            '\\fill (A1) circle (1pt) node[above] {$A_1$};\n'
            '\\fill (B1) circle (1pt) node[below left] {$B_1$};\n'
            '\\fill (C1) circle (1pt) node[below right] {$C_1$};\n'
            '\\fill (A2) circle (1pt) node[below] {$A_2$};\n'
            '\\fill (B2) circle (1pt) node[right] {$B_2$};\n'
            '\\fill (C2) circle (1pt) node[left] {$C_2$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $A_1B_1C_1$ có chu vi bằng $%s\\text{ cm}$. Tam giác $A_2B_2C_2$ có các đỉnh là trung điểm ba cạnh của tam giác $A_1B_1C_1$; tam giác $A_3B_3C_3$ có các đỉnh là trung điểm ba cạnh của tam giác $A_2B_2C_2$. Tính tổng chu vi của cả ba tam giác đó (đơn vị: $\\text{cm}$).\n%s'
            % (c1, hinh_ve)
        )

        loigiai = (
            'Vì ba cạnh của tam giác $A_2B_2C_2$ là ba đường trung bình của tam giác $A_1B_1C_1$ nên chu vi tam giác $A_2B_2C_2$ bằng $\\frac{1}{2}$ chu vi tam giác $A_1B_1C_1$, tức là $C_2 = \\frac{%s}{2} = %s\\text{ cm}$.\\\\'
            'Tương tự, chu vi tam giác $A_3B_3C_3$ bằng $\\frac{1}{2}$ chu vi tam giác $A_2B_2C_2$, tức là $C_3 = \\frac{%s}{2} = %s\\text{ cm}$.\\\\'
            'Vậy tổng chu vi của cả ba tam giác là $%s + %s + %s = %s\\text{ cm}$.'
            % (c1, c2, c2, c3, c1, c2, c3, kq_str)
        )

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
