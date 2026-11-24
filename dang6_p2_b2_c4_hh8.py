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

def bt_dang6_p2_b2_c4_hh8(self):
    ac = random.choice([8, 10, 12, 14, 16, 18, 20])
    ef = ac // 2
    cv_efgh = ef * 4

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,3.2);
\\coordinate (B) at (0,1.0);
\\coordinate (C) at (2.5,0);
\\coordinate (D) at (4.4,2.0);
\\coordinate (E) at ($(A)!0.5!(B)$);
\\coordinate (F) at ($(B)!0.5!(C)$);
\\coordinate (G) at ($(C)!0.5!(D)$);
\\coordinate (H) at ($(D)!0.5!(A)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (E)--(F)--(G)--(H)--cycle;
\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (F) circle (1pt) node[below left] {$F$};
\\fill (G) circle (1pt) node[below right] {$G$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho tứ giác $ABCD$ có hai đường chéo $AC = BD = %s\\text{ cm}$. Gọi $E, F, G, H$ lần lượt là trung điểm của $AB, BC, CD, DA$ (như hình vẽ).%s''' % (fmt_num(ac), hinhve))

    nb_da_1_d = '\\True $EF = GH = %s\\text{ cm}$' % fmt_num(ef)
    nb_da_1_s = '$EF = GH = %s\\text{ cm}$' % fmt_num(ac)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Vì $EF$ và $GH$ lần lượt là đường trung bình của tam giác $ABC$ và tam giác $ADC$ nên $EF = GH = \\dfrac{1}{2}AC = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.' % (fmt_num(ac), fmt_num(ef))]

    th_da_1_d = '\\True $EH = FG = %s\\text{ cm}$' % fmt_num(ef)
    th_da_1_s = '$EH = FG = %s\\text{ cm}$' % fmt_num(ac * 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Vì $EH$ và $FG$ lần lượt là đường trung bình của tam giác $ABD$ và tam giác $CBD$ nên $EH = FG = \\dfrac{1}{2}BD = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$.' % (fmt_num(ac), fmt_num(ef))]

    vd_da_1_d = '\\True Tứ giác $EFGH$ là hình thoi'
    vd_da_1_s = 'Tứ giác $EFGH$ luôn là hình vuông'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Tứ giác $EFGH$ có bốn cạnh bằng nhau ($EF = FG = GH = HE = %s\\text{ cm}$) nên $EFGH$ là hình thoi (chưa đủ điều kiện vuông góc để kết luận là hình vuông).' % fmt_num(ef)]

    vdc_da_1_d = '\\True Chu vi của tứ giác $EFGH$ bằng $%s\\text{ cm}$' % fmt_num(cv_efgh)
    vdc_da_1_s = 'Chu vi của tứ giác $EFGH$ bằng $%s\\text{ cm}$' % fmt_num(ac)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Chu vi của hình thoi $EFGH$ là $EF + FG + GH + HE = 4 \\cdot %s = %s\\text{ cm}$.' % (fmt_num(ef), fmt_num(cv_efgh))]

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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
