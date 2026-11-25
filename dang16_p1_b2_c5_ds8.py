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


def bt_dang16_p1_b2_c5_ds8(self):
    # Dạng 16 (Thông hiểu): Phân tích biểu đồ cột kép để tính tổng và độ chênh lệch
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        toan_8a = random.randint(16, 20)
        van_8a = random.randint(11, 14)
        toan_8b = random.randint(13, 15)
        van_8b = random.randint(18, 22)
        
        tong_8a = toan_8a + van_8a
        tong_8b = toan_8b + van_8b
        while tong_8b <= tong_8a:
            van_8b += 1
            tong_8b = toan_8b + van_8b
            
        chenh_lech = tong_8b - tong_8a
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.8) node[above] {Số học sinh};
        \\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[right] {Lớp};
        \\draw[line width=1pt, dashed] (0,1.0) -- (5.0,1.0);
        \\draw[line width=1pt, dashed] (0,2.0) -- (5.0,2.0);
        \\node[left] at (0,0) {$0$};
        \\node[left] at (0,1.0) {$10$};
        \\node[left] at (0,2.0) {$20$};
        \\draw[line width=1pt, fill=black!35] (0.8,0) rectangle (1.4,%.2f);
        \\node[above] at (1.1,%.2f) {$%s$};
        \\draw[line width=1pt, fill=white] (1.4,0) rectangle (2.0,%.2f);
        \\node[above] at (1.7,%.2f) {$%s$};
        \\node[below] at (1.4,0) {Lớp 8A};
        \\draw[line width=1pt, fill=black!35] (3.0,0) rectangle (3.6,%.2f);
        \\node[above] at (3.3,%.2f) {$%s$};
        \\draw[line width=1pt, fill=white] (3.6,0) rectangle (4.2,%.2f);
        \\node[above] at (3.9,%.2f) {$%s$};
        \\node[below] at (3.6,0) {Lớp 8B};
        \\draw[line width=1pt, fill=black!35] (5.3,1.8) rectangle (5.6,2.1);
        \\node[right] at (5.6,1.95) {Toán};
        \\draw[line width=1pt, fill=white] (5.3,1.3) rectangle (5.6,1.6);
        \\node[right] at (5.6,1.45) {Ngữ văn};
        \\end{tikzpicture}
        \\end{center}""" % (toan_8a*0.1, toan_8a*0.1, toan_8a,
                              van_8a*0.1, van_8a*0.1, van_8a,
                              toan_8b*0.1, toan_8b*0.1, toan_8b,
                              van_8b*0.1, van_8b*0.1, van_8b))
        
        du = ['Tổng số học sinh giỏi hai môn của lớp 8B nhiều hơn lớp 8A là $%s$ em' % chenh_lech]
        da = random.choice(du)
        s = [
            'Số học sinh giỏi Toán của lớp 8B nhiều hơn lớp 8A là $%s$ em' % (toan_8a - toan_8b),
            'Tổng số học sinh giỏi Ngữ văn của cả hai lớp là $%s$ em' % (van_8a + van_8b + 2),
            'Lớp 8A có số học sinh giỏi Ngữ văn nhiều hơn số học sinh giỏi Toán'
        ]
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
        
        noidungcauhoi = ("""Biểu đồ cột kép dưới đây biểu diễn số lượng học sinh giỏi môn Toán và môn Ngữ văn của hai lớp 8A và 8B:%sNhận xét nào sau đây là \textbf{đúng}?""" % tikz_code)
        
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        
        loigiai = ("""Từ biểu đồ cột kép, ta có:\\\\
    - Tổng số học sinh giỏi hai môn của lớp 8A là: $%s + %s = %s$ (em).\\\\
    - Tổng số học sinh giỏi hai môn của lớp 8B là: $%s + %s = %s$ (em).\\\\
    - Số học sinh giỏi hai môn của lớp 8B nhiều hơn lớp 8A là: $%s - %s = %s$ (em).\\\\
    Vậy nhận xét đúng là: Tổng số học sinh giỏi hai môn của lớp 8B nhiều hơn lớp 8A là $%s$ em."""
                   % (toan_8a, van_8a, tong_8a, toan_8b, van_8b, tong_8b, tong_8b, tong_8a, chenh_lech, chenh_lech))

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
