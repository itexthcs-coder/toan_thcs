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


def bt_dang20_p4_b4_c6_ds9(self):
    def fmt_vn(val):
        s = f"{val.normalize():f}"
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        t1_dec = random.choice([Decimal('1.7'), Decimal('3.4')])
        do_sau_dec = Decimal('5') * (t1_dec**2)
        t_am_dec = do_sau_dec / Decimal('340')
        tong_t_dec = t1_dec + t_am_dec

        c_pt = int(Decimal('340') * tong_t_dec)
        a_pt = 20
        b_pt = 1360
        c_pt_4 = -4 * c_pt
        g = math.gcd(a_pt, math.gcd(b_pt, abs(c_pt_4)))
        a_pt //= g
        b_pt //= g
        c_pt_4 //= g

        delta = b_pt**2 - 4 * a_pt * c_pt_4
        can_delta = int(math.isqrt(delta))
        x_am = Decimal(-b_pt - can_delta) / Decimal(2 * a_pt)

        tong_t_str = fmt_vn(tong_t_dec)
        t1_str = fmt_vn(t1_dec)
        do_sau_str = fmt_vn(do_sau_dec)
        x_am_str = fmt_vn(x_am)

        noidungcauhoi = ('''Để đo độ sâu của một giếng nước cạn, người ta thả rơi tự do một viên sỏi từ miệng giếng và đo thời gian kể từ lúc thả đến khi nghe thấy tiếng viên sỏi chạm đáy giếng vang lên. Biết quãng đường rơi tự do của viên sỏi là $s = 5t^2\\text{ (m)}$ (với $t$ là thời gian rơi tính bằng giây) và vận tốc truyền âm thanh trong không khí là $340\\text{ m/s}$. Tổng thời gian từ lúc thả viên sỏi đến khi nghe thấy tiếng động là $%s$ giây. \\\\
a) Tính thời gian viên sỏi rơi từ miệng giếng xuống đến đáy giếng. \\\\
b) Tính độ sâu của giếng nước đó. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,0) -- (0,-3.2) -- (1.8,-3.2) -- (1.8,0);
\\draw[line width=1pt, dashed] (0,0) -- (1.8,0);
\\fill (0.9,-0.4) circle (1.5pt) node[right] {Viên sỏi};
\\draw[line width=1pt, ->] (0.9,-0.6) -- (0.9,-2.9);
\\node[right] at (1.8,-1.6) {$h$};
\\end{tikzpicture}
\\end{center}'''
                         %(tong_t_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $x$ (giây) là thời gian viên sỏi rơi từ miệng giếng xuống đáy giếng. Điều kiện: $0 < x < %s$. \\\\
Khi đó độ sâu của giếng là $h = 5x^2\\text{ (m)}$. \\\\
Thời gian âm thanh truyền từ đáy giếng lên đến miệng giếng là $\\frac{h}{340} = \\frac{5x^2}{340} = \\frac{x^2}{68}$ (giây). \\\\
Vì tổng thời gian từ lúc thả viên sỏi đến khi nghe thấy tiếng động là $%s$ giây nên ta có phương trình: \\\\
$x + \\frac{x^2}{68} = %s$. \\\\
Quy đồng mẫu và biến đổi về dạng phương trình bậc hai hệ số nguyên, ta được: \\\\
$%s = 0$. \\\\
Ta có: $\\Delta = %s^2 - 4 \\cdot %s \\cdot (%s) = %s$, $\\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt: \\\\
$x_1 = %s$ (loại); \\quad $x_2 = %s$ (thoả mãn điều kiện). \\\\
Vậy thời gian viên sỏi rơi từ miệng giếng xuống đáy giếng là $%s$ giây.
\\item Độ sâu của giếng nước đó là: $h = 5 \\cdot (%s)^2 = %s\\text{ (m)}$.
\\end{enumEX}'''
                   %(tong_t_str, tong_t_str, tong_t_str,
                     latex(a_pt * x**2 + b_pt * x + c_pt_4),
                     latex(b_pt), latex(a_pt), latex(c_pt_4), latex(delta), latex(can_delta),
                     x_am_str, t1_str, t1_str,
                     t1_str, do_sau_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
