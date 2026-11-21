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


def bt_dang18_p2_b4_c2_ds8(self):
    y = symbols('y')
    a = random.randint(2, 4)
    b = random.randint(2, 4)
    ab = a * b
    x_val = 10 * a
    y_val = 10 * b + a
    
    tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) rectangle (3.5,2.2);
    \\draw[line width=1pt, dashed] (3.5,0) -- (4.3,0) -- (4.3,1.6) -- (0,1.6);
    \\draw[line width=1pt, <->] (0,2.45) -- (3.5,2.45) node[midway, above] {$x$};
    \\draw[line width=1pt, <->] (-0.25,0) -- (-0.25,2.2) node[midway, left] {$y$};
\\end{tikzpicture}
\\end{center}'''
    
    noidungcauhoi = ('''Một công viên hình chữ nhật có chiều dài là $x\\text{ (m)}$ và chiều rộng là $y\\text{ (m)}$ ($x > y > %s$). Ban quản lý dự án mở rộng chiều dài công viên thêm $%s\\text{ m}$ và thu hẹp chiều rộng đi $%s\\text{ m}$ để làm vỉa hè.''' % (b + 1, a, b) + tikz_hinh)
    
    nb_da_1_d = '\\True Diện tích công viên ban đầu là $xy\\text{ (m}^2\\text{)}$ và diện tích sau khi điều chỉnh là $(x + %s)(y - %s)\\text{ (m}^2\\text{)}$' % (a, b)
    nb_da_1_s = 'Diện tích công viên ban đầu là $xy\\text{ (m}^2\\text{)}$ và diện tích sau khi điều chỉnh là $(x - %s)(y + %s)\\text{ (m}^2\\text{)}$' % (a, b)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['''Chiều dài mới là $x + %s\\text{ (m)}$ và chiều rộng mới là $y - %s\\text{ (m)}$ nên diện tích mới là $(x + %s)(y - %s)\\text{ (m}^2\\text{)}$.'''
                 % (a, b, a, b)]
    
    delta_s = a*y - b*x - ab
    th_da_1_d = '\\True Phần diện tích chênh lệch (diện tích mới trừ diện tích cũ) được biểu diễn bởi đa thức $\\Delta S = %s\\text{ (m}^2\\text{)}$' % (latex(delta_s))
    th_da_1_s = 'Phần diện tích chênh lệch (diện tích mới trừ diện tích cũ) được biểu diễn bởi đa thức $\\Delta S = %sy - %sx + %s\\text{ (m}^2\\text{)}$' % (a, b, ab)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['''Ta có $\\Delta S = (x + %s)(y - %s) - xy = xy - %sx + %sy - %s - xy = %s\\text{ (m}^2\\text{)}$.'''
                 % (a, b, b, a, ab, latex(delta_s))]
    
    vd_da_1_d = '\\True Nếu chiều dài ban đầu $x = %s\\text{ m}$ và chiều rộng ban đầu $y = %s\\text{ m}$ thì diện tích công viên không đổi' % (x_val, y_val)
    vd_da_1_s = 'Nếu chiều dài ban đầu $x = %s\\text{ m}$ và chiều rộng ban đầu $y = %s\\text{ m}$ thì diện tích tăng thêm $%s\\text{ m}^2$' % (x_val, y_val, ab)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['''Thay $x = %s, y = %s$ vào $\\Delta S$: $\\Delta S = %s \\cdot %s - %s \\cdot %s - %s = 0\\text{ (m}^2\\text{)}$, nên diện tích không đổi.'''
                 % (x_val, y_val, a, y_val, b, x_val, ab)]
    
    vdc_da_1_d = '\\True Khi $%sy - %sx = %s$, diện tích công viên trước và sau khi điều chỉnh luôn bằng nhau' % (a, b, ab)
    vdc_da_1_s = 'Khi $%sy - %sx = %s$, diện tích công viên sau khi điều chỉnh luôn lớn hơn ban đầu' % (a, b, ab)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['''Khi $%sy - %sx = %s$ thì $\\Delta S = (%sy - %sx) - %s = 0$, nên diện tích trước và sau bằng nhau.'''
                  % (a, b, ab, a, b, ab)]

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
