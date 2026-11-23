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


def bt_dang11_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'D', 'E', 'F', 'K'),
            ('M', 'N', 'P', 'Q', 'E', 'F', 'K')
        ])
        A, B, C, D, E, F, K = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.5);
\\coordinate (B) at (2.5,2.5);
\\coordinate (C) at (2.5,0);
\\coordinate (D) at (0,0);
\\coordinate (E) at (2.5,1.6);
\\coordinate (F) at (1.3,0);
\\coordinate (K) at (-0.9,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(E)--(F)--cycle;
\\draw[line width=1pt, dashed] (D)--(K) (A)--(K);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below] {$%s$};
\\fill (E) circle (1pt) node[right] {$%s$};
\\fill (F) circle (1pt) node[below] {$%s$};
\\fill (K) circle (1pt) node[left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, E, F, K))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình vuông $%s%s%s%s$. Trên cạnh $%s%s$ lấy điểm $%s$, trên cạnh $%s%s$ lấy điểm $%s$ sao cho $\\widehat{%s%s%s} = 45^\\circ$. \\\\
a) Chứng minh $%s%s = %s%s + %s%s$. \\\\
b) Chứng minh chu vi của $\\Delta %s%s%s$ luôn không đổi khi $%s$ và $%s$ di chuyển trên $%s%s$ và $%s%s$ sao cho $\\widehat{%s%s%s} = 45^\\circ$.%s'''
                         % (A, B, C, D, B, C, E, C, D, F, E, A, F,
                            E, F, B, E, D, F,
                            C, E, F, E, F, B, C, C, D, E, A, F, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Trên tia đối của tia $%s%s$ lấy điểm $%s$ sao cho $%s%s = %s%s$.\\\\
Xét hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có: $%s%s = %s%s$ (cạnh hình vuông), $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$, $%s%s = %s%s$ (cách dựng).\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c), do đó $%s%s = %s%s$ và $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\
Ta có $\\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s} = \\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ - \\widehat{%s%s%s} = 90^\\circ - 45^\\circ = 45^\\circ = \\widehat{%s%s%s}$.\\\\
Xét $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có: $%s%s = %s%s$, $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 45^\\circ$, cạnh $%s%s$ chung.\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c), do đó $%s%s = %s%s = %s%s + %s%s = %s%s + %s%s$.
\\item Chu vi của $\\Delta %s%s%s$ bằng:\\\\
$%s%s + %s%s + %s%s = %s%s + %s%s + (%s%s + %s%s) = (%s%s + %s%s) + (%s%s + %s%s) = %s%s + %s%s = 2%s%s$.\\\\
Vì độ dài cạnh $%s%s$ của hình vuông $%s%s%s%s$ không đổi nên chu vi của $\\Delta %s%s%s$ luôn không đổi.
\\end{enumEX} \n'''
                   % (D, C, K, D, K, B, E,
                      A, D, K, A, B, E, A, D, A, B, A, D, K, A, B, E, D, K, B, E,
                      A, D, K, A, B, E, A, K, A, E, D, A, K, B, A, E,
                      K, A, F, K, A, D, D, A, F, B, A, E, D, A, F, E, A, F, E, A, F,
                      A, K, F, A, E, F, A, K, A, E, K, A, F, E, A, F, A, F,
                      A, K, F, A, E, F, E, F, K, F, D, K, D, F, B, E, D, F,
                      C, E, F,
                      C, E, C, F, E, F, C, E, C, F, B, E, D, F, B, E, E, C, D, F, F, C, B, C, C, D, A, B,
                      A, B, A, B, C, D, C, E, F))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
