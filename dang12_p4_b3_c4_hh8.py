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

def bt_dang12_p4_b3_c4_hh8(self):
    # Dạng 12: Chứng minh tính chất hình học từ trọng tâm và trung điểm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'D', 'E', 'G', 'I', 'K'),
            ('M', 'N', 'P', 'E', 'F', 'G', 'H', 'K')
        ]
        A, B, C, D, E, G, I, K = random.choice(bo_dinh)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (1.8,3.4);\n'
            '\\coordinate (%s) at (0,0);\n'
            '\\coordinate (%s) at (4.6,0);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at (intersection of %s--%s and %s--%s);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s) (%s)--(%s)--(%s)--(%s)--cycle;\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, D, A, C, E, A, B, G, B, D, C, E, I, G, B, K, G, C, A, B, C, B, D, C, E, E, D, K, I, A, A, B, B, C, C, D, D, E, E, G, G, I, I, K, K)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ có các đường trung tuyến $%s%s$ và $%s%s$ cắt nhau tại trọng tâm $%s$. Gọi $%s, %s$ lần lượt là trung điểm của $%s%s$ và $%s%s$.\\\\\n'
            'a) Chứng minh tứ giác $%s%s%s%s$ là hình bình hành.\\\\\n'
            'b) Tam giác $%s%s%s$ cần thêm điều kiện gì để tứ giác $%s%s%s%s$ là hình chữ nhật?\n%s'
            % (A, B, C, B, D, C, E, G, I, K, G, B, G, C, E, D, K, I, A, B, C, E, D, K, I, hinh_ve)
        )

        p1 = (
            '\\item Trong tam giác $%s%s%s$, $%s, %s$ lần lượt là trung điểm của $%s%s, %s%s$ nên $%s%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s%s // %s%s$ và $%s%s = \\frac{1}{2}%s%s$.\\\\'
            % (A, B, C, E, D, A, B, A, C, E, D, A, B, C, E, D, B, C, E, D, B, C)
        )
        p2 = (
            'Trong tam giác $%s%s%s$, $%s, %s$ lần lượt là trung điểm của $%s%s, %s%s$ nên $%s%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s%s // %s%s$ và $%s%s = \\frac{1}{2}%s%s$.\\\\'
            % (G, B, C, I, K, G, B, G, C, I, K, G, B, C, I, K, B, C, I, K, B, C)
        )
        p3 = (
            'Do đó $%s%s // %s%s$ và $%s%s = %s%s$, suy ra tứ giác $%s%s%s%s$ là hình bình hành (điều phải chứng minh). \n'
            % (E, D, I, K, E, D, I, K, E, D, K, I)
        )
        p4 = (
            '\\item Hình bình hành $%s%s%s%s$ là hình chữ nhật khi và chỉ khi hai đường chéo $%s%s$ và $%s%s$ bằng nhau.\\\\'
            % (E, D, K, I, E, K, D, I)
        )
        p5 = (
            'Vì $%s$ là trọng tâm tam giác $%s%s%s$ nên $%s%s = \\frac{1}{3}%s%s$ và $%s%s = \\frac{1}{2}%s%s = \\frac{1}{3}%s%s$, suy ra $%s%s = %s%s + %s%s = \\frac{2}{3}%s%s$. Tương tự $%s%s = \\frac{2}{3}%s%s$.\\\\'
            % (G, A, B, C, G, D, B, D, G, I, G, B, B, D, D, I, G, D, G, I, B, D, E, K, C, E)
        )
        p6 = (
            'Do đó $%s%s = %s%s \\Leftrightarrow %s%s = %s%s \\Leftrightarrow$ tam giác $%s%s%s$ cân tại $%s$. \n'
            % (E, K, D, I, B, D, C, E, A, B, C, A)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + p5 + p6 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
