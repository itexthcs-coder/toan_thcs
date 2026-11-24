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


def bt_dang4_p4_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 4])
        am = 2 * k
        mb = 3 * k
        an = 4 * k
        nc = 6 * k
        ac = an + nc
        bc = 4 * k
        cp = 6 * k
        bp = bc + cp
        ts = Rational(2, 3)

        noidungcauhoi = ("""Cho $\\Delta ABC$, trên cạnh $AB$ lấy điểm $M$ sao cho $AM = %s\\text{ cm}$, $MB = %s\\text{ cm}$. Trên cạnh $AC$ lấy điểm $N$ sao cho $AN = %s\\text{ cm}$, $NC = %s\\text{ cm}$. Trên tia đối của tia $CB$ lấy điểm $P$ sao cho $CP = %s\\text{ cm}$, biết độ dài cạnh $BC = %s\\text{ cm}$ (như hình vẽ bên dưới). \\\\
a) Chứng minh rằng $MN // BC$. \\\\
b) Chứng minh rằng $NP // AB$.
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (2.5,0);
\\coordinate (P) at (5.5,0);
\\coordinate (M) at ($(A)!0.4!(B)$);
\\coordinate (N) at ($(A)!0.4!(C)$);
\\draw[line width=1pt] (A)--(B)--(P) (A)--(C) (M)--(N) (N)--(P);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[above right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                         % (am, mb, an, nc, cp, bc))

        loigiai = ("""\\begin{enumEX}[a)]{1}
\\item Xét $\\Delta ABC$ có $M \\in AB$, $N \\in AC$, ta có: \\\\
$\\dfrac{AM}{MB} = \\dfrac{%s}{%s} = %s$ và $\\dfrac{AN}{NC} = \\dfrac{%s}{%s} = %s$. \\\\
Vì $\\dfrac{AM}{MB} = \\dfrac{AN}{NC} = %s$ nên $MN // BC$ (theo định lí Thalès đảo).
\\item Ta có $AC = AN + NC = %s + %s = %s\\text{ (cm)}$ và $BP = BC + CP = %s + %s = %s\\text{ (cm)}$. \\\\
Xét $\\Delta ABP$ có $N \\in AC$, $C \\in BP$, ta có: \\\\
$\\dfrac{CN}{CA} = \\dfrac{%s}{%s} = \\dfrac{3}{5}$ và $\\dfrac{CP}{BP} = \\dfrac{%s}{%s} = \\dfrac{3}{5}$. \\\\
Vì $\\dfrac{CN}{CA} = \\dfrac{CP}{BP} = \\dfrac{3}{5}$ nên $NP // AB$ (theo định lí Thalès đảo).
\\end{enumEX}"""
                   % (am, mb, latex(ts), an, nc, latex(ts), latex(ts),
                      an, nc, ac, bc, cp, bp,
                      nc, ac, cp, bp))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
