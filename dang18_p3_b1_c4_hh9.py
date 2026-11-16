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


def bt_dang18_p3_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        kc = randint(25, 65)
        goc = randint(30, 58)
        h_ke = random.choice([1.2, 1.4, 1.5, 1.6])
        h_ke_str = str(h_ke).replace('.', ',')
        h_thap = h_ke + kc * math.tan(math.radians(goc))
        number = Decimal(str(h_thap))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(int(kq))
        h_1tp = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        h_1tp_str = str(h_1tp).replace('.', ',')

        # Hình vẽ TikZ
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (C) at (0,0);
    \\coordinate (D) at (4,0);
    \\coordinate (A) at (0,0.8);
    \\coordinate (H) at (4,0.8);
    \\coordinate (B) at (4,3.8);
    \\draw[line width=1pt] (C)--(D)--(B);
    \\draw[line width=1pt] (C)--(A)--(B);
    \\draw[line width=1pt, dashed] (A)--(H);
    \\draw[line width=1pt] (3.7,0.8)--(3.7,1.1)--(4,1.1);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below left] {$C$};
    \\fill (D) circle (1pt) node[below right] {$D$};
    \\fill (H) circle (1pt) node[right] {$H$};
    \\node[left] at (0,0.4) {$%s\\text{ m}$};
    \\node[below] at (2,0) {$%s\\text{ m}$};
    \\node[above right] at (0.5,0.8) {$%s^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (h_ke_str, str(kc), str(goc)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Để đo chiều cao của một tòa tháp, một người đặt giác kế cách chân tháp $%s\\text{ m}$ và nhìn thấy đỉnh tháp dưới một góc nâng $%s^\\circ$ so với phương nằm ngang. Biết chiều cao của giác kế là $%s\\text{ m}$. Tính chiều cao của tòa tháp (đơn vị: mét, làm tròn đến hàng đơn vị). %s'''
                         % (str(kc), str(goc), h_ke_str, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Gọi $AC = %s\\text{ m}$ là chiều cao của giác kế, $CD = %s\\text{ m}$ là khoảng cách từ giác kế đến chân tháp và $BD$ là chiều cao của tòa tháp. \\\\
Kẻ $AH \\perp BD$ ($H \\in BD$), khi đó tứ giác $ACDH$ là hình chữ nhật nên $AH = CD = %s\\text{ m}$ và $HD = AC = %s\\text{ m}$. \\\\
Xét tam giác $ABH$ vuông tại $H$ với $\\widehat{BAH} = %s^\\circ$, ta có: \\\\
$\\tan \\widehat{BAH} = \\dfrac{BH}{AH} \\Rightarrow BH = AH \\cdot \\tan %s^\\circ = %s \\cdot \\tan %s^\\circ$. \\\\
Chiều cao của tòa tháp là: \\\\
$BD = BH + HD = %s \\cdot \\tan %s^\\circ + %s \\approx %s\\text{ (m)}$. \\\\
Làm tròn đến hàng đơn vị, chiều cao tòa tháp là $%s\\text{ m}$.'''
                   % (h_ke_str, str(kc), str(kc), h_ke_str, str(goc),
                      str(goc), str(kc), str(goc),
                      str(kc), str(goc), h_ke_str, h_1tp_str, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
