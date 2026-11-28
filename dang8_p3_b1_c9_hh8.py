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
def bt_dang8_p3_b1_c9_hh8(self):
    # Dạng 8: Khai thác hình thang có hai đường chéo cắt nhau tạo thành cặp tam giác đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (4.5, 13.5, 2.5),
            (4, 12, 3),
            (5, 15, 2.5),
            (6, 15, 4),
            (4.5, 9, 3.5),
            (3.5, 10.5, 2),
            (6, 18, 3.5),
            (5, 12.5, 3),
        ]
        ab, cd, oa = random.choice(cases)
        ab_f = Fraction(str(ab))
        cd_f = Fraction(str(cd))
        oa_f = Fraction(str(oa))
        oc_f = oa_f * cd_f / ab_f
        ac_f = oa_f + oc_f
        
        ab_s = fmt_num(ab_f)
        cd_s = fmt_num(cd_f)
        oa_s = fmt_num(oa_f)
        oc_s = fmt_num(oc_f)
        kq_str = fmt_num(ac_f)
        ratio_f = ab_f / cd_f
        ratio_tex = '\\frac{%s}{%s}' % (ratio_f.numerator, ratio_f.denominator)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (1.0,2.2);\n'
            ' \\coordinate (B) at (2.8,2.2);\n'
            ' \\coordinate (D) at (0,0);\n'
            ' \\coordinate (C) at (4.4,0);\n'
            ' \\coordinate (O) at (intersection of A--C and B--D);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D);\n'
            ' \\fill (A) circle (1pt) node[above left] {$A$};\n'
            ' \\fill (B) circle (1pt) node[above right] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (D) circle (1pt) node[below left] {$D$};\n'
            ' \\fill (O) circle (1pt) node[above] {$O$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho hình thang $ABCD$ ($AB // CD$) có đáy nhỏ $AB = %s\\text{ cm}$, đáy lớn $CD = %s\\text{ cm}$. Hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Biết $OA = %s\\text{ cm}$, tính độ dài đoạn thẳng $AC$ (đơn vị: cm).\\\\
%s''' % (ab_s, cd_s, oa_s, tikz_code)
        )

        loigiai = (
            '''Xét $\\Delta OCD$ có đường thẳng $AB$ cắt phần kéo dài của hai cạnh $OC, OD$ lần lượt tại $A, B$ và $AB // CD$.\\\\
Theo chú ý của định lí về hai tam giác đồng dạng, ta có $\\Delta OAB \\backsim \\Delta OCD$.\\\\
Suy ra tỉ số các cạnh tương ứng là:\\\\
$\\frac{OA}{OC} = \\frac{AB}{CD} = \\frac{%s}{%s} = %s$.\\\\
Thay $OA = %s\\text{ cm}$ vào hệ thức trên, ta được:\\\\
$\\frac{%s}{OC} = %s \\Rightarrow OC = \\frac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\\
Vì điểm $O$ nằm giữa $A$ và $C$ nên độ dài đoạn thẳng $AC$ là:\\\\
$AC = OA + OC = %s + %s = %s\\text{ (cm)}$.''' % (
                ab_s, cd_s, ratio_tex, oa_s,
                oa_s, ratio_tex, oa_s, ratio_f.denominator, ratio_f.numerator, oc_s,
                oa_s, oc_s, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
