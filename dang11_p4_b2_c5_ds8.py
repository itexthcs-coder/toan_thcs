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


def bt_dang11_p4_b2_c5_ds8(self):
    # Dạng 11 (Tự luận - Vận dụng): Tìm ẩn số x từ điều kiện góc ở tâm trên biểu đồ hình quạt tròn
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        x_val = 40 * k
        c1, c2, c3 = 15 * k, 15 * k, 30 * k
        ga = 3 * x_val + c1
        vit = 2 * x_val + c2
        ngan = x_val + c3
        tong = ga + vit + ngan
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.4) node[above] {Số lượng (con)};
        \\draw[line width=1pt, ->] (0,0) -- (4.8,0) node[right] {Loại gia cầm};
        \\draw[line width=1pt, fill=black!25] (0.6,0) rectangle (1.3,2.0); \\node[above] at (0.95,2.0) {$%s$}; \\node[below] at (0.95,0) {Gà};
        \\draw[line width=1pt, fill=black!25] (1.9,0) rectangle (2.6,1.4); \\node[above] at (2.25,1.4) {$%s$}; \\node[below] at (2.25,0) {Vịt};
        \\draw[line width=1pt, fill=black!25] (3.2,0) rectangle (3.9,1.0); \\node[above] at (3.55,1.0) {$%s$}; \\node[below] at (3.55,0) {Ngan};
        \\end{tikzpicture}
        \\end{center}""" % (ga, vit, ngan))
        
        noidungcauhoi = ("""Một trang trại chăn nuôi thống kê số lượng gia cầm gồm ba loại: Gà có $3x + %s$ con, Vịt có $2x + %s$ con và Ngan có $x + %s$ con (với $x$ là số nguyên dương). Biết rằng khi biểu diễn bảng thống kê này bằng biểu đồ hình quạt tròn thì hình quạt biểu diễn số lượng Gà có góc ở tâm bằng $162^\\circ$.\\\\
        a) Tính tỉ lệ phần trăm của số lượng Gà trong tổng số gia cầm của trang trại.\\\\
        b) Tìm $x$, từ đó lập bảng thống kê số lượng cụ thể của từng loại gia cầm và vẽ biểu đồ cột biểu diễn bảng thống kê đó."""
                         % (c1, c2, c3))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Tỉ lệ phần trăm của số lượng Gà trong tổng số gia cầm của trang trại là:
        $$\\dfrac{162^\\circ}{360^\\circ} \\cdot 100\\%% = 45\\%%.$$
        \\item Tổng số gia cầm của trang trại là: $(3x + %s) + (2x + %s) + (x + %s) = 6x + %s$ (con).\\\\
        Vì số lượng Gà chiếm $45\\%%$ tổng số gia cầm nên ta có phương trình:
        $$\\dfrac{3x + %s}{6x + %s} = \\dfrac{45}{100} = \\dfrac{9}{20} \\Rightarrow 20(3x + %s) = 9(6x + %s) \\Leftrightarrow 60x + %s = 54x + %s \\Leftrightarrow 6x = %s \\Leftrightarrow x = %s.$$
        Khi đó số lượng Gà là $%s$ con, Vịt là $%s$ con, Ngan là $%s$ con.\\\\
        Bảng thống kê và biểu đồ cột tương ứng:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|}
        \\hline
        \\textbf{Loại gia cầm} & Gà & Vịt & Ngan \\\\
        \\hline
        \\textbf{Số lượng (con)} & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}%s
        \\end{enumEX}""" % (c1, c2, c3, c1+c2+c3, c1, c1+c2+c3, c1, c1+c2+c3, 20*c1, 9*(c1+c2+c3), 6*x_val, x_val, ga, vit, ngan, ga, vit, ngan, tikz_a))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
