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

def bt_dang5_p4_b3_c7_ds8(self):
    # Dạng 5: Phân tích hệ thức liên hệ giữa hai đại lượng x, y để xác định y có phải hàm số của x không
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([3, 5, 7])
        c = a * b * random.choice([1, 2])
        r = random.choice([3, 4, 5])
        r2 = r ** 2

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (9.5,2.4);\n'
            '\\draw[line width=1pt] (0,1.6) -- (9.5,1.6) (0,0.8) -- (9.5,0.8);\n'
            '\\draw[line width=1pt] (3,0) -- (3,2.4);\n'
            '\\node at (1.5,2.0) {Kí hiệu};\n'
            '\\node at (6.25,2.0) {Hệ thức liên hệ giữa $x$ và $y$};\n'
            '\\node at (1.5,1.2) {Hệ thức $(1)$};\n'
            '\\node at (6.25,1.2) {$%sx + %sy = %s$ (với $x \\in \\mathbb{R}$)};\n'
            '\\node at (1.5,0.4) {Hệ thức $(2)$};\n'
            '\\node at (6.25,0.4) {$x^2 + y^2 = %s$ (với $-%s < x < %s$)};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (a, b, c, r2, r, r)

        noidungcauhoi = (
            'Xét hai đại lượng $x$ và $y$ được liên hệ bởi các hệ thức đại số cho trong bảng dưới đây:\\ %s'
        ) % (bang_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Từ hệ thức $(1)$, ta biểu diễn được $y$ theo $x$ là $y = \\dfrac{%s - %sx}{%s}$' % (c, a, b)
        nb_da_1_s = 'Từ hệ thức $(1)$, ta biểu diễn được $y$ theo $x$ là $y = \\dfrac{%s + %sx}{%s}$' % (c, a, b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Từ $%sx + %sy = %s \\Leftrightarrow %sy = %s - %sx \\Leftrightarrow y = \\dfrac{%s - %sx}{%s}$.' % (a, b, c, b, c, a, c, a, b)

        # Thông hiểu
        th_da_1_d = '\\True Trong hệ thức $(1)$, đại lượng $y$ là một hàm số của đại lượng $x$'
        th_da_1_s = 'Trong hệ thức $(1)$, đại lượng $y$ không phải là hàm số của đại lượng $x$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Với mỗi giá trị thực của $x$, biểu thức $y = \\dfrac{%s - %sx}{%s}$ xác định duy nhất một giá trị tương ứng của $y$ nên $y$ là hàm số của $x$.' % (c, a, b)

        # Vận dụng
        vd_da_1_d = '\\True Trong hệ thức $(2)$, tại $x = 0$ có hai giá trị của $y$ thỏa mãn là $y = %s$ và $y = -%s$' % (r, r)
        vd_da_1_s = 'Trong hệ thức $(2)$, tại $x = 0$ chỉ có duy nhất một giá trị của $y$ thỏa mãn là $y = %s$' % (r)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Thay $x = 0$ vào hệ thức $(2)$ ta được $0^2 + y^2 = %s \\Leftrightarrow y^2 = %s \\Leftrightarrow y = %s$ hoặc $y = -%s$.' % (r2, r2, r, r)

        # Vận dụng cao
        vdc_da_1_d = '\\True Trong hệ thức $(2)$, đại lượng $y$ không phải là hàm số của $x$ nhưng nếu thêm điều kiện $y \\ge 0$ thì $y$ trở thành hàm số của $x$'
        vdc_da_1_s = 'Trong hệ thức $(2)$, đại lượng $y$ luôn là hàm số của $x$ mà không cần thêm bất kì điều kiện nào của $y$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Vì với $x = 0$ có tới hai giá trị của $y$ ($y = %s$ và $y = -%s$) nên $y$ không là hàm số của $x$. '
            'Nếu thêm điều kiện $y \\ge 0$ thì với mỗi $x \\in (-%s; %s)$, giá trị $y = \\sqrt{%s - x^2}$ là duy nhất nên $y$ là hàm số của $x$.'
        ) % (r, r, r, r, r2)

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

        content = (
            '\\begin{minipage}{\\textwidth} \n'
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
            '\\end{ex}\n \\end{minipage}\n\n'
        )
        return content
