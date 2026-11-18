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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang16_p4_b3_c6_ds9(self):
    def fmt_vn(val):
        s = str(val).rstrip('0').rstrip('.') if '.' in str(val) else str(val)
        return s.replace('.', ',')

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        while True:
            r_dm = randint(8, 14)
            d_dm = randint(r_dm + 3, 22)
            if (3 * r_dm) % 2 == 0:
                break
                
        r_m = Decimal(r_dm) / Decimal(10)
        d_m = Decimal(d_dm) / Decimal(10)
        S_kinh = r_m * d_m
        L_nhom = 2*d_m + 3*r_m
        
        S_tong = L_nhom / Decimal(2)
        P_tich = Decimal('1.5') * S_kinh
        delta_val = S_tong**2 - Decimal(4)*P_tich
        sqrt_delta = Decimal(str(math.isqrt(int(delta_val * Decimal(100))))) / Decimal(10)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Một kiến trúc sư thiết kế một khung cửa sổ hình chữ nhật có diện tích kính là $%s\\text{ m}^{2}$. Để viền nhôm xung quanh khung cửa (tính cả $1$ thanh nhôm chia đôi khung cửa theo chiều rộng như hình vẽ), người thợ cần dùng tổng cộng $%s\\text{ m}$ thanh nhôm. Tính chiều dài và chiều rộng của khung cửa sổ đó.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (2.4,0);
\\coordinate (C) at (2.4,3.6);
\\coordinate (D) at (0,3.6);
\\coordinate (M) at (0,1.8);
\\coordinate (N) at (2.4,1.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}'''
                         % (fmt_vn(S_kinh), fmt_vn(L_nhom)))
        
        # Nội dung lời giải
        loigiai = ('''Gọi chiều dài và chiều rộng của khung cửa sổ lần lượt là $a$ (m) và $b$ (m) (điều kiện: $a > b > 0$). \\\\
Vì khung cửa hình chữ nhật có diện tích kính là $%s\\text{ m}^{2}$ nên $ab = %s$. \\\\
Vì khung có $2$ thanh dọc theo chiều dài và $3$ thanh ngang theo chiều rộng nên tổng độ dài thanh nhôm là: \\\\
$2a + 3b = %s \\Leftrightarrow a + 1,5b = %s$. \\\\
Đặt $y = 1,5b$ ($y > 0$). Khi đó ta có: \\\\
$\\begin{cases} a + y = %s \\\\ ay = 1,5ab = 1,5 \\cdot %s = %s \\end{cases}$. \\\\
Do đó, $a$ và $y$ là hai nghiệm của phương trình bậc hai: $X^{2} - %sX + %s = 0$. \\\\
Ta có: $\\Delta = (-%s)^{2} - 4 \\cdot 1 \\cdot %s = %s > 0 \\Rightarrow \\sqrt{\\Delta} = %s$. \\\\
Suy ra phương trình có hai nghiệm phân biệt là $X_{1} = %s$ và $X_{2} = %s$. \\\\
Trường hợp 1: $a = %s$ và $y = %s \\Rightarrow b = \\dfrac{%s}{1,5} = %s$ (thỏa mãn $a > b > 0$). \\\\
Trường hợp 2: $a = %s$ và $y = %s \\Rightarrow b = \\dfrac{%s}{1,5} = %s$ (loại vì $a < b$). \\\\
Vậy chiều dài của khung cửa sổ là $%s\\text{ m}$ và chiều rộng là $%s\\text{ m}$.'''
                   % (fmt_vn(S_kinh), fmt_vn(S_kinh),
                      fmt_vn(L_nhom), fmt_vn(S_tong),
                      fmt_vn(S_tong), fmt_vn(S_kinh), fmt_vn(P_tich),
                      fmt_vn(S_tong), fmt_vn(P_tich),
                      fmt_vn(S_tong), fmt_vn(P_tich), fmt_vn(delta_val), fmt_vn(sqrt_delta),
                      fmt_vn(d_m), fmt_vn(Decimal('1.5')*r_m),
                      fmt_vn(d_m), fmt_vn(Decimal('1.5')*r_m), fmt_vn(Decimal('1.5')*r_m), fmt_vn(r_m),
                      fmt_vn(Decimal('1.5')*r_m), fmt_vn(d_m), fmt_vn(d_m), fmt_vn(d_m / Decimal('1.5')),
                      fmt_vn(d_m), fmt_vn(r_m)))
    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
