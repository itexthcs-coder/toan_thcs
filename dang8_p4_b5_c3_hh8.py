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


def bt_dang8_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'D', 'M', 'N', 'E', 'P'),
            ('M', 'N', 'P', 'Q', 'I', 'K', 'E', 'H')
        ])
        A, B, C, D, M, N, E, P = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2);
\\coordinate (P) at (2,2);
\\coordinate (B) at (4,2);
\\coordinate (D) at (0,0);
\\coordinate (M) at (2,0);
\\coordinate (C) at (4,0);
\\coordinate (N) at (4,1);
\\coordinate (E) at (6,2);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (P)--(M) (B)--(D) (M)--(E)--(C) (B)--(E);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (P) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[above] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below left] {$%s$};
\\fill (M) circle (1pt) node[below] {$%s$};
\\fill (N) circle (1pt) node[right] {$%s$};
\\fill (E) circle (1pt) node[above right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, P, B, C, D, M, N, E))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chữ nhật $%s%s%s%s$ có $%s%s = 2%s%s$. Gọi $%s$ là trung điểm của cạnh $%s%s$. Qua $%s$ kẻ đường thẳng song song với $%s%s$ cắt $%s%s$ tại $%s$. Lấy điểm $%s$ sao cho $%s$ là trung điểm của $%s%s$. \\\\
a) Chứng minh tứ giác $%s%s%s%s$ là hình bình hành. \\\\
b) Chứng minh tứ giác $%s%s%s%s$ là hình thang cân. \\\\
c) Gọi $%s$ là trung điểm của $%s%s$. Chứng minh tứ giác $%s%s%s%s$ là hình vuông.%s'''
                         % (A, B, C, D, A, B, A, D, M, C, D, M, B, D, B, C, N, E, N, M, E,
                            M, B, E, C,
                            M, B, E, D,
                            P, A, B, A, P, M, D, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n\\item Xét $\\Delta %s%s%s$ có $%s$ là trung điểm của $%s%s$ và $%s%s // %s%s$ nên $%s$ là trung điểm của $%s%s$.\\\\\nTứ giác $%s%s%s%s$ có hai đường chéo $%s%s$ và $%s%s$ cắt nhau tại trung điểm $%s$ của mỗi đường nên là hình bình hành.\n\\item Vì $%s%s%s%s$ là hình bình hành nên $%s%s // %s%s$ và $%s%s = %s%s$.\\\\\nMà $%s$ là trung điểm $%s%s$ nên $%s%s = %s%s$, suy ra $%s%s = %s%s$ và $%s%s // %s%s$, do đó $%s%s%s%s$ là hình bình hành, suy ra $%s%s = %s%s$.\\\\\nMặt khác $%s%s%s%s$ là hình bình hành nên $%s%s = %s%s$, suy ra $%s%s = %s%s$.\\\\\nTứ giác $%s%s%s%s$ có $%s%s // %s%s$ (do $%s%s // %s%s$) nên là hình thang, lại có hai đường chéo $%s%s = %s%s$ nên là hình thang cân.\n\\item Vì $%s%s%s%s$ là hình chữ nhật nên $%s%s // %s%s$, $%s%s = %s%s$ và $\\widehat{%s} = 90^\\circ$.\\\\\nMà $%s, %s$ lần lượt là trung điểm của $%s%s$ và $%s%s$ nên $%s%s = %s%s = \\dfrac{%s%s}{2} = %s%s$ và $%s%s // %s%s$.\\\\\nSuy ra tứ giác $%s%s%s%s$ là hình bình hành. Hình bình hành $%s%s%s%s$ có $\\widehat{%s} = 90^\\circ$ và hai cạnh kề $%s%s = %s%s$ nên là hình vuông.\n\\end{enumEX} \n'''
                   % (B, C, D, M, C, D, M, N, B, D, N, B, C, M, B, E, C, B, C, M, E, N, M, B, E, C, B, E, M, C, B, E, M, C, M, C, D, D, M, M, C, B, E, D, M, B, E, D, M, M, B, E, D, M, B, E, D, M, B, E, C, M, E, B, C, M, E, B, D, M, B, E, D, B, E, M, D, B, E, C, D, M, E, B, D, A, B, C, D, A, B, C, D, A, B, C, D, A, P, M, A, B, C, D, A, P, D, M, A, B, A, D, A, P, D, M, A, P, M, D, A, P, M, D, A, A, P, A, D))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
