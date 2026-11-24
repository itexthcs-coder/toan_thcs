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


def bt_dang9_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
            ('M', 'N', 'P', 'Q', 'I', 'H', 'K')
        ]
        A_t, B_t, C_t, D_t, E_t, F_t, G_t = random.choice(bo_ten)

        noidungcauhoi = ("""Cho hình bình hành $%s%s%s%s$. Một đường thẳng $d$ đi qua đỉnh $%s$ cắt đường chéo $%s%s$ tại $%s$, cắt cạnh $%s%s$ tại $%s$ và cắt tia đối của tia $%s%s$ tại $%s$ (như hình vẽ bên dưới). \\\\
a) Chứng minh rằng $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ và $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$. \\\\
b) Chứng minh rằng $%s%s^2 = %s%s \\cdot %s%s$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (0,0);
\\coordinate (C) at (3.2,0);
\\coordinate (G) at (5.6,0);
\\coordinate (A) at (1.0,2.5);
\\coordinate (B) at (4.2,2.5);
\\coordinate (E) at (intersection of A--G and B--D);
\\coordinate (F) at (intersection of A--G and B--C);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (B)--(D) (C)--(G) (A)--(G);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below] {$%s$};
\\fill (D) circle (1pt) node[below left] {$%s$};
\\fill (G) circle (1pt) node[below right] {$%s$};
\\fill (E) circle (1pt) node[above right] {$%s$};
\\fill (F) circle (1pt) node[above right] {$%s$};
\\end{tikzpicture}
\\end{center}"""
                         % (A_t, B_t, C_t, D_t, A_t, B_t, D_t, E_t, B_t, C_t, F_t, D_t, C_t, G_t,
                            A_t, E_t, E_t, G_t, B_t, E_t, E_t, D_t, E_t, F_t, A_t, E_t, B_t, E_t, E_t, D_t,
                            A_t, E_t, E_t, F_t, E_t, G_t,
                            A_t, B_t, C_t, D_t, G_t, E_t, F_t))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Vì $%s%s%s%s$ là hình bình hành nên $%s%s // %s%s$ và $%s%s // %s%s$. \\\\
Xét $\\Delta %s%s%s$ có $%s%s // %s%s$ (vì $%s%s // %s%s$), theo định lí Thalès trong tam giác ta có: $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ (1). \\\\
Xét $\\Delta %s%s%s$ có $%s%s // %s%s$ (vì $%s%s // %s%s$), theo định lí Thalès trong tam giác ta có: $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$ (2).
\\item Từ (1) và (2) suy ra $\\dfrac{%s%s}{%s%s} = \\dfrac{%s%s}{%s%s}$. \\\\
Nhân chéo hai vế của tỉ lệ thức trên, ta được: $%s%s^2 = %s%s \\cdot %s%s$ (điều phải chứng minh).
\\end{enumEX}"""
                   % (A_t, B_t, C_t, D_t, A_t, B_t, D_t, G_t, B_t, F_t, A_t, D_t,
                      E_t, D_t, G_t, A_t, B_t, D_t, G_t, A_t, B_t, D_t, C_t, A_t, E_t, E_t, G_t, B_t, E_t, E_t, D_t,
                      E_t, A_t, D_t, B_t, F_t, A_t, D_t, B_t, C_t, A_t, D_t, E_t, F_t, A_t, E_t, B_t, E_t, E_t, D_t,
                      A_t, E_t, E_t, G_t, E_t, F_t, A_t, E_t,
                      A_t, E_t, E_t, F_t, E_t, G_t))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
