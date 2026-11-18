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


def bt_dang19_p3_b4_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        L = random.choice([26, 30, 34, 40])
        W = random.choice([18, 20, 22, 24])
        x_ans = random.choice([3, 4, 5])
        S_bia = L * W
        S_day = (L - 2 * x_ans) * (W - 2 * x_ans)
        b_p = (L + W) // 2
        c_s = (S_bia - S_day) // 4
        delta_p = b_p**2 - 4 * c_s
        sqrt_dp = int(math.isqrt(delta_p))
        x1 = (b_p - sqrt_dp) // 2
        x2 = (b_p + sqrt_dp) // 2

        tikz = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3);
    \\coordinate (B) at (4.5,3);
    \\coordinate (C) at (4.5,0);
    \\coordinate (D) at (0,0);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt, dashed] (0.6,3)--(0.6,2.4)--(0,2.4);
    \\draw[line width=1pt, dashed] (3.9,3)--(3.9,2.4)--(4.5,2.4);
    \\draw[line width=1pt, dashed] (0.6,0)--(0.6,0.6)--(0,0.6);
    \\draw[line width=1pt, dashed] (3.9,0)--(3.9,0.6)--(4.5,0.6);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\node[above] at (0.3,3) {$x$};
    \\node[left] at (0,2.7) {$x$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Từ một tấm bìa hình chữ nhật có chiều dài $%s\\text{ cm}$ và chiều rộng $%s\\text{ cm}$, người ta cắt bỏ ở bốn góc bốn hình vuông bằng nhau có cạnh $x$ (cm), rồi gấp phần còn lại thành một chiếc hộp chữ nhật không nắp có diện tích đáy bằng $%s\\text{ cm}^2$. Tính độ dài cạnh hình vuông bị cắt bỏ (đơn vị: cm).'''
                         % (str(L), str(W), str(S_day)))

        loigiai = ('''%s\\\\
                   Điều kiện của cạnh hình vuông bị cắt bỏ là $0 < x < %s$.\\\\
                   Sau khi cắt bỏ bốn góc, đáy chiếc hộp là hình chữ nhật có chiều dài là $%s - 2x$ (cm) và chiều rộng là $%s - 2x$ (cm).\\\\
                   Vì diện tích đáy hộp bằng $%s\\text{ cm}^2$ nên ta có phương trình:\\\\
                   $(%s - 2x)(%s - 2x) = %s$\\\\
                   $4x^2 - %sx + %s = %s$\\\\
                   $4x^2 - %sx + %s = 0$ hay $x^2 - %sx + %s = 0$.\\\\
                   Ta có: $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot %s = %s$; $\\sqrt{\\Delta} = %s$.\\\\
                   Suy ra phương trình có hai nghiệm phân biệt:\\\\
                   $x_1 = \\dfrac{%s - %s}{2} = %s$ (thỏa mãn điều kiện); $x_2 = \\dfrac{%s + %s}{2} = %s$ (loại vì $%s > %s$).\\\\
                   Vậy độ dài cạnh hình vuông bị cắt bỏ là $%s\\text{ cm}$.'''
                   % (tikz, str(W // 2), str(L), str(W), str(S_day),
                      str(L), str(W), str(S_day),
                      str(2 * (L + W)), str(S_bia), str(S_day),
                      str(2 * (L + W)), str(S_bia - S_day), str(b_p), str(c_s),
                      str(b_p), str(c_s), str(delta_p), str(sqrt_dp),
                      str(b_p), str(sqrt_dp), str(x1), str(b_p), str(sqrt_dp), str(x2), str(x2), str(W // 2), str(x_ans)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(x_ans))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
