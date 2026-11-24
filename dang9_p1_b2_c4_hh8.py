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
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def bt_dang9_p1_b2_c4_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_diem = random.choice([
            ('A', 'B', 'C', 'M', 'N', 'P'),
            ('D', 'E', 'F', 'I', 'K', 'H')
        ])
        A, B, C, M, N, P = bo_diem
        cv_abc = random.choice([18, 20, 24, 28, 30, 32, 36, 40])
        cv_mnp = cv_abc // 2
    
        du = ['$%s\\text{ cm}$' % fmt_num(cv_mnp)]
        da = random.choice(du)
        s = [
            '$%s\\text{ cm}$' % fmt_num(cv_abc * 2),
            '$%s\\text{ cm}$' % fmt_num(cv_abc),
            '$%s\\text{ cm}$' % fmt_num(cv_abc // 3),
            '$%s\\text{ cm}$' % fmt_num(cv_mnp // 2),
            '$%s\\text{ cm}$' % fmt_num(cv_mnp + 4)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (1.5,3);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (4.5,0);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s)--(%s)--cycle;
\\fill (%s) circle (1pt) node[above] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[below] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, M, A, B, N, B, C, P, A, C, A, B, C, M, N, P, A, A, B, B, C, C, M, M, N, N, P, P))
    
        noidungcauhoi = ('''Cho tam giác $%s%s%s$ có chu vi bằng $%s\\text{ cm}$. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$ (như hình vẽ). Chu vi của tam giác $%s%s%s$ bằng%s''' % (A, B, C, fmt_num(cv_abc), M, N, P, A, B, B, C, C, A, M, N, P, hinhve))
    
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        loigiai = ('''Vì $%s, %s, %s$ lần lượt là trung điểm của các cạnh $%s%s, %s%s, %s%s$ nên $%s%s, %s%s, %s%s$ là ba đường trung bình của tam giác $%s%s%s$.\\
Theo tính chất đường trung bình của tam giác, ta có:\\
$%s%s = \\dfrac{1}{2}%s%s$; $%s%s = \\dfrac{1}{2}%s%s$; $%s%s = \\dfrac{1}{2}%s%s$.\\
Chu vi tam giác $%s%s%s$ là:\\
$%s%s + %s%s + %s%s = \\dfrac{1}{2}(%s%s + %s%s + %s%s) = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.\\
Vậy chu vi của tam giác $%s%s%s$ bằng $%s\\text{ cm}$.''' % (M, N, P, A, B, B, C, C, A, M, N, N, P, P, M, A, B, C, M, N, A, C, N, P, A, B, P, M, B, C, M, N, P, M, N, N, P, P, M, A, C, A, B, B, C, fmt_num(cv_abc), fmt_num(cv_mnp), M, N, P, fmt_num(cv_mnp)))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
