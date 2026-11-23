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


def bt_dang13_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'M', 'D', 'E', 'H', 'K'),
            ('M', 'N', 'P', 'I', 'D', 'E', 'H', 'K')
        ])
        A, B, C, M, D, E, H, K = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (-1.5,0);
\\coordinate (C) at (1.5,0);
\\coordinate (M) at (-0.4,0);
\\coordinate (D) at (-1.15,0.6);
\\coordinate (E) at (0.98,0.9);
\\coordinate (H) at (0.75,1.3);
\\coordinate (K) at (-0.17,0.75);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(D) (M)--(E) (B)--(H) (M)--(K);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (M) circle (1pt) node[below] {$%s$};
\\fill (D) circle (1pt) node[left] {$%s$};
\\fill (E) circle (1pt) node[right] {$%s$};
\\fill (H) circle (1pt) node[above right] {$%s$};
\\fill (K) circle (1pt) node[above left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, M, D, E, H, K))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $\\Delta %s%s%s$ cân tại $%s$, điểm $%s$ di chuyển trên cạnh $%s%s$ ($%s$ khác $%s, %s$). Gọi $%s$ và $%s$ lần lượt là chân đường vuông góc hạ từ $%s$ xuống $%s%s$ và $%s%s$; $%s%s$ là đường cao của $\\Delta %s%s%s$ ($%s \\in %s%s$). \\\\
a) Kẻ $%s%s \\perp %s%s$ ($%s \\in %s%s$). Chứng minh tứ giác $%s%s%s%s$ là hình chữ nhật. \\\\
b) Chứng minh tổng khoảng cách $%s%s + %s%s$ không phụ thuộc vào vị trí của điểm $%s$ trên cạnh $%s%s$.%s'''
                         % (A, B, C, A, M, B, C, M, B, C, D, E, M, A, B, A, C, B, H, A, B, C, H, A, C,
                            M, K, B, H, K, B, H, M, K, H, E,
                            M, D, M, E, M, B, C, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Tứ giác $%s%s%s%s$ có $\\widehat{%s%s%s} = 90^\\circ$ ($%s%s \\perp %s%s$), $\\widehat{%s%s%s} = 90^\\circ$ ($%s%s \\perp %s%s$) và $\\widehat{%s%s%s} = 90^\\circ$ ($%s%s \\perp %s%s$).\\\\
Tứ giác $%s%s%s%s$ có ba góc vuông nên là hình chữ nhật.
\\item Vì $%s%s%s%s$ là hình chữ nhật nên $%s%s // %s%s$ và $%s%s = %s%s$.\\\\
Suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc đồng vị).\\\\
Mà $\\Delta %s%s%s$ cân tại $%s$ nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$, do đó $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\
Xét hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có cạnh huyền $%s%s$ chung và $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.h - g.n), do đó $%s%s = %s%s$.\\\\
Vậy $%s%s + %s%s = %s%s + %s%s = %s%s$. Vì $\\Delta %s%s%s$ cố định nên đường cao $%s%s$ không đổi, do đó tổng $%s%s + %s%s$ không phụ thuộc vào vị trí của $%s$ trên cạnh $%s%s$.
\\end{enumEX} \n'''
                   % (M, K, H, E, M, K, H, M, K, B, H, K, H, E, B, H, A, C, H, E, M, M, E, A, C,
                      M, K, H, E,
                      M, K, H, E, M, K, A, C, K, H, M, E,
                      K, M, B, A, C, B,
                      A, B, C, A, A, B, C, A, C, B, D, B, M, K, M, B,
                      M, D, B, M, K, B, B, M, D, B, M, K, M, B,
                      M, D, B, M, K, B, M, D, B, K,
                      M, D, M, E, B, K, K, H, B, H, A, B, C, B, H, M, D, M, E, M, B, C))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
