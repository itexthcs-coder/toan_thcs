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


def bt_dang16_p3_b2_c5_ds8(self):
    # Dạng 16 (Vận dụng): Phân tích biểu đồ cột kép để tính tỉ lệ phần trăm đạt chuẩn của hai nhóm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        si_so = 40
        g_8a, k_8a = random.choice([(14, 18), (15, 17), (16, 16)])
        g_8b, k_8b = random.choice([(16, 16), (18, 18), (12, 20)])
        tong_dat = (g_8a + k_8a) + (g_8b + k_8b)
        pct = tong_dat * 100 // (2 * si_so)
        kq_str = str(pct)
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số học sinh};
        \\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[right] {Lớp};
        \\draw[line width=1pt, fill=black!35] (0.7,0) rectangle (1.3,1.4) (2.6,0) rectangle (3.2,1.6);
        \\draw[line width=1pt, fill=white] (1.3,0) rectangle (1.9,1.8) (3.2,0) rectangle (3.8,1.7);
        \\node[above] at (1.0,1.4) {$%s$}; \\node[above] at (1.6,1.8) {$%s$};
        \\node[above] at (2.9,1.6) {$%s$}; \\node[above] at (3.5,1.7) {$%s$};
        \\node[below] at (1.3,0) {Lớp 8A}; \\node[below] at (3.2,0) {Lớp 8B};
        \\draw[line width=1pt, fill=black!35] (4.6,1.7) rectangle (4.9,2.0); \\node[right] at (4.9,1.85) {Giỏi};
        \\draw[line width=1pt, fill=white] (4.6,1.2) rectangle (4.9,1.5); \\node[right] at (4.9,1.35) {Khá};
        \\end{tikzpicture}
        \\end{center}""" % (g_8a, k_8a, g_8b, k_8b))
        
        noidungcauhoi = ("""Biểu đồ cột kép dưới đây biểu diễn số học sinh đạt điểm Giỏi và điểm Khá môn Toán của hai lớp 8A và 8B (biết mỗi lớp đều có sĩ số là $%s$ học sinh):%sTính tỉ lệ phần trăm số học sinh đạt từ điểm Khá trở lên của cả hai lớp gộp lại."""
                         % (si_so, tikz_code))
        
        loigiai = ("""Tổng số học sinh của cả hai lớp là: $%s + %s = %s$ (học sinh).\\\\
        Tổng số học sinh đạt từ điểm Khá trở lên của cả hai lớp là:
        $$(%s + %s) + (%s + %s) = %s \\text{ (học sinh)}.$$
        Tỉ lệ phần trăm số học sinh đạt từ điểm Khá trở lên của cả hai lớp gộp lại là:
        $$\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%.$$"""
                   % (si_so, si_so, 2 * si_so, g_8a, k_8a, g_8b, k_8b, tong_dat, tong_dat, 2 * si_so, pct))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
