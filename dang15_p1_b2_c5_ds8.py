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


def bt_dang15_p1_b2_c5_ds8(self):
    # Dạng 15 (Thông hiểu): Quy đổi từ tỉ lệ phần trăm trên biểu đồ quạt tròn ra số lượng cụ thể
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tong_ly = random.choice([200, 240, 300, 360])
        p_ts = random.choice([40, 45, 50])
        p_cf = random.choice([25, 30, 35])
        p_ne = 100 - p_ts - p_cf
        
        ly_ts = tong_ly * p_ts // 100
        ly_cf = tong_ly * p_cf // 100
        ly_ne = tong_ly * p_ne // 100
        
        ang1 = p_ts * 3.6
        ang2 = ang1 + p_cf * 3.6
        mid1 = ang1 / 2.0
        mid2 = ang1 + (p_cf * 3.6) / 2.0
        mid3 = ang2 + (p_ne * 3.6) / 2.0
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.6);
        \\draw[line width=1pt] (0,0) -- (0:1.6);
        \\draw[line width=1pt] (0,0) -- (%.1f:1.6);
        \\draw[line width=1pt] (0,0) -- (%.1f:1.6);
        \\node at (%.1f:0.95) {$%s\\%%$};
        \\node at (%.1f:0.95) {$%s\\%%$};
        \\node at (%.1f:0.95) {$%s\\%%$};
        \\node[right] at (2.1, 0.7) {Trà sữa: $%s\\%%$};
        \\node[right] at (2.1, 0.0) {Cà phê: $%s\\%%$};
        \\node[right] at (2.1, -0.7) {Nước ép: $%s\\%%$};
        \\end{tikzpicture}
        \\end{center}""" % (ang1, ang2, mid1, p_ts, mid2, p_cf, mid3, p_ne, p_ts, p_cf, p_ne))
        
        du = ['$%s$ ly' % ly_ts]
        da = random.choice(du)
        s = [
            '$%s$ ly' % ly_cf,
            '$%s$ ly' % ly_ne,
            '$%s$ ly' % (ly_ts + 12),
            '$%s$ ly' % (ly_ts - 12)
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Biểu đồ hình quạt tròn dưới đây cho biết tỉ lệ các loại nước giải khát bán được trong một ngày của quán cà phê:%sBiết tổng số ly nước bán được trong ngày là $%s$ ly. Hỏi quán đã bán được bao nhiêu ly Trà sữa?"""
                         % (tikz_code, tong_ly))
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Quan sát biểu đồ hình quạt tròn, tỉ lệ ly Trà sữa bán được chiếm $%s\\%%$ tổng số ly nước bán được trong ngày.\\\\
    Số ly Trà sữa quán đã bán được là:
    $$%s \\cdot %s\\%% = \\frac{%s \\cdot %s}{100} = %s \\text{ (ly)}.$$"""
                   % (p_ts, tong_ly, p_ts, tong_ly, p_ts, ly_ts))

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
