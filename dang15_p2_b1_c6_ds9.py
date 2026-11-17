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


def bt_dang15_p2_b1_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    k_val = random.choice([2, 3])
    k_sq = k_val ** 2
    d2_len = 2 * k_val

    tikz_code = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};\n'
        '\\draw[->, line width=1pt] (0,-0.5) -- (0,4.2) node[right] {$y$};\n'
        '\\draw[line width=1pt, smooth, samples=100, domain=-1.95:1.95] plot (\\x, {(\\x)^2});\n'
        '\\draw[line width=1pt, smooth, samples=100, domain=-3.2:3.2] plot (\\x, {0.25*(\\x)^2});\n'
        '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
        '\\node[above] at (1.5,3.5) {$(P_1)$};\n'
        '\\node[right] at (3,2.3) {$(P_2)$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho hai parabol $(P_1): y = x^2$ và $(P_2): y = \\frac{1}{%s}x^2$ được vẽ trên cùng một mặt phẳng toạ độ $Oxy$ như hình minh hoạ:%s' % (fmt_num(k_sq), tikz_code)
    )

    nb_da_1_d = '\\True Cả hai đồ thị đều nằm phía trên trục hoành và nhận $Oy$ làm trục đối xứng'
    nb_da_1_s = 'Đồ thị $(P_1)$ nằm trên trục hoành còn $(P_2)$ nằm dưới trục hoành'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Cả hai hàm số đều có hệ số $a > 0$ ($1 > 0$ và $\\frac{1}{%s} > 0$) nên hai đồ thị đều nằm phía trên trục hoành và nhận $Oy$ làm trục đối xứng.' % (fmt_num(k_sq))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Với cùng một giá trị $x \\ne 0$, điểm thuộc $(P_1)$ luôn nằm cao hơn điểm thuộc $(P_2)$'
    th_da_1_s = 'Với cùng một giá trị $x \\ne 0$, điểm thuộc $(P_2)$ luôn nằm cao hơn điểm thuộc $(P_1)$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Với mọi $x \\ne 0$, ta có $x^2 > 0$ và $1 > \\frac{1}{%s}$ nên $x^2 > \\frac{1}{%s}x^2$. Do đó điểm thuộc $(P_1)$ luôn có tung độ lớn hơn (nằm cao hơn) điểm thuộc $(P_2)$.' % (fmt_num(k_sq), fmt_num(k_sq))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đường thẳng $y = 1$ cắt $(P_1)$ tại hai điểm cách nhau $2$ đơn vị và cắt $(P_2)$ tại hai điểm cách nhau $%s$ đơn vị' % (fmt_num(d2_len))
    vd_da_1_s = 'Đường thẳng $y = 1$ cắt $(P_1)$ tại hai điểm cách nhau $1$ đơn vị và cắt $(P_2)$ tại hai điểm cách nhau $%s$ đơn vị' % (fmt_num(k_val))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Đường thẳng $y = 1$ cắt $(P_1)$ tại $(-1; 1)$ và $(1; 1)$, khoảng cách giữa chúng là $1 - (-1) = 2$ đơn vị. \\\\ Đường thẳng $y = 1$ cắt $(P_2)$ tại $(-%s; 1)$ và $(%s; 1)$, khoảng cách giữa chúng là $%s - (-%s) = %s$ đơn vị.' % (fmt_num(k_val), fmt_num(k_val), fmt_num(k_val), fmt_num(k_val), fmt_num(d2_len))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Hai parabol $(P_1)$ và $(P_2)$ chỉ có một điểm chung duy nhất là gốc toạ độ $O(0;0)$'
    vdc_da_1_s = 'Hai parabol $(P_1)$ và $(P_2)$ có hai giao điểm phân biệt'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Xét phương trình hoành độ giao điểm: $x^2 = \\frac{1}{%s}x^2 \\Leftrightarrow \\left(1 - \\frac{1}{%s}\\right)x^2 = 0 \\Leftrightarrow x = 0$. \\\\ Vậy hai parabol chỉ có một giao điểm duy nhất là gốc toạ độ $O(0;0)$.' % (fmt_num(k_sq), fmt_num(k_sq))
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
