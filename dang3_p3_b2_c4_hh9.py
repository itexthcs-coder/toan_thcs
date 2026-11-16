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


def bt_dang3_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.randint(1, 5)
        loai = random.choice([1, 2])
        if loai == 1:
            ac = 2 * k * sqrt(3)
            bd = 2 * k
            oa = k * sqrt(3)
            ob = k
            tan_str = '\\dfrac{\\sqrt{3}}{3}'
            g_oab = 30
        else:
            ac = 2 * k
            bd = 2 * k * sqrt(3)
            oa = k
            ob = k * sqrt(3)
            tan_str = '\\sqrt{3}'
            g_oab = 60

        g_nhon = 60
        g_tu = 120
        m = random.choice([1, 2, 3])
        n = random.choice([1, 2])
        kq = m * g_nhon + n * g_tu
        kq_str = str(kq)

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (-2.4,0);
    \\coordinate (C) at (2.4,0);
    \\coordinate (B) at (0,1.4);
    \\coordinate (D) at (0,-1.4);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D);
    \\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
    \\fill (O) circle (1pt) node[below right] {$O$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\end{tikzpicture}
    \\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thoi $ABCD$ có hai đường chéo $AC$ và $BD$ cắt nhau tại $O$, biết $AC = %s\\text{ cm}$ và $BD = %s\\text{ cm}$ (như hình vẽ). Gọi $\\alpha$ là số đo góc nhọn và $\\beta$ là số đo góc tù của hình thoi đó (tính theo đơn vị độ). Tính giá trị biểu thức $T = %s\\alpha + %s\\beta$.
    %s''' % (latex(ac), latex(bd), m, n, hinhve))

        # Nội dung lời giải
        loigiai = ('''Vì $ABCD$ là hình thoi nên $AC \\perp BD$ tại trung điểm $O$ của mỗi đường.\\\\
    Suy ra $OA = \\dfrac{AC}{2} = %s\\text{ (cm)}$ và $OB = \\dfrac{BD}{2} = %s\\text{ (cm)}$.\\\\
    Xét tam giác $OAB$ vuông tại $O$, ta có $\\tan \\widehat{OAB} = \\dfrac{OB}{OA} = \\dfrac{%s}{%s} = %s \\Rightarrow \\widehat{OAB} = %s^\\circ$.\\\\
    Do $AC$ là tia phân giác của $\\widehat{BAD}$ nên $\\widehat{BAD} = 2 \\cdot %s^\\circ = %s^\\circ$, suy ra $\\widehat{ABC} = 180^\\circ - %s^\\circ = %s^\\circ$.\\\\
    Vậy góc nhọn $\\alpha = 60$, góc tù $\\beta = 120$ và $T = %s \\cdot 60 + %s \\cdot 120 = %s$.'''
                   % (latex(oa), latex(ob), latex(ob), latex(oa), tan_str, g_oab,
                      g_oab, 2 * g_oab, 2 * g_oab, 180 - 2 * g_oab,
                      m, n, kq))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
