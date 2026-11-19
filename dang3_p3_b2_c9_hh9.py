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

def bt_dang3_p3_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        bo_pytago = [(3, 4, 5), (6, 8, 10), (9, 12, 15), (12, 16, 20), (5, 12, 13)]
        ab, ac, bc = random.choice(bo_pytago)
        R_val = Rational(bc, 2)
        og_val = Rational(bc, 6)
        number = Decimal(str(float(og_val)))
        if og_val.q == 1:
            kq_str = str(og_val.p)
        elif og_val.q in (2, 4, 5):
            kq_str = str(float(og_val)).replace('.', ',')
        else:
            kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq).replace('.', ',')

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (B) at (-1.6,0);
\\coordinate (C) at (1.6,0);
\\coordinate (A) at (125:1.6);
\\coordinate (G) at ($(O)!0.333!(A)$);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (A)--(O);
\\draw[line width=1pt] ($(A)!0.15!(B)$)--($(A)!0.15!(B)!0.15!90:(B)$)--($(A)!0.15!(C)$);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (G) circle (1pt) node[right] {$G$};
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (C) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ có $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$. Gọi $O$ là tâm đường tròn ngoại tiếp và $G$ là trọng tâm của tam giác $%s%s%s$. Độ dài đoạn thẳng $OG$ bằng bao nhiêu $\\text{cm}$ (nếu kết quả là số thập phân vô hạn thì làm tròn đến hàng phần trăm)?%s'''
                         % (A, B, C, A, A, B, ab, A, C, ac, A, B, C, hinh_ve))

        loigiai = ('''Áp dụng định lí Pythagore vào tam giác $%s%s%s$ vuông tại $%s$, ta có:
$$%s%s = \\sqrt{%s%s^2 + %s%s^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}.$$
Vì tam giác $%s%s%s$ vuông tại $%s$ nên tâm $O$ của đường tròn ngoại tiếp là trung điểm của cạnh huyền $%s%s$, suy ra trung tuyến $%sO = R = \\frac{%s}{2} = %s\\text{ (cm)}$.\\\\
Vì $G$ là trọng tâm của tam giác $%s%s%s$ nên $G$ nằm trên đoạn $%sO$ và $OG = \\frac{1}{3}%sO = \\frac{%s}{3} = %s \\approx %s\\text{ (cm)}$.'''
                   % (A, B, C, A, B, C, A, B, A, C, ab, ac, bc, A, B, C, A, B, C, A, bc, latex(R_val), A, B, C, A, A, latex(R_val), latex(og_val), str(kq_str)))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
