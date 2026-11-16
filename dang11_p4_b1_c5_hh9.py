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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang11_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_pytago = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
        a, b_abs, R = random.choice(bo_pytago)
        xi = a
        yi = -b_abs
        xa = 2 * a
        yb = -2 * b_abs

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (I) at (0.8,-1.1);
\\coordinate (A) at (1.6,0);
\\coordinate (B) at (0,-2.2);
\\draw[->, line width=1pt] (-1.2,0)--(2.8,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-2.8)--(0,1.2) node[left] {$y$};
\\draw[line width=1pt] (I) circle (1.36);
\\draw[line width=1pt] (A)--(B);
\\fill (O) circle (1pt) node[above left] {$O$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho điểm $I(%s; %s)$ và đường tròn $(I; %s)$ (như hình vẽ). \\\\
a) Chứng minh rằng đường tròn $(I; %s)$ đi qua gốc tọa độ $O(0; 0)$. \\\\
b) Đường tròn $(I; %s)$ cắt trục hoành $Ox$ tại điểm $A$ (khác $O$) và cắt trục tung $Oy$ tại điểm $B$ (khác $O$). Tìm tọa độ các điểm $A, B$ và chứng minh ba điểm $A, I, B$ thẳng hàng.
%s''' % (xi, yi, R, R, R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Áp dụng định lí Pythagore trong mặt phẳng tọa độ $Oxy$, khoảng cách từ tâm $I(%s; %s)$ đến gốc tọa độ $O(0; 0)$ là:\\\\
$IO = \\sqrt{(0 - %s)^2 + (0 - (%s))^2} = \\sqrt{%s^2 + %s^2} = %s = R$.\\\\
Vì $IO = R$ nên điểm $O(0; 0)$ nằm trên đường tròn $(I; %s)$, tức là đường tròn $(I; %s)$ đi qua gốc tọa độ $O$.
\\item - Điểm $A(x_A; 0) \\in Ox$ ($x_A \\ne 0$) nằm trên $(I; %s)$ khi và chỉ khi:\\\\
$IA = %s \\Leftrightarrow (x_A - %s)^2 + (0 - (%s))^2 = %s^2 \\Leftrightarrow (x_A - %s)^2 = %s^2$.\\\\
Giải ra được $x_A = 0$ (loại) hoặc $x_A = %s$. Vậy $A(%s; 0)$.\\\\
- Điểm $B(0; y_B) \\in Oy$ ($y_B \\ne 0$) nằm trên $(I; %s)$ khi và chỉ khi:\\\\
$IB = %s \\Leftrightarrow (0 - %s)^2 + (y_B - (%s))^2 = %s^2 \\Leftrightarrow (y_B + %s)^2 = %s^2$.\\\\
Giải ra được $y_B = 0$ (loại) hoặc $y_B = %s$. Vậy $B(0; %s)$.\\\\
- Ta thấy trung điểm của đoạn thẳng $AB$ có tọa độ $\\left(\\dfrac{%s + 0}{2}; \\dfrac{0 + (%s)}{2}\\right) = (%s; %s)$, trùng với tọa độ tâm $I(%s; %s)$.\\\\
Do $I$ là trung điểm của đoạn thẳng $AB$ nên ba điểm $A, I, B$ thẳng hàng.
\\end{enumEX}''' % (xi, yi, xi, yi, a, b_abs, R, R, R, R, R, xi, yi, R, xi, a, xa, xa, R, R, xi, yi, R, b_abs, b_abs, yb, yb, xa, yb, xi, yi, xi, yi))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
