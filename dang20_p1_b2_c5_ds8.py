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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang20_p1_b2_c5_ds8(self):
    # Dạng 20 (Thông hiểu): Đọc biểu đồ đoạn thẳng và tính phần trăm tăng trưởng giữa hai mốc
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        y2022 = random.choice([600, 700, 800, 900])
        y2023 = random.choice([1000, 1200, 1500])
        pct_inc = random.choice([15, 20, 25, 30])
        y2024 = y2023 + (y2023 * pct_inc // 100)
        
        s_2022 = f"{y2022:,}".replace(",", "\\,")
        s_2023 = f"{y2023:,}".replace(",", "\\,")
        s_2024 = f"{y2024:,}".replace(",", "\\,")
        s_diff = f"{(y2024 - y2023):,}".replace(",", "\\,")
        
        p1_y = (y2022 - 500) / 600.0
        p2_y = (y2023 - 500) / 600.0
        p3_y = (y2024 - 500) / 600.0
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.8) node[above] {Số cây};
        \\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[right] {Năm};
        \\draw[line width=1pt, dashed] (0,0.83) -- (4.8,0.83);
        \\draw[line width=1pt, dashed] (0,1.67) -- (4.8,1.67);
        \\draw[line width=1pt, dashed] (0,2.50) -- (4.8,2.50);
        \\node[left] at (0,0) {$500$};
        \\node[left] at (0,0.83) {$1\\,000$};
        \\node[left] at (0,1.67) {$1\\,500$};
        \\node[left] at (0,2.50) {$2\\,000$};
        \\coordinate (A) at (1.0,%.2f);
        \\coordinate (B) at (2.6,%.2f);
        \\coordinate (C) at (4.2,%.2f);
        \\draw[line width=1pt] (A)--(B)--(C);
        \\fill (A) circle (1pt) node[above left] {$%s$};
        \\fill (B) circle (1pt) node[above left] {$%s$};
        \\fill (C) circle (1pt) node[above] {$%s$};
        \\node[below] at (1.0,0) {$2022$};
        \\node[below] at (2.6,0) {$2023$};
        \\node[below] at (4.2,0) {$2024$};
        \\end{tikzpicture}
        \\end{center}""" % (p1_y, p2_y, p3_y, s_2022, s_2023, s_2024))
        
        wrong1 = Decimal(str((y2024 - y2023) * 100 / y2024)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_wrong1 = str(wrong1).replace(".", ",")
        wrong2 = Decimal(str((y2024 - y2022) * 100 / y2022)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        s_wrong2 = str(wrong2).replace(".", ",")
        
        du = ['$%s\\%%$' % pct_inc]
        da = random.choice(du)
        s = [
            '$%s\\%%$' % s_wrong1,
            '$%s\\%%$' % s_wrong2,
            '$%s\\%%$' % (pct_inc + 10)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Biểu đồ đoạn thẳng dưới đây cho biết số lượng cây xanh được trồng mới tại một xã qua ba năm $2022$, $2023$, $2024$:%sHỏi số cây trồng được năm $2024$ tăng bao nhiêu phần trăm so với năm $2023$?""" % tikz_code)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Quan sát biểu đồ đoạn thẳng, số cây trồng mới năm $2023$ là $%s$ cây và năm $2024$ là $%s$ cây.\\\\
    Số cây trồng được năm $2024$ nhiều hơn năm $2023$ là:
    $$%s - %s = %s \\text{ (cây)}.$$
    Tỉ lệ phần trăm số cây trồng được năm $2024$ tăng so với năm $2023$ là:
    $$\\frac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$"""
                   % (s_2023, s_2024, s_2024, s_2023, s_diff, s_diff, s_2023, pct_inc))

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
