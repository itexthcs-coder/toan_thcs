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


def bt_dang12_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        k_mul = random.choice([1, 2])
        xA_val = -2 * k_mul
        yA_val = 2 * (k_mul**2)
        xB_val = 4 * k_mul
        yB_val = 8 * (k_mul**2)
        m_d = k_mul
        n_d = 4 * (k_mul**2)
        area_OAB = (n_d * (abs(xA_val) + abs(xB_val))) // 2
        str_md = str(m_d) if m_d > 1 else ''

        tikz_fig = ('\\begin{center}\n' +
                    '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
                    '\\draw[->, line width=1pt] (-3.5,0) -- (4.5,0) node[below] {$x$};\n' +
                    '\\draw[->, line width=1pt] (0,-0.8) -- (0,5.2) node[left] {$y$};\n' +
                    '\\draw[line width=1pt, smooth, samples=100, domain=-3:3] plot(\\x, {0.5*(\\x)^2});\n' +
                    '\\draw[line width=1pt, domain=-3.2:3.5] plot(\\x, {0.5*\\x + 2});\n' +
                    '\\coordinate (O) at (0,0);\n' +
                    '\\coordinate (A) at (-1.5,1.125);\n' +
                    '\\coordinate (B) at (2.5,3.125);\n' +
                    '\\coordinate (C) at (0,2);\n' +
                    '\\draw[line width=1pt, dashed] (-1.5,0) -- (A) -- (0,1.125);\n' +
                    '\\draw[line width=1pt, dashed] (2.5,0) -- (B) -- (0,3.125);\n' +
                    '\\fill (O) circle (1pt) node[below left] {$O$};\n' +
                    '\\fill (A) circle (1pt) node[above left] {$A$};\n' +
                    '\\fill (B) circle (1pt) node[above left] {$B$};\n' +
                    '\\fill (C) circle (1pt) node[above left] {$C$};\n' +
                    '\\end{tikzpicture}\n' +
                    '\\end{center}')

        noidungcauhoi = ('Trong mặt phẳng tọa độ $Oxy$, cho parabol $(P): y = \\frac{1}{2}x^2$ và đường thẳng $(d): y = %sx + %s$ (hình vẽ minh họa).\n%s\nXét tính đúng sai của các khẳng định sau:' % (str_md, n_d, tikz_fig))

        nb_da_1_d = '\\True Điểm $A(%s; %s)$ thuộc parabol $(P)$' % (xA_val, yA_val)
        nb_da_1_s = 'Điểm $A(%s; -%s)$ thuộc parabol $(P)$' % (xA_val, yA_val)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thay $x = %s$ vào hàm số $y = \\frac{1}{2}x^2$ ta được $y = \\frac{1}{2} \\cdot (%s)^2 = %s$. Vậy điểm $A(%s; %s)$ thuộc $(P)$.' % (xA_val, xA_val, yA_val, xA_val, yA_val))

        th_da_1_d = '\\True Hoành độ giao điểm của $(P)$ và $(d)$ là nghiệm của phương trình $x^2 - %sx - %s = 0$' % (2*m_d, 2*n_d)
        th_da_1_s = 'Hoành độ giao điểm của $(P)$ và $(d)$ là nghiệm của phương trình $x^2 + %sx + %s = 0$' % (2*m_d, 2*n_d)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Phương trình hoành độ giao điểm của $(P)$ và $(d)$ là: \\\\ $\\frac{1}{2}x^2 = %sx + %s \\Leftrightarrow x^2 = %sx + %s \\Leftrightarrow x^2 - %sx - %s = 0$.' % (str_md, n_d, 2*m_d, 2*n_d, 2*m_d, 2*n_d))

        vd_da_1_d = '\\True Đường thẳng $(d)$ cắt parabol $(P)$ tại hai điểm phân biệt nằm ở hai phía khác nhau của trục tung $Oy$'
        vd_da_1_s = 'Đường thẳng $(d)$ cắt parabol $(P)$ tại hai điểm phân biệt nằm cùng một phía đối với trục tung $Oy$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Giải phương trình $x^2 - %sx - %s = 0$ ta được hai nghiệm $x_1 = %s < 0$ và $x_2 = %s > 0$. \\\\ Do hai hoành độ trái dấu nên hai giao điểm $A, B$ nằm ở hai phía khác nhau đối với trục tung $Oy$.' % (2*m_d, 2*n_d, xA_val, xB_val))

        vdc_da_1_d = '\\True Diện tích tam giác $OAB$ (với $A, B$ là hai giao điểm của $(d)$ và $(P)$) bằng $%s$ (đơn vị diện tích)' % (area_OAB)
        vdc_da_1_s = 'Diện tích tam giác $OAB$ (với $A, B$ là hai giao điểm của $(d)$ và $(P)$) bằng $%s$ (đơn vị diện tích)' % (area_OAB // 2)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Gọi $C(0; %s)$ là giao điểm của đường thẳng $(d)$ với trục tung $Oy \\Rightarrow OC = %s$. \\\\ Hai giao điểm là $A(%s; %s)$ và $B(%s; %s)$. \\\\ Diện tích $\\triangle OAB$ là: $S_{\\triangle OAB} = S_{\\triangle OAC} + S_{\\triangle OBC} = \\frac{1}{2} \\cdot OC \\cdot |x_A| + \\frac{1}{2} \\cdot OC \\cdot |x_B| = \\frac{1}{2} \\cdot %s \\cdot (%s + %s) = %s$.' % (n_d, n_d, xA_val, yA_val, xB_val, yB_val, n_d, abs(xA_val), abs(xB_val), area_OAB))

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
