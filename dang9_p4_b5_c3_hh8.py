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


def bt_dang9_p4_b5_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_pytago = random.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)])
        a, b, r = bo_pytago
        o1o2 = 2 * b
        ab = 2 * a
        dien_tich = (o1o2 * ab) // 2

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O1) at (-1.5,0);
\\coordinate (O2) at (1.5,0);
\\coordinate (A) at (0,1.32);
\\coordinate (B) at (0,-1.32);
\\coordinate (H) at (0,0);
\\draw[line width=1pt] (O1) circle (2cm);
\\draw[line width=1pt] (O2) circle (2cm);
\\draw[line width=1pt] (O1)--(A)--(O2)--(B)--cycle (O1)--(O2) (A)--(B);
\\fill (O1) circle (1pt) node[left] {$O_1$};
\\fill (O2) circle (1pt) node[right] {$O_2$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai đường tròn $(O_1; %s\\text{ cm})$ và $(O_2; %s\\text{ cm})$ cắt nhau tại hai điểm phân biệt $A$ và $B$ sao cho $O_1O_2 = %s\\text{ cm}$. \\\\
a) Chứng minh tứ giác $O_1AO_2B$ là hình thoi. \\\\
b) Tính độ dài dây chung $AB$ và diện tích của tứ giác $O_1AO_2B$.%s'''
                         % (r, r, o1o2, hinh_ve))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} 
\\item Vì $A$ và $B$ cùng thuộc đường tròn $(O_1; %s\\text{ cm})$ nên $O_1A = O_1B = %s\\text{ cm}$.\\\\
Vì $A$ và $B$ cùng thuộc đường tròn $(O_2; %s\\text{ cm})$ nên $O_2A = O_2B = %s\\text{ cm}$.\\\\
Suy ra tứ giác $O_1AO_2B$ có bốn cạnh bằng nhau: $O_1A = AO_2 = O_2B = BO_1 = %s\\text{ cm}$.\\\\
Theo định nghĩa, tứ giác $O_1AO_2B$ là hình thoi.
\\item Gọi $H$ là giao điểm của hai đường chéo $O_1O_2$ và $AB$.\\\\
Vì $O_1AO_2B$ là hình thoi nên $O_1O_2 \\perp AB$ và $H$ là trung điểm của mỗi đường.\\\\
Do đó $O_1H = \\dfrac{O_1O_2}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$ và $\\widehat{AHO_1} = 90^\\circ$.\\\\
Áp dụng định lí Pythagore vào $\\Delta AHO_1$ vuông tại $H$, ta có:\\\\
$AH^2 = O_1A^2 - O_1H^2 = %s^2 - %s^2 = %s - %s = %s \\Rightarrow AH = %s\\text{ (cm)}$.\\\\
Suy ra độ dài dây chung $AB = 2AH = 2 \\cdot %s = %s\\text{ (cm)}$.\\\\
Diện tích hình thoi $O_1AO_2B$ là:\\\\
$S_{O_1AO_2B} = \\dfrac{1}{2}O_1O_2 \\cdot AB = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2)$.
\\end{enumEX} \n'''
                   % (r, r, r, r, r,
                      o1o2, b, r, b, r**2, b**2, a**2, a, a, ab,
                      o1o2, ab, dien_tich))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
