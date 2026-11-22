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


def bt_dang17_p4_b2_c3_hh8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ma = random.randint(4, 7)
        mb = random.randint(5, 8)
        mc = random.randint(6, 9)
        chu_vi = ma + mb + mc

        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (2,3.46);\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4,0);\n'
            '\\coordinate (M) at (1.8,1.3);\n'
            '\\coordinate (P) at (1.05,1.82);\n'
            '\\coordinate (Q) at (2.55,0);\n'
            '\\coordinate (R) at (2.55,2.51);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(A) (P)--(Q)--(R)--(P);\n'
            '\\draw[line width=1pt, dashed] (M)--(P) (M)--(Q) (M)--(R);\n'
            '\\fill (A) circle (1pt) node[above] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (M) circle (1pt) node[below left] {$M$};\n'
            '\\fill (P) circle (1pt) node[left] {$P$};\n'
            '\\fill (Q) circle (1pt) node[below] {$Q$};\n'
            '\\fill (R) circle (1pt) node[right] {$R$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho điểm $M$ nằm trong tam giác đều $ABC$. Qua $M$ kẻ các đường thẳng song song với $BC$, $CA$, $AB$ lần lượt cắt $AB$, $BC$, $CA$ tại $P$, $Q$, $R$ (như hình vẽ).\\\\\n'
            'a) Chứng minh rằng tứ giác $APMR$ là hình thang cân.\\\\\n'
            'b) Biết $MA = %s\\text{ cm}$, $MB = %s\\text{ cm}$, $MC = %s\\text{ cm}$, tính chu vi tam giác $PQR$. %s'
            % (ma, mb, mc, hinh_ve)
        )

        loigiai = (
            '\\begin{enumEX}[a)]{1} \\n'
            '\\item Vì $PM // BC$ nên $PM // AR$, do đó tứ giác $APMR$ là hình thang.\\\\ '
            'Tam giác $ABC$ đều nên $\\widehat{PAR} = 60^\\circ$; vì $MR // AB$ nên $\\widehat{MRA} = \\widehat{B} = 60^\\circ$ (đồng vị).\\\\ '
            'Hình thang $APMR$ có hai góc kề đáy $AR$ bằng nhau ($\\widehat{PAR} = \\widehat{MRA} = 60^\\circ$) nên là hình thang cân. \\n'
            '\\item Tương tự, $BQMP$ và $CRMQ$ cũng là các hình thang cân nên:\\\\ '
            '$PR = MA = %s\\text{ cm}$, $PQ = MB = %s\\text{ cm}$, $QR = MC = %s\\text{ cm}$.\\\\ '
            'Chu vi tam giác $PQR$ là: $PQ + QR + RP = %s + %s + %s = %s\\text{ cm}$. \\n'
            '\\end{enumEX} \\n'
            % (ma, mb, mc, mb, mc, ma, chu_vi)
        )

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
