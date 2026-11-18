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

def bt_dang16_p3_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([
            (24, 25, 5, 4),
            (20, 30, 6, 4),
            (18, 24, 4, 3),
            (25, 30, 6, 5),
            (30, 40, 8, 6)
        ])
        rong, dai, tang_dai, giam_rong = bo_so
        dien_tich = rong * dai
        chu_vi = 2 * (rong + dai)
        kq_str = str(chu_vi)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một bãi đỗ xe ô tô hình chữ nhật có diện tích $%s\\text{ m}^2$. Người ta mở rộng chiều dài thêm $%s\\text{ m}$ và giảm chiều rộng đi $%s\\text{ m}$ để phù hợp với quy hoạch đường giao thông thì diện tích bãi đỗ xe không thay đổi (minh họa như hình vẽ). Tính chu vi ban đầu của bãi đỗ xe đó (đơn vị: mét).
\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) rectangle (4.5,2.8);
\\draw[line width=1pt, dashed] (0,0) rectangle (5.6,2.1);
\\node[above] at (2.25,2.8) {Chiều dài ban đầu};
\\node[left] at (0,1.4) {$x$};
\\draw[<->, line width=1pt] (4.5,1.05) -- (5.6,1.05) node[midway, below] {$+%s\\text{ m}$};
\\draw[<->, line width=1pt] (2.25,2.1) -- (2.25,2.8) node[midway, right] {$-%s\\text{ m}$};
\\end{tikzpicture}
\\end{center}'''
                         %(str(dien_tich), str(tang_dai), str(giam_rong), str(tang_dai), str(giam_rong)
                         ))

        # Nội dung lời giải
        loigiai = ('''Gọi chiều rộng ban đầu của bãi đỗ xe là $x$ ($\\text{m}$, $x > %s$). \\\\
                   Chiều dài ban đầu của bãi đỗ xe là $\\frac{%s}{x}$ ($\\text{m}$). \\\\
                   Sau khi quy hoạch, chiều dài mới là $\\frac{%s}{x} + %s$ ($\\text{m}$) và chiều rộng mới là $x - %s$ ($\\text{m}$). \\\\
                   Vì diện tích bãi đỗ xe không đổi nên ta có phương trình: \\\\
                   $\\left(\\frac{%s}{x} + %s\\right)(x - %s) = %s$ \\\\
                   $\\Leftrightarrow %s - \\frac{%s}{x} + %sx - %s = %s$ \\\\
                   $\\Leftrightarrow %sx^2 - %sx - %s = 0 \\Leftrightarrow x^2 - %sx - %s = 0$. \\\\
                   Giải phương trình trên ta tìm được hai nghiệm $x_1 = %s$ (thỏa mãn điều kiện) và $x_2 = %s$ (loại). \\\\
                   Suy ra chiều rộng ban đầu là $%s\\text{ m}$ và chiều dài ban đầu là $\\frac{%s}{%s} = %s\\text{ m}$. \\\\
                   Chu vi ban đầu của bãi đỗ xe là $2 \\cdot (%s + %s) = %s$ (mét).'''
                   %(str(giam_rong),
                     str(dien_tich),
                     str(dien_tich), str(tang_dai), str(giam_rong),
                     str(dien_tich), str(tang_dai), str(giam_rong), str(dien_tich),
                     str(dien_tich), str(dien_tich * giam_rong), str(tang_dai), str(tang_dai * giam_rong), str(dien_tich),
                     str(tang_dai), str(tang_dai * giam_rong), str(dien_tich * giam_rong), str(giam_rong), str((dien_tich * giam_rong) // tang_dai),
                     str(rong), str(giam_rong - rong),
                     str(rong), str(dien_tich), str(rong), str(dai),
                     str(rong), str(dai), kq_str
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(kq_str)

    # Xuất câu trắc nghiệm trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
