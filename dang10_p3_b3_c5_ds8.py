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

def bt_dang10_p3_b3_c5_ds8(self):
    # Dạng 10: Tính phần trăm thị phần thu hẹp giữa hai quốc gia trên biểu đồ cột kép
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m21 = Decimal('16.5')
        n21 = Decimal('28.0')
        m25, n25 = random.choice([
            (Decimal('19.8'), Decimal('24.5')),
            (Decimal('20.2'), Decimal('25.0')),
            (Decimal('19.4'), Decimal('23.8')),
            (Decimal('20.5'), Decimal('26.2'))
        ])
        d21 = n21 - m21
        d25 = n25 - m25
        thu_hep = d21 - d25
        kq_str = str(thu_hep).replace('.', ',')
        
        def fmt_vn(d):
            return str(d).replace('.', ',')
            
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[below] {Năm};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Thị phần ($\\%%$)};\n' +
            '\\node[below left] at (0,0) {$0$};\n' +
            '\\draw[line width=1pt, fill=black!15] (0.8,0) rectangle (1.5,1.8); \\node[above] at (1.15,1.8) {$%s\\%%$};\n' % fmt_vn(m21) +
            '\\draw[line width=1pt, fill=black!45] (1.5,0) rectangle (2.2,3.1); \\node[above] at (1.85,3.1) {$%s\\%%$};\n' % fmt_vn(n21) +
            '\\node[below] at (1.5,0) {$2021$};\n' +
            '\\draw[line width=1pt, fill=black!15] (2.9,0) rectangle (3.6,2.2); \\node[above] at (3.25,2.2) {$%s\\%%$};\n' % fmt_vn(m25) +
            '\\draw[line width=1pt, fill=black!45] (3.6,0) rectangle (4.3,2.7); \\node[above] at (3.95,2.7) {$%s\\%%$};\n' % fmt_vn(n25) +
            '\\node[below] at (3.6,0) {$2025$};\n' +
            '\\draw[line width=1pt, fill=black!15] (5.4,2.8) rectangle (5.8,3.1) node[right, yshift=-4pt] {Quốc gia $M$};\n' +
            '\\draw[line width=1pt, fill=black!45] (5.4,2.0) rectangle (5.8,2.3) node[right, yshift=-4pt] {Quốc gia $N$};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ cột kép dưới đây biểu diễn thị phần xuất khẩu cà phê toàn cầu của hai quốc gia $M$ và $N$ trong năm $2021$ và năm $2025$:\n' +
                         tikz_code + '\n' +
                         'Hỏi từ năm $2021$ đến năm $2025$, khoảng cách chênh lệch thị phần giữa hai quốc gia $N$ và $M$ đã thu hẹp lại bao nhiêu điểm phần trăm?')
        
        loigiai = ('- Năm $2021$, chênh lệch thị phần giữa quốc gia $N$ và quốc gia $M$ là: $%s\\%% - %s\\%% = %s$ (điểm phần trăm).\\\\' +
                   '- Năm $2025$, chênh lệch thị phần giữa quốc gia $N$ và quốc gia $M$ là: $%s\\%% - %s\\%% = %s$ (điểm phần trăm).\\\\' +
                   'Khoảng cách chênh lệch thị phần giữa hai quốc gia đã thu hẹp lại số điểm phần trăm là:\\\\' +
                   '$$%s - %s = %s \\text{ (điểm phần trăm)}.$$'
                   ) % (fmt_vn(n21), fmt_vn(m21), fmt_vn(d21), fmt_vn(n25), fmt_vn(m25), fmt_vn(d25), fmt_vn(d21), fmt_vn(d25), kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
