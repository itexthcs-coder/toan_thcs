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
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        s = ('%.4f' % val).rstrip('0').rstrip('.')
        return s.replace('.', ',')
    if isinstance(val, Decimal):
        s = str(val).rstrip('0').rstrip('.') if '.' in str(val) else str(val)
        return s.replace('.', ',')
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        return '\dfrac{%s}{%s}' % (val.numerator, val.denominator)
    return str(val)

def bt_dang13_p2_b1_c9_hh8(self):
    # Dạng 13: Phân tích các mệnh đề lý thuyết về hai tam giác đồng dạng
    ang = random.choice([40, 50, 70, 80])
    ang_base = (180 - ang) // 2
    ang_top = 180 - 2 * ang

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (A) at (0,0);'
        '\\coordinate (B) at (0,1.8);'
        '\\coordinate (C) at (1.8,0);'
        '\\coordinate (D) at (3.5,0);'
        '\\coordinate (E) at (3.5,2.7);'
        '\\coordinate (F) at (6.2,0);'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E)--(F)--cycle;'
        '\\fill (A) circle (1pt) node[below left] {$A$};'
        '\\fill (B) circle (1pt) node[above] {$B$};'
        '\\fill (C) circle (1pt) node[right] {$C$};'
        '\\fill (D) circle (1pt) node[below left] {$D$};'
        '\\fill (E) circle (1pt) node[above] {$E$};'
        '\\fill (F) circle (1pt) node[right] {$F$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Xét các khẳng định về hai tam giác đồng dạng trên mặt phẳng:%s'
        % tikz
    )

    nb_da_1_d = '\\True Mọi tam giác đều đồng dạng với chính nó theo tỉ số đồng dạng $k = 1$'
    nb_da_1_s = 'Hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 0$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Theo nhận xét về hai tam giác đồng dạng: hai tam giác bằng nhau thì đồng dạng với nhau theo tỉ số đồng dạng $k = 1$. '
        'Đặc biệt, mọi tam giác đồng dạng với chính nó theo tỉ số $k = 1$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Hai tam giác vuông cân bất kì luôn đồng dạng với nhau'
    th_da_1_s = 'Hai tam giác vuông bất kì luôn đồng dạng với nhau'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Mọi tam giác vuông cân đều có các góc bằng $90^\\circ, 45^\\circ, 45^\\circ$ và ba cạnh tỉ lệ theo bộ $1 : 1 : \\sqrt{2}$ '
        'nên hai tam giác vuông cân bất kì luôn đồng dạng với nhau theo định nghĩa.'
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Hai tam giác cân có một góc bằng $%s^\\circ$ thì chưa chắc đồng dạng với nhau' % ang
    vd_da_1_s = 'Hai tam giác cân có một góc bằng $%s^\\circ$ thì luôn đồng dạng với nhau' % ang
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Nếu một tam giác cân có góc ở đỉnh bằng $%s^\\circ$ thì các góc của nó là $%s^\\circ, %s^\\circ, %s^\\circ$.\\ '
        'Nếu một tam giác cân khác có góc ở đáy bằng $%s^\\circ$ thì các góc của nó là $%s^\\circ, %s^\\circ, %s^\\circ$.\\ '
        'Hai tam giác này không có các góc tương ứng bằng nhau nên chưa chắc đồng dạng.'
        % (ang, ang, ang_base, ang_base, ang, ang_top, ang, ang)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu $\\Delta ABC \\backsim \\Delta MNP$ và $\\Delta ABC$ cân thì $\\Delta MNP$ cũng là tam giác cân'
    vdc_da_1_s = 'Nếu $\\Delta ABC \\backsim \\Delta MNP$ và $\\Delta ABC$ có chu vi gấp đôi thì các góc cũng gấp đôi'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Giả sử $\\Delta ABC$ cân tại $A$ nên $AB = AC$. Vì $\\Delta ABC \\backsim \\Delta MNP$ nên $\\dfrac{AB}{MN} = \\dfrac{AC}{MP}$.\\ '
        'Suy ra $MN = MP$, do đó $\\Delta MNP$ cân tại $M$.'
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
