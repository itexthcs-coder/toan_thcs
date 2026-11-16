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


def bt_dang17_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ac = random.choice([40, 50, 60])
        goc = 40
        rad = math.radians(goc)
        d_val = ac * math.tan(rad)
        bc_val = ac / math.cos(rad)
        v_boi = 1.2
        v_boi_str = '1,2'
        tg_boi = int(Decimal(str(bc_val / v_boi)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

        d_str = str(Decimal(str(d_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        bc_str = str(Decimal(str(bc_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (3.6,0);
    \\coordinate (C) at (0,0);
    \\coordinate (B) at (3.6,2.4);
    \\draw[line width=1pt] (-0.5,0)--(4.3,0) (-0.5,2.4)--(4.3,2.4);
    \\draw[line width=1pt] (C)--(B);
    \\draw[line width=1pt, dashed] (A)--(B);
    \\draw[line width=1pt] (3.38,0)--(3.38,0.22)--(3.6,0.22);
    \\draw[line width=1pt] (0.65,0) arc (0:33.7:0.65);
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\node[below] at (1.8,0) {$%s\\text{ m}$};
    \\node[right] at (3.6,1.2) {$d$};
    \\node at (0.98,0.25) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (ac, goc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Để đo chiều rộng $d$ của một khúc sông thẳng có hai bờ song song mà không cần sang bờ bên kia, một nhóm học sinh chọn một cây cột mốc $B$ ở sát mép bờ bên kia, đứng tại điểm $A$ đối diện vuông góc với $B$ ở bờ bên này, sau đó đi dọc theo bờ sông đến điểm $C$ cách $A$ một đoạn $%s\\text{ m}$ và dùng giác kế đo được góc $\\widehat{ACB} = %s^\\circ$ (như hình vẽ). \\\\
    a) Tính chiều rộng $d$ của khúc sông (làm tròn đến mét). \\\\
    b) Một người bơi thẳng từ $C$ hướng tới cột mốc $B$ với vận tốc $%s\\text{ m/s}$. Hỏi sau bao nhiêu giây người đó bơi sang tới điểm $B$ (làm tròn đến giây)?
    %s''' % (ac, goc, v_boi_str, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $ABC$ vuông tại $A$, theo Định lí 2 ta có chiều rộng của khúc sông là:\\\\
    $d = AB = AC \\cdot \\tan C = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ (m)}$.
    \\item Khoảng cách bơi thẳng từ $C$ tới $B$ là cạnh huyền của tam giác vuông $ABC$:\\\\
    $BC = \\dfrac{AC}{\\cos C} = \\dfrac{%s}{\\cos %s^\\circ} \\approx %s\\text{ (m)}$.\\\\
    Thời gian để người đó bơi từ $C$ sang tới $B$ là $t = \\dfrac{BC}{%s} \\approx \\dfrac{%s}{%s} \\approx %s\\text{ (giây)}$.
    \\end{enumEX}'''
                   % (ac, goc, d_str,
                      ac, goc, bc_str,
                      v_boi_str, bc_str, v_boi_str, tg_boi))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
