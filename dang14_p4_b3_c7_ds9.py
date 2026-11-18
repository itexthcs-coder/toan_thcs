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


def bt_dang14_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tikz_sol = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (7.5,0) node[below] {Quãng đường ($\\text{km}$)};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {Mật độ ($y_i$)};
\\foreach \\y/\\lbl in {1/1, 2/2, 2.5/2.5} {
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=4pt] {$\\lbl$};
}
\\draw[line width=1pt] (0,0) rectangle (1,1.0);
\\node[above] at (0.5,1.0) {$10\\%%$};
\\draw[line width=1pt] (1,0) rectangle (2,2.5);
\\node[above] at (1.5,2.5) {$25\\%%$};
\\draw[line width=1pt] (2,0) rectangle (4,2.0);
\\node[above] at (3.0,2.0) {$40\\%%$};
\\draw[line width=1pt] (4,0) rectangle (7,0.83);
\\node[above] at (5.5,0.83) {$25\\%%$};
\\node[below] at (0,0) {$0$};
\\node[below] at (1,0) {$10$};
\\node[below] at (2,0) {$20$};
\\node[below] at (4,0) {$40$};
\\node[below] at (7,0) {$70$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Khảo sát quãng đường di chuyển bằng xe máy mỗi ngày (đơn vị: $\\text{km}$) của $200$ nhân viên giao hàng tại một công ty vận chuyển thu được bảng thống kê với các nhóm có độ dài \textbf{không bằng nhau}:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Quãng đường ($\\text{km}$) & $[0; 10)$ & $[10; 20)$ & $[20; 40)$ & $[40; 70)$ \\\\
\\hline
Số nhân viên & $20$ & $50$ & $80$ & $50$ \\\\
\\hline
\\end{tabular}
\\end{center}
Để vẽ biểu đồ tần số tương đối dạng cột sao cho diện tích mỗi cột chính bằng tần số tương đối của nhóm đó, chiều cao cột được xác định bởi công thức mật độ $y_i = \\dfrac{f_i}{l_i}$ (trong đó $f_i$ là tần số tương đối tính theo $\\%%$, $l_i$ là độ dài nhóm).\\
a) Tính tần số tương đối $f_i$ và chiều cao $y_i$ (làm tròn đến hàng phần trăm nếu cần) của từng cột.\\
b) Vẽ biểu đồ tần số tương đối dạng cột cho bảng thống kê trên theo đúng tỉ lệ chiều cao $y_i$ và độ rộng đáy $l_i$.''')

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Ta tính độ dài nhóm $l_i$, tần số tương đối $f_i$ và chiều cao mật độ $y_i = \\dfrac{f_i}{l_i}$ cho từng nhóm:
\\begin{itemize}
\\item Nhóm $[0; 10)$: $l_1 = 10$; $f_1 = \\dfrac{20}{200} \\cdot 100\\%% = 10\\%%$; $y_1 = \\dfrac{10}{10} = 1$.
\\item Nhóm $[10; 20)$: $l_2 = 10$; $f_2 = \\dfrac{50}{200} \\cdot 100\\%% = 25\\%%$; $y_2 = \\dfrac{25}{10} = 2,5$.
\\item Nhóm $[20; 40)$: $l_3 = 20$; $f_3 = \\dfrac{80}{200} \\cdot 100\\%% = 40\\%%$; $y_3 = \\dfrac{40}{20} = 2$.
\\item Nhóm $[40; 70)$: $l_4 = 30$; $f_4 = \\dfrac{50}{200} \\cdot 100\\%% = 25\\%%$; $y_4 = \\dfrac{25}{30} \\approx 0,83$.
\\end{itemize}
\\item Biểu đồ tần số tương đối dạng cột với độ dài nhóm không bằng nhau:
%s
\\end{enumEX}''' % (tikz_sol))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
