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


def bt_dang20_p2_b3_c1_ds8(self):
    # Khai báo biến
    x, y = symbols('x y')

    a = random.choice([2, 3, 4])
    b = random.choice([2, 3])
    c1 = random.choice([12, 15, 18])
    c2 = random.choice([22, 25, 28])
    tong_hang = c1 + c2

    M = a*x**2*y - b*x*y**2 + c1
    N = b*x*y**2 - a*x**2*y + c2

    pts = [(1, -1), (-2, 1), (2, 2), (3, -2)]
    m_vals = [int(M.subs({x: px, y: py})) for px, py in pts]
    n_vals = [int(N.subs({x: px, y: py})) for px, py in pts]
    n_vals[2] += 10

    noidungcauhoi = ('''Trong một phần mềm kiểm thử tự động, máy tính xuất ra đồng thời hai tham số kiểm soát $M = %s$ và $N = %s$ ứng với các cặp đầu vào $(x; y)$ khác nhau như bảng sau:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Lần chạy & Lần 1 & Lần 2 & Lần 3 & Lần 4 \\\\
\\hline
$(x; y)$ & $(1; -1)$ & $(-2; 1)$ & $(2; 2)$ & $(3; -2)$ \\\\
\\hline
$M$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
$N$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}''' % (latex(M), latex(N),
                        m_vals[0], m_vals[1], m_vals[2], m_vals[3],
                        n_vals[0], n_vals[1], n_vals[2], n_vals[3]))

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Tổng hai đa thức $M + N$ luôn bằng $%s$ với mọi giá trị của $x$ và $y$.' % (tong_hang)
    nb_da_1_s = 'Tổng hai đa thức $M + N$ luôn bằng $%s$ với mọi giá trị của $x$ và $y$.' % (c2 - c1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ('''Ta có: $M + N = (%s) + (%s) = %s$ với mọi $x, y$.''' % (latex(M), latex(N), tong_hang))
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Ở Lần 1, Lần 2 và Lần 4, tổng $M + N$ đều thỏa mãn bằng $%s$.' % (tong_hang)
    th_da_1_s = 'Ở Lần 2 và Lần 3, tổng $M + N$ đều thỏa mãn bằng $%s$.' % (tong_hang)
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ('''Kiểm tra từng cột: Lần 1 ($%s + %s = %s$), Lần 2 ($%s + %s = %s$), Lần 4 ($%s + %s = %s$).''' % (m_vals[0], n_vals[0], tong_hang, m_vals[1], n_vals[1], tong_hang, m_vals[3], n_vals[3], tong_hang))
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Dựa vào tính chất bất biến của $M + N$, ta phát hiện ngay kết quả ở Lần 3 bị lỗi.'
    vd_da_1_s = 'Dựa vào tính chất bất biến của $M + N$, ta phát hiện ngay kết quả ở Lần 4 bị lỗi.'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ('''Ở Lần 3, ta có $M + N = %s + %s = %s \\neq %s$, nên Lần 3 bị lỗi.''' % (m_vals[2], n_vals[2], m_vals[2] + n_vals[2], tong_hang))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Hiệu $M - N$ phụ thuộc vào cả hai biến $x$ và $y$.'
    vdc_da_1_s = 'Hiệu $M - N$ cũng là một hằng số không phụ thuộc vào $x$ và $y$.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ('''Ta có $M - N = %s$, vẫn chứa biến $x$ và $y$ nên không phải hằng số.''' % (latex(simplify(M - N))))
    list_vdc_2 = [loigiai_vdc_1]

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
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
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
