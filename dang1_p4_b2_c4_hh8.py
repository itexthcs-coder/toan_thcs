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

def bt_dang1_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_diem = random.choice([
            ('A', 'B', 'C', 'D', 'E', 'F', 'M', 'N', 'O'),
            ('M', 'N', 'P', 'D', 'E', 'F', 'H', 'K', 'I')
        ])
        A, B, C, D, E, F, M, N, O = bo_diem

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (%s) at (1.5,3.2);
\\coordinate (%s) at (0,0);
\\coordinate (%s) at (4.8,0);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\coordinate (%s) at ($(%s)!0.5!(%s)$);
\\draw[line width=1pt] (%s)--(%s)--(%s)--cycle (%s)--(%s)--(%s)--cycle (%s)--(%s) (%s)--(%s);
\\fill (%s) circle (1pt) node[above] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[below] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[left] {$%s$};
\\fill (%s) circle (1pt) node[right] {$%s$};
\\fill (%s) circle (1pt) node[above left] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, B, C, E, A, C, F, A, B, M, A, F, N, D, E, O, A, D, A, B, C, D, E, F, A, D, M, N, A, A, B, B, C, C, D, D, E, E, F, F, M, M, N, N, O, O))

        noidungcauhoi = ('''Cho tam giác $%(A)s%(B)s%(C)s$ ($%(A)s%(B)s < %(A)s%(C)s$). Gọi $%(D)s, %(E)s, %(F)s$ lần lượt là trung điểm của các cạnh $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$.\\
a) Chứng minh tứ giác $%(A)s%(E)s%(D)s%(F)s$ là hình bình hành.\\
b) Chứng minh hai đoạn thẳng $%(A)s%(D)s$ và $%(E)s%(F)s$ cắt nhau tại trung điểm $%(O)s$ của mỗi đoạn.\\
c) Gọi $%(M)s, %(N)s$ lần lượt là trung điểm của $%(A)s%(F)s$ và $%(D)s%(E)s$. Chứng minh ba đường thẳng $%(A)s%(D)s, %(E)s%(F)s, %(M)s%(N)s$ đồng quy tại $%(O)s$.%(hinhve)s''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'M': M, 'N': N, 'O': O, 'hinhve': hinhve})

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $%(A)s%(B)s%(C)s$ có $%(D)s, %(E)s, %(F)s$ lần lượt là trung điểm của $%(B)s%(C)s, %(C)s%(A)s, %(A)s%(B)s$ nên $%(D)s%(E)s$ và $%(D)s%(F)s$ là các đường trung bình của tam giác $%(A)s%(B)s%(C)s$.\\
Theo tính chất đường trung bình của tam giác, ta có $%(D)s%(E)s // %(A)s%(B)s$ và $%(D)s%(F)s // %(A)s%(C)s$, hay $%(D)s%(E)s // %(A)s%(F)s$ và $%(D)s%(F)s // %(A)s%(E)s$.\\
Tứ giác $%(A)s%(E)s%(D)s%(F)s$ có các cặp cạnh đối song song nên $%(A)s%(E)s%(D)s%(F)s$ là hình bình hành.
\\item Vì $%(A)s%(E)s%(D)s%(F)s$ là hình bình hành nên hai đường chéo $%(A)s%(D)s$ và $%(E)s%(F)s$ cắt nhau tại trung điểm của mỗi đường.\\
Mà $%(O)s$ là giao điểm của $%(A)s%(D)s$ và $%(E)s%(F)s$ nên $%(O)s$ là trung điểm của cả hai đoạn thẳng $%(A)s%(D)s$ và $%(E)s%(F)s$.
\\item Vì $%(A)s%(E)s%(D)s%(F)s$ là hình bình hành nên $%(A)s%(F)s // %(D)s%(E)s$ và $%(A)s%(F)s = %(D)s%(E)s$.\\
Mà $%(M)s, %(N)s$ lần lượt là trung điểm của $%(A)s%(F)s$ và $%(D)s%(E)s$ nên $%(A)s%(M)s = \\dfrac{1}{2}%(A)s%(F)s$ và $%(D)s%(N)s = \\dfrac{1}{2}%(D)s%(E)s$.\\
Suy ra $%(A)s%(M)s // %(D)s%(N)s$ và $%(A)s%(M)s = %(D)s%(N)s$, do đó tứ giác $%(A)s%(N)s%(D)s%(M)s$ là hình bình hành.\\
Suy ra hai đường chéo $%(A)s%(D)s$ và $%(M)s%(N)s$ cắt nhau tại trung điểm của mỗi đường. Mà $%(O)s$ là trung điểm của $%(A)s%(D)s$ nên $%(M)s%(N)s$ cũng đi qua $%(O)s$.\\
Vậy ba đường thẳng $%(A)s%(D)s, %(E)s%(F)s, %(M)s%(N)s$ đồng quy tại $%(O)s$.
\\end{enumEX}''' % {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'M': M, 'N': N, 'O': O})

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
