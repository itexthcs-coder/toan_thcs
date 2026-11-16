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


def bt_dang10_p1_b1_c4_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        goc_nhon = random.randint(25, 65)
        loai_ts = random.choice([
            ('\\sin', 'AC', 'BC', 'DF', 'EF', 'DE', 'DF'),
            ('\\cos', 'AB', 'BC', 'DE', 'EF', 'DF', 'DE'),
            ('\\tan', 'AC', 'AB', 'DF', 'DE', 'EF', 'DF'),
            ('\\cot', 'AB', 'AC', 'DE', 'DF', 'EF', 'DE')
        ])
        ten_ts, c1_abc, c2_abc, d1, d2, s1_a, s1_b = loai_ts

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (2.8,0);
\\coordinate (C) at (0,2);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above left] {$C$};

\\coordinate (D) at (4.5,0);
\\coordinate (E) at (8.5,0);
\\coordinate (F) at (4.5,2.85);
\\draw[line width=1pt] (D)--(E)--(F)--cycle;
\\draw[line width=1pt] (4.5,0.25)--(4.75,0.25)--(4.75,0);
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (E) circle (1pt) node[below right] {$E$};
\\fill (F) circle (1pt) node[above left] {$F$};
\\end{tikzpicture}
\\end{center}''')

        du = ['$\\dfrac{%s}{%s}$' % (d1, d2)]
        da = random.choice(du)
        s = [
            '$\\dfrac{%s}{%s}$' % (d2, d1),
            '$\\dfrac{%s}{%s}$' % (s1_a, d2),
            '$\\dfrac{%s}{%s}$' % (d1, s1_a)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho $\\triangle ABC$ vuông tại $A$ và $\\triangle DEF$ vuông tại $D$ có $\\widehat{B} = \\widehat{E} = %s^\\circ$ như hình vẽ. Biết $%s B = \\dfrac{%s}{%s}$, tỉ số nào sau đây cũng bằng $%s %s^\\circ$?
%s''' % (goc_nhon, ten_ts, c1_abc, c2_abc, ten_ts, goc_nhon, hinh_ve))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''Xét $\\triangle ABC$ vuông tại $A$ và $\\triangle DEF$ vuông tại $D$ có $\\widehat{B} = \\widehat{E} = %s^\\circ$. \\\\
Suy ra $\\triangle ABC \\backsim \\triangle DEF$ (g.g). \\\\
Do đó tỉ số các cạnh tương ứng bằng nhau: $\\dfrac{%s}{%s} = \\dfrac{%s}{%s}$. \\\\
Vậy $%s %s^\\circ = %s E = \\dfrac{%s}{%s}$.'''
                   % (goc_nhon, c1_abc, c2_abc, d1, d2, ten_ts, goc_nhon, ten_ts, d1, d2))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
