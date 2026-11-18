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


def bt_dang3_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([120, 160, 200])
        f1, f2, f3, f4 = 15, 40, 30, 15
        m1 = (n * f1) // 100
        m2 = (n * f2) // 100
        m3 = (n * f3) // 100
        m4 = (n * f4) // 100
        m_thuong = m1 + m2

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.2,0) node[below] {Mức lương (triệu đồng)};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1,0) rectangle (2,1.05);
\\node[above] at (1.5,1.05) {$15\\%%$};
\\draw[line width=1pt] (2,0) rectangle (3,2.8);
\\node[above] at (2.5,2.8) {$40\\%%$};
\\draw[line width=1pt] (3,0) rectangle (4,2.1);
\\node[above] at (3.5,2.1) {$30\\%%$};
\\draw[line width=1pt] (4,0) rectangle (5,1.05);
\\node[above] at (4.5,1.05) {$15\\%%$};
\\node[below] at (1,0) {$6$};
\\node[below] at (2,0) {$9$};
\\node[below] at (3,0) {$12$};
\\node[below] at (4,0) {$15$};
\\node[below] at (5,0) {$18$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Biểu đồ tần số tương đối ghép nhóm dạng cột dưới đây thống kê mức lương tháng (đơn vị: triệu đồng) của $%s$ nhân viên tại một doanh nghiệp dịch vụ:
%s
a) Lập bảng tần số tương đối ghép nhóm và bảng tần số ghép nhóm cho dữ liệu được biểu diễn trên biểu đồ.\\
b) Doanh nghiệp dự định thưởng Tết thêm $1$ tháng lương cho các nhân viên có mức lương dưới $12$ triệu đồng. Hỏi có bao nhiêu nhân viên được nhận khoản thưởng này?''' % (n, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Từ biểu đồ cột đã cho, ta lập được bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Mức lương (triệu đồng) & $[6; 9)$ & $[9; 12)$ & $[12; 15)$ & $[15; 18)$ \\\\
\\hline
Tần số tương đối & $15\\%%$ & $40\\%%$ & $30\\%%$ & $15\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
Với cỡ mẫu $n = %s$, tần số của các nhóm lần lượt là: $m_1 = %s \\cdot 15\\%% = %s$; $m_2 = %s \\cdot 40\\%% = %s$; $m_3 = %s \\cdot 30\\%% = %s$; $m_4 = %s \\cdot 15\\%% = %s$. Ta có bảng tần số ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Mức lương (triệu đồng) & $[6; 9)$ & $[9; 12)$ & $[12; 15)$ & $[15; 18)$ \\\\
\\hline
Số nhân viên & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Số nhân viên có mức lương dưới $12$ triệu đồng (thuộc hai nhóm $[6; 9)$ và $[9; 12)$) là:
$$%s + %s = %s \\text{ (nhân viên)}.$$
\\end{enumEX}''' % (n, n, m1, n, m2, n, m3, n, m4, m1, m2, m3, m4, m1, m2, m_thuong))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
