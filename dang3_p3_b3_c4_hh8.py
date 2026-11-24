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

def bt_dang3_p3_b3_c4_hh8(self):
    # Dạng 3: Tính độ dài đoạn thẳng phân giác ngoài kết hợp đường phân giác trong tại cùng một đỉnh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (6, 12, 9, 3, 9, 12),
            (6, 10, 8, 3, 12, 15),
            (4, 6, 5, 2, 10, 12),
            (8, 12, 10, 4, 20, 24),
            (9, 15, 12, 4.5, 18, 22.5)
        ]
        ab, ac, bc, bd, d1b, dd1 = random.choice(bo_so)
        s_bd = fmt_num(bd)
        s_d1b = fmt_num(d1b)
        kq_str = fmt_num(dd1)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (3.2,2.2);\n'
            '\\coordinate (B) at (2.8,0);\n'
            '\\coordinate (C) at (6.2,0);\n'
            '\\coordinate (D) at (4.1,0);\n'
            '\\coordinate (D1) at (0,0);\n'
            '\\draw[line width=1pt] (D1)--(C) (A)--(B) (A)--(C) (A)--(D) (D1)--(A);\n'
            '\\fill (A) circle (1pt) node[above right] {$A$};\n'
            '\\fill (B) circle (1pt) node[below] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (D1) circle (1pt) node[above left] {$D\'$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$, $BC = %s\\text{ cm}$. Tia phân giác trong và tia phân giác ngoài của góc $A$ cắt đường thẳng $BC$ lần lượt tại $D$ và $D\'$ ($B$ nằm giữa $D\'$ và $C$). Tính độ dài đoạn thẳng $DD\'$ (đơn vị: $\\text{cm}$).\n%s'
            % (ab, ac, bc, hinh_ve)
        )

        loigiai = (
            'Vì $AD$ là tia phân giác trong của góc $A$ nên $\\frac{BD}{CD} = \\frac{AB}{AC} = \\frac{%s}{%s}$, kết hợp $BD + CD = %s\\text{ cm}$ suy ra $BD = %s\\text{ cm}$.\\\\'
            'Vì $AD\'$ là tia phân giác ngoài của góc $A$ nên $\\frac{D\'B}{D\'C} = \\frac{AB}{AC} = \\frac{%s}{%s}$. Vì điểm $B$ nằm giữa $D\'$ và $C$ nên $D\'C = D\'B + %s$.\\\\'
            'Thay vào tỉ lệ thức ta được $\\frac{D\'B}{D\'B + %s} = \\frac{%s}{%s}$, suy ra $D\'B = %s\\text{ cm}$.\\\\'
            'Vì điểm $B$ nằm giữa $D\'$ và $D$ nên $DD\' = D\'B + BD = %s + %s = %s\\text{ cm}$.'
            % (ab, ac, bc, s_bd, ab, ac, bc, bc, ab, ac, s_d1b, s_d1b, s_bd, kq_str)
        )

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
