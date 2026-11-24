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

def bt_dang10_p4_b3_c4_hh8(self):
    # Dạng 10: Chứng minh hệ thức tỉ lệ giữa phân giác trong và phân giác ngoài tại cùng một đỉnh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'D', 'O'),
            ('M', 'N', 'P', 'E', 'O')
        ]
        A, B, C, D, O = random.choice(bo_dinh)
        D_prime = D + "'"

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (3.2,2.2);\n'
            '\\coordinate (%s) at (2.8,0);\n'
            '\\coordinate (%s) at (6.2,0);\n'
            '\\coordinate (%s) at (4.1,0);\n'
            '\\coordinate (D1) at (0,0);\n'
            '\\coordinate (%s) at (2.05,0);\n'
            '\\draw[line width=1pt] (D1)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s) (D1)--(%s);\n'
            '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (D1) circle (1pt) node[above left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, D, O, C, A, B, A, C, A, D, A, A, A, B, B, C, C, D, D, D_prime, O, O)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ ($%s%s < %s%s$). Đường phân giác trong và đường phân giác ngoài của góc $%s$ cắt đường thẳng $%s%s$ lần lượt tại $%s$ và $%s$ ($%s$ nằm giữa $%s$ và $%s$). Gọi $%s$ là trung điểm của đoạn thẳng $%s%s$.\\\\\n'
            'a) Chứng minh rằng $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$ và $\\widehat{%s%s%s} = 90^\\circ$.\\\\\n'
            'b) Chứng minh $%s%s \\cdot %s%s = %s%s^2$.\n%s'
            % (A, B, C, A, B, A, C, A, B, C, D, D_prime, B, D_prime, C, O, D, D_prime, D, B, D, C, D_prime, B, D_prime, C, D, A, D_prime, O, B, O, C, O, D, hinh_ve)
        )

        p1 = (
            '\\item Trong tam giác $%s%s%s$, theo tính chất đường phân giác trong ta có $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$, và theo tính chất đường phân giác ngoài ta có $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$. Suy ra $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s}$.\\\\'
            % (A, B, C, D, B, D, C, A, B, A, C, D_prime, B, D_prime, C, A, B, A, C, D, B, D, C, D_prime, B, D_prime, C)
        )
        p2 = (
            'Mặt khác, $%s%s$ và $%s%s$ là hai tia phân giác của hai góc kề bù (góc trong và góc ngoài tại đỉnh $%s$) nên $%s%s \\perp %s%s$, tức là $\\widehat{%s%s%s} = 90^\\circ$ (điều phải chứng minh). \n'
            % (A, D, A, D_prime, A, A, D, A, D_prime, D, A, D_prime)
        )
        p3 = (
            '\\item Xét tam giác $%s%s%s$ vuông tại $%s$ có $%s%s$ là đường trung tuyến ứng với cạnh huyền $%s%s$ nên $%s%s = %s%s = %s%s$, suy ra tam giác $%s%s%s$ cân tại $%s$, do đó $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\'
            % (D, A, D_prime, A, A, O, D, D_prime, O, A, O, D, O, D_prime, O, A, D, O, O, A, D, O, D, A)
        )
        p4 = (
            'Mà $\\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s}$ (góc ngoài tam giác $%s%s%s$) và $\\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s}$ (do $%s%s$ là phân giác góc $%s%s%s$).\\\\'
            % (O, D, A, D, A, C, A, C, D, A, C, D, O, A, D, O, A, B, B, A, D, A, D, B, A, C)
        )
        p5 = (
            'Suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s}$, do đó $\\Delta %s%s%s \\sim \\Delta %s%s%s$ (g.g).\\\\'
            % (O, A, B, A, C, O, O, A, B, O, C, A)
        )
        p6 = (
            'Từ hai tam giác đồng dạng suy ra $\\frac{%s%s}{%s%s} = \\frac{%s%s}{%s%s} \\Rightarrow %s%s \\cdot %s%s = %s%s^2$. Mà $%s%s = %s%s$ nên $%s%s \\cdot %s%s = %s%s^2$ (điều phải chứng minh). \n'
            % (O, B, O, A, O, A, O, C, O, B, O, C, O, A, O, A, O, D, O, B, O, C, O, D)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + p5 + p6 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
