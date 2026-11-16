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


def bt_dang4_p3_b2_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ad = random.randint(3, 8)
        g1 = random.choice([18, 20, 22, 25])
        g2 = random.choice([35, 38, 40, 42])

        ac_val = ad / math.tan(math.radians(g1))
        ab_val = ac_val * math.tan(math.radians(g2))
        bd_val = ab_val - ad

        ac_str = str(Decimal(str(ac_val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')
        ab_str = str(Decimal(str(ab_val)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',')

        number = Decimal(str(bd_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (C) at (4.2,0);
    \\coordinate (D) at (0,1.5);
    \\coordinate (B) at (0,2.9);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle (C)--(D);
    \\draw[line width=1pt] (0,0.22)--(0.22,0.22)--(0.22,0);
    \\draw[line width=1pt] (3.55,0) arc (180:160.3:0.65);
    \\draw[line width=1pt] (3.15,0) arc (180:145.4:1.05);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[above left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\node[left] at (0,0.75) {$%s\\text{ cm}$};
    \\node at (3.25,0.22) {$%s^\\circ$};
    \\node at (2.75,0.58) {$%s^\\circ$};
    \\end{tikzpicture}
    \\end{center}''' % (ad, g1, g2))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$, trên cạnh $AB$ lấy điểm $D$ sao cho $\\widehat{ACB} = %s^\\circ$, $\\widehat{ACD} = %s^\\circ$ và $AD = %s\\text{ cm}$ (như hình vẽ). Tính độ dài đoạn thẳng $BD$ theo đơn vị xentimét (làm tròn kết quả đến hàng phần mười).
    %s''' % (g2, g1, ad, hinhve))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $ADC$ vuông tại $A$, ta có $AD = AC \\cdot \\tan \\widehat{ACD}$.\\\\
    Suy ra $AC = \\dfrac{AD}{\\tan %s^\\circ} = \\dfrac{%s}{\\tan %s^\\circ} \\approx %s\\text{ (cm)}$.\\\\
    Xét tam giác $ABC$ vuông tại $A$, ta có:\\\\
    $AB = AC \\cdot \\tan \\widehat{ACB} \\approx %s \\cdot \\tan %s^\\circ \\approx %s\\text{ (cm)}$.\\\\
    Do điểm $D$ nằm giữa $A$ và $B$ nên $BD = AB - AD \\approx %s - %s \\approx %s\\text{ (cm)}$.'''
                   % (g1, ad, g1, ac_str,
                      ac_str, g2, ab_str,
                      ab_str, ad, str(kq_str)))

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
