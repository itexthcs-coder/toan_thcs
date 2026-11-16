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


def bt_dang20_p3_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d1 = randint(8, 18) * 10
        g1 = randint(8, 14)
        d2 = randint(10, 22) * 10
        g2 = randint(15, 22)
        h1 = d1 * math.sin(math.radians(g1))
        h2 = d2 * math.sin(math.radians(g2))
        tong_h = h1 + h2
        number = Decimal(str(tong_h))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        h1_str = str(Decimal(str(h1)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        h2_str = str(Decimal(str(h2)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        # Hình vẽ TikZ
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (H) at (2.5,0);
    \\coordinate (B) at (2.5,0.9);
    \\coordinate (K) at (5.2,0.9);
    \\coordinate (C) at (5.2,2.3);
    \\coordinate (E) at (5.2,0);
    \\draw[line width=1pt] (A)--(E);
    \\draw[line width=1pt] (A)--(B)--(C);
    \\draw[line width=1pt, dashed] (B)--(H) (B)--(K) (C)--(E);
    \\draw[line width=1pt] (2.2,0)--(2.2,0.3)--(2.5,0.3);
    \\draw[line width=1pt] (4.9,0.9)--(4.9,1.2)--(5.2,1.2);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[above left] {$B$};
    \\fill (C) circle (1pt) node[above right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\fill (K) circle (1pt) node[right] {$K$};
    \\fill (E) circle (1pt) node[below right] {$E$};
    \\node[above left] at (1.25,0.45) {$%s\\text{ m}$};
    \\node[above left] at (3.85,1.6) {$%s\\text{ m}$};
    \\node[above right] at (0.5,0) {$%s^\\circ$};
    \\node[above right] at (2.9,0.9) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (str(d1), str(d2), str(g1), str(g2)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một con đường dốc lên đồi gồm hai đoạn thẳng nối tiếp nhau: đoạn thứ nhất dài $%s\\text{ m}$ nghiêng góc $%s^\\circ$ so với phương ngang, đoạn thứ hai dài $%s\\text{ m}$ nghiêng góc $%s^\\circ$ so với phương ngang. Hỏi đỉnh dốc cao hơn chân dốc bao nhiêu mét? (Làm tròn đến chữ số thập phân thứ nhất). %s'''
                         % (str(d1), str(g1), str(d2), str(g2), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Mô hình hóa đoạn dốc thứ nhất là $AB = %s\\text{ m}$ tạo với phương ngang góc $\\widehat{BAH} = %s^\\circ$ ($BH \\perp AH$) và đoạn dốc thứ hai là $BC = %s\\text{ m}$ tạo với phương ngang góc $\\widehat{CBK} = %s^\\circ$ ($CK \\perp BK$). \\\\
Xét tam giác $ABH$ vuông tại $H$, độ cao đạt được ở đoạn dốc thứ nhất là: \\\\
$BH = AB \\cdot \\sin %s^\\circ = %s \\cdot \\sin %s^\\circ \\approx %s\\text{ (m)}$. \\\\
Xét tam giác $BCK$ vuông tại $K$, độ cao tăng thêm ở đoạn dốc thứ hai là: \\\\
$CK = BC \\cdot \\sin %s^\\circ = %s \\cdot \\sin %s^\\circ \\approx %s\\text{ (m)}$. \\\\
Vì $BHEK$ là hình chữ nhật nên $KE = BH$. Vậy đỉnh dốc $C$ cao hơn chân dốc $A$ một khoảng là: \\\\
$CE = CK + BH \\approx %s + %s \\approx %s\\text{ (m)}$.'''
                   % (str(d1), str(g1), str(d2), str(g2),
                      str(g1), str(d1), str(g1), h1_str,
                      str(g2), str(d2), str(g2), h2_str,
                      h2_str, h1_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \end{minipage} \n\n')
    return content
