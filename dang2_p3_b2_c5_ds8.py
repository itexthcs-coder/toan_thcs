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


def bt_dang2_p3_b2_c5_ds8(self):
    # Dạng 2 (Vận dụng): Tìm giá trị quy ước của mỗi biểu tượng trên biểu đồ tranh
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        unit = random.choice([12, 15, 18, 20, 25])
        c1, c2, c3, c4 = 5, 7, 4, 8
        tong_bt = c1 + c2 + c3 + c4
        tong_san_luong = tong_bt * unit
        kq_str = str(unit)
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (-1.0, 0.2) rectangle (5.6, 3.4);
        \\draw[line width=1pt] (0.4, 0.2) -- (0.4, 3.4);
        \\draw[line width=1pt] (-1.0, 2.6) -- (5.6, 2.6);
        \\draw[line width=1pt] (-1.0, 1.8) -- (5.6, 1.8);
        \\draw[line width=1pt] (-1.0, 1.0) -- (5.6, 1.0);
        \\node at (-0.3, 3.0) {Tàu $A$};
        \\node at (-0.3, 2.2) {Tàu $B$};
        \\node at (-0.3, 1.4) {Tàu $C$};
        \\node at (-0.3, 0.6) {Tàu $D$};
        \\foreach \\i in {0,...,4} { \\draw[line width=1pt] (0.9 + \\i*0.56, 3.0) circle (0.18); }
        \\foreach \\i in {0,...,6} { \\draw[line width=1pt] (0.9 + \\i*0.56, 2.2) circle (0.18); }
        \\foreach \\i in {0,...,3} { \\draw[line width=1pt] (0.9 + \\i*0.56, 1.4) circle (0.18); }
        \\foreach \\i in {0,...,7} { \\draw[line width=1pt] (0.9 + \\i*0.56, 0.6) circle (0.18); }
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Biểu đồ tranh dưới đây biểu diễn sản lượng cá đánh bắt được của bốn tàu cá $A, B, C, D$ (mỗi hình tròn ứng với một lượng cá như nhau):%sBiết tổng sản lượng cá của cả bốn tàu là $%s$ tấn. Hỏi mỗi biểu tượng ứng với bao nhiêu tấn cá?"""
                         % (tikz_code, tong_san_luong))
        
        loigiai = ("""Quan sát biểu đồ tranh, tổng số biểu tượng của cả bốn tàu cá là:
        $$%s + %s + %s + %s = %s \\text{ (biểu tượng)}.$$
        Vì tổng sản lượng cá của cả bốn tàu là $%s$ tấn nên mỗi biểu tượng ứng với số tấn cá là:
        $$%s : %s = %s \\text{ (tấn)}.$$"""
                   % (c1, c2, c3, c4, tong_bt, tong_san_luong, tong_san_luong, tong_bt, unit))

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
