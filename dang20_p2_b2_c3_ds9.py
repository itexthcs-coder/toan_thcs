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


def bt_dang20_p2_b2_c3_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([2, 3])
        m, n = random.choice([(3, 5), (2, 3), (3, 4)])
        h1 = k * (m**2)
        h2 = k * (n**2)
        h3 = 4 * h1
        in_sqrt1 = str(round(12.74 * k, 2)).replace('.', ',')
        ratio_frac = Rational(n, m)

        noidungcauhoi = ('''Khoảng cách nhìn xa tối đa $d$ $(\\text{km})$ từ một người quan sát đứng ở độ cao $h$ $(\\text{m})$ so với mực nước biển đến đường chân trời được tính gần đúng bằng công thức $d = \\sqrt{12,74 \\cdot h}$. Một ngọn hải đăng có hai đài quan sát: đài thấp ở độ cao $h_1 = %d\\text{ m}$ và đài cao ở độ cao $h_2 = %d\\text{ m}$. Xét tính đúng sai của các khẳng định sau:''' % (h1, h2))

        nb_da_1_d = '\\True Tầm nhìn xa từ đài quan sát thấp là $d_1 = %d\\sqrt{%s}\\text{ km}$' % (m, in_sqrt1)
        nb_da_1_s = 'Tầm nhìn xa từ đài quan sát thấp là $d_1 = %d\\sqrt{%s}\\text{ km}$' % (m**2, in_sqrt1)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thay $h_1 = %d$ vào công thức, ta có $d_1 = \\sqrt{12,74 \\cdot %d} = \\sqrt{%d \\cdot %s} = %d\\sqrt{%s}\\text{ (km)}$.''' % (h1, h1, m**2, in_sqrt1, m, in_sqrt1))

        th_da_1_d = '\\True Tỉ số tầm nhìn xa giữa đài cao và đài thấp là $\\dfrac{d_2}{d_1} = %s$' % (latex(ratio_frac))
        th_da_1_s = 'Tỉ số tầm nhìn xa giữa đài cao và đài thấp là $\\dfrac{d_2}{d_1} = %s$' % (latex(Rational(n**2, m**2)))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Áp dụng quy tắc chia hai căn bậc hai, ta có $\\dfrac{d_2}{d_1} = \\dfrac{\\sqrt{12,74 \\cdot %d}}{\\sqrt{12,74 \\cdot %d}} = \\sqrt{\\dfrac{%d}{%d}} = \\sqrt{\\dfrac{%d}{%d}} = %s$.''' % (h2, h1, h2, h1, n**2, m**2, latex(ratio_frac)))

        vd_da_1_d = '\\True Hiệu tầm nhìn xa giữa đài cao và đài thấp là $d_2 - d_1 = %d\\sqrt{%s}\\text{ km}$' % (n - m, in_sqrt1)
        vd_da_1_s = 'Tầm nhìn xa từ đài cao lớn hơn tầm nhìn xa từ đài thấp đúng $10\\text{ km}$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Tương tự câu a, ta có $d_2 = %d\\sqrt{%s}\\text{ km}$. Do đó $d_2 - d_1 = %d\\sqrt{%s} - %d\\sqrt{%s} = %d\\sqrt{%s}\\text{ km}$.''' % (n, in_sqrt1, n, in_sqrt1, m, in_sqrt1, n - m, in_sqrt1))

        vdc_da_1_d = '\\True Muốn tầm nhìn xa tăng gấp đôi so với đài thấp ($d_3 = 2d_1$) thì cần xây đài quan sát ở độ cao $h_3 = %d\\text{ m}$' % (h3)
        vdc_da_1_s = 'Muốn tầm nhìn xa tăng gấp đôi so với đài thấp ($d_3 = 2d_1$) thì cần xây đài quan sát ở độ cao $h_3 = %d\\text{ m}$' % (2 * h1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Ta có $d_3 = 2d_1 \\Leftrightarrow \\sqrt{12,74 \\cdot h_3} = 2\\sqrt{12,74 \\cdot %d} = \\sqrt{12,74 \\cdot 4 \\cdot %d} \\Leftrightarrow h_3 = 4 \\cdot %d = %d\\text{ (m)}$.''' % (h1, h1, h1, h3))

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
