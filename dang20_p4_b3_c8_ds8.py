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


def bt_dang20_p4_b3_c8_ds8(self):
    # Dạng 20: Bài toán tọa độ trên mặt phẳng Oxy kết hợp xác suất (Có hình vẽ TikZ)
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        def fmt_int(n):
            return '{:,}'.format(int(n)).replace(',', '\\,')
        
        def fmt_dec(val, places=None):
            if places is not None:
                d = Decimal(str(val)).quantize(Decimal(places), rounding=ROUND_HALF_UP)
                s = format(d, 'f')
            else:
                s = str(val)
            return s.replace('.', ',')
        
        def round_int(val):
            return int(Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        
        def round_ten(val):
            return int(Decimal(str(val)).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
        tap_s = [-2, -1, 0, 1, 2, 3]
        hs_cfg = random.choice([
            (2, -1, "y = 2x - 1"),
            (1, 1, "y = x + 1"),
            (-1, 1, "y = -x + 1"),
            (2, 1, "y = 2x + 1")
        ])
        he_a, he_b, str_hs = hs_cfg
        
        all_pts = [(a, b) for a in tap_s for b in tap_s]
        tot_pts = len(all_pts) # 36
        
        pts_p = [(a, b) for (a, b) in all_pts if b == he_a * a + he_b]
        pts_q = [(a, b) for (a, b) in all_pts if a < 0 and b > 0]
        
        frac_p = Fraction(len(pts_p), tot_pts)
        frac_q = Fraction(len(pts_q), tot_pts)
        
        str_pts_p = "; ".join("(%s; %s)" % (a, b) for (a, b) in pts_p)
        str_pts_q = "; ".join("(%s; %s)" % (a, b) for (a, b) in pts_q)
        
        # Vẽ hệ trục tọa độ Oxy minh họa 4 góc phần tư bằng TikZ màu black, nét 1pt
        tikz_oxy = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt, ->] (-3,0)--(4,0) node[below] {$x$};\n"
            "\\draw[line width=1pt, ->] (0,-3)--(0,4) node[left] {$y$};\n"
            "\\fill (0,0) circle (1pt) node[below left] {$O$};\n"
            "\\node at (2,2.2) {Góc phần tư I};\n"
            "\\node at (-1.8,2.2) {Góc phần tư II};\n"
            "\\node at (-1.8,-1.8) {Góc phần tư III};\n"
            "\\node at (2,-1.8) {Góc phần tư IV};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )
        
        noidungcauhoi = ('''Cho tập hợp $S = \\{-2; -1; 0; 1; 2; 3\\}$. Chọn ngẫu nhiên một số $a \\in S$ làm hoành độ và một số $b \\in S$ làm tung độ để tạo thành điểm $M(a; b)$ trên mặt phẳng tọa độ $Oxy$ ($a$ và $b$ có thể giống nhau).\\
%s\\
a) Có bao nhiêu điểm $M(a; b)$ khác nhau có thể được tạo thành?\\
b) Tính xác suất của biến cố $P$: "Điểm $M(a; b)$ nằm trên đồ thị của hàm số bậc nhất $%s$".\\
c) Tính xác suất của biến cố $Q$: "Điểm $M(a; b)$ nằm ở góc phần tư thứ II của mặt phẳng tọa độ".'''
                         % (tikz_oxy, str_hs))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tập hợp $S$ có $6$ phần tử.\\
- Có $6$ cách chọn hoành độ $a \\in S$.\\
- Với mỗi cách chọn $a$, có $6$ cách chọn tung độ $b \\in S$.\\
Vậy có tất cả $6 \\cdot 6 = %s$ điểm $M(a; b)$ khác nhau có thể được tạo thành. Các kết quả này là đồng khả năng.
\\item Điểm $M(a; b)$ nằm trên đồ thị của hàm số $%s$ khi và chỉ khi $b = %s$.\\
Thay lần lượt các giá trị $a \\in S$ vào công thức hàm số, ta tìm được $%s$ điểm thỏa mãn là: $%s$.\\
Vậy xác suất của biến cố $P$ là $P(P) = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\item Điểm $M(a; b)$ nằm ở góc phần tư thứ II của mặt phẳng tọa độ $Oxy$ khi và chỉ khi $a < 0$ và $b > 0$.\\
Do $a, b \\in S$ nên $a \\in \\{-2; -1\\}$ ($2$ cách chọn) và $b \\in \\{1; 2; 3\\}$ ($3$ cách chọn).\\
Có $%s$ điểm thuận lợi cho biến cố $Q$ là: $%s$.\\
Vậy xác suất của biến cố $Q$ là $P(Q) = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\end{enumEX}'''
                   % (tot_pts,
                      str_hs, str_hs.split('= ')[1], len(pts_p), str_pts_p,
                      len(pts_p), tot_pts, frac_p.numerator, frac_p.denominator,
                      len(pts_q), str_pts_q,
                      len(pts_q), tot_pts, frac_q.numerator, frac_q.denominator))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
