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


def bt_dang10_p2_b1_c6_ds9(self):
    def fmt_num(val):
        if isinstance(val, Rational) and val.q != 1:
            return latex(val)
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    a_val = -Rational(1, 2)
    x_pair = random.choice([2, 4])
    y_pair = a_val * (x_pair ** 2)
    x_big = 2 * x_pair
    y_big = a_val * (x_big ** 2)
    ab_sq = (x_big - x_pair) ** 2 + (y_big - y_pair) ** 2
    ab_len = sqrt(ab_sq)

    noidungcauhoi = (
        'Xét hai điểm phân biệt $A(x_1; y_1)$ và $B(x_2; y_2)$ cùng thuộc đồ thị hàm số $y = -\\frac{1}{2}x^2$.'
    )

    nb_da_1_d = '\\True Nếu $x_1 = -x_2$ thì $y_1 = y_2$'
    nb_da_1_s = 'Nếu $x_1 = -x_2$ thì $y_1 = -y_2$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Khi $x_1 = -x_2$, ta có $y_1 = -\\frac{1}{2}x_1^2 = -\\frac{1}{2}(-x_2)^2 = -\\frac{1}{2}x_2^2 = y_2$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Nếu $y_1 = y_2 = %s$ và $x_1 < x_2$ thì $x_1 = -%s$ và $x_2 = %s$' % (fmt_num(y_pair), fmt_num(x_pair), fmt_num(x_pair))
    th_da_1_s = 'Nếu $y_1 = y_2 = %s$ và $x_1 < x_2$ thì $x_1 = -%s$ và $x_2 = %s$' % (fmt_num(y_pair), fmt_num(x_pair**2), fmt_num(x_pair**2))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay $y = %s$ vào hàm số ta được: $-\\frac{1}{2}x^2 = %s \\Leftrightarrow x^2 = %s \\Leftrightarrow x = %s$ hoặc $x = -%s$. \\\\ Vì $x_1 < x_2$ nên $x_1 = -%s$ và $x_2 = %s$.' % (fmt_num(y_pair), fmt_num(y_pair), fmt_num(x_pair**2), fmt_num(x_pair), fmt_num(x_pair), fmt_num(x_pair), fmt_num(x_pair))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đường thẳng đi qua hai điểm $A(-%s; %s)$ và $B(%s; %s)$ vuông góc với trục tung $Oy$' % (fmt_num(x_pair), fmt_num(y_pair), fmt_num(x_pair), fmt_num(y_pair))
    vd_da_1_s = 'Đường thẳng đi qua hai điểm $A(-%s; %s)$ và $B(%s; %s)$ song song với trục tung $Oy$' % (fmt_num(x_pair), fmt_num(y_pair), fmt_num(x_pair), fmt_num(y_pair))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Hai điểm $A(-%s; %s)$ và $B(%s; %s)$ đối xứng nhau qua trục tung $Oy$ nên đoạn thẳng $AB$ vuông góc với trục tung $Oy$ tại trung điểm của $AB$.' % (fmt_num(x_pair), fmt_num(y_pair), fmt_num(x_pair), fmt_num(y_pair))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Với $x_1 = %s$ và $x_2 = %s$, độ dài đoạn thẳng $AB$ bằng $%s$' % (fmt_num(x_pair), fmt_num(x_big), latex(ab_len))
    vdc_da_1_s = 'Với $x_1 = %s$ và $x_2 = %s$, độ dài đoạn thẳng $AB$ bằng $%s$' % (fmt_num(x_pair), fmt_num(x_big), fmt_num(x_big - x_pair))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Với $x_1 = %s \\Rightarrow y_1 = %s$, ta có $A(%s; %s)$. Với $x_2 = %s \\Rightarrow y_2 = %s$, ta có $B(%s; %s)$. \\\\ Độ dài đoạn thẳng $AB = \\sqrt{(%s - %s)^2 + (%s - (%s))^2} = \\sqrt{%s} = %s$.' % (fmt_num(x_pair), fmt_num(y_pair), fmt_num(x_pair), fmt_num(y_pair), fmt_num(x_big), fmt_num(y_big), fmt_num(x_big), fmt_num(y_big), fmt_num(x_big), fmt_num(x_pair), fmt_num(y_big), fmt_num(y_pair), fmt_num(ab_sq), latex(ab_len))
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
