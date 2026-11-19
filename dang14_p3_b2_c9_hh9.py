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

def bt_dang14_p3_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        af = randint(3, 9)
        bf = randint(4, 11)
        ce = randint(5, 12)
        ab = af + bf
        bc = bf + ce
        ca = af + ce
        p = af + bf + ce
        kq_str = str(af)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.5);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (I) at (1.62,0.9);
\\coordinate (D) at (1.62,0);
\\coordinate (E) at (2.44,1.25);
\\coordinate (F) at (0.84,1.4);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.9);
\\fill (I) circle (1pt) node[below] {$I$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (F) circle (1pt) node[left] {$F$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác $%s%s%s$ ngoại tiếp đường tròn $(I)$ với các tiếp điểm trên $%s%s, %s%s, %s%s$ lần lượt là $D, E, F$. Biết $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$. Độ dài đoạn thẳng $%sF$ bằng bao nhiêu $\\text{cm}$?%s'''
                         % (A, B, C, B, C, C, A, A, B, A, B, ab, B, C, bc, C, A, ca, A, hinh_ve))

        loigiai = ('''Theo tính chất hai tiếp tuyến cắt nhau của đường tròn $(I)$, ta có:
$$%sE = %sF, \\quad %sD = %sF, \\quad %sD = %sE.$$
Nửa chu vi của tam giác $%s%s%s$ là:
$$p = \\frac{%s%s + %s%s + %s%s}{2} = \\frac{%s + %s + %s}{2} = %s\\text{ (cm)}.$$
Mặt khác, $p = %sF + (%sD + %sD) = %sF + %s%s$.\\\\
Vậy độ dài đoạn thẳng $%sF$ là:
$$%sF = p - %s%s = %s - %s = %s\\text{ (cm)}.$$'''
                   % (A, A, B, B, C, C, A, B, C, A, B, B, C, C, A, ab, bc, ca, p, A, B, C, A, B, C, A, A, B, C, p, bc, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
