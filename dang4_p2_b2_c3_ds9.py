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


def bt_dang4_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        m_val, n_val = random.choice([(6, 2), (8, 4), (9, 5), (10, 6)])
        k1 = random.choice([2, 3, 5])
        k2 = random.choice([3, 5, 7])

        num_M1 = k1 * (m_val**2)
        num_M2 = k1
        num_N1 = k2 * (n_val**2)
        num_N2 = k2

        diff_MN = m_val - n_val

        noidungcauhoi = ('''Cho hai biểu thức $M = \\dfrac{\\sqrt{%d}}{\\sqrt{%d}}$ và $N = \\sqrt{%d} : \\sqrt{%d}$. Xét tính đúng sai của các khẳng định sau:''' % (num_M1, num_M2, num_N1, num_N2))

        nb_da_1_d = '\\True Áp dụng quy tắc chia hai căn bậc hai, ta có $M = \\sqrt{\\dfrac{%d}{%d}} = %d$' % (num_M1, num_M2, m_val)
        nb_da_1_s = 'Áp dụng quy tắc chia hai căn bậc hai, ta có $M = \\sqrt{\\dfrac{%d}{%d}} = %d$' % (num_M1, num_M2, m_val**2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $M = \\dfrac{\\sqrt{%d}}{\\sqrt{%d}} = \\sqrt{\\dfrac{%d}{%d}} = \\sqrt{%d} = %d$.''' % (num_M1, num_M2, num_M1, num_M2, m_val**2, m_val))

        th_da_1_d = '\\True Giá trị của $N$ bằng $%d$' % (n_val)
        th_da_1_s = 'Giá trị của $N$ bằng $%d$' % (n_val**2)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Ta có $N = \\sqrt{%d} : \\sqrt{%d} = \\sqrt{%d : %d} = \\sqrt{%d} = %d$.''' % (num_N1, num_N2, num_N1, num_N2, n_val**2, n_val))

        if m_val % n_val == 0:
            vd_da_1_d = '\\True Thương $\\dfrac{M}{N}$ bằng $%d$' % (m_val // n_val)
            vd_da_1_s = 'Thương $\\dfrac{M}{N}$ bằng $%d$' % (m_val // n_val + 1)
            loigiai_vd_1 = ('''Thay $M = %d$ và $N = %d$, ta được $\\dfrac{M}{N} = \\dfrac{%d}{%d} = %d$.''' % (m_val, n_val, m_val, n_val, m_val // n_val))
        else:
            frac_MN = Rational(m_val, n_val)
            vd_da_1_d = '\\True Thương $\\dfrac{M}{N}$ bằng $%s$' % (latex(frac_MN))
            vd_da_1_s = 'Thương $\\dfrac{M}{N}$ bằng $%s$' % (latex(frac_MN + 1))
            loigiai_vd_1 = ('''Thay $M = %d$ và $N = %d$, ta được $\\dfrac{M}{N} = \\dfrac{%d}{%d} = %s$.''' % (m_val, n_val, m_val, n_val, latex(frac_MN)))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Hiệu $M - N = %d$ là một số chính phương' % (diff_MN)
        vdc_da_1_s = 'Hiệu $M - N = %d$ là một số nguyên tố' % (diff_MN)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Ta có $M - N = %d - %d = %d = %d^2$, nên $M - N$ là một số chính phương.''' % (m_val, n_val, diff_MN, math.isqrt(diff_MN)))

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
