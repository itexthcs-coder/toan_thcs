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

def bt_dang8_p1_b3_c5_ds8(self):
    # Dạng 8: Đọc tỉ trọng trên biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        names = ['Xe máy', 'Ô tô cá nhân', 'Xe buýt', 'Đi bộ hoặc xe đạp']
        pcts = random.choice([
            [52, 18, 22, 8],
            [50, 15, 25, 10],
            [55, 16, 21, 8],
            [48, 17, 26, 9]
        ])
        
        # Sắp xếp tăng dần để tìm thấp thứ hai
        paired = list(zip(pcts, names))
        paired_sorted = sorted(paired, key=lambda x: x[0])
        
        da = paired_sorted[1][1]
        s_pool = [paired_sorted[0][1], paired_sorted[2][1], paired_sorted[3][1]]
        das1, das2, das3 = s_pool[0], s_pool[1], s_pool[2]
        
        # Tính góc tích lũy để vẽ quạt tròn TikZ
        a0 = 0
        a1 = round(pcts[0] * 3.6, 1)
        a2 = round((pcts[0] + pcts[1]) * 3.6, 1)
        a3 = round((pcts[0] + pcts[1] + pcts[2]) * 3.6, 1)
        
        m0 = round(a1 / 2.0, 1)
        m1 = round((a1 + a2) / 2.0, 1)
        m2 = round((a2 + a3) / 2.0, 1)
        m3 = round((a3 + 360.0) / 2.0, 1)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:2) arc (0:%s:2) -- cycle;\n' % a1 +
            '\\draw[line width=1pt, fill=black!25] (0,0) -- (%s:2) arc (%s:%s:2) -- cycle;\n' % (a1, a1, a2) +
            '\\draw[line width=1pt, fill=black!40] (0,0) -- (%s:2) arc (%s:%s:2) -- cycle;\n' % (a2, a2, a3) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (%s:2) arc (%s:360:2) -- cycle;\n' % (a3, a3) +
            '\\node at (%s:1.25) {$%s\\%%$};\n' % (m0, pcts[0]) +
            '\\node at (%s:1.35) {$%s\\%%$};\n' % (m1, pcts[1]) +
            '\\node at (%s:1.3) {$%s\\%%$};\n' % (m2, pcts[2]) +
            '\\node at (%s:1.45) {$%s\\%%$};\n' % (m3, pcts[3]) +
            '\\draw[line width=1pt, fill=black!10] (2.8,1.2) rectangle (3.2,1.5) node[right, yshift=-4pt] {Xe máy};\n' +
            '\\draw[line width=1pt, fill=black!25] (2.8,0.4) rectangle (3.2,0.7) node[right, yshift=-4pt] {Ô tô cá nhân};\n' +
            '\\draw[line width=1pt, fill=black!40] (2.8,-0.4) rectangle (3.2,-0.1) node[right, yshift=-4pt] {Xe buýt};\n' +
            '\\draw[line width=1pt, fill=white] (2.8,-1.2) rectangle (3.2,-0.9) node[right, yshift=-4pt] {Đi bộ hoặc xe đạp};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây thống kê tỉ lệ các phương tiện đi lại của toàn thể nhân viên một công ty:\n' +
                         tikz_code + '\n' +
                         'Phương tiện nào chiếm tỉ lệ thấp thứ hai trong công ty?')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Từ biểu đồ hình quạt tròn, tỉ lệ các phương tiện đi lại của nhân viên công ty gồm:\\\\' +
                   '- Xe máy: $%s\\%%$;\\\\' +
                   '- Ô tô cá nhân: $%s\\%%$;\\\\' +
                   '- Xe buýt: $%s\\%%$;\\\\' +
                   '- Đi bộ hoặc xe đạp: $%s\\%%$.\\\\' +
                   'Sắp xếp các tỉ lệ theo thứ tự tăng dần ta được: $%s\\%% < %s\\%% < %s\\%% < %s\\%%$.\\\\' +
                   'Vậy phương tiện chiếm tỉ lệ thấp thứ hai trong công ty là %s.'
                   ) % (pcts[0], pcts[1], pcts[2], pcts[3],
                        paired_sorted[0][0], paired_sorted[1][0], paired_sorted[2][0], paired_sorted[3][0], da)

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
