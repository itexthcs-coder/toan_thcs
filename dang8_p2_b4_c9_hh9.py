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


def bt_dang8_p2_b4_c9_hh9(self):
    ten_ng = random.choice(["ABCDE", "MNPQK"])
    a, b, c, d, e = ten_ng[0], ten_ng[1], ten_ng[2], ten_ng[3], ten_ng[4]

    hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (B) at (162:1.7);
\\coordinate (C) at (234:1.7);
\\coordinate (D) at (306:1.7);
\\coordinate (E) at (18:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--(E)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (C) circle (1pt) node[below left] {$%s$};
\\fill (D) circle (1pt) node[below right] {$%s$};
\\fill (E) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (a, b, c, d, e)

    noidungcauhoi = ('''Cho ngũ giác đều $%s$ nội tiếp đường tròn $(O)$ với các đỉnh $%s, %s, %s, %s, %s$ sắp xếp theo thứ tự ngược chiều kim đồng hồ (như hình vẽ). Xét tính đúng sai của các khẳng định sau: %s''' % (ten_ng, a, b, c, d, e, hinh_tikz))

    nb_da_1_d = '\\True Phép quay thuận chiều $216^\\circ$ tâm $O$ biến điểm $%s$ thành điểm $%s$' % (a, c)
    nb_da_1_s = 'Phép quay thuận chiều $144^\\circ$ tâm $O$ biến điểm $%s$ thành điểm $%s$' % (a, c)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Mỗi cung nhỏ của ngũ giác đều có số đo bằng $\\frac{360^\\circ}{5} = 72^\\circ$. Đi thuận chiều kim đồng hồ từ $%s$ qua $%s, %s$ đến $%s$ gồm $3$ cung nhỏ nên góc quay là $3 \\cdot 72^\\circ = 216^\\circ$.''' % (a, e, d, c))

    th_da_1_d = '\\True Phép quay ngược chiều $144^\\circ$ tâm $O$ biến điểm $%s$ thành điểm $%s$' % (b, d)
    th_da_1_s = 'Phép quay ngược chiều $144^\\circ$ tâm $O$ biến điểm $%s$ thành điểm $%s$' % (b, e)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Đi ngược chiều kim đồng hồ từ $%s$ qua $%s$ đến $%s$ gồm $2$ cung nhỏ nên góc quay bằng $2 \\cdot 72^\\circ = 144^\\circ$.''' % (b, c, d))

    vd_da_1_d = '\\True Phép quay thuận chiều $288^\\circ$ tâm $O$ biến cạnh $%s%s$ thành cạnh $%s%s$' % (a, e, e, d)
    vd_da_1_s = 'Phép quay thuận chiều $288^\\circ$ tâm $O$ biến cạnh $%s%s$ thành cạnh $%s%s$' % (a, e, b, c)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $288^\\circ = 4 \\cdot 72^\\circ$. Phép quay thuận chiều $288^\\circ$ tâm $O$ biến $%s$ thành $%s$ và biến $%s$ thành $%s$ nên biến cạnh $%s%s$ thành cạnh $%s%s$.''' % (a, e, e, d, a, e, e, d))

    vdc_da_1_d = '\\True Phép quay ngược chiều $72^\\circ$ tâm $O$ giữ nguyên ngũ giác đều $%s$' % (ten_ng)
    vdc_da_1_s = 'Phép quay ngược chiều $36^\\circ$ tâm $O$ giữ nguyên ngũ giác đều $%s$' % (ten_ng)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Phép quay ngược chiều $72^\\circ$ tâm $O$ biến các đỉnh $%s, %s, %s, %s, %s$ lần lượt thành $%s, %s, %s, %s, %s$ nên giữ nguyên ngũ giác đều $%s$.''' % (a, b, c, d, e, b, c, d, e, a, ten_ng))

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
