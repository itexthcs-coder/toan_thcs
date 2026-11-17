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


def bt_dang18_p2_b1_c6_ds9(self):
    def fmt_num(val):
        if isinstance(val, Rational) and val.q != 1:
            return latex(val)
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    r_chao = random.choice([60, 80])
    d_chao = 2 * r_chao
    h_chao = 20 if r_chao == 60 else 32
    mau_a = (r_chao ** 2) // h_chao
    f_dist = mau_a // 4
    x_mid = r_chao // 2
    h_mid = h_chao // 4

    tikz_code = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\draw[->, line width=1pt] (-3.5,0) -- (3.5,0) node[below] {$x$};\n'
        '\\draw[->, line width=1pt] (0,-0.5) -- (0,3.2) node[right] {$y$};\n'
        '\\draw[line width=1pt, smooth, samples=100, domain=-2.8:2.8] plot (\\x, {0.25*(\\x)^2});\n'
        '\\draw[line width=1pt, dashed] (-2.8,1.96) -- (2.8,1.96);\n'
        '\\draw[line width=1pt, dashed] (-2.8,1.96) -- (-2.8,0) (2.8,1.96) -- (2.8,0);\n'
        '\\fill (0,0) circle (1pt) node[below left] {$O$};\n'
        '\\fill (0,1) circle (1pt) node[right] {$F$};\n'
        '\\fill (2.8,1.96) circle (1pt) node[above right] {$B$};\n'
        '\\fill (-2.8,1.96) circle (1pt) node[above left] {$A$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một chiếc ăng-ten chảo thu sóng vệ tinh có mặt cắt đi qua trục đối xứng là một đường parabol $y = ax^2$ với đỉnh là tâm chảo $O(0;0)$ hướng lên trên. Biết đường kính miệng chảo là $%s\\text{ cm}$ và độ sâu của lòng chảo (tính từ tâm miệng chảo xuống đỉnh $O$) là $%s\\text{ cm}$.%s' % (fmt_num(d_chao), fmt_num(h_chao), tikz_code)
    )

    nb_da_1_d = '\\True Trong hệ trục toạ độ $Oxy$ với $Oy$ là trục đối xứng, hai mép ngoài miệng chảo có toạ độ là $(%s; %s)$ và $(-%s; %s)$' % (fmt_num(r_chao), fmt_num(h_chao), fmt_num(r_chao), fmt_num(h_chao))
    nb_da_1_s = 'Trong hệ trục toạ độ $Oxy$ với $Oy$ là trục đối xứng, hai mép ngoài miệng chảo có toạ độ là $(%s; %s)$ và $(-%s; %s)$' % (fmt_num(d_chao), fmt_num(h_chao), fmt_num(d_chao), fmt_num(h_chao))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Bán kính miệng chảo là $\\frac{%s}{2} = %s\\text{ cm}$ và độ sâu lòng chảo là $%s\\text{ cm}$ nên hai điểm mép miệng chảo có toạ độ là $(%s; %s)$ và $(-%s; %s)$.' % (fmt_num(d_chao), fmt_num(r_chao), fmt_num(h_chao), fmt_num(r_chao), fmt_num(h_chao), fmt_num(r_chao), fmt_num(h_chao))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Hệ số $a$ của parabol mặt cắt chảo là $a = \\frac{1}{%s}$' % (fmt_num(mau_a))
    th_da_1_s = 'Hệ số $a$ của parabol mặt cắt chảo là $a = \\frac{1}{%s}$' % (fmt_num(mau_a // 2))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay toạ độ điểm $(%s; %s)$ vào phương trình $y = ax^2$ ta được: \\\\ $a \\cdot %s^2 = %s \\Leftrightarrow %sa = %s \\Leftrightarrow a = \\frac{%s}{%s} = \\frac{1}{%s}$.' % (fmt_num(r_chao), fmt_num(h_chao), fmt_num(r_chao), fmt_num(h_chao), fmt_num(r_chao**2), fmt_num(h_chao), fmt_num(h_chao), fmt_num(r_chao**2), fmt_num(mau_a))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đầu thu tín hiệu được đặt trên trục $Oy$ cách đỉnh $O$ một khoảng bằng $\\frac{1}{4a}$. Khoảng cách từ đỉnh $O$ đến đầu thu tín hiệu là $%s\\text{ cm}$' % (fmt_num(f_dist))
    vd_da_1_s = 'Đầu thu tín hiệu được đặt trên trục $Oy$ cách đỉnh $O$ một khoảng bằng $\\frac{1}{4a}$. Khoảng cách từ đỉnh $O$ đến đầu thu tín hiệu là $%s\\text{ cm}$' % (fmt_num(f_dist * 2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Khoảng cách từ đỉnh $O$ đến đầu thu tín hiệu là $OF = \\frac{1}{4a} = \\frac{1}{4 \\cdot \\frac{1}{%s}} = \\frac{%s}{4} = %s\\text{ (cm)}$.' % (fmt_num(mau_a), fmt_num(mau_a), fmt_num(f_dist))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tại điểm trên lòng chảo cách trục đối xứng $%s\\text{ cm}$, độ cao của điểm đó so với đỉnh $O$ là $%s\\text{ cm}$' % (fmt_num(x_mid), fmt_num(h_mid))
    vdc_da_1_s = 'Tại điểm trên lòng chảo cách trục đối xứng $%s\\text{ cm}$, độ cao của điểm đó so với đỉnh $O$ là $%s\\text{ cm}$' % (fmt_num(x_mid), fmt_num(h_chao // 2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Điểm trên lòng chảo cách trục đối xứng $%s\\text{ cm}$ có hoành độ $|x| = %s$. \\\\ Thay vào phương trình parabol ta được độ cao so với đỉnh $O$ là $y = \\frac{1}{%s} \\cdot %s^2 = \\frac{%s}{%s} = %s\\text{ (cm)}$.' % (fmt_num(x_mid), fmt_num(x_mid), fmt_num(mau_a), fmt_num(x_mid), fmt_num(x_mid**2), fmt_num(mau_a), fmt_num(h_mid))
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
