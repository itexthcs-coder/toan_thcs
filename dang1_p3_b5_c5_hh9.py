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


def bt_dang1_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = randint(1, 3)
        b = randint(4, 7)
        d = randint(10, 18)
        m_min = math.floor((d - a - b) / 3) + 1
        m_min = max(1, m_min)
        m_max = math.ceil(d + b - a) - 1
        so_gia_tri = max(0, m_max - m_min + 1)
        kq_str = str(so_gia_tri)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (3.2,0);
\\draw[line width=1pt] (O) circle (2.2cm);
\\draw[line width=1pt] (Op) circle (1.6cm);
\\draw[line width=1pt, dashed] (O)--(Op);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (Op) circle (1pt) node[right] {$O'$};
\\fill (1.95, 1.02) circle (1pt) node[above] {$A$};
\\fill (1.95, -1.02) circle (1pt) node[below] {$B$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai đường tròn $(O; 2m + %s)$ và $(O'; m + %s)$ với $m > 0$, biết độ dài đoạn nối tâm $OO' = %s$. Có bao nhiêu giá trị nguyên của $m$ để hai đường tròn đã cho cắt nhau?\\\\
%s''' % (a, b, d, hinhve))

        loigiai = ('''Để hai đường tròn $(O; R)$ và $(O'; R')$ với $R = 2m + %s$ và $R' = m + %s$ cắt nhau thì hệ thức giữa đoạn nối tâm và hai bán kính phải thỏa mãn: \\\\
$|R - R'| < OO' < R + R'$ \\\\
$\\Leftrightarrow |(2m + %s) - (m + %s)| < %s < (2m + %s) + (m + %s)$ \\\\
$\\Leftrightarrow |m - %s| < %s < 3m + %s$. \\\\
Giải hệ bất phương trình: \\\\
1) $3m + %s > %s \\Leftrightarrow 3m > %s \\Leftrightarrow m > %s$. \\\\
2) $|m - %s| < %s \\Leftrightarrow -%s < m - %s < %s \\Leftrightarrow -%s < m < %s$. \\\\
Kết hợp với điều kiện đề bài $m > 0$ và $m \\in \\mathbb{Z}$, ta được $%s \\le m \\le %s$. \\\\
Vậy có tất cả $%s$ giá trị nguyên của $m$ thỏa mãn yêu cầu bài toán.'''
                   % (a, b, a, b, d, a, b, b - a, d, a + b,
                      a + b, d, d - a - b, latex(Rational(d - a - b, 3)),
                      b - a, d, d, b - a, d, d - (b - a), d + b - a,
                      m_min, m_max, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
