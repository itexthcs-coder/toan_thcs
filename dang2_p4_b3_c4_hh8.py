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

def bt_dang2_p4_b3_c4_hh8(self):
    # Dạng 2: Chứng minh tỉ lệ thức và hình thoi trong tam giác có phân giác và đường thẳng song song
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'D', 'E', 'F'),
            ('M', 'N', 'P', 'D', 'E', 'F')
        ]
        A, B, C, D, E, F = random.choice(bo_dinh)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (1.5,3.2);\n'
            '\\coordinate (%s) at (0,0);\n'
            '\\coordinate (%s) at (4.6,0);\n'
            '\\coordinate (%s) at (1.84,0);\n'
            '\\coordinate (%s) at ($(%s)!0.4!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.6!(%s)$);\n'
            '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s) (%s)--(%s);\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above left] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, D, E, A, C, F, A, B, A, B, C, A, D, D, E, D, F, A, A, B, B, C, C, D, D, E, E, F, F)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ ($%s%s < %s%s$), đường phân giác $%s%s$ ($%s \\in %s%s$). Đường thẳng qua $%s$ song song với $%s%s$ cắt cạnh $%s%s$ tại $%s$; đường thẳng qua $%s$ song song với $%s%s$ cắt cạnh $%s%s$ tại $%s$.\\\\\n'
            'a) Chứng minh rằng $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$ và $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\\n'
            'b) Chứng minh tứ giác $%s%s%s%s$ là hình thoi và $\\frac{1}{%s%s} + \\frac{1}{%s%s} = \\frac{1}{%s%s}$.\n%s'
            % (A, B, C, A, B, A, C, A, D, D, B, C, D, A, B, A, C, E, D, A, C, A, B, F, E, C, E, A, A, C, A, B, F, B, F, A, A, B, A, C, A, E, D, F, A, B, A, C, A, E, hinh_ve)
        )

        p1 = (
            '\\item Trong tam giác $%s%s%s$ có $%s%s$ là đường phân giác của góc $%s$ nên $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$ và $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\'
            % (A, B, C, A, D, A, D, C, D, B, A, C, A, B, D, B, D, C, A, B, A, C)
        )
        p2 = (
            'Vì $%s%s // %s%s$ nên theo định lí Thalès, ta có $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\'
            % (D, E, A, B, E, C, E, A, D, C, D, B, A, C, A, B)
        )
        p3 = (
            'Vì $%s%s // %s%s$ nên theo định lí Thalès, ta có $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$ (điều phải chứng minh). \n'
            % (D, F, A, C, F, B, F, A, D, B, D, C, A, B, A, C)
        )
        p4 = (
            '\\item Tứ giác $%s%s%s%s$ có $%s%s // %s%s$ và $%s%s // %s%s$ nên là hình bình hành. Lại có đường chéo $%s%s$ là tia phân giác của góc $%s%s%s$ nên $%s%s%s%s$ là hình thoi, suy ra $%s%s = %s%s = %s%s = %s%s$.\\\\'
            % (A, E, D, F, D, E, A, F, D, F, A, E, A, D, E, A, F, A, E, D, F, A, E, E, D, D, F, F, A)
        )
        p5 = (
            'Từ $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s} \\Rightarrow \\frac{%s%s - %s%s}{%s%s} = \\frac{%s%s}{%s%s} \\Rightarrow \\frac{%s%s}{%s%s} - 1 = \\frac{%s%s}{%s%s} \\Rightarrow \\frac{%s%s}{%s%s} = 1 + \\frac{%s%s}{%s%s} = \\frac{%s%s + %s%s}{%s%s}$.\\\\'
            % (E, C, E, A, A, C, A, B, A, C, A, E, A, E, A, C, A, B, A, C, A, E, A, C, A, B, A, C, A, E, A, C, A, B, A, B, A, C, A, B)
        )
        p6 = (
            'Chia hai vế cho $%s%s$, ta được $\\frac{1}{%s%s} = \\frac{1}{%s%s} + \\frac{1}{%s%s}$ (điều phải chứng minh). \n'
            % (A, C, A, E, A, C, A, B)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + p5 + p6 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
