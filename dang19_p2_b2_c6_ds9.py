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


def bt_dang19_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        x1_val = 1
        x2_val = random.choice([4, 5])
        b_val = 0.25 * (x1_val + x2_val)
        b_str = str(b_val).replace('.', ',')
        sum_x = x1_val + x2_val

        x_floor = (sum_x + math.sqrt(sum_x**2 + 32)) / 2
        x_floor_round = str(Decimal(str(x_floor)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
        x_floor_wrong = str(Decimal(str(x_floor - 0.5)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

        tikz_fig = ('\\begin{center}\n' +
                    '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
                    '\\draw[->, line width=1pt] (-0.5,0) -- (6.5,0) node[below] {$x$};\n' +
                    '\\draw[->, line width=1pt] (0,-0.5) -- (0,4.2) node[left] {$y$};\n' +
                    '\\draw[line width=1pt, smooth, samples=100, domain=0:5.8] plot(\\x, {-0.2*(\\x)^2 + 1.0*\\x + 2});\n' +
                    '\\draw[line width=1.5pt] (4.2,0) -- (4.2,3.1);\n' +
                    '\\draw[line width=1.5pt] (3.8,3.05) -- (4.2,3.05);\n' +
                    '\\fill (0,0) circle (1pt) node[below left] {$O$};\n' +
                    '\\fill (0,2) circle (1.5pt) node[left] {$2$};\n' +
                    '\\end{tikzpicture}\n' +
                    '\\end{center}')

        noidungcauhoi = ('Trong một trận bóng rổ, một vận động viên ném bóng từ vị trí cách trụ rổ theo phương ngang $%s \\text{ m}$. Quỹ đạo bay của quả bóng trong mặt phẳng tọa độ $Oxy$ (với gốc $O$ là hình chiếu vuông góc của vị trí ném trên mặt sàn, đơn vị trên mỗi trục là mét) được cho bởi công thức $y = -0,25x^2 + %sx + 2$, trong đó $y$ là độ cao của bóng so với mặt sàn khi bóng cách vị trí ném một khoảng $x$ theo phương ngang ($x \\ge 0$, như hình vẽ).\n%s\nXét tính đúng sai của các khẳng định sau:' % (x2_val, b_str, tikz_fig))

        nb_da_1_d = '\\True Độ cao của quả bóng tại thời điểm rời tay vận động viên ($x = 0$) là $2 \\text{ m}$'
        nb_da_1_s = 'Độ cao của quả bóng tại thời điểm rời tay vận động viên ($x = 0$) là $2,25 \\text{ m}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thay $x = 0$ vào công thức quỹ đạo ta được $y = -0,25 \\cdot 0^2 + %s \\cdot 0 + 2 = 2 \\text{ (m)}$.' % (b_str))

        th_da_1_d = '\\True Quả bóng đạt độ cao $3 \\text{ m}$ tại hai thời điểm ứng với $x = 1 \\text{ m}$ và $x = %s \\text{ m}$' % (x2_val)
        th_da_1_s = 'Quả bóng đạt độ cao $3 \\text{ m}$ tại hai thời điểm ứng với $x = 2 \\text{ m}$ và $x = %s \\text{ m}$' % (x2_val)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Giải phương trình $-0,25x^2 + %sx + 2 = 3 \\Leftrightarrow -0,25x^2 + %sx - 1 = 0 \\Leftrightarrow x^2 - %sx + 4 = 0 \\Leftrightarrow x_1 = 1$ hoặc $x_2 = %s$.' % (b_str, b_str, sum_x, x2_val))

        vd_da_1_d = '\\True Biết vành rổ đặt ở độ cao $3,05 \\text{ m}$ so với mặt sàn và cách vị trí ném $%s \\text{ m}$ theo phương ngang, cú ném này đã đưa bóng đi thấp hơn vành rổ' % (x2_val)
        vd_da_1_s = 'Biết vành rổ đặt ở độ cao $3,05 \\text{ m}$ so với mặt sàn và cách vị trí ném $%s \\text{ m}$ theo phương ngang, cú ném này đã đưa bóng đi trúng vào rổ' % (x2_val)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Tại vị trí cách người ném $x = %s \\text{ m}$ theo phương ngang, độ cao của bóng là $y = 3 \\text{ m} < 3,05 \\text{ m}$ nên bóng bay thấp hơn vành rổ (không trúng rổ).' % (x2_val))

        vdc_da_1_d = '\\True Nếu không chạm rổ, quả bóng sẽ rơi chạm mặt sàn tại vị trí cách người ném khoảng $%s \\text{ m}$ (làm tròn đến hàng phần trăm)' % (x_floor_round)
        vdc_da_1_s = 'Nếu không chạm rổ, quả bóng sẽ rơi chạm mặt sàn tại vị trí cách người ném khoảng $%s \\text{ m}$ (làm tròn đến hàng phần trăm)' % (x_floor_wrong)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Bóng chạm mặt sàn khi $y = 0 \\Leftrightarrow -0,25x^2 + %sx + 2 = 0 \\Leftrightarrow x^2 - %sx - 8 = 0$. \\\\ Có $\\Delta = (-%s)^2 - 4 \\cdot 1 \\cdot (-8) = %s$. Vì $x > 0$ nên $x = \\frac{%s + \\sqrt{%s}}{2} \\approx %s \\text{ (m)}$.' % (b_str, sum_x, sum_x, sum_x**2 + 32, sum_x, sum_x**2 + 32, x_floor_round))

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
