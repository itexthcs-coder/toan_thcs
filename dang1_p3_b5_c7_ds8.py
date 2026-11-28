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


def bt_dang1_p3_b5_c7_ds8(self):
    # Dang 1: Tim tung do giao diem voi truc Oy cua duong thang song song voi duong thang cho truoc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3, 4])
        m_val = random.choice([i for i in range(-6, 7) if i != 0 and i != 1])
        a_val = k * m_val - 1
        c_val = random.choice([i for i in range(-8, 9) if i != 0])
        b1_const = random.choice([i for i in range(-10, 11) if i != 0])
        b_res = c_val * m_val + b1_const
        b2_val = random.choice([i for i in range(-10, 11) if i != b_res])
        
        sign_b1 = '+' if b1_const > 0 else '-'
        abs_b1 = abs(b1_const)
        sign_b2 = '+' if b2_val > 0 else '-'
        abs_b2 = abs(b2_val)
        
        d_str = 'y = (%sm - 1)x + %sm %s %s' % (k, c_val, sign_b1, abs_b1)
        dp_str = 'y = %sx %s %s' % (a_val, sign_b2, abs_b2)
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,4) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-2,-1) -- (2,3) node[right] {$(d)$};\n'
            '\\draw[line width=1pt, dashed] (-2.5,0.5) -- (1.5,4.5) node[above] {$(d\')$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,1) circle (1pt) node[right] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho đường thẳng $(d): %s$ song song với đường thẳng $(d\'): %s$. '
            'Tính tung độ giao điểm của đường thẳng $(d)$ với trục tung $Oy$.\n%s'
            % (d_str, dp_str, tikz)
        )
        
        loigiai = (
            'Đường thẳng $(d)$ có hệ số góc là $a = %sm - 1$ và tung độ gốc là $b = %sm %s %s$.\\ '
            'Đường thẳng $(d\')$ có hệ số góc là $a\' = %s$ và tung độ gốc là $b\' = %s$.\\ '
            'Vì đường thẳng $(d) // (d\')$ nên ta có điều kiện: $a = a\'$ và $b \\neq b\'$.\\ '
            'Suy ra: $%sm - 1 = %s \\Leftrightarrow %sm = %s \\Leftrightarrow m = %s$.\\ '
            'Thay $m = %s$ vào biểu thức của $b$, ta được: $b = %s \\cdot (%s) %s %s = %s \\neq %s$ (thỏa mãn).\\ '
            'Vậy tung độ giao điểm của đường thẳng $(d)$ với trục tung $Oy$ là $%s$.'
            % (k, c_val, sign_b1, abs_b1, a_val, b2_val, k, a_val, k, a_val + 1, m_val, m_val, c_val, m_val, sign_b1, abs_b1, b_res, b2_val, b_res)
        )
        
        dapan = '\\shortans[0]{$%s$}\n' % b_res

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
