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


def bt_dang14_p4_b1_c9_hh8(self):
    # Dạng 14: Bài toán hai đường thẳng song song tạo nhiều tầng tam giác đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        OA = random.choice([3, 4, 6])
        AB = random.choice([3, 4, 6])
        BC = random.choice([3, 6, 9])
        
        m = random.choice([2, 3])
        OD = OA * m
        DE = AB * m
        EF = BC * m
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (1.5,1);\n'
            '\\coordinate (B) at (3.3,2.2);\n'
            '\\coordinate (C) at (5.4,3.6);\n'
            '\\coordinate (D) at (1.8,0);\n'
            '\\coordinate (E) at (3.96,0);\n'
            '\\coordinate (F) at (6.48,0);\n'
            '\\draw[line width=1pt] (O)--(6,4) (O)--(7.2,0) (A)--(D) (B)--(E) (C)--(F);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[above left] {$B$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (E) circle (1pt) node[below] {$E$};\n'
            '\\fill (F) circle (1pt) node[below] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho góc nhọn $xOy$. Trên tia $Ox$ lấy ba điểm $A, B, C$ theo thứ tự đó sao cho $OA = %s\\text{ cm}$, $AB = %s\\text{ cm}$, $BC = %s\\text{ cm}$. '
            'Trên tia $Oy$ lấy điểm $D$ sao cho $OD = %s\\text{ cm}$. Qua $B$ và $C$ lần lượt kẻ các đường thẳng song song với $AD$ cắt tia $Oy$ tại $E$ và $F$.\\\n'
            'a) Chứng minh $\\Delta OAD \\backsim \\Delta OBE$ và $\\Delta OBE \\backsim \\Delta OCF$.\\\n'
            'b) Tính độ dài các đoạn thẳng $DE$ và $EF$.\\\n%s'
            % (OA, AB, BC, OD, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Xét $\\Delta OBE$ có $AD // BE$ ($A \\in OB$, $D \\in OE$) nên $\\Delta OAD \\backsim \\Delta OBE$.\\\n'
            'Xét $\\Delta OCF$ có $BE // CF$ ($B \\in OC$, $E \\in OF$) nên $\\Delta OBE \\backsim \\Delta OCF$.\n'
            '\\item Ta có $OB = OA + AB = %s + %s = %s\\text{ (cm)}$ và $OC = OB + BC = %s + %s = %s\\text{ (cm)}$.\\\n'
            '- Vì $\\Delta OAD \\backsim \\Delta OBE$ nên $\\dfrac{OD}{OE} = \\dfrac{OA}{OB} \\Rightarrow \\dfrac{%s}{OE} = \\dfrac{%s}{%s} \\Rightarrow OE = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\n'
            'Suy ra $DE = OE - OD = %s - %s = %s\\text{ (cm)}$.\\\n'
            '- Vì $\\Delta OBE \\backsim \\Delta OCF$ nên $\\dfrac{OE}{OF} = \\dfrac{OB}{OC} \\Rightarrow \\dfrac{%s}{OF} = \\dfrac{%s}{%s} \\Rightarrow OF = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\n'
            'Suy ra $EF = OF - OE = %s - %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (OA, AB, OA + AB, OA + AB, BC, OA + AB + BC,
               OD, OA, OA + AB, OD, OA + AB, OA, OD + DE,
               OD + DE, OD, DE,
               OD + DE, OA + AB, OA + AB + BC, OD + DE, OA + AB + BC, OA + AB, OD + DE + EF,
               OD + DE + EF, OD + DE, EF)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
