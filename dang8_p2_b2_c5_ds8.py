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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang8_p2_b2_c5_ds8(self):
    # Dạng 8 (Vận dụng - Thuần túy toán học): Chuyển đổi biểu đồ cột kép sang hai biểu đồ cột đơn và so sánh tổng
    d = random.choice([0, 4, 8])
    u1, u2, u3, u4 = 24 + d, 36 + d, 30 + d, 42 + d
    v1, v2, v3, v4 = 30 + d, 28 + d, 34 + d, 40 + d
    tong_u = u1 + u2 + u3 + u4
    diff_n2 = u2 - v2
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt, ->] (0,0) -- (0,2.6) node[above] {Giá trị};
    \\draw[line width=1pt, ->] (0,0) -- (6.6,0) node[right] {$n$};
    \\draw[line width=1pt, fill=black!35] (0.5,0) rectangle (0.95,1.2) (2.0,0) rectangle (2.45,1.8) (3.5,0) rectangle (3.95,1.5) (5.0,0) rectangle (5.45,2.1);
    \\draw[line width=1pt, fill=white] (0.95,0) rectangle (1.4,1.5) (2.45,0) rectangle (2.9,1.4) (3.95,0) rectangle (4.4,1.7) (5.45,0) rectangle (5.9,2.0);
    \\node[above] at (0.72,1.2) {$%s$}; \\node[above] at (1.18,1.5) {$%s$};
    \\node[above] at (2.22,1.8) {$%s$}; \\node[above] at (2.68,1.4) {$%s$};
    \\node[above] at (3.72,1.5) {$%s$}; \\node[above] at (4.18,1.7) {$%s$};
    \\node[above] at (5.22,2.1) {$%s$}; \\node[above] at (5.68,2.0) {$%s$};
    \\node[below] at (0.95,0) {$n=1$}; \\node[below] at (2.45,0) {$n=2$};
    \\node[below] at (3.95,0) {$n=3$}; \\node[below] at (5.45,0) {$n=4$};
    \\draw[line width=1pt, fill=black!35] (6.3,1.8) rectangle (6.6,2.1); \\node[right] at (6.6,1.95) {$u_n$};
    \\draw[line width=1pt, fill=white] (6.3,1.3) rectangle (6.6,1.6); \\node[right] at (6.6,1.45) {$v_n$};
    \\end{tikzpicture}
    \\end{center}""" % (u1, v1, u2, v2, u3, v3, u4, v4))
    
    noidungcauhoi = ("""Cho biểu đồ cột kép so sánh hai dãy số liệu $(u_n)$ và $(v_n)$ tại $4$ vị trí $n \\in \\{1; 2; 3; 4\\}$:%sXét tính đúng sai của các khẳng định sau:""" % tikz_code)
    
    nb_da_1_d = '\\True Nếu tách riêng dãy $(u_n)$ để vẽ biểu đồ cột đơn thì cột cao nhất ứng với $n = 4$ có giá trị $%s$' % u4
    nb_da_1_s = 'Nếu tách riêng dãy $(u_n)$ để vẽ biểu đồ cột đơn thì cột cao nhất ứng với $n = 2$ có giá trị $%s$' % u2
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Trong dãy $(u_n)$ gồm các số hạng $%s; %s; %s; %s$, giá trị lớn nhất là $u_4 = %s$.""" % (u1, u2, u3, u4, u4))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_s = '\\True Tại mọi vị trí $n$, giá trị của $u_n$ đều nhỏ hơn giá trị của $v_n$'
    th_da_1_d = 'Tại các vị trí $n = 2$ và $n = 4$, giá trị của $u_n$ lớn hơn giá trị của $v_n$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Tại $n = 2$, ta có $u_2 = %s > v_2 = %s$; tại $n = 4$, ta có $u_4 = %s > v_4 = %s$ nên khẳng định $u_n < v_n$ với mọi $n$ là sai.""" % (u2, v2, u4, v4))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Hiệu số $|u_n - v_n|$ đạt giá trị lớn nhất tại vị trí $n = 2$ (bằng $%s$)' % diff_n2
    vd_da_1_s = 'Hiệu số $|u_n - v_n|$ đạt giá trị lớn nhất tại vị trí $n = 1$ (bằng $6$)'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Các độ chênh lệch $|u_n - v_n|$ lần lượt là: tại $n=1$ bằng $6$; tại $n=2$ bằng $|%s - %s| = %s$; tại $n=3$ bằng $4$; tại $n=4$ bằng $2$. Vậy lớn nhất tại $n = 2$.""" % (u2, v2, diff_n2))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_d = '\\True Tổng các số hạng của dãy $(u_n)$ bằng tổng các số hạng của dãy $(v_n)$ (cùng bằng $%s$)' % tong_u
    vdc_da_1_s = 'Tổng các số hạng của dãy $(u_n)$ lớn hơn tổng các số hạng của dãy $(v_n)$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Ta có $u_1 + u_2 + u_3 + u_4 = %s + %s + %s + %s = %s$ và $v_1 + v_2 + v_3 + v_4 = %s + %s + %s + %s = %s$."""
                     % (u1, u2, u3, u4, tong_u, v1, v2, v3, v4, tong_u))
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
