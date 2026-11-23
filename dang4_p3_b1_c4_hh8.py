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


def bt_dang4_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m = random.choice([2, 3])
        # BM = m * MC => BM / BC = m / (m + 1) => BM / AD = m / (m + 1)
        # BI / ID = BM / AD = m / (m + 1) => BI / BD = m / (2m + 1)
        tong_p = 2 * m + 1
        bd = tong_p * random.randint(2, 5)
        bi = (m * bd) // tong_p
        ab = random.randint(12, 24)
        kq_str = str(bi)

        noidungcauhoi = ("""Cho hình bình hành $ABCD$ có cạnh $AB = %s\\text{ cm}$ và đường chéo $BD = %s\\text{ cm}$. Trên cạnh $BC$ lấy điểm $M$ sao cho $BM = %s MC$. Tia $AM$ cắt đường chéo $BD$ tại $I$ (như hình vẽ bên dưới). Độ dài đoạn thẳng $BI$ bằng bao nhiêu $\\text{cm}$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (4.5,0);
\\coordinate (D) at (1.2,2.6);
\\coordinate (C) at (5.7,2.6);
\\coordinate (M) at ($(B)!0.6667!(C)$);
\\coordinate (I) at (intersection of A--M and B--D);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (B)--(D) (A)--(M);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (M) circle (1pt) node[right] {$M$};
\\fill (I) circle (1pt) node[above] {$I$};
\\end{tikzpicture}
\\end{center}"""
                         % (ab, bd, m))

        loigiai = ("""Vì $ABCD$ là hình bình hành nên $AD = BC$ và $AD // BC$. \\\\
Vì $BM = %s MC$ nên $BC = BM + MC = %s MC + MC = %s MC$, suy ra $\\dfrac{BM}{BC} = \\dfrac{%s}{%s}$, do đó $\\dfrac{BM}{AD} = \\dfrac{%s}{%s}$. \\\\
Xét $\\Delta IAD$ có $BM // AD$ (do $BC // AD$), theo định lí Thalès ta có: \\\\
$\\dfrac{BI}{ID} = \\dfrac{BM}{AD} = \\dfrac{%s}{%s} \\Rightarrow \\dfrac{BI}{BI + ID} = \\dfrac{%s}{%s + %s} = \\dfrac{%s}{%s}$ hay $\\dfrac{BI}{BD} = \\dfrac{%s}{%s}$. \\\\
Thay $BD = %s\\text{ cm}$ vào hệ thức trên, ta được: $BI = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$. \\\\
Vậy độ dài đoạn thẳng $BI$ bằng $%s\\text{ cm}$."""
                   % (m, m, m + 1, m, m + 1, m, m + 1,
                      m, m + 1, m, m, m + 1, m, tong_p, m, tong_p,
                      bd, m, tong_p, bd, bi, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
