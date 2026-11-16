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


def bt_dang3_p4_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2, 3])
        hb = 3 * k
        hc = 6 * k
        bc = 9 * k
        ah_sym = 2 * k * sqrt(3)
        ac_sym = 4 * k * sqrt(3)
        ab_sym = k * sqrt(21)

        ah_val = 2 * k * math.sqrt(3)
        deg_b = int(Decimal(str(math.degrees(math.atan(ah_val / hb)))).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        deg_c = 30
        deg_a = 180 - deg_b - deg_c
        bk_val = bc * math.sin(math.radians(deg_c))
        bk_str = str(Decimal(str(bk_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (H) at (1.5,0);
    \\coordinate (C) at (4.5,0);
    \\coordinate (A) at (1.5,1.73);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(H);
    \\draw[line width=1pt] (1.5,0.22)--(1.72,0.22)--(1.72,0);
    \\draw[line width=1pt] (1.5,1.25) arc (270:330:0.48);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\node[below] at (0.75,0) {$%s\\text{ cm}$};
    \\node[below] at (3.0,0) {$%s\\text{ cm}$};
    \\node at (1.82,1.15) {$60^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (hb, hc))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ nhọn có chân đường cao $AH$ nằm giữa $B$ và $C$. Biết $HB = %s\\text{ cm}$, $HC = %s\\text{ cm}$ và $\\widehat{HAC} = 60^\\circ$ (như hình vẽ). \\\\
    a) Tính độ dài đường cao $AH$ và độ dài các cạnh $AB, AC$ (kết quả giữ dưới dạng căn thức thu gọn). \\\\
    b) Tính số đo các góc $B, C, A$ của tam giác $ABC$ (làm tròn đến độ). \\\\
    c) Kẻ đường cao $BK$ của tam giác $ABC$. Tính độ dài đoạn thẳng $BK$ (làm tròn đến chữ số thập phân thứ hai).
    %s''' % (hb, hc, hinhve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
    \\item Xét tam giác $AHC$ vuông tại $H$, ta có:\\\\
    $AH = HC \\cdot \\cot \\widehat{HAC} = %s \\cdot \\cot 60^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{3} = %s\\text{ (cm)}$.\\\\
    $AC = \\dfrac{HC}{\\sin \\widehat{HAC}} = \\dfrac{%s}{\\sin 60^\\circ} = \\dfrac{%s}{\\dfrac{\\sqrt{3}}{2}} = %s\\text{ (cm)}$.\\\\
    Xét tam giác $ABH$ vuông tại $H$, áp dụng định lí Pythagore ta có:\\\\
    $AB = \\sqrt{HB^2 + AH^2} = \\sqrt{%s^2 + (%s)^2} = %s\\text{ (cm)}$.
    \\item Trong tam giác vuông $AHC$, ta có $\\widehat{C} = 90^\\circ - \\widehat{HAC} = 90^\\circ - 60^\\circ = 30^\\circ$.\\\\
    Trong tam giác vuông $ABH$, ta có $\\tan B = \\dfrac{AH}{HB} = \\dfrac{%s}{%s} = \\dfrac{2\\sqrt{3}}{3} \\Rightarrow \\widehat{B} \\approx %s^\\circ$.\\\\
    Suy ra $\\widehat{BAC} = 180^\\circ - (\\widehat{B} + \\widehat{C}) \\approx 180^\\circ - (%s^\\circ + 30^\\circ) = %s^\\circ$.
    \\item Ta có $BC = HB + HC = %s + %s = %s\\text{ (cm)}$.\\\\
    Xét tam giác $BKC$ vuông tại $K$, theo Định lí 1 ta có $BK = BC \\cdot \\sin C = %s \\cdot \\sin 30^\\circ = %s\\text{ (cm)}$.
    \\end{enumEX}'''
                   % (hc, hc, latex(ah_sym),
                      hc, hc, latex(ac_sym),
                      hb, latex(ah_sym), latex(ab_sym),
                      latex(ah_sym), hb, deg_b,
                      deg_b, deg_a,
                      hb, hc, bc,
                      bc, bk_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
