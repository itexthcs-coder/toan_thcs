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


def bt_dang4_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R2 = randint(3, 6)
        k = randint(2, 4)
        R1 = k * R2
        PO_p = randint(6, 15)
        OO_p = (k - 1) * PO_p
        while OO_p <= R1 + R2:
            PO_p += 3
            OO_p = (k - 1) * PO_p
        kq_str = str(PO_p)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (3.2,0);
\\coordinate (P) at (6.4,0);
\\coordinate (A) at (0.56, 1.71);
\\coordinate (B) at (3.48, 0.85);
\\draw[line width=1pt] (O) circle (1.8cm);
\\draw[line width=1pt] (Op) circle (0.9cm);
\\draw[line width=1pt] (O)--(P) (A)--(P) (O)--(A) (Op)--(B);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (Op) circle (1pt) node[below] {$O'$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ ở ngoài nhau với $OO' = %s\\text{ cm}$. Tiếp tuyến chung ngoài $d$ tiếp xúc với $(O)$ tại $A$, tiếp xúc với $(O')$ tại $B$ và cắt tia $OO'$ tại $P$. Tính độ dài đoạn thẳng $PO'$ (đơn vị: $\\text{cm}$).\\\\
%s''' % (R1, R2, OO_p, hinhve))

        loigiai = ('''Vì đường thẳng $d$ tiếp xúc với $(O)$ tại $A$ và tiếp xúc với $(O')$ tại $B$ nên $OA \\perp d$ và $O'B \\perp d$. \\\\
Suy ra $O'B // OA$. \\\\
Xét tam giác $POA$ có $O'B // OA$, theo hệ quả của định lí Thalès (hoặc hai tam giác đồng dạng $\\triangle PO'B \\sim \\triangle POA$), ta có: \\\\
$\\dfrac{PO'}{PO} = \\dfrac{O'B}{OA} = \\dfrac{%s}{%s} = \\dfrac{1}{%s}$. \\\\
Suy ra $PO = %s PO'$. \\\\
Vì $P$ nằm trên tia $OO'$ và $R > R'$ nên $O'$ nằm giữa $O$ và $P$, do đó $PO = PO' + OO'$. \\\\
Thay $OO' = %s\\text{ cm}$ và $PO = %s PO'$, ta được: \\\\
$%s PO' = PO' + %s \\Leftrightarrow %s PO' = %s \\Leftrightarrow PO' = %s\\text{ (cm)}$.'''
                   % (R2, R1, k, k, OO_p, k, k, OO_p, k - 1, OO_p, PO_p))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
