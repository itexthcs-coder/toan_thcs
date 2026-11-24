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


def bt_dang8_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'M', 'N', 'P', 'Q'),
            ('M', 'N', 'P', 'Q', 'E', 'F', 'H', 'K')
        ]
        A_t, B_t, C_t, D_t, M_t, N_t, P_t, Q_t = random.choice(bo_ten)

        noidungcauhoi = ("""Cho hình thang $%s%s%s%s$ ($%s%s // %s%s$, $%s%s < %s%s$). Một đường thẳng song song với hai đáy cắt các cạnh bên $%s%s$, $%s%s$ và hai đường chéo $%s%s$, $%s%s$ lần lượt tại $%s$, $%s$, $%s$, $%s$ ($%s \\in %s%s$, $%s \\in %s%s$, $%s \\in %s%s$, $%s \\in %s%s$) như hình vẽ bên dưới. \\\\
a) Chứng minh rằng $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$. \\\\
b) Chứng minh rằng $%s%s = %s%s$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (0,0);
\\coordinate (C) at (5.2,0);
\\coordinate (A) at (1.2,2.8);
\\coordinate (B) at (3.6,2.8);
\\coordinate (M) at ($(A)!0.45!(D)$);
\\coordinate (N) at ($(B)!0.45!(C)$);
\\coordinate (P) at (intersection of B--D and M--N);
\\coordinate (Q) at (intersection of A--C and M--N);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N);
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below left] {$%s$};
\\fill (M) circle (1pt) node[left] {$%s$};
\\fill (N) circle (1pt) node[right] {$%s$};
\\fill (P) circle (1pt) node[above] {$%s$};
\\fill (Q) circle (1pt) node[above] {$%s$};
\\end{tikzpicture}
\\end{center}"""
                         % (A_t, B_t, C_t, D_t, A_t, B_t, C_t, D_t, A_t, B_t, C_t, D_t,
                            A_t, D_t, B_t, C_t, B_t, D_t, A_t, C_t, M_t, N_t, P_t, Q_t,
                            M_t, A_t, D_t, N_t, B_t, C_t, P_t, B_t, D_t, Q_t, A_t, C_t,
                            A_t, M_t, A_t, D_t, B_t, N_t, B_t, C_t,
                            M_t, P_t, N_t, Q_t,
                            A_t, B_t, C_t, D_t, M_t, N_t, P_t, Q_t))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Xét $\\Delta %s%s%s$ có $%s%s // %s%s$ (vì $%s%s // %s%s$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ (1). \\\\
Xét $\\Delta %s%s%s$ có $%s%s // %s%s$ (vì $%s%s // %s%s$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ (2). \\\\
Từ (1) và (2) suy ra $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$.
\\item Xét $\\Delta %s%s%s$ có $%s%s // %s%s$, theo định lí Thalès trong tam giác ta có: $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ (3). \\\\
Xét $\\Delta %s%s%s$ có $%s%s // %s%s$, theo định lí Thalès trong tam giác ta có: $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ (4). \\\\
Mà theo câu a) ta có $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$, kết hợp với (3) và (4) suy ra: \\\\
$\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s} \\Rightarrow %s%s = %s%s$ (điều phải chứng minh).
\\end{enumEX}"""
                   % (A_t, D_t, C_t, M_t, Q_t, D_t, C_t, M_t, N_t, C_t, D_t,
                      A_t, M_t, A_t, D_t, A_t, Q_t, A_t, C_t,
                      C_t, A_t, B_t, Q_t, N_t, A_t, B_t, M_t, N_t, A_t, B_t,
                      A_t, Q_t, A_t, C_t, B_t, N_t, B_t, C_t,
                      A_t, M_t, A_t, D_t, B_t, N_t, B_t, C_t,
                      D_t, A_t, B_t, M_t, P_t, A_t, B_t, M_t, P_t, A_t, B_t, D_t, M_t, D_t, A_t,
                      C_t, B_t, A_t, N_t, Q_t, A_t, B_t, N_t, Q_t, A_t, B_t, C_t, N_t, C_t, B_t,
                      D_t, M_t, D_t, A_t, C_t, N_t, C_t, B_t,
                      M_t, P_t, A_t, B_t, N_t, Q_t, A_t, B_t, M_t, P_t, N_t, Q_t))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
