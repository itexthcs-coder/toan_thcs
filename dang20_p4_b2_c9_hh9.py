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

def bt_dang20_p4_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        ab = 13 * k
        bc = 14 * k
        ac = 15 * k
        p_vuon = 21 * k
        S_vuon = 84 * (k**2)
        r_tuoi = 4 * k
        af = 7 * k
        ai_val = k * sqrt(65)

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.3,2.3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.5,0);
\\coordinate (I) at (1.5,0.85);
\\coordinate (F) at (0.72,1.28);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (I) circle (0.85);
\\draw[line width=1pt, dashed] (A)--(I)--(F);
\\fill (I) circle (1pt) node[right] {$I$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (F) circle (1pt) node[left] {$F$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một khu vườn sinh thái có dạng hình tam giác $ABC$ với chiều dài ba hàng rào bao quanh là $AB = %s\\text{ m}$, $BC = %s\\text{ m}$ và $AC = %s\\text{ m}$. Chủ vườn muốn lắp đặt một trụ tưới nước xoay tròn tự động tại vị trí $I$ sao cho vòng tròn nước tưới vừa chạm tới cả ba hàng rào của khu vườn.%s
\\begin{enumEX}[a)]{1}
\\item Hãy trình bày cách xác định vị trí đặt trụ tưới $I$ trên bản vẽ thiết kế khu vườn bằng thước kẻ và compa.
\\item Biết diện tích tam giác tính theo công thức Heron là $S = \\sqrt{p(p-a)(p-b)(p-c)}$ với $p$ là nửa chu vi tam giác. Tính khoảng cách từ trụ tưới $I$ đến mỗi hàng rào và tính khoảng cách từ trụ tưới $I$ đến góc vườn $A$.
\\end{enumEX}''' % (ab, bc, ac, hinh_ve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì vòng tròn nước tưới chạm tới cả ba hàng rào của khu vườn nên $I$ là tâm đường tròn nội tiếp tam giác $ABC$. Cách dựng điểm $I$ bằng thước kẻ và compa trên bản vẽ như sau:\\\\
- Dựng tia phân giác của góc $B$: Vẽ cung tròn tâm $B$ cắt $BC, BA$ lần lượt tại $X, Y$. Vẽ hai cung tròn tâm $X, Y$ cùng bán kính cắt nhau tại $Z$ ($Z \\neq B$), kẻ tia $BZ$.\\\\
- Tương tự, dựng tia phân giác của góc $C$. Giao điểm của hai tia phân giác này chính là vị trí đặt trụ tưới $I$.
\\item Nửa chu vi của khu vườn tam giác $ABC$ là:
$$p = \\frac{%s + %s + %s}{2} = %s\\text{ (m)}.$$
Áp dụng công thức Heron, diện tích khu vườn là:
$$S = \\sqrt{%s \\cdot (%s - %s) \\cdot (%s - %s) \\cdot (%s - %s)} = \\sqrt{%s} = %s\\text{ (m}^2).$$
Khoảng cách từ trụ tưới $I$ đến mỗi hàng rào chính là bán kính đường tròn nội tiếp:
$$r = \\frac{S}{p} = \\frac{%s}{%s} = %s\\text{ (m)}.$$
Gọi $F$ là tiếp điểm của đường tròn $(I)$ trên cạnh $AB$, ta có $IF \\perp AB$ và $AF = p - BC = %s - %s = %s\\text{ (m)}$.\\\\
Áp dụng định lí Pythagore vào tam giác $AFI$ vuông tại $F$, khoảng cách từ trụ tưới $I$ đến góc vườn $A$ là:
$$AI = \\sqrt{AF^2 + IF^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s\\text{ (m)}.$$
\\end{enumEX}''' % (ab, bc, ac, p_vuon, p_vuon, p_vuon, ab, p_vuon, bc, p_vuon, ac, S_vuon**2, S_vuon, S_vuon, p_vuon, r_tuoi, p_vuon, bc, af, af, r_tuoi, af**2 + r_tuoi**2, latex(ai_val)))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
