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


def bt_dang12_p4_b2_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [('A', 'B', 'C', 'D', 'E'), ('M', 'N', 'P', 'Q', 'I')]
        d1, d2, d3, d4, diem = random.choice(bo_dinh)
        ten_ht = d1 + d2 + d3 + d4
        day1, day2 = d1 + d2, d3 + d4
        dc1, dc2 = d1 + d3, d2 + d4

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (3.6,0);\n'
            '\\coordinate (A) at (0.8,1.8);\n'
            '\\coordinate (B) at (2.8,1.8);\n'
            '\\coordinate (E) at (1.8,-1.8);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);\n'
            '\\draw[line width=1pt, dashed] (A)--(C) (B)--(D) (C)--(E)--(D);\n'
            '\\fill (A) circle (1pt) node[above left] {$%s$};\n'
            '\\fill (B) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (C) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (D) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (E) circle (1pt) node[below] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (d1, d2, d3, d4, diem)
        )

        noidungcauhoi = (
            'Cho hình thang $%s$ ($%s // %s$). Kẻ đường thẳng vuông góc với $%s$ tại $%s$ và đường thẳng vuông góc với $%s$ tại $%s$, hai đường thẳng này cắt nhau tại $%s$ (như hình vẽ).\\\\\n'
            'a) Nêu tên hai tam giác vuông $\\triangle %s%s%s$ và $\\triangle %s%s%s$.\\\\\n'
            'b) Chứng minh rằng nếu $%s = %s$ thì hình thang $%s$ là hình thang cân. %s'
            % (ten_ht, day1, day2, dc1, d3, dc2, d4, diem, diem, d3, d1, diem, d4, d2, diem+d3, diem+d4, ten_ht, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \\n'
            '\\item Hai tam giác vuông là $\\triangle %s%s%s$ (vuông tại $%s$) và $\\triangle %s%s%s$ (vuông tại $%s$). \\n'
            '\\item Trong hai tam giác vuông $\\triangle %s%s%s$ và $\\triangle %s%s%s$, nếu $%s = %s$ thì theo định lí Pythagore, ta có:\\\\ '
            '$%s^2 = %s^2 + %s^2$ và $%s^2 = %s^2 + %s^2$.\\\\ '
            'Vì $%s = %s$ và $%s = %s$ nên $%s^2 = %s^2$, suy ra $%s = %s$.\\\\ '
            'Theo Định lí $3$, hình thang $%s$ có hai đường chéo bằng nhau nên là hình thang cân. \\n'
            '\\end{enumEX} \\n'
            % (diem, d3, d1, d3, diem, d4, d2, d4, diem, d3, d1, diem, d4, d2, diem+d3, diem+d4, dc1, diem+d3, d1+diem, dc2, diem+d4, d2+diem, diem+d3, diem+d4, d1+diem, d2+diem, dc1, dc2, dc1, dc2, ten_ht)
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
