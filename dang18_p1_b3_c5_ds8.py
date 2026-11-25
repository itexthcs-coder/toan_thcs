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

def bt_dang18_p1_b3_c5_ds8(self):
    # Dạng 18: Chuyển đổi và tính toán số liệu từ biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tong_hs = random.choice([600, 700, 800, 900, 1000])
        p_tot = random.choice([60, 62, 65, 68])
        p_kha = random.choice([24, 25, 28, 30])
        p_dat = 100 - p_tot - p_kha
        
        kq_kha = int(tong_hs * p_kha // 100)
        kq_tot = int(tong_hs * p_tot // 100)
        kq_dat = int(tong_hs * p_dat // 100)
        
        da = '$%s$ học sinh' % kq_kha
        s_pool = [
            '$%s$ học sinh' % kq_tot,
            '$%s$ học sinh' % kq_dat,
            '$%s$ học sinh' % (kq_kha + 20),
            '$%s$ học sinh' % (kq_kha - 15)
        ]
        das1 = random.choice(s_pool)
        s_pool.remove(das1)
        das2 = random.choice(s_pool)
        s_pool.remove(das2)
        das3 = random.choice(s_pool)
        
        a1 = round(p_tot * 3.6, 1)
        a2 = round((p_tot + p_kha) * 3.6, 1)
        m0 = round(a1 / 2.0, 1)
        m1 = round((a1 + a2) / 2.0, 1)
        m2 = round((a2 + 360.0) / 2.0, 1)
        
        tikz_code = (
            '\\begin{center}\n' +
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
            '\\draw[line width=1pt, fill=black!15] (0,0) -- (0:1.9) arc (0:%s:1.9) -- cycle;\n' % a1 +
            '\\draw[line width=1pt, fill=black!35] (0,0) -- (%s:1.9) arc (%s:%s:1.9) -- cycle;\n' % (a1, a1, a2) +
            '\\draw[line width=1pt, fill=white] (0,0) -- (%s:1.9) arc (%s:360:1.9) -- cycle;\n' % (a2, a2) +
            '\\node at (%s:1.15) {$%s\\%%$};\n' % (m0, p_tot) +
            '\\node at (%s:1.25) {$%s\\%%$};\n' % (m1, p_kha) +
            '\\node at (%s:1.35) {$%s\\%%$};\n' % (m2, p_dat) +
            '\\draw[line width=1pt, fill=black!15] (2.6,0.9) rectangle (3.0,1.2) node[right, yshift=-4pt] {Mức Tốt};\n' +
            '\\draw[line width=1pt, fill=black!35] (2.6,0.0) rectangle (3.0,0.3) node[right, yshift=-4pt] {Mức Khá};\n' +
            '\\draw[line width=1pt, fill=white] (2.6,-0.9) rectangle (3.0,-0.6) node[right, yshift=-4pt] {Mức Đạt};\n' +
            '\\end{tikzpicture}\n' +
            '\\end{center}'
        )
        
        noidungcauhoi = ('Một trường THCS có tổng cộng $%s$ học sinh. Biểu đồ hình quạt tròn dưới đây thống kê tỉ lệ xếp loại rèn luyện học kì I của toàn trường:\n' % tong_hs +
                         tikz_code + '\n' +
                         'Số học sinh xếp loại rèn luyện mức Khá của trường đó là')
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ('Từ biểu đồ hình quạt tròn, tỉ lệ học sinh xếp loại rèn luyện mức Khá chiếm $%s\\%%$ tổng số học sinh toàn trường.\\\\' +
                   'Số học sinh xếp loại rèn luyện mức Khá của trường là:\\\\' +
                   '$$%s \\cdot %s\\%% = %s \\cdot \\dfrac{%s}{100} = %s \\text{ (học sinh)}.$$\\\\' +
                   'Vậy chọn phương án: %s.'
                   ) % (p_kha, tong_hs, p_kha, tong_hs, p_kha, kq_kha, da)

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
