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


def bt_dang19_p4_b1_c9_hh8(self):
    # Dạng 19: Tính đường kính vùng chiếu sáng đèn pha sân khấu
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        p = random.choice([2, 3, 4])
        q = 5
        H = q * random.choice([1, 2])
        h_phong = (q - p) * (H // q)
        d_san = q * random.choice([1, 2])
        d_phong = p * (d_san // q)
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (4.5,0);\n'
            '\\coordinate (S) at (2.25,4);\n'
            '\\coordinate (H) at (2.25,0);\n'
            '\\coordinate (M) at ($(S)!0.6!(A)$);\n'
            '\\coordinate (N) at ($(S)!0.6!(B)$);\n'
            '\\coordinate (K) at ($(S)!0.6!(H)$);\n'
            '\\draw[line width=1pt] (S)--(A)--(B)--cycle (M)--(N);\n'
            '\\draw[line width=1pt, dashed] (S)--(H);\n'
            '\\fill (S) circle (1pt) node[above] {$S$};\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (H) circle (1pt) node[below] {$H$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (K) circle (1pt) node[above right] {$K$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Một đèn chiếu sân khấu đặt tại vị trí $S$ trên trần nhà cao $SH = %s\\text{ m}$ chiếu một chùm sáng đối xứng xuống mặt sàn phẳng '
            'tạo thành một vùng sáng có đường kính $AB = %s\\text{ m}$ ($H$ là trung điểm của $AB$ và $SH \\perp AB$). '
            'Nếu đặt một tấm phông chắn sáng $MN$ nằm ngang song song với mặt sàn ($M \\in SA$, $N \\in SB$) ở độ cao $KH = %s\\text{ m}$ so với mặt sàn '
            '($K$ là giao điểm của $SH$ và $MN$) thì đường kính $MN$ của vùng sáng in trên tấm phông đó bằng bao nhiêu mét?\\\n%s'
            % (H, d_san, h_phong, tikz)
        )
        
        loigiai = (
            'Ta có khoảng cách từ đèn $S$ đến tấm phông $MN$ là: $SK = SH - KH = %s - %s = %s\\text{ (m)}$.\\\n'
            'Xét $\\Delta SAH$ có $MK // AH$ ($M \\in SA$, $K \\in SH$) nên $\\Delta SMK \\backsim \\Delta SAH$, suy ra $\\dfrac{SM}{SA} = \\dfrac{SK}{SH} = \\dfrac{%s}{%s}$.\\\n'
            'Xét $\\Delta SAB$ có $MN // AB$ ($M \\in SA$, $N \\in SB$) nên $\\Delta SMN \\backsim \\Delta SAB$.\\\n'
            'Suy ra $\\dfrac{MN}{AB} = \\dfrac{SM}{SA} = \\dfrac{%s}{%s} \\Rightarrow MN = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (m)}$.\\\n'
            'Vậy đường kính vùng sáng in trên tấm phông bằng $%s\\text{ m}$.'
            % (H, h_phong, H - h_phong, H - h_phong, H, p, q, p, q, d_san, d_phong, d_phong)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
