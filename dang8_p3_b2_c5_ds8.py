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


def bt_dang8_p3_b2_c5_ds8(self):
    # Dạng 8 (Vận dụng): Chuyển đổi biểu đồ quạt tròn sang biểu đồ cột đơn sau khi điều chuyển số liệu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tong_hs = random.choice([200, 300, 400])
        tt1 = tong_hs * 45 // 100
        nt1 = tong_hs * 30 // 100
        kh1 = tong_hs * 25 // 100
        chuyen = tong_hs * 5 // 100
        tt2 = tt1 - chuyen
        nt2 = nt1
        kh2 = kh1 + chuyen
        hieu = tt2 - nt2
        kq_str = str(hieu)
        
        tikz_code = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (0,0) circle (1.5);
        \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (162:1.5) (0,0) -- (270:1.5);
        \\node at (81:0.9) {$45\\%%$};
        \\node at (216:0.9) {$30\\%%$};
        \\node at (315:0.9) {$25\\%%$};
        \\node[right] at (1.9, 0.6) {Thể thao: $45\\%%$};
        \\node[right] at (1.9, 0.0) {Nghệ thuật: $30\\%%$};
        \\node[right] at (1.9, -0.6) {Khoa học: $25\\%%$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Biểu đồ hình quạt tròn dưới đây cho biết tỉ lệ học sinh tham gia các câu lạc bộ của $%s$ học sinh khối 8 ở học kì I:%sSang học kì II, có $%s$ học sinh chuyển từ câu lạc bộ Thể thao sang câu lạc bộ Khoa học (tổng số học sinh không đổi). Nếu vẽ biểu đồ cột đơn biểu diễn số học sinh của ba câu lạc bộ ở học kì II, thì cột cao nhất hơn cột thấp nhất bao nhiêu học sinh?"""
                         % (tong_hs, tikz_code, chuyen))
        
        loigiai = ("""Số học sinh của từng câu lạc bộ ở học kì I là:\\\\
        - Câu lạc bộ Thể thao: $%s \\cdot 45\\%% = %s$ (học sinh).\\\\
        - Câu lạc bộ Nghệ thuật: $%s \\cdot 30\\%% = %s$ (học sinh).\\\\
        - Câu lạc bộ Khoa học: $%s \\cdot 25\\%% = %s$ (học sinh).\\\\
        Sang học kì II, sau khi chuyển $%s$ học sinh từ Thể thao sang Khoa học thì số học sinh của ba câu lạc bộ lần lượt là: Thể thao có $%s - %s = %s$ em; Nghệ thuật có $%s$ em; Khoa học có $%s + %s = %s$ em.\\\\
        Trên biểu đồ cột đơn ở học kì II, cột cao nhất ứng với $%s$ học sinh và cột thấp nhất ứng với $%s$ học sinh, chênh lệch nhau: $%s - %s = %s$ (học sinh)."""
                   % (tong_hs, tt1, tong_hs, nt1, tong_hs, kh1, chuyen,
                      tt1, chuyen, tt2, nt2, kh1, chuyen, kh2,
                      tt2, nt2, tt2, nt2, hieu))

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
