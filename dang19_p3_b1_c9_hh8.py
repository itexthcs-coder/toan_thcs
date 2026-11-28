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
def bt_dang19_p3_b1_c9_hh8(self):
    # Dạng 19 (Thực tế): Bài toán chiếu sáng (mô hình đèn chiếu tạo bóng trên tường)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cases = [
            (4, Fraction(3, 2), 30),
            (5, Fraction(2, 1), 24),
            (3, Fraction(6, 5), 28),
            (4, Fraction(8, 5), 32),
            (6, Fraction(3, 2), 25),
            (5, Fraction(5, 2), 35),
            (4, Fraction(1, 1), 22),
            (6, Fraction(2, 1), 27),
        ]
        tuong_m, bia_m, day_bia_cm = random.choice(cases)
        day_bong_cm = day_bia_cm * tuong_m / bia_m
        bia_s = fmt_num(bia_m)
        r_f = bia_m / Fraction(tuong_m, 1)
        r_tex = '\\frac{%s}{%s}' % (r_f.numerator, r_f.denominator)
        kq_str = fmt_num(day_bong_cm)

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            ' \\coordinate (O) at (0,1.4);\n'
            ' \\coordinate (B) at (4.5,0);\n'
            ' \\coordinate (C) at (4.5,2.8);\n'
            ' \\coordinate (M) at ($(O)!0.4!(B)$);\n'
            ' \\coordinate (N) at ($(O)!0.4!(C)$);\n'
            ' \\draw[line width=1pt] (O)--(B)--(C)--cycle (M)--(N);\n'
            ' \\fill (O) circle (1pt) node[left] {$O$};\n'
            ' \\fill (B) circle (1pt) node[below right] {$B$};\n'
            ' \\fill (C) circle (1pt) node[above right] {$C$};\n'
            ' \\fill (M) circle (1pt) node[below] {$M$};\n'
            ' \\fill (N) circle (1pt) node[above] {$N$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            '''Một đèn pin đặt tại điểm $O$ trên sàn nhà chiếu thẳng về phía một bức tường cách đèn $%s\\text{ m}$. Một người cầm một tấm bìa hình tam giác có cạnh đáy $%s\\text{ cm}$ đặt song song với bức tường và cách đèn pin $%s\\text{ m}$. Tính độ dài cạnh đáy tương ứng của bóng tấm bìa in trên bức tường (đơn vị: cm).\\\\
%s''' % (tuong_m, day_bia_cm, bia_s, tikz_code)
        )

        loigiai = (
            '''Xét mặt phẳng chứa tia sáng đi qua đèn pin $O$ và hai đầu mút cạnh đáy của tấm bìa ($M, N$) tạo thành hai đầu mút cạnh đáy của bóng trên tường ($B, C$).\\\\
Vì tấm bìa đặt song song với bức tường nên $MN // BC$.\\\\
Xét $\\Delta OBC$ có $MN // BC$ ($M \\in OB, N \\in OC$), theo định lí về hai tam giác đồng dạng ta có $\\Delta OMN \\backsim \\Delta OBC$.\\\\
Tỉ số khoảng cách từ đèn pin $O$ đến tấm bìa và đến bức tường cũng chính là tỉ số đồng dạng của hai tam giác này:\\\\
$\\frac{MN}{BC} = \\frac{%s}{%s} = %s$.\\\\
Thay $MN = %s\\text{ cm}$ vào hệ thức trên, ta được:\\\\
$\\frac{%s}{BC} = %s \\Rightarrow BC = \\frac{%s \\cdot %s}{%s} = %s\\text{ (cm)}$.\\\\
Vậy độ dài cạnh đáy tương ứng của bóng tấm bìa in trên bức tường là $%s\\text{ cm}$.''' % (
                bia_s, tuong_m, r_tex, day_bia_cm,
                day_bia_cm, r_tex, day_bia_cm, r_f.denominator, r_f.numerator, kq_str, kq_str
            )
        )

        dapan = '\\shortans[0]{$%s$}\n' % kq_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
