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


def bt_dang1_p3_b3_c7_ds8(self):
    # Dạng 1: Tìm tham số từ bảng giá trị để đại lượng y không phải là hàm số của x
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        xs = random.sample(range(-8, 12), 3)
        xs.sort()
        x1, x2, x3 = xs[0], xs[1], xs[2]
        ys = random.sample(range(-9, 15), 4)
        y1, y2, y3, y4 = ys[0], ys[1], ys[2], ys[3]
        c = random.choice([i for i in range(-5, 6) if i != 0])

        m1 = x1 - c
        m2 = x2 - c
        m3 = x3 - c
        tong_m = m1 + m2 + m3

        dau_c = '+' if c > 0 else '-'
        abs_c = abs(c)
        bieu_thuc_x = 'm %s %s' % (dau_c, abs_c)

        kq_str = str(tong_m)

        noidungcauhoi = ('''Cho bảng giá trị tương ứng của hai đại lượng $x$ và $y$ như sau:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
$x$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
$y$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Tìm tổng tất cả các giá trị nguyên của $m$ sao cho $y$ không phải là một hàm số của $x$.'''
                         % (x1, bieu_thuc_x, x2, x3,
                            y1, y2, y3, y4))

        loigiai = ('''Theo định nghĩa hàm số, đại lượng $y$ là hàm số của đại lượng thay đổi $x$ nếu với mỗi giá trị của $x$ ta luôn xác định được chỉ một giá trị tương ứng của $y$. \\\\
Quan sát bảng giá trị đã cho, các giá trị $y$ tương ứng đều đôi một khác nhau ($%s; %s; %s; %s$). \\\\
Do đó, để $y$ không phải là một hàm số của $x$ thì giá trị $%s$ phải trùng với một trong ba giá trị $%s; %s; %s$ (khi đó một giá trị của $x$ sẽ cho hai giá trị khác nhau của $y$). \\\\
Ta xét ba trường hợp sau: \\\\
- Trường hợp 1: $%s = %s \\Leftrightarrow m = %s$. \\\\
- Trường hợp 2: $%s = %s \\Leftrightarrow m = %s$. \\\\
- Trường hợp 3: $%s = %s \\Leftrightarrow m = %s$. \\\\
Vậy tổng tất cả các giá trị nguyên của $m$ thỏa mãn yêu cầu bài toán là: $%s + (%s) + (%s) = %s$.'''
                   % (y1, y2, y3, y4,
                      bieu_thuc_x, x1, x2, x3,
                      bieu_thuc_x, x1, m1,
                      bieu_thuc_x, x2, m2,
                      bieu_thuc_x, x3, m3,
                      m1, m2, m3, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
