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


def bt_dang18_p4_b4_c2_ds8(self):
    y = symbols('y')
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        w_duong = random.choice([2, 3])
        x_val = random.randint(28, 42)
        y_val = random.randint(18, 26)
        kq = (x_val - w_duong) * (y_val - w_duong)
        
        tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) rectangle (4.0,2.6);
    \\draw[line width=1pt] (1.7,0) -- (1.7,2.6) (2.1,0) -- (2.1,2.6);
    \\draw[line width=1pt] (0,1.1) -- (4.0,1.1) (0,1.5) -- (4.0,1.5);
    \\draw[line width=1pt, <->] (0,2.85) -- (4.0,2.85) node[midway, above] {$x$};
    \\draw[line width=1pt, <->] (-0.25,0) -- (-0.25,2.6) node[midway, left] {$y$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Bác An có một khu đất hình chữ nhật có chiều dài $x\\text{ (m)}$ và chiều rộng $y\\text{ (m)}$ ($x > y > %s$). Bác dự định làm một lối đi rộng $%s\\text{ m}$ chạy dọc theo chiều dài và một lối đi rộng $%s\\text{ m}$ chạy ngang theo chiều rộng chia khu đất thành $4$ mảnh vườn nhỏ để trồng các loại cây ăn quả khác nhau. \\
a) Viết biểu thức biểu thị tổng diện tích $S$ của phần đất trồng cây ăn quả (không tính diện tích hai lối đi) theo $x$ và $y$, sau đó phân tích $S$ thành nhân tử. \\\\
b) Tính tổng diện tích đất trồng cây ăn quả khi $x = %s\\text{ m}$ và $y = %s\\text{ m}$.'''
                         % (2*w_duong, w_duong, w_duong, x_val, y_val) + tikz_hinh)
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích cả khu đất hình chữ nhật ban đầu là $xy\\text{ (m}^2\\text{)}$.\\\\
Diện tích lối đi chạy dọc chiều dài là $%sx\\text{ (m}^2\\text{)}$, diện tích lối đi chạy ngang chiều rộng là $%sy\\text{ (m}^2\\text{)}$ và phần giao nhau của hai lối đi là hình vuông diện tích $%s^2 = %s\\text{ (m}^2\\text{)}$.\\\\
Tổng diện tích phần đất trồng cây ăn quả là:
\\begin{align*}
S &= xy - %sx - %sy + %s \\\\
&= (xy - %sx) - (%sy - %s) \\\\
&= x(y - %s) - %s(y - %s) \\\\
&= (x - %s)(y - %s)\\text{ (m}^2\\text{)}.
\\end{align*}
\\item Thay $x = %s\\text{ m}$ và $y = %s\\text{ m}$ vào biểu thức trên, ta được:
\\begin{align*}
S = (%s - %s)(%s - %s) = %s \\cdot %s = %s\\text{ (m}^2\\text{)}.
\\end{align*}
\\end{enumEX}''' % (w_duong, w_duong, w_duong, w_duong**2,
                      w_duong, w_duong, w_duong**2,
                      w_duong, w_duong, w_duong**2,
                      w_duong, w_duong, w_duong,
                      w_duong, w_duong,
                      x_val, y_val, x_val, w_duong, y_val, w_duong,
                      x_val - w_duong, y_val - w_duong, kq))

    # Xuất câu hỏi và lời giải tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
