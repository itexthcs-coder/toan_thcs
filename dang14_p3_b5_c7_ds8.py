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


def bt_dang14_p3_b5_c7_ds8(self):
    # Dang 14: Tim toa do diem co dinh ma ho duong thang luon di qua
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([-4, -3, -2, 2, 3, 4])
        c = -x0
        k = random.choice([2, 3, 4])
        y0 = random.choice([2, 3, 4, 5, 6])
        d = y0 + k * x0
        ans = x0 + y0
        
        s_c = '+' if c >= 0 else '-'
        s_d = '+' if d >= 0 else '-'
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3,0) -- (2.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-2.5,0.5) -- (1.5,3);\n'
            '\\draw[line width=1pt] (-2.5,2.8) -- (1.5,0.2);\n'
            '\\draw[line width=1pt, dashed] (-1.2,-0.5) -- (-1.2,3.2);\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (-1.2,1.3) circle (1pt) node[above] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho đường thẳng $(d): y = (m - %s)x + %sm %s %s$. Biết rằng với mọi giá trị của tham số $m$, '
            'đường thẳng $(d)$ luôn đi qua một điểm cố định $I(x_0; y_0)$. Tính tổng $x_0 + y_0$.\n%s'
            % (k, c, s_d, abs(d), tikz)
        )
        
        loigiai = (
            'Giả sử $I(x_0; y_0)$ là điểm cố định mà đường thẳng $(d)$ luôn đi qua với mọi $m$. Khi đó ta có:\\ '
            '$y_0 = (m - %s)x_0 + %sm %s %s$ với mọi $m$\\ '
            '$\\Leftrightarrow (x_0 %s %s)m + (-%sx_0 - y_0 %s %s) = 0$ với mọi $m$.\\ '
            'Điều này xảy ra khi và chỉ khi:\\ '
            '$\\begin{cases} x_0 %s %s = 0 \\\\ -%sx_0 - y_0 %s %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x_0 = %s \\\\ y_0 = %s \\end{cases}$.\\ '
            'Vậy điểm cố định là $I(%s; %s)$ và tổng $x_0 + y_0 = %s + %s = %s$.'
            % (k, c, s_d, abs(d), s_c, abs(c), k, s_d, abs(d), s_c, abs(c), k, s_d, abs(d), x0, y0, x0, y0, x0, y0, ans)
        )
        
        dapan = '\\shortans[0]{$%s$}\n' % ans

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
