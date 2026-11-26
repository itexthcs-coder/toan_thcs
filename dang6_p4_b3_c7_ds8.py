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

def bt_dang6_p4_b3_c7_ds8(self):
    # Dạng 6: Bảng giá trị chứa tham số m và điều kiện để bảng xác định một hàm số
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x1 = random.choice([-3, -2])
        x2 = random.choice([1, 2])
        x4 = random.choice([4, 5])
        y1 = random.choice([2, 3])
        y2 = random.choice([5, 6])
        y3 = random.choice([8, 9])
        y4 = random.choice([10, 12])
        k = random.choice([1, 2, 3])

        bang_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[line width=1pt] (0,0) rectangle (10,1.6);\n'
            '\\draw[line width=1pt] (0,0.8) -- (10,0.8);\n'
            '\\draw[line width=1pt] (2,0) -- (2,1.6) (4,0) -- (4,1.6) (6,0) -- (6,1.6) (8,0) -- (8,1.6);\n'
            '\\node at (1,1.2) {$x$};\n'
            '\\node at (1,0.4) {$y$};\n'
            '\\node at (3,1.2) {$%s$};\n'
            '\\node at (3,0.4) {$%s$};\n'
            '\\node at (5,1.2) {$%s$};\n'
            '\\node at (5,0.4) {$%s$};\n'
            '\\node at (7,1.2) {$m - %s$};\n'
            '\\node at (7,0.4) {$%s$};\n'
            '\\node at (9,1.2) {$%s$};\n'
            '\\node at (9,0.4) {$%s$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (x1, y1, x2, y2, k, y3, x4, y4)

        noidungcauhoi = (
            'Cho bảng giá trị tương ứng giữa hai đại lượng $x$ và $y$ phụ thuộc vào tham số $m$ như sau:\\ %s'
        ) % (bang_tikz)

        m_bad1 = x1 + k
        m_bad2 = x2 + k
        m_bad3 = x4 + k
        sum_bad = m_bad1 + m_bad2 + m_bad3

        # Nhận biết
        nb_da_1_d = '\\True Khi $m = %s$ thì cột thứ ba của bảng có giá trị $x = %s$' % (m_bad1, x1)
        nb_da_1_s = 'Khi $m = %s$ thì cột thứ ba của bảng có giá trị $x = %s$' % (m_bad1, m_bad1)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Thay $m = %s$ vào biểu thức $m - %s$ ta được $x = %s - %s = %s$.' % (m_bad1, k, m_bad1, k, x1)

        # Thông hiểu
        th_da_1_d = '\\True Với $m = %s$, đại lượng $y$ không phải là hàm số của $x$ vì tại $x = %s$ có hai giá trị của $y$ là $%s$ và $%s$' % (m_bad1, x1, y1, y3)
        th_da_1_s = 'Với $m = %s$, đại lượng $y$ vẫn là hàm số của $x$ vì các giá trị của $y$ đều khác nhau' % (m_bad1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Khi $m = %s$ thì $m - %s = %s$, khi đó giá trị $x = %s$ ứng với hai giá trị khác nhau của $y$ là $%s$ và $%s$ nên $y$ không là hàm số của $x$.' % (m_bad1, k, x1, x1, y1, y3)

        # Vận dụng
        vd_da_1_d = '\\True Có đúng $3$ giá trị của tham số $m$ làm cho đại lượng $y$ không phải là hàm số của $x$'
        vd_da_1_s = 'Chỉ có duy nhất $1$ giá trị của tham số $m$ làm cho đại lượng $y$ không phải là hàm số của $x$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Vì các giá trị $y$ ở tất cả các cột ($%s; %s; %s; %s$) đều đôi một khác nhau nên $y$ không là hàm số của $x$ khi $m - %s$ trùng với một trong ba giá trị $%s; %s; %s$.\\ '
            'Suy ra $m \\in \\{%s; %s; %s\\}$ (có $3$ giá trị).'
        ) % (y1, y2, y3, y4, k, x1, x2, x4, m_bad1, m_bad2, m_bad3)

        # Vận dụng cao
        vdc_da_1_d = '\\True Điều kiện để $y$ là một hàm số của $x$ là $m \\notin \\{%s; %s; %s\\}$ và tổng các giá trị loại trừ của $m$ bằng $%s$' % (m_bad1, m_bad2, m_bad3, sum_bad)
        vdc_da_1_s = 'Điều kiện để $y$ là một hàm số của $x$ là $m \\notin \\{%s; %s; %s\\}$' % (x1, x2, x4)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Để $y$ là hàm số của $x$ thì $m - %s \\notin \\{%s; %s; %s\\} \\Leftrightarrow m \\notin \\{%s; %s; %s\\}$.\\ '
            'Tổng các giá trị loại trừ là $%s + %s + %s = %s$.'
        ) % (k, x1, x2, x4, m_bad1, m_bad2, m_bad3, m_bad1, m_bad2, m_bad3, sum_bad)

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
