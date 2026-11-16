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


def bt_dang17_p3_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = randint(6, 16)
        dh = randint(3, 10)
        cd = ab + 2 * dh
        ad = 2 * dh
        kq_str = str(ad)

        # Hình vẽ TikZ
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (5,0);
    \\coordinate (H) at (1.2,0);
    \\coordinate (K) at (3.8,0);
    \\coordinate (A) at (1.2,2.1);
    \\coordinate (B) at (3.8,2.1);
    \\draw[line width=1pt] (D)--(C)--(B)--(A)--cycle;
    \\draw[line width=1pt, dashed] (A)--(H) (B)--(K);
    \\draw[line width=1pt] (1.2,0.3)--(1.5,0.3)--(1.5,0);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[above right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (H) circle (1pt) node[below] {$H$};
    \\fill (K) circle (1pt) node[below] {$K$};
    \\node[above] at (2.5,2.1) {$%s\\text{ cm}$};
    \\node[below] at (2.5,-0.25) {$%s\\text{ cm}$};
    \\node[above right] at (0.15,0) {$60^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (str(ab), str(cd)))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$) có đáy nhỏ $AB = %s\\text{ cm}$, đáy lớn $CD = %s\\text{ cm}$ và góc ở đáy $\\widehat{D} = 60^\\circ$. Tính độ dài cạnh bên $AD$ của hình thang cân (đơn vị: $\\text{cm}$). %s'''
                         % (str(ab), str(cd), hinh_ve))

        # Nội dung lời giải
        loigiai = ('''Kẻ các đường cao $AH \\perp CD$ và $BK \\perp CD$ ($H, K \\in CD$). \\\\
Vì $ABCD$ là hình thang cân có $AB // CD$ nên tứ giác $ABKH$ là hình chữ nhật, suy ra $HK = AB = %s\\text{ cm}$ và $DH = KC$. \\\\
Do đó $DH = \\dfrac{CD - HK}{2} = \\dfrac{%s - %s}{2} = %s\\text{ (cm)}$. \\\\
Xét tam giác $AHD$ vuông tại $H$, ta có: \\\\
$\\cos D = \\dfrac{DH}{AD}$. \\\\
Suy ra $AD = \\dfrac{DH}{\\cos 60^\\circ} = \\dfrac{%s}{\\dfrac{1}{2}} = %s\\text{ (cm)}$.'''
                   % (str(ab), str(cd), str(ab), str(dh), str(dh), kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \end{minipage} \n\n')
    return content
