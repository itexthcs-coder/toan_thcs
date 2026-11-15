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


def bt_dang3_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k1 = random.choice([11, 12, 13, 14, 15, 16, 17, 18, 19, 25])
        num1_str = f"{k1**2 / 100:.2f}".replace('.', ',')
        ans1_str = f"{k1 / 10:.1f}".replace('.', ',')

        k2 = random.choice([2, 3, 4, 5])
        m2 = random.choice([6, 7, 8, 9])
        num2_a = f"{k2**2 / 100:.2f}".replace('.', ',')
        num2_b = m2**2
        ans2_str = f"{(k2 * m2) / 10:.1f}".replace('.', ',')

        pairs = [(2.5, 1.6, 2), (0.4, 0.9, 0.6), (1.6, 0.9, 1.2), (2.5, 0.9, 1.5)]
        p_a, p_b, p_ans = random.choice(pairs)
        pa_str = str(p_a).replace('.', ',')
        pb_str = str(p_b).replace('.', ',')
        pans_str = str(p_ans).replace('.', ',')

        k4 = random.choice([3, 4, 5, 6, 7, 8, 9])
        num4_str = f"{k4**2 / 10000:.4f}".replace('.', ',')
        ans4_true = f"{k4 / 100:.2f}".replace('.', ',')
        ans4_false = f"{k4 / 10:.1f}".replace('.', ',')

        noidungcauhoi = ('''Xét việc tính giá trị của các căn bậc hai liên quan đến số thập phân thông qua quy tắc khai phương một tích và một thương:''')

        nb_da_1_d = '\\True $\\sqrt{%s} = \\sqrt{\\dfrac{%d}{100}} = \\dfrac{%d}{10} = %s$' % (num1_str, k1**2, k1, ans1_str)
        nb_da_1_s = '$\\sqrt{%s} = \\sqrt{\\dfrac{%d}{10}} = %s$' % (num1_str, k1**2, ans1_str)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $%s = \\dfrac{%d}{100}$ nên $\\sqrt{%s} = \\sqrt{\\dfrac{%d}{100}} = \\dfrac{\\sqrt{%d}}{\\sqrt{100}} = \\dfrac{%d}{10} = %s$.''' % (num1_str, k1**2, num1_str, k1**2, k1**2, k1, ans1_str))

        th_da_1_d = '\\True $\\sqrt{%s \\cdot %d} = \\sqrt{%s} \\cdot \\sqrt{%d} = %s$' % (num2_a, num2_b, num2_a, num2_b, ans2_str)
        th_da_1_s = '$\\sqrt{%s \\cdot %d} = \\sqrt{%s} \\cdot \\sqrt{%d} = %d$' % (num2_a, num2_b, num2_a, num2_b, k2 * m2)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Ta có $\\sqrt{%s \\cdot %d} = \\sqrt{\\dfrac{%d}{100}} \\cdot \\sqrt{%d} = \\dfrac{%d}{10} \\cdot %d = %s$.''' % (num2_a, num2_b, k2**2, num2_b, k2, m2, ans2_str))

        vd_da_1_d = '\\True $\\sqrt{%s} \\cdot \\sqrt{%s} = %s$' % (pa_str, pb_str, pans_str)
        vd_da_1_s = '$\\sqrt{%s} \\cdot \\sqrt{%s} = %s$' % (pa_str, pb_str, str(round(p_a * p_b, 2)).replace('.', ','))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Áp dụng quy tắc nhân các căn bậc hai, ta có $\\sqrt{%s} \\cdot \\sqrt{%s} = \\sqrt{%s \\cdot %s} = \\sqrt{%s} = %s$.''' % (pa_str, pb_str, pa_str, pb_str, str(round(p_a * p_b, 2)).replace('.', ','), pans_str))

        vdc_da_1_d = '\\True $\\sqrt{%s} = %s$' % (num4_str, ans4_true)
        vdc_da_1_s = '$\\sqrt{%s} = %s$' % (num4_str, ans4_false)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Ta có $\\sqrt{%s} = \\sqrt{\\dfrac{%d}{10000}} = \\dfrac{\\sqrt{%d}}{\\sqrt{10000}} = \\dfrac{%d}{100} = %s$.''' % (num4_str, k4**2, k4**2, k4, ans4_true))

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
