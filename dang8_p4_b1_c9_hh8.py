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


def bt_dang8_p4_b1_c9_hh8(self):
    # Dạng 8: Khai thác cặp tam giác đồng dạng ẩn trong hình bình hành
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        p = random.choice([1, 2])
        q = random.choice([3, 4])
        while math.gcd(p, q) != 1:
            q = random.choice([3, 4])
        
        m_ab = random.choice([3, 4])
        AB = q * m_ab
        AE = p * m_ab
        EB = AB - AE
        
        m_bc = random.choice([2, 3])
        BC = (q - p) * m_bc
        BF = p * m_bc
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (4,0);\n'
            '\\coordinate (D) at (1.2,2.5);\n'
            '\\coordinate (C) at (5.2,2.5);\n'
            '\\coordinate (E) at ($(A)!0.35!(B)$);\n'
            '\\coordinate (F) at (intersection of D--E and C--B);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (D)--(F) (B)--(F);\n'
            '\\fill (A) circle (1pt) node[below left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[above right] {$C$};\n'
            '\\fill (D) circle (1pt) node[above left] {$D$};\n'
            '\\fill (E) circle (1pt) node[below] {$E$};\n'
            '\\fill (F) circle (1pt) node[below right] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho hình bình hành $ABCD$ có $AB = %s\\text{ cm}$, $BC = %s\\text{ cm}$. '
            'Trên cạnh $AB$ lấy điểm $E$ sao cho $AE = %s\\text{ cm}$. Tia $DE$ cắt tia $CB$ tại $F$.\\\n'
            'a) Hãy liệt kê ba cặp tam giác (phân biệt) đồng dạng có trong hình và giải thích.\\\n'
            'b) Tính độ dài đoạn thẳng $BF$.\\\n%s'
            % (AB, BC, AE, tikz)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $ABCD$ là hình bình hành nên $AB // CD$, $AD // BC$ và $AD = BC = %s\\text{ cm}$, $CD = AB = %s\\text{ cm}$.\\\n'
            '- Xét $\\Delta FDC$ có $EB // DC$ ($E \\in DF$, $B \\in CF$) nên $\\Delta FEB \\backsim \\Delta FDC$ (1).\\\n'
            '- Xét $\\Delta FDC$ có đường thẳng $EA$ cắt phần kéo dài của hai cạnh $FD, FC$ tại $E, A$ và $EA // BC$ (vì $AD // BC$) nên $\\Delta EAD \\backsim \\Delta EBF$ (2).\\\n'
            '- Từ (1) và (2), theo tính chất bắc cầu suy ra $\\Delta EAD \\backsim \\Delta FDC$ (3).\\\n'
            'Vậy ba cặp tam giác đồng dạng là: $\\Delta FEB \\backsim \\Delta FDC$, $\\Delta EAD \\backsim \\Delta EBF$ và $\\Delta EAD \\backsim \\Delta FDC$.\n'
            '\\item Ta có $EB = AB - AE = %s - %s = %s\\text{ (cm)}$.\\\n'
            'Vì $\\Delta EAD \\backsim \\Delta EBF$ nên $\\dfrac{BF}{AD} = \\dfrac{EB}{EA}$.\\\n'
            'Suy ra $BF = \\dfrac{EB}{EA} \\cdot AD = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$.\n'
            '\\end{enumEX}'
            % (BC, AB, AB, AE, EB, EB, AE, BC, BF)
        )
        
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n\\end{minipage}\n\n')
    return content
