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


def bt_dang1_p2_b1_c6_ds9(self):
    def fmt_num(val):
        if isinstance(val, Rational) and val.q != 1:
            return latex(val)
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    tu = random.choice([2, 3, 4, 5])
    mau = random.choice([3, 5, 7])
    while math.gcd(tu, mau) != 1:
        mau = random.choice([3, 5, 7])

    a_val = Rational(tu, mau)
    x0 = -mau
    y0 = a_val * (x0 ** 2)
    y_target = a_val * ((2 * mau) ** 2)
    x_target = 2 * mau

    bang_tabular = (
        '\\begin{center}\n'
        '\\begin{tabular}{|c|c|c|c|c|c|}\n'
        '\\hline\n'
        '$x$ & $-%s$ & $-%s$ & $0$ & $%s$ & $%s$ \\\\ \n'
        '\\hline\n'
        '$y$ & $?$ & $%s$ & $0$ & $%s$ & $?$ \\\\ \n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}' % (fmt_num(x_target), fmt_num(mau), fmt_num(mau), fmt_num(x_target), fmt_num(y0), fmt_num(y0))
    )

    noidungcauhoi = (
        'Cho hàm số $y = %sx^2$ có bảng giá trị một số điểm như sau:%s' % (latex(a_val), bang_tabular)
    )

    nb_da_1_d = '\\True Hàm số xác định với mọi giá trị thực của $x$'
    nb_da_1_s = 'Hàm số chỉ xác định với các giá trị $x \\ge 0$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Hàm số $y = %sx^2$ có hệ số $a = %s \\ne 0$ nên xác định với mọi giá trị $x \\in \\mathbb{R}$.' % (latex(a_val), latex(a_val))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Đồ thị của hàm số là một đường parabol nằm phía trên trục hoành (trừ gốc toạ độ $O$)'
    th_da_1_s = 'Đồ thị của hàm số là một đường parabol nằm phía dưới trục hoành (trừ gốc toạ độ $O$)'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Vì hệ số $a = %s > 0$ nên đồ thị của hàm số là một đường parabol có đỉnh là gốc toạ độ $O(0;0)$, nhận trục tung $Oy$ làm trục đối xứng và nằm phía trên trục hoành.' % (latex(a_val))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Với $x = %s$, giá trị tương ứng của hàm số là $y = %s$' % (fmt_num(x0), fmt_num(y0))
    vd_da_1_s = 'Với $x = %s$, giá trị tương ứng của hàm số là $y = -%s$' % (fmt_num(x0), fmt_num(y0))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Thay $x = %s$ vào công thức hàm số ta được: $y = %s \\cdot (%s)^2 = %s \\cdot %s = %s$.' % (fmt_num(x0), latex(a_val), fmt_num(x0), latex(a_val), fmt_num(x0**2), fmt_num(y0))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Có hai điểm thuộc đồ thị có tung độ bằng $%s$, và hai điểm này đối xứng nhau qua trục tung' % (fmt_num(y_target))
    vdc_da_1_s = 'Chỉ có duy nhất một điểm thuộc đồ thị có tung độ bằng $%s$' % (fmt_num(y_target))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Thay $y = %s$ vào công thức hàm số ta có: $%sx^2 = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$. \\\\ Vậy có hai điểm thuộc đồ thị là $(%s; %s)$ và $(-%s; %s)$, hai điểm này đối xứng nhau qua trục tung $Oy$.' % (fmt_num(y_target), latex(a_val), fmt_num(y_target), fmt_num(x_target**2), fmt_num(x_target), fmt_num(x_target), fmt_num(x_target), fmt_num(y_target), fmt_num(x_target), fmt_num(y_target))
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
