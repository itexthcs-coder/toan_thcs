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


def bt_dang15_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        xA = random.choice([2, 4])
        xB = random.choice([-2, -4, -6])
        a = Rational(1, 2)
        yA = a * (xA**2)
        yB = a * (xB**2)
        HK = xA - xB
        S = Rational(1, 2) * (yA + yB) * HK

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho điểm $A(%s; %s)$ thuộc parabol $(P): y=ax^2$. Lấy điểm $B$ thuộc $(P)$ có hoành độ bằng $%s$. Gọi $H$ và $K$ lần lượt là hình chiếu vuông góc của $A$ và $B$ lên trục hoành $Ox$. Diện tích tứ giác $ABKH$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (2.8,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.8) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.8:2.2] plot (\\x, {0.5*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (1.5,1.125);
\\coordinate (H) at (1.5,0);
\\coordinate (B) at (-2.5,3.125);
\\coordinate (K) at (-2.5,0);
\\draw[line width=1pt] (A)--(B)--(K)--(H)--cycle;
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[right] {$A$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (K) circle (1pt) node[below] {$K$};
\\end{tikzpicture}
\\end{center}'''
                         % (str(xA), latex(yA), str(xB)))

        # Nội dung lời giải
        loigiai = ('''Vì $A(%s; %s)$ thuộc parabol $(P): y = ax^2$ nên thay $x = %s, y = %s$, ta được: \\\\
$%s = a \\cdot %s^2 \\Leftrightarrow a = \\dfrac{%s}{%s} = %s$. \\\\
Suy ra phương trình parabol $(P)$ là $y = %s x^2$. \\\\
Điểm $B$ thuộc $(P)$ có hoành độ $x_B = %s$ nên tung độ của $B$ là $y_B = %s \\cdot (%s)^2 = %s$. \\\\
Vì $H$ và $K$ lần lượt là hình chiếu vuông góc của $A$ và $B$ lên trục $Ox$ nên $H(%s; 0)$, $K(%s; 0)$ và tứ giác $ABKH$ là hình thang vuông tại $H$ và $K$. \\\\
Bảng các kích thước của hình thang vuông $ABKH$: \\\\
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Kích thước & Công thức & Giá trị \\\\
\\hline
Đáy nhỏ $AH$ & $y_A$ & $%s$ \\\\
\\hline
Đáy lớn $BK$ & $y_B$ & $%s$ \\\\
\\hline
Chiều cao $HK$ & $|x_A - x_B|$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center} \\\\
Diện tích hình thang vuông $ABKH$ là: \\\\
$S_{ABKH} = \\dfrac{(AH + BK) \\cdot HK}{2} = \\dfrac{(%s + %s) \\cdot %s}{2} = %s$.'''
                   % (str(xA), latex(yA), str(xA), latex(yA),
                      latex(yA), str(xA), latex(yA), str(xA**2), latex(a),
                      latex(a),
                      str(xB), latex(a), str(xB), latex(yB),
                      str(xA), str(xB),
                      latex(yA), latex(yB), str(HK),
                      latex(yA), latex(yB), str(HK), latex(S)))

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
