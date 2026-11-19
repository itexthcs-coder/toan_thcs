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

def bt_dang16_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r_gom = randint(10, 25)
        a_khung = 2 * r_gom * sqrt(3)
        R_thep = 2 * r_gom

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.6);
\\coordinate (B) at (210:1.6);
\\coordinate (C) at (-30:1.6);
\\draw[line width=1.2pt] (O) circle (1.6);
\\draw[line width=1.2pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (O) circle (0.8);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một nghệ nhân làm khung tranh gỗ muốn chế tác một bộ khung trang trí treo tường gồm một khung gỗ hình tam giác đều $ABC$ bao quanh một đĩa gốm sứ hình tròn có bán kính $r = %s\\text{ cm}$ tiếp xúc với cả ba cạnh bên trong của khung gỗ. Sau đó, nghệ nhân đặt toàn bộ khung gỗ tam giác đều này lọt vừa khít vào bên trong một vòng thép bảo vệ hình tròn lớn đi qua cả ba đỉnh $A, B, C$ của khung tam giác. Coi bề dày thanh gỗ không đáng kể.%s
\\begin{enumEX}[a)]{1}
\\item Tính độ dài mỗi cạnh của khung gỗ hình tam giác đều $ABC$.
\\item Tính bán kính của vòng thép bảo vệ hình tròn bên ngoài.
\\end{enumEX}''' % (r_gom, hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đĩa gốm sứ hình tròn tiếp xúc với cả ba cạnh bên trong của khung gỗ tam giác đều $ABC$ chính là đường tròn nội tiếp tam giác đều $ABC$ với bán kính $r = %s\\text{ cm}$.\\\\
Gọi $a$ là độ dài mỗi cạnh của khung gỗ hình tam giác đều $ABC$. Ta có công thức bán kính đường tròn nội tiếp tam giác đều là:
$$r = \\frac{\\sqrt{3}}{6}a.$$
Thay $r = %s\\text{ cm}$, ta được:
$$\\frac{\\sqrt{3}}{6}a = %s \\Rightarrow a = \\frac{%s}{\\sqrt{3}} = %s\\text{ (cm)}.$$
Vậy độ dài mỗi cạnh của khung gỗ hình tam giác đều $ABC$ là $%s\\text{ cm}$.
\\item Vòng thép bảo vệ hình tròn đi qua cả ba đỉnh $A, B, C$ chính là đường tròn ngoại tiếp tam giác đều $ABC$.\\\\
Bán kính của vòng thép bảo vệ là:
$$R = \\frac{\\sqrt{3}}{3}a = \\frac{\\sqrt{3}}{3} \\cdot %s = %s\\text{ (cm)}.$$
\\end{enumEX}''' % (r_gom, r_gom, r_gom, 6 * r_gom, latex(a_khung), latex(a_khung), latex(a_khung), R_thep))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
