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


def bt_dang10_p3_b3_c7_ds8(self):
    # Dạng 10: Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số từ đồ thị gồm hữu hạn điểm
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        xs = [-2, 0, 2, 3]
        ys = random.sample(range(-3, 5), 4)
        y1, y2, y3, y4 = ys[0], ys[1], ys[2], ys[3]
        M = max(ys)
        m = min(ys)
        p = random.randint(2, 4)
        q = random.randint(2, 4)
        kq = p * M - q * m
        kq_str = str(kq)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.55, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (-3,0) -- (4.2,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-4) -- (0,5.2) node[left] {$y$};
\\fill (0,0) circle (1pt) node[below left] {$O$};
\\draw[line width=1pt, dashed] (%s,0) -- (%s,%s) -- (0,%s);
\\draw[line width=1pt, dashed] (%s,0) -- (%s,%s) -- (0,%s);
\\draw[line width=1pt, dashed] (%s,0) -- (%s,%s) -- (0,%s);
\\fill (%s,%s) circle (1pt) node[above left] {$A$};
\\fill (%s,%s) circle (1pt) node[right] {$B$};
\\fill (%s,%s) circle (1pt) node[above right] {$C$};
\\fill (%s,%s) circle (1pt) node[right] {$D$};
\\end{tikzpicture}
\\end{center}''' % (xs[0], xs[0], y1, y1,
                      xs[2], xs[2], y3, y3,
                      xs[3], xs[3], y4, y4,
                      xs[0], y1, xs[1], y2, xs[2], y3, xs[3], y4))

        noidungcauhoi = ('''Đồ thị của hàm số $y = f(x)$ gồm đúng $4$ điểm là $A(%s;\\, %s)$, $B(%s;\\, %s)$, $C(%s;\\, %s)$ và $D(%s;\\, %s)$ (minh họa như hình vẽ). Gọi $M$ là giá trị lớn nhất và $m$ là giá trị nhỏ nhất của hàm số đã cho. Tính giá trị của biểu thức $T = %sM - %sm$.
%s'''
                         % (xs[0], y1, xs[1], y2, xs[2], y3, xs[3], y4, p, q, tikz_code))

        loigiai = ('''Vì đồ thị của hàm số $y = f(x)$ gồm $4$ điểm $A(%s;\\, %s)$, $B(%s;\\, %s)$, $C(%s;\\, %s)$ và $D(%s;\\, %s)$ nên tập hợp các giá trị của hàm số là tung độ của các điểm đó: $\\{%s; %s; %s; %s\\}$. \\\\
Trong các giá trị trên, giá trị lớn nhất là $M = %s$ và giá trị nhỏ nhất là $m = %s$. \\\\
Vậy $T = %sM - %sm = %s \\cdot (%s) - %s \\cdot (%s) = %s$.'''
                   % (xs[0], y1, xs[1], y2, xs[2], y3, xs[3], y4,
                      y1, y2, y3, y4,
                      M, m, p, q, p, M, q, m, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
