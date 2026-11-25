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


def bt_dang6_p1_b2_c5_ds8(self):
    # Dạng 6 (Nhận biết): Đọc số liệu từ biểu đồ cột đơn có số thập phân
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        def fmt_vn(val):
            return f"{val:.2f}".replace(".", ",")
            
        h_an = Decimal(str(random.choice([1.54, 1.56, 1.58])))
        h_binh = Decimal(str(random.choice([1.64, 1.66, 1.68])))
        h_chi = Decimal(str(random.choice([1.50, 1.52])))
        h_dung = Decimal(str(random.choice([1.60, 1.62])))
        
        diff_max_min = (h_binh - h_chi).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        diff_binh_an = (h_binh - h_an).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        diff_dung_chi = (h_dung - h_chi).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        wrong_diff = (diff_max_min + Decimal('0.02')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        y_an = float((h_an - Decimal('1.45')) * 10)
        y_binh = float((h_binh - Decimal('1.45')) * 10)
        y_chi = float((h_chi - Decimal('1.45')) * 10)
        y_dung = float((h_dung - Decimal('1.45')) * 10)
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,3.0) node[above] {Chiều cao (m)};
        \\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[right] {Học sinh};
        \\draw[line width=1pt, dashed] (0,0.5) -- (5.8,0.5);
        \\draw[line width=1pt, dashed] (0,1.0) -- (5.8,1.0);
        \\draw[line width=1pt, dashed] (0,1.5) -- (5.8,1.5);
        \\draw[line width=1pt, dashed] (0,2.0) -- (5.8,2.0);
        \\draw[line width=1pt, dashed] (0,2.5) -- (5.8,2.5);
        \\node[left] at (0,0) {$1,45$};
        \\node[left] at (0,0.5) {$1,50$};
        \\node[left] at (0,1.0) {$1,55$};
        \\node[left] at (0,1.5) {$1,60$};
        \\node[left] at (0,2.0) {$1,65$};
        \\node[left] at (0,2.5) {$1,70$};
        \\draw[line width=1pt, fill=black!20] (0.6,0) rectangle (1.3,%.2f);
        \\node[above] at (0.95,%.2f) {$%s$};
        \\node[below] at (0.95,0) {An};
        \\draw[line width=1pt, fill=black!20] (1.9,0) rectangle (2.6,%.2f);
        \\node[above] at (2.25,%.2f) {$%s$};
        \\node[below] at (2.25,0) {Bình};
        \\draw[line width=1pt, fill=black!20] (3.2,0) rectangle (3.9,%.2f);
        \\node[above] at (3.55,%.2f) {$%s$};
        \\node[below] at (3.55,0) {Chi};
        \\draw[line width=1pt, fill=black!20] (4.5,0) rectangle (5.2,%.2f);
        \\node[above] at (4.85,%.2f) {$%s$};
        \\node[below] at (4.85,0) {Dũng};
        \\end{tikzpicture}
        \\end{center}""" % (y_an, y_an, fmt_vn(h_an),
                              y_binh, y_binh, fmt_vn(h_binh),
                              y_chi, y_chi, fmt_vn(h_chi),
                              y_dung, y_dung, fmt_vn(h_dung)))
        
        du = ['Bình cao nhất, cao hơn Chi $%s$ m' % fmt_vn(diff_max_min)]
        da = random.choice(du)
        s = [
            'Bình cao nhất, cao hơn An $%s$ m' % fmt_vn(diff_binh_an),
            'Dũng cao nhất, cao hơn Chi $%s$ m' % fmt_vn(diff_dung_chi),
            'Bình cao nhất, cao hơn Chi $%s$ m' % fmt_vn(wrong_diff)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Cho biểu đồ cột biểu diễn chiều cao của bốn bạn học sinh lớp 8A:%sHỏi bạn nào có chiều cao lớn nhất và cao hơn bạn thấp nhất bao nhiêu mét?""" % tikz_code)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Quan sát biểu đồ cột, chiều cao của bốn bạn lần lượt là: An ($%s\\text{ m}$), Bình ($%s\\text{ m}$), Chi ($%s\\text{ m}$), Dũng ($%s\\text{ m}$).\\\\
    - Bạn có chiều cao lớn nhất là Bình ($%s\\text{ m}$).\\\\
    - Bạn có chiều cao thấp nhất là Chi ($%s\\text{ m}$).\\\\
    - Bình cao hơn Chi số mét là: $%s - %s = %s$ (m)."""
                   % (fmt_vn(h_an), fmt_vn(h_binh), fmt_vn(h_chi), fmt_vn(h_dung),
                      fmt_vn(h_binh), fmt_vn(h_chi),
                      fmt_vn(h_binh), fmt_vn(h_chi), fmt_vn(diff_max_min)))

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
