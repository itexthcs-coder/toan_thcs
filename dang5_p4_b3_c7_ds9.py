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


def bt_dang5_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        m1, m2, m3, m4, m5 = 4 * k, 10 * k, 14 * k, 8 * k, 4 * k
        n = 40 * k

        tikz_sol = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (6.5,0) node[below] {Chiều cao ($\\text{cm}$)};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {Tần số tương đối (\\%%)};
\\foreach \\y/\\lbl in {0.7/10, 1.4/20, 2.1/30, 2.8/40} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (1,0.7) -- (2,1.75) -- (3,2.45) -- (4,1.4) -- (5,0.7);
\\fill (1,0.7) circle (1pt) node[above] {$10\\%%$};
\\fill (2,1.75) circle (1pt) node[above] {$25\\%%$};
\\fill (3,2.45) circle (1pt) node[above] {$35\\%%$};
\\fill (4,1.4) circle (1pt) node[above] {$20\\%%$};
\\fill (5,0.7) circle (1pt) node[above] {$10\\%%$};
\\node[below] at (1,0) {$45$};
\\node[below] at (2,0) {$55$};
\\node[below] at (3,0) {$65$};
\\node[below] at (4,0) {$75$};
\\node[below] at (5,0) {$85$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Khảo sát chiều cao (đơn vị: $\\text{cm}$) của $%s$ cây bạch đàn giống sau $6$ tháng gieo trồng thu được kết quả:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|c|}
\\hline
Chiều cao ($\\text{cm}$) & $[40; 50)$ & $[50; 60)$ & $[60; 70)$ & $[70; 80)$ & $[80; 90)$ \\\\
\\hline
Số cây & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
a) Xác định giá trị đại diện của từng nhóm và lập bảng tần số tương đối ghép nhóm.\\
b) Vẽ biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng cho bảng thống kê trên.''' % (n, m1, m2, m3, m4, m5))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Giá trị đại diện của các nhóm lần lượt là: $x_1 = 45$; $x_2 = 55$; $x_3 = 65$; $x_4 = 75$; $x_5 = 85$.\\
Với cỡ mẫu $n = %s$, tần số tương đối của các nhóm lần lượt là: $10\\%%$; $25\\%%$; $35\\%%$; $20\\%%$; $10\\%%$. Ta có bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|c|}
\\hline
Chiều cao ($\\text{cm}$) & $[40; 50)$ & $[50; 60)$ & $[60; 70)$ & $[70; 80)$ & $[80; 90)$ \\\\
\\hline
Giá trị đại diện & $45$ & $55$ & $65$ & $75$ & $85$ \\\\
\\hline
Tần số tương đối & $10\\%%$ & $25\\%%$ & $35\\%%$ & $20\\%%$ & $10\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng:
%s
\\end{enumEX}''' % (n, tikz_sol))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
