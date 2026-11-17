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


def bt_dang6_p2_b1_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    k_coef = random.choice([2, 3, 4, 5])
    h_val = 3 * k_coef
    r_test = random.choice([2, 3])
    v_exact = k_coef * (r_test ** 2)
    v_approx = Decimal(str(v_exact)) * Decimal('3.14')
    v_approx_str = str(v_approx.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

    r_find = random.choice([4, 5, 6])
    v_find = k_coef * (r_find ** 2)

    tikz_code = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (S) at (0,2.8);\n'
        '\\coordinate (A) at (-1.5,0);\n'
        '\\coordinate (B) at (1.5,0);\n'
        '\\draw[line width=1pt] (A) arc (180:360:1.5 and 0.45);\n'
        '\\draw[line width=1pt, dashed] (B) arc (0:180:1.5 and 0.45);\n'
        '\\draw[line width=1pt] (S) -- (A) (S) -- (B);\n'
        '\\draw[line width=1pt, dashed] (S) -- (O) -- (B);\n'
        '\\fill (O) circle (1pt) node[below] {$O$};\n'
        '\\fill (S) circle (1pt) node[above] {$S$};\n'
        '\\fill (B) circle (1pt) node[right] {$B$};\n'
        '\\node[below] at (0.75,0) {$r$};\n'
        '\\node[left] at (0,1.4) {$h$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho hình nón có bán kính đáy là $r$ (cm) ($r > 0$) và chiều cao cố định $h = %s\\text{ cm}$. Thể tích hình nón được tính bởi công thức $V = \\frac{1}{3}\\pi r^2 h$.%s' % (fmt_num(h_val), tikz_code)
    )

    nb_da_1_d = '\\True Công thức biểu thị thể tích $V$ theo bán kính $r$ là $V = %s\\pi r^2$' % (fmt_num(k_coef))
    nb_da_1_s = 'Công thức biểu thị thể tích $V$ theo bán kính $r$ là $V = %s\\pi r^2$' % (fmt_num(h_val))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Thay $h = %s$ vào công thức thể tích hình nón ta được: $V = \\frac{1}{3}\\pi r^2 \\cdot %s = %s\\pi r^2$.' % (fmt_num(h_val), fmt_num(h_val), fmt_num(k_coef))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Với $\\pi \\approx 3,14$ và $r = %s\\text{ cm}$, thể tích của hình nón xấp xỉ $%s\\text{ cm}^3$' % (fmt_num(r_test), v_approx_str)
    th_da_1_s = 'Với $\\pi \\approx 3,14$ và $r = %s\\text{ cm}$, thể tích của hình nón xấp xỉ $%s\\text{ cm}^3$' % (fmt_num(r_test), str((v_approx * 2).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Với $r = %s\\text{ cm}$ và $\\pi \\approx 3,14$, thể tích của hình nón là: \\\\ $V = %s \\cdot 3,14 \\cdot %s^2 = %s \\cdot 3,14 \\cdot %s = %s\\text{ (cm}^3\\text{)}$.' % (fmt_num(r_test), fmt_num(k_coef), fmt_num(r_test), fmt_num(k_coef), fmt_num(r_test**2), v_approx_str)
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu thể tích hình nón bằng $%s\\pi\\text{ cm}^3$ thì bán kính đáy $r = %s\\text{ cm}$' % (fmt_num(v_find), fmt_num(r_find))
    vd_da_1_s = 'Nếu thể tích hình nón bằng $%s\\pi\\text{ cm}^3$ thì bán kính đáy $r = %s\\text{ cm}$' % (fmt_num(v_find), fmt_num(r_find ** 2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Thay $V = %s\\pi$ vào công thức $V = %s\\pi r^2$ ta được: \\\\ $%s\\pi r^2 = %s\\pi \\Leftrightarrow r^2 = %s$. Vì $r > 0$ nên $r = %s\\text{ (cm)}$.' % (fmt_num(v_find), fmt_num(k_coef), fmt_num(k_coef), fmt_num(v_find), fmt_num(r_find**2), fmt_num(r_find))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Xét hàm số $V = %s\\pi r^2$ với $r \\in \\mathbb{R}$, đồ thị của hàm số là một parabol nhận trục tung làm trục đối xứng' % (fmt_num(k_coef))
    vdc_da_1_s = 'Xét hàm số $V = %s\\pi r^2$ với $r \\in \\mathbb{R}$, đồ thị của hàm số là một đường thẳng đi qua gốc toạ độ' % (fmt_num(k_coef))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Hàm số $V = %s\\pi r^2$ có dạng $y = ax^2$ với hệ số $a = %s\\pi > 0$ nên đồ thị trên $\\mathbb{R}$ là một đường parabol có đỉnh là gốc toạ độ và nhận trục tung làm trục đối xứng.' % (fmt_num(k_coef), fmt_num(k_coef))
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
