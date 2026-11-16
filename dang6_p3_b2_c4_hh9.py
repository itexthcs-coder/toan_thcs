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


def bt_dang6_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        nm = random.choice([20, 25, 30, 35])
        a_deg = 27
        b_deg = 19
        gk = 1.6
        gk_str = '1,6'

        cot_b = 1.0 / math.tan(math.radians(b_deg))
        cot_a = 1.0 / math.tan(math.radians(a_deg))
        ph_val = nm / (cot_b - cot_a)
        cao_val = ph_val + gk

        ph_str = str(Decimal(str(ph_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        number = Decimal(str(cao_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (N) at (0,0);
    \\coordinate (M) at (1.6,0);
    \\coordinate (P) at (4.6,0);
    \\coordinate (N1) at (0,0.45);
    \\coordinate (M1) at (1.6,0.45);
    \\coordinate (H) at (4.6,0.45);
    \\coordinate (P1) at (4.6,2.45);
    \\draw[line width=1pt] (N)--(P)--(P1) (N)--(N1)--(H) (M)--(M1) (N1)--(P1) (M1)--(P1);
    \\draw[line width=1pt] (4.38,0.45)--(4.38,0.67)--(4.6,0.67);
    \\draw[line width=1pt] (0.65,0.45) arc (0:25.2:0.65);
    \\draw[line width=1pt] (2.15,0.45) arc (0:33.7:0.55);
    \\fill (N) circle (1pt) node[below] {$N$};
    \\fill (M) circle (1pt) node[below] {$M$};
    \\fill (P) circle (1pt) node[below] {$P$};
    \\fill (N1) circle (1pt) node[above left] {$N'$};
    \\fill (M1) circle (1pt) node[above left] {$M'$};
    \\fill (H) circle (1pt) node[right] {$H$};
    \\fill (P1) circle (1pt) node[above right] {$P'$};
    \\node[below] at (0.8,0) {$%s\\text{ m}$};
    \\node[left] at (0,0.22) {$%s\\text{ m}$};
    \\node at (0.95,0.62) {$%s^\\circ$};
    \\node at (2.42,0.65) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (nm, gk_str, b_deg, a_deg))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Để đo chiều cao của một tòa lâu đài, người ta đặt giác kế thẳng đứng tại điểm $M$ thì nhìn thấy đỉnh $P'$ của tòa lâu đài dưới góc nâng $\\alpha = %s^\\circ$. Sau đó lùi giác kế ra xa theo phương thẳng hàng với chân lâu đài một đoạn $NM = %s\\text{ m}$ thì nhìn thấy đỉnh $P'$ dưới góc nâng $\\beta = %s^\\circ$ (như hình vẽ). Biết chiều cao giác kế là $%s\\text{ m}$, tính chiều cao của tòa lâu đài theo đơn vị mét (làm tròn kết quả đến hàng phần mười).
    %s''' % (a_deg, nm, b_deg, gk_str, hinhve))

        # Nội dung lời giải
        loigiai = ('''Gọi $H$ là hình chiếu vuông góc của $P'$ trên đường thẳng ngang qua ống ngắm $N'M'$. Ta có $N'M' = NM = %s\\text{ m}$ và $HP = NN' = %s\\text{ m}$.\\\\
    Xét tam giác $P'HM'$ vuông tại $H$, ta có $M'H = P'H \\cdot \\cot %s^\\circ$.\\\\
    Xét tam giác $P'HN'$ vuông tại $H$, ta có $N'H = P'H \\cdot \\cot %s^\\circ$.\\\\
    Mặt khác $N'H - M'H = N'M' = %s$, suy ra $P'H(\\cot %s^\\circ - \\cot %s^\\circ) = %s$.\\\\
    Do đó $P'H = \\dfrac{%s}{\\cot %s^\\circ - \\cot %s^\\circ} \\approx %s\\text{ (m)}$.\\\\
    Vậy chiều cao của tòa lâu đài là $P'P = P'H + HP \\approx %s + %s \\approx %s\\text{ (m)}$.'''
                   % (nm, gk_str, a_deg, b_deg, nm, b_deg, a_deg, nm,
                      nm, b_deg, a_deg, ph_str,
                      ph_str, gk_str, str(kq_str)))

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
