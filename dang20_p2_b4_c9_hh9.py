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


def bt_dang20_p2_b4_c9_hh9(self):
    canh = random.choice([4, 6, 8, 10, 12])
    dt_o = Rational(3 * canh * canh, 2) * sqrt(3)

    hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A1) at (0:1.1);
\\coordinate (A2) at (60:1.1);
\\coordinate (A3) at (120:1.1);
\\coordinate (A4) at (180:1.1);
\\coordinate (A5) at (240:1.1);
\\coordinate (A6) at (300:1.1);
\\draw[line width=1pt] (O)--(A1)--(A2)--(A3)--cycle;
\\draw[line width=1pt] (O)--(A3)--(A4)--(A5)--cycle;
\\draw[line width=1pt] (O)--(A5)--(A6)--(A1)--cycle;
\\fill (O) circle (1pt) node[below right] {$O$};
\\end{tikzpicture}
\\end{center}'''

    noidungcauhoi = ('''Trong kiến trúc và tự nhiên (như cấu trúc các lỗ tổ ong), người ta thường sử dụng các viên gạch hoặc ô ngăn hình lục giác đều cạnh $a = %s\\text{ cm}$ ghép khít vào nhau quanh một đỉnh chung $O$ mà không để lại khe hở (như hình vẽ). Xét tính đúng sai của các khẳng định sau: %s''' % (canh, hinh_tikz))

    nb_da_1_d = '\\True Tại một đỉnh chung $O$, có thể ghép khít vừa đủ $3$ hình lục giác đều cạnh $%s\\text{ cm}$ mà không chồng lên nhau và không có khe hở' % (canh)
    nb_da_1_s = 'Tại một đỉnh chung $O$, có thể ghép khít vừa đủ $4$ hình lục giác đều cạnh $%s\\text{ cm}$ mà không chồng lên nhau và không có khe hở' % (canh)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Mỗi góc trong của hình lục giác đều bằng $120^\\circ$, do đó tại một đỉnh chung $O$ có thể ghép khít vừa đủ $\\frac{360^\\circ}{120^\\circ} = 3$ hình lục giác đều.''')

    th_da_1_d = '\\True Tổng số đo các góc của $3$ hình lục giác đều tại đỉnh chung $O$ bằng $360^\\circ$'
    th_da_1_s = 'Tổng số đo các góc của $3$ hình lục giác đều tại đỉnh chung $O$ bằng $300^\\circ$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tổng số đo của $3$ góc lục giác đều tại đỉnh $O$ bằng $3 \\cdot 120^\\circ = 360^\\circ$.''')

    vd_da_1_d = '\\True Nếu thay bằng các viên gạch hình ngũ giác đều thì không thể ghép khít quanh một đỉnh chung theo cách tương tự'
    vd_da_1_s = 'Nếu thay bằng các viên gạch hình ngũ giác đều thì cũng có thể ghép khít quanh một đỉnh chung theo cách tương tự'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Mỗi góc trong của ngũ giác đều bằng $108^\\circ$. Vì $360^\\circ$ không chia hết cho $108^\\circ$ ($3 \\cdot 108^\\circ = 324^\\circ < 360^\\circ < 4 \\cdot 108^\\circ = 432^\\circ$) nên không thể ghép khít các ngũ giác đều quanh một đỉnh.''')

    vdc_da_1_d = '\\True Diện tích bề mặt của mỗi ô lục giác đều cạnh $%s\\text{ cm}$ bằng $%s\\text{ cm}^2$' % (canh, latex(dt_o))
    vdc_da_1_s = 'Diện tích bề mặt của mỗi ô lục giác đều cạnh $%s\\text{ cm}$ bằng $%s\\text{ cm}^2$' % (canh, latex(dt_o // 2))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Diện tích mỗi ô lục giác đều cạnh $%s\\text{ cm}$ gồm $6$ tam giác đều cạnh $%s\\text{ cm}$ nên bằng $6 \\cdot \\frac{%s^2\\sqrt{3}}{4} = %s\\text{ cm}^2$.''' % (canh, canh, canh, latex(dt_o)))

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
