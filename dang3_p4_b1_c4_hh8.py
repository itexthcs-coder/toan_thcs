# -*- coding: utf-8 -*-
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


def bt_dang3_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # AD = x, AB = 12 => DB = 12 - x. BE = x + 3, EC = 10.
        # x / (12 - x) = (x + 3) / 10 => 10x = (12 - x)(x + 3) = 36 + 9x - x^2 => x^2 + x - 36 = 0 (khong nguyen)
        # Chon so nguyen dep: x = 6, AB = 15 => DB = 9 => x / DB = 6 / 9 = 2 / 3.
        # BE = x + 2 = 8, EC = 12 => BE / EC = 8 / 12 = 2 / 3!
        k = random.choice([1, 2])
        x_val = 6 * k
        ab = 15 * k
        db = ab - x_val
        c_add = 2 * k
        ec = 12 * k
        be = x_val + c_add
        bc = be + ec

        noidungcauhoi = ("""Cho $\\Delta ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$. Trên cạnh $AB$ lấy điểm $D$ sao cho $AD = x\\text{ (cm)}$, trên cạnh $BC$ lấy điểm $E$ sao cho $BE = x + %s\\text{ (cm)}$ và $EC = %s\\text{ cm}$ (với $0 < x < %s$). Biết $DE \\perp AB$ tại $D$ (như hình vẽ bên dưới). Tìm giá trị của $x$ và tính độ dài cạnh huyền $BC$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (0,3);
\\coordinate (C) at (4,0);
\\coordinate (D) at (0,1.8);
\\coordinate (E) at (1.6,1.8);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (0,2.05)--(0.25,2.05)--(0.25,1.8);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[above left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\end{tikzpicture}
\\end{center}"""
                         % (ab, c_add, ec, ab))

        loigiai = ("""Ta có $DE \\perp AB$ và $AC \\perp AB$ (do $\\Delta ABC$ vuông tại $A$) nên $DE // AC$ (từ vuông góc đến song song). \\\\
Độ dài đoạn thẳng $DB$ là: $DB = AB - AD = %s - x\\text{ (cm)}$. \\\\
Xét $\\Delta ABC$ có $DE // AC$ ($D \\in AB$, $E \\in BC$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{AD}{DB} = \\dfrac{BE}{EC} \\Rightarrow \\dfrac{x}{%s - x} = \\dfrac{x + %s}{%s}$. \\\\
Suy ra $%s x = (%s - x)(x + %s) \\Leftrightarrow %s x = %s + %s x - x^2 \\Leftrightarrow x^2 + %s x - %s = 0$ \\\\
$\\Leftrightarrow (x - %s)(x + %s) = 0$. \\\\
Vì $0 < x < %s$ nên $x + %s > 0$, suy ra $x - %s = 0 \\Leftrightarrow x = %s$. \\\\
Khi đó $BE = %s + %s = %s\\text{ (cm)}$, suy ra độ dài cạnh huyền $BC = BE + EC = %s + %s = %s\\text{ (cm)}$."""
                   % (ab, ab, c_add, ec,
                      ec, ab, c_add, ec, ab * c_add, ab - c_add, ec - ab + c_add, ab * c_add,
                      x_val, x_val + ec - ab + c_add, ab, x_val + ec - ab + c_add, x_val, x_val,
                      x_val, c_add, be, be, ec, bc))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
