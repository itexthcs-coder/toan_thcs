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
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang3_p4_b3_c4_hh8(self):
    # Dạng 3: Vận dụng tính chất đường phân giác của hai tam giác kề nhau qua đường trung tuyến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p = random.choice([2, 3, 4])
        q = random.choice([3, 4, 5])
        while p >= q or math.gcd(p, q) != 1:
            p = random.choice([2, 3, 4])
            q = random.choice([3, 4, 5])
        k = random.choice([2, 3])
        am = p * k
        mb = q * k
        bc = 2 * mb
        de_val = round(bc * p / (p + q), 2)
        s_de = fmt_num(de_val)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (1.8,3.4);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.6,0);\n'
            '\\coordinate (M) at ($(B)!0.5!(C)$);\n'
            '\\coordinate (D) at ($(A)!0.43!(B)$);\n'
            '\\coordinate (E) at ($(A)!0.43!(C)$);\n'
            '\\coordinate (I) at (intersection of A--M and D--E);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(M) (M)--(D)--(E)--cycle;\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (M) circle (1pt) node[below] {$M$};\n'
            '\\fill (D) circle (1pt) node[left] {$D$};\n'
            '\\fill (E) circle (1pt) node[right] {$E$};\n'
            '\\fill (I) circle (1pt) node[above left] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho tam giác $ABC$ có đường trung tuyến $AM$ ($M \\in BC$). Tia phân giác của góc $AMB$ cắt cạnh $AB$ tại $D$, tia phân giác của góc $AMC$ cắt cạnh $AC$ tại $E$. Gọi $I$ là giao điểm của $AM$ và $DE$.\\\\\n'
            'a) Chứng minh rằng $DE // BC$.\\\\\n'
            'b) Chứng minh $I$ là trung điểm của đoạn thẳng $DE$.\\\\\n'
            'c) Tính độ dài đoạn thẳng $DE$ biết $AM = %s\\text{ cm}$ và $BC = %s\\text{ cm}$.\n%s'
            % (am, bc, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \n'
            '\\item Trong tam giác $AMB$, $MD$ là tia phân giác của góc $AMB$ nên $\\frac{DA}{DB} = \\frac{MA}{MB}$ (tính chất đường phân giác của tam giác).\\\\'
            'Trong tam giác $AMC$, $ME$ là tia phân giác của góc $AMC$ nên $\\frac{EA}{EC} = \\frac{MA}{MC}$ (tính chất đường phân giác của tam giác).\\\\'
            'Mặt khác, $MB = MC$ (do $M$ là trung điểm của $BC$). Suy ra $\\frac{DA}{DB} = \\frac{EA}{EC}$.\\\\'
            'Xét tam giác $ABC$ có $\\frac{DA}{DB} = \\frac{EA}{EC}$ nên theo định lí Thalès đảo, ta có $DE // BC$ (điều phải chứng minh). \n'
            '\\item Xét tam giác $ABM$ có $DI // BM$ (vì $DE // BC$), theo hệ quả của định lí Thalès ta có: $\\frac{DI}{BM} = \\frac{AI}{AM}$.\\\\'
            'Xét tam giác $ACM$ có $EI // CM$ (vì $DE // BC$), theo hệ quả của định lí Thalès ta có: $\\frac{EI}{CM} = \\frac{AI}{AM}$.\\\\'
            'Suy ra $\\frac{DI}{BM} = \\frac{EI}{CM}$, mà $BM = CM$ nên $DI = EI$. Mặt khác điểm $I$ nằm giữa $D$ và $E$ nên $I$ là trung điểm của đoạn thẳng $DE$. \n'
            '\\item Vì $M$ là trung điểm của $BC$ nên $MB = \\frac{BC}{2} = \\frac{%s}{2} = %s\\text{ cm}$.\\\\'
            'Ta có $\\frac{DA}{DB} = \\frac{MA}{MB} = \\frac{%s}{%s} = \\frac{%s}{%s}$, suy ra $\\frac{DA}{AB} = \\frac{%s}{%s + %s} = \\frac{%s}{%s}$.\\\\'
            'Vì $DE // BC$ nên theo hệ quả của định lí Thalès, ta có $\\frac{DE}{BC} = \\frac{DA}{AB} = \\frac{%s}{%s}$.\\\\'
            'Do đó $DE = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}$. \n'
            '\\end{enumEX} \n'
            % (bc, mb, am, mb, p, q, p, p, q, p, p + q, p, p + q, p, p + q, bc, s_de)
        )

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
