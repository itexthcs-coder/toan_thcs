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


def bt_dang5_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cap_ban_kinh = [(8, 2), (9, 4), (16, 4), (18, 2), (25, 4), (12, 3), (20, 5)]
        R1, R2 = random.choice(cap_ban_kinh)
        AM = int(math.sqrt(R1 * R2))
        BC = 2 * AM
        kq_str = str(AM)

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (Op) at (3.2,0);
\\coordinate (A) at (2.0,0);
\\coordinate (B) at (0.75, 1.85);
\\coordinate (C) at (3.65, 1.11);
\\coordinate (M) at (2.31, 1.50);
\\draw[line width=1pt] (O) circle (2.0cm);
\\draw[line width=1pt] (Op) circle (1.2cm);
\\draw[line width=1pt] (O)--(Op) (O)--(B) (Op)--(C) (B)--(C) (M)--(A);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (Op) circle (1pt) node[below] {$O'$};
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (M) circle (1pt) node[above] {$M$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc ngoài tại $A$. Một tiếp tuyến chung ngoài tiếp xúc với $(O)$ tại $B$ và tiếp xúc với $(O')$ tại $C$. Tiếp tuyến chung tại $A$ cắt $BC$ tại $M$. Tính độ dài đoạn thẳng $AM$ (đơn vị: $\\text{cm}$).\\\\
%s''' % (R1, R2, hinhve))

        loigiai = ('''Xét đường tròn $(O)$ có hai tiếp tuyến $MB$ và $MA$ cắt nhau tại $M$, theo tính chất hai tiếp tuyến cắt nhau ta có $MB = MA$. \\\\
Tương tự, xét đường tròn $(O')$ có hai tiếp tuyến $MC$ và $MA$ cắt nhau tại $M$, ta có $MC = MA$. \\\\
Suy ra $MA = MB = MC = \\dfrac{1}{2}BC$. \\\\
Mặt khác, theo công thức tính độ dài đoạn tiếp tuyến chung ngoài của hai đường tròn tiếp xúc ngoài $(O; R)$ và $(O'; R')$, ta có: \\\\
$BC = 2\\sqrt{R \\cdot R'} = 2\\sqrt{%s \\cdot %s} = 2\\sqrt{%s} = %s\\text{ (cm)}$. \\\\
Vậy $AM = \\dfrac{BC}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$.'''
                   % (R1, R2, R1 * R2, BC, BC, AM))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
