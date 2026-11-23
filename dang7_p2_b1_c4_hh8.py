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


def bt_dang7_p2_b1_c4_hh8(self):
    me = 3
    nf = 5
    a = 1
    b = 4
    # (x+1)/3 = (x+4)/5 => 5x + 5 = 3x + 12 => 2x = 7 => x = 3.5
    c_add = random.choice([1, 3, 5])
    # (x + c_add)/3 = (x + c_add + 3)/5 => 5x + 5c = 3x + 3c + 9 => 2x = 9 - 2c
    x_val = Rational(9 - 2 * c_add, 2)
    x_str = str(float(x_val)).replace('.', ',')
    d_add = c_add + 3
    de_val = x_val + c_add + me
    de_str = str(float(de_val)).replace('.', ',')
    dm_str = str(float(x_val + c_add)).replace('.', ',')

    noidungcauhoi = ("""Cho $\\Delta DEF$, trên cạnh $DE$ lấy điểm $M$, trên cạnh $DF$ lấy điểm $N$ sao cho $DM = x + %s$, $ME = %s$, $DN = x + %s$, $NF = %s$ (với $x > 0$ và các kích thước tính theo $\\text{cm}$) như hình vẽ bên dưới. Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (1.5,3);
\\coordinate (E) at (0,0);
\\coordinate (F) at (4.5,0);
\\coordinate (M) at ($(D)!0.55!(E)$);
\\coordinate (N) at ($(D)!0.55!(F)$);
\\draw[line width=1pt] (D)--(E)--(F)--cycle (M)--(N);
\\fill (D) circle (1pt) node[above] {$D$};
\\fill (E) circle (1pt) node[below left] {$E$};
\\fill (F) circle (1pt) node[below right] {$F$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                     % (c_add, me, d_add, nf))

    nb_da_1_d = '\\True Để $MN // EF$ thì ta phải có tỉ lệ thức $\\dfrac{x + %s}{%s} = \\dfrac{x + %s}{%s}$' % (c_add, me, d_add, nf)
    nb_da_1_s = 'Để $MN // EF$ thì ta phải có tỉ lệ thức $\\dfrac{x + %s}{%s} = \\dfrac{%s}{x + %s}$' % (c_add, me, nf, d_add)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Theo định lí Thalès đảo, để $MN // EF$ thì $\\dfrac{DM}{ME} = \\dfrac{DN}{NF}$ hay $\\dfrac{x + %s}{%s} = \\dfrac{x + %s}{%s}$."""
                    % (c_add, me, d_add, nf))

    th_da_1_d = '\\True Với $x = %s$ thì $MN // EF$' % (x_str)
    th_da_1_s = 'Với $x = %s$ thì $MN // EF$' % (str(float(x_val + 1)).replace('.', ','))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Giải phương trình $\\dfrac{x + %s}{%s} = \\dfrac{x + %s}{%s} \\Leftrightarrow %s(x + %s) = %s(x + %s) \\Leftrightarrow 2x = %s \\Leftrightarrow x = %s$ (thỏa mãn $x > 0$)."""
                    % (c_add, me, d_add, nf, nf, c_add, me, d_add, 9 - 2 * c_add, x_str))

    vd_da_1_d = '\\True Khi $MN // EF$, độ dài đoạn thẳng $DE$ bằng $%s\\text{ cm}$' % (de_str)
    vd_da_1_s = 'Khi $MN // EF$, độ dài đoạn thẳng $DE$ bằng $%s\\text{ cm}$' % (dm_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Khi $MN // EF$, ta có $x = %s$, suy ra $DM = %s + %s = %s\\text{ (cm)}$ và $DE = DM + ME = %s + %s = %s\\text{ (cm)}$."""
                    % (x_str, x_str, c_add, dm_str, dm_str, me, de_str))

    vdc_da_1_d = '\\True Khi $x \\neq %s$, đường thẳng $MN$ không song song với cạnh $EF$' % (x_str)
    vdc_da_1_s = 'Với mọi $x > 0$, đường thẳng $MN$ luôn song song với cạnh $EF$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Vì $MN // EF$ chỉ xảy ra duy nhất khi $x = %s$ nên với $x \\neq %s$, hai đường thẳng $MN$ và $EF$ không song song với nhau."""
                     % (x_str, x_str))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
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
