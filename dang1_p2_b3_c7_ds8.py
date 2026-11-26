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


def bt_dang1_p2_b3_c7_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        xs = sorted(random.sample(range(-6, 8), 5))
        c = random.choice([i for i in range(-5, 6) if i != 0])
        x1, x2, x3, x4, x5 = xs
        
        bang_latex = (
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|c|c|c|}\n'
            '\\hline\n'
            '$x$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '$y$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
        ) % (x1, x2, x3, x4, x5, c, c, c, c, c)
        
        tik_pts = ' '.join(['(%s,%s)' % (xi, c) for xi in xs])
        tik_dots = '\n'.join(['        \\fill (%s,%s) circle (1pt);' % (xi, c) for xi in xs])
        
        noidungcauhoi = (
            'Cho bảng giá trị tương ứng giữa hai đại lượng $x$ và $y$ như sau:%s'
            'Xét tính đúng sai của các khẳng định sau:'
        ) % bang_latex

        # Mệnh đề 1 (nb)
        nb_da_1_d = '\\True Đại lượng $y$ là một hàm số của đại lượng $x$'
        nb_da_1_s = 'Đại lượng $y$ không phải là hàm số của đại lượng $x$ vì các giá trị của $y$ không thay đổi'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = (
            'Với mỗi giá trị của $x \\in \\{%s; %s; %s; %s; %s\\}$, ta luôn xác định được duy nhất một giá trị tương ứng của $y$ (đều bằng $%s$). '
            'Do đó, đại lượng $y$ là một hàm số của đại lượng $x$ (gọi là hàm hằng).'
        ) % (x1, x2, x3, x4, x5, c)

        # Mệnh đề 2 (th)
        th_da_1_d = '\\True Đại lượng $x$ không phải là hàm số của đại lượng $y$'
        th_da_1_s = 'Đại lượng $x$ là một hàm số của đại lượng $y$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            'Khi $y = %s$, ta xác định được tới $5$ giá trị tương ứng khác nhau của $x$ là $%s; %s; %s; %s; %s$. '
            'Vì vậy, đại lượng $x$ không phải là hàm số của đại lượng $y$.'
        ) % (c, x1, x2, x3, x4, x5)

        # Mệnh đề 3 (vd)
        vd_da_1_d = '\\True Đồ thị của hàm số trên là tập hợp gồm $5$ điểm cùng nằm trên một đường thẳng song song với trục hoành'
        vd_da_1_s = 'Đồ thị của hàm số trên là tập hợp gồm $5$ điểm cùng nằm trên một đường thẳng song song với trục tung'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Đồ thị của hàm số gồm $5$ điểm $A(%s;%s)$, $B(%s;%s)$, $C(%s;%s)$, $D(%s;%s)$, $E(%s;%s)$. '
            'Vì tất cả các điểm này đều có tung độ bằng $%s \\neq 0$ nên chúng cùng nằm trên đường thẳng đi qua điểm $(0;%s)$ và song song với trục hoành $Ox$.'
        ) % (x1, c, x2, c, x3, c, x4, c, x5, c, c, c)

        # Mệnh đề 4 (vdc)
        tong_y = 5 * c
        vdc_da_1_d = '\\True Tổng các tung độ của tất cả các điểm thuộc đồ thị hàm số đã cho bằng $%s$' % tong_y
        vdc_da_1_s = 'Tổng các tung độ của tất cả các điểm thuộc đồ thị hàm số đã cho bằng $%s$' % (tong_y + c)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Đồ thị hàm số có $5$ điểm phân biệt và mỗi điểm đều có tung độ bằng $%s$. '
            'Vậy tổng các tung độ của $5$ điểm thuộc đồ thị là: $5 \\cdot (%s) = %s$.'
        ) % (c, c, tong_y)

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

        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]
        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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

