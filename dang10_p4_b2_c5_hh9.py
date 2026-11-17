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

def bt_dang10_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_pytago = random.choice([(5, 12, 13), (3, 4, 5), (6, 8, 10), (8, 15, 17)])
        OI, AI_min, R = bo_pytago
        AB_min = 2 * AI_min
        AB_max = 2 * R
        so_giua = AB_max - AB_min - 1
        so_day_nguyen = 2 + 2 * so_giua

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ và điểm $I$ cố định nằm trong đường tròn sao cho $OI = %s\\text{ cm}$ (như hình vẽ).\\\\
                         a) Chứng minh rằng mọi dây cung $AB$ đi qua $I$ của đường tròn $(O)$ đều có độ dài không nhỏ hơn $%s\\text{ cm}$.\\\\
                         b) Hỏi có tất cả bao nhiêu dây cung đi qua $I$ có độ dài là một số nguyên?
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (I) at (0,0.7);
                         \\coordinate (A) at (157:1.8);
                         \\coordinate (B) at (23:1.8);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (A)--(B) (O)--(A);
                         \\draw[line width=1pt, dashed] (O)--(I);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (I) circle (1pt) node[above] {$I$};
                         \\fill (A) circle (1pt) node[above left] {$A$};
                         \\fill (B) circle (1pt) node[above right] {$B$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (R, OI, AB_min))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Kẻ $OH \\perp AB$ tại $H$. Trong tam giác $OHI$ vuông tại $H$ (hoặc khi $H \\equiv I$), ta luôn có $OH \\le OI = %s\\text{ cm}$.\\\\
                        Áp dụng định lí Pythagore trong tam giác $OHA$ vuông tại $H$, ta có:\\\\
                        $AH = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - OH^2} \\ge \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$.\\\\
                        Vậy độ dài dây cung $AB = 2AH \\ge 2 \\cdot %s = %s\\text{ cm}$.
                        \\item Độ dài mọi dây cung $AB$ đi qua $I$ thỏa mãn $%s\\text{ cm} \\le AB \\le 2R = %s\\text{ cm}$.\\\\
                        - Với $AB = %s\\text{ cm}$ (giá trị nhỏ nhất): có duy nhất $1$ dây cung (dây vuông góc với $OI$ tại $I$).\\\\
                        - Với $AB = %s\\text{ cm}$ (giá trị lớn nhất): có duy nhất $1$ dây cung (đường kính đi qua $I$).\\\\
                        - Với mỗi giá trị nguyên $k$ thỏa mãn $%s < k < %s$ (gồm $%s$ giá trị nguyên), do tính đối xứng của đường tròn qua đường thẳng $OI$ nên ứng với mỗi giá trị $k$ có $2$ dây cung đi qua $I$ có độ dài bằng $k\\text{ cm}$.\\\\
                        Vậy có tất cả $1 + 1 + 2 \\cdot %s = %s$ dây cung đi qua $I$ có độ dài là một số nguyên.
                        \\end{enumEX}'''
                   % (OI, R, R, OI, AI_min, AI_min, AB_min,
                      AB_min, AB_max, AB_min, AB_max, AB_min, AB_max,
                      so_giua, so_giua, so_day_nguyen))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
