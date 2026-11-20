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


def bt_dang15_p4_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = [
            (3, 4, 5),
            (6, 8, 10),
            (5, 12, 13),
            (12, 5, 13)
        ]
        h_val, r_val, l_val = random.choice(bo_pythagore)
        v_tru = (r_val ** 2) * h_val
        v_non = v_tru // 3
        v_con = v_tru - v_non
        sxq_tru = 2 * r_val * h_val
        s_day = r_val ** 2
        sxq_non = r_val * l_val
        s_tong = sxq_tru + s_day + sxq_non

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Quay tam giác $ABC$ một vòng quanh đường thẳng $d$ đi qua $C$ và song song với $AB$ (như hình vẽ). \\\\
a) Mô tả khối tròn xoay tạo thành khi quay tam giác $ABC$ quanh đường thẳng $d$. \\\\
b) Tính thể tích và diện tích toàn bộ bề mặt của khối tròn xoay tạo thành.
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (C) at (0,2.6);
\\coordinate (O) at (0,0);
\\coordinate (A) at (1.5,2.6);
\\coordinate (B) at (1.5,0);
\\draw[line width=1pt] (0,2.6) ellipse (1.5 and 0.35);
\\draw[line width=1pt] (-1.5,0) arc (180:360:1.5 and 0.35);
\\draw[line width=1pt, dashed] (1.5,0) arc (0:180:1.5 and 0.35);
\\draw[line width=1pt] (-1.5,0)--(-1.5,2.6) (1.5,0)--(1.5,2.6);
\\draw[line width=1pt] (C)--(A)--(B);
\\draw[line width=1pt, dashed] (C)--(B) (C)--(O);
\\draw[line width=1pt] (0,-0.6)--(0,3.3);
\\node[right] at (0,3.2) {$d$};
\\fill (C) circle (1pt) node[left] {$C$};
\\fill (A) circle (1pt) node[right] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\end{tikzpicture}
\\end{center}'''
                         % (h_val, r_val))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khối tròn xoay tạo thành là một hình trụ có bán kính đáy $R = AC = %s\\text{ cm}$ và chiều cao $h = AB = %s\\text{ cm}$ bị khoét đi một hình nón có đỉnh là $C$, đáy là hình tròn tâm $O$ (bán kính $R = %s\\text{ cm}$) và chiều cao $h = CO = %s\\text{ cm}$.
\\item Thể tích của khối tròn xoay tạo thành bằng hiệu thể tích của hình trụ và hình nón:
$$V = V_{\\text{trụ}} - V_{\\text{nón}} = \\pi R^2 h - \\frac{1}{3}\\pi R^2 h = \\frac{2}{3}\\pi R^2 h = \\frac{2}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Độ dài đường sinh của hình nón là: $l = BC = \\sqrt{AB^2 + AC^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$. \\\\
Diện tích toàn bộ bề mặt của khối tròn xoay gồm mặt xung quanh hình trụ, mặt đáy trên và mặt xung quanh hình nón bị khoét:
$$S = S_{xq\\text{ (trụ)}} + S_{\\text{đáy trên}} + S_{xq\\text{ (nón)}} = 2\\pi R h + \\pi R^2 + \\pi R l = 2\\pi \\cdot %s \\cdot %s + \\pi \\cdot %s^2 + \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\end{enumEX}'''
                   % (r_val, h_val, r_val, h_val, r_val, h_val, v_con,
                      h_val, r_val, l_val, r_val, h_val, r_val, r_val, l_val, s_tong))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
