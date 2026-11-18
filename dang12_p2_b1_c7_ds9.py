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


def bt_dang12_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        a_val = random.choice([2, 3, 4])
        b_val = 8 - a_val
        tong_diem = 6*2 + 7*a_val + 8*7 + 9*b_val + 10*3
        rhs = tong_diem - (12 + 56 + 30)
        tb_str = str(tong_diem / 20).replace('.', ',')
        so_gioi = 7 + b_val + 3
        pct_gioi = so_gioi * 5
        noidungcauhoi = ('''Điểm kiểm tra môn Tiếng Anh của một nhóm $20$ học sinh được cho trong bảng tần số sau (với $a, b \\in \\mathbb{N}^*$):
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
Điểm số & $6$ & $7$ & $8$ & $9$ & $10$ \\\\
\\hline
Tần số & $2$ & $a$ & $7$ & $b$ & $3$ \\\\
\\hline
\\end{tabular}
\\end{center}
Biết rằng điểm trung bình của cả nhóm là $%s$.''' % tb_str)
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Phương trình biểu diễn tổng số học sinh của nhóm là $a + b = 8$')
        nb_da_1_s = ('Phương trình biểu diễn tổng số học sinh của nhóm là $a + b = 12$')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Phương trình biểu diễn tổng số điểm của cả nhóm là $7a + 9b = %s$' % rhs)
        th_da_1_s = ('Phương trình biểu diễn tổng số điểm của cả nhóm là $7a + 9b = %s$' % (rhs + 4))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Tần số của điểm $7$ là $%s$' % a_val)
        vd_da_1_s = ('Tần số của điểm $7$ là $%s$' % (a_val + 1))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Số học sinh đạt điểm giỏi (từ $8$ trở lên) chiếm $%s\\%%$ tổng số học sinh của nhóm' % pct_gioi)
        vdc_da_1_s = ('Số học sinh đạt điểm giỏi (từ $8$ trở lên) chiếm $%s\\%%$ tổng số học sinh của nhóm' % (pct_gioi - 10))
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
        
        loigiai_nb_1 = ('Đúng. Vì nhóm có $20$ học sinh nên $2 + a + 7 + b + 3 = 20 \\Leftrightarrow a + b = 8$.') if '\\True' in nb_da_1 else ('Sai. Từ tổng tần số bằng $20$, ta có $2 + a + 7 + b + 3 = 20 \\Leftrightarrow a + b = 8$.')
        loigiai_th_1 = ('Đúng. Tổng số điểm là $20 \\cdot %s = %s$. Ta có $6 \\cdot 2 + 7a + 8 \\cdot 7 + 9b + 10 \\cdot 3 = %s \\Leftrightarrow 7a + 9b = %s$.' % (tb_str, tong_diem, tong_diem, rhs)) if '\\True' in th_da_1 else ('Sai. Tổng điểm cả nhóm bằng $20 \\cdot %s = %s$, suy ra $7a + 9b = %s - 98 = %s$.' % (tb_str, tong_diem, tong_diem, rhs))
        loigiai_vd_1 = ('Đúng. Giải hệ $\\begin{cases} a + b = 8 \\\\ 7a + 9b = %s \\end{cases}$ ta được $a = %s$ và $b = %s$. Vậy tần số của điểm $7$ là $%s$.' % (rhs, a_val, b_val, a_val)) if '\\True' in vd_da_1 else ('Sai. Giải hệ phương trình từ cỡ mẫu và tổng điểm ta tìm được $a = %s$ và $b = %s$.' % (a_val, b_val))
        loigiai_vdc_1 = ('Đúng. Số học sinh đạt từ $8$ điểm trở lên là $7 + %s + 3 = %s$, chiếm $\\dfrac{%s}{20} \\cdot 100\\%% = %s\\%%$.' % (b_val, so_gioi, so_gioi, pct_gioi)) if '\\True' in vdc_da_1 else ('Sai. Có $7 + %s + 3 = %s$ học sinh đạt điểm từ $8$ trở lên, chiếm $\\dfrac{%s}{20} \\cdot 100\\%% = %s\\%%$.' % (b_val, so_gioi, so_gioi, pct_gioi))
        
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
