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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang1_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p1, p2, p3 = random.sample([2, 3, 4, 5, 6], 3)
        A_val = p1 * p2 * p3
        A_inside = (p1**2) * (p2**2) * (p3**2)

        k = random.choice([2, 3, 5])
        m, n = random.sample([2, 3, 4], 2)
        b1 = k * (m**2)
        b2 = k * (n**2)
        B_val = k * m * n
        B_inside = b1 * b2

        S = math.isqrt(A_val + B_val) + 1
        c_val = S**2 - (A_val + B_val)

        noidungcauhoi = ('''Cho hai biểu thức $A = \\sqrt{%d \\cdot %d \\cdot %d}$ và $B = \\sqrt{%d} \\cdot \\sqrt{%d}$. Xét tính đúng sai của các khẳng định sau:''' % (p1**2, p2**2, p3**2, b1, b2))

        nb_da_1_d = '\\True Giá trị của biểu thức $A$ bằng $%d$' % (A_val)
        nb_da_1_s = 'Giá trị của biểu thức $A$ bằng $%d$' % (A_val + p1)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $A = \\sqrt{%d \\cdot %d \\cdot %d} = \\sqrt{%d^2} \\cdot \\sqrt{%d^2} \\cdot \\sqrt{%d^2} = %d \\cdot %d \\cdot %d = %d$.''' % (p1**2, p2**2, p3**2, p1, p2, p3, p1, p2, p3, A_val))

        th_da_1_d = '\\True Biểu thức $B$ có thể viết lại thành $\\sqrt{%d \\cdot %d} = %d$' % (b1, b2, B_val)
        th_da_1_s = 'Biểu thức $B$ có thể viết lại thành $\\sqrt{%d + %d} = %d$' % (b1, b2, B_val + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Áp dụng quy tắc nhân các căn bậc hai, ta có $B = \\sqrt{%d} \\cdot \\sqrt{%d} = \\sqrt{%d \\cdot %d} = \\sqrt{%d} = %d$.''' % (b1, b2, b1, b2, B_inside, B_val))

        if A_val > B_val:
            vd_da_1_d = '\\True Giá trị của biểu thức $A$ lớn hơn giá trị của biểu thức $B$ là $%d$ đơn vị' % (A_val - B_val)
            vd_da_1_s = 'Giá trị của biểu thức $A$ nhỏ hơn giá trị của biểu thức $B$ là $%d$ đơn vị' % (A_val - B_val)
            loigiai_vd_1 = ('''Vì $A = %d$ và $B = %d$ nên $A > B$ và $A - B = %d - %d = %d$.''' % (A_val, B_val, A_val, B_val, A_val - B_val))
        else:
            vd_da_1_d = '\\True Giá trị của biểu thức $B$ lớn hơn hoặc bằng giá trị của biểu thức $A$'
            vd_da_1_s = 'Giá trị của biểu thức $A$ luôn lớn hơn giá trị của biểu thức $B$'
            loigiai_vd_1 = ('''Ta có $A = %d$ và $B = %d$, suy ra $B \\ge A$.''' % (A_val, B_val))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Giá trị của biểu thức $\\sqrt{A + B + %d}$ là một số tự nhiên' % (c_val)
        vdc_da_1_s = 'Giá trị của biểu thức $\\sqrt{A + B + %d}$ là một số vô tỉ' % (c_val)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Ta có $\\sqrt{A + B + %d} = \\sqrt{%d + %d + %d} = \\sqrt{%d} = %d$, đây là một số tự nhiên.''' % (c_val, A_val, B_val, c_val, S**2, S))

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
