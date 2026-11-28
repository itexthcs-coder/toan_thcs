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


def bt_dang10_p4_b1_c9_hh8(self):
    # Dạng 10: Tính độ dài đoạn thẳng song song xen giữa hai cạnh bên của hình thang
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([1, 2])
        b = random.choice([3, 5])
        while math.gcd(a, b) != 1:
            b = random.choice([3, 5])
        tong = a + b
        
        m1 = random.choice([2, 3])
        AB = tong * m1
        MI = b * m1
        
        m2 = random.choice([4, 5, 6])
        CD = tong * m2
        IN = a * m2
        
        MN = MI + IN
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (6,0);\n'
            '\\coordinate (A) at (1.5,3);\n'
            '\\coordinate (B) at (4,3);\n'
            '\\coordinate (M) at ($(A)!0.35!(D)$);\n'
            '\\coordinate (N) at ($(B)!0.35!(C)$);\n'
            '\\coordinate (I) at (intersection of M--N and B--D);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (B)--(D) (M)--(N);\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[above right] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (I) circle (1pt) node[above right] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hình thang $ABCD$ ($AB // CD$) có $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$. '
            'Trên cạnh bên $AD$ lấy điểm $M$ sao cho $\\dfrac{AM}{MD} = \\dfrac{%s}{%s}$. '
            'Qua $M$ kẻ đường thẳng song song với hai đáy cắt $BD$ tại $I$ và cắt $BC$ tại $N$.\\\n'
            'a) Chứng minh $\\Delta DMI \\backsim \\Delta DAB$ và $\\Delta BNI \\backsim \\Delta BCD$.\\\n'
            'b) Tính độ dài đoạn thẳng $MN$.\\\n%s'
            % (AB, CD, a, b, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\Delta DAB$ có $MI // AB$ ($M \\in AD$, $I \\in BD$) nên $\\Delta DMI \\backsim \\Delta DAB$.\\\n'
            'Vì $MN // AB // CD$, áp dụng định lí Thalès trong hình thang $ABCD$ ta có $\\dfrac{BN}{NC} = \\dfrac{BI}{ID} = \\dfrac{AM}{MD} = \\dfrac{%s}{%s}$.\\\n'
            'Xét $\\Delta BCD$ có $IN // CD$ ($I \\in BD$, $N \\in BC$) nên $\\Delta BNI \\backsim \\Delta BCD$.\n'
            '\\item Từ $\\dfrac{AM}{MD} = \\dfrac{%s}{%s}$ suy ra $\\dfrac{MD}{AD} = \\dfrac{%s}{%s}$ và $\\dfrac{BI}{BD} = \\dfrac{%s}{%s}$.\\\n'
            '- Vì $\\Delta DMI \\backsim \\Delta DAB$ nên $\\dfrac{MI}{AB} = \\dfrac{MD}{AD} = \\dfrac{%s}{%s} \\Rightarrow MI = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\\\n'
            '- Vì $\\Delta BNI \\backsim \\Delta BCD$ nên $\\dfrac{IN}{CD} = \\dfrac{BI}{BD} = \\dfrac{%s}{%s} \\Rightarrow IN = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\\\n'
            'Vậy độ dài đoạn thẳng $MN$ là: $MN = MI + IN = %s + %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (a, b,
               a, b, b, tong, a, tong,
               b, tong, b, tong, AB, MI,
               a, tong, a, tong, CD, IN,
               MI, IN, MN)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
