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


def bt_dang17_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (2.6,2.6);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at (0.8,2.6);
\\coordinate (N) at (2.6,1.8);
\\coordinate (P) at (1.8,0);
\\coordinate (Q) at (0,0.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N)--(P)--(Q)--cycle;
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[below] {$P$};
\\fill (Q) circle (1pt) node[left] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình vuông $ABCD$ có cạnh bằng $a$. Trên các cạnh $AB, BC, CD, DA$ lần lượt lấy các điểm $M, N, P, Q$ sao cho $AM = BN = CP = DQ = x$ ($0 < x < a$). \\\\
a) Chứng minh tứ giác $MNPQ$ là hình vuông. \\\\
b) Tìm vị trí của các điểm $M, N, P, Q$ (xác định $x$ theo $a$) để diện tích hình vuông $MNPQ$ đạt giá trị nhỏ nhất và tính giá trị nhỏ nhất đó theo $a$.%s'''
                         % (hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Ta có $AQ = AD - DQ = a - x$, $BM = AB - AM = a - x$, $CN = BC - BN = a - x$, $DP = CD - CP = a - x$.\\\\
Xét bốn tam giác vuông $\\Delta AMQ, \\Delta BNM, \\Delta CPN, \\Delta DQP$ có các cặp cạnh góc vuông tương ứng bằng nhau ($x$ và $a - x$) nên bằng nhau theo trường hợp (c.g.c).\\\\
Suy ra $MQ = MN = NP = PQ$, do đó tứ giác $MNPQ$ là hình thoi.\\\\
Lại có $\\widehat{QMN} = 180^\\circ - (\widehat{AMQ} + \\widehat{BMN}) = 180^\\circ - (\widehat{AMQ} + \\widehat{AQM}) = 180^\\circ - 90^\\circ = 90^\\circ$.\\\\
Hình thoi $MNPQ$ có một góc vuông nên là hình vuông.
\\item Áp dụng định lí Pythagore vào $\\Delta AMQ$ vuông tại $A$, diện tích hình vuông $MNPQ$ là:\\\\
$S_{MNPQ} = MQ^2 = AM^2 + AQ^2 = x^2 + (a - x)^2 = 2x^2 - 2ax + a^2 = 2\\left(x - \\dfrac{a}{2}\\right)^2 + \\dfrac{a^2}{2}$.\\\\
Vì $2\\left(x - \\dfrac{a}{2}\\right)^2 \\ge 0$ với mọi $x$ nên $S_{MNPQ} \\ge \\dfrac{a^2}{2}$.\\\\
Dấu bằng xảy ra khi $x = \\dfrac{a}{2}$, tức là $M, N, P, Q$ lần lượt là trung điểm của các cạnh $AB, BC, CD, DA$.\\\\
Vậy giá trị nhỏ nhất của diện tích hình vuông $MNPQ$ bằng $\\dfrac{a^2}{2}$.
\\end{enumEX} \n''')

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
