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


def bt_dang1_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        k = randint(2, 6)
        a_num = randint(1, 3)
        a_den = randint(1, 3)
        a = Rational(a_num, a_den)
        y0 = a * (k**2)
        f = a * x**2
        S = k * y0

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, cho parabol $(P): y=%s$. Gọi $A$ và $B$ là hai điểm phân biệt thuộc $(P)$ có cùng tung độ bằng $%s$. Diện tích tam giác $OAB$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.5) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.8:2.8] plot (\\x, {0.5*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2.4,2.88);
\\coordinate (B) at (2.4,2.88);
\\coordinate (H) at (0,2.88);
\\draw[line width=1pt] (O)--(A)--(B)--cycle;
\\draw[line width=1pt, dashed] (-2.4,0)--(A) (2.4,0)--(B);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(f), latex(y0)))

        # Nội dung lời giải
        loigiai = ('''Ta có $A$ và $B$ thuộc parabol $(P): y=%s$ và có cùng tung độ $y=%s$ nên hoành độ của $A$ và $B$ là nghiệm của phương trình: \\\\
$%s = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = %s$. \\\\
Không mất tính tổng quát, giả sử $A\\left(%s; %s\\right)$ và $B\\left(%s; %s\\right)$. \\\\
Gọi $H\\left(0; %s\\right)$ là hình chiếu vuông góc của $O$ lên đường thẳng $AB$. \\\\
Khi đó ta có bảng tọa độ và độ dài các đoạn thẳng như sau: \\\\
\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
Điểm / Đoạn thẳng & Tọa độ / Biểu thức & Giá trị \\\\
\\hline
Điểm $A$ & $\\left(%s; %s\\right)$ & Hoành độ $x_A = %s$ \\\\
\\hline
Điểm $B$ & $\\left(%s; %s\\right)$ & Hoành độ $x_B = %s$ \\\\
\\hline
Độ dài đáy $AB$ & $|x_B - x_A|$ & $%s$ \\\\
\\hline
Chiều cao $OH$ & $|y_H|$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center} \\\\
Vậy diện tích tam giác $OAB$ là $S_{OAB} = \\dfrac{1}{2} \\cdot OH \\cdot AB = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s$.'''
                   % (latex(f), latex(y0),
                      latex(f), latex(y0), latex(k**2), latex(-k), latex(k),
                      latex(-k), latex(y0), latex(k), latex(y0),
                      latex(y0),
                      latex(-k), latex(y0), latex(-k),
                      latex(k), latex(y0), latex(k),
                      latex(2*k),
                      latex(y0),
                      latex(y0), latex(2*k), latex(S)))

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
