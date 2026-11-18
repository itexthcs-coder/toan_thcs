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


def bt_dang13_p4_b2_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = randint(1, 3)
        yA = a
        yB = 4 * a
        S_ht = Rational((yA + yB) * 3, 2)
        S_OAH = Rational(1 * yA, 2)
        S_OBK = Rational(2 * yB, 2)
        S_OAB = S_ht - S_OAH - S_OBK
        
        # Vẽ hình minh họa theo đúng chuẩn TikZ (không random tọa độ điểm)
        hinhve = ('''\\begin{center}
                   \\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                   \\draw[->, line width=1pt] (-2.5,0) -- (3,0) node[below] {$x$};
                   \\draw[->, line width=1pt] (0,-0.6) -- (0,4.8) node[left] {$y$};
                   \\draw[line width=1pt, smooth, samples=100, domain=-2.15:2.15] plot(\\x, {(\\x)^2});
                   \\coordinate (O) at (0,0);
                   \\coordinate (A) at (-1,1);
                   \\coordinate (B) at (2,4);
                   \\coordinate (H) at (-1,0);
                   \\coordinate (K) at (2,0);
                   \\draw[line width=1pt] (O) -- (A) -- (B) -- cycle;
                   \\draw[line width=1pt, dashed] (H) -- (A);
                   \\draw[line width=1pt, dashed] (K) -- (B);
                   \\fill (O) circle (1pt) node[below left] {$O$};
                   \\fill (A) circle (1pt) node[above left] {$A$};
                   \\fill (B) circle (1pt) node[above right] {$B$};
                   \\fill (H) circle (1pt) node[below] {$H$};
                   \\fill (K) circle (1pt) node[below] {$K$};
                   \\node[right] at (2.15,4.5) {$(P)$};
                   \\end{tikzpicture}
                   \\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y = %sx^2$ có đồ thị $(P)$ (như hình vẽ minh họa). Gọi $A$ và $B$ là hai điểm thuộc $(P)$ có hoành độ lần lượt là $x_A = -1$ và $x_B = 2$. Tính diện tích tam giác $OAB$ (với $O$ là gốc tọa độ). %s'''
                         %(latex(a) if a > 1 else "", hinhve
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Thay $x_A = -1$ vào công thức hàm số $y = %sx^2$, ta được $y_A = %s \\cdot (-1)^2 = %s$. Suy ra $A(-1; %s)$. \\\\
                   Thay $x_B = 2$ vào công thức hàm số $y = %sx^2$, ta được $y_B = %s \\cdot 2^2 = %s$. Suy ra $B(2; %s)$. \\\\
                   Gọi $H(-1; 0)$ và $K(2; 0)$ lần lượt là hình chiếu vuông góc của $A$ và $B$ trên trục hoành $Ox$. \\\\
                   Ta có độ dài các đoạn thẳng: \\\\
                   $AH = |y_A| = %s$; $BK = |y_B| = %s$; $OH = |-1| = 1$; $OK = |2| = 2$; $HK = OH + OK = 1 + 2 = 3$. \\\\
                   Tứ giác $AHKB$ là hình thang vuông tại $H$ và $K$ nên có diện tích là: \\\\
                   $S_{AHKB} = \\dfrac{(AH + BK) \\cdot HK}{2} = \\dfrac{(%s + %s) \\cdot 3}{2} = %s$. \\\\
                   Diện tích các tam giác vuông $OAH$ và $OBK$ lần lượt là: \\\\
                   $S_{OAH} = \\dfrac{1}{2} \\cdot OH \\cdot AH = \\dfrac{1}{2} \\cdot 1 \\cdot %s = %s$; \\\\
                   $S_{OBK} = \\dfrac{1}{2} \\cdot OK \\cdot BK = \\dfrac{1}{2} \\cdot 2 \\cdot %s = %s$. \\\\
                   Vậy diện tích tam giác $OAB$ là: \\\\
                   $S_{OAB} = S_{AHKB} - S_{OAH} - S_{OBK} = %s - %s - %s = %s$ (đơn vị diện tích).'''
                   %(latex(a) if a > 1 else "", latex(a), latex(yA), latex(yA),
                     latex(a) if a > 1 else "", latex(a), latex(yB), latex(yB),
                     latex(yA), latex(yB),
                     latex(yA), latex(yB), latex(S_ht),
                     latex(yA), latex(S_OAH),
                     latex(yB), latex(S_OBK),
                     latex(S_ht), latex(S_OAH), latex(S_OBK), latex(S_OAB)
                   ))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
