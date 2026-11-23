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


def bt_dang12_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'D', 'M', 'E', 'F'),
            ('M', 'N', 'P', 'Q', 'I', 'E', 'F')
        ])
        A, B, C, D, M, E, F = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.5);
\\coordinate (B) at (2.5,2.5);
\\coordinate (C) at (2.5,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at (0.9,0.9);
\\coordinate (E) at (0.9,2.5);
\\coordinate (F) at (0,0.9);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (B)--(D) (M)--(E) (M)--(F) (C)--(F) (D)--(E) (C)--(M) (B)--(F);
\\draw[line width=1pt] (0,2.3)--(0.2,2.3)--(0.2,2.5);
\\draw[line width=1pt] (0.9,2.3)--(1.1,2.3)--(1.1,2.5);
\\draw[line width=1pt] (0,1.1)--(0.2,1.1)--(0.2,0.9);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below left] {$%s$};
\\fill (M) circle (1pt) node[below right] {$%s$};
\\fill (E) circle (1pt) node[above] {$%s$};
\\fill (F) circle (1pt) node[left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, M, E, F))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình vuông $%s%s%s%s$. Lấy điểm $%s$ nằm trên đường chéo $%s%s$ ($%s$ khác $%s, %s$). Hạ $%s%s \\perp %s%s$ ($%s \\in %s%s$) và $%s%s \\perp %s%s$ ($%s \\in %s%s$). \\\\
a) Chứng minh $%s%s = %s%s$ và $%s%s \\perp %s%s$. \\\\
b) Chứng minh ba đường thẳng $%s%s, %s%s, %s%s$ đồng quy tại một điểm.%s'''
                         % (A, B, C, D, M, B, D, M, B, D, M, E, A, B, E, A, B, M, F, A, D, F, A, D,
                            C, F, D, E, C, F, D, E,
                            C, M, B, F, D, E, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Tứ giác $%s%s%s%s$ có $\\widehat{%s} = \\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$ nên là hình chữ nhật.\\\\
Mặt khác đường chéo $%s%s$ của hình vuông $%s%s%s%s$ là tia phân giác của $\\widehat{%s%s%s}$ nên hình chữ nhật $%s%s%s%s$ là hình vuông.\\\\
Suy ra $%s%s = %s%s = %s%s$.\\\\
Xét hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có: $%s%s = %s%s$, $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$, $%s%s = %s%s$.\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c), do đó $%s%s = %s%s$ và $\\widehat{%s%s%s} = \\widehat{%s%s%s}$.\\\\
Vì $\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$ nên $\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$, suy ra $%s%s \\perp %s%s$.
\\item Tương tự câu a, ta chứng minh được $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c) nên $%s%s \\perp %s%s$ (với $%s%s = %s%s = %s%s$).\\\\
Lại có $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c) nên $%s%s \\perp %s%s$.\\\\
Xét $\\Delta %s%s%s$ có: $%s%s \\perp %s%s$, $%s%s \\perp %s%s$ và $%s%s \\perp %s%s$ nên $%s%s, %s%s, %s%s$ là ba đường cao của $\\Delta %s%s%s$.\\\\
Vậy ba đường thẳng $%s%s, %s%s, %s%s$ đồng quy tại trực tâm của $\\Delta %s%s%s$.
\\end{enumEX} \n'''
                   % (A, E, M, F, A, A, E, M, A, F, M,
                      B, D, A, B, C, D, A, B, D, A, E, M, F,
                      A, E, M, F, A, F,
                      C, D, F, D, A, E, C, D, D, A, C, D, F, D, A, E, D, F, A, E,
                      C, D, F, D, A, E, C, F, D, E, D, C, F, A, D, E,
                      D, C, F, D, F, C, A, D, E, D, F, C, C, F, D, E,
                      B, A, F, C, B, E, B, F, C, E, B, E, M, F, A, F,
                      M, E, F, C, M, E, C, M, E, F,
                      C, E, F, C, M, E, F, B, F, C, E, D, E, C, F, C, M, B, F, D, E, C, E, F,
                      C, M, B, F, D, E, C, E, F))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
