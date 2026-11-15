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


def bt_dang18_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mu_val, coef_prod = random.choice([(0.5, 9.8), (0.8, 15.68)])
        mu_str = str(mu_val).replace('.', ',')
        coef_str = str(coef_prod).replace('.', ',')

        k_ratio = random.choice([2, 3])
        k_sq = k_ratio**2
        s_sub = 25 if mu_val == 0.8 else 20
        prod_sub = int(round(coef_prod * s_sub))
        v_sub_str = "14\\sqrt{2}" if prod_sub == 392 else "14"

        noidungcauhoi = ('''Khi một ô tô phanh gấp trên mặt đường khô, tốc độ $v$ $(\\text{m/s})$ của xe ngay trước khi phanh có thể ước tính qua chiều dài vết trượt của lốp xe $s$ $(\\text{m})$ và hệ số ma sát $\\mu$ theo công thức $v = \\sqrt{2 \\cdot g \\cdot \\mu \\cdot s}$, trong đó $g \\approx 9,8\\text{ m/s}^2$ là gia tốc trọng trường. Giả sử hai xe $A$ và $B$ cùng phanh gấp trên cùng một đoạn đường có hệ số ma sát $\\mu = %s$. Xét tính đúng sai của các khẳng định sau:''' % (mu_str))

        nb_da_1_d = '\\True Công thức tính tốc độ theo chiều dài vết trượt trên đoạn đường này là $v = \\sqrt{%s \\cdot s}$' % (coef_str)
        nb_da_1_s = 'Công thức tính tốc độ theo chiều dài vết trượt trên đoạn đường này là $v = %s\\sqrt{s}$' % (coef_str)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thay $g = 9,8$ và $\\mu = %s$ vào công thức, ta được $v = \\sqrt{2 \\cdot 9,8 \\cdot %s \\cdot s} = \\sqrt{%s \\cdot s}$.''' % (mu_str, mu_str, coef_str))

        th_da_1_d = '\True Nếu vết trượt của xe $A$ dài $s_A = 10\text{ m}$ thì tốc độ của xe $A$ là $v_A = \sqrt{%s}\text{ m/s}$' % (str(round(coef_prod * 10, 1)).replace('.', ','))
        th_da_1_s = 'Nếu vết trượt của xe $A$ dài $s_A = 10\text{ m}$ thì tốc độ của xe $A$ là $v_A = %s\text{ m/s}$' % (str(round(coef_prod * 10, 1)).replace('.', ','))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thay $s_A = 10$ vào công thức $v = \sqrt{%s \cdot s}$, ta được $v_A = \sqrt{%s \cdot 10} = \sqrt{%s}\text{ (m/s)}$.''' % (coef_str, coef_str, str(round(coef_prod * 10, 1)).replace('.', ',')))

        vd_da_1_d = '\\True Nếu vết trượt của xe $B$ dài gấp $%d$ lần vết trượt của xe $A$ ($s_B = %ds_A$) thì tốc độ của xe $B$ gấp $%d$ lần tốc độ của xe $A$' % (k_sq, k_sq, k_ratio)
        vd_da_1_s = 'Nếu vết trượt của xe $B$ dài gấp $%d$ lần vết trượt của xe $A$ ($s_B = %ds_A$) thì tốc độ của xe $B$ gấp $%d$ lần tốc độ của xe $A$' % (k_sq, k_sq, k_sq)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Áp dụng quy tắc khai phương một tích, ta có $v_B = \\sqrt{%s \\cdot (%ds_A)} = \\sqrt{%d} \\cdot \\sqrt{%s \\cdot s_A} = %d v_A$. Vậy tốc độ của xe $B$ gấp $%d$ lần tốc độ của xe $A$.''' % (coef_str, k_sq, k_sq, coef_str, k_ratio, k_ratio))

        vdc_da_1_d = '\\True Khi vết trượt dài $s = %d\\text{ m}$, tốc độ của xe lúc phanh là $v = %s\\text{ m/s}$' % (s_sub, v_sub_str)
        vdc_da_1_s = 'Khi vết trượt dài $s = %d\\text{ m}$, tốc độ của xe lúc phanh là $v = %d\\text{ m/s}$' % (s_sub, prod_sub)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi $s = %d\\text{ m}$, ta có $v = \\sqrt{%s \\cdot %d} = \\sqrt{%d} = %s\\text{ (m/s)}$.''' % (s_sub, coef_str, s_sub, prod_sub, v_sub_str))

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
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
