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


def bt_dang1_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([3, 4])
        ac = 2 * n * random.randint(2, 5)
        ap = ac // 2
        pq = ap // n
        kq_str = str(pq)

        noidungcauhoi = ("""Cho $\\Delta ABC$ có $AC = %s\\text{ cm}$. Gọi $M$ là trung điểm của cạnh $AB$. Trên đoạn thẳng $MB$ lấy điểm $N$ sao cho $MN = \\dfrac{1}{%s} MB$. Qua $M$ và $N$ lần lượt vẽ các đường thẳng song song với $BC$, cắt cạnh $AC$ theo thứ tự tại $P$ và $Q$ (như hình vẽ bên dưới). Độ dài đoạn thẳng $PQ$ bằng bao nhiêu $\\text{cm}$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (P) at ($(A)!0.5!(C)$);
\\coordinate (N) at ($(M)!0.3333!(B)$);
\\coordinate (Q) at ($(P)!0.3333!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(P) (N)--(Q);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (N) circle (1pt) node[left] {$N$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}"""
                         % (ac, n))

        loigiai = ("""Xét $\\Delta ABC$ có $MP // BC$ và $M$ là trung điểm của $AB$ ($AM = MB$), theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{AP}{PC} = \\dfrac{AM}{MB} = 1 \\Rightarrow AP = PC = \\dfrac{AC}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$. \\\\
Xét $\\Delta ABC$ có $NQ // BC$, theo định lí Thalès ta có: \\\\
$\\dfrac{PQ}{PC} = \\dfrac{MN}{MB} = \\dfrac{1}{%s} \\Rightarrow PQ = \\dfrac{1}{%s} \\cdot %s = %s\\text{ (cm)}$. \\\\
Vậy độ dài đoạn thẳng $PQ$ bằng $%s\\text{ cm}$."""
                   % (ac, ap, n, n, ap, pq, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
