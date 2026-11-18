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


def bt_dang9_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f1 = random.randint(26, 32)
        f2 = random.randint(14, 18)
        f3 = random.randint(10, 13)
        f4 = random.randint(6, 9)
        tong_34 = f3 + f4
        y1 = round(f1 * 0.1, 2)
        y2 = round(f2 * 0.1, 2)
        y3 = round(f3 * 0.1, 2)
        y4 = round(f4 * 0.1, 2)
        noidungcauhoi = ('''Trong $30$ phút, trạm kiểm soát ghi nhận lưu lượng các loại xe đi qua và biểu diễn bởi biểu đồ tần số dạng cột dưới đây:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Loại xe};
\\draw[line width=1pt, ->] (0,0) -- (0,3.8) node[left] {Số lượng (xe)};
\\foreach \\y/\\lbl in {1/10, 2/20, 3/30}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\draw[line width=1pt] (0.7,0) rectangle (1.3,%s);
\\node[above] at (1,%s) {$%s$};
\\node[below] at (1,0) {$4$ chỗ};
\\draw[line width=1pt] (2.0,0) rectangle (2.6,%s);
\\node[above] at (2.3,%s) {$%s$};
\\node[below] at (2.3,0) {$7$ chỗ};
\\draw[line width=1pt] (3.3,0) rectangle (3.9,%s);
\\node[above] at (3.6,%s) {$%s$};
\\node[below] at (3.6,0) {Xe tải};
\\draw[line width=1pt] (4.6,0) rectangle (5.2,%s);
\\node[above] at (4.9,%s) {$%s$};
\\node[below] at (4.9,0) {Xe khách};
\\end{tikzpicture}
\\end{center}''' % (y1, y1, f1, y2, y2, f2, y3, y3, f3, y4, y4, f4))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Tần số của loại xe $7$ chỗ là $%s$' % f2)
        nb_da_1_s = ('Tần số của loại xe $7$ chỗ là $%s$' % f3)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Loại xe qua trạm nhiều nhất là xe $4$ chỗ')
        th_da_1_s = ('Loại xe qua trạm nhiều nhất là xe $7$ chỗ')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Nếu vẽ biểu đồ tần số dạng đoạn thẳng, điểm biểu diễn xe khách có tung độ bằng $%s$' % f4)
        vd_da_1_s = ('Nếu vẽ biểu đồ tần số dạng đoạn thẳng, điểm biểu diễn xe khách có tung độ bằng $%s$' % f3)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Số lượng xe $4$ chỗ nhiều hơn tổng số xe tải và xe khách cộng lại')
        vdc_da_1_s = ('Số lượng xe $4$ chỗ ít hơn tổng số xe tải và xe khách cộng lại')
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
        
        loigiai_nb_1 = ('Đúng. Quan sát cột xe $7$ chỗ trên biểu đồ ta thấy tần số là $%s$.' % f2) if '\\True' in nb_da_1 else ('Sai. Cột xe $7$ chỗ có chiều cao ứng với tần số $%s$.' % f2)
        loigiai_th_1 = ('Đúng. Xe $4$ chỗ có tần số lớn nhất ($%s$ xe) nên đi qua trạm nhiều nhất.' % f1) if '\\True' in th_da_1 else ('Sai. Xe $4$ chỗ có tần số $%s$ lớn hơn xe $7$ chỗ ($%s$).' % (f1, f2))
        loigiai_vd_1 = ('Đúng. Tung độ của điểm biểu diễn trên biểu đồ tần số đoạn thẳng chính là tần số của loại xe đó (bằng $%s$).' % f4) if '\\True' in vd_da_1 else ('Sai. Tần số của xe khách là $%s$ nên điểm biểu diễn có tung độ bằng $%s$.' % (f4, f4))
        loigiai_vdc_1 = ('Đúng. Tổng số xe tải và xe khách là $%s + %s = %s$ (xe), ít hơn số xe $4$ chỗ ($%s$ xe).' % (f3, f4, tong_34, f1)) if '\\True' in vdc_da_1 else ('Sai. Số xe $4$ chỗ là $%s$, lớn hơn tổng số xe tải và xe khách ($%s + %s = %s$).' % (f1, f3, f4, tong_34))
        
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
