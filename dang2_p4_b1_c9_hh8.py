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


def bt_dang2_p4_b1_c9_hh8(self):
    # Dạng 2: Tìm tỉ số đồng dạng và chu vi của tam giác tạo bởi đường thẳng song song
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([3, 5, 7])
        while math.gcd(a, b) != 1:
            b = random.choice([3, 5, 7])
        tong = a + b
        chu_vi_ABC = tong * random.choice([4, 5, 6, 7])
        chu_vi_ADE = chu_vi_ABC * a // tong
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (A) at (2,3.5);\n'
            '\\coordinate (D) at ($(A)!0.4!(B)$);\n'
            '\\coordinate (E) at ($(A)!0.4!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (D) circle (1pt) node[left] {$D$};\n'
            '\\fill (E) circle (1pt) node[right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC$ có chu vi bằng $%s\\text{ cm}$. Trên cạnh $AB$ lấy điểm $D$ sao cho $\\dfrac{AD}{DB} = \\dfrac{%s}{%s}$. '
            'Qua $D$ kẻ đường thẳng song song với $BC$ cắt $AC$ tại $E$.\\\n'
            'a) Chứng minh $\\Delta ADE \\backsim \\Delta ABC$ và tìm tỉ số đồng dạng.\\\n'
            'b) Tính chu vi của $\\Delta ADE$.\\\n%s'
            % (chu_vi_ABC, a, b, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\Delta ABC$ có $DE // BC$ ($D \\in AB$, $E \\in AC$) nên $\\Delta ADE \\backsim \\Delta ABC$.\\\n'
            'Vì $\\dfrac{AD}{DB} = \\dfrac{%s}{%s}$ và $D$ nằm giữa $A$ và $B$ nên $\\dfrac{AD}{AB} = \\dfrac{AD}{AD + DB} = \\dfrac{%s}{%s + %s} = \\dfrac{%s}{%s}$.\\\n'
            'Vậy $\\Delta ADE \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$.\n'
            '\\item Vì $\\Delta ADE \\backsim \\Delta ABC$ theo tỉ số đồng dạng $k = \\dfrac{%s}{%s}$ nên $\\dfrac{AD}{AB} = \\dfrac{AE}{AC} = \\dfrac{DE}{BC} = \\dfrac{%s}{%s}$.\\\n'
            'Áp dụng tính chất của dãy tỉ số bằng nhau, ta có:\\\n'
            '$\\dfrac{AD}{AB} = \\dfrac{AE}{AC} = \\dfrac{DE}{BC} = \\dfrac{AD + AE + DE}{AB + AC + BC} = \\dfrac{C_{\\Delta ADE}}{C_{\\Delta ABC}} = \\dfrac{%s}{%s}$.\\\n'
            'Suy ra chu vi của $\\Delta ADE$ là: $C_{\\Delta ADE} = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (a, b, a, a, b, a, tong, a, tong,
               a, tong, a, tong, a, tong, a, tong, chu_vi_ABC, chu_vi_ADE)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
