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


def bt_dang7_p4_b1_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 12)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (210:2);\n'
            '\\coordinate (B) at (330:2);\n'
            '\\coordinate (M) at (270:2);\n'
            '\\coordinate (C) at (125:2);\n'
            '\\coordinate (D) at (55:2);\n'
            '\\coordinate (E) at (intersection of M--C and A--B);\n'
            '\\coordinate (F) at (intersection of M--D and A--B);\n'
            '\\draw[line width=1pt] (O) circle (2cm);\n'
            '\\draw[line width=1pt] (A)--(B) (M)--(C)--(D)--cycle (M)--(A)--(C);\n'
            '\\fill (O) circle (1pt) node[above] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (M) circle (1pt) node[below] {$M$};\n'
            '\\fill (C) circle (1pt) node[above left] {$C$};\n'
            '\\fill (D) circle (1pt) node[above right] {$D$};\n'
            '\\fill (E) circle (1pt) node[above left] {$E$};\n'
            '\\fill (F) circle (1pt) node[above right] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho đường tròn $(O; %s\\text{ cm})$ và dây cung $AB$ không đi qua tâm. Gọi $M$ là điểm chính giữa của cung nhỏ $AB$. Qua $M$ vẽ hai dây cung $MC$ và $MD$ cắt dây $AB$ lần lượt tại $E$ và $F$ ($E$ nằm giữa $A$ và $F$) như hình vẽ.\\\\'
            'a) Chứng minh $\\widehat{MCA} = \\widehat{MAB}$ và $\\triangle MEA \\backsim \\triangle MAC$.\\\\'
            'b) Chứng minh $MA^2 = ME \\cdot MC = MF \\cdot MD$.\\\\'
            'c) Chứng minh $\\widehat{EFD} + \\widehat{ECD} = 180^\\circ$.\n%s'
            % (R, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Vì $M$ là điểm chính giữa cung nhỏ $AB$ của đường tròn $(O; %s\\text{ cm})$ nên $\\text{sđ}\\overset\\frown{MA} = \\text{sđ}\\overset\\frown{MB}$. Hai góc nội tiếp $\\widehat{MCA}$ và $\\widehat{MAB}$ lần lượt chắn hai cung bằng nhau $MA$ và $MB$ nên $\\widehat{MCA} = \\widehat{MAB}$.\\\\'
            'Xét $\\triangle MEA$ và $\\triangle MAC$ có $\\widehat{AME}$ chung và $\\widehat{MAE} = \\widehat{MCA}$ nên $\\triangle MEA \\backsim \\triangle MAC$ (g.g).\n'
            '\\item Từ $\\triangle MEA \\backsim \\triangle MAC$, ta suy ra $\\dfrac{ME}{MA} = \\dfrac{MA}{MC} \\Rightarrow MA^2 = ME \\cdot MC$.\\\\'
            'Chứng minh hoàn toàn tương tự, ta có $\\triangle MFA \\backsim \\triangle MAD$ (g.g), suy ra $MA^2 = MF \\cdot MD$. Vậy $MA^2 = ME \\cdot MC = MF \\cdot MD$.\n'
            '\\item Từ $ME \\cdot MC = MF \\cdot MD \\Rightarrow \\dfrac{ME}{MD} = \\dfrac{MF}{MC}$. Xét $\\triangle MEF$ và $\\triangle MDC$ có $\\widehat{EMF}$ chung và $\\dfrac{ME}{MD} = \\dfrac{MF}{MC}$ nên $\\triangle MEF \\backsim \\triangle MDC$ (c.g.c), suy ra $\\widehat{MFE} = \\widehat{MCD}$.\\\\'
            'Vì $\\widehat{MFE} + \\widehat{EFD} = 180^\\circ$ (hai góc kề bù) và $\\widehat{MFE} = \\widehat{MCD} = \\widehat{ECD}$ nên $\\widehat{EFD} + \\widehat{ECD} = 180^\\circ$.\n'
            '\\end{enumEX}'
            % (R)
        )

    # Xuất câu hỏi với lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
