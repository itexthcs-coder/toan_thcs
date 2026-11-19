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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang2_p2_b4_c9_hh9(self):
    cap_da_giac = [
        (5, "ngũ giác đều $ABCDE$", 8, "bát giác đều $MNPQRSTU$"),
        (6, "lục giác đều $ABCDEF$", 9, "đa giác đều $9$ cạnh"),
        (6, "lục giác đều $ABCDEF$", 12, "đa giác đều $12$ cạnh"),
        (5, "ngũ giác đều $ABCDE$", 10, "đa giác đều $10$ cạnh")
    ]
    n1, ten1, n2, ten2 = random.choice(cap_da_giac)
    gt1 = 360 // n1
    gt2 = 360 // n2
    hieu_gt = gt1 - gt2
    g1 = 180 - gt1
    g2 = 180 - gt2
    tong_g = g1 + g2

    hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (90:1.4);
\\coordinate (B) at (162:1.4);
\\coordinate (C) at (234:1.4);
\\coordinate (D) at (306:1.4);
\\coordinate (E) at (18:1.4);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--cycle;
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[below left] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\begin{scope}[xshift=4.2cm]
\\foreach \\i in {1,...,8} {
    \\coordinate (P\\i) at (45*\\i:1.4);
}
\\draw[line width=1pt] (P1)--(P2)--(P3)--(P4)--(P5)--(P6)--(P7)--(P8)--cycle;
\\fill (P1) circle (1pt) node[above right] {$M$};
\\fill (P2) circle (1pt) node[above] {$N$};
\\end{scope}
\\end{tikzpicture}
\\end{center}'''

    noidungcauhoi = ('''Xét hai đa giác đều là %s ($%s$ cạnh) và %s ($%s$ cạnh). Xét tính đúng sai của các khẳng định sau: %s''' % (ten1, n1, ten2, n2, hinh_tikz))

    nb_da_1_d = '\\True Số đo góc ở tâm chắn mỗi cạnh của %s lớn hơn số đo góc ở tâm chắn mỗi cạnh của %s là $%s^\\circ$' % (ten1, ten2, hieu_gt)
    nb_da_1_s = 'Số đo góc ở tâm chắn mỗi cạnh của %s lớn hơn số đo góc ở tâm chắn mỗi cạnh của %s là $%s^\\circ$' % (ten1, ten2, hieu_gt + 10)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Góc ở tâm chắn mỗi cạnh của %s là $\\frac{360^\\circ}{%s} = %s^\\circ$, của %s là $\\frac{360^\\circ}{%s} = %s^\\circ$. Hiệu số đo hai góc ở tâm bằng $%s^\\circ - %s^\\circ = %s^\\circ$.''' % (ten1, n1, gt1, ten2, n2, gt2, gt1, gt2, hieu_gt))

    th_da_1_d = '\\True Mỗi góc trong của %s có số đo bằng $%s^\\circ$' % (ten1, g1)
    th_da_1_s = 'Mỗi góc trong của %s có số đo bằng $%s^\\circ$' % (ten1, g1 - 12)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Mỗi góc trong của %s có số đo bằng $180^\\circ - \\frac{360^\\circ}{%s} = 180^\\circ - %s^\\circ = %s^\\circ$.''' % (ten1, n1, gt1, g1))

    vd_da_1_d = '\\True Mỗi góc trong của %s có số đo bằng $%s^\\circ$' % (ten2, g2)
    vd_da_1_s = 'Mỗi góc trong của %s có số đo bằng $%s^\\circ$' % (ten2, g2 + 15)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Mỗi góc trong của %s có số đo bằng $180^\\circ - \\frac{360^\\circ}{%s} = 180^\\circ - %s^\\circ = %s^\\circ$.''' % (ten2, n2, gt2, g2))

    vdc_da_1_d = '\\True Tổng số đo của một góc trong %s và một góc trong %s bằng $%s^\\circ$' % (ten1, ten2, tong_g)
    vdc_da_1_s = 'Tổng số đo của một góc trong %s và một góc trong %s bằng $%s^\\circ$' % (ten1, ten2, tong_g - 3)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Tổng số đo một góc trong của %s và một góc trong của %s bằng $%s^\\circ + %s^\\circ = %s^\\circ$.''' % (ten1, ten2, g1, g2, tong_g))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
