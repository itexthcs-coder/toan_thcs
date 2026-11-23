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


def bt_dang2_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_dinh = random.choice([
            ('A', 'B', 'C', 'D', 'E', 'F', 'K'),
            ('M', 'N', 'P', 'D', 'E', 'F', 'I')
        ])
        A, B, C, D, E, F, K = bo_dinh

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0.6,2.5);
\\coordinate (B) at (-1.2,0);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0.38,0);
\\coordinate (E) at (1.52,1.35);
\\coordinate (F) at (-0.36,1.16);
\\coordinate (K) at (-0.23,1.35);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (D)--(E) (D)--(F) (E)--(K);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below] {$%s$};
\\fill (E) circle (1pt) node[right] {$%s$};
\\fill (F) circle (1pt) node[left] {$%s$};
\\fill (K) circle (1pt) node[above left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, E, F, K))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho $\\Delta %s%s%s$ nhọn ($%s%s < %s%s$), tia phân giác của góc $\\widehat{%s%s%s}$ cắt cạnh $%s%s$ tại $%s$. Qua $%s$ kẻ đường thẳng song song với $%s%s$ cắt $%s%s$ tại $%s$, qua $%s$ kẻ đường thẳng song song với $%s%s$ cắt $%s%s$ tại $%s$. \\\\
a) Chứng minh tứ giác $%s%s%s%s$ là hình thoi. \\\\
b) Đường thẳng qua $%s$ song song với $%s%s$ cắt $%s%s$ tại $%s$. Chứng minh $%s%s = %s%s$.%s'''
                         % (A, B, C, A, B, A, C, B, A, C, B, C, D, D, A, B, A, C, E, D, A, C, A, B, F,
                            A, F, D, E,
                            E, B, C, A, B, K, A, E, B, K, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Xét tứ giác $%s%s%s%s$ có $%s%s // %s%s$ (vì $%s%s // %s%s$) và $%s%s // %s%s$ (vì $%s%s // %s%s$).\\\\
Suy ra tứ giác $%s%s%s%s$ là hình bình hành.\\\\
Mặt khác, đường chéo $%s%s$ là tia phân giác của góc $\\widehat{%s%s%s}$ (giả thiết).\\\\
Theo dấu hiệu nhận biết hình thoi, hình bình hành có một đường chéo là đường phân giác của một góc là hình thoi.\\\\
Vậy tứ giác $%s%s%s%s$ là hình thoi.
\\item Xét tứ giác $%s%s%s%s$ có $%s%s // %s%s$ (giả thiết) và $%s%s // %s%s$ (do $%s%s // %s%s$).\\\\
Suy ra tứ giác $%s%s%s%s$ là hình bình hành, do đó $%s%s = %s%s$ (hai cạnh đối của hình bình hành).\\\\
Vì $%s%s%s%s$ là hình thoi (chứng minh ở câu a) nên $%s%s = %s%s$.\\\\
Từ hai đẳng thức trên suy ra $%s%s = %s%s$.
\\end{enumEX} \n'''
                   % (A, F, D, E, D, E, A, F, D, E, A, B, D, F, A, E, D, F, A, C,
                      A, F, D, E,
                      A, D, F, A, E,
                      A, F, D, E,
                      B, K, E, D, K, E, B, D, K, B, E, D, D, E, A, B,
                      B, K, E, D, B, K, E, D,
                      A, F, D, E, A, E, E, D,
                      A, E, B, K))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
