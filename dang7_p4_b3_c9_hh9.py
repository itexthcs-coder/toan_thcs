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


def bt_dang7_p4_b3_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ae, ec, ac = random.choice([(6, 8, 10), (3, 4, 5), (5, 12, 13), (8, 15, 17)])
        r_val = Rational(ac, 2)
        r_str = str(float(r_val)).replace('.0', '').replace('.', ',')
        dt = ae * ec

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.8,0);
\\coordinate (C) at (1.8,0);
\\coordinate (B) at (0,1.8);
\\coordinate (D) at (0,-1.8);
\\coordinate (E) at (125:1.8);
\\coordinate (F) at (-55:1.8);
\\draw[line width=1pt, dashed] (O) circle (1.8);
\\draw[line width=1pt] (A)--(C);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (A)--(E)--(C)--(F)--cycle;
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (F) circle (1pt) node[below right] {$F$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đoạn thẳng $AC = %s\\text{ cm}$ cố định. Vẽ hình vuông $ABCD$ và hai hình chữ nhật phân biệt $AECF$, $AGCH$ sao cho cả ba hình đều nhận $AC$ làm một đường chéo. \\\\
a) Chứng minh rằng tám điểm $A, B, C, D, E, F, G, H$ cùng nằm trên một đường tròn, xác định tâm $O$ và bán kính của đường tròn đó. \\\\
b) Biết $AE = %s\\text{ cm}$, tính độ dài cạnh $EC$ và diện tích hình chữ nhật $AECF$.%s''' % (ac, ae, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $O$ là trung điểm của đoạn thẳng $AC$.\\\\
Vì hình vuông $ABCD$ và hai hình chữ nhật $AECF, AGCH$ đều nhận $AC$ làm một đường chéo nên giao điểm hai đường chéo của cả ba tứ giác đều trùng với trung điểm $O$ của $AC$.\\\\
Theo tính chất đường tròn ngoại tiếp hình vuông và hình chữ nhật, ta có:\\\\
$OA = OB = OC = OD = OE = OF = OG = OH = \\dfrac{AC}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$.\\\\
Vậy tám điểm $A, B, C, D, E, F, G, H$ cùng nằm trên đường tròn tâm $O$ (trung điểm của $AC$) bán kính $R = %s\\text{ cm}$.
\\item Vì $AECF$ là hình chữ nhật nên $\\widehat{AEC} = 90^\\circ$.\\\\
Áp dụng định lí Pythagore cho tam giác $AEC$ vuông tại $E$, ta có:\\\\
$EC = \\sqrt{AC^2 - AE^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}$.\\\\
Diện tích hình chữ nhật $AECF$ là $S_{AECF} = AE \\cdot EC = %s \\cdot %s = %s\\text{ (cm}^2)$.
\\end{enumEX}''' % (ac, r_str, r_str, ac, ae, ec, ae, ec, dt))

    # Xuất câu hỏi và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
