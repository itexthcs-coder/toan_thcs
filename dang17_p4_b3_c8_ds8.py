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


def bt_dang17_p4_b3_c8_ds8(self):
    # Dạng 17: Bài toán xác suất hình học trên bảng chữ nhật và hình tròn (Có hình vẽ TikZ)
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
        cfg = random.choice([
            (40, 30, 10, 300, 79),
            (50, 30, 10, 400, 84),
            (40, 25, 8, 500, 101),
            (30, 20, 6, 400, 75)
        ])
        dai, rong, r_tron, n_phi, k_trung = cfg
        s_hcn = dai * rong
        r_sq = r_tron * r_tron
        frac_c = Fraction(k_trung, n_phi)
        
        # pi approx (k_trung * s_hcn) / (n_phi * r_sq)
        pi_val = Decimal(k_trung * s_hcn) / Decimal(n_phi * r_sq)
        pi_str = fmt_dec(pi_val, '0.01')
        
        # Tỉ lệ vẽ TikZ cố định chuẩn đẹp màu black, line width 1pt
        tikz_code = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\draw[line width=1pt] (0,0) rectangle (4,3);\n"
            "\\draw[line width=1pt] (2,1.5) circle (1);\n"
            "\\draw[line width=1pt, dashed] (2,1.5)--(3,1.5);\n"
            "\\fill (2,1.5) circle (1pt) node[above] {$O$};\n"
            "\\node[above] at (2.5,1.5) {$R$};\n"
            "\\node[below] at (2,0) {$%s\\text{ cm}$};\n"
            "\\node[left] at (0,1.5) {$%s\\text{ cm}$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        ) % (dai, rong)
        
        noidungcauhoi = ('''Trên một bảng gỗ hình chữ nhật kích thước $%s\\text{ cm} \\times %s\\text{ cm}$, người ta vẽ một hình tròn tâm $O$ bán kính $R = %s\\text{ cm}$ nằm hoàn toàn bên trong bảng gỗ (như hình vẽ). Một người phi tiêu ngẫu nhiên $%s$ lần vào bảng gỗ (giả sử tất cả các phi tiêu đều găm trúng bảng gỗ và bỏ qua kích thước đầu phi tiêu). Quan sát thấy có $%s$ lần mũi tiêu găm vào miền bên trong hình tròn.\\
%s\\
a) Tính xác suất thực nghiệm của biến cố $C$: "Mũi tiêu găm vào miền bên trong hình tròn".\\
b) Biết rằng về mặt lí thuyết, xác suất mũi tiêu găm vào hình tròn bằng tỉ số giữa diện tích hình tròn và diện tích bảng gỗ hình chữ nhật. Từ kết quả thực nghiệm trên, hãy tìm giá trị gần đúng của số $\\pi$ (làm tròn đến chữ số thập phân thứ hai).'''
                         % (dai, rong, r_tron, n_phi, k_trung, tikz_code))
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Trong $%s$ lần phi tiêu, biến cố $C$ xảy ra $%s$ lần.\\
Vậy xác suất thực nghiệm của biến cố $C$ là $\\dfrac{%s}{%s} = \\dfrac{%s}{%s}$.
\\item Diện tích của bảng gỗ hình chữ nhật là: $S_{\\text{HCN}} = %s \\cdot %s = %s$ ($\\text{cm}^2$).\\
Diện tích của hình tròn bán kính $R = %s\\text{ cm}$ là: $S_{\\text{tròn}} = \\pi R^2 = \\pi \\cdot %s^2 = %s\\pi$ ($\\text{cm}^2$).\\
Theo đề bài, xác suất lí thuyết của biến cố $C$ là: $P(C) = \\dfrac{S_{\\text{tròn}}}{S_{\\text{HCN}}} = \\dfrac{%s\\pi}{%s}$.\\
Ước lượng $P(C)$ bằng xác suất thực nghiệm ở câu a, ta có: $\\dfrac{%s\\pi}{%s} \\approx \\dfrac{%s}{%s}$.\\
Suy ra $\\pi \\approx \\dfrac{%s \\cdot %s}{%s \\cdot %s} \\approx %s$.
\\end{enumEX}'''
                   % (n_phi, k_trung, k_trung, n_phi, frac_c.numerator, frac_c.denominator,
                      dai, rong, fmt_int(s_hcn),
                      r_tron, r_tron, r_sq,
                      r_sq, fmt_int(s_hcn),
                      r_sq, fmt_int(s_hcn), k_trung, n_phi,
                      k_trung, fmt_int(s_hcn), n_phi, r_sq, pi_str))

    
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
