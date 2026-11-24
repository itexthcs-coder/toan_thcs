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

def bt_dang9_p2_b2_c4_hh8(self):
    ab = random.choice([6, 8, 10, 12])
    cd = ab + random.choice([6, 8, 10])
    mi = cd // 2
    in_len = ab // 2
    mn = mi + in_len

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.0,2.8);
\\coordinate (B) at (3.2,2.8);
\\coordinate (C) at (4.8,0);
\\coordinate (D) at (0,0);
\\coordinate (M) at ($(A)!0.5!(D)$);
\\coordinate (N) at ($(B)!0.5!(C)$);
\\coordinate (I) at ($(A)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N) (A)--(C);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (I) circle (1pt) node[above right] {$I$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho hình thang $ABCD$ ($AB // CD$) có $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$. Gọi $M, N$ lần lượt là trung điểm của $AD$ và $BC$. Đường thẳng $MN$ cắt đường chéo $AC$ tại $I$ (như hình vẽ).%s''' % (fmt_num(ab), fmt_num(cd), hinhve))

    nb_da_1_d = '\\True $MN // AB // CD$'
    nb_da_1_s = '$MN$ cắt đường thẳng $CD$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Đoạn thẳng $MN$ nối trung điểm hai cạnh bên của hình thang $ABCD$ nên $MN // AB // CD$ (tính chất đường trung bình của hình thang, chứng minh qua hai tam giác $ADC$ và $ABC$).']

    th_da_1_d = '\\True $I$ là trung điểm của $AC$ và $MI = %s\\text{ cm}$' % fmt_num(mi)
    th_da_1_s = '$I$ là trung điểm của $AC$ và $MI = %s\\text{ cm}$' % fmt_num(in_len)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Xét tam giác $ADC$, có $M$ là trung điểm của $AD$ và $MI // CD$ nên $I$ là trung điểm của $AC$. Khi đó $MI$ là đường trung bình của tam giác $ADC$, suy ra $MI = \\dfrac{1}{2}CD = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.' % (fmt_num(cd), fmt_num(mi))]

    vd_da_1_d = '\\True Độ dài đoạn thẳng $IN$ bằng $%s\\text{ cm}$' % fmt_num(in_len)
    vd_da_1_s = 'Độ dài đoạn thẳng $IN$ bằng $%s\\text{ cm}$' % fmt_num(ab)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Xét tam giác $ABC$, vì $I$ là trung điểm của $AC$ và $N$ là trung điểm của $BC$ nên $IN$ là đường trung bình của tam giác $ABC$. Suy ra $IN = \\dfrac{1}{2}AB = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.' % (fmt_num(ab), fmt_num(in_len))]

    vdc_da_1_d = '\\True Độ dài đoạn thẳng $MN$ bằng $%s\\text{ cm}$' % fmt_num(mn)
    vdc_da_1_s = 'Độ dài đoạn thẳng $MN$ bằng $%s\\text{ cm}$' % fmt_num(mi - in_len)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Vì điểm $I$ nằm giữa $M$ và $N$ nên $MN = MI + IN = %s + %s = %s\\text{ cm}$.' % (fmt_num(mi), fmt_num(in_len), fmt_num(mn))]

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
