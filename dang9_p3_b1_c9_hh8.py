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
def bt_dang9_p3_b1_c9_hh8(self):
    # Dạng 9: Đường thẳng qua giao điểm hai đường chéo hình thang song song với hai đáy
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        pairs = [
            (6, 12),
            (4, 12),
            (6, 18),
            (10, 15),
            (12, 24),
            (9, 18),
            (15, 30),
            (8, 24),
        ]
        ab, cd = random.choice(pairs)
        om = Fraction(ab * cd, ab + cd)
        mn = 2 * om
        om_s = fmt_num(om)
        kq_str = fmt_num(mn)
        r_ab_cd = Fraction(ab, cd)
        r_ao_ac = Fraction(ab, ab + cd)
        r_ab_cd_tex = '\\frac{%s}{%s}' % (r_ab_cd.numerator, r_ab_cd.denominator)
        r_ao_ac_tex = '\\frac{%s}{%s}' % (r_ao_ac.numerator, r_ao_ac.denominator)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (A) at (1.1,2.4);\n'
            ' \\coordinate (B) at (2.9,2.4);\n'
            ' \\coordinate (D) at (0,0);\n'
            ' \\coordinate (C) at (4.5,0);\n'
            ' \\coordinate (O) at (intersection of A--C and B--D);\n'
            ' \\coordinate (M) at (intersection of A--D and O--[xshift=-5cm]O);\n'
            ' \\coordinate (N) at (intersection of B--C and O--[xshift=5cm]O);\n'
            ' \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D) (M)--(N);\n'
            ' \\fill (A) circle (1pt) node[above left] {$A$};\n'
            ' \\fill (B) circle (1pt) node[above right] {$B$};\n'
            ' \\fill (C) circle (1pt) node[below right] {$C$};\n'
            ' \\fill (D) circle (1pt) node[below left] {$D$};\n'
            ' \\fill (O) circle (1pt) node[above] {$O$};\n'
            ' \\fill (M) circle (1pt) node[left] {$M$};\n'
            ' \\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Cho hình thang $ABCD$ ($AB // CD$) có $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$. Qua giao điểm $O$ của hai đường chéo, kẻ đường thẳng song song với hai đáy cắt $AD$ và $BC$ lần lượt tại $M$ và $N$. Tính độ dài đoạn thẳng $MN$ (đơn vị: cm).\\\\
%s''' % (ab, cd, tikz_code)
        )

        loigiai = (
            '''Vì $AB // CD$ nên theo chú ý của định lí hai tam giác đồng dạng ta có $\\Delta OAB \\backsim \\Delta OCD$.\\\\
Suy ra $\\frac{OA}{OC} = \\frac{AB}{CD} = \\frac{%s}{%s} = %s$, do đó $\\frac{OA}{OA + OC} = \\frac{OA}{AC} = %s$.\\\\
Xét $\\Delta ADC$ có $OM // CD$ ($M \\in AD, O \\in AC$), theo định lí về hai tam giác đồng dạng ta có $\\Delta AOM \\backsim \\Delta ACD$.\\\\
Suy ra $\\frac{OM}{CD} = \\frac{OA}{AC} = %s \\Rightarrow OM = %s \\cdot %s = %s\\text{ (cm)}$.\\\\
Tương tự, xét $\\Delta BDC$ có $ON // CD$ ($N \\in BC, O \\in BD$) nên $\\Delta BON \\backsim \\Delta BDC$, suy ra $\\frac{ON}{CD} = \\frac{OB}{BD} = %s \\Rightarrow ON = %s\\text{ (cm)}$.\\\\
Vậy độ dài đoạn thẳng $MN$ là:\\\\
$MN = OM + ON = %s + %s = %s\\text{ (cm)}$.''' % (
                ab, cd, r_ab_cd_tex, r_ao_ac_tex,
                r_ao_ac_tex, r_ao_ac_tex, cd, om_s,
                r_ao_ac_tex, om_s,
                om_s, om_s, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
