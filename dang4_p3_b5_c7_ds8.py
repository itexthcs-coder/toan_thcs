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


def bt_dang4_p3_b5_c7_ds8(self):
    # Dang 4: Tim tham so de ba duong thang dong quy tai mot diem
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x0 = random.choice([2, 3, 4])
        y0 = random.choice([3, 4, 5, 6])
        b1 = y0 - x0
        b2 = y0 - 2 * x0
        
        a3_target = random.choice([3, 4, 5])
        m_res = a3_target + 1
        b3 = y0 - a3_target * x0
        
        s_b1 = '+' if b1 >= 0 else '-'
        s_b2 = '+' if b2 >= 0 else '-'
        s_b3 = '+' if b3 >= 0 else '-'
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-1.5,-0.5) -- (3,2.5) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-0.5,-1.5) -- (2.5,3) node[above] {$(d_2)$};\n'
            '\\draw[line width=1pt, dashed] (-1,2.5) -- (2.5,0.5) node[right] {$(d_3)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (1.2,1.3) circle (1pt) node[above left] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho ba đường thẳng $(d_1): y = x %s %s$, $(d_2): y = 2x %s %s$ và $(d_3): y = (m - 1)x %s %s$. '
            'Tìm giá trị của $m$ để ba đường thẳng đã cho đồng quy tại một điểm.\n%s'
            % (s_b1, abs(b1), s_b2, abs(b2), s_b3, abs(b3), tikz)
        )
        
        loigiai = (
            'Hoành độ giao điểm của $(d_1)$ và $(d_2)$ là nghiệm của phương trình: $x %s %s = 2x %s %s \\Leftrightarrow x = %s$.\\ '
            'Thay $x = %s$ vào phương trình đường thẳng $(d_1)$, ta được: $y = %s %s %s = %s$.\\ '
            'Suy ra giao điểm của $(d_1)$ và $(d_2)$ là điểm $M(%s; %s)$.\\ '
            'Để ba đường thẳng đồng quy thì đường thẳng $(d_3)$ phải đi qua điểm $M(%s; %s)$ (với điều kiện $m - 1 \\neq 1$ và $m - 1 \\neq 2$).\\ '
            'Thay $x = %s, y = %s$ vào phương trình của $(d_3)$, ta có: $%s = (m - 1) \\cdot %s %s %s \\Leftrightarrow %s(m - 1) = %s \\Leftrightarrow m - 1 = %s \\Leftrightarrow m = %s$ (thỏa mãn).\\ '
            'Vậy giá trị cần tìm là $m = %s$.'
            % (s_b1, abs(b1), s_b2, abs(b2), x0, x0, x0, s_b1, abs(b1), y0, x0, y0, x0, y0, x0, y0, y0, x0, s_b3, abs(b3), x0, a3_target * x0, a3_target, m_res, m_res)
        )
        
        dapan = '\\shortans[0]{$%s$}\n' % m_res

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
