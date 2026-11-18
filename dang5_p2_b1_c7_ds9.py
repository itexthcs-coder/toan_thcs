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


def bt_dang5_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f0 = random.randint(6, 8)
        f1 = random.randint(16, 20)
        f2 = random.randint(8, 10)
        f3 = random.randint(3, 5)
        tong = f0 + f1 + f2 + f3
        tu_2 = f2 + f3
        y0 = round(f0 * 0.2, 2)
        y1 = round(f1 * 0.2, 2)
        y2 = round(f2 * 0.2, 2)
        y3 = round(f3 * 0.2, 2)
        noidungcauhoi = ('''Biểu đồ tần số dạng đoạn thẳng (đa giác tần số) dưới đây thống kê số anh, chị, em ruột của các bạn học sinh lớp $9C$:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (5.2,0) node[below] {Số anh, chị, em ruột};
\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Số học sinh};
\\foreach \\y/\\lbl in {1/5, 2/10, 3/15, 4/20}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (4.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\coordinate (A) at (1,%s);
\\coordinate (B) at (2,%s);
\\coordinate (C) at (3,%s);
\\coordinate (D) at (4,%s);
\\draw[line width=1pt] (A) -- (B) -- (C) -- (D);
\\fill (A) circle (1pt) node[above] {$%s$};
\\fill (B) circle (1pt) node[above] {$%s$};
\\fill (C) circle (1pt) node[above] {$%s$};
\\fill (D) circle (1pt) node[above] {$%s$};
\\node[below] at (1,0) {$0$};
\\node[below] at (2,0) {$1$};
\\node[below] at (3,0) {$2$};
\\node[below] at (4,0) {$3$};
\\end{tikzpicture}
\\end{center}''' % (y0, y1, y2, y3, f0, f1, f2, f3))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Có $%s$ học sinh trong lớp là con một (có $0$ anh, chị, em ruột)' % f0)
        nb_da_1_s = ('Có $%s$ học sinh trong lớp là con một (có $0$ anh, chị, em ruột)' % f1)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Số học sinh có $1$ anh, chị, em ruột chiếm tỉ lệ cao nhất trong lớp')
        th_da_1_s = ('Số học sinh có $2$ anh, chị, em ruột chiếm tỉ lệ cao nhất trong lớp')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Cỡ mẫu của thống kê này là $%s$ học sinh' % tong)
        vd_da_1_s = ('Cỡ mẫu của thống kê này là $%s$ học sinh' % (tong - 2))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Số học sinh có từ $2$ anh, chị, em ruột trở lên là $%s$ học sinh' % tu_2)
        vdc_da_1_s = ('Số học sinh có từ $2$ anh, chị, em ruột trở lên là $%s$ học sinh' % f2)
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
        
        loigiai_nb_1 = ('Đúng. Tại giá trị $0$ trên trục ngang, tần số tương ứng là $%s$ học sinh.' % f0) if '\\True' in nb_da_1 else ('Sai. Giá trị $0$ anh, chị, em ruột có tần số bằng $%s$, nên có $%s$ học sinh là con một.' % (f0, f0))
        loigiai_th_1 = ('Đúng. Giá trị $1$ có tần số bằng $%s$ là giá trị lớn nhất trong mẫu dữ liệu.' % f1) if '\\True' in th_da_1 else ('Sai. Giá trị $1$ anh, chị, em ruột có tần số cao nhất ($%s$ học sinh).' % f1)
        loigiai_vd_1 = ('Đúng. Cỡ mẫu bằng tổng các tần số: $%s + %s + %s + %s = %s$ (học sinh).' % (f0, f1, f2, f3, tong)) if '\\True' in vd_da_1 else ('Sai. Cỡ mẫu của thống kê này là $%s + %s + %s + %s = %s$ (học sinh).' % (f0, f1, f2, f3, tong))
        loigiai_vdc_1 = ('Đúng. Số học sinh có $2$ hoặc $3$ anh, chị, em ruột là $%s + %s = %s$ (học sinh).' % (f2, f3, tu_2)) if '\\True' in vdc_da_1 else ('Sai. Cần cộng tần số của cả giá trị $2$ và $3$: $%s + %s = %s$ (học sinh).' % (f2, f3, tu_2))
        
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
