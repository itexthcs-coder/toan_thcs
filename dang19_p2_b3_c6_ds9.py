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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang19_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cap_x = 16
        cap_y = 24
        n_8 = random.choice([17, 19, 23])
        N_students = n_8 * 8
        ways = []
        for xv in range(1, n_8 // 2 + 1):
            rem = n_8 - 2 * xv
            if rem > 0 and rem % 3 == 0:
                ways.append((xv, rem // 3))
        ways_str = ', '.join(['(%s; %s)' % (w[0], w[1]) for w in ways])
        min_xe_sol = min(ways, key=lambda item: item[0] + item[1])
        max_xe_sol = max(ways, key=lambda item: item[0] + item[1])

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một trường THCS tổ chức cho $%s$ học sinh đi tham quan bằng hai loại xe: xe lớn chở $%s$ học sinh và xe nhỏ chở $%s$ học sinh. Gọi $x$ là số xe nhỏ và $y$ là số xe lớn cần thuê sao cho tất cả các xe đều chở vừa đủ số người quy định ($x, y \\in \\mathbb{N}$).'''
                         % (N_students, cap_y, cap_x))

        # Nhận biết
        nb_da_1_d = '\\True Phương trình biểu diễn mối quan hệ giữa $x$ và $y$ sau khi rút gọn là $2x + 3y = %s$' % (n_8)
        nb_da_1_s = 'Phương trình biểu diễn mối quan hệ giữa $x$ và $y$ sau khi rút gọn là $3x + 2y = %s$' % (n_8)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Tổng số học sinh được chở trên các xe là $%sx + %sy = %s$. Chia cả hai vế của phương trình cho $8$, ta được phương trình rút gọn là $2x + 3y = %s$.'''
                        % (cap_x, cap_y, N_students, n_8))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Nếu nhà trường thuê cả hai loại xe ($x \\ge 1, y \\ge 1$) thì có tất cả $%s$ phương án thuê xe' % (len(ways))
        th_da_1_s = 'Nếu nhà trường thuê cả hai loại xe ($x \\ge 1, y \\ge 1$) thì chỉ có duy nhất $1$ phương án thuê xe'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Các nghiệm nguyên dương $(x; y)$ của phương trình $2x + 3y = %s$ là: $%s$, gồm tất cả $%s$ phương án thuê xe.'''
                        % (n_8, ways_str, len(ways)))
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Phương án dùng tổng số xe ít nhất (vẫn có đủ cả hai loại xe) là thuê $%s$ xe nhỏ và $%s$ xe lớn' % (min_xe_sol[0], min_xe_sol[1])
        vd_da_1_s = 'Phương án dùng tổng số xe ít nhất (vẫn có đủ cả hai loại xe) là thuê $%s$ xe nhỏ và $%s$ xe lớn' % (max_xe_sol[0], max_xe_sol[1])
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Để tổng số xe $x + y$ nhỏ nhất, ta cần thuê số xe lớn $y$ nhiều nhất có thể, ứng với cặp nghiệm $(%s; %s)$ (tổng cộng $%s$ xe).'''
                        % (min_xe_sol[0], min_xe_sol[1], min_xe_sol[0] + min_xe_sol[1]))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Nhà trường không thể chỉ thuê duy nhất một loại xe để chở vừa đủ $%s$ học sinh' % (N_students)
        vdc_da_1_s = 'Nếu chỉ thuê toàn xe $24$ chỗ thì nhà trường cần dùng vừa đủ $%s$ xe' % (N_students // 24)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Vì $%s$ là số lẻ (không chia hết cho $2$) và cũng không chia hết cho $3$ nên nếu cho $x = 0$ hoặc $y = 0$ thì phương trình $2x + 3y = %s$ đều không có nghiệm tự nhiên.'''
                         % (n_8, n_8))
        list_vdc_2 = [loigiai_vdc_1]

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
