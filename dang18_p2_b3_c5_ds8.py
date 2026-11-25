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

def bt_dang18_p2_b3_c5_ds8(self):
    # Dạng 18: Khôi phục số liệu tuyệt đối khi biết hiệu số giữa hai phần trên biểu đồ hình quạt tròn
    p_tot, p_kha, p_dat, p_cd = 25, 45, 26, 4
    diff_p = p_kha - p_tot # 20%
    hieu_hs = random.choice([50, 60, 70, 80])
    tong_hs = int(hieu_hs * 100 // diff_p)
    hs_dat = int(tong_hs * p_dat // 100)
    hs_cd = int(tong_hs * p_cd // 100)
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:1.9) arc (0:90:1.9) -- cycle;\n' +
        '\\draw[line width=1pt, fill=black!25] (0,0) -- (90:1.9) arc (90:252:1.9) -- cycle;\n' +
        '\\draw[line width=1pt, fill=black!40] (0,0) -- (252:1.9) arc (252:345.6:1.9) -- cycle;\n' +
        '\\draw[line width=1pt, fill=white] (0,0) -- (345.6:1.9) arc (345.6:360:1.9) -- cycle;\n' +
        '\\node at (45:1.15) {$25\\%%$};\n' +
        '\\node at (171:1.15) {$45\\%%$};\n' +
        '\\node at (298:1.25) {$26\\%%$};\n' +
        '\\node at (353:1.5) {$4\\%%$};\n' +
        '\\draw[line width=1pt, fill=black!10] (2.6,1.2) rectangle (3.0,1.5) node[right, yshift=-4pt] {Mức Tốt};\n' +
        '\\draw[line width=1pt, fill=black!25] (2.6,0.4) rectangle (3.0,0.7) node[right, yshift=-4pt] {Mức Khá};\n' +
        '\\draw[line width=1pt, fill=black!40] (2.6,-0.4) rectangle (3.0,-0.1) node[right, yshift=-4pt] {Mức Đạt};\n' +
        '\\draw[line width=1pt, fill=white] (2.6,-1.2) rectangle (3.0,-0.9) node[right, yshift=-4pt] {Chưa đạt};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây thống kê kết quả xếp loại học tập cuối năm của học sinh khối $8$ một trường THCS. Biết rằng số học sinh xếp loại Khá nhiều hơn số học sinh xếp loại Tốt là $%s$ em:\n' % hieu_hs +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Tỉ lệ học sinh xếp loại Khá nhiều hơn tỉ lệ học sinh xếp loại Tốt là $20\\%%$ tổng số học sinh toàn khối'
    nb_da_1_s = 'Tỉ lệ học sinh xếp loại Khá nhiều hơn tỉ lệ học sinh xếp loại Tốt là $25\\%%$ tổng số học sinh toàn khối'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Chênh lệch tỉ lệ phần trăm giữa mức Khá ($45\\%%$) và mức Tốt ($25\\%%$) là $45\\%% - 25\\%% = 20\\%%$.' )
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Tổng số học sinh khối $8$ của trường đó là $%s$ học sinh' % tong_hs
    th_da_1_s = 'Tổng số học sinh khối $8$ của trường đó là $%s$ học sinh' % (tong_hs + 50)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Vì $20\\%%$ tổng số học sinh ứng với $%s$ em nên tổng số học sinh khối $8$ là $\\dfrac{%s}{20\\%%} = %s$ (học sinh).' % (hieu_hs, hieu_hs, tong_hs))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Số học sinh xếp loại Đạt của khối $8$ là $%s$ học sinh' % hs_dat
    vd_da_1_s = 'Số học sinh xếp loại Đạt của khối $8$ là $%s$ học sinh' % (hs_dat + 12)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Số học sinh xếp loại Đạt chiếm $26\\%%$, bằng $%s \\cdot 26\\%% = %s$ (học sinh).' % (tong_hs, hs_dat))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Có đúng $%s$ học sinh xếp loại Chưa đạt cần rèn luyện thêm trong hè' % hs_cd
    vdc_da_1_s = 'Có $%s$ học sinh xếp loại Chưa đạt cần rèn luyện thêm trong hè' % (hs_cd + 4)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Số học sinh xếp loại Chưa đạt chiếm $4\\%%$, bằng $%s \\cdot 4\\%% = %s$ (học sinh).' % (tong_hs, hs_cd))
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
