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
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang3_p2_b3_c4_hh8(self):
    # Dạng 3: Phân tích đồng thời hai đường phân giác của hai tam giác kề nhau qua đường trung tuyến
    p = random.choice([2, 3, 4])
    q = random.choice([3, 4, 5])
    while p >= q or math.gcd(p, q) != 1:
        p = random.choice([2, 3, 4])
        q = random.choice([3, 4, 5])
    k = random.choice([2, 3])
    am = p * k
    mb = q * k
    bc = 2 * mb
    de_val = round(bc * p / (p + q), 2)
    s_de = fmt_num(de_val)

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (1.8,3.4);\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (4.6,0);\n'
        '\\coordinate (M) at ($(B)!0.5!(C)$);\n'
        '\\coordinate (D) at ($(A)!0.43!(B)$);\n'
        '\\coordinate (E) at ($(A)!0.43!(C)$);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(M) (M)--(D)--(E)--cycle;\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (M) circle (1pt) node[below] {$M$};\n'
        '\\fill (D) circle (1pt) node[left] {$D$};\n'
        '\\fill (E) circle (1pt) node[right] {$E$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho tam giác $ABC$ có đường trung tuyến $AM$ ($M \\in BC$). Tia phân giác của góc $AMB$ cắt cạnh $AB$ tại $D$, tia phân giác của góc $AMC$ cắt cạnh $AC$ tại $E$. Biết $AM = %s\\text{ cm}$ và $BC = %s\\text{ cm}$.\n%s'
        % (am, bc, hinh_ve)
    )

    nb_da_1_d = '\\True $MB = MC = %s\\text{ cm}$' % mb
    nb_da_1_s = '$MB = MC = %s\\text{ cm}$' % bc
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Vì $AM$ là đường trung tuyến của tam giác $ABC$ nên $M$ là trung điểm của $BC$, suy ra $MB = MC = \\frac{BC}{2} = \\frac{%s}{2} = %s\\text{ cm}$.' % (bc, mb)
    loigiai_nb_s = 'Sai. Vì $M$ là trung điểm của $BC$ nên $MB = MC = \\frac{BC}{2} = %s\\text{ cm}$.' % mb

    th_da_1_d = '\\True $\\frac{AD}{DB} = \\frac{EA}{EC} = \\frac{%s}{%s}$' % (p, q)
    th_da_1_s = '$\\frac{AD}{DB} = \\frac{EA}{EC} = \\frac{%s}{%s}$' % (q, p)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Áp dụng tính chất đường phân giác cho tam giác $AMB$ và tam giác $AMC$, kết hợp với $MB = MC$, ta có: $\\frac{AD}{DB} = \\frac{MA}{MB} = \\frac{%s}{%s} = \\frac{%s}{%s}$ và $\\frac{EA}{EC} = \\frac{MA}{MC} = \\frac{%s}{%s}$.' % (am, mb, p, q, p, q)
    loigiai_th_s = 'Sai. Ta có $\\frac{AD}{DB} = \\frac{EA}{EC} = \\frac{MA}{MB} = \\frac{%s}{%s} = \\frac{%s}{%s}$.' % (am, mb, p, q)

    vd_da_1_d = '\\True $DE // BC$'
    vd_da_1_s = '$DE$ cắt $BC$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Xét tam giác $ABC$ có $\\frac{AD}{DB} = \\frac{EA}{EC}$ nên theo định lí Thalès đảo, ta suy ra $DE // BC$.'
    loigiai_vd_s = 'Sai. Vì $\\frac{AD}{DB} = \\frac{EA}{EC}$ nên theo định lí Thalès đảo, ta có $DE // BC$.'

    vdc_da_1_d = '\\True Độ dài đoạn thẳng $DE = %s\\text{ cm}$' % s_de
    vdc_da_1_s = 'Độ dài đoạn thẳng $DE = %s\\text{ cm}$' % mb
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Vì $DE // BC$ nên theo hệ quả của định lí Thalès, ta có $\\frac{DE}{BC} = \\frac{AD}{AB} = \\frac{%s}{%s}$. Suy ra $DE = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}$.' % (p, p + q, p, p + q, bc, s_de)
    loigiai_vdc_s = 'Sai. Theo hệ quả của định lí Thalès, $\\frac{DE}{BC} = \\frac{AD}{AB} = \\frac{%s}{%s}$, suy ra $DE = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}$.' % (p, p + q, p, p + q, bc, s_de)

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

    loigiai_nb_1 = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    loigiai_th_1 = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    loigiai_vd_1 = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    loigiai_vdc_1 = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    list_nb_1 = [nb_da_1]
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    list_vd_1 = [vd_da_1]
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    list_vdc_1 = [vdc_da_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
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
