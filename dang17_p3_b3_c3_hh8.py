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

def bt_dang17_p3_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_eisenstein = random.choice([(3, 5, 7), (5, 3, 7), (7, 8, 13), (8, 7, 13)])
        ab, ad, ef = bo_eisenstein
        kq_str = str(ef)
        
        bh_rat = Rational(ad, 2)
        str_bh = str(int(bh_rat)) if bh_rat.q == 1 else str(float(bh_rat)).replace('.', ',')
        ch2_rat = Rational(3 * ad**2, 4)
        str_ch2 = str(int(ch2_rat)) if ch2_rat.q == 1 else str(float(ch2_rat)).replace('.', ',')
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (3.2,0);
\\coordinate (D) at (-1.1,-1.9);
\\coordinate (C) at (2.1,-1.9);
\\coordinate (E) at (1.6,2.77);
\\coordinate (F) at (-2.2,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(E)--(B) (A)--(F)--(D) (E)--(F);
\\draw[line width=1pt, dashed] (E)--(C);
\\fill (A) circle (1pt) node[below right] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (E) circle (1pt) node[above] {$E$};
\\fill (F) circle (1pt) node[left] {$F$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có $\\widehat{A} = 120^\\circ$, $AB = %s$ cm, $AD = %s$ cm. Về phía ngoài hình bình hành, dựng hai tam giác đều $ABE$ và $ADF$ (như hình vẽ). Tính độ dài đoạn thẳng $EF$ (đơn vị: cm).
%s''' % (ab, ad, hinh_ve))
        
        loigiai = ('''Ta có $\\widehat{EAF} = 360^\\circ - (\\widehat{DAB} + \\widehat{EAB} + \\widehat{FAD}) = 360^\\circ - (120^\\circ + 60^\\circ + 60^\\circ) = 120^\\circ$. \\\\
Mặt khác, trong hình bình hành $ABCD$, hai góc kề cạnh $AB$ bù nhau nên $\\widehat{ABC} = 180^\\circ - 120^\\circ = 60^\\circ$, suy ra $\\widehat{EBC} = \\widehat{EBA} + \\widehat{ABC} = 60^\\circ + 60^\\circ = 120^\\circ$. \\\\
Xét $\\Delta EAF$ và $\\Delta EBC$ có: $EA = EB = %s$ cm, $\\widehat{EAF} = \\widehat{EBC} = 120^\\circ$, $AF = AD = BC = %s$ cm. \\\\
Do đó $\\Delta EAF = \\Delta EBC$ (c.g.c), suy ra $EF = EC$. \\\\
Kẻ đường cao $CH \\perp EB$ ($H$ thuộc tia đối của tia $EB$), ta có $\\widehat{CBH} = 60^\\circ \\Rightarrow BH = \\frac{1}{2}BC = %s$ cm và $CH^2 = BC^2 - BH^2 = %s^2 - (%s)^2 = %s$. \\\\
Áp dụng định lí Pythagore trong $\\Delta EHC$ vuông tại $H$: $EC^2 = (EB + BH)^2 + CH^2 = (%s + %s)^2 + %s = %s \\Rightarrow EC = %s$ (cm). \\\\
Vậy $EF = %s$ cm.'''
                   % (ab, ad, str_bh, ad, str_bh, str_ch2, ab, str_bh, str_ch2, ef**2, kq_str, kq_str))
        
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
