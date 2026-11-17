# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:27:56 2024

@author: Pham Ngoc Chien
"""
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

def bt_dang7_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        goc_mon = randint(45, 82)
        sd_ac_nho = 2 * goc_mon
        sd_ac_lon = 360 - sd_ac_nho

        noidungcauhoi = ('''Cho ba điểm $A, B, C$ phân biệt cùng thuộc đường tròn $(O)$ sao cho điểm $B$ nằm trên cung nhỏ $\\overparen{AC}$. Gọi $M$ là điểm chính giữa của cung nhỏ $\\overparen{AB}$ và $N$ là điểm chính giữa của cung nhỏ $\\overparen{BC}$ (như hình vẽ).\\\\
                         a) Chứng minh rằng $\\text{sđ}\\overparen{MBN} = \\dfrac{1}{2}\\text{sđ}\\overparen{AC}_{\\text{nhỏ}}$.\\\\
                         b) Biết $\\widehat{MON} = %s^\\circ$, hãy tính số đo của cung lớn $\\overparen{AC}$.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (10:1.8);
                         \\coordinate (M) at (40:1.8);
                         \\coordinate (B) at (70:1.8);
                         \\coordinate (N) at (110:1.8);
                         \\coordinate (C) at (150:1.8);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (A)--(O)--(C) (O)--(B) (O)--(M) (O)--(N);
                         \\fill (O) circle (1pt) node[below] {$O$};
                         \\fill (A) circle (1pt) node[right] {$A$};
                         \\fill (M) circle (1pt) node[above right] {$M$};
                         \\fill (B) circle (1pt) node[above] {$B$};
                         \\fill (N) circle (1pt) node[above left] {$N$};
                         \\fill (C) circle (1pt) node[left] {$C$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (goc_mon))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Vì $M$ là điểm chính giữa của cung nhỏ $\\overparen{AB}$ nên $\\text{sđ}\\overparen{MB} = \\dfrac{1}{2}\\text{sđ}\\overparen{AB}$.\\\\
                        Tương tự, vì $N$ là điểm chính giữa của cung nhỏ $\\overparen{BC}$ nên $\\text{sđ}\\overparen{BN} = \\dfrac{1}{2}\\text{sđ}\\overparen{BC}$.\\\\
                        Do điểm $B$ nằm trên cung nhỏ $\\overparen{MBN}$ và cũng nằm trên cung nhỏ $\\overparen{AC}$, áp dụng tính chất cộng số đo cung ta có:\\\\
                        $\\text{sđ}\\overparen{MBN} = \\text{sđ}\\overparen{MB} + \\text{sđ}\\overparen{BN} = \\dfrac{1}{2}\\left(\\text{sđ}\\overparen{AB} + \\text{sđ}\\overparen{BC}\\right) = \\dfrac{1}{2}\\text{sđ}\\overparen{AC}_{\\text{nhỏ}}$.
                        \\item Vì góc ở tâm $\\widehat{MON} = %s^\\circ$ chắn cung nhỏ $\\overparen{MBN}$ nên $\\text{sđ}\\overparen{MBN} = %s^\\circ$.\\\\
                        Theo câu a), ta có $\\text{sđ}\\overparen{AC}_{\\text{nhỏ}} = 2 \\cdot \\text{sđ}\\overparen{MBN} = 2 \\cdot %s^\\circ = %s^\\circ$.\\\\
                        Vậy số đo của cung lớn $\\overparen{AC}$ là $\\text{sđ}\\overparen{AC}_{\\text{lớn}} = 360^\\circ - %s^\\circ = %s^\\circ$.
                        \\end{enumEX}'''
                   % (goc_mon, goc_mon, goc_mon, sd_ac_nho, sd_ac_nho, sd_ac_lon))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
