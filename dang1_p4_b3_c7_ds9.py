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


def bt_dang1_p4_b3_c7_ds9(self):
    def fmt_vn(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        # Tổng 25 con gà: 4 nhóm [1,7; 2,0), [2,0; 2,3), [2,3; 2,6), [2,6; 2,9]
        m1, m2, m3, m4 = random.choice([
            (3, 8, 9, 5),
            (4, 7, 9, 5),
            (3, 7, 10, 5)
        ])
        g1 = [Decimal(str(random.randint(17, 19))) / Decimal('10') for _ in range(m1)]
        g2 = [Decimal(str(random.randint(20, 22))) / Decimal('10') for _ in range(m2)]
        g3 = [Decimal(str(random.randint(23, 25))) / Decimal('10') for _ in range(m3)]
        g4 = [Decimal(str(random.randint(26, 29))) / Decimal('10') for _ in range(m4)]
        g1[0] = Decimal('1.7')
        g2[0] = Decimal('2.0')
        g3[0] = Decimal('2.3')
        g4[0] = Decimal('2.9')

        raw = g1 + g2 + g3 + g4
        random.shuffle(raw)
        raw_str = '; \\quad '.join(fmt_vn(x) for x in raw)

        f1 = fmt_vn(Decimal(str(m1 * 100)) / Decimal('25'))
        f2 = fmt_vn(Decimal(str(m2 * 100)) / Decimal('25'))
        f3 = fmt_vn(Decimal(str(m3 * 100)) / Decimal('25'))
        f4 = fmt_vn(Decimal(str(m4 * 100)) / Decimal('25'))

        noidungcauhoi = ('''Cân nặng (đơn vị: $\\text{kg}$) của $25$ con gà mái trưởng thành tại một trang trại chăn nuôi được ghi lại như sau:
$$%s.$$
a) Lập bảng tần số ghép nhóm cho mẫu số liệu trên với các nhóm $[1,7; 2,0)$, $[2,0; 2,3)$, $[2,3; 2,6)$, $[2,6; 2,9]$.\\
b) Lập bảng tần số tương đối ghép nhóm tương ứng và cho biết nhóm cân nặng nào chiếm tỉ lệ cao nhất.''' % (raw_str))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Đếm số giá trị thuộc từng nhóm trong dãy số liệu, ta được bảng tần số ghép nhóm sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Cân nặng ($\\text{kg}$) & $[1,7; 2,0)$ & $[2,0; 2,3)$ & $[2,3; 2,6)$ & $[2,6; 2,9]$ \\\\
\\hline
Số con gà & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Cỡ mẫu là $n = %s + %s + %s + %s = 25$. Tính tần số tương đối của từng nhóm theo công thức $f_i = \\dfrac{m_i}{25} \\cdot 100\\%%$, ta có bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Cân nặng ($\\text{kg}$) & $[1,7; 2,0)$ & $[2,0; 2,3)$ & $[2,3; 2,6)$ & $[2,6; 2,9]$ \\\\
\\hline
Tần số tương đối & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
Nhóm cân nặng $[2,3; 2,6)$ chiếm tỉ lệ cao nhất ($%s\\%%$).
\\end{enumEX}''' % (m1, m2, m3, m4, m1, m2, m3, m4, f1, f2, f3, f4, f3))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
