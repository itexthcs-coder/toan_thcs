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


def bt_dang6_p3_b3_c7_ds8(self):
    # Dạng 6: Tìm số giá trị nguyên của tham số để điểm thuộc góc phần tư cho trước
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        gpt = random.choice(['II', 'IV'])
        c1 = random.randint(2, 4)
        c2 = random.randint(2, 4)
        m_min = random.randint(-3, 2)
        so_nguyen = random.randint(1, 5)
        m_max = m_min + so_nguyen - 1

        # m_min <= a <= m_max <=> (m_min - 1) < a < (m_max + 1)
        b1 = c1 * (m_min - 1) + 1
        b2 = c2 * (m_max + 1) - 1

        if gpt == 'IV':
            # x > 0 and y < 0 => c1*a - b1 > 0 and c2*a - b2 < 0
            hd_str = '%sa - %s' % (c1, b1) if b1 >= 0 else '%sa + %s' % (c1, abs(b1))
            td_str = '%sa - %s' % (c2, b2) if b2 >= 0 else '%sa + %s' % (c2, abs(b2))
            dk_text = 'hoành độ dương và tung độ âm'
            bpt1 = '%s > 0 \\Leftrightarrow a > %s' % (hd_str, latex(Rational(b1, c1)))
            bpt2 = '%s < 0 \\Leftrightarrow a < %s' % (td_str, latex(Rational(b2, c2)))
        else:
            # gpt == 'II': x < 0 and y > 0 => -c1*a + b1 < 0 (a > b1/c1) and -c2*a + b2 > 0 (a < b2/c2)
            hd_str = '%s - %sa' % (b1, c1)
            td_str = '%s - %sa' % (b2, c2)
            dk_text = 'hoành độ âm và tung độ dương'
            bpt1 = '%s < 0 \\Leftrightarrow a > %s' % (hd_str, latex(Rational(b1, c1)))
            bpt2 = '%s > 0 \\Leftrightarrow a < %s' % (td_str, latex(Rational(b2, c2)))

        ds_nguyen = ', '.join(str(i) for i in range(m_min, m_max + 1))
        kq_str = str(so_nguyen)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.75, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (-2.5,0) -- (2.5,0) node[below] {$x$};
\\draw[line width=1pt, ->] (0,-2.2) -- (0,2.2) node[left] {$y$};
\\fill (0,0) circle (1pt) node[below left] {$O$};
\\node at (1.3,1.2) {I};
\\node at (-1.3,1.2) {II};
\\node at (-1.3,-1.2) {III};
\\node at (1.3,-1.2) {IV};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, điểm $A(%s;\\, %s)$ nằm trong góc phần tư thứ %s (tham khảo sơ đồ bốn góc phần tư dưới đây). Có bao nhiêu giá trị nguyên của $a$ thỏa mãn điều kiện trên?
%s'''
                         % (hd_str, td_str, gpt, tikz_code))

        loigiai = ('''Điểm $A$ nằm trong góc phần tư thứ %s nên điểm $A$ có %s. \\\\
Do đó ta có: \\\\
$\\begin{cases} %s \\\\ %s \\end{cases} \\Rightarrow %s < a < %s$. \\\\
Vì $a$ là số nguyên nên $a \\in \\{%s\\}$. \\\\
Vậy có tất cả $%s$ giá trị nguyên của $a$ thỏa mãn yêu cầu bài toán.'''
                   % (gpt, dk_text, bpt1, bpt2,
                      latex(Rational(b1, c1)), latex(Rational(b2, c2)),
                      ds_nguyen, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % str(kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
