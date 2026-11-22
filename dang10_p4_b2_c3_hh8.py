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


def bt_dang10_p4_b2_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = [('M', 'N', 'P', 'Q'), ('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H')]
        d1, d2, d3, d4 = random.choice(bo_dinh)
        ten_ht = d1 + d2 + d3 + d4
        day1, day2 = d1 + d2, d3 + d4
        cb1, cb2 = d1 + d4, d2 + d3

        mn_dec = Decimal(random.randint(4, 7)) + Decimal('0.5')
        pq_dec = Decimal(random.randint(8, 12)) + Decimal('0.5')
        mq_dec = Decimal(random.randint(3, 6)) + Decimal('0.5')
        cv_dec = mn_dec + pq_dec + Decimal(2) * mq_dec

        mn_str = str(mn_dec).replace('.', ',')
        pq_str = str(pq_dec).replace('.', ',')
        mq_str = str(mq_dec).replace('.', ',')
        cv_str = str(cv_dec).replace('.', ',')
        if cv_str.endswith(',0'):
            cv_str = cv_str[:-2]

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (3.6,0);\n'
            '\\coordinate (A) at (0.8,1.8);\n'
            '\\coordinate (B) at (2.8,1.8);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--(A);\n'
            '\\fill (A) circle (1pt) node[above left] {$%s$};\n'
            '\\fill (B) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (C) circle (1pt) node[below right] {$%s$};\n'
            '\\fill (D) circle (1pt) node[below left] {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
            % (d1, d2, d3, d4)
        )

        noidungcauhoi = (
            'Cho hình thang cân $%s$ ($%s // %s$) có $%s = %s\\text{ cm}$, $%s = %s\\text{ cm}$ và $%s = %s\\text{ cm}$ (như hình vẽ).\\\\\n'
            'a) Nêu độ dài cạnh bên $%s$.\\\\\n'
            'b) Tính chu vi của hình thang cân $%s$. %s'
            % (ten_ht, day1, day2, day1, mn_str, day2, pq_str, cb1, mq_str, cb2, ten_ht, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \\n'
            '\\item Theo Định lí $1$, trong hình thang cân hai cạnh bên bằng nhau nên $%s = %s = %s\\text{ cm}$. \\n'
            '\\item Chu vi của hình thang cân $%s$ là:\\\\ '
            '$%s + %s + %s + %s = %s + %s + %s + %s = %s\\text{ cm}$. \\n'
            '\\end{enumEX} \\n'
            % (cb2, cb1, mq_str, ten_ht, day1, day2, cb1, cb2, mn_str, pq_str, mq_str, mq_str, cv_str)
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
