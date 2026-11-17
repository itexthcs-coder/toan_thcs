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


def bt_dang3_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cap_ban_kinh = [(9, 4), (16, 9), (25, 4), (25, 9), (16, 1), (36, 9), (18, 8)]
        R1, R2 = random.choice(cap_ban_kinh)
        OO_p = R1 + R2
        hieu_R = R1 - R2
        AB = int(2 * math.sqrt(R1 * R2))
        kq_str = str(AB)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (3.6,0);
\\coordinate (A) at (0.83, 2.04);
\\coordinate (B) at (4.13, 1.31);
\\coordinate (H) at (0.53, 1.31);
\\draw[line width=1pt] (O) circle (2.2cm);
\\draw[line width=1pt] (Op) circle (1.4cm);
\\draw[line width=1pt] (O)--(Op) (O)--(A) (Op)--(B) (A)--(B);
\\draw[line width=1pt, dashed] (Op)--(H);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (Op) circle (1pt) node[below] {$O'$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc ngoài với nhau. Một đường thẳng tiếp xúc với $(O)$ tại $A$ và tiếp xúc với $(O')$ tại $B$ ($A, B$ nằm cùng phía đối với đường thẳng $OO'$). Tính độ dài đoạn thẳng $AB$ (đơn vị: $\\text{cm}$).\\\\
%s''' % (R1, R2, hinhve))

        loigiai = ('''Vì hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc ngoài với nhau nên độ dài đoạn nối tâm là: \\\\
$OO' = R + R' = %s + %s = %s\\text{ (cm)}$. \\\\
Vì đường thẳng $AB$ tiếp xúc với $(O)$ tại $A$ và tiếp xúc với $(O')$ tại $B$ nên $OA \\perp AB$ và $O'B \\perp AB$. \\\\
Kẻ $O'H \\perp OA$ tại $H$. Tứ giác $ABO'H$ có ba góc vuông ($\\widehat{HAB} = \\widehat{ABO'} = \\widehat{O'HA} = 90^\\circ$) nên $ABO'H$ là hình chữ nhật. \\\\
Suy ra $AB = O'H$ và $AH = O'B = %s\\text{ cm}$. \\\\
Do đó $OH = OA - AH = %s - %s = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore vào tam giác $OHO'$ vuông tại $H$, ta có: \\\\
$O'H = \\sqrt{OO'^2 - OH^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s\\text{ (cm)}$. \\\\
Vậy độ dài đoạn thẳng $AB = O'H = %s\\text{ (cm)}$.'''
                   % (R1, R2, R1, R2, OO_p, R2, R1, R2, hieu_R, OO_p, hieu_R, OO_p**2 - hieu_R**2, AB, AB))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
