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

def bt_dang6_p4_b3_c4_hh8(self):
    # Dạng 6: Kết hợp đường trung bình và trực tâm tam giác để chứng minh quan hệ vuông góc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'D', 'E', 'H', 'M', 'N', 'P'),
            ('M', 'N', 'P', 'E', 'F', 'H', 'I', 'K', 'L')
        ]
        A, B, C, D, E, H, M, N, P = random.choice(bo_dinh)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (1.6,3.4);\n'
            '\\coordinate (%s) at (0,0);\n'
            '\\coordinate (%s) at (4.6,0);\n'
            '\\coordinate (%s) at (3.25,1.53);\n'
            '\\coordinate (%s) at (0.85,1.81);\n'
            '\\coordinate (%s) at (intersection of %s--%s and %s--%s);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s) (%s)--(%s)--(%s)--cycle;\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[right] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, D, E, H, B, D, C, E, M, B, C, N, B, H, P, C, H, A, B, C, B, D, C, E, M, N, P, A, A, B, B, C, C, D, D, E, E, H, H, M, M, N, N, P, P)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ nhọn ($%s%s < %s%s$), hai đường cao $%s%s$ và $%s%s$ cắt nhau tại trực tâm $%s$. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$.\\\\\n'
            'a) Chứng minh $%s%s // %s%s$ và $%s%s // %s%s$.\\\\\n'
            'b) Chứng minh $%s%s \\perp %s%s$ và tam giác $%s%s%s$ vuông tại $%s$.\n%s'
            % (A, B, C, A, B, A, C, B, D, C, E, H, M, N, P, B, C, B, H, C, H, N, P, B, C, M, N, C, H, M, N, A, B, N, M, P, N, hinh_ve)
        )

        p1 = (
            '\\item Xét tam giác $%s%s%s$ có $%s$ là trung điểm của $%s%s$ và $%s$ là trung điểm của $%s%s$ nên $%s%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s%s // %s%s$.\\\\'
            % (H, B, C, N, B, H, P, C, H, N, P, H, B, C, N, P, B, C)
        )
        p2 = (
            'Xét tam giác $%s%s%s$ có $%s$ là trung điểm của $%s%s$ và $%s$ là trung điểm của $%s%s$ nên $%s%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s%s // %s%s$ (điều phải chứng minh). \n'
            % (H, B, C, M, B, C, N, B, H, M, N, H, B, C, M, N, C, H)
        )
        p3 = (
            '\\item Vì $%s%s // %s%s$ và $%s%s \\perp %s%s$ (do $%s%s$ là đường cao của tam giác $%s%s%s$) nên $%s%s \\perp %s%s$.\\\\'
            % (M, N, C, H, C, H, A, B, C, E, A, B, C, M, N, A, B)
        )
        p4 = (
            'Mặt khác, $%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s // %s%s$, mà $%s%s \\perp %s%s$ nên $%s%s \\perp %s%s$. Vì $%s%s // %s%s$ nên $%s%s \\perp %s%s$. Vậy tam giác $%s%s%s$ vuông tại $%s$ (điều phải chứng minh). \n'
            % (M, P, H, B, C, M, P, B, H, B, H, A, C, M, P, A, C, N, P, B, C, M, N, N, P, N, M, P, N)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
