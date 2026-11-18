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


def bt_dang11_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_par = randint(1, 3)
        x1 = -1
        x2 = 2
        m = a_par * (x1 + x2)
        n = -a_par * x1 * x2
        y1 = a_par * (x1**2)
        y2 = a_par * (x2**2)
        
        b_pt = -m
        c_pt = -n
        delta = b_pt**2 - 4 * a_par * c_pt
        
        sign_n = "+" if n >= 0 else "-"
        abs_n = abs(n)
        
        # Vẽ hình minh họa theo đúng chuẩn TikZ (không random tọa độ điểm)
        hinhve = ('''\\begin{center}
                   \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                   \\draw[->, line width=1pt] (-3,0) -- (3.5,0) node[below] {$x$};
                   \\draw[->, line width=1pt] (0,-0.8) -- (0,5.2) node[left] {$y$};
                   \\draw[line width=1pt, smooth, samples=100, domain=-2.2:2.2] plot(\\x, {(\\x)^2});
                   \\draw[line width=1pt, domain=-2.2:2.6] plot(\\x, {\\x + 2});
                   \\coordinate (O) at (0,0);
                   \\coordinate (A) at (-1,1);
                   \\coordinate (B) at (2,4);
                   \\draw[line width=1pt, dashed] (-1,0) -- (A) -- (0,1);
                   \\draw[line width=1pt, dashed] (2,0) -- (B) -- (0,4);
                   \\fill (O) circle (1pt) node[below left] {$O$};
                   \\fill (A) circle (1pt) node[above left] {$A$};
                   \\fill (B) circle (1pt) node[above left] {$B$};
                   \\node[right] at (2.2,4.8) {$(P)$};
                   \\node[right] at (2.6,4.5) {$(d)$};
                   \\end{tikzpicture}
                   \\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho Parabol $(P): y = %sx^2$ và đường thẳng $(d): y = %sx %s %s$ như hình vẽ minh họa. Tìm tọa độ các giao điểm $A$ và $B$ của $(P)$ và $(d)$ bằng phép tính. %s'''
                         %(latex(a_par) if a_par > 1 else "", latex(m) if m > 1 else "", sign_n, latex(abs_n), hinhve
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Hoành độ giao điểm của Parabol $(P)$ và đường thẳng $(d)$ là nghiệm của phương trình: \\\\
                   $%sx^2 = %sx %s %s \\Leftrightarrow %sx^2 - %sx - %s = 0$. \\\\
                   Phương trình bậc hai trên có các hệ số $a = %s$, $b = %s$, $c = %s$. \\\\
                   Ta có biệt thức $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot (%s) = %s > 0$. \\\\
                   Phương trình có hai nghiệm phân biệt: \\\\
                   $x_1 = \\dfrac{-(%s) - \\sqrt{%s}}{2 \\cdot %s} = -1$; \\\\
                   $x_2 = \\dfrac{-(%s) + \\sqrt{%s}}{2 \\cdot %s} = 2$. \\\\
                   \\begin{itemize}
                   \\item Với $x_1 = -1$, thay vào $(P)$ ta được $y_1 = %s \\cdot (-1)^2 = %s$. Suy ra điểm $A(-1; %s)$.
                   \\item Với $x_2 = 2$, thay vào $(P)$ ta được $y_2 = %s \\cdot 2^2 = %s$. Suy ra điểm $B(2; %s)$.
                   \\end{itemize}
                   Vậy tọa độ các giao điểm của $(P)$ và $(d)$ là $A(-1; %s)$ và $B(2; %s)$.'''
                   %(latex(a_par) if a_par > 1 else "", latex(m) if m > 1 else "", sign_n, latex(abs_n),
                     latex(a_par) if a_par > 1 else "", latex(m) if m > 1 else "", latex(n),
                     latex(a_par), latex(b_pt), latex(c_pt),
                     latex(b_pt), latex(a_par), latex(c_pt), latex(delta),
                     latex(b_pt), latex(delta), latex(a_par),
                     latex(b_pt), latex(delta), latex(a_par),
                     latex(a_par), latex(y1), latex(y1),
                     latex(a_par), latex(y2), latex(y2),
                     latex(y1), latex(y2)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
