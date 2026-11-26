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
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang2_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        p = randint(2, 4)
        k = randint(3, 12)
        q = p * k + randint(1, p - 1)
        count_m = k

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y=(%sm-%s)x^2$. Có bao nhiêu giá trị nguyên dương của tham số $m$ để đồ thị hàm số nằm phía dưới trục hoành?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3,0) -- (3,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-3.5) -- (0,1.2) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.2:2.2] plot (\\x, {-0.65*(\\x)^2});
\\coordinate (O) at (0,0);
\\fill (O) circle (1pt) node[above left] {$O$};
\\node at (0,-4) {Đồ thị nằm phía dưới trục hoành ($a < 0$)};
\\end{tikzpicture}
\\end{center}'''
                         % (str(p), str(q)))

        # Nội dung lời giải
        loigiai = ('''Hàm số đã cho có dạng $y = ax^2$ với hệ số $a = %sm - %s$. \\\\
Để đồ thị hàm số nằm phía dưới trục hoành thì hệ số $a < 0$, tức là: \\\\
$%sm - %s < 0 \\Leftrightarrow %sm < %s \\Leftrightarrow m < \\dfrac{%s}{%s}$. \\\\
Vì $m$ là số nguyên dương nên $m \\in \\mathbb{N}^*$ và $1 \\le m \\le %s$. \\\\
Bảng liệt kê điều kiện của hệ số $a$: \\\\
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Điều kiện của $m$ & Dấu của hệ số $a = %sm - %s$ & Vị trí đồ thị so với trục $Ox$ \\\\
\\hline
$1 \\le m \\le %s$ & $a < 0$ & Nằm phía dưới trục hoành \\\\
\\hline
$m \\ge %s$ & $a > 0$ & Nằm phía trên trục hoành \\\\
\\hline
\\end{tabular}
\\end{center}
Vậy có tất cả $%s$ giá trị nguyên dương của tham số $m$ thỏa mãn yêu cầu bài toán.'''
                   % (str(p), str(q),
                      str(p), str(q), str(p), str(q), str(q), str(p),
                      str(k),
                      str(p), str(q),
                      str(k),
                      str(k + 1),
                      str(count_m)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(count_m))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
