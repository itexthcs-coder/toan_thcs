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

def bt_dang19_p3_b4_c7_ds8(self):
    # Dạng 19 (Ứng dụng thực tế): Chiều cao ngọn nến giảm đều theo thời gian thắp sáng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        h0 = random.choice([20, 24, 25, 28, 30, 32, 36])
        v_num = random.choice([3, 4, 5])
        v_val = Fraction(v_num, 2)
        v_str = str(Decimal(str(float(v_val)))).replace('.', ',') if v_val.denominator != 1 else str(int(v_val))
        t_val = random.choice([2, 4, 6, 8])
        while h0 - v_val * t_val <= 2:
            t_val = random.choice([2, 4, 6])
        h_rem = int(h0 - v_val * t_val)
        kq_str = str(h_rem)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (3.8,0) node[below] {$t\\text{ (giờ)}$};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {$h\\text{ (cm)}$};
\\coordinate (O) at (0,0);
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (3.2,0);
\\draw[line width=1pt] (A) -- (B);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (h0))

        noidungcauhoi = ('''Một cây nến cao $%s\\text{ cm}$ khi bắt đầu thắp sáng. Sau mỗi giờ cháy, chiều cao của cây nến giảm đi đều đặn $%s\\text{ cm}$ (đồ thị biểu diễn chiều cao $h$ theo thời gian $t$ như hình vẽ). Hỏi sau khi thắp sáng được $%s\\text{ giờ}$, chiều cao còn lại của cây nến là bao nhiêu xentimét?%s'''
                         % (h0, v_str, t_val, tikz_code))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

        loigiai = ('''Gọi $t$ (giờ) là thời gian thắp sáng cây nến ($t \\ge 0$) và $h$ (cm) là chiều cao còn lại của cây nến sau $t$ giờ.\\\\
Vì mỗi giờ chiều cao cây nến giảm đi $%s\\text{ cm}$ nên sau $t$ giờ chiều cao giảm đi là $%st\\text{ (cm)}$.\\\\
Công thức hàm số bậc nhất biểu thị chiều cao còn lại $h$ của cây nến theo thời gian $t$ là:\\\\
$h = -%st + %s$.\\\\
Thay $t = %s$ vào công thức trên, ta được:\\\\
$h = -%s \\cdot %s + %s = -%s + %s = %s\\text{ (cm)}$.\\\\
Vậy sau khi thắp sáng được $%s\\text{ giờ}$, chiều cao còn lại của cây nến là $%s\\text{ cm}$.'''
                   % (v_str, v_str,
                      v_str, h0,
                      t_val,
                      v_str, t_val, h0, int(v_val * t_val), h0, kq_str,
                      t_val, kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
