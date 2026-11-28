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
from mpl_toolkits.mplot3d import Axes3D

def fmt_so(val):
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val < 0:
            return '-\\frac{%s}{%s}' % (abs(val.numerator), val.denominator)
        return '\\frac{%s}{%s}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        s = ('%g' % val).replace('.', ',')
        return s
    return str(val)

def fmt_dt(a, b):
    if a == 1:
        sa = 'x'
    elif a == -1:
        sa = '-x'
    else:
        sa = '%sx' % fmt_so(a)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_so(b))
    else:
        return '%s - %s' % (sa, fmt_so(abs(b)))

def bt_dang7_p4_b5_c7_ds8(self):
    # Dạng 7: So sánh góc tạo bởi các đường thẳng với trục Ox
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([2, 3, 4])
        a2 = random.choice([2, 3, 4])
        a3 = random.choice([-2, -3, -4])
        b1 = random.choice([1, 2])
        b2 = random.choice([-1, -2])
        b3 = random.choice([3, 4])
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-1.5) -- (0,3.5) node[left] {$y$};\n'
            '\\draw[line width=1pt] (-2.8,-0.4) -- (2.8,2.4) node[right] {$(d_1)$};\n'
            '\\draw[line width=1pt] (-0.5,-1.5) -- (1.8,3.1) node[right] {$(d_2)$};\n'
            '\\draw[line width=1pt] (-0.2,3.2) -- (2.5,-0.8) node[right] {$(d_3)$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Cho ba đường thẳng $(d_1): y = \\frac{1}{%s}x + %s$; $(d_2): y = %sx - %s$ và $(d_3): y = %sx + %s$. Gọi $\\alpha_1, \\alpha_2, \\alpha_3$ lần lượt là các góc tạo bởi $(d_1), (d_2), (d_3)$ với trục $Ox$. Không dùng thước đo góc, hãy sắp xếp $\\alpha_1, \\alpha_2, \\alpha_3$ theo thứ tự tăng dần và giải thích chi tiết dựa vào tính chất hệ số góc.'
            % (p, b1, a2, abs(b2), a3, b3)
        )
        
        loigiai = (
            'Ta xét hệ số góc của từng đường thẳng:\\\n'
            '- Đường thẳng $(d_1)$ có hệ số góc $a_1 = \\frac{1}{%s} > 0$ nên góc $\\alpha_1$ tạo bởi $(d_1)$ và trục $Ox$ là góc nhọn ($0^\\circ < \\alpha_1 < 90^\\circ$).\\\n'
            '- Đường thẳng $(d_2)$ có hệ số góc $a_2 = %s > 0$ nên góc $\\alpha_2$ tạo bởi $(d_2)$ và trục $Ox$ cũng là góc nhọn ($0^\\circ < \\alpha_2 < 90^\\circ$).\\\n'
            '- Đường thẳng $(d_3)$ có hệ số góc $a_3 = %s < 0$ nên góc $\\alpha_3$ tạo bởi $(d_3)$ và trục $Ox$ là góc tù ($90^\\circ < \\alpha_3 < 180^\\circ$).\\\n'
            'Khi hai đường thẳng cùng có hệ số góc dương, đường thẳng nào có hệ số góc lớn hơn thì độ dốc đi lên lớn hơn, do đó góc tạo bởi đường thẳng đó với trục $Ox$ lớn hơn. Vì $0 < \\frac{1}{%s} < %s$ nên $\\alpha_1 < \\alpha_2 < 90^\\circ$.\\\n'
            'Mặt khác, $\\alpha_3$ là góc tù nên $\\alpha_3 > 90^\\circ$.\\\n'
            'Vậy thứ tự tăng dần của các góc là: $\\alpha_1 < \\alpha_2 < \\alpha_3$.%s'
            % (p, a2, a3, p, a2, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
