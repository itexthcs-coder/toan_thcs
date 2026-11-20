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


def bt_dang12_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [
            (9, 12, 15, 6),
            (6, 8, 10, 4),
            (3, 4, 5, 2)
        ]
        r_val, h_non, l_non, h_tru = random.choice(bo_pythagore)
        v_tru = (r_val ** 2) * h_tru
        v_non = ((r_val ** 2) * h_non) // 3
        sxq_tru = 2 * r_val * h_tru
        sxq_non = r_val * l_non

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho một hình trụ và một hình nón có cùng bán kính đáy $R = %s\\text{ cm}$ (như hình vẽ). Biết thể tích của hình nón bằng $\\frac{2}{3}$ thể tích của hình trụ, và chiều cao của hình trụ là $h_{\\text{trụ}} = %s\\text{ cm}$. \\\\
a) Tính chiều cao của hình nón. \\\\
b) So sánh diện tích xung quanh của hình trụ và diện tích xung quanh của hình nón.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.2) ellipse (1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0) arc (180:360:1.2 and 0.3);
\\draw[line width=1pt, dashed] (1.2,0) arc (0:180:1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0)--(-1.2,2.2) (1.2,0)--(1.2,2.2);
\\draw[line width=1pt, dashed] (0,0)--(1.2,0);
\\node[below] at (0.6,0) {$R$};
\\coordinate (S) at (4,2.8);
\\coordinate (O) at (4,0);
\\coordinate (A) at (2.8,0);
\\coordinate (B) at (5.2,0);
\\draw[line width=1pt] (S)--(A) (S)--(B);
\\draw[line width=1pt] (2.8,0) arc (180:360:1.2 and 0.3);
\\draw[line width=1pt, dashed] (5.2,0) arc (0:180:1.2 and 0.3);
\\draw[line width=1pt, dashed] (S)--(O)--(B);
\\node[below] at (4.6,0) {$R$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_val, h_tru))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Thể tích của hình trụ là: $V_{\\text{trụ}} = \\pi R^2 h_{\\text{trụ}} = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$. \\\\
Thể tích của hình nón là: $V_{\\text{nón}} = \\frac{2}{3} V_{\\text{trụ}} = \\frac{2}{3} \\cdot %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$. \\\\
Từ công thức $V_{\\text{nón}} = \\frac{1}{3}\\pi R^2 h_{\\text{nón}}$, suy ra chiều cao của hình nón là:
$$h_{\\text{nón}} = \\frac{3 V_{\\text{nón}}}{\\pi R^2} = \\frac{3 \\cdot %s\\pi}{\\pi \\cdot %s^2} = %s\\text{ (cm)}.$$
\\item Độ dài đường sinh của hình nón là: $l = \\sqrt{R^2 + h_{\\text{nón}}^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$. \\\\
Diện tích xung quanh của hình nón là: $S_{xq\\text{ (nón)}} = \\pi R l = \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Diện tích xung quanh của hình trụ là: $S_{xq\\text{ (trụ)}} = 2\\pi R h_{\\text{trụ}} = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$. \\\\
Vì $%s\\pi > %s\\pi$ nên diện tích xung quanh của hình nón lớn hơn diện tích xung quanh của hình trụ.
\\end{enumEX}'''
                   % (r_val, h_tru, v_tru, v_tru, v_non, v_non, r_val, h_non,
                      r_val, h_non, l_non, r_val, l_non, sxq_non, r_val, h_tru, sxq_tru, sxq_non, sxq_tru))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
