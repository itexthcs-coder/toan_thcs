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


def bt_dang2_p2_b2_c7_ds8(self):
    # Dạng 2: Quy đồng và giải phương trình chứa mẫu số hằng số
    m1, m2, m3, mtc = random.choice([(3, 4, 6, 12), (2, 3, 6, 6), (3, 5, 15, 15), (4, 5, 10, 20)])
    k1 = mtc // m1
    k2 = mtc // m2
    k3 = mtc // m3
    a = random.randint(2, 4)
    b = random.randint(1, 3)
    c = random.randint(1, 3)
    d = random.randint(1, 4)
    # (ax - b)/m1 - (cx + d)/m2 = 1/m3
    # k1*(ax - b) - k2*(cx + d) = k3
    hs_x = k1 * a - k2 * c
    while hs_x <= 0:
        a += 1
        hs_x = k1 * a - k2 * c
    vp = k3 + k1 * b + k2 * d
    g = math.gcd(hs_x, vp)
    tu_nghiem = vp // g
    mau_nghiem = hs_x // g
    str_nghiem = str(tu_nghiem) if mau_nghiem == 1 else "\\dfrac{%s}{%s}" % (tu_nghiem, mau_nghiem)

    noidungcauhoi = "Cho phương trình $\\dfrac{%sx - %s}{%s} - \\dfrac{%sx + %s}{%s} = \\dfrac{1}{%s}$. Xét tính đúng, sai của các khẳng định sau:" % (
        a, b, m1, c, d, m2, m3
    )

    nb_da_1_d = '\\True Mẫu thức chung nhỏ nhất của các phân thức trong phương trình là $%s$.' % mtc
    nb_da_1_s = 'Mẫu thức chung nhỏ nhất của các phân thức trong phương trình là $%s$.' % (mtc * 2)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Vì $\\text{BCNN}(%s, %s, %s) = %s$ nên mẫu thức chung nhỏ nhất của phương trình là $%s$.' % (m1, m2, m3, mtc, mtc)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khi quy đồng và khử mẫu, ta thu được phương trình $%s(%sx - %s) - %s(%sx + %s) = %s$.' % (k1, a, b, k2, c, d, k3)
    th_da_1_s = 'Khi quy đồng và khử mẫu, ta thu được phương trình $%s(%sx - %s) - %s(%sx + %s) = 1$.' % (k1, a, b, k2, c, d)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Nhân cả hai vế của phương trình với $%s$, ta được: $%s(%sx - %s) - %s(%sx + %s) = %s$.' % (mtc, k1, a, b, k2, c, d, k3)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Sau khi thu gọn, phương trình có dạng $%sx = %s$.' % (hs_x, vp)
    vd_da_1_s = 'Sau khi thu gọn, phương trình có dạng $%sx = %s$.' % (hs_x, vp - 2 * k2 * d)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Ta có: $%sx - %s - %sx - %s = %s \\Leftrightarrow %sx = %s + %s + %s \\Leftrightarrow %sx = %s$.' % (
        k1 * a, k1 * b, k2 * c, k2 * d, k3, hs_x, k3, k1 * b, k2 * d, hs_x, vp
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nghiệm của phương trình là $x = %s$.' % str_nghiem
    vdc_da_1_s = 'Nghiệm của phương trình là $x = %s$.' % (tu_nghiem + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Từ $%sx = %s$, suy ra $x = \\dfrac{%s}{%s} = %s$.' % (hs_x, vp, vp, hs_x, str_nghiem)
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
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n'
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
