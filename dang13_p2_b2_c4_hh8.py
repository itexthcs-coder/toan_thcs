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
    if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
        return str(int(val))
    return str(val).replace('.', ',')

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang13_p2_b2_c4_hh8(self):
    ab = random.choice([6, 8, 10])
    ac = ab + random.choice([4, 6, 8])
    bc_min = ac - ab
    bc_max = ac + ab
    de_min = bc_min // 2
    de_max = bc_max // 2
    cv_max = (ab + ac) // 2 + de_max

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (D) at ($(A)!0.5!(B)$);
\\coordinate (E) at ($(A)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (D)--(E);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Gọi $D, E$ lần lượt là trung điểm của $AB$ và $AC$ (như hình vẽ).%s''' % (fmt_num(ab), fmt_num(ac), hinhve))

    nb_da_1_d = '\\True $DE = \\dfrac{1}{2}BC$'
    nb_da_1_s = '$DE = 2BC$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Vì $D, E$ lần lượt là trung điểm của $AB$ và $AC$ nên $DE$ là đường trung bình của tam giác $ABC$, suy ra $DE = \\dfrac{1}{2}BC$.']

    th_da_1_d = '\\True Độ dài cạnh $BC$ thỏa mãn $%s\\text{ cm} < BC < %s\\text{ cm}$' % (fmt_num(bc_min), fmt_num(bc_max))
    th_da_1_s = 'Độ dài cạnh $BC$ thỏa mãn $%s\\text{ cm} < BC < %s\\text{ cm}$' % (fmt_num(ab), fmt_num(ac))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Áp dụng bất đẳng thức tam giác trong tam giác $ABC$, ta có $AC - AB < BC < AC + AB$, hay $%s - %s < BC < %s + %s \\Leftrightarrow %s\\text{ cm} < BC < %s\\text{ cm}$.' % (fmt_num(ac), fmt_num(ab), fmt_num(ac), fmt_num(ab), fmt_num(bc_min), fmt_num(bc_max))]

    vd_da_1_d = '\\True Độ dài đoạn thẳng $DE$ thỏa mãn $%s\\text{ cm} < DE < %s\\text{ cm}$' % (fmt_num(de_min), fmt_num(de_max))
    vd_da_1_s = 'Độ dài đoạn thẳng $DE$ có thể bằng $%s\\text{ cm}$' % fmt_num(de_max)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Vì $DE = \\dfrac{1}{2}BC$ và $%s < BC < %s$ nên $%s\\text{ cm} < DE < %s\\text{ cm}$. Do đó $DE$ không thể bằng $%s\\text{ cm}$.' % (fmt_num(bc_min), fmt_num(bc_max), fmt_num(de_min), fmt_num(de_max), fmt_num(de_max))]

    vdc_da_1_d = '\\True Chu vi của tam giác $ADE$ luôn nhỏ hơn $%s\\text{ cm}$' % fmt_num(cv_max)
    vdc_da_1_s = 'Chu vi của tam giác $ADE$ luôn lớn hơn $%s\\text{ cm}$' % fmt_num(cv_max)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Ta có $AD = \\dfrac{1}{2}AB = %s\\text{ cm}$, $AE = \\dfrac{1}{2}AC = %s\\text{ cm}$. Chu vi tam giác $ADE$ là $AD + AE + DE = %s + %s + DE = %s + DE < %s + %s = %s\\text{ cm}$.' % (fmt_num(ab // 2), fmt_num(ac // 2), fmt_num(ab // 2), fmt_num(ac // 2), fmt_num((ab + ac) // 2), fmt_num((ab + ac) // 2), fmt_num(de_max), fmt_num(cv_max))]

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
