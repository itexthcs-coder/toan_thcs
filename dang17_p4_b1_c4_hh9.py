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


def bt_dang17_p4_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = randint(3, 10)
        hc = randint(3, 9)
        cd = ab + hc
        goc_c = randint(35, 65)
        bc_val = Decimal(str(hc / math.cos(math.radians(goc_c)))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        ad_val = Decimal(str(hc * math.tan(math.radians(goc_c)))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        s_val = Decimal(str((ab + cd) * float(ad_val) / 2.0)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        bc_str = str(bc_val).replace('.', ',')
        ad_str = str(ad_val).replace('.', ',')
        s_str = str(s_val).replace('.', ',')

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (H) at (2.2,0);
    \\coordinate (C) at (4.5,0);
    \\coordinate (A) at (0,2.5);
    \\coordinate (B) at (2.2,2.5);
    \\draw[line width=1pt] (D)--(C)--(B)--(A)--cycle;
    \\draw[line width=1pt, dashed] (B)--(H);
    \\draw[line width=1pt] (0,0.3)--(0.3,0.3)--(0.3,0);
    \\draw[line width=1pt] (2.2,0.3)--(2.5,0.3)--(2.5,0);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[above] at (1.1,2.5) {$%s\\text{ cm}$};
    \\node[below] at (2.25,-0.25) {$%s\\text{ cm}$};
    \\node[above left] at (4.1,0) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (str(ab), str(cd), str(goc_c)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) có đáy nhỏ $AB = %s\\text{ cm}$, đáy lớn $CD = %s\\text{ cm}$ và $\\widehat{BCD} = %s^\\circ$. Kẻ đường cao $BH$ ($H \\in CD$). %s \\\\
a) Tính độ dài cạnh bên $BC$ và chiều cao $AD$ (làm tròn đến chữ số thập phân thứ hai). \\\\
b) Tính diện tích hình thang $ABCD$ (làm tròn đến chữ số thập phân thứ hai).'''
                         % (str(ab), str(cd), str(goc_c), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
\\item Tứ giác $ABHD$ có ba góc vuông ($\\widehat{A} = \\widehat{D} = \\widehat{BHD} = 90^\\circ$) nên là hình chữ nhật, suy ra $DH = AB = %s\\text{ cm}$ và $BH = AD$. \\\\
Do đó $HC = CD - DH = %s - %s = %s\\text{ (cm)}$. \\\\
Xét tam giác $BHC$ vuông tại $H$ có $\\widehat{C} = %s^\\circ$, ta có: \\\\
$\\cos C = \\dfrac{HC}{BC} \\Rightarrow BC = \\dfrac{HC}{\\cos %s^\\circ} = \\dfrac{%s}{\\cos %s^\\circ} \\approx %s\\text{ (cm)}$; \\\\
$\\tan C = \\dfrac{BH}{HC} \\Rightarrow AD = BH = HC \\cdot \\tan %s^\\circ = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ (cm)}$. \n
\\item Diện tích hình thang $ABCD$ là: \\\\
$S_{ABCD} = \\dfrac{(AB + CD) \\cdot AD}{2} \\approx \\dfrac{(%s + %s) \\cdot %s}{2} \\approx %s\\text{ (cm}^2\\text{)}$. \n
\\end{enumEX} \n'''
                   % (str(ab), str(cd), str(ab), str(hc),
                      str(goc_c), str(goc_c), str(hc), str(goc_c), bc_str,
                      str(goc_c), str(hc), str(goc_c), ad_str,
                      str(ab), str(cd), ad_str, s_str))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \end{minipage} \n\n')
    return content
