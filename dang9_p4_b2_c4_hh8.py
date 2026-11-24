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


def fmt_num(val):
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def bt_dang9_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mn = random.choice([3, 4, 5, 6, 7])
        de = mn * 4
        pq = mn * 3

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.6);
\\coordinate (B) at (1.0,1.8);
\\coordinate (C) at (3.2,1.8);
\\coordinate (D) at (0.2,0);
\\coordinate (E) at (4.6,0);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(A)!0.5!(C)$);
\\coordinate (P) at ($(B)!0.5!(D)$);
\\coordinate (Q) at ($(C)!0.5!(E)$);
\\draw[line width=1pt] (A)--(D)--(E)--cycle (B)--(C) (M)--(N) (P)--(Q);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (Q) circle (1pt) node[right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ có $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Gọi $D$ là điểm đối xứng với $A$ qua $B$, $E$ là điểm đối xứng với $A$ qua $C$. Biết $MN = %s\\text{ cm}$ (như hình vẽ).\\
a) Chứng minh $MN // DE$ và tính độ dài đoạn thẳng $DE$.\\
b) Gọi $P, Q$ lần lượt là trung điểm của $BD$ và $CE$. Chứng minh tứ giác $MPQN$ là hình thang và tính độ dài đoạn thẳng $PQ$.%s''' % (fmt_num(mn), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $M, N$ lần lượt là trung điểm của $AB$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$, suy ra $MN // BC$ và $BC = 2MN = 2 \\cdot %s = %s\\text{ cm}$.\\
Vì $D$ đối xứng với $A$ qua $B$ và $E$ đối xứng với $A$ qua $C$ nên $B, C$ lần lượt là trung điểm của $AD$ và $AE$.\\
Do đó $BC$ là đường trung bình của tam giác $ADE$, suy ra $BC // DE$ và $DE = 2BC = 2 \\cdot %s = %s\\text{ cm}$.\\
Vì $MN // BC$ và $BC // DE$ nên $MN // DE$.
\\item Xét hình thang $BCED$ ($BC // DE$) có $P, Q$ lần lượt là trung điểm của hai cạnh bên $BD$ và $CE$.\\
Gọi $I$ là trung điểm của đường chéo $BE$. Áp dụng tính chất đường trung bình cho hai tam giác $BED$ và $BEC$, ta có $PI // DE$, $PI = \\dfrac{1}{2}DE$ và $IQ // BC$, $IQ = \\dfrac{1}{2}BC$.\\
Suy ra ba điểm $P, I, Q$ thẳng hàng, $PQ // BC // DE$ và $PQ = \\dfrac{BC + DE}{2} = \\dfrac{%s + %s}{2} = %s\\text{ cm}$.\\
Vì $MN // BC$ và $PQ // BC$ nên $MN // PQ$, suy ra tứ giác $MPQN$ là hình thang.
\\end{enumEX}''' % (fmt_num(mn), fmt_num(2*mn), fmt_num(2*mn), fmt_num(de), fmt_num(2*mn), fmt_num(de), fmt_num(pq)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
