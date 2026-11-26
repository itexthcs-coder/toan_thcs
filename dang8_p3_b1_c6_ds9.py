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


def bt_dang8_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        x1 = randint(1, 3)
        x2 = x1 + randint(2, 4)
        a = Rational(1, randint(2, 4))
        y1 = a * (x1**2)
        y2 = a * (x2**2)
        f = a * x**2
        AB = 2 * x1
        CD = 2 * x2
        h = y2 - y1
        S = Rational(1, 2) * (AB + CD) * h

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$) có cả bốn đỉnh đều nằm trên parabol $(P): y=%s$. Biết $A$ và $B$ có tung độ bằng $%s$, còn $C$ và $D$ có tung độ bằng $%s$. Diện tích hình thang $ABCD$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.8) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.8:2.8] plot (\\x, {0.5*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.2,0.72);
\\coordinate (B) at (1.2,0.72);
\\coordinate (D) at (-2.5,3.125);
\\coordinate (C) at (2.5,3.125);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(f), latex(y1), latex(y2)))

        # Nội dung lời giải
        loigiai = ('''Tìm tọa độ hai đỉnh $A$ và $B$: Thay $y = %s$ vào phương trình $(P)$, ta có: \\\\
$%s = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$. \\\\
Suy ra $A\\left(-%s; %s\\right)$ và $B\\left(%s; %s\\right)$, do đó độ dài đáy nhỏ $AB = 2 \\cdot %s = %s$. \\\\
Tìm tọa độ hai đỉnh $C$ và $D$: Thay $y = %s$ vào phương trình $(P)$, ta có: \\\\
$%s = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$. \\\\
Suy ra $D\\left(-%s; %s\\right)$ và $C\\left(%s; %s\\right)$, do đó độ dài đáy lớn $CD = 2 \\cdot %s = %s$. \\\\
Bảng tổng hợp các yếu tố của hình thang cân $ABCD$: \\\\
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Yếu tố hình thang & Biểu thức & Giá trị \\\\
\\hline
Đáy nhỏ $AB$ & $|x_B - x_A|$ & $%s$ \\\\
\\hline
Đáy lớn $CD$ & $|x_C - x_D|$ & $%s$ \\\\
\\hline
Chiều cao $h$ & $y_C - y_A$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Diện tích hình thang $ABCD$ là: \\\\
$S_{ABCD} = \\dfrac{(AB + CD) \\cdot h}{2} = \\dfrac{(%s + %s) \\cdot %s}{2} = %s$.'''
                   % (latex(y1),
                      latex(f), latex(y1), str(x1**2), str(x1), str(x1),
                      str(x1), latex(y1), str(x1), latex(y1), str(x1), str(AB),
                      latex(y2),
                      latex(f), latex(y2), str(x2**2), str(x2), str(x2),
                      str(x2), latex(y2), str(x2), latex(y2), str(x2), str(CD),
                      str(AB), str(CD), latex(h),
                      str(AB), str(CD), latex(h), latex(S)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (latex(S))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
