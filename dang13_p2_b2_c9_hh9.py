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

def bt_dang13_p2_b2_c9_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_diem = [('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')]
        A, B, C = random.choice(bo_diem)
        bo_pytago = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)]
        ab, ac, bc = random.choice(bo_pytago)
        S = (ab * ac) // 2
        p = (ab + ac + bc) // 2
        r = S // p
        R_val = Rational(bc, 2)
        R_str = str(R_val.p) if R_val.q == 1 else str(float(R_val)).replace('.', ',')
        tong_R_r = R_val + r
        tong_str = str(tong_R_r.p) if tong_R_r.q == 1 else str(float(tong_R_r)).replace('.', ',')

        hinh_ve = ('''\\\\
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (B) at (-1.6,0);
\\coordinate (C) at (1.6,0);
\\coordinate (A) at (126:1.6);
\\coordinate (I) at (-0.35,0.48);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (I) circle (0.48);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (I) circle (1pt) node[above] {$I$};
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[left] {$%s$};
\\fill (C) circle (1pt) node[right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C))

        noidungcauhoi = ('''Cho tam giác $%s%s%s$ vuông tại $%s$ có $%s%s = %s\\text{ cm}$, $%s%s = %s\\text{ cm}$. Gọi $(I; r)$ là đường tròn nội tiếp tam giác $%s%s%s$ và $(O; R)$ là đường tròn ngoại tiếp tam giác $%s%s%s$. Xét tính đúng, sai của các khẳng định sau:%s''' % (A, B, C, A, A, B, ab, A, C, ac, A, B, C, A, B, C, hinh_ve))

        ######################################################################## Nhận biết ############################################
        nb_da_1_d = '\\True Diện tích tam giác $%s%s%s$ bằng $%s\\text{ cm}^2$' % (A, B, C, S)
        nb_da_1_s = 'Diện tích tam giác $%s%s%s$ bằng $%s\\text{ cm}^2$' % (A, B, C, ab * ac)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        list_nb_1 = [nb_da_1]
        loigiai_nb_1 = ('''Diện tích tam giác $%s%s%s$ vuông tại $%s$ là $S = \\frac{1}{2} \\cdot %s%s \\cdot %s%s = \\frac{1}{2} \\cdot %s \\cdot %s = %s\\text{ (cm}^2)$.''' % (A, B, C, A, A, B, A, C, ab, ac, S))
        list_nb_2 = [loigiai_nb_1]

        ######################################################################## Thông hiểu ############################################
        th_da_1_d = '\\True Nửa chu vi $p$ của tam giác $%s%s%s$ bằng $%s\\text{ cm}$' % (A, B, C, p)
        th_da_1_s = 'Nửa chu vi $p$ của tam giác $%s%s%s$ bằng $%s\\text{ cm}$' % (A, B, C, 2 * p)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        list_th_1 = [th_da_1]
        loigiai_th_1 = ('''Theo định lí Pythagore, $%s%s = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$. Nửa chu vi tam giác $%s%s%s$ là $p = \\frac{%s + %s + %s}{2} = %s\\text{ (cm)}$.''' % (B, C, ab, ac, bc, A, B, C, ab, ac, bc, p))
        list_th_2 = [loigiai_th_1]

        ######################################################################## Vận dụng ############################################
        vd_da_1_d = '\\True Bán kính đường tròn nội tiếp $r = %s\\text{ cm}$' % (r)
        vd_da_1_s = 'Bán kính đường tròn nội tiếp $r = %s\\text{ cm}$' % (r + 1)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        list_vd_1 = [vd_da_1]
        loigiai_vd_1 = ('''Ta có $S = p \\cdot r \\Rightarrow r = \\frac{S}{p} = \\frac{%s}{%s} = %s\\text{ (cm)}$.''' % (S, p, r))
        list_vd_2 = [loigiai_vd_1]

        ######################################################################## Vận dụng cao ############################################
        vdc_da_1_d = '\\True Tổng độ dài $R + r$ bằng $%s\\text{ cm}$' % (tong_str)
        vdc_da_1_s = 'Tổng độ dài $R + r$ bằng $%s\\text{ cm}$' % (bc)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        list_vdc_1 = [vdc_da_1]
        loigiai_vdc_1 = ('''Ta có $R = \\frac{%s%s}{2} = %s\\text{ (cm)}$ và $r = %s\\text{ cm}$, suy ra $R + r = %s + %s = %s\\text{ (cm)}$.''' % (B, C, R_str, r, R_str, r, tong_str))
        list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
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
