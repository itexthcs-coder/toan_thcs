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


def bt_dang2_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [
            (15, 13, 14, 12),
            (20, 15, 25, 12),
            (25, 17, 28, 15),
            (30, 26, 28, 24),
            (10, 17, 21, 8)
        ]
        R1, R2, d, h = random.choice(bo_so)
        AB = 2 * h
        p = (R1 + R2 + d) // 2
        S = int(math.sqrt(p * (p - R1) * (p - R2) * (p - d)))
        kq_str = str(AB)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (3.2,0);
\\coordinate (H) at (2.05,0);
\\coordinate (A) at (2.05,1.65);
\\coordinate (B) at (2.05,-1.65);
\\draw[line width=1pt] (O) circle (2.63cm);
\\draw[line width=1pt] (Op) circle (2.01cm);
\\draw[line width=1pt] (O)--(Op) (A)--(B) (O)--(A) (Op)--(A);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (Op) circle (1pt) node[right] {$O'$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ cắt nhau tại hai điểm $A$ và $B$, biết độ dài đoạn nối tâm $OO' = %s\\text{ cm}$. Tính độ dài dây chung $AB$ (đơn vị: $\\text{cm}$).\\\\
%s''' % (R1, R2, d, hinhve))

        loigiai = ('''Gọi $H$ là giao điểm của đoạn nối tâm $OO'$ và dây chung $AB$. \\\\
Vì hai đường tròn $(O)$ và $(O')$ cắt nhau tại $A$ và $B$ nên đường nối tâm $OO'$ là đường trung trực của đoạn thẳng $AB$. \\\\
Suy ra $OO' \\perp AB$ tại $H$ và $H$ là trung điểm của $AB$, do đó $AB = 2AH$. \\\\
Xét tam giác $OAO'$ có $OA = %s\\text{ cm}$, $O'A = %s\\text{ cm}$ và $OO' = %s\\text{ cm}$. \\\\
Nửa chu vi tam giác $OAO'$ là: $p = \\dfrac{%s + %s + %s}{2} = %s\\text{ (cm)}$. \\\\
Theo công thức Heron, diện tích tam giác $OAO'$ là: \\\\
$S_{OAO'} = \\sqrt{p(p - OA)(p - O'A)(p - OO')} = \\sqrt{%s \\cdot (%s - %s) \\cdot (%s - %s) \\cdot (%s - %s)} = %s\\text{ (cm}^2\\text{)}$. \\\\
Mặt khác, $S_{OAO'} = \\dfrac{1}{2} \\cdot AH \\cdot OO' \\Rightarrow AH = \\dfrac{2 S_{OAO'}}{OO'} = \\dfrac{2 \\cdot %s}{%s} = %s\\text{ (cm)}$. \\\\
Vậy độ dài dây chung $AB = 2 \\cdot %s = %s\\text{ (cm)}$.'''
                   % (R1, R2, d, R1, R2, d, p, p, p, R1, p, R2, p, d, S, S, d, h, h, AB))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
