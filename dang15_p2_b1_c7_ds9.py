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


def bt_dang15_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f4, f5, f7 = 3, 6, 8
        hieu = random.choice([3, 5, 7])
        tong_xy = 30 - (f4 + f5 + f7)
        x_val = (tong_xy + hieu) // 2
        y_val = tong_xy - x_val
        tu_7 = f7 + y_val
        pct_7 = round(tu_7 * 100 / 30)
        y_m1 = round(f4 * 0.3, 2)
        y_m2 = round(f5 * 0.3, 2)
        y_m3 = round(x_val * 0.3, 2)
        y_m4 = round(f7 * 0.3, 2)
        y_m5 = round(y_val * 0.3, 2)
        noidungcauhoi = ('''Một trạm quan trắc ghi lại số giờ nắng mỗi ngày tại một địa phương trong tháng $4$ ($30$ ngày) và biểu diễn bằng đa giác tần số như hình dưới đây. Biết số ngày có $6$ giờ nắng nhiều hơn số ngày có $8$ giờ nắng là $%s$ ngày:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Số giờ nắng};
\\draw[line width=1pt, ->] (0,0) -- (0,3.6) node[left] {Số ngày};
\\foreach \\y/\\lbl in {1.5/5, 3.0/10}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\coordinate (M1) at (1,%s);
\\coordinate (M2) at (2,%s);
\\coordinate (M3) at (3,%s);
\\coordinate (M4) at (4,%s);
\\coordinate (M5) at (5,%s);
\\draw[line width=1pt] (M1) -- (M2) -- (M3) -- (M4) -- (M5);
\\fill (M1) circle (1pt) node[above] {$3$};
\\fill (M2) circle (1pt) node[above] {$6$};
\\fill (M3) circle (1pt) node[above] {$x$};
\\fill (M4) circle (1pt) node[above] {$8$};
\\fill (M5) circle (1pt) node[above] {$y$};
\\node[below] at (1,0) {$4$};
\\node[below] at (2,0) {$5$};
\\node[below] at (3,0) {$6$};
\\node[below] at (4,0) {$7$};
\\node[below] at (5,0) {$8$};
\\end{tikzpicture}
\\end{center}''' % (hieu, y_m1, y_m2, y_m3, y_m4, y_m5))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Tổng tần số của hai giá trị $6$ giờ nắng và $8$ giờ nắng là $13$')
        nb_da_1_s = ('Tổng tần số của hai giá trị $6$ giờ nắng và $8$ giờ nắng là $17$')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Số ngày có $6$ giờ nắng là $%s$ ngày' % x_val)
        th_da_1_s = ('Số ngày có $6$ giờ nắng là $%s$ ngày' % (x_val + 1))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Điểm $M_5$ trên đa giác tần số có tọa độ là $(8; %s)$' % y_val)
        vd_da_1_s = ('Điểm $M_5$ trên đa giác tần số có tọa độ là $(%s; 8)$' % y_val)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Số ngày có từ $7$ giờ nắng trở lên chiếm $%s\\%%$ số ngày trong tháng $4$' % pct_7)
        vdc_da_1_s = ('Số ngày có từ $7$ giờ nắng trở lên chiếm $%s\\%%$ số ngày trong tháng $4$' % (pct_7 + 10))
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
        
        loigiai_nb_1 = ('Đúng. Tháng $4$ có $30$ ngày nên $3 + 6 + x + 8 + y = 30 \\Leftrightarrow x + y = 13$.') if '\\True' in nb_da_1 else ('Sai. Vì tổng số ngày trong tháng $4$ là $30$ nên $x + y = 30 - (3 + 6 + 8) = 13$.')
        loigiai_th_1 = ('Đúng. Ta có $x + y = 13$ và $x - y = %s$, suy ra $x = \\dfrac{13 + %s}{2} = %s$ (ngày).' % (hieu, hieu, x_val)) if '\\True' in th_da_1 else ('Sai. Giải hệ $\\begin{cases} x + y = 13 \\\\ x - y = %s \\end{cases}$ ta tìm được $x = %s$ và $y = %s$.' % (hieu, x_val, y_val))
        loigiai_vd_1 = ('Đúng. Giá trị $8$ giờ nắng có tần số $y = %s$ nên điểm $M_5$ có tọa độ $(8; %s)$.' % (y_val, y_val)) if '\\True' in vd_da_1 else ('Sai. Hoành độ là số giờ nắng ($8$) và tung độ là tần số ($y = %s$), nên tọa độ là $(8; %s)$.' % (y_val, y_val))
        loigiai_vdc_1 = ('Đúng. Số ngày có từ $7$ giờ nắng trở lên là $8 + %s = %s$ (ngày), chiếm $\\dfrac{%s}{30} \\cdot 100\\%% = %s\\%%$.' % (y_val, tu_7, tu_7, pct_7)) if '\\True' in vdc_da_1 else ('Sai. Số ngày có $7$ hoặc $8$ giờ nắng là $8 + %s = %s$ ngày, chiếm $\\dfrac{%s}{30} \\cdot 100\\%% = %s\\%%$.' % (y_val, tu_7, tu_7, pct_7))
        
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
