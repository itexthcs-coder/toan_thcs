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


def bt_dang9_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([1, 2])
        ac_val = Decimal('6') * k
        bc_val = Decimal('8') * k
        ab_val = Decimal('10') * k
        ch_val = Decimal('4.8') * k
        ah_val = Decimal('3.6') * k
        sxq_pi = ch_val * ac_val
        v_pi = (ch_val ** 2 * ah_val) / Decimal('3')

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        ac_s = fmt(ac_val)
        bc_s = fmt(bc_val)
        ab_s = fmt(ab_val)
        ch_s = fmt(ch_val)
        ah_s = fmt(ah_val)
        sxq_s = fmt(sxq_pi)
        v_s = fmt(v_pi)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho nửa đường tròn tâm $O$, đường kính $AB = %s\\text{ cm}$. Lấy điểm $C$ trên nửa đường tròn sao cho dây cung $AC = %s\\text{ cm}$. Kẻ $CH \\perp AB$ tại $H$. Quay tam giác vuông $ACH$ một vòng quanh trục $AB$ cố định ta được một hình nón đỉnh $A$ (như hình vẽ). \\\\
a) Tính độ dài các đoạn thẳng $BC$, $CH$ và $AH$. \\\\
b) Tính diện tích xung quanh và thể tích của hình nón tạo thành.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (-2.2,0);
\\coordinate (B) at (2.2,0);
\\coordinate (O) at (0,0);
\\coordinate (H) at (-0.8,0);
\\coordinate (C) at (-0.8,1.65);
\\coordinate (D) at (-0.8,-1.65);
\\draw[line width=1pt] (B) arc (0:180:2.2);
\\draw[line width=1pt] (A)--(B) (A)--(C)--(B) (A)--(D);
\\draw[line width=1pt] (-0.8,-1.65) arc (-90:90:0.35 and 1.65);
\\draw[line width=1pt, dashed] (-0.8,1.65) arc (90:270:0.35 and 1.65);
\\draw[line width=1pt, dashed] (C)--(H);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (C) circle (1pt) node[above] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (ab_s, ac_s))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì điểm $C$ nằm trên nửa đường tròn đường kính $AB$ nên $\\widehat{ACB} = 90^\\circ$, hay $\\Delta ABC$ vuông tại $C$. \\\\
Theo định lí Pythagore: $BC = \\sqrt{AB^2 - AC^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$. \\\\
Xét $\\Delta ABC$ vuông tại $C$ có đường cao $CH$, ta có:
$$CH = \\frac{AC \\cdot BC}{AB} = \\frac{%s \\cdot %s}{%s} = %s\\text{ (cm)}; \\qquad AH = \\frac{AC^2}{AB} = \\frac{%s^2}{%s} = %s\\text{ (cm)}.$$
\\item Khi quay $\\Delta ACH$ quanh trục $AB$ cố định, ta được hình nón đỉnh $A$ có bán kính đáy $r = CH = %s\\text{ cm}$, chiều cao $h = AH = %s\\text{ cm}$ và đường sinh $l = AC = %s\\text{ cm}$. \\\\
Diện tích xung quanh của hình nón là: $S_{xq} = \\pi r l = \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Thể tích của hình nón là: $V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\cdot (%s)^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.
\\end{enumEX}'''
                   % (ab_s, ac_s, bc_s, ac_s, bc_s, ab_s, ch_s, ac_s, ab_s, ah_s,
                      ch_s, ah_s, ac_s, ch_s, ac_s, sxq_s, ch_s, ah_s, v_s))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
