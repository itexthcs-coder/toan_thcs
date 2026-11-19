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

def bt_dang2_p3_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('M', 'N', 'P'), ('A', 'B', 'C'), ('D', 'E', 'F')]
        M, N, P = random.choice(bo_diem)
        k = randint(2, 6) # R + r = k*sqrt(3) -> a = 2k -> S = 4k^2*sqrt(3)/4 = k^2*sqrt(3) <= 36*1.732 = 62.4 (4 ky tu!)
        a = 2 * k
        S_val = Rational(a**2, 4) * sqrt(3)
        number = Decimal(str(float(S_val)))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (G) at (0,0);
\\coordinate (M) at (90:1.6);
\\coordinate (N) at (210:1.6);
\\coordinate (P) at (-30:1.6);
\\draw[line width=1pt] (G) circle (1.6);
\\draw[line width=1pt] (G) circle (0.8);
\\draw[line width=1pt] (M)--(N)--(P)--cycle;
\\fill (G) circle (1pt) node[below] {$G$};
\\fill (M) circle (1pt) node[above] {$%s$};
\\fill (N) circle (1pt) node[below left] {$%s$};
\\fill (P) circle (1pt) node[below right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (M, N, P))

        noidungcauhoi = ('''Cho tam giác đều $%s%s%s$ có tổng bán kính đường tròn ngoại tiếp và bán kính đường tròn nội tiếp bằng $%s\\sqrt{3}\\text{ cm}$. Diện tích của tam giác $%s%s%s$ bằng bao nhiêu $\\text{cm}^2$ (làm tròn kết quả đến hàng phần mười)?%s'''
                         % (M, N, P, k, M, N, P, hinh_ve))

        loigiai = ('''Gọi $a$ là độ dài cạnh của tam giác đều $%s%s%s$.\\\\
Ta có $R = \\frac{\\sqrt{3}}{3}a$ và $r = \\frac{\\sqrt{3}}{6}a$.\\\\
Theo đề bài, $R + r = %s\\sqrt{3}$ nên:
$$\\frac{\\sqrt{3}}{3}a + \\frac{\\sqrt{3}}{6}a = %s\\sqrt{3} \\Leftrightarrow \\frac{\\sqrt{3}}{2}a = %s\\sqrt{3} \\Leftrightarrow a = %s\\text{ (cm)}.$$
Diện tích tam giác đều $%s%s%s$ là:
$$S = \\frac{a^2\\sqrt{3}}{4} = \\frac{%s^2\\sqrt{3}}{4} = %s \\approx %s\\text{ (cm}^2).$$'''
                   % (M, N, P, k, k, k, a, M, N, P, a, latex(S_val), str(kq_str)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
