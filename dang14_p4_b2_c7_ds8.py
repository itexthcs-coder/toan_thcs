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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang14_p4_b2_c7_ds8(self):
    # Dạng 14: Giải bài toán bằng cách lập phương trình - Hình học tam giác vuông
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Bộ ba Pythagore cơ bản nhân hệ số
        triples = [
            (3, 4, 5, 2),   # 6, 8, 10 -> P = 24
            (3, 4, 5, 3),   # 9, 12, 15 -> P = 36
            (3, 4, 5, 4),   # 12, 16, 20 -> P = 48
            (5, 12, 13, 2), # 10, 24, 26 -> P = 60
            (8, 15, 17, 1)  # 8, 15, 17 -> P = 40
        ]
        a0, b0, c0, scale = random.choice(triples)
        ab = a0 * scale
        ac = b0 * scale
        bc = c0 * scale
        chu_vi = ab + ac + bc
        d1 = ac - ab
        d2 = bc - ac
        
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,2.5);
\\coordinate (C) at (4,0);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[above left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\end{tikzpicture}
\\end{center}''')
        
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có chu vi bằng $%s\\text{ cm}$. Biết độ dài cạnh huyền $BC$ dài hơn cạnh góc vuông $AC$ là $%s\\text{ cm}$ và cạnh góc vuông $AC$ dài hơn cạnh góc vuông $AB$ là $%s\\text{ cm}$. Tính độ dài ba cạnh của tam giác $ABC$.'''
                         % (chu_vi, d2, d1))
        
        loigiai = ('''%s \\\\
Gọi độ dài cạnh góc vuông $AB$ là $x\\text{ (cm)}$ (điều kiện: $x > 0$). \\\\
Vì cạnh $AC$ dài hơn cạnh $AB$ là $%s\\text{ cm}$ nên độ dài cạnh $AC$ là $x + %s\\text{ (cm)}$. \\\\
Vì cạnh huyền $BC$ dài hơn cạnh $AC$ là $%s\\text{ cm}$ nên độ dài cạnh $BC$ là $x + %s + %s = x + %s\\text{ (cm)}$. \\\\
Theo đề bài, chu vi tam giác $ABC$ bằng $%s\\text{ cm}$ nên ta có phương trình: \\\\
$x + (x + %s) + (x + %s) = %s$ \\\\
$\\Leftrightarrow 3x + %s = %s$ \\\\
$\\Leftrightarrow 3x = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy độ dài ba cạnh của tam giác $ABC$ lần lượt là: $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$ và $BC = %s\\text{ cm}$.'''
                   % (hinh_ve, d1, d1, d2, d1, d2, d1 + d2,
                      chu_vi,
                      d1, d1 + d2, chu_vi,
                      2 * d1 + d2, chu_vi,
                      chu_vi - (2 * d1 + d2), ab,
                      ab, ac, bc))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
