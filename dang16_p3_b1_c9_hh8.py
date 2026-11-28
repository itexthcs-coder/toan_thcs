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
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        dec = (Decimal(val.numerator) / Decimal(val.denominator)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        s = format(dec.normalize(), 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')
    s = str(val)
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')
def bt_dang16_p3_b1_c9_hh8(self):
    # Dạng 16 (Thực tế): Đo chiều cao vật thể bằng bóng nắng tại cùng một thời điểm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (Fraction(3, 2), Fraction(6, 5), 16),
            (Fraction(3, 2), Fraction(3, 4), 12),
            (Fraction(2, 1), Fraction(5, 4), 15),
            (Fraction(8, 5), Fraction(4, 5), 14),
            (Fraction(9, 5), Fraction(6, 5), 18),
            (Fraction(3, 2), Fraction(9, 10), 15),
            (Fraction(2, 1), Fraction(8, 5), 20),
            (Fraction(3, 2), Fraction(1, 1), 14),
        ]
        coc, bong_coc, bong_nha = random.choice(cases)
        cao_nha = coc * bong_nha / bong_coc
        coc_s = fmt_num(coc)
        bc_s = fmt_num(bong_coc)
        kq_str = fmt_num(cao_nha)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (B) at (0,0);\n'
            ' \\coordinate (A) at (0,2.8);\n'
            ' \\coordinate (E) at (4.2,0);\n'
            ' \\coordinate (C) at (2.8,0);\n'
            ' \\coordinate (D) at (2.8,0.933);\n'
            ' \\draw[line width=1pt] (B)--(A)--(E)--cycle (C)--(D);\n'
            ' \\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0) (2.8,0.2)--(3.0,0.2)--(3.0,0);\n'
            ' \\fill (A) circle (1pt) node[above left] {$A$};\n'
            ' \\fill (B) circle (1pt) node[below left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below] {$C$};\n'
            ' \\fill (D) circle (1pt) node[above right] {$D$};\n'
            ' \\fill (E) circle (1pt) node[below right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Vào một thời điểm trong ngày, một chiếc cọc cao $%s\\text{ m}$ cắm thẳng đứng trên mặt đất tạo ra bóng dài $%s\\text{ m}$. Cùng lúc đó, một tòa nhà gần đó có bóng trên mặt đất dài $%s\\text{ m}$. Tính chiều cao của tòa nhà (đơn vị: mét).\\\\
%s''' % (coc_s, bc_s, bong_nha, tikz_code)
        )

        loigiai = (
            '''Mô hình hóa bài toán như hình vẽ, trong đó $AB$ là chiều cao của tòa nhà, $BE = %s\\text{ m}$ là bóng của tòa nhà; $CD = %s\\text{ m}$ là chiều cao chiếc cọc, $CE = %s\\text{ m}$ là bóng của chiếc cọc.\\\\
Vì tòa nhà và chiếc cọc cùng thẳng đứng trên mặt đất nên $AB \\perp BE$ và $CD \\perp BE$, suy ra $CD // AB$.\\\\
Xét $\\Delta ABE$ có $CD // AB$ ($C \\in BE, D \\in AE$), theo định lí về hai tam giác đồng dạng ta có $\\Delta ECD \\backsim \\Delta EBA$.\\\\
Suy ra tỉ số các cạnh tương ứng là:\\\\
$\\frac{CD}{AB} = \\frac{CE}{BE}$.\\\\
Thay các số đo đã biết vào hệ thức trên, ta được:\\\\
$\\frac{%s}{AB} = \\frac{%s}{%s} \\Rightarrow AB = \\frac{%s \\cdot %s}{%s} = %s\\text{ (m)}$.\\\\
Vậy chiều cao của tòa nhà là $%s\\text{ m}$.''' % (
                bong_nha, coc_s, bc_s,
                coc_s, bc_s, bong_nha, coc_s, bong_nha, bc_s, kq_str, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
