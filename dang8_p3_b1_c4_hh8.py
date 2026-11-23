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


def bt_dang8_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([3, 4])
        b = a + 4
        k1 = random.choice([2, 3])
        ab = a * k1
        cd = b * k1
        ad = (a + b) * random.choice([1, 2])
        if ad == 10:
            ad = 15
            # a=3, b=7 => a+b=10 => ad = 15 => am = 4.5
            a, b = 3, 7
            ab = 3 * k1
            cd = 7 * k1
        am_val = Rational(a * ad, a + b)
        if am_val.is_Integer:
            kq_str = str(int(am_val))
        else:
            kq_str = str(float(am_val)).replace('.', ',')

        noidungcauhoi = ("""Cho hình thang $ABCD$ ($AB // CD$) có $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$. Hai đường chéo $AC$ và $BD$ cắt nhau tại $O$. Qua $O$ kẻ đường thẳng song song với hai đáy, cắt cạnh bên $AD$ tại $M$ và cắt cạnh bên $BC$ tại $N$ (như hình vẽ bên dưới). Biết $AD = %s\\text{ cm}$, độ dài đoạn thẳng $AM$ bằng bao nhiêu $\\text{cm}$?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (0,0);
\\coordinate (C) at (5,0);
\\coordinate (A) at (1.2,2.8);
\\coordinate (B) at (3.6,2.8);
\\coordinate (O) at (intersection of A--C and B--D);
\\coordinate (M) at ($(A)!0.3!(D)$);
\\coordinate (N) at ($(B)!0.3!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N);
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                         % (ab, cd, ad))

        loigiai = ("""Trên tia đối của tia $OC$ lấy điểm $A'$ sao cho $OA' = OA$, trên tia đối của tia $OD$ lấy điểm $B'$ sao cho $OB' = OB$. \\\\
Khi đó $A'B' = AB = %s\\text{ cm}$ và $A'B' // AB // CD$. \\\\
Xét $\\Delta OCD$ có $A'B' // CD$, theo định lí Thalès ta có: $\\dfrac{OA'}{OC} = \\dfrac{A'B'}{CD} \\Rightarrow \\dfrac{OA}{OC} = \\dfrac{AB}{CD} = \\dfrac{%s}{%s} = \\dfrac{%s}{%s}$. \\\\
Suy ra $\\dfrac{OA}{OA + OC} = \\dfrac{%s}{%s + %s} = \\dfrac{%s}{%s}$ hay $\\dfrac{OA}{AC} = \\dfrac{%s}{%s}$. \\\\
Xét $\\Delta ADC$ có $MO // CD$, theo định lí Thalès trong tam giác ta có: \\\\
$\\dfrac{AM}{AD} = \\dfrac{OA}{AC} = \\dfrac{%s}{%s} \\Rightarrow AM = \\dfrac{%s}{%s} \\cdot %s = %s\\text{ (cm)}$. \\\\
Vậy độ dài đoạn thẳng $AM$ bằng $%s\\text{ cm}$."""
                   % (ab, ab, cd, a, b, a, a, b, a, a + b, a, a + b,
                      a, a + b, a, a + b, ad, kq_str, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
