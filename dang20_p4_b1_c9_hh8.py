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


def bt_dang20_p4_b1_c9_hh8(self):
    # Dạng 20: Ứng dụng tam giác đồng dạng trong thiết kế dốc cầu thang / đường dẫn xe lăn
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([2, 3, 4])
        AM = random.choice([2, 3, 4])
        AC = AM * k
        
        h_cot_cm = random.choice([25, 30, 35])
        h_cot = Decimal(h_cot_cm) / Decimal(100)
        str_h_cot = str(h_cot).replace('.', ',')
        
        h_them = h_cot * Decimal(k)
        str_h_them = str(h_them.normalize()).replace('.', ',')
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (5.5,0);\n'
            '\\coordinate (C) at (5.5,1.8);\n'
            '\\coordinate (M) at ($(A)!0.35!(C)$);\n'
            '\\coordinate (N) at ($(A)!0.35!(B)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[above right] {$C$};\n'
            '\\fill (M) circle (1pt) node[above left] {$M$};\n'
            '\\fill (N) circle (1pt) node[below] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Để xây dựng một đường dốc thoải cho xe lăn từ mặt sân lên thềm nhà cao $BC = %s\\text{ m}$, '
            'người ta thiết kế mặt cắt đường dốc là tam giác $ABC$ vuông tại $B$ có chiều dài mặt dốc $AC = %s\\text{ m}$. '
            'Tại vị trí $M$ trên mặt dốc cách chân dốc $A$ một khoảng $AM = %s\\text{ m}$, người ta dựng một cột trụ $MN$ thẳng đứng '
            '($N \\in AB$, $MN \\perp AB$) chống đỡ mặt dốc. Tính chiều cao $MN$ của cột trụ chống đỡ đó.\\\n%s'
            % (str_h_them, AC, AM, tikz)
        )
        
        loigiai = (
            'Vì cột trụ $MN$ và tường thềm nhà $BC$ cùng thẳng đứng nên $MN \\perp AB$ và $BC \\perp AB$, suy ra $MN // BC$.\\\n'
            'Xét $\\Delta ABC$ có $MN // BC$ ($M \\in AC$, $N \\in AB$) nên $\\Delta AMN \\backsim \\Delta ACB$.\\\n'
            'Suy ra $\\dfrac{MN}{BC} = \\dfrac{AM}{AC}$.\\\n'
            'Thay $BC = %s\\text{ m}$, $AM = %s\\text{ m}$, $AC = %s\\text{ m}$ ta được:\\\n'
            '$\\dfrac{MN}{%s} = \\dfrac{%s}{%s} \\Rightarrow MN = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (m)}$.\\\n'
            'Vậy chiều cao của cột trụ chống đỡ là $%s\\text{ m}$.'
            % (str_h_them, AM, AC, str_h_them, AM, AC, str_h_them, AM, AC, str_h_cot, str_h_cot)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
