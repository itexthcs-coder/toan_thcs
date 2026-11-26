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


def bt_dang14_p2_b3_c7_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([3, 4, 5])
        b = random.choice([1, 2])
        ab_dist = 2 * b

        tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.65, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '    \\draw[line width=1pt, ->] (-1,0) -- (%s,0) node[below] {$x$};\n'
            '    \\draw[line width=1pt, ->] (0,%s) -- (0,%s) node[left] {$y$};\n'
            '    \\coordinate (O) at (0,0);\n'
            '    \\coordinate (A) at (%s,%s);\n'
            '    \\coordinate (B) at (%s,%s);\n'
            '    \\coordinate (C) at (%s,%s);\n'
            '    \\draw[line width=1pt] (A)--(B);\n'
            '    \\draw[line width=1pt, dashed] (0,%s)--(A) (0,%s)--(B) (%s,0)--(C)--(0,%s);\n'
            '    \\fill (O) circle (1pt) node[below left] {$O$};\n'
            '    \\fill (A) circle (1pt) node[above right] {$A$};\n'
            '    \\fill (B) circle (1pt) node[below right] {$B$};\n'
            '    \\fill (C) circle (1pt) node[above right] {$C$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (a + 1, -b - 1, a + 1, a, b, a, -b, b, a, b, -b, b, a)

        noidungcauhoi = (
            'Trên mặt phẳng tọa độ $Oxy$, cho điểm $A(%s; %s)$. Gọi $B$ là điểm có hoành độ bằng hoành độ điểm $A$ và tung độ đối với tung độ điểm $A$; '
            'gọi $C$ là điểm có tọa độ đảo ngược vị trí hoành độ và tung độ của điểm $A$ (như hình vẽ).%s'
            'Xét tính đúng sai của các khẳng định sau:'
        ) % (a, b, tikz_code)

        nb_da_1_d = '\\True Tọa độ của điểm $B$ là $(%s; -%s)$' % (a, b)
        nb_da_1_s = 'Tọa độ của điểm $B$ là $(-%s; %s)$' % (a, b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = (
            'Điểm $A(%s; %s)$ có hoành độ là $%s$ và tung độ là $%s$. '
            'Điểm $B$ có hoành độ bằng $%s$ và tung độ đối của $%s$ là $-%s$, nên $B(%s; -%s)$.'
        ) % (a, b, a, b, a, b, b, a, b)

        th_da_1_d = '\\True Tọa độ của điểm $C$ là $(%s; %s)$' % (b, a)
        th_da_1_s = 'Điểm $C$ trùng với điểm $A$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            'Khi đảo ngược vị trí hoành độ và tung độ của điểm $A(%s; %s)$, ta được hoành độ mới là $%s$ và tung độ mới là $%s$. '
            'Vậy $C(%s; %s)$ (khác điểm $A$ vì $%s \\neq %s$).'
        ) % (a, b, b, a, b, a, a, b)

        vd_da_1_d = '\\True Điểm $B$ nằm ở góc phần tư thứ IV của mặt phẳng tọa độ'
        vd_da_1_s = 'Hai điểm $A$ và $B$ cùng nằm ở góc phần tư thứ I'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Điểm $B(%s; -%s)$ có hoành độ $%s > 0$ và tung độ $-%s < 0$ nên nằm ở góc phần tư thứ IV (trong khi $A$ nằm ở góc phần tư thứ I).'
        ) % (a, b, a, b)

        vdc_da_1_d = '\\True Độ dài đoạn thẳng $AB$ bằng $%s$ đơn vị dài' % ab_dist
        vdc_da_1_s = 'Độ dài đoạn thẳng $AB$ bằng $%s$ đơn vị dài' % b
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Hai điểm $A(%s; %s)$ và $B(%s; -%s)$ có cùng hoành độ bằng $%s$ nên đoạn thẳng $AB$ song song với trục tung $Oy$. '
            'Độ dài đoạn thẳng $AB$ là: $AB = |%s - (-%s)| = %s$ (đơn vị dài).'
        ) % (a, b, a, b, a, b, b, ab_dist)

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

        list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]
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

