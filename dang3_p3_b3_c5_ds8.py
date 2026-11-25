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

def bt_dang3_p3_b3_c5_ds8(self):
    # Dạng 3: Tính tỉ số chiều cao cột bị phóng đại khi gốc trục đứng khác 0
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g0 = random.choice([500, 600, 800, 900])
        d2 = random.choice([4, 5, 6, 8])
        k = random.choice([3, 4, 5])
        v2 = g0 + d2
        v1 = g0 + k * d2
        kq_str = str(k)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[below] {Phân xưởng};\n' +
            '\\draw[line width=1pt, ->] (0,0) -- (0,%s) node[left] {Sản phẩm};\n' % (k + 0.8) +
            '\\node[left] at (0,0) {$%s$};\n' % g0 +
            '\\draw[line width=1pt, dashed] (0,1) -- (4.2,1);\n' +
            '\\node[left] at (0,1) {$%s$};\n' % v2 +
            '\\draw[line width=1pt, dashed] (0,%s) -- (4.2,%s);\n' % (k, k) +
            '\\node[left] at (0,%s) {$%s$};\n' % (k, v1) +
            '\\draw[line width=1pt, fill=black!30] (0.8,0) rectangle (1.8,%s);\n' % k +
            '\\node[above] at (1.3,%s) {$%s$};\n' % (k, v1) +
            '\\node[below] at (1.3,0) {Phân xưởng I};\n' +
            '\\draw[line width=1pt, fill=black!15] (2.6,0) rectangle (3.6,1);\n' +
            '\\node[above] at (3.1,1) {$%s$};\n' % v2 +
            '\\node[below] at (3.1,0) {Phân xưởng II};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một nhân viên thiết kế vẽ biểu đồ cột biểu diễn số lượng sản phẩm đạt chuẩn xuất khẩu của hai phân xưởng trong tháng: Phân xưởng I đạt $%s$ sản phẩm, Phân xưởng II đạt $%s$ sản phẩm. Do đặt gốc của trục đứng bắt đầu từ $%s$ thay vì $0$ nên biểu đồ có dạng như hình vẽ:\n' % (v1, v2, g0) +
                         tikz_code + '\n' +
                         'Trên hình vẽ này, chiều cao cột của Phân xưởng I gấp mấy lần chiều cao cột của Phân xưởng II?')
        
        loigiai = ('Vì gốc của trục đứng bắt đầu từ $%s$ nên:\\\\' +
                   '- Chiều cao cột biểu diễn Phân xưởng I tỉ lệ với $%s - %s = %s$ (đơn vị).\\\\' +
                   '- Chiều cao cột biểu diễn Phân xưởng II tỉ lệ với $%s - %s = %s$ (đơn vị).\\\\' +
                   'Vậy trên hình vẽ, chiều cao cột của Phân xưởng I gấp chiều cao cột của Phân xưởng II số lần là:\\\\' +
                   '$$\\dfrac{%s}{%s} = %s \\text{ (lần)}.$$'
                   ) % (g0, v1, g0, k * d2, v2, g0, d2, k * d2, d2, kq_str)

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
