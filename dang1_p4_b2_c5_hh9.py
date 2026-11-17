# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang1_p4_b2_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tam = random.choice(['O', 'I'])
        bk = random.choice(['R', 'r'])

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(%s; %s)$ và hai dây cung $AB, CD$ không đi qua tâm. Gọi $H, K$ lần lượt là hình chiếu vuông góc của tâm $%s$ trên $AB$ và $CD$ (như hình vẽ).\\\\
                         a) Chứng minh rằng $AB^2 + 4%sH^2 = CD^2 + 4%sK^2$.\\\\
                         b) Từ đó chứng minh rằng nếu $%sH < %sK$ thì $AB > CD$, và ngược lại nếu $AB > CD$ thì $%sH < %sK$.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (150:1.8);
                         \\coordinate (B) at (30:1.8);
                         \\coordinate (C) at (-135:1.8);
                         \\coordinate (D) at (-45:1.8);
                         \\coordinate (H) at (0,0.9);
                         \\coordinate (K) at (0,-1.27);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (A)--(B) (C)--(D) (O)--(A) (O)--(C);
                         \\draw[line width=1pt, dashed] (O)--(H) (O)--(K);
                         \\fill (O) circle (1pt) node[left] {$%s$};
                         \\fill (A) circle (1pt) node[above left] {$A$};
                         \\fill (B) circle (1pt) node[above right] {$B$};
                         \\fill (C) circle (1pt) node[below left] {$C$};
                         \\fill (D) circle (1pt) node[below right] {$D$};
                         \\fill (H) circle (1pt) node[above] {$H$};
                         \\fill (K) circle (1pt) node[below] {$K$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (tam, bk, tam, tam, tam, tam, tam, tam, tam, tam))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì tam giác $%sAB$ cân tại $%s$ ($%sA = %sB = %s$) có đường cao $%sH$ nên $H$ là trung điểm của $AB$, suy ra $AH = \\dfrac{AB}{2}$.\\\\
                        Áp dụng định lí Pythagore trong tam giác $%sHA$ vuông tại $H$, ta có:\\\\
                        $%sH^2 + AH^2 = %sA^2 \\Leftrightarrow %sH^2 + \\left(\\dfrac{AB}{2}\\right)^2 = %s^2 \\Leftrightarrow AB^2 + 4%sH^2 = 4%s^2$.\\\\
                        Chứng minh hoàn toàn tương tự với dây cung $CD$, ta được $CD^2 + 4%sK^2 = 4%s^2$.\\\\
                        Từ đó suy ra $AB^2 + 4%sH^2 = CD^2 + 4%sK^2$.
                        \\item Từ đẳng thức $AB^2 + 4%sH^2 = CD^2 + 4%sK^2$, suy ra $AB^2 - CD^2 = 4(%sK^2 - %sH^2)$.\\\\
                        - Nếu $%sH < %sK$ thì $%sK^2 - %sH^2 > 0$ (do $%sH, %sK > 0$), suy ra $AB^2 - CD^2 > 0 \\Rightarrow AB > CD$ (do $AB, CD > 0$).\\\\
                        - Ngược lại, nếu $AB > CD$ thì $AB^2 - CD^2 > 0$, suy ra $4(%sK^2 - %sH^2) > 0 \\Rightarrow %sK^2 > %sH^2 \\Rightarrow %sH < %sK$.
                        \\end{enumEX}'''
                   % (tam, tam, tam, tam, bk, tam,
                      tam, tam, tam, tam, bk, tam, bk,
                      tam, bk, tam, tam,
                      tam, tam, tam, tam,
                      tam, tam, tam, tam, tam, tam,
                      tam, tam, tam, tam, tam, tam))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
