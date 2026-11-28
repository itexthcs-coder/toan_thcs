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

def bt_dang18_p4_b5_c7_ds8(self):
    # Dạng 18: Bài toán thực tế về độ dốc mái nhà (đối xứng và song song)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = random.choice([0.5, 0.6, 0.75, 0.8])
        b1 = random.choice([3, 4])
        b_xa = b1 - random.choice([0.4, 0.5, 0.6])
        a1_str = fmt_so(a1)
        a2_str = fmt_so(-a1)
        b_xa_str = fmt_so(b_xa)
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$ (m)};\n'
            '\\draw[->, line width=1pt] (0,-0.5) -- (0,3.5) node[left] {$y$ (m)};\n'
            '\\draw[line width=1pt] (-3,0.9) -- (0,2.7) node[above right] {$I$};\n'
            '\\draw[line width=1pt] (0,2.7) -- (3,0.9) node[right] {$(d_2)$};\n'
            '\\draw[line width=1pt, dashed] (-3,0.3) -- (0,2.1) node[below right] {$K$};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (0,2.7) circle (1pt);\n'
            '\\fill (0,2.1) circle (1pt);\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Trong thiết kế xây dựng, độ dốc của mái nhà được mô phỏng bởi hệ số góc của đường thẳng biểu diễn mặt cắt mái nhà trong hệ trục tọa độ $Oxy$ (đơn vị trên mỗi trục là mét). Một ngôi nhà có mặt cắt mái bên trái nằm trên đường thẳng $(d_1): y = %sx + %s$ và mặt cắt mái bên phải nằm trên đường thẳng $(d_2): y = ax + b$ ($a \\neq 0$).\\\n'
            'a) Biết hai mái nhà đối xứng nhau qua trục tung $Oy$ và gặp nhau tại đỉnh nóc nhà nằm trên trục $Oy$, hãy xác định hệ số góc $a$ và tung độ gốc $b$ của đường thẳng $(d_2)$.\\\n'
            'b) Một thanh xà gồ phụ được lắp đặt bên dưới mái trái, song song với $(d_1)$ và đi qua điểm $K(0; %s)$. Viết phương trình đường thẳng biểu diễn thanh xà gồ này.'
            % (a1_str, b1, b_xa_str)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Đỉnh nóc nhà là giao điểm của $(d_1)$ với trục tung $Oy$ nên có tọa độ là $I(0; %s)$. Vì $(d_2)$ cũng đi qua đỉnh $I(0; %s)$ nên tung độ gốc của $(d_2)$ là $b = %s$.\\\n'
            'Mặt khác, hai mái nhà đối xứng nhau qua trục tung $Oy$ nên góc dốc của hai mái bằng nhau, nhưng mái trái đi lên từ trái sang phải ($a_1 = %s > 0$) còn mái phải đi xuống từ trái sang phải ($a < 0$). Do đó hệ số góc của $(d_2)$ là $a = %s$.\n'
            '\\item Gọi phương trình đường thẳng biểu diễn thanh xà gồ phụ là $y = a\\prime x + b\\prime$ ($a\\prime \\neq 0$).\\\n'
            'Vì thanh xà gồ song song với mái trái $(d_1): y = %sx + %s$ nên $a\\prime = %s$ (với $b\\prime \\neq %s$).\\\n'
            'Vì đường thẳng đi qua điểm $K(0; %s)$ trên trục tung nên $b\\prime = %s$ (thỏa mãn $b\\prime \\neq %s$).\\\n'
            'Vậy phương trình đường thẳng biểu diễn thanh xà gồ là $y = %sx + %s$.%s\n'
            '\\end{enumEX}'
            % (b1, b1, b1, a1_str, a2_str,
               a1_str, b1, a1_str, b1, b_xa_str, b_xa_str, b1, a1_str, b_xa_str, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
