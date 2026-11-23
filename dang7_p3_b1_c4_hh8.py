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


def bt_dang7_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # OA / OC = 2 / 5; OB = m + 1; OD = 3m - 1 => 2/5 = (m+1)/(3m-1) => 6m - 2 = 5m + 5 => m = 7
        k = random.choice([2, 3])
        oa = 2 * k
        oc = 5 * k
        c_sub = random.choice([1, 2, 3])
        # (m + 1) / (3m - c_sub) = 2 / 5 => 6m - 2*c_sub = 5m + 5 => m = 5 + 2*c_sub
        m_val = 5 + 2 * c_sub
        kq_str = str(m_val)

        noidungcauhoi = ("""Cho hai đoạn thẳng $AC$ và $BD$ cắt nhau tại $O$ sao cho $OA = %s\\text{ cm}$, $OC = %s\\text{ cm}$, $OB = m + 1\\text{ (cm)}$ và $OD = 3m - %s\\text{ (cm)}$ (với $m > 1$) như hình vẽ bên dưới. Giá trị của $m$ để $AB // CD$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (2,1.6);
\\coordinate (A) at (0.6,3);
\\coordinate (B) at (3.2,3);
\\coordinate (C) at (3.8,0);
\\coordinate (D) at (0.4,0);
\\draw[line width=1pt] (A)--(B)--(D)--(C)--cycle;
\\fill (O) circle (1pt) node[right] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\end{tikzpicture}
\\end{center}"""
                         % (oa, oc, c_sub))

        loigiai = ("""Trên tia đối của tia $OC$ lấy điểm $A'$ sao cho $OA' = OA = %s\\text{ cm}$, trên tia đối của tia $OD$ lấy điểm $B'$ sao cho $OB' = OB = m + 1\\text{ (cm)}$. \\\\
Khi đó $AB // A'B'$, nên để $AB // CD$ thì $A'B' // CD$. \\\\
Xét $\\Delta OCD$, theo định lí Thalès đảo, để $A'B' // CD$ thì: \\\\
$\\dfrac{OA'}{OC} = \\dfrac{OB'}{OD}$ hay $\\dfrac{OA}{OC} = \\dfrac{OB}{OD}$. \\\\
Thay các giá trị vào hệ thức trên, ta được: \\\\
$\\dfrac{%s}{%s} = \\dfrac{m + 1}{3m - %s} \\Leftrightarrow \\dfrac{2}{5} = \\dfrac{m + 1}{3m - %s}$ \\\\
$\\Rightarrow 2(3m - %s) = 5(m + 1) \\Leftrightarrow 6m - %s = 5m + 5 \\Leftrightarrow m = %s$ (thỏa mãn $m > 1$). \\\\
Vậy giá trị cần tìm là $m = %s$."""
                   % (oa, oa, oc, c_sub, c_sub, c_sub, 2 * c_sub, m_val, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
