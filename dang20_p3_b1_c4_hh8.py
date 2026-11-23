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


def bt_dang20_p3_b1_c4_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([1, 2])
        ce = 10 * k
        ek = 15 * k
        kb = 5 * k
        bc = ce + ek + kb
        ac = 36 * k
        dh = (ek * ac) // bc
        kq_str = str(dh)

        noidungcauhoi = ("""Một đường ống thoát nước thẳng dài $AC = %s\\text{ m}$ đặt nghiêng từ tầng thượng xuống mặt đất nằm ngang $BC$ (tạo với phương thẳng đứng $AB$ một tam giác vuông $ABC$ vuông tại $B$). Kĩ sư lắp hai trụ đỡ thẳng đứng $DE$ và $HK$ vuông góc với mặt đất $BC$ ($D, H \\in AC$ và $E, K \\in BC$) như hình vẽ bên dưới. Biết khoảng cách trên mặt đất $CE = %s\\text{ m}$, $EK = %s\\text{ m}$ và $KB = %s\\text{ m}$. Độ dài đoạn ống $DH$ nằm giữa hai trụ đỡ bằng bao nhiêu mét?
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (A) at (0,3);
\\coordinate (C) at (4.8,0);
\\coordinate (E) at (3.2,0);
\\coordinate (D) at (3.2,1.0);
\\coordinate (K) at (0.8,0);
\\coordinate (H) at (0.8,2.5);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E) (H)--(K);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (3.2,0.25)--(3.45,0.25)--(3.45,0);
\\draw[line width=1pt] (0.8,0.25)--(1.05,0.25)--(1.05,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\fill (E) circle (1pt) node[below] {$E$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\end{tikzpicture}
\\end{center}"""
                         % (ac, ce, ek, kb))

        loigiai = ("""Ta có chiều dài đoạn mặt đất $BC$ là: $BC = CE + EK + KB = %s + %s + %s = %s\\text{ (m)}$. \\\\
Vì các trụ đỡ $DE$, $HK$ và tường $AB$ cùng vuông góc với mặt đất $BC$ nên $DE // HK // AB$. \\\\
Xét $\\Delta CAB$ có $DE // AB$, theo định lí Thalès ta có: $\\dfrac{CD}{AC} = \\dfrac{CE}{BC} = \\dfrac{%s}{%s} = \\dfrac{1}{3} \\Rightarrow CD = \\dfrac{1}{3} \\cdot %s = %s\\text{ (m)}$. \\\\
Xét $\\Delta CAB$ có $HK // AB$, theo định lí Thalès ta có: $\\dfrac{CH}{AC} = \\dfrac{CK}{BC} = \\dfrac{%s + %s}{%s} = \\dfrac{5}{6} \\Rightarrow CH = \\dfrac{5}{6} \\cdot %s = %s\\text{ (m)}$. \\\\
Vậy độ dài đoạn ống $DH$ nằm giữa hai trụ đỡ là: $DH = CH - CD = %s - %s = %s\\text{ (m)}$."""
                   % (ce, ek, kb, bc,
                      ce, bc, ac, ac // 3,
                      ce, ek, bc, ac, (5 * ac) // 6,
                      (5 * ac) // 6, ac // 3, dh))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
