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


def bt_dang5_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        he_so = random.choice([1, 2, 3, 4])
        canh_nho_str = "a" if he_so == 1 else "%sa" % (he_so)
        canh_lon_str = "3a" if he_so == 1 else "%sa" % (3 * he_so)
        dt_kq = Rational(3 * (he_so ** 2), 2) * sqrt(3)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (90:2.1);
\\coordinate (B) at (210:2.1);
\\coordinate (C) at (330:2.1);
\\coordinate (M) at ($(A)!0.333!(B)$);
\\coordinate (N) at ($(A)!0.667!(B)$);
\\coordinate (P) at ($(B)!0.333!(C)$);
\\coordinate (Q) at ($(B)!0.667!(C)$);
\\coordinate (E) at ($(C)!0.333!(A)$);
\\coordinate (F) at ($(C)!0.667!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (M)--(F) (N)--(P) (Q)--(E);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[left] {$N$};
\\fill (P) circle (1pt) node[below] {$P$};
\\fill (Q) circle (1pt) node[below] {$Q$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (F) circle (1pt) node[right] {$F$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho tam giác đều $ABC$ có độ dài cạnh bằng $%s$ ($a > 0$). Trên các cạnh $AB, BC, CA$ lần lượt lấy các điểm $M, N$; $P, Q$; $E, F$ sao cho chín đoạn thẳng $AM, MN, NB, BP, PQ, QC, CE, EF, FA$ đều bằng $%s$ (như hình vẽ). Chứng minh rằng $MNPQEF$ là một lục giác đều và tính diện tích của lục giác đều đó theo $a$. %s'''
                         % (canh_lon_str, canh_nho_str, hinh_tikz))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Chứng minh $MNPQEF$ là lục giác đều: \\\\
Xét $\\triangle ABC$ có $\\frac{AM}{AB} = \\frac{AF}{AC} = \\frac{1}{3}$, theo định lí Thalès đảo suy ra $MF // BC$ và $\\frac{MF}{BC} = \\frac{1}{3} \\Rightarrow MF = \\frac{1}{3}BC = %s$. \\\\
Chứng minh tương tự, ta được $NP = QE = %s$. Vậy lục giác lồi $MNPQEF$ có tất cả $6$ cạnh bằng nhau và đều bằng $%s$. \\\\
Mặt khác, tam giác $AMF$ có $AM = MF = FA = %s$ nên $\\triangle AMF$ đều, suy ra $\\widehat{AMF} = 60^\\circ \\Rightarrow \\widehat{FMN} = 180^\\circ - 60^\\circ = 120^\\circ$. \\\\
Tương tự các góc trong tại các đỉnh $N, P, Q, E, F$ của lục giác $MNPQEF$ đều bằng $120^\\circ$. \\\\
Vậy $MNPQEF$ là một lục giác đều.
\\item Tính diện tích lục giác đều $MNPQEF$: \\\\
Lục giác đều $MNPQEF$ có cạnh bằng $%s$ gồm $6$ tam giác đều có cạnh bằng $%s$, do đó diện tích của lục giác đều $MNPQEF$ là:
$$S_{MNPQEF} = 6 \\cdot \\frac{(%s)^2\\sqrt{3}}{4} = %s a^2.$$'''
                   % (canh_nho_str, canh_nho_str, canh_nho_str, canh_nho_str, canh_nho_str, canh_nho_str, canh_nho_str, latex(dt_kq))) + '\\end{enumEX}'

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
