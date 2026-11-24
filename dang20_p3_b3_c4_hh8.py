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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang20_p3_b3_c4_hh8(self):
    # Dạng 20: Tính chiều dài thanh đỡ ngang trên giàn giáo chữ A (Thực tế)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (3, 1.8, 1, 0.9, 0.6, 1.5),
            (2.4, 1.2, 0.8, 0.6, 0.4, 1),
            (3.6, 2.4, 1.2, 1.2, 0.8, 2),
            (3, 2.4, 1, 1.2, 0.8, 2),
            (4.5, 3, 1.5, 1.5, 1, 2.5)
        ]
        ab, bc, ap, mn, pq, tong = random.choice(bo_so)
        s_ab = fmt_num(ab)
        s_bc = fmt_num(bc)
        s_ap = fmt_num(ap)
        s_mn = fmt_num(mn)
        s_pq = fmt_num(pq)
        kq_str = fmt_num(tong)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (1.8,3.6);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (3.6,0);\n'
            '\\coordinate (M) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (N) at ($(A)!0.5!(C)$);\n'
            '\\coordinate (P) at ($(A)!0.333!(B)$);\n'
            '\\coordinate (Q) at ($(A)!0.333!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B) (A)--(C) (M)--(N) (P)--(Q);\n'
            '\\draw[line width=1pt, dashed] (B)--(C);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (M) circle (1pt) node[left] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (P) circle (1pt) node[left] {$P$};\n'
            '\\fill (Q) circle (1pt) node[right] {$Q$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Một khung giàn giáo chữ A có dạng tam giác $ABC$ cân tại $A$ với chiều dài hai chân $AB = AC = %s\\text{ m}$ và khoảng cách giữa hai chân chạm đất là $BC = %s\\text{ m}$. Người ta lắp hai thanh ngang $MN$ và $PQ$ cùng song song với mặt đất $BC$ ($M, P \\in AB$ và $N, Q \\in AC$), biết $M, N$ là trung điểm của $AB, AC$ và $AP = AQ = %s\\text{ m}$. Tính tổng chiều dài hai thanh ngang $MN$ và $PQ$ (đơn vị: $\\text{m}$).\n%s'
            % (s_ab, s_bc, s_ap, hinh_ve)
        )

        loigiai = (
            'Vì $M, N$ là trung điểm của $AB, AC$ nên $MN$ là đường trung bình của tam giác $ABC$, suy ra $MN = \\frac{1}{2}BC = \\frac{1}{2} \\cdot %s = %s\\text{ m}$.\\\\'
            'Vì $PQ // BC$ nên theo hệ quả của định lí Thalès trong tam giác $ABC$, ta có: $\\frac{PQ}{BC} = \\frac{AP}{AB} = \\frac{%s}{%s}$, suy ra $PQ = \\frac{%s}{%s} \\cdot %s = %s\\text{ m}$.\\\\'
            'Vậy tổng chiều dài hai thanh ngang là $MN + PQ = %s + %s = %s\\text{ m}$.'
            % (s_bc, s_mn, s_ap, s_ab, s_ap, s_ab, s_bc, s_pq, s_mn, s_pq, kq_str)
        )

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
