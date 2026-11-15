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


def bt_dang17_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        d_inch = random.choice([43, 50, 55, 65])
        width_inch = round(d_inch * 9 / math.sqrt(337), 2)
        length_inch = d_inch * 16 / math.sqrt(337)
        length_cm = round(length_inch * 2.54, 1)
        threshold_m = round((length_cm + 10) / 100, 1)

        width_str = f"{width_inch:.2f}".replace('.', ',')
        length_cm_str = f"{length_cm:.1f}".replace('.', ',')
        thresh_str = f"{threshold_m:.1f}".replace('.', ',')

        noidungcauhoi = ('''Kích thước màn hình tivi hình chữ nhật được xác định bởi độ dài đường chéo (tính bằng inch, biết $1\\text{ inch} \\approx 2,54\\text{ cm}$). Một chiếc tivi thông minh có tỉ lệ chiều dài và chiều rộng màn hình là $16 : 9$. Gọi $x$ $(\\text{inch})$ là chiều rộng của màn hình tivi ($x > 0$). Xét tính đúng sai của các khẳng định sau:''')

        nb_da_1_d = '\\True Chiều dài của màn hình tivi tính theo $x$ là $\\dfrac{16}{9}x$ $(\\text{inch})$'
        nb_da_1_s = 'Chiều dài của màn hình tivi tính theo $x$ là $\\dfrac{9}{16}x$ $(\\text{inch})$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì tỉ lệ chiều dài và chiều rộng màn hình là $16 : 9$ và chiều rộng là $x$ nên chiều dài của màn hình tivi là $\\dfrac{16}{9}x$ $(\\text{inch})$.''')

        th_da_1_d = '\\True Độ dài đường chéo $d$ $(\\text{inch})$ của màn hình tivi là $d = \\dfrac{\\sqrt{337}}{9}x$'
        th_da_1_s = 'Độ dài đường chéo $d$ $(\\text{inch})$ của màn hình tivi là $d = \\dfrac{25}{9}x$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Áp dụng định lí Pythagore và quy tắc khai phương một thương, một tích (với $x > 0$): \\\\ $d = \\sqrt{x^2 + \\left(\\dfrac{16}{9}x\\right)^2} = \\sqrt{x^2 + \\dfrac{256}{81}x^2} = \\sqrt{\\dfrac{337}{81}x^2} = \\dfrac{\\sqrt{337}}{9}x$.''')

        vd_da_1_d = '\\True Nếu tivi này là loại $%d\\text{ inch}$ ($d = %d$) thì chiều rộng $x$ xấp xỉ $%s\\text{ inch}$ (làm tròn đến chữ số thập phân thứ hai)' % (d_inch, d_inch, width_str)
        vd_da_1_s = 'Nếu tivi này là loại $%d\\text{ inch}$ ($d = %d$) thì chiều rộng $x$ xấp xỉ $%s\\text{ inch}$ (làm tròn đến chữ số thập phân thứ hai)' % (d_inch, d_inch, f"{width_inch + 3.5:.2f}".replace('.', ','))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Với $d = %d$, ta có $\\dfrac{\\sqrt{337}}{9}x = %d \\Rightarrow x = \\dfrac{%d \\cdot 9}{\\sqrt{337}} \\approx %s\\text{ (inch)}$.''' % (d_inch, d_inch, d_inch, width_str))

        vdc_da_1_d = '\\True Chiều dài của chiếc tivi $%d\\text{ inch}$ này nhỏ hơn $%s\\text{ mét}$' % (d_inch, thresh_str)
        vdc_da_1_s = 'Chiều dài của chiếc tivi $%d\\text{ inch}$ này lớn hơn $%s\\text{ mét}$' % (d_inch, thresh_str)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Chiều dài màn hình tivi là $\\dfrac{16}{9}x = \\dfrac{16}{9} \\cdot \\dfrac{%d \\cdot 9}{\\sqrt{337}} = \\dfrac{%d}{\\sqrt{337}}\\text{ (inch)} \\approx %s\\text{ cm} < %s\\text{ m}$.''' % (d_inch, d_inch * 16, length_cm_str, thresh_str))

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
               '\\end{ex}\n \end{minipage} \n\n')
    return content
