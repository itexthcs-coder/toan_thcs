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

def bt_dang10_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2.2,3.4);
\\coordinate (B) at (0.8,1.7);
\\coordinate (C) at (3.2,1.7);
\\coordinate (D) at ($(A)!2!(C)$);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (I) at ($(B)!0.5!(D)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (C)--(D)--(B) (M)--(N)--(C) (M)--(I)--(C);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (I) circle (1pt) node[below left] {$I$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tam giác $ABC$ cân tại $A$. Trên tia đối của tia $CA$ lấy điểm $D$ sao cho $CD = CA$. Gọi $M$ là trung điểm của $AB$, $N$ là trung điểm của $BC$ (như hình vẽ).\\
a) Chứng minh $MN$ là đường trung bình của tam giác $ABC$ và $CN$ là đường trung bình của tam giác $ABD$.\\
b) Gọi $I$ là trung điểm của $BD$. Chứng minh $MI = AC$ và $CI = \\dfrac{1}{2}AB$.\\
c) Chứng minh tứ giác $AMCI$ là hình bình hành.%s''' % (hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $ABC$ có $M, N$ lần lượt là trung điểm của $AB$ và $BC$ nên $MN$ là đường trung bình của tam giác $ABC$.\\
Vì $D$ nằm trên tia đối của tia $CA$ và $CD = CA$ nên $C$ là trung điểm của $AD$.\\
Xét tam giác $ABD$ có $C$ là trung điểm của $AD$ và $N$ là trung điểm của $BC$ nên $CN$ là đường trung bình của tam giác $ABD$.
\\item Xét tam giác $ABD$ có $M$ là trung điểm của $AB$ và $I$ là trung điểm của $BD$ nên $MI$ là đường trung bình của tam giác $ABD$, suy ra $MI // AD$ (hay $MI // AC$) và $MI = \\dfrac{1}{2}AD = AC$.\\
Tương tự, $CI$ là đường trung bình của tam giác $ABD$ nên $CI // AB$ (hay $CI // AM$) và $CI = \\dfrac{1}{2}AB$.
\\item Tứ giác $AMCI$ có $MI // AC$ và $CI // AM$ nên tứ giác $AMCI$ là hình bình hành.
\\end{enumEX}''')

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
