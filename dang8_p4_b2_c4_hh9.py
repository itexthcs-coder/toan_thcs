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


def bt_dang8_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([3, 4, 5])
        h = 3.5
        h_str = '3,5'
        dh_val = h / 1.25
        ck_val = h / 1.5
        cd_val = dh_val + ab + ck_val
        ad_val = math.sqrt(h**2 + dh_val**2)
        bc_val = math.sqrt(h**2 + ck_val**2)
        dt_val = (ab + cd_val) * h / 2.0

        dh_str = str(Decimal(str(dh_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        ck_str = str(Decimal(str(ck_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        cd_str = str(Decimal(str(cd_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        ad_str = str(Decimal(str(ad_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        bc_str = str(Decimal(str(bc_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
        dt_str = str(Decimal(str(dt_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (H) at (1.3,0);
    \\coordinate (K) at (2.8,0);
    \\coordinate (C) at (3.9,0);
    \\coordinate (A) at (1.3,1.8);
    \\coordinate (B) at (2.8,1.8);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(H);
    \\draw[line width=1pt, dashed] (B)--(K);
    \\draw[line width=1pt] (1.3,0.22)--(1.52,0.22)--(1.52,0);
    \\draw[line width=1pt] (2.8,0.22)--(3.02,0.22)--(3.02,0);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\fill (K) circle (1pt) node[below] {$K$};
    \\node[above] at (2.05,1.8) {$%s\\text{ m}$};
    \\node[right] at (1.3,0.9) {$%s\\text{ m}$};
    \\end{tikzpicture}
    \\end{center}''' % (ab, h_str))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Mặt cắt ngang của một đập ngăn nước có dạng hình thang $ABCD$ ($AB // CD$), trong đó $AB$ là mặt trên của đập rộng $%s\\text{ m}$ và chiều cao của đập bằng $%s\\text{ m}$ (như hình vẽ). Biết độ dốc của sườn $AD$ là $\\tan D = 1,25$ và độ dốc của sườn $BC$ là $\\tan C = 1,5$. \\\\
    a) Tính chiều rộng $CD$ của chân đập (làm tròn đến dm). \\\\
    b) Tính chiều dài các sườn nghiêng $AD$ và $BC$ của đập (làm tròn đến dm). \\\\
    c) Tính diện tích mặt cắt ngang $ABCD$ của đập ngăn nước đó (làm tròn đến hàng phần mười).
    %s''' % (ab, h_str, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Kẻ các đường cao $AH \\perp CD$ và $BK \\perp CD$. Tứ giác $ABKH$ là hình chữ nhật nên $HK = AB = %s\\text{ m}$ và $AH = BK = %s\\text{ m}$.\\\\
    Xét tam giác $AHD$ vuông tại $H$, ta có $DH = \\dfrac{AH}{\\tan D} = \\dfrac{%s}{1,25} = %s\\text{ (m)}$.\\\\
    Xét tam giác $BKC$ vuông tại $K$, ta có $CK = \\dfrac{BK}{\\tan C} = \\dfrac{%s}{1,5} \\approx %s\\text{ (m)}$.\\\\
    Chiều rộng chân đập là $CD = DH + HK + CK \\approx %s + %s + %s \\approx %s\\text{ (m)}$.
    \\item Áp dụng định lí Pythagore trong hai tam giác vuông $AHD$ và $BKC$, ta có:\\\\
    $AD = \\sqrt{AH^2 + DH^2} = \\sqrt{%s^2 + %s^2} \\approx %s\\text{ (m)}$.\\\\
    $BC = \\sqrt{BK^2 + CK^2} \\approx \\sqrt{%s^2 + %s^2} \\approx %s\\text{ (m)}$.
    \\item Diện tích mặt cắt ngang hình thang $ABCD$ là:\\\\
    $S = \\dfrac{(AB + CD) \\cdot AH}{2} \\approx \\dfrac{(%s + %s) \\cdot %s}{2} \\approx %s\\text{ (m}^2\\text{)}$.
    \\end{enumEX}'''
                   % (ab, h_str, h_str, dh_str, h_str, ck_str,
                      dh_str, ab, ck_str, cd_str,
                      h_str, dh_str, ad_str,
                      h_str, ck_str, bc_str,
                      ab, cd_str, h_str, dt_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
