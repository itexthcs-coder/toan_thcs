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

def bt_dang15_p2_b3_c5_ds8(self):
    # Dạng 15: Kết hợp biểu đồ cột kép và đơn giá để tính lợi nhuận thực tế của doanh nghiệp
    hn1, hn2 = 240, 310
    dn1, dn2 = 160, 210
    loi_don = Decimal('1.5') # triệu đồng/chiếc
    
    tong_q1 = hn1 + dn1 # 400
    tong_q2 = hn2 + dn2 # 520
    chenh_q = tong_q2 - tong_q1 # 120
    
    tong_hn = hn1 + hn2 # 550
    tong_dn = dn1 + dn2 # 370
    tong_all = tong_hn + tong_dn # 920
    
    ln_hn = int(Decimal(tong_hn) * loi_don) # 825
    ln_diff = int(Decimal(tong_hn - tong_dn) * loi_don) # 270
    
    pct_dn = (Decimal(tong_dn * 100) / Decimal(tong_all)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) # 40.22
    pct_dn_str = str(pct_dn).replace('.', ',')
    
    y_hn = [round(v / 100.0, 2) for v in [hn1, hn2]]
    y_dn = [round(v / 100.0, 2) for v in [dn1, dn2]]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[below] {Quý};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số máy (chiếc)};\n' +
        '\\foreach \\y/\\lbl in {1/100, 2/200, 3/300, 4/400}{\n' +
        '    \\draw[line width=1pt, dashed] (0,\\y) -- (4.8,\\y);\n' +
        '    \\node[left] at (0,\\y) {$\\lbl$};\n' +
        '}\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!15] (0.8,0) rectangle (1.5,%s); \\node[above] at (1.15,%s) {$%s$};\n' % (y_hn[0], y_hn[0], hn1) +
        '\\draw[line width=1pt, fill=black!45] (1.5,0) rectangle (2.2,%s); \\node[above] at (1.85,%s) {$%s$};\n' % (y_dn[0], y_dn[0], dn1) +
        '\\node[below] at (1.5,0) {Quý I};\n' +
        '\\draw[line width=1pt, fill=black!15] (2.9,0) rectangle (3.6,%s); \\node[above] at (3.25,%s) {$%s$};\n' % (y_hn[1], y_hn[1], hn2) +
        '\\draw[line width=1pt, fill=black!45] (3.6,0) rectangle (4.3,%s); \\node[above] at (3.95,%s) {$%s$};\n' % (y_dn[1], y_dn[1], dn2) +
        '\\node[below] at (3.6,0) {Quý II};\n' +
        '\\draw[line width=1pt, fill=black!15] (5.4,3.2) rectangle (5.8,3.5) node[right, yshift=-4pt] {Hà Nội};\n' +
        '\\draw[line width=1pt, fill=black!45] (5.4,2.4) rectangle (5.8,2.7) node[right, yshift=-4pt] {Đà Nẵng};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột kép dưới đây ghi lại số lượng máy lọc nước bán ra (chiếc) tại hai chi nhánh Hà Nội và Đà Nẵng trong Quý I và Quý II. Biết rằng mỗi chiếc máy lọc nước bán ra mang lại lợi nhuận ròng trung bình là $1,5$ triệu đồng:\n' +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Tổng số máy lọc nước cả hai chi nhánh bán được trong Quý II nhiều hơn Quý I là $%s$ chiếc' % chenh_q
    nb_da_1_s = 'Tổng số máy lọc nước cả hai chi nhánh bán được trong Quý II nhiều hơn Quý I là $100$ chiếc'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Quý I bán được $%s + %s = %s$ chiếc; Quý II bán được $%s + %s = %s$ chiếc. Chênh lệch là $%s - %s = %s$ (chiếc).' % (hn1, dn1, tong_q1, hn2, dn2, tong_q2, tong_q2, tong_q1, chenh_q))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Tổng lợi nhuận ròng của Chi nhánh Hà Nội trong hai quý đạt $%s$ triệu đồng' % ln_hn
    th_da_1_s = 'Tổng lợi nhuận ròng của Chi nhánh Hà Nội trong hai quý đạt $750$ triệu đồng'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Tổng số máy Chi nhánh Hà Nội bán được trong hai quý là $%s + %s = %s$ (chiếc), thu về lợi nhuận $%s \\cdot 1,5 = %s$ (triệu đồng).' % (hn1, hn2, tong_hn, tong_hn, ln_hn))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Trong cả hai quý, lợi nhuận của Chi nhánh Hà Nội nhiều hơn Chi nhánh Đà Nẵng là $%s$ triệu đồng' % ln_diff
    vd_da_1_s = 'Trong cả hai quý, lợi nhuận của Chi nhánh Hà Nội nhiều hơn Chi nhánh Đà Nẵng là $180$ triệu đồng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Chi nhánh Hà Nội bán nhiều hơn Đà Nẵng là $%s - %s = %s$ (chiếc), tương ứng lợi nhuận nhiều hơn $%s \\cdot 1,5 = %s$ (triệu đồng).' % (tong_hn, tong_dn, tong_hn - tong_dn, tong_hn - tong_dn, ln_diff))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Tổng số máy bán được của Chi nhánh Đà Nẵng chiếm khoảng $%s\\%%$ tổng số máy bán được của cả hai chi nhánh' % pct_dn_str
    vdc_da_1_s = 'Tổng số máy bán được của Chi nhánh Đà Nẵng chiếm đúng $45\\%%$ tổng số máy bán được của cả hai chi nhánh'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng số máy bán được của cả hai chi nhánh là $%s + %s = %s$ (chiếc). Tỉ trọng của Đà Nẵng là $\\dfrac{%s}{%s} \\cdot 100\\%% \\approx %s\\%%$.' % (tong_hn, tong_dn, tong_all, tong_dn, tong_all, pct_dn_str))
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
