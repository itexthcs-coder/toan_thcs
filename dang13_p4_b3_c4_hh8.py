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

def bt_dang13_p4_b3_c4_hh8(self):
    # Dạng 13: Khai thác đường trung bình trong tam giác vuông để chứng minh thẳng hàng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [
            ('A', 'B', 'C', 'D', 'E', 'F', 'I'),
            ('M', 'N', 'P', 'D', 'E', 'F', 'K')
        ]
        A, B, C, D, E, F, I = random.choice(bo_dinh)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (%s) at (0,0);\n'
            '\\coordinate (%s) at (0,2.6);\n'
            '\\coordinate (%s) at (3.6,0);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\coordinate (%s) at ($(%s)!0.5!(%s)$);\n'
            '\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s);\n'
            '\\fill (%s) circle (1pt) node[below left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
            '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (A, B, C, D, A, B, E, B, C, F, A, C, I, D, E, A, B, C, D, E, F, A, E, B, F, A, A, B, B, C, C, D, D, E, E, F, F, I, I)

        noidungcauhoi = (
            'Cho tam giác $%s%s%s$ vuông tại $%s$. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$. Gọi $%s$ là trung điểm của $%s%s$.\\\\\n'
            'a) Chứng minh tứ giác $%s%s%s%s$ là hình chữ nhật và $%s%s = %s%s$.\\\\\n'
            'b) Chứng minh ba điểm $%s, %s, %s$ thẳng hàng.\n%s'
            % (A, B, C, A, D, E, F, A, B, B, C, A, C, I, D, E, A, D, E, F, A, E, D, F, B, I, F, hinh_ve)
        )

        p1 = (
            '\\item Trong tam giác $%s%s%s$, $%s%s$ là đường trung bình nên $%s%s // %s%s$ và $%s%s = \\frac{1}{2}%s%s = %s%s$.\\\\'
            % (A, B, C, D, E, D, E, A, C, D, E, A, C, A, F)
        )
        p2 = (
            'Tứ giác $%s%s%s%s$ có $%s%s // %s%s$ và $%s%s = %s%s$ nên là hình bình hành. Lại có $\\widehat{%s} = 90^\\circ$ nên $%s%s%s%s$ là hình chữ nhật, suy ra hai đường chéo bằng nhau: $%s%s = %s%s$ (điều phải chứng minh). \n'
            % (A, D, E, F, D, E, A, F, D, E, A, F, A, A, D, E, F, A, E, D, F)
        )
        p3 = (
            '\\item Ta có $%s%s // %s%s$ (vì $%s%s // %s%s$) và $%s%s = %s%s$ (cùng bằng $\\frac{1}{2}%s%s$), suy ra tứ giác $%s%s%s%s$ là hình bình hành.\\\\'
            % (D, E, B, F, D, E, A, C, D, E, B, F, A, C, B, D, E, F)
        )
        p4 = (
            'Do đó hai đường chéo $%s%s$ và $%s%s$ cắt nhau tại trung điểm của mỗi đường. Mà $%s$ là trung điểm của đường chéo $%s%s$ nên $%s$ cũng là trung điểm của đường chéo $%s%s$. Vậy ba điểm $%s, %s, %s$ thẳng hàng (điều phải chứng minh). \n'
            % (B, F, D, E, I, D, E, I, B, F, B, I, F)
        )
        loigiai = '\\begin{enumEX}[a)]{1} \n' + p1 + p2 + p3 + p4 + '\\end{enumEX} \n'

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
