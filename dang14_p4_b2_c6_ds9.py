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


def bt_dang14_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15)]
        ab, ac, bc = random.choice(triples)
        diff = ac - ab
        
        c_pt = (diff**2 - bc**2) // 2
        delta = diff**2 - 4*c_pt
        x2_neg = -ac
        chu_vi = ab + ac + bc
        
        # Vẽ hình minh họa theo đúng chuẩn TikZ (không random tọa độ điểm)
        hinhve = ('''\\begin{center}
                   \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                   \\coordinate (A) at (0,0);
                   \\coordinate (B) at (0,2.5);
                   \\coordinate (C) at (4.5,0);
                   \\draw[line width=1pt] (A) -- (B) -- (C) -- cycle;
                   \\draw[line width=1pt] (0,0.3) -- (0.3,0.3) -- (0.3,0);
                   \\fill (A) circle (1pt) node[below left] {$A$};
                   \\fill (B) circle (1pt) node[above left] {$B$};
                   \\fill (C) circle (1pt) node[below right] {$C$};
                   \\end{tikzpicture}
                   \\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho tam giác $ABC$ vuông tại $A$ có cạnh huyền $BC = %s\\text{ cm}$ (như hình vẽ minh họa). Biết độ dài cạnh góc vuông $AC$ lớn hơn độ dài cạnh góc vuông $AB$ là $%s\\text{ cm}$. Tính chu vi của tam giác vuông $ABC$. %s'''
                         %(latex(bc), latex(diff), hinhve
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Gọi độ dài cạnh góc vuông $AB$ là $x$ ($\\text{cm}$), điều kiện: $x > 0$. \\\\
                   Vì độ dài cạnh góc vuông $AC$ lớn hơn $AB$ là $%s\\text{ cm}$ nên độ dài cạnh $AC$ là $x + %s$ ($\\text{cm}$). \\\\
                   Áp dụng định lí Pythagore vào tam giác $ABC$ vuông tại $A$, ta có: \\\\
                   $AB^2 + AC^2 = BC^2$ \\\\
                   $\\Leftrightarrow x^2 + (x + %s)^2 = %s^2$ \\\\
                   $\\Leftrightarrow x^2 + x^2 + %sx + %s = %s$ \\\\
                   $\\Leftrightarrow 2x^2 + %sx - %s = 0$ \\\\
                   $\\Leftrightarrow x^2 + %sx - %s = 0$. \\\\
                   Phương trình bậc hai trên có $a = 1$, $b = %s$, $c = %s$. \\\\
                   Ta có biệt thức $\\Delta = %s^2 - 4 \\cdot 1 \\cdot (%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{-%s + \\sqrt{%s}}{2 \\cdot 1} = %s$ (thỏa mãn điều kiện $x > 0$); \\\\
                   $x_2 = \\dfrac{-%s - \\sqrt{%s}}{2 \\cdot 1} = %s$ (không thỏa mãn điều kiện nên loại). \\\\
                   Do đó, $AB = %s\\text{ cm}$ và $AC = %s + %s = %s\\text{ cm}$. \\\\
                   Vậy chu vi của tam giác vuông $ABC$ là: \\\\
                   $P = AB + AC + BC = %s + %s + %s = %s\\text{ (cm)}$.'''
                   %(latex(diff), latex(diff),
                     latex(diff), latex(bc),
                     latex(2*diff), latex(diff**2), latex(bc**2),
                     latex(2*diff), latex(bc**2 - diff**2),
                     latex(diff), latex(abs(c_pt)),
                     latex(diff), latex(c_pt),
                     latex(diff), latex(c_pt), latex(delta),
                     latex(diff), latex(delta), latex(ab),
                     latex(diff), latex(delta), latex(x2_neg),
                     latex(ab), latex(ab), latex(diff), latex(ac),
                     latex(ab), latex(ac), latex(bc), latex(chu_vi)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
