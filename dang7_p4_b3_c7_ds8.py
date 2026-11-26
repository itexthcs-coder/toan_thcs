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

def bt_dang7_p4_b3_c7_ds8(self):
    # Dạng 7: Điểm thuộc đồ thị hàm số y = a*x + b và tìm tọa độ điểm thỏa mãn điều kiện ràng buộc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, 4])
        b = random.choice([-3, -2, -1, 1, 2])
        xA = random.choice([1, 2])
        yA = a * xA + b
        xB = random.choice([-2, -1])
        yB_wrong = a * xB + b + random.choice([2, 3])
        xD = 2 * yA
        yD = a * xD + b

        sign_b = '+' if b >= 0 else '-'
        abs_b = abs(b)

        # Hình vẽ minh họa mặt phẳng tọa độ với điểm A thuộc đồ thị và điểm B nằm ngoài
        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-2.5,0) -- (3,0) node[below] {$x$};\n'
            '\\draw[->, line width=1pt] (0,-2.5) -- (0,3) node[left] {$y$};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (A) at (1.2,1.8);\n'
            '\\coordinate (B) at (-1.2,1.2);\n'
            '\\draw[line width=1pt] (-1.2,-2.2) -- (1.8,2.8);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (A) circle (1pt) node[right] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        noidungcauhoi = (
            'Cho hàm số $y = f(x) = %sx %s %s$ và ba điểm $A(%s; %s)$, $B(%s; %s)$, $C(0; %s)$ trong mặt phẳng tọa độ $Oxy$ (hình minh họa):\\ %s'
        ) % (a, sign_b, abs_b, xA, yA, xB, yB_wrong, b, hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Điểm $C(0; %s)$ nằm trên trục tung $Oy$ và thuộc đồ thị của hàm số đã cho' % (b)
        nb_da_1_s = 'Điểm $C(0; %s)$ nằm trên trục hoành $Ox$ và không thuộc đồ thị hàm số' % (b)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Điểm $C(0; %s)$ có hoành độ bằng $0$ nên nằm trên trục tung $Oy$, và $f(0) = %s$ nên $C$ thuộc đồ thị hàm số.' % (b, b)

        # Thông hiểu
        th_da_1_d = '\\True Điểm $A(%s; %s)$ thuộc đồ thị hàm số còn điểm $B(%s; %s)$ không thuộc đồ thị hàm số' % (xA, yA, xB, yB_wrong)
        th_da_1_s = 'Cả hai điểm $A(%s; %s)$ và $B(%s; %s)$ đều thuộc đồ thị của hàm số đã cho' % (xA, yA, xB, yB_wrong)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = (
            'Ta có $f(%s) = %s \\cdot %s %s %s = %s = y_A$ nên $A$ thuộc đồ thị.\\ '
            'Còn $f(%s) = %s \\cdot (%s) %s %s = %s \\neq %s$ nên $B$ không thuộc đồ thị.'
        ) % (xA, a, xA, sign_b, abs_b, yA, xB, a, xB, sign_b, abs_b, a * xB + b, yB_wrong)

        # Vận dụng
        vd_da_1_d = '\\True Điểm $D$ thuộc đồ thị hàm số có hoành độ gấp đôi tung độ của $A$ thì có tọa độ là $D(%s; %s)$' % (xD, yD)
        vd_da_1_s = 'Điểm $D$ thuộc đồ thị hàm số có hoành độ gấp đôi tung độ của $A$ thì có tọa độ là $D(%s; %s)$' % (xD, yD + a)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = (
            'Hoành độ của $D$ là $x_D = 2 y_A = 2 \\cdot %s = %s$.\\ '
            'Tung độ của $D$ là $y_D = f(%s) = %s \\cdot %s %s %s = %s$. Vậy $D(%s; %s)$.'
        ) % (yA, xD, xD, a, xD, sign_b, abs_b, yD, xD, yD)

        # Vận dụng cao
        # Tìm điểm M(xM; yM) thuộc đồ thị sao cho xM = yM => xM = a*xM + b => (1-a)*xM = b
        # Để xM nguyên, chọn b chia hết cho (1 - a): ta lấy ví dụ khác hoặc tìm điểm N(xN; yN) sao cho yN - xN = k
        # Ở đây (a - 1)*x + b = y - x. Chọn xM = random.choice([-1, 1, 2]), diff_yx = yM - xM
        xM = random.choice([-1, 1, 2])
        yM = a * xM + b
        diff_yx = yM - xM
        vdc_da_1_d = '\\True Trên đồ thị hàm số có duy nhất một điểm $M$ thỏa mãn tung độ lớn hơn hoành độ $%s$ đơn vị, đó là $M(%s; %s)$' % (diff_yx, xM, yM)
        vdc_da_1_s = 'Trên đồ thị hàm số có hai điểm $M$ phân biệt thỏa mãn tung độ lớn hơn hoành độ $%s$ đơn vị' % (diff_yx)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Gọi $M(x_M; y_M)$ thuộc đồ thị hàm số nên $y_M = %sx_M %s %s$.\\ '
            'Theo đề bài $y_M - x_M = %s \\Leftrightarrow (%sx_M %s %s) - x_M = %s \\Leftrightarrow %sx_M = %s \\Leftrightarrow x_M = %s \\Rightarrow y_M = %s$.'
        ) % (a, sign_b, abs_b, diff_yx, a, sign_b, abs_b, diff_yx, a - 1, diff_yx - b, xM, yM)

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
