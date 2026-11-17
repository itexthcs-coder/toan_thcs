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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
### CÔNG CỤ
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang18_p1_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        mau = random.choice([2, 3, 4])
        a_val = Rational(1, mau)
        x0 = random.randint(2, 5)
        x_bp = x0 ** 2
        y0 = a_val * x_bp
        while y0.q != 1:
            x0 = random.randint(2, 5)
            x_bp = x0 ** 2
            y0 = a_val * x_bp
        mn_len = 2 * x0
        dien_tich = Rational(1, 2) * mn_len * y0

        # Các đáp án trắc nghiệm
        du = ['$%s$ (đvdt)' % (dien_tich)]
        da = random.choice(du)
        s = [
            '$%s$ (đvdt)' % (2 * dien_tich),
            '$%s$ (đvdt)' % (latex(Rational(dien_tich, 2))),
            '$%s$ (đvdt)' % (mn_len + y0),
            '$%s$ (đvdt)' % (4 * dien_tich)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Trên đồ thị của hàm số $y=%sx^2$, lấy hai điểm $M$ và $N$ có cùng tung độ bằng $%s$ ($M$ có hoành độ âm, $N$ có hoành độ dương). Diện tích tam giác $OMN$ (với $O$ là gốc tọa độ) bằng'''
                         % (latex(a_val), y0))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Thay $y=%s$ vào công thức hàm số $y=%sx^2$, ta có:\\\\
                    $%sx^2 = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = -%s$ hoặc $x = %s$.\\\\
                    Do $M$ có hoành độ âm và $N$ có hoành độ dương nên $M(-%s; %s)$ và $N(%s; %s)$.\\\\
                    Gọi $H(0; %s)$ là giao điểm của đoạn thẳng $MN$ với trục tung $Oy$, ta có hình minh họa sau:\\\\
                    \\begin{center}
                    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                    \\coordinate (O) at (0,0);
                    \\coordinate (M) at (-1.5,2);
                    \\coordinate (N) at (1.5,2);
                    \\coordinate (H) at (0,2);
                    \\draw[->, line width=1pt] (-2.3,0)--(2.3,0) node[below] {$x$};
                    \\draw[->, line width=1pt] (0,-0.4)--(0,2.7) node[left] {$y$};
                    \\draw[line width=1pt, smooth, samples=100, domain=-1.7:1.7] plot (\\x, {0.888*\\x*\\x});
                    \\draw[line width=1pt] (O)--(M)--(N)--cycle;
                    \\fill (O) circle (1pt) node[below left] {$O$};
                    \\fill (M) circle (1pt) node[left] {$M$};
                    \\fill (N) circle (1pt) node[right] {$N$};
                    \\fill (H) circle (1pt) node[above right] {$H$};
                    \\end{tikzpicture}
                    \\end{center}
                    Khi đó $OH \\perp MN$ tại $H$, với chiều cao $OH = %s$ và độ dài cạnh đáy $MN = |%s - (-%s)| = %s$.\\\\
                    Diện tích tam giác $OMN$ là:\\\\
                    $S_{OMN} = \\frac{1}{2} \\cdot OH \\cdot MN = \\frac{1}{2} \\cdot %s \\cdot %s = %s$ (đvdt).\\\\
                    Vậy diện tích tam giác $OMN$ bằng $%s$ (đvdt).'''
                   % (y0, latex(a_val), latex(a_val), y0, x_bp, x0, x0,
                      x0, y0, x0, y0, y0, y0, x0, x0, mn_len, y0, mn_len, dien_tich, dien_tich))

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
