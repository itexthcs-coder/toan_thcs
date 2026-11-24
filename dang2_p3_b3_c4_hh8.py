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

def bt_dang2_p3_b3_c4_hh8(self):
    # Dạng 2: Tìm tham số đại số x trong biểu thức độ dài đoạn thẳng qua tính chất đường phân giác
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (6, 9, 2, 3, 1, 2, 1, 1),
            (8, 12, 2, 3, 2, 4, 0, 2),
            (10, 15, 2, 3, 3, 6, -1, 3),
            (9, 12, 3, 4, 2, 3, 1, 2),
            (12, 16, 3, 4, 3, 4, 2, 3)
        ]
        ab, ac, p, q, c1, c2, c3, x_val = random.choice(bo_so)
        kq_str = fmt_num(x_val)
        str_c3 = '+ %s' % c3 if c3 > 0 else ('- %s' % abs(c3) if c3 < 0 else '')

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (1.5,3.2);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.6,0);\n'
            '\\coordinate (D) at (1.84,0);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Đường phân giác của góc $A$ cắt cạnh $BC$ tại $D$ sao cho $BD = x + %s\\text{ (cm)}$ và $CD = %sx %s\\text{ (cm)}$. Tìm giá trị của $x$.\n%s'
            % (ab, ac, c1, c2, str_c3, hinh_ve)
        )

        loigiai = (
            'Trong tam giác $ABC$ có $AD$ là đường phân giác của góc $A$ ($D \\in BC$).\\\\'
            'Theo tính chất đường phân giác của tam giác, ta có: $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{%s}{%s} = \\frac{%s}{%s}$.\\\\'
            'Thay $BD = x + %s$ và $CD = %sx %s$ vào tỉ lệ thức, ta được: $\\frac{x + %s}{%sx %s} = \\frac{%s}{%s}$.\\\\'
            'Suy ra $%s(x + %s) = %s(%sx %s) \\Leftrightarrow %sx + %s = %sx %s \\Leftrightarrow x = %s$.'
            % (ab, ac, p, q, c1, c2, str_c3, c1, c2, str_c3, p, q, q, c1, p, c2, str_c3, q, q * c1, p * c2, ('+ %s' % (p * c3) if p * c3 > 0 else ('- %s' % abs(p * c3) if p * c3 < 0 else '')), kq_str)
        )

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
