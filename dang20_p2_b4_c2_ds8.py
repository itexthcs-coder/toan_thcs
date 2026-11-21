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


def bt_dang20_p2_b4_c2_ds8(self):
    m = random.choice([12, 15, 18])
    k = random.choice([4, 5, 6])
    n = m + k
    hieu_dt = k * n
    x_val = random.choice([200, 250, 300])
    t1_val = x_val * (x_val + m)
    t2_val = (x_val - k) * (x_val + n)
    tong_dt_str = "{:,}".format(t1_val + t2_val).replace(",", ".")
    tong_dt_sai_str = "{:,}".format(t1_val + t2_val + hieu_dt).replace(",", ".")
    
    noidungcauhoi = ('''Trong một đợt khuyến mãi tại siêu thị, giá bán mỗi chiếc áo sơ mi là $x$ (nghìn đồng). Trong buổi sáng, cửa hàng bán được $x$ chiếc áo và buổi chiều bán được thêm $%s$ chiếc áo nữa. Sang ngày hôm sau, cửa hàng giảm giá mỗi chiếc áo đi $%s$ nghìn đồng (tức giá mới là $x - %s$ nghìn đồng) và bán được tổng cộng $x + %s$ chiếc áo.'''
                     % (m, k, k, n))
    
    nb_da_1_d = '\\True Tổng doanh thu ngày thứ nhất là $T_1 = x^2 + %sx$ (nghìn đồng)' % (m)
    nb_da_1_s = 'Tổng doanh thu ngày thứ nhất là $T_1 = 2x + %s$ (nghìn đồng)' % (m)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['''Tổng số áo bán ngày thứ nhất là $x + %s$ chiếc, giá mỗi chiếc là $x$ nghìn đồng nên $T_1 = x(x + %s) = x^2 + %sx$ (nghìn đồng).''' % (m, m, m)]
    
    th_da_1_d = '\\True Tổng doanh thu ngày thứ hai là $T_2 = (x - %s)(x + %s)$ (nghìn đồng)' % (k, n)
    th_da_1_s = 'Tổng doanh thu ngày thứ hai là $T_2 = (x + %s)(x + %s)$ (nghìn đồng)' % (k, n)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['''Ngày thứ hai bán $x + %s$ chiếc với giá $x - %s$ nghìn đồng mỗi chiếc nên $T_2 = (x - %s)(x + %s)$ (nghìn đồng).''' % (n, k, k, n)]
    
    vd_da_1_d = '\\True Hiệu doanh thu giữa ngày thứ nhất và ngày thứ hai là $T_1 - T_2 = %s$ (nghìn đồng) với mọi giá bán $x$' % (hieu_dt)
    vd_da_1_s = 'Hiệu doanh thu giữa ngày thứ nhất và ngày thứ hai phụ thuộc vào giá bán $x$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['''Ta có $T_1 - T_2 = (x^2 + %sx) - (x^2 + %sx - %s) = %s$ (nghìn đồng) không phụ thuộc vào $x$.''' % (m, m, hieu_dt, hieu_dt)]
    
    vdc_da_1_d = '\\True Nếu giá bán ban đầu của mỗi chiếc áo là $x = %s$ nghìn đồng thì tổng doanh thu cả hai ngày là $%s$ nghìn đồng' % (x_val, tong_dt_str)
    vdc_da_1_s = 'Nếu giá bán ban đầu của mỗi chiếc áo là $x = %s$ nghìn đồng thì tổng doanh thu cả hai ngày là $%s$ nghìn đồng' % (x_val, tong_dt_sai_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['''Với $x = %s$: $T_1 = %s \\cdot (%s + %s) = %s$; $T_2 = %s \\cdot %s = %s$. Tổng doanh thu là $T_1 + T_2 = %s$ (nghìn đồng).'''
                  % (x_val, x_val, x_val, m, "{:,}".format(t1_val).replace(",", "."), x_val - k, x_val + n, "{:,}".format(t2_val).replace(",", "."), tong_dt_str)]

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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
