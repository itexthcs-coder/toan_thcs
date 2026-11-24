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


def bt_dang7_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ten = [
            ('A', 'B', 'C', 'G', 'M', 'E', 'F', 'H', 'K'),
            ('M', 'N', 'P', 'G', 'I', 'D', 'E', 'H', 'K')
        ]
        A_t, B_t, C_t, G_t, M_t, E_t, F_t, H_t, K_t = random.choice(bo_ten)

        noidungcauhoi = ("""Cho $\\Delta %s%s%s$ có trọng tâm $%s$, đường trung tuyến $%s%s$ ($%s \\in %s%s$). Qua $%s$ kẻ đường thẳng $d$ cắt các cạnh $%s%s$, $%s%s$ lần lượt tại $%s$ và $%s$ ($%s \\in %s%s$, $%s \\in %s%s$). Qua $%s$ và $%s$ lần lượt kẻ các đường thẳng song song với $d$, cắt đường thẳng $%s%s$ tại $%s$ và $%s$ (như hình vẽ bên dưới). \\\\
a) Chứng minh rằng $%s%s = %s%s$. \\\\
b) Chứng minh rằng $\\dfrac{%s%s}{%s%s} + \\dfrac{%s%s}{%s%s} = 3$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (G) at ($(A)!0.6667!(M)$);
\\coordinate (E) at ($(A)!0.58!(B)$);
\\coordinate (F) at (intersection of E--G and A--C);
\\coordinate (H) at (intersection of A--M and B--{$(B)+(G)-(E)$});
\\coordinate (K) at (intersection of A--M and C--{$(C)+(F)-(G)$});
\\draw[line width=1pt] (A)--(B)--(C)--cycle (E)--(F);
\\draw[line width=1pt, dashed] (A)--(K) (B)--(H) (C)--(K);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[below left] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (M) circle (1pt) node[below left] {$%s$};
\\fill (G) circle (1pt) node[above right] {$%s$};
\\fill (E) circle (1pt) node[left] {$%s$};
\\fill (F) circle (1pt) node[right] {$%s$};
\\fill (H) circle (1pt) node[left] {$%s$};
\\fill (K) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}"""
                         % (A_t, B_t, C_t, G_t, A_t, M_t, M_t, B_t, C_t, G_t,
                            A_t, B_t, A_t, C_t, E_t, F_t, E_t, A_t, B_t, F_t, A_t, C_t,
                            B_t, C_t, A_t, M_t, H_t, K_t,
                            M_t, H_t, M_t, K_t,
                            A_t, B_t, A_t, E_t, A_t, C_t, A_t, F_t,
                            A_t, B_t, C_t, M_t, G_t, E_t, F_t, H_t, K_t))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Vì $%s%s // %s%s$ (cùng song song với đường thẳng $d$) nên $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc so le trong). \\\\
Xét $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có: \\\\
$\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (chứng minh trên); \\\\
$%s%s = %s%s$ (vì $%s$ là trung điểm của $%s%s$); \\\\
$\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc đối đỉnh). \\\\
Do đó $\\Delta %s%s%s = \\Delta %s%s%s$ (g.c.g), suy ra $%s%s = %s%s$ (hai cạnh tương ứng).
\\item Xét $\\Delta %s%s%s$ có $%s%s // %s%s$, theo định lí Thalès trong tam giác ta có: $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$. \\\\
Xét $\\Delta %s%s%s$ có $%s%s // %s%s$, theo định lí Thalès trong tam giác ta có: $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$. \\\\
Cộng vế theo vế hai đẳng thức trên, ta được: \\\\
$\\dfrac{%s%s}{%s%s} + \\dfrac{%s%s}{%s%s} = \\dfrac{%s%s + %s%s}{%s%s} = \\dfrac{(%s%s - %s%s) + (%s%s + %s%s)}{%s%s} = \\dfrac{2 %s%s + (%s%s - %s%s)}{%s%s}$. \\\\
Vì $%s%s = %s%s$ (theo câu a) nên $%s%s - %s%s = 0$, và vì $%s$ là trọng tâm $\\Delta %s%s%s$ nên $\\dfrac{%s%s}{%s%s} = \\dfrac{3}{2}$. \\\\
Vậy $\\dfrac{%s%s}{%s%s} + \\dfrac{%s%s}{%s%s} = \\dfrac{2 %s%s}{%s%s} = 2 \\cdot \\dfrac{3}{2} = 3$ (điều phải chứng minh).
\\end{enumEX}"""
                   % (B_t, H_t, C_t, K_t, M_t, B_t, H_t, M_t, C_t, K_t,
                      M_t, B_t, H_t, M_t, C_t, K_t,
                      M_t, B_t, H_t, M_t, C_t, K_t,
                      M_t, B_t, M_t, C_t, M_t, B_t, C_t,
                      B_t, M_t, H_t, C_t, M_t, K_t,
                      M_t, B_t, H_t, M_t, C_t, K_t, M_t, H_t, M_t, K_t,
                      A_t, B_t, H_t, E_t, G_t, B_t, H_t, A_t, B_t, A_t, E_t, A_t, H_t, A_t, G_t,
                      A_t, C_t, K_t, G_t, F_t, C_t, K_t, A_t, C_t, A_t, F_t, A_t, K_t, A_t, G_t,
                      A_t, B_t, A_t, E_t, A_t, C_t, A_t, F_t, A_t, H_t, A_t, K_t, A_t, G_t,
                      A_t, M_t, M_t, H_t, A_t, M_t, M_t, K_t, A_t, G_t,
                      A_t, M_t, M_t, K_t, M_t, H_t, A_t, G_t,
                      M_t, H_t, M_t, K_t, M_t, K_t, M_t, H_t, G_t, A_t, B_t, C_t, A_t, M_t, A_t, G_t,
                      A_t, B_t, A_t, E_t, A_t, C_t, A_t, F_t, A_t, M_t, A_t, G_t))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
