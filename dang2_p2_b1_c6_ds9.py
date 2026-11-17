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


def bt_dang2_p2_b1_c6_ds9(self):
    def fmt_num(val):
        if isinstance(val, Rational) and val.q != 1:
            return latex(val)
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    tu = random.choice([3, 5, 7])
    mau = random.choice([2, 4])
    a_val = -Rational(tu, mau)
    x_M = -2
    y_M = a_val * (x_M ** 2)
    m_val = 4
    y_N = a_val * (m_val ** 2)

    tikz_code = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};\n'
        '\\draw[->, line width=1pt] (0,-4.5) -- (0,1) node[right] {$y$};\n'
        '\\draw[line width=1pt, smooth, samples=100, domain=-2.2:2.2] plot (\\x, {-0.8*(\\x)^2});\n'
        '\\fill (0,0) circle (1pt) node[above right] {$O$};\n'
        '\\fill (-1.5,-1.8) circle (1pt) node[left] {$M$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Xét hàm số $y = %sx^2$ có đồ thị minh hoạ như hình bên dưới:%s' % (latex(a_val), tikz_code)
    )

    nb_da_1_d = '\\True Điểm cao nhất của đồ thị hàm số là gốc toạ độ $O(0;0)$'
    nb_da_1_s = 'Điểm thấp nhất của đồ thị hàm số là gốc toạ độ $O(0;0)$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Vì hệ số $a = %s < 0$ nên đồ thị nằm phía dưới trục hoành và nhận gốc toạ độ $O(0;0)$ làm điểm cao nhất.' % (latex(a_val))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Điểm $M(%s; %s)$ thuộc đồ thị của hàm số đã cho' % (fmt_num(x_M), fmt_num(y_M))
    th_da_1_s = 'Điểm $M(%s; %s)$ thuộc đồ thị của hàm số đã cho' % (fmt_num(x_M), fmt_num(-y_M))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay $x = %s$ vào hàm số ta được: $y = %s \\cdot (%s)^2 = %s \\cdot %s = %s$. \\\\ Vậy điểm $M(%s; %s)$ thuộc đồ thị của hàm số đã cho.' % (fmt_num(x_M), latex(a_val), fmt_num(x_M), latex(a_val), fmt_num(x_M**2), fmt_num(y_M), fmt_num(x_M), fmt_num(y_M))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu điểm $N(m; %s)$ thuộc đồ thị hàm số thì $m = %s$ hoặc $m = -%s$' % (fmt_num(y_N), fmt_num(m_val), fmt_num(m_val))
    vd_da_1_s = 'Nếu điểm $N(m; %s)$ thuộc đồ thị hàm số thì chỉ có duy nhất $m = %s$' % (fmt_num(y_N), fmt_num(m_val))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Vì điểm $N(m; %s)$ thuộc đồ thị hàm số nên thay $x = m$ và $y = %s$ vào công thức hàm số ta được: \\\\ $%sm^2 = %s \\Leftrightarrow m^2 = %s \\Leftrightarrow m = %s$ hoặc $m = -%s$.' % (fmt_num(y_N), fmt_num(y_N), latex(a_val), fmt_num(y_N), fmt_num(m_val**2), fmt_num(m_val), fmt_num(m_val))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khi $x$ nhận các giá trị đối nhau thì giá trị tương ứng của $y$ bằng nhau'
    vdc_da_1_s = 'Khi $x$ nhận các giá trị đối nhau thì giá trị tương ứng của $y$ cũng đối nhau'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Với mọi $x \\in \\mathbb{R}$, ta có $(-x)^2 = x^2$ nên $%s(-x)^2 = %sx^2$. \\\\ Do đó khi $x$ nhận các giá trị đối nhau thì giá trị tương ứng của $y$ luôn bằng nhau (hai điểm đối xứng nhau qua trục tung $Oy$).' % (latex(a_val), latex(a_val))
    )
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
