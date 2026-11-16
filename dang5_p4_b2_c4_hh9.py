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


def bt_dang5_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2, 3])
        ca = 9 * k
        cb = 15 * k
        ch = Rational(ca, 2)
        ah_sym = Rational(ca, 2) * sqrt(3)
        hb = ch + cb
        ab = 21 * k

        ah_val = float(ah_sym)
        hb_val = float(hb)
        deg_b = int(Decimal(str(math.degrees(math.atan(ah_val / hb_val)))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        ck_sym = simplify(ah_sym * cb / ab)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (H) at (0,0);
    \\coordinate (C) at (1.35,0);
    \\coordinate (B) at (4.5,0);
    \\coordinate (A) at (0,2.34);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt, dashed] (A)--(H)--(C);
    \\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
    \\draw[line width=1pt] (1.85,0) arc (0:120:0.5);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (H) circle (1pt) node[below left] {$H$};
    \\node[above right] at (0.68,1.17) {$%s\\text{ cm}$};
    \\node[below] at (2.92,0) {$%s\\text{ cm}$};
    \\node at (1.62,0.52) {$120^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (ca, cb))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ có $CA = %s\\text{ cm}$, $CB = %s\\text{ cm}$ và $\\widehat{ACB} = 120^\\circ$ (như hình vẽ). \\\\
    a) Kẻ đường cao $AH$ của tam giác $ABC$ ($H$ thuộc tia đối của tia $CB$). Tính độ dài các đoạn thẳng $CH$ và $AH$. \\\\
    b) Tính độ dài cạnh $AB$ và số đo góc $B$ của tam giác $ABC$ (góc làm tròn đến độ). \\\\
    c) Tính độ dài đường cao $CK$ xuất phát từ đỉnh $C$ của tam giác $ABC$.
    %s''' % (ca, cb, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Vì $\\widehat{ACB} = 120^\\circ$ nên góc kề bù $\\widehat{ACH} = 180^\\circ - 120^\\circ = 60^\\circ$.\\\\
    Xét tam giác $AHC$ vuông tại $H$, theo Định lí 1 ta có:\\\\
    $CH = CA \\cdot \\cos 60^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ (cm)}$ và $AH = CA \\cdot \\sin 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s\\text{ (cm)}$.
    \\item Vì $C$ nằm giữa $H$ và $B$ nên $HB = CH + CB = %s + %s = %s\\text{ (cm)}$.\\\\
    Áp dụng định lí Pythagore trong tam giác vuông $AHB$, ta có:\\\\
    $AB = \\sqrt{AH^2 + HB^2} = \\sqrt{\\left(%s\\right)^2 + \\left(%s\\right)^2} = \\sqrt{%s} = %s\\text{ (cm)}$.\\\\
    Ta có $\\tan B = \\dfrac{AH}{HB} = \\dfrac{%s}{%s} = \\dfrac{3\\sqrt{3}}{13} \\Rightarrow \\widehat{B} \\approx %s^\\circ$.
    \\item Diện tích tam giác $ABC$ là $S = \\dfrac{1}{2} AH \\cdot BC = \\dfrac{1}{2} CK \\cdot AB$.\\\\
    Suy ra đường cao $CK = \\dfrac{AH \\cdot BC}{AB} = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.
    \\end{enumEX}'''
                   % (ca, latex(ch), ca, latex(ah_sym),
                      latex(ch), cb, latex(hb),
                      latex(ah_sym), latex(hb), ab**2, ab,
                      latex(ah_sym), latex(hb), deg_b,
                      latex(ah_sym), cb, ab, latex(ck_sym)))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
