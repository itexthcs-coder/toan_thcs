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

def bt_dang8_p3_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        k = random.choice([1, 2])
        ab = 10 * k
        bc = 12 * k
        ah = 8 * k
        S = 48 * (k**2)
        p = 16 * k
        r = 3 * k
        R_val = Rational(25 * k, 4)
        oh_val = ah - R_val
        oi_val = abs(r - oh_val)
        kq_str = str(oi_val.p) if oi_val.q == 1 else str(float(oi_val)).replace('.', ',')

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.6);
\\coordinate (B) at (225:1.6);
\\coordinate (C) at (-45:1.6);
\\coordinate (H) at (0,-1.13);
\\coordinate (I) at (0,-0.35);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (I) circle (0.78);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(H);
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (I) circle (1pt) node[right] {$I$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác $%s%s%s$ cân tại $%s$ có $%s%s = %s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$. Gọi $O$ và $I$ lần lượt là tâm đường tròn ngoại tiếp và tâm đường tròn nội tiếp tam giác $%s%s%s$. Độ dài đoạn thẳng $OI$ bằng bao nhiêu $\\text{cm}$?%s'''
                         % (A, B, C, A, A, B, A, C, ab, B, C, bc, A, B, C, hinh_ve))

        loigiai = ('''Gọi $H$ là trung điểm của cạnh $%s%s$, ta có $H%s = %s\\text{ cm}$ và $%sH = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$.\\\\
Vì tam giác $%s%s%s$ cân tại $%s$ nên cả hai tâm $O$ và $I$ đều nằm trên đoạn thẳng $%sH$.\\\\
Diện tích tam giác $%s%s%s$ là $S = \\frac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2)$, nửa chu vi $p = \\frac{%s + %s + %s}{2} = %s\\text{ (cm)}$.\\\\
Suy ra bán kính đường tròn nội tiếp là $r = IH = \\frac{S}{p} = \\frac{%s}{%s} = %s\\text{ (cm)}$.\\\\
Gọi $R$ là bán kính đường tròn ngoại tiếp, ta có:
$$R^2 = (%s - R)^2 + %s^2 \\Leftrightarrow %sR = %s \\Leftrightarrow R = %s\\text{ (cm)}.$$
Suy ra $OH = %s - %s = %s\\text{ (cm)}$. Vậy $OI = IH - OH = %s - %s = %s\\text{ (cm)}$.'''
                   % (B, C, B, bc // 2, A, ab, bc // 2, ah, A, B, C, A, A, A, B, C, ah, bc, S, ab, ab, bc, p, S, p, r, ah, bc // 2, 2 * ah, ab**2, str(float(R_val)).replace('.', ','), ah, str(float(R_val)).replace('.', ','), str(float(oh_val)).replace('.', ','), r, str(float(oh_val)).replace('.', ','), kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
