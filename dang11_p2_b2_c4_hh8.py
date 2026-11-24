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

def bt_dang11_p2_b2_c4_hh8(self):
    bc = random.choice([8, 10, 12, 14, 16, 18, 20])
    ed = bc // 2

    hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.6,0);
\\coordinate (D) at ($(A)!0.5!(C)$);
\\coordinate (E) at ($(A)!0.5!(B)$);
\\coordinate (G) at (intersection of B--D and C--E);
\\coordinate (M) at ($(G)!0.5!(B)$);
\\coordinate (N) at ($(G)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(D) (C)--(E) (E)--(D)--(N)--(M)--cycle;
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (E) circle (1pt) node[left] {$E$};
\\fill (G) circle (1pt) node[above] {$G$};
\\fill (M) circle (1pt) node[below right] {$M$};
\\fill (N) circle (1pt) node[below left] {$N$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho tam giác $ABC$ có hai đường trung tuyến $BD$ và $CE$ cắt nhau tại trọng tâm $G$. Gọi $M, N$ lần lượt là trung điểm của $BG$ và $CG$ (như hình vẽ).%s''' % (hinhve))

    nb_da_1_d = '\\True $ED$ là đường trung bình của tam giác $ABC$ nên $ED = \\dfrac{1}{2}BC$'
    nb_da_1_s = '$ED$ là đường trung bình của tam giác $GBC$ nên $ED = \\dfrac{1}{2}BC$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['Vì $BD$ và $CE$ là hai đường trung tuyến của tam giác $ABC$ nên $D, E$ lần lượt là trung điểm của $AC$ và $AB$. Do đó $ED$ là đường trung bình của tam giác $ABC$, suy ra $ED // BC$ và $ED = \\dfrac{1}{2}BC$.']

    th_da_1_d = '\\True $MN$ là đường trung bình của tam giác $GBC$ nên $MN // BC$ và $MN = \\dfrac{1}{2}BC$'
    th_da_1_s = '$MN$ là đường trung bình của tam giác $GBC$ nên $MN = \\dfrac{1}{3}BC$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['Xét tam giác $GBC$ có $M, N$ lần lượt là trung điểm của $BG$ và $CG$ nên $MN$ là đường trung bình của tam giác $GBC$. Suy ra $MN // BC$ và $MN = \\dfrac{1}{2}BC$.']

    vd_da_1_d = '\\True Tứ giác $MNDE$ là hình bình hành'
    vd_da_1_s = 'Tứ giác $MNDE$ là hình thang cân'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['Vì $MN // BC$ và $ED // BC$ nên $MN // ED$. Mặt khác $MN = ED = \\dfrac{1}{2}BC$. Tứ giác $MNDE$ có hai cạnh đối $MN$ và $ED$ vừa song song vừa bằng nhau nên là hình bình hành.']

    vdc_da_1_d = '\\True Nếu $BC = %s\\text{ cm}$ thì $MN + ED = %s\\text{ cm}$' % (fmt_num(bc), fmt_num(bc))
    vdc_da_1_s = 'Nếu $BC = %s\\text{ cm}$ thì $MN + ED = %s\\text{ cm}$' % (fmt_num(bc), fmt_num(ed))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['Khi $BC = %s\\text{ cm}$, ta có $MN = ED = \\dfrac{1}{2} \\cdot %s = %s\\text{ cm}$. Vậy $MN + ED = %s + %s = %s\\text{ cm}$.' % (fmt_num(bc), fmt_num(bc), fmt_num(ed), fmt_num(ed), fmt_num(ed), fmt_num(bc))]

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
