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

def bt_dang13_p4_b2_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([6, 8, 10, 12])
        cd = ab + random.choice([6, 8, 10, 12])
        mn = (cd - ab) // 2

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.0,2.6);
\\coordinate (B) at (2.8,2.6);
\\coordinate (C) at (4.8,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(C)!0.5!(D)$);
\\coordinate (E) at (1.8,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N) (B)--(E);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (E) circle (1pt) node[below] {$E$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hình thang $ABCD$ ($AB // CD$) có $\\widehat{C} + \\widehat{D} = 90^\\circ$, $AB = %s\\text{ cm}$ và $CD = %s\\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của hai đáy $AB$ và $CD$ (như hình vẽ).\\
a) Qua $B$ kẻ đường thẳng song song với $AD$ cắt $CD$ tại $E$. Chứng minh tam giác $BEC$ vuông tại $B$.\\
b) Chứng minh $MN = \\dfrac{CD - AB}{2}$ và tính độ dài đoạn thẳng $MN$.%s''' % (fmt_num(ab), fmt_num(cd), hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $BE // AD$ nên $\\widehat{BEC} = \\widehat{D}$ (hai góc đồng vị).\\
Xét tam giác $BEC$, ta có $\\widehat{BEC} + \\widehat{C} = \\widehat{D} + \\widehat{C} = 90^\\circ$ (giả thiết).\\
Suy ra $\\widehat{EBC} = 180^\\circ - (\\widehat{BEC} + \\widehat{C}) = 90^\\circ$, hay tam giác $BEC$ vuông tại $B$.
\\item Tứ giác $ABED$ có $AB // DE$ và $BE // AD$ nên $ABED$ là hình bình hành, suy ra $DE = AB$ và $BE = AD$.\\
Do đó $EC = CD - DE = CD - AB$.\\
Gọi $I$ là trung điểm của $EC$. Ta có $NI = |NC - IC| = \\left|\\dfrac{CD}{2} - \\dfrac{CD - AB}{2}\\right| = \\dfrac{AB}{2} = MB$.\\
Tứ giác $MBIN$ có $MB // NI$ (do $AB // CD$) và $MB = NI$ nên $MBIN$ là hình bình hành, suy ra $MN = BI$.\\
Trong tam giác $BEC$ vuông tại $B$, $BI$ là đường trung tuyến ứng với cạnh huyền $EC$ nên $BI = \\dfrac{1}{2}EC = \\dfrac{CD - AB}{2}$.\\
Vậy $MN = \\dfrac{CD - AB}{2} = \\dfrac{%s - %s}{2} = %s\\text{ cm}$.
\\end{enumEX}''' % (fmt_num(cd), fmt_num(ab), fmt_num(mn)))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
