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


def bt_dang6_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        p1 = random.choice([2, 3])
        q1 = random.choice([3, 5])
        a1, b1, c1 = p1**2, -2*p1*q1, q1**2
        x_kep = Rational(q1, p1)

        b2 = random.choice([3, 5])
        c2 = random.choice([4, 5])
        delta2 = b2**2 - 4*(-2)*(-c2)

        a3 = random.choice([3, 5])
        b3 = random.choice([4, 7])
        c3 = -random.choice([2, 6])

        noidungcauhoi = ('Cho ba phương trình bậc hai: \\\\ $(1): %sx^2 %sx + %s = 0$; $\\quad (2): -2x^2 + %sx - %s = 0$; $\\quad (3): %sx^2 + %sx %s = 0$. \\\\ Xét tính đúng sai của các khẳng định sau:' % (a1, b1, c1, b2, c2, a3, b3, c3))

        nb_da_1_d = '\\True Phương trình $(3)$ có hệ số $a$ và $c$ trái dấu nên chắc chắn có hai nghiệm phân biệt'
        nb_da_1_s = 'Phương trình $(3)$ vô nghiệm vì có hệ số $c = %s < 0$' % (c3)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Phương trình $(3)$ có $a = %s > 0$ và $c = %s < 0$ nên $a$ và $c$ trái dấu ($ac < 0$). \\\\ Do đó $\\Delta = b^2 - 4ac > 0$, phương trình $(3)$ chắc chắn có hai nghiệm phân biệt.' % (a3, c3))

        th_da_1_d = '\\True Phương trình $(2)$ có biệt thức $\\Delta = %s < 0$ nên phương trình vô nghiệm' % (delta2)
        th_da_1_s = 'Phương trình $(2)$ có biệt thức $\\Delta = %s > 0$ nên có hai nghiệm phân biệt' % (-delta2)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Phương trình $(2)$ có $\\Delta = %s^2 - 4 \\cdot (-2) \\cdot (-%s) = %s - %s = %s < 0$. \\\\ Vậy phương trình $(2)$ vô nghiệm.' % (b2, c2, b2**2, 8*c2, delta2))

        vd_da_1_d = '\\True Phương trình $(1)$ có biệt thức $\\Delta = 0$ nên có nghiệm kép $x_1 = x_2 = %s$' % (latex(x_kep))
        vd_da_1_s = 'Phương trình $(1)$ có biệt thức $\\Delta = 0$ nên có nghiệm kép $x_1 = x_2 = -%s$' % (latex(x_kep))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Phương trình $(1)$ có $\\Delta = (%s)^2 - 4 \\cdot %s \\cdot %s = 0$. \\\\ Do đó phương trình có nghiệm kép $x_1 = x_2 = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot %s} = %s$.' % (b1, a1, c1, b1, a1, latex(x_kep)))

        vdc_da_1_d = '\\True Tổng số nghiệm thực phân biệt của cả ba phương trình trên là $3$'
        vdc_da_1_s = 'Tổng số nghiệm thực phân biệt của cả ba phương trình trên là $4$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Phương trình $(1)$ có $1$ nghiệm kép ($x = %s$), phương trình $(2)$ có $0$ nghiệm, phương trình $(3)$ có $2$ nghiệm phân biệt. \\\\ Vậy tổng cộng cả ba phương trình có $1 + 0 + 2 = 3$ nghiệm thực phân biệt.' % (latex(x_kep)))

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
