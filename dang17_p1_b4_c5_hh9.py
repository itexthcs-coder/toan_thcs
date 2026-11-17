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


def bt_dang17_p1_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        oh, half_ab, r_outer = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])
        ab = 2 * half_ab
        r_inner = random.choice([oh - 1, oh, oh + 1])
    
        if oh == r_inner:
            dap_an_dung = 'Tiếp xúc nhau'
            dau_ss = '='
            ket_luan = 'đường thẳng $AB$ tiếp xúc với đường tròn $(O; %s\\text{ cm})$' % r_inner
        elif oh < r_inner:
            dap_an_dung = 'Cắt nhau'
            dau_ss = '<'
            ket_luan = 'đường thẳng $AB$ cắt đường tròn $(O; %s\\text{ cm})$ tại hai điểm phân biệt' % r_inner
        else:
            dap_an_dung = 'Không giao nhau'
            dau_ss = '>'
            ket_luan = 'đường thẳng $AB$ và đường tròn $(O; %s\\text{ cm})$ không giao nhau' % r_inner
    
        # Các đáp án trắc nghiệm
        du = [dap_an_dung]
        da = random.choice(du)
        s = ['Cắt nhau', 'Tiếp xúc nhau', 'Không giao nhau', 'Cắt nhau tại $A$ và $B$']
        s.remove(da)
    
        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)
    
        # Câu hỏi
        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ và dây cung $AB = %s\\text{ cm}$ (như hình vẽ). Xét đường tròn đồng tâm $(O; %s\\text{ cm})$, đường thẳng $AB$ có vị trí tương đối nào đối với $(O; %s\\text{ cm})$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.44,-1.08);
\\coordinate (B) at (1.44,-1.08);
\\coordinate (H) at (0,-1.08);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (-2.2,-1.08)--(2.2,-1.08);
\\draw[line width=1pt, dashed] (O)--(H) (O)--(A);
\\draw[line width=1pt] (0,-0.83)--(0.25,-0.83)--(0.25,-1.08);
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_outer, ab, r_inner, r_inner))
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải
        loigiai = ('''Kẻ $OH \\perp AB$ tại $H$ ($H \\in AB$). Vì tam giác $OAB$ cân tại $O$ ($OA = OB = %s\\text{ cm}$) nên đường cao $OH$ đồng thời là đường trung tuyến.\\\\
Suy ra $AH = \\frac{AB}{2} = \\frac{%s}{2} = %s\\text{ (cm)}$.\\\\
Áp dụng định lí Pythagore vào tam giác $OAH$ vuông tại $H$, ta có:
\\begin{align*}
OH^2 &= OA^2 - AH^2 = %s^2 - %s^2 = %s \\\\
OH &= %s\\text{ (cm)}.
\\end{align*}
Khoảng cách từ tâm $O$ đến đường thẳng $AB$ là $d = OH = %s\\text{ cm}$. So sánh với bán kính $R' = %s\\text{ cm}$ của đường tròn $(O; %s\\text{ cm})$, ta thấy $%s %s %s$ nên $d %s R'$.\\\\
Vậy %s.'''
                   % (r_outer, ab, half_ab, r_outer, half_ab, oh ** 2, oh, oh, r_inner, r_inner, oh, dau_ss, r_inner, dau_ss, ket_luan))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
