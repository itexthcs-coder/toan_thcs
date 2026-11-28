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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def fmt_so(val):
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        if val < 0:
            return '-\\frac{%s}{%s}' % (abs(val.numerator), val.denominator)
        return '\\frac{%s}{%s}' % (val.numerator, val.denominator)
    if isinstance(val, float):
        s = ('%g' % val).replace('.', ',')
        return s
    return str(val)

def fmt_dt(a, b):
    if a == 1:
        sa = 'x'
    elif a == -1:
        sa = '-x'
    else:
        sa = '%sx' % fmt_so(a)
    if b == 0:
        return sa
    elif b > 0:
        return '%s + %s' % (sa, fmt_so(b))
    else:
        return '%s - %s' % (sa, fmt_so(abs(b)))

def bt_dang19_p4_b5_c7_ds8(self):
    # Dạng 19: Bài toán thực tế về chuyển động đều (song song = không đuổi kịp, cắt nhau = đuổi kịp)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        s0 = random.choice([15, 20, 30])
        v_xm = random.choice([35, 40, 45])
        t_duoi = random.choice([1, 2])
        v_oto = v_xm + s0 // t_duoi
        gio_xp = random.choice([6, 7, 8])
        gio_gap = gio_xp + t_duoi
        
        tikz_hinh = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (0,0) -- (4.5,0) node[below] {$t$ (giờ)};\n'
            '\\draw[->, line width=1pt] (0,0) -- (0,3.8) node[left] {$s$ (km)};\n'
            '\\draw[line width=1pt] (0,0.9) -- (4,3.1) node[right] {Xe máy};\n'
            '\\draw[line width=1pt] (0,0) -- (3.6,3.4) node[right] {Ô tô};\n'
            '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
            '\\fill (2.28,2.15) circle (1pt) node[above left] {$G$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Lúc $%s$ giờ sáng, một xe máy xuất phát từ địa điểm $A$ cách bến xe trung tâm $O$ là $%s\\text{ km}$ và đi về phía tỉnh $B$ (cùng chiều dương trục tọa độ $Ox$ gốc tại $O$) với vận tốc không đổi $%s\\text{ km/h}$. Cùng lúc đó, một ô tô xuất phát từ bến xe trung tâm $O$ cũng đi về phía tỉnh $B$ với vận tốc $v\\text{ (km/h)}$ ($v > 0$). Gọi $s$ (km) là khoảng cách từ mỗi xe đến bến xe $O$ sau $t$ giờ kể từ lúc $%s$ giờ sáng.\\\n'
            'a) Lập hàm số biểu diễn khoảng cách $s$ theo thời gian $t$ của xe máy và ô tô.\\\n'
            'b) Với giá trị nào của vận tốc $v$ thì đồ thị biểu diễn chuyển động của hai xe là hai đường thẳng song song? Điều này có ý nghĩa gì về khả năng đuổi kịp nhau của hai xe?\\\n'
            'c) Nếu ô tô đi với vận tốc $v = %s\\text{ km/h}$, hỏi lúc mấy giờ thì ô tô đuổi kịp xe máy?'
            % (gio_xp, s0, v_xm, gio_xp, v_oto)
        )
        
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Sau $t$ giờ, xe máy đi được quãng đường là $%st$ (km), cộng với khoảng cách ban đầu $%s$ km nên khoảng cách từ xe máy đến $O$ là: $s_1 = %st + %s$.\\\n'
            'Sau $t$ giờ, ô tô xuất phát từ $O$ đi được quãng đường là $vt$ (km) nên khoảng cách từ ô tô đến $O$ là: $s_2 = vt$.\n'
            '\\item Đồ thị biểu diễn chuyển động của hai xe là hai đường thẳng song song khi và chỉ khi $\\begin{cases} v = %s \\\\ 0 \\neq %s \\end{cases} \\Leftrightarrow v = %s\\text{ (km/h)}$.\\\n'
            'Ý nghĩa thực tế: Khi hai xe chạy cùng vận tốc $%s\\text{ km/h}$ thì khoảng cách giữa hai xe luôn không đổi bằng $%s\\text{ km}$, hai đường thẳng biểu diễn không có điểm chung nên ô tô không bao giờ đuổi kịp xe máy.\n'
            '\\item Với $v = %s\\text{ km/h}$, ta có $s_2 = %st$. Ô tô đuổi kịp xe máy khi $s_1 = s_2 \\Leftrightarrow %st + %s = %st \\Leftrightarrow %st = %s \\Leftrightarrow t = %s$ (giờ).\\\n'
            'Vậy ô tô đuổi kịp xe máy lúc $%s + %s = %s$ giờ sáng.%s\n'
            '\\end{enumEX}'
            % (v_xm, s0, v_xm, s0,
               v_xm, s0, v_xm, v_xm, s0,
               v_oto, v_oto, v_xm, s0, v_oto, v_oto - v_xm, s0, t_duoi, gio_xp, t_duoi, gio_gap, tikz_hinh)
        )
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
