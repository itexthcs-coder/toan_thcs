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
def bt_dang11_p3_b1_c9_hh8(self):
    # Dạng 11: Kết hợp tính chất tia phân giác và định lí tam giác đồng dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (6, 9, 10),
            (4, 6, 8),
            (6, 12, 15),
            (8, 12, 15),
            (5, 10, 12),
            (9, 12, 14),
            (6, 10, 12),
            (4, 12, 10),
        ]
        ab, ac, bc = random.choice(cases)
        de = Fraction(ab * ac, ab + ac)
        r_dc_bc = Fraction(ac, ab + ac)
        r_dc_db = Fraction(ac, ab)
        r_dc_db_tex = '\\frac{%s}{%s}' % (r_dc_db.numerator, r_dc_db.denominator)
        r_dc_bc_tex = '\\frac{%s}{%s}' % (r_dc_bc.numerator, r_dc_bc.denominator)
        kq_str = fmt_num(de)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (1.3,2.5);\n'
            ' \\coordinate (B) at (0,0);\n'
            ' \\coordinate (C) at (3.6,0);\n'
            ' \\coordinate (D) at ($(B)!0.4!(C)$);\n'
            ' \\coordinate (E) at ($(C)!0.6!(A)$);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(D) (D)--(E);\n'
            ' \\fill (A) circle (1pt) node[above] {$A$};\n'
            ' \\fill (B) circle (1pt) node[below left] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (D) circle (1pt) node[below] {$D$};\n'
            ' \\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho $\\Delta ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$, $BC = %s\\text{ cm}$. Tia phân giác của góc $A$ cắt $BC$ tại $D$. Qua $D$ kẻ đường thẳng song song với $AB$ cắt $AC$ tại $E$. Tính độ dài đoạn thẳng $DE$ (đơn vị: cm).\\\\
%s''' % (ab, ac, bc, tikz_code)
        )

        loigiai = (
            '''Trong $\\Delta ABC$, vì $AD$ là tia phân giác của góc $A$ nên theo tính chất đường phân giác của tam giác ta có:\\\\
$\\frac{DC}{DB} = \\frac{AC}{AB} = \\frac{%s}{%s} = %s$.\\\\
Suy ra $\\frac{DC}{DB + DC} = \\frac{DC}{BC} = %s$.\\\\
Xét $\\Delta ABC$ có $DE // AB$ ($D \\in BC, E \\in AC$), theo định lí về hai tam giác đồng dạng ta có $\\Delta EDC \\backsim \\Delta ABC$.\\\\
Do đó ta có tỉ số các cạnh tương ứng:\\\\
$\\frac{DE}{AB} = \\frac{DC}{BC} = %s$.\\\\
Thay $AB = %s\\text{ cm}$ vào hệ thức trên, ta được:\\\\
$DE = %s \\cdot %s = %s\\text{ (cm)}$.\\\\
Vậy độ dài đoạn thẳng $DE$ bằng $%s\\text{ cm}$.''' % (
                ac, ab, r_dc_db_tex, r_dc_bc_tex,
                r_dc_bc_tex, ab, r_dc_bc_tex, ab, kq_str, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
