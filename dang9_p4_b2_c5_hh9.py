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

def bt_dang9_p4_b2_c5_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([4, 6, 8, 10, 12])
        AB = 2 * R
        AH = R // 2
        OH_val = R - AH

        noidungcauhoi = ('''Cho đường tròn $(O)$ có đường kính $AB$ và điểm $C$ nằm trên đường tròn ($C$ khác $A, B$). Qua $C$ kẻ dây cung $CD$ vuông góc với đường kính $AB$ tại $H$ (như hình vẽ).\\\\
                         a) Chứng minh rằng $\\text{sđ}\\overset\\frown{AC}_{\\text{nhỏ}} = \\text{sđ}\\overset\\frown{AD}_{\\text{nhỏ}}$ và $\\text{sđ}\\overset\\frown{BC}_{\\text{nhỏ}} = \\text{sđ}\\overset\\frown{BD}_{\\text{nhỏ}}$.\\\\
                         b) Biết $AB = %s\\text{ cm}$ và $AH = %s\\text{ cm}$. Tính số đo của cung lớn $\\overset\\frown{CD}$.
                         \\begin{center}
                         \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                         \\coordinate (O) at (0,0);
                         \\coordinate (A) at (-1.8,0);
                         \\coordinate (B) at (1.8,0);
                         \\coordinate (C) at (120:1.8);
                         \\coordinate (D) at (-120:1.8);
                         \\coordinate (H) at (-0.9,0);
                         \\draw[line width=1pt] (O) circle (1.8);
                         \\draw[line width=1pt] (A)--(B) (C)--(D) (O)--(C) (O)--(D);
                         \\fill (O) circle (1pt) node[below right] {$O$};
                         \\fill (A) circle (1pt) node[left] {$A$};
                         \\fill (B) circle (1pt) node[right] {$B$};
                         \\fill (C) circle (1pt) node[above left] {$C$};
                         \\fill (D) circle (1pt) node[below left] {$D$};
                         \\fill (H) circle (1pt) node[below left] {$H$};
                         \\end{tikzpicture}
                         \\end{center}'''
                         % (AB, AH))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                        \\item Tam giác $OCD$ cân tại $O$ ($OC = OD$) có đường cao $OH$ đồng thời là đường phân giác của góc $\\widehat{COD}$, suy ra $\\widehat{AOC} = \\widehat{AOD}$.\\\\
                        Vì hai góc ở tâm này lần lượt chắn hai cung nhỏ $\\overset\\frown{AC}$ và $\\overset\\frown{AD}$ nên $\\text{sđ}\\overset\\frown{AC}_{\\text{nhỏ}} = \\text{sđ}\\overset\\frown{AD}_{\\text{nhỏ}}$.\\\\
                        Mặt khác, $\\widehat{BOC} = 180^\\circ - \\widehat{AOC} = 180^\\circ - \\widehat{AOD} = \\widehat{BOD}$, suy ra $\\text{sđ}\\overset\\frown{BC}_{\\text{nhỏ}} = \\text{sđ}\\overset\\frown{BD}_{\\text{nhỏ}}$.
                        \\item Bán kính đường tròn $(O)$ là $R = \\dfrac{AB}{2} = \\dfrac{%s}{2} = %s\\text{ cm}$.\\\\
                        Vì $AH = %s\\text{ cm} < R$ nên $H$ nằm giữa $O$ và $A$, do đó $OH = OA - AH = %s - %s = %s\\text{ cm}$.\\\\
                        Xét tam giác $OHC$ vuông tại $H$, ta có $\\cos \\widehat{COH} = \\dfrac{OH}{OC} = \\dfrac{%s}{%s} = \\dfrac{1}{2} \\Rightarrow \\widehat{COH} = 60^\\circ$.\\\\
                        Suy ra $\\widehat{COD} = 2\\widehat{COH} = 120^\\circ$, nên $\\text{sđ}\\overset\\frown{CD}_{\\text{nhỏ}} = 120^\\circ$.\\\\
                        Vậy số đo của cung lớn $\\overset\\frown{CD}$ là $\\text{sđ}\\overset\\frown{CD}_{\\text{lớn}} = 360^\\circ - 120^\\circ = 240^\\circ$.
                        \\end{enumEX}'''
                   % (AB, R, AH, R, AH, OH_val, OH_val, R))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
