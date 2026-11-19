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


def bt_dang7_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (135:1.7);
\\coordinate (B) at (90:1.7);
\\coordinate (C) at (45:1.7);
\\coordinate (D) at (0:1.7);
\\coordinate (E) at (-45:1.7);
\\coordinate (F) at (-90:1.7);
\\coordinate (G) at (-135:1.7);
\\coordinate (H) at (180:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--(F)--(G)--(H)--cycle;
\\draw[line width=1pt, dashed] (B)--(D) (A)--(E);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (E) circle (1pt) node[below right] {$E$};
\\fill (F) circle (1pt) node[below] {$F$};
\\fill (G) circle (1pt) node[below left] {$G$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Cho bát giác đều $ABCDEFGH$ nội tiếp đường tròn tâm $O$ (như hình vẽ). Chứng minh rằng tứ giác $ABDE$ là hình thang cân nội tiếp đường tròn $(O)$ và tính số đo các góc trong của tứ giác $ABDE$. %s'''
                         % (hinh_tikz))

        loigiai = ('''Bát giác đều $ABCDEFGH$ nội tiếp đường tròn $(O)$ chia đường tròn thành $8$ cung nhỏ bằng nhau, mỗi cung có số đo bằng $\\frac{360^\\circ}{8} = 45^\\circ$. \\\\
Do bốn đỉnh $A, B, D, E$ cùng nằm trên đường tròn $(O)$ nên $ABDE$ là tứ giác nội tiếp đường tròn $(O)$. \\\\
Ta có $\\text{sđ}\\wideparen{AE} = 4 \\cdot 45^\\circ = 180^\\circ$ nên $AE$ là đường kính của đường tròn $(O)$. \\\\
Xét góc nội tiếp $\\widehat{ABD}$ chắn cung nhỏ $AD$ ($3$ cung nhỏ) và góc nội tiếp $\\widehat{BAE}$ chắn cung nhỏ $BE$ ($3$ cung nhỏ):
$$\\widehat{ABD} = \\frac{1}{2}\\text{sđ}\\wideparen{AD} = \\frac{3 \\cdot 45^\\circ}{2} = 67,5^\\circ; \\qquad \\widehat{BAE} = \\frac{1}{2}\\text{sđ}\\wideparen{BE} = \\frac{3 \\cdot 45^\\circ}{2} = 67,5^\\circ.$$
Mặt khác, $\\widehat{BDE}$ là góc nội tiếp chắn cung nhỏ $BAE$ ($3$ cung nhỏ) nên $\\widehat{BDE} = 67,5^\\circ$. \\\\
Ta thấy hai góc trong cùng phía $\\widehat{ABD} + \\widehat{BDE} = 67,5^\\circ + 67,5^\\circ = 135^\\circ$ (chưa bằng $180^\\circ$), còn $\\widehat{DAE} = \\frac{1}{2}\\text{sđ}\\wideparen{DE} = 22,5^\\circ$ và $\\widehat{ADB} = \\frac{1}{2}\\text{sđ}\\wideparen{AB} = 22,5^\\circ$. \\\\
Vì $\\widehat{DAE} = \\widehat{ADB} = 22,5^\\circ$ ở vị trí so le trong nên $BD // AE$. \\\\
Do đó tứ giác $ABDE$ là hình thang. Lại có hai góc kề đáy lớn bằng nhau ($\\widehat{BAE} = \\widehat{AED} = 67,5^\\circ$) nên $ABDE$ là hình thang cân. \\\\
Các góc trong của tứ giác $ABDE$ là:
$$\\widehat{BAE} = \\widehat{AED} = 67,5^\\circ; \\qquad \\widehat{ABD} = \\widehat{BDE} = 180^\\circ - 67,5^\\circ = 112,5^\\circ.$$''')

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
