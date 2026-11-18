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


def bt_dang19_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tikz_sol = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.2,0) node[below] {Điểm thi};
\\draw[->, line width=1pt] (0,0) -- (0,3.6) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40, 3.5/50} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1.2, 0.6) -- (2.4, 1.8) -- (3.6, 3.2) -- (4.8, 1.4);
\\fill (1.2, 0.6) circle (1pt) node[above] {$8,6\\%%$};
\\fill (2.4, 1.8) circle (1pt) node[above] {$25,7\\%%$};
\\fill (3.6, 3.2) circle (1pt) node[above] {$45,7\\%%$};
\\fill (4.8, 1.4) circle (1pt) node[above] {$20,0\\%%$};
\\node[below] at (1.2,0) {$4$};
\\node[below] at (2.4,0) {$5,75$};
\\node[below] at (3.6,0) {$7,25$};
\\node[below] at (4.8,0) {$9$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Điểm thi thử môn Toán vào lớp $10$ (thang điểm $10$) của $35$ học sinh lớp $9\\text{A}$ được thống kê như sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Điểm thi & $[3; 5)$ & $[5; 6,5)$ & $[6,5; 8)$ & $[8; 10]$ \\\\
\\hline
Số học sinh & $3$ & $9$ & $16$ & $7$ \\\\
\\hline
\\end{tabular}
\\end{center}
a) Lập bảng tần số tương đối ghép nhóm cho mẫu số liệu trên (làm tròn kết quả đến hàng phần mười).\\
b) Nhận xét về tổng các tần số tương đối sau khi làm tròn và vẽ biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng minh họa bảng số liệu trên.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Tính tần số tương đối của từng nhóm (cỡ mẫu $n = 35$) và làm tròn đến hàng phần mười:
\\begin{itemize}
\\item $f_1 = \\dfrac{3}{35} \\cdot 100\\%% \\approx 8,6\\%%$; \quad $f_2 = \\dfrac{9}{35} \\cdot 100\\%% \\approx 25,7\\%%$;
\\item $f_3 = \\dfrac{16}{35} \\cdot 100\\%% \\approx 45,7\\%%$; \quad $f_4 = \\dfrac{7}{35} \\cdot 100\\%% = 20,0\\%%$.
\\end{itemize}
Ta có bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Điểm thi & $[3; 5)$ & $[5; 6,5)$ & $[6,5; 8)$ & $[8; 10]$ \\\\
\\hline
Giá trị đại diện & $4$ & $5,75$ & $7,25$ & $9$ \\\\
\\hline
Tần số tương đối & $8,6\\%%$ & $25,7\\%%$ & $45,7\\%%$ & $20,0\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Tổng các tần số tương đối sau làm tròn là $8,6\\%% + 25,7\\%% + 45,7\\%% + 20,0\\%% = 100\\%%$. Biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng:
%s
\\end{enumEX}''' % (tikz_sol))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
