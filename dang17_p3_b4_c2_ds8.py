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


def bt_dang17_p3_b4_c2_ds8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x_val = random.randint(28, 42)
        y_val = random.randint(18, 26)
        z_val = random.randint(2, 5)
        kq = x_val * y_val - 4 * (z_val**2)
        kq_str = str(kq)
        
        tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) rectangle (4.0,2.6);
    \\draw[line width=1pt, dashed] (0,2.1) rectangle (0.5,2.6);
    \\draw[line width=1pt, dashed] (3.5,2.1) rectangle (4.0,2.6);
    \\draw[line width=1pt, dashed] (0,0) rectangle (0.5,0.5);
    \\draw[line width=1pt, dashed] (3.5,0) rectangle (4.0,0.5);
    \\draw[line width=1pt, <->] (0,2.85) -- (4.0,2.85) node[midway, above] {$x$};
    \\draw[line width=1pt, <->] (-0.25,0) -- (-0.25,2.6) node[midway, left] {$y$};
    \\node at (0.25,2.35) {$z$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Từ một tấm tôn hình chữ nhật có chiều dài $x\\text{ (cm)}$ và chiều rộng $y\\text{ (cm)}$, người thợ cơ khí cắt bỏ đi bốn hình vuông ở bốn góc, mỗi hình vuông có cạnh bằng $z\\text{ (cm)}$ để gập thành một chiếc khay không nắp. Biết $x = %s\\text{ cm}$, $y = %s\\text{ cm}$ và $z = %s\\text{ cm}$. Tính diện tích phần tôn còn lại làm chiếc khay (đơn vị: $\\text{cm}^2$).'''
                         % (x_val, y_val, z_val) + tikz_hinh)
        
        loigiai = ('''Diện tích tấm tôn hình chữ nhật ban đầu là $xy\\text{ (cm}^2\\text{)}$.\\\\
Diện tích bốn hình vuông bị cắt bỏ ở bốn góc là $4z^2\\text{ (cm}^2\\text{)}$.\\\\
Biểu thức tính diện tích phần tôn còn lại là:
\\begin{align*}
S = xy - 4z^2 = xy - (2z)^2.
\\end{align*}
Thay $x = %s\\text{ cm}$, $y = %s\\text{ cm}$ và $z = %s\\text{ cm}$ vào biểu thức trên, ta được:
\\begin{align*}
S = %s \\cdot %s - 4 \\cdot %s^2 = %s - %s = %s\\text{ (cm}^2\\text{)}.
\\end{align*}''' % (x_val, y_val, z_val, x_val, y_val, z_val, x_val * y_val, 4 * (z_val**2), kq_str))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
