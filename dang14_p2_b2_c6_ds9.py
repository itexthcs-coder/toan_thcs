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


def bt_dang14_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        h_val = random.choice([6, 9, 12])
        coef_v = h_val // 3
        x_test = random.choice([4, 5])
        v_test = coef_v * (x_test**2)
        x_target = random.choice([6, 7, 8])
        v_target = coef_v * (x_target**2)

        tikz_fig = ('\\begin{center}\n' +
                    '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
                    '\\coordinate (A) at (0,0);\n' +
                    '\\coordinate (B) at (4.5,0);\n' +
                    '\\coordinate (C) at (3.2,-1.3);\n' +
                    '\\coordinate (D) at (-1.3,-1.3);\n' +
                    '\\coordinate (O) at (1.6,-0.65);\n' +
                    '\\coordinate (S) at (1.6,3.2);\n' +
                    '\\draw[line width=1pt] (S)--(D)--(C)--(B)--cycle (S)--(C);\n' +
                    '\\draw[line width=1pt, dashed] (S)--(A)--(D) (A)--(B) (A)--(C) (B)--(D) (S)--(O);\n' +
                    '\\fill (A) circle (1pt) node[above left] {$A$};\n' +
                    '\\fill (B) circle (1pt) node[right] {$B$};\n' +
                    '\\fill (C) circle (1pt) node[below right] {$C$};\n' +
                    '\\fill (D) circle (1pt) node[below left] {$D$};\n' +
                    '\\fill (O) circle (1pt) node[below] {$O$};\n' +
                    '\\fill (S) circle (1pt) node[above] {$S$};\n' +
                    '\\end{tikzpicture}\n' +
                    '\\end{center}')

        noidungcauhoi = ('Cho một hình chóp tứ giác đều $S.ABCD$ có đáy là hình vuông cạnh $x \\text{ (cm)}$ ($x > 0$) và chiều cao $SO = %s \\text{ cm}$ (như hình vẽ).\n%s\nXét tính đúng sai của các khẳng định sau:' % (h_val, tikz_fig))

        nb_da_1_d = '\\True Thể tích $V$ của hình chóp được tính theo công thức $V = %sx^2 \\text{ (cm}^3\\text{)}$' % (coef_v)
        nb_da_1_s = 'Thể tích $V$ của hình chóp được tính theo công thức $V = %sx^2 \\text{ (cm}^3\\text{)}$' % (h_val)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Diện tích đáy hình vuông là $S = x^2 \\text{ (cm}^2\\text{)}$. \\\\ Thể tích hình chóp tứ giác đều là $V = \\frac{1}{3} S \\cdot h = \\frac{1}{3} \\cdot x^2 \\cdot %s = %sx^2 \\text{ (cm}^3\\text{)}$.' % (h_val, coef_v))

        th_da_1_d = '\\True Khi cạnh đáy $x = %s \\text{ cm}$, thể tích của hình chóp bằng $%s \\text{ cm}^3$' % (x_test, v_test)
        th_da_1_s = 'Khi cạnh đáy $x = %s \\text{ cm}$, thể tích của hình chóp bằng $%s \\text{ cm}^3$' % (x_test, coef_v * x_test)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Thay $x = %s$ vào công thức thể tích ta được: $V = %s \\cdot %s^2 = %s \\text{ (cm}^3\\text{)}$.' % (x_test, coef_v, x_test, v_test))

        vd_da_1_d = '\\True Để thể tích hình chóp đạt $%s \\text{ cm}^3$ thì cạnh đáy phải bằng $%s \\text{ cm}$' % (v_target, x_target)
        vd_da_1_s = 'Để thể tích hình chóp đạt $%s \\text{ cm}^3$ thì cạnh đáy phải bằng $%s \\text{ cm}$' % (v_target, x_target + 2)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Ta có phương trình: $%sx^2 = %s \\Leftrightarrow x^2 = %s$. \\\\ Vì $x > 0$ nên $x = %s \\text{ (cm)}$.' % (coef_v, v_target, x_target**2, x_target))

        vdc_da_1_d = '\\True Nếu tăng độ dài cạnh đáy lên $3$ lần thì thể tích của hình chóp tăng lên $9$ lần'
        vdc_da_1_s = 'Nếu tăng độ dài cạnh đáy lên $3$ lần thì thể tích của hình chóp tăng lên $6$ lần'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Khi độ dài cạnh đáy tăng lên $3$ lần thành $3x$, thể tích mới của hình chóp là: \\\\ $V\\prime = %s(3x)^2 = %s \\cdot 9x^2 = 9V$. Vậy thể tích hình chóp tăng lên $9$ lần.' % (coef_v, coef_v))

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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
