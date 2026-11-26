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

def bt_dang15_p4_b3_c7_ds8(self):
    # Dạng 15: Khôi phục hàm số y = ax + b từ tọa độ hai điểm trên đồ thị và tìm giao điểm với trục hoành
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, 4])
        x_int = random.choice([1, 2, 3]) # giao điểm trục hoành (x_int; 0)
        b = -a * x_int
        x2 = x_int + random.choice([1, 2])
        y2 = a * x2 + b

        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-1.5,0) -- (3.5,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,2.5) node[left] {$y$};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (0,-1.8);\n'
            '\\coordinate (B) at (2.4,1.8);\n'
            '\\coordinate (E) at (1.2,0);\n'
            '\\draw[line width=1pt] (-0.4,-2.4) -- (2.8,2.4);\n'
            '\\draw[line width=1pt, dashed] (2.4,0) -- (B) -- (0,1.8);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (A) circle (1pt) node[left] {$A(0; %s)$};\n'
            '\\fill (B) circle (1pt) node[above right] {$B(%s; %s)$};\n'
            '\\fill (E) circle (1pt) node[below right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (b, x2, y2)

        noidungcauhoi = (
            'Đồ thị của hàm số bậc nhất $y = f(x) = ax + b$ là đường thẳng đi qua hai điểm $A(0; %s)$ và $B(%s; %s)$, cắt trục hoành $Ox$ tại điểm $E$ như hình vẽ:\\ %s'
        ) % (b, x2, y2, hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Điểm $A(0; %s)$ nằm trên trục tung $Oy$ nên hệ số tự do là $b = %s$' % (b, b)
        nb_da_1_s = 'Điểm $A(0; %s)$ nằm trên trục hoành $Ox$ nên hệ số tự do là $b = 0$' % (b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Vì đồ thị đi qua $A(0; %s)$ nên $f(0) = a \\cdot 0 + b = %s \\Rightarrow b = %s$.' % (b, b, b)

        # Thông hiểu
        th_da_1_d = '\\True Hệ số $a$ của hàm số trên là $a = %s$' % (a)
        th_da_1_s = 'Hệ số $a$ của hàm số trên là $a = %s$' % (-a)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Thay tọa độ $B(%s; %s)$ và $b = %s$ vào công thức: $%s = a \\cdot %s + (%s) \\Leftrightarrow %sa = %s \\Leftrightarrow a = %s$.' % (x2, y2, b, y2, x2, b, x2, y2 - b, a)

        # Vận dụng
        vd_da_1_d = '\\True Giao điểm $E$ của đồ thị hàm số với trục hoành $Ox$ có tọa độ là $E(%s; 0)$' % (x_int)
        vd_da_1_s = 'Giao điểm $E$ của đồ thị hàm số với trục hoành $Ox$ có tọa độ là $E(0; %s)$' % (x_int)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'Điểm $E$ nằm trên trục hoành $Ox$ nên $y_E = 0$. Giải $%sx %s = 0 \\Leftrightarrow x = %s$. Vậy $E(%s; 0)$.' % (a, b, x_int, x_int)

        # Vận dụng cao
        area_OAE = (abs(b) * x_int) // 2
        vdc_da_1_d = '\\True Diện tích tam giác $OAE$ tạo bởi đồ thị và hai trục tọa độ bằng $%s$ đơn vị diện tích' % (area_OAE)
        vdc_da_1_s = 'Diện tích tam giác $OAE$ tạo bởi đồ thị và hai trục tọa độ bằng $%s$ đơn vị diện tích' % (abs(b) * x_int)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = 'Tam giác $OAE$ vuông tại $O$ có $OA = |%s| = %s$ và $OE = %s$, nên $S_{OAE} = \\dfrac{1}{2} \\cdot %s \\cdot %s = %s$ (đơn vị diện tích).' % (b, abs(b), x_int, abs(b), x_int, area_OAE)

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
