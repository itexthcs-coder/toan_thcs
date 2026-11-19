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


def bt_dang4_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_canh = random.randint(4, 12)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (90:1.8);
\\coordinate (B) at (18:1.8);
\\coordinate (C) at (-54:1.8);
\\coordinate (D) at (-126:1.8);
\\coordinate (E) at (162:1.8);
\\coordinate (M) at (intersection of B--E and A--C);
\\coordinate (N) at (intersection of A--C and B--D);
\\coordinate (P) at (intersection of B--D and C--E);
\\coordinate (Q) at (intersection of C--E and D--A);
\\coordinate (K) at (intersection of D--A and E--B);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--cycle;
\\draw[line width=1pt, dashed] (A)--(C)--(E)--(B)--(D)--cycle;
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (Q) circle (1pt) node[below left] {$Q$};
\\fill (K) circle (1pt) node[left] {$K$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho ngũ giác đều $ABCDE$ có cạnh bằng $%s\\text{ cm}$ nội tiếp đường tròn $(O)$ (như hình vẽ). Các đường chéo $AC, BD, CE, DA, EB$ cắt nhau tạo thành ngũ giác $MNPQK$ ở miền trong của ngũ giác $ABCDE$ (trong đó $M$ là giao điểm của $BE$ và $AC$, $N$ là giao điểm của $AC$ và $BD$, $P$ là giao điểm của $BD$ và $CE$, $Q$ là giao điểm của $CE$ và $DA$, $K$ là giao điểm của $DA$ và $EB$). Chứng minh rằng $MNPQK$ là một ngũ giác đều. %s'''
                         % (a_canh, hinh_tikz))

        loigiai = ('''Ngũ giác đều $ABCDE$ nội tiếp đường tròn $(O)$ chia đường tròn thành $5$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $\\frac{360^\\circ}{5} = 72^\\circ$. \\\\
Xét $\\triangle ABN$, ta có $\\widehat{BAN} = \\widehat{BAC} = \\frac{1}{2}\\text{sđ}\\wideparen{BC} = 36^\\circ$ và $\\widehat{ABN} = \\widehat{ABD} = \\frac{1}{2}\\text{sđ}\\wideparen{AD} = 36^\\circ$. \\\\
Suy ra $\\triangle ABN$ cân tại $N$ và $\\widehat{ANB} = 180^\\circ - 36^\\circ - 36^\\circ = 108^\\circ$. \\\\
Do đó góc trong $\\widehat{MNP}$ của ngũ giác $MNPQK$ (đối đỉnh với $\\widehat{ANB}$) bằng $108^\\circ$. \\\\
Chứng minh tương tự cho năm tam giác cân bằng nhau $\\triangle ABN = \\triangle BCP = \\triangle CDQ = \\triangle DEK = \\triangle EAM$ (g.c.g), ta suy ra: \\\\
- Năm góc trong tại các đỉnh $M, N, P, Q, K$ của ngũ giác lồi $MNPQK$ đều bằng $108^\\circ$. \\\\
- Các đoạn thẳng $AN = NB = BP = PC = CQ = QD = DK = KE = EM = MA$. \\\\
Mặt khác, năm đường chéo của ngũ giác đều bằng nhau ($AC = BD = CE = DA = EB$) và $AC = AM + MN + NC$, suy ra:
$$MN = NP = PQ = QK = KM.$$
Vậy $MNPQK$ là một ngũ giác đều.''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
