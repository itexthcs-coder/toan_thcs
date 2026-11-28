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


def bt_dang9_p4_b1_c9_hh8(self):
    # Dạng 9: Chứng minh đẳng thức tổng tỉ số đồng dạng từ một điểm trong tam giác
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        BC = random.choice([12, 15, 18])
        d1 = BC // 2
        d2 = BC * 2 // 3
        d3 = BC * 5 // 6
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (6,0);\n'
            '\\coordinate (A) at (2.2,4.2);\n'
            '\\coordinate (O) at (2.6,1.6);\n'
            '\\coordinate (M) at ($(A)!0.62!(B)$);\n'
            '\\coordinate (N) at ($(A)!0.62!(C)$);\n'
            '\\coordinate (P) at ($(B)!0.38!(A)$);\n'
            '\\coordinate (Q) at ($(B)!0.38!(C)$);\n'
            '\\coordinate (E) at ($(C)!0.42!(A)$);\n'
            '\\coordinate (F) at ($(C)!0.42!(B)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (P)--(Q) (E)--(F);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (P) circle (1pt) node[above left] {$P$};\n'
            '\\fill (Q) circle (1pt) node[below] {$Q$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\fill (F) circle (1pt) node[below] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho $\\Delta ABC$ có $BC = %s\\text{ cm}$. Từ một điểm $O$ nằm trong tam giác kẻ các đường thẳng song song với $BC$, $AC$, $AB$ '
            'lần lượt cắt $AB, AC$ tại $M, N$; cắt $BA, BC$ tại $P, Q$; cắt $CA, CB$ tại $E, F$.\\\n'
            'a) Chứng minh rằng tổng tỉ số đồng dạng của ba tam giác $\\Delta AMN$, $\\Delta PBQ$, $\\Delta EFC$ với $\\Delta ABC$ luôn bằng $2$.\\\n'
            'b) Biết $MN = %s\\text{ cm}$ và $BQ = %s\\text{ cm}$, hãy tính độ dài đoạn thẳng $FC$.\\\n%s'
            % (BC, d1, d2, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $MN // BC$, $PQ // AC$, $EF // AB$ nên các tứ giác $BMOF$ và $CNOQ$ là các hình bình hành, suy ra $BF = MO$ và $QC = ON$.\\\n'
            'Theo định lí về hai tam giác đồng dạng, ta có:\\\n'
            '- $MN // BC \\Rightarrow \\Delta AMN \\backsim \\Delta ABC$ với tỉ số đồng dạng $k_1 = \\dfrac{MN}{BC} = \\dfrac{MO + ON}{BC}$.\\\n'
            '- $PQ // AC \\Rightarrow \\Delta PBQ \\backsim \\Delta ABC$ với tỉ số đồng dạng $k_2 = \\dfrac{BQ}{BC}$.\\\n'
            '- $EF // AB \\Rightarrow \\Delta EFC \\backsim \\Delta ABC$ với tỉ số đồng dạng $k_3 = \\dfrac{FC}{BC}$.\\\n'
            'Cộng vế theo vế ba tỉ số đồng dạng trên, ta được:\\\n'
            '$k_1 + k_2 + k_3 = \\dfrac{MO + ON + BQ + FC}{BC} = \\dfrac{(BF + FC) + (BQ + QC)}{BC} = \\dfrac{BC + BC}{BC} = 2$.\n'
            '\\item Theo câu a, ta có $k_1 + k_2 + k_3 = 2$, suy ra $\\dfrac{MN}{BC} + \\dfrac{BQ}{BC} + \\dfrac{FC}{BC} = 2 \\Rightarrow MN + BQ + FC = 2BC$.\\\n'
            'Thay $BC = %s\\text{ cm}$, $MN = %s\\text{ cm}$, $BQ = %s\\text{ cm}$ ta được:\\\n'
            '$%s + %s + FC = 2 \\cdot %s = %s \\Rightarrow FC = %s - %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (BC, d1, d2, d1, d2, BC, 2*BC, 2*BC, d1 + d2, d3)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
