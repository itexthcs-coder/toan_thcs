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


def bt_dang1_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'H', 'M', 'D', 'E'),
            ('M', 'N', 'P', 'H', 'I', 'D', 'K')
        ])
        A, B, C, H, M, D, E = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.5);
\\coordinate (B) at (-1.5,0);
\\coordinate (C) at (1.5,0);
\\coordinate (H) at (0,0);
\\coordinate (M) at (0.75,1.25);
\\coordinate (D) at (1.5,2.5);
\\coordinate (E) at (-0.75,1.25);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(H) (H)--(D) (A)--(D)--(C) (E)--(M);
\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (H) circle (1pt) node[below] {$%s$};
\\fill (M) circle (1pt) node[right] {$%s$};
\\fill (D) circle (1pt) node[above right] {$%s$};
\\fill (E) circle (1pt) node[left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, H, M, D, E))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $\\Delta %s%s%s$ cân tại $%s$ có đường cao $%s%s$ ($%s \\in %s%s$). Gọi $%s$ là trung điểm của cạnh $%s%s$. Trên tia đối của tia $%s%s$ lấy điểm $%s$ sao cho $%s%s = %s%s$. \\\\
a) Chứng minh tứ giác $%s%s%s%s$ là hình chữ nhật. \\\\
b) Gọi $%s$ là trung điểm của cạnh $%s%s$. Chứng minh tứ giác $%s%s%s%s$ là hình thoi.%s'''
                         % (A, B, C, A, A, H, H, B, C, M, A, C, M, H, D, M, D, M, H,
                            A, H, C, D,
                            E, A, B, A, E, H, D, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Xét tứ giác $%s%s%s%s$ có $%s$ là trung điểm của $%s%s$ (giả thiết) và $%s$ là trung điểm của $%s%s$ (vì $%s$ thuộc tia đối của tia $%s%s$ và $%s%s = %s%s$).\\\\
Suy ra hai đường chéo $%s%s$ và $%s%s$ cắt nhau tại trung điểm $%s$ của mỗi đường, do đó $%s%s%s%s$ là hình bình hành.\\\\
Mặt khác $%s%s$ là đường cao của $\\Delta %s%s%s$ nên $%s%s \\perp %s%s$, tức là $\\widehat{%s%s%s} = 90^\\circ$.\\\\
Hình bình hành $%s%s%s%s$ có một góc vuông nên là hình chữ nhật.
\\item Vì $\\Delta %s%s%s$ cân tại $%s$ nên $%s%s = %s%s$ và đường cao $%s%s$ đồng thời là đường trung tuyến, suy ra $%s$ là trung điểm của $%s%s$.\\\\
Xét $\\Delta %s%s%s$ có $%s, %s$ lần lượt là trung điểm của $%s%s$ và $%s%s$ nên $%s%s$ là đường trung bình của $\\Delta %s%s%s$, suy ra $%s%s // %s%s$ và $%s%s = \\dfrac{1}{2}%s%s$.\\\\
Mà $%s%s%s%s$ là hình chữ nhật nên $%s%s // %s%s$ và $%s%s = %s%s$, kết hợp với $%s$ là trung điểm của $%s%s$ suy ra $%s%s // %s%s$ và $%s%s = %s%s$.\\\\
Do đó $%s%s%s%s$ là hình bình hành.\\\\
Lại có $%s%s = \\dfrac{1}{2}%s%s$ (vì $%s$ là trung điểm $%s%s$) và $%s%s = \\dfrac{1}{2}%s%s$ (vì $%s$ là trung điểm $%s%s$), mà $%s%s = %s%s$ nên $%s%s = %s%s$.\\\\
Hình bình hành $%s%s%s%s$ có hai cạnh kề bằng nhau nên là hình thoi.
\\end{enumEX} \n'''
                   % (A, H, C, D, M, A, C, M, H, D, D, M, H, M, D, M, H,
                      A, C, H, D, M, A, H, C, D,
                      A, H, A, B, C, A, H, B, C, A, H, C,
                      A, H, C, D,
                      A, B, C, A, A, B, A, C, A, H, H, B, C,
                      A, B, C, E, H, A, B, B, C, E, H, A, B, C, E, H, A, C, E, H, A, C,
                      A, H, C, D, A, D, H, C, A, D, H, C, H, B, C, A, D, E, H, A, D, E, H,
                      A, E, H, D,
                      A, E, A, B, E, A, B, A, M, A, C, M, A, C, A, B, A, C, A, E, A, M,
                      A, E, H, D))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
