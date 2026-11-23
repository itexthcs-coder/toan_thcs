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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang17_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mn_10 = random.choice([30, 35, 45])
        nc_10 = random.choice([24, 30, 36])
        k = random.choice([5, 6, 8])
        bc_10 = nc_10 * k
        ab_10 = mn_10 * k
        mn_s = str(mn_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
        nc_s = str(nc_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
        bc_s = str(bc_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
        ab_s = str(ab_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
        kq_str = ab_s

        noidungcauhoi = ("""Vào lúc $9\\text{ giờ}$ sáng, một tòa nhà cao tầng thẳng đứng $AB$ có bóng đổ trên sân bằng phẳng là đoạn $BC = %s\\text{ m}$. Cùng thời điểm đó, một cột cờ thẳng đứng $MN$ cao $%s\\text{ m}$ đặt sao cho đỉnh $M$ nằm trên đoạn $AC$ và chân $N$ nằm trên đoạn $BC$, có bóng đổ trên sân là đoạn $NC = %s\\text{ m}$ (như hình vẽ bên dưới). Chiều cao $AB$ của tòa nhà bằng bao nhiêu mét?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (A) at (0,3.2);
\\coordinate (C) at (4.8,0);
\\coordinate (N) at (3.6,0);
\\coordinate (M) at (3.6,0.8);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (3.6,0.25)--(3.85,0.25)--(3.85,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\end{tikzpicture}
\\end{center}"""
                         % (bc_s, mn_s, nc_s))

        loigiai = ("""Vì tòa nhà $AB$ và cột cờ $MN$ cùng thẳng đứng vuông góc với mặt sân $BC$ nên $MN // AB$. \\\\
Xét $\\Delta CAB$ có $MN // AB$ ($M \\in AC$, $N \\in BC$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{MN}{AB} = \\dfrac{CN}{CB}$. \\\\
Thay $MN = %s\\text{ m}$, $CN = %s\\text{ m}$, $CB = %s\\text{ m}$ vào hệ thức trên, ta được: \\\\
$\\dfrac{%s}{AB} = \\dfrac{%s}{%s} \\Rightarrow AB = \\dfrac{%s \\cdot %s}{%s} = %s\\text{ (m)}$. \\\\
Vậy chiều cao của tòa nhà bằng $%s\\text{ m}$."""
                   % (mn_s, nc_s, bc_s, mn_s, nc_s, bc_s, mn_s, bc_s, nc_s, ab_s, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
