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


def bt_dang18_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f1 = random.choice([12, 14, 16])
        f2 = random.choice([8, 10, 12])
        tong_03 = 40 - f1 - f2
        f3 = tong_03 // 4
        f0 = 3 * f3
        pct_0 = f0 * 100 // 40
        y1 = round(f1 * 0.2, 2)
        y2 = round(f2 * 0.2, 2)
        noidungcauhoi = ('''Một biểu đồ tần số dạng cột biểu diễn số lỗi kỹ thuật của $40$ máy tính trong phòng thực hành gồm các mức: $0$ lỗi, $1$ lỗi, $2$ lỗi, $3$ lỗi. Do bị che khuất hai cột ngoài cùng, người ta chỉ đọc được tần số cột $1$ lỗi là $%s$, cột $2$ lỗi là $%s$, đồng thời biết cột $0$ lỗi cao gấp $3$ lần cột $3$ lỗi:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (5.5,0) node[below] {Số lỗi};
\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Số máy};
\\foreach \\y/\\lbl in {1/5, 2/10, 3/15}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.0,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\draw[line width=1pt, dashed] (0.7,0) rectangle (1.3,2.4);
\\node at (1,1.2) {$?$};
\\node[below] at (1,0) {$0$};
\\draw[line width=1pt] (1.9,0) rectangle (2.5,%s);
\\node[above] at (2.2,%s) {$%s$};
\\node[below] at (2.2,0) {$1$};
\\draw[line width=1pt] (3.1,0) rectangle (3.7,%s);
\\node[above] at (3.4,%s) {$%s$};
\\node[below] at (3.4,0) {$2$};
\\draw[line width=1pt, dashed] (4.3,0) rectangle (4.9,0.8);
\\node at (4.6,0.4) {$?$};
\\node[below] at (4.6,0) {$3$};
\\end{tikzpicture}
\\end{center}''' % (f1, f2, y1, y1, f1, y2, y2, f2))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Tổng tần số của hai cột $0$ lỗi và $3$ lỗi là $%s$' % tong_03)
        nb_da_1_s = ('Tổng tần số của hai cột $0$ lỗi và $3$ lỗi là $%s$' % (tong_03 + 4))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Số máy tính có $3$ lỗi kỹ thuật là $%s$ máy' % f3)
        th_da_1_s = ('Số máy tính có $3$ lỗi kỹ thuật là $%s$ máy' % (f3 + 1))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Số máy tính không mắc lỗi nào ($0$ lỗi) là $%s$ máy' % f0)
        vd_da_1_s = ('Số máy tính không mắc lỗi nào ($0$ lỗi) là $%s$ máy' % (f0 - 3))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Tỉ lệ máy tính không mắc lỗi chiếm $%s\\%%$ tổng số máy trong phòng' % pct_0)
        vdc_da_1_s = ('Tỉ lệ máy tính không mắc lỗi chiếm $%s\\%%$ tổng số máy trong phòng' % (pct_0 + 5))
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
        
        loigiai_nb_1 = ('Đúng. Vì có $40$ máy tính nên tổng tần số hai cột còn lại là $40 - (%s + %s) = %s$.' % (f1, f2, tong_03)) if '\\True' in nb_da_1 else ('Sai. Tổng tần số của hai cột bị che khuất là $40 - %s - %s = %s$.' % (f1, f2, tong_03))
        loigiai_th_1 = ('Đúng. Gọi số máy có $3$ lỗi là $x$ thì số máy có $0$ lỗi là $3x$. Ta có $3x + x = %s \\Leftrightarrow 4x = %s \\Leftrightarrow x = %s$.' % (tong_03, tong_03, f3)) if '\\True' in th_da_1 else ('Sai. Từ $3x + x = %s$, ta tìm được số máy có $3$ lỗi là $x = %s$ máy.' % (tong_03, f3))
        loigiai_vd_1 = ('Đúng. Số máy tính có $0$ lỗi là $3 \\cdot %s = %s$ (máy).' % (f3, f0)) if '\\True' in vd_da_1 else ('Sai. Cột $0$ lỗi cao gấp $3$ lần cột $3$ lỗi nên có $3 \\cdot %s = %s$ (máy).' % (f3, f0))
        loigiai_vdc_1 = ('Đúng. Tỉ lệ máy tính có $0$ lỗi là $\\dfrac{%s}{40} \\cdot 100\\%% = %s\\%%$.' % (f0, pct_0)) if '\\True' in vdc_da_1 else ('Sai. Có $%s$ trên $40$ máy không mắc lỗi, chiếm $\\dfrac{%s}{40} \\cdot 100\\%% = %s\\%%$.' % (f0, f0, pct_0))
        
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
