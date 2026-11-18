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


def bt_dang4_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f6 = random.randint(2, 4)
        f7 = random.randint(6, 8)
        f10 = random.randint(3, 5)
        f8 = 3 * f10
        f9 = random.randint(8, 11)
        tong = f6 + f7 + f8 + f9 + f10
        tu_9 = f9 + f10
        y6 = round(f6 * 0.25, 2)
        y7 = round(f7 * 0.25, 2)
        y8 = round(f8 * 0.25, 2)
        y9 = round(f9 * 0.25, 2)
        y10 = round(f10 * 0.25, 2)
        noidungcauhoi = ('''Cho biểu đồ tần số dạng cột biểu diễn điểm kiểm tra $15$ phút môn Toán của lớp $9B$:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Điểm};
\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Tần số};
\\foreach \\y/\\lbl in {0.5/2, 1/4, 1.5/6, 2/8, 2.5/10, 3/12, 3.5/14, 4/16}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\draw[line width=1pt] (0.7,0) rectangle (1.3,%s);
\\node[above] at (1,%s) {$%s$};
\\node[below] at (1,0) {$6$};
\\draw[line width=1pt] (1.7,0) rectangle (2.3,%s);
\\node[above] at (2,%s) {$%s$};
\\node[below] at (2,0) {$7$};
\\draw[line width=1pt] (2.7,0) rectangle (3.3,%s);
\\node[above] at (3,%s) {$%s$};
\\node[below] at (3,0) {$8$};
\\draw[line width=1pt] (3.7,0) rectangle (4.3,%s);
\\node[above] at (4,%s) {$%s$};
\\node[below] at (4,0) {$9$};
\\draw[line width=1pt] (4.7,0) rectangle (5.3,%s);
\\node[above] at (5,%s) {$%s$};
\\node[below] at (5,0) {$10$};
\\end{tikzpicture}
\\end{center}''' % (y6, y6, f6, y7, y7, f7, y8, y8, f8, y9, y9, f9, y10, y10, f10))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Trục đứng của biểu đồ trên biểu diễn tần số (số học sinh)')
        nb_da_1_s = ('Trục đứng của biểu đồ trên biểu diễn điểm số của học sinh')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Lớp $9B$ có $%s$ học sinh tham gia bài kiểm tra' % tong)
        th_da_1_s = ('Lớp $9B$ có $%s$ học sinh tham gia bài kiểm tra' % (tong + 2))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Số học sinh đạt điểm $8$ nhiều gấp $3$ lần số học sinh đạt điểm $10$')
        vd_da_1_s = ('Số học sinh đạt điểm $8$ nhiều gấp $2$ lần số học sinh đạt điểm $10$')
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Có $%s$ học sinh đạt điểm từ $9$ trở lên' % tu_9)
        vdc_da_1_s = ('Có $%s$ học sinh đạt điểm từ $9$ trở lên' % f9)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        
        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)
        
        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            true_count = count_true_answers(answers)
            if 1 <= true_count <= 3:
                break
        
        loigiai_nb_1 = ('Đúng. Trên biểu đồ tần số dạng cột, trục đứng biểu diễn tần số và trục ngang biểu diễn điểm số.') if '\\True' in nb_da_1 else ('Sai. Trục ngang mới biểu diễn điểm số, còn trục đứng biểu diễn tần số.')
        loigiai_th_1 = ('Đúng. Tổng số học sinh là $%s + %s + %s + %s + %s = %s$ (học sinh).' % (f6, f7, f8, f9, f10, tong)) if '\\True' in th_da_1 else ('Sai. Tổng số học sinh tham gia kiểm tra là $%s + %s + %s + %s + %s = %s$ (học sinh).' % (f6, f7, f8, f9, f10, tong))
        loigiai_vd_1 = ('Đúng. Số học sinh đạt điểm $8$ là $%s$, số học sinh đạt điểm $10$ là $%s$, mà $%s : %s = 3$.' % (f8, f10, f8, f10)) if '\\True' in vd_da_1 else ('Sai. Tỉ số giữa số học sinh đạt điểm $8$ và điểm $10$ là $\\dfrac{%s}{%s} = 3$.' % (f8, f10))
        loigiai_vdc_1 = ('Đúng. Số học sinh đạt điểm từ $9$ trở lên gồm điểm $9$ ($%s$) và điểm $10$ ($%s$), tổng là $%s + %s = %s$.' % (f9, f10, f9, f10, tu_9)) if '\\True' in vdc_da_1 else ('Sai. Học sinh đạt từ $9$ điểm trở lên gồm cả điểm $9$ và điểm $10$, có $%s + %s = %s$ học sinh.' % (f9, f10, tu_9))
        
        list_nb_1 = [nb_da_1]
        list_nb_2 = [loigiai_nb_1]
        combined_nb = list(zip(list_nb_1, list_nb_2))
        random.shuffle(combined_nb)
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        list_th_1 = [th_da_1]
        list_th_2 = [loigiai_th_1]
        combined_th = list(zip(list_th_1, list_th_2))
        random.shuffle(combined_th)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        list_vd_1 = [vd_da_1]
        list_vd_2 = [loigiai_vd_1]
        combined_vd = list(zip(list_vd_1, list_vd_2))
        random.shuffle(combined_vd)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        list_vdc_1 = [vdc_da_1]
        list_vdc_2 = [loigiai_vdc_1]
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))
        random.shuffle(combined_vdc)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
        
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
