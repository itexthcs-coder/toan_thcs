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

def bt_dang20_p2_b2_c4_hh8(self):
    ac = random.choice([20, 30, 40, 50])
    bd = random.choice([16, 20, 24, 30])
    mn = ac // 2
    mq = bd // 2
    s_hoa = mn * mq
    s_dat = ac * bd // 2

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3.2);
\\coordinate (B) at (0,1.2);
\\coordinate (C) at (2.2,0);
\\coordinate (D) at (4.5,1.8);
\\coordinate (M) at ($(A)!0.5!(B)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (P) at ($(C)!0.5!(D)$);
\\coordinate (Q) at ($(D)!0.5!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[below left] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (Q) circle (1pt) node[above right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Một công viên có một khu đất hình tứ giác $ABCD$ với hai lối đi chéo $AC = %s\\text{ m}$ và $BD = %s\\text{ m}$ vuông góc với nhau tại giao điểm. Ban quản lý trồng hoa ở phần đất hình tứ giác $MNPQ$ có các đỉnh là trung điểm của bốn cạnh $AB, BC, CD, DA$, phần đất còn lại trồng cỏ (như hình vẽ).%s''' % (fmt_num(ac), fmt_num(bd), hinhve))

    nb_da_1_d = '\\True Khu vực trồng hoa $MNPQ$ có dạng hình chữ nhật'
    nb_da_1_s = 'Khu vực trồng hoa $MNPQ$ có dạng hình thoi'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Ta có $MN // PQ // AC$, $MQ // NP // BD$ và $AC \\perp BD$ nên $MN \\perp MQ$. Tứ giác $MNPQ$ là hình bình hành có một góc vuông nên có dạng hình chữ nhật.']

    th_da_1_d = '\\True Hai kích thước của khu đất trồng hoa lần lượt là $%s\\text{ m}$ và $%s\\text{ m}$' % (fmt_num(mn), fmt_num(mq))
    th_da_1_s = 'Hai kích thước của khu đất trồng hoa lần lượt là $%s\\text{ m}$ và $%s\\text{ m}$' % (fmt_num(ac), fmt_num(bd))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Áp dụng tính chất đường trung bình của tam giác, hai kích thước của hình chữ nhật $MNPQ$ là $MN = \\dfrac{1}{2}AC = %s\\text{ m}$ và $MQ = \\dfrac{1}{2}BD = %s\\text{ m}$.' % (fmt_num(mn), fmt_num(mq))]

    vd_da_1_d = '\\True Diện tích khu đất trồng hoa $MNPQ$ bằng $%s\\text{ m}^2$' % fmt_num(s_hoa)
    vd_da_1_s = 'Diện tích khu đất trồng hoa $MNPQ$ bằng $%s\\text{ m}^2$' % fmt_num(s_dat)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Diện tích khu đất trồng hoa hình chữ nhật $MNPQ$ là $S_{MNPQ} = MN \\cdot MQ = %s \\cdot %s = %s\\text{ m}^2$.' % (fmt_num(mn), fmt_num(mq), fmt_num(s_hoa))]

    vdc_da_1_d = '\\True Diện tích phần đất trồng hoa bằng đúng một nửa diện tích toàn bộ khu đất $ABCD$'
    vdc_da_1_s = 'Diện tích phần đất trồng hoa bằng $\\dfrac{1}{4}$ diện tích toàn bộ khu đất $ABCD$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Khu đất $ABCD$ có hai đường chéo vuông góc nên $S_{ABCD} = \\dfrac{1}{2}AC \\cdot BD = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s\\text{ m}^2$. Suy ra $S_{MNPQ} = \\dfrac{1}{2}S_{ABCD}$.' % (fmt_num(ac), fmt_num(bd), fmt_num(s_dat))]

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
