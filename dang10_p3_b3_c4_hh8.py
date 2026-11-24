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

def bt_dang10_p3_b3_c4_hh8(self):
    # Dạng 10: Tính độ dài đoạn thẳng nối trung điểm hai cạnh bên của hình thang
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ab = random.choice([5, 6, 7, 8, 9, 10])
        cd = ab + random.choice([4, 6, 8, 10])
        ef = (ab + cd) / 2
        kq_str = fmt_num(ef)

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0.8,2.6);\n'
            '\\coordinate (B) at (3.4,2.6);\n'
            '\\coordinate (C) at (4.8,0);\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (E) at ($(A)!0.5!(D)$);\n'
            '\\coordinate (F) at ($(B)!0.5!(C)$);\n'
            '\\coordinate (K) at ($(A)!0.5!(C)$);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (E)--(F);\n'
            '\\fill (A) circle (1pt) node[above left] {$A$};\n'
            '\\fill (B) circle (1pt) node[above right] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below left] {$D$};\n'
            '\\fill (E) circle (1pt) node[left] {$E$};\n'
            '\\fill (F) circle (1pt) node[right] {$F$};\n'
            '\\fill (K) circle (1pt) node[above] {$K$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho hình thang $ABCD$ ($AB // CD$) có hai đáy $AB = %s\\text{ cm}$ và $CD = %s\\text{ cm}$. Gọi $E, F$ lần lượt là trung điểm của hai cạnh bên $AD$ và $BC$. Tính độ dài đoạn thẳng $EF$ (đơn vị: $\\text{cm}$).\n%s'
            % (ab, cd, hinh_ve)
        )

        loigiai = (
            'Gọi $K$ là trung điểm của đường chéo $AC$.\\\\'
            'Trong tam giác $ADC$, $EK$ là đường trung bình nên $EK // CD$ và $EK = \\frac{1}{2}CD = \\frac{%s}{2} = %s\\text{ cm}$.\\\\'
            'Trong tam giác $ABC$, $FK$ là đường trung bình nên $FK // AB$ và $FK = \\frac{1}{2}AB = \\frac{%s}{2} = %s\\text{ cm}$.\\\\'
            'Vì $AB // CD$ nên qua $K$ hai đường thẳng $EK$ và $FK$ trùng nhau, tức là ba điểm $E, K, F$ thẳng hàng.\\\\'
            'Vậy $EF = EK + FK = %s + %s = %s\\text{ cm}$.'
            % (cd, fmt_num(cd / 2), ab, fmt_num(ab / 2), fmt_num(cd / 2), fmt_num(ab / 2), kq_str)
        )

    dapan = '\n\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
