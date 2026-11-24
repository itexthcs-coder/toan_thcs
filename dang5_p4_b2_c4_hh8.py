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

def bt_dang5_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bc = random.choice([12, 16, 20, 24, 28])
        de = bc // 4

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(A)!0.5!(C)$);
\\coordinate (D) at ($(A)!0.5!(M)$);
\\coordinate (E) at ($(A)!0.5!(N)$);
\\coordinate (H) at ($(B)!0.5!(N)$);
\\coordinate (K) at ($(C)!0.5!(M)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (D)--(E) (B)--(N) (C)--(M) (H)--(K) (D)--(H) (E)--(K);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (H) circle (1pt) node[below] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ có $BC = %s\\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của $AB, AC$; gọi $D, E$ lần lượt là trung điểm của $AM, AN$; gọi $H, K$ lần lượt là trung điểm của $BN$ và $CM$ (như hình vẽ).\\
a) Chứng minh $DE // BC$ và tính độ dài $DE$.\\
b) Chứng minh $HK // BC$ và tính độ dài $HK$.\\
c) Chứng minh tứ giác $DEKH$ là hình bình hành.%s''' % (fmt_num(bc), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $M, N$ lần lượt là trung điểm của $AB$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$, suy ra $MN // BC$ và $MN = \\dfrac{1}{2}BC$.\\
Xét tam giác $AMN$ có $D, E$ lần lượt là trung điểm của $AM$ và $AN$ nên $DE$ là đường trung bình của tam giác $AMN$, suy ra $DE // MN$ và $DE = \\dfrac{1}{2}MN$.\\
Do đó $DE // BC$ và $DE = \\dfrac{1}{4}BC = \\dfrac{1}{4} \\cdot %s = %s\\text{ cm}$.
\\item Xét hình thang $BCNM$ ($MN // BC$), gọi $P$ là trung điểm của cạnh bên $BM$.\\
Xét tam giác $BMN$ có $P$ là trung điểm $BM$ và $H$ là trung điểm $BN$ nên $PH$ là đường trung bình của tam giác $BMN$, suy ra $PH // MN$ và $PH = \\dfrac{1}{2}MN$.\\
Xét tam giác $BMC$ có $P$ là trung điểm $BM$ và $K$ là trung điểm $CM$ nên $PK$ là đường trung bình của tam giác $BMC$, suy ra $PK // BC$ và $PK = \\dfrac{1}{2}BC$.\\
Vì $MN // BC$ nên qua $P$ có $PH$ và $PK$ cùng song song với $BC$, suy ra ba điểm $P, H, K$ thẳng hàng.\\
Do đó $HK // BC$ và $HK = PK - PH = \\dfrac{1}{2}BC - \\dfrac{1}{2}MN = \\dfrac{1}{2}BC - \\dfrac{1}{4}BC = \\dfrac{1}{4}BC = %s\\text{ cm}$.
\\item Từ câu a) và câu b), ta có $DE // HK$ (cùng song song với $BC$) và $DE = HK = %s\\text{ cm}$.\\
Tứ giác $DEKH$ có hai cạnh đối $DE$ và $HK$ vừa song song vừa bằng nhau nên $DEKH$ là hình bình hành.
\\end{enumEX}''' % (fmt_num(bc), fmt_num(de), fmt_num(de), fmt_num(de)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
