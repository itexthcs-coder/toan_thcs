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


def bt_dang11_p2_b3_c2_ds9(self):
    gia_thuoc = random.choice([18, 24, 30])
    gia_vo = random.choice([7, 8, 9, 11])
    so_vo_max = random.randint(10, 15)
    du = random.randint(0, gia_vo - 1)
    tong_tien = gia_thuoc + gia_vo * so_vo_max + du

    noidungcauhoi = ('''Bạn Lan mang theo $%s$ nghìn đồng vào nhà sách. Lan mua một bộ thước kẻ giá $%s$ nghìn đồng và một số quyển tập, mỗi quyển tập có giá $%s$ nghìn đồng. Gọi $x$ ($x \\in \\mathbb{N}^*$) là số quyển tập Lan có thể mua. Xét tính đúng sai của các khẳng định sau:''' % (latex(tong_tien), latex(gia_thuoc), latex(gia_vo)))

    nb_da_1_d = '\\True Tổng số tiền Lan phải trả cho $1$ bộ thước và $x$ quyển tập là $%sx + %s$ (nghìn đồng)' % (latex(gia_vo), latex(gia_thuoc))
    nb_da_1_s = 'Tổng số tiền Lan phải trả cho $1$ bộ thước và $x$ quyển tập là $%sx + %s$ (nghìn đồng)' % (latex(gia_thuoc), latex(gia_vo))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Giá tiền $x$ quyển tập là $%sx$ nghìn đồng, cộng với bộ thước $%s$ nghìn đồng nên tổng số tiền là $%sx + %s$ (nghìn đồng).''' % (latex(gia_vo), latex(gia_thuoc), latex(gia_vo), latex(gia_thuoc)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Bất phương trình biểu diễn điều kiện số tiền mua hàng không vượt quá số tiền Lan có là $%sx + %s \\le %s$' % (latex(gia_vo), latex(gia_thuoc), latex(tong_tien))
    th_da_1_s = 'Bất phương trình biểu diễn điều kiện số tiền mua hàng không vượt quá số tiền Lan có là $%sx + %s < %s$' % (latex(gia_vo), latex(gia_thuoc), latex(tong_tien))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì số tiền mua hàng không vượt quá $%s$ nghìn đồng nên ta có bất phương trình $%sx + %s \\le %s$.''' % (latex(tong_tien), latex(gia_vo), latex(gia_thuoc), latex(tong_tien)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Lan có thể mua được nhiều nhất $%s$ quyển tập' % (latex(so_vo_max))
    vd_da_1_s = 'Lan có thể mua được nhiều nhất $%s$ quyển tập' % (latex(so_vo_max + 1))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $%sx + %s \\le %s \\Leftrightarrow %sx \\le %s \\Leftrightarrow x \\le \\dfrac{%s}{%s}$. Vì $x \\in \\mathbb{N}^*$ nên Lan mua được nhiều nhất $%s$ quyển tập.''' % (latex(gia_vo), latex(gia_thuoc), latex(tong_tien), latex(gia_vo), latex(tong_tien - gia_thuoc), latex(tong_tien - gia_thuoc), latex(gia_vo), latex(so_vo_max)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu Lan mua tối đa số quyển tập có thể thì bạn còn thừa lại $%s$ nghìn đồng' % (latex(du))
    vdc_da_1_s = 'Nếu Lan mua tối đa số quyển tập có thể thì bạn còn thừa lại $%s$ nghìn đồng' % (latex(du + 1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Số tiền Lan còn thừa khi mua $%s$ quyển tập là $%s - (%s \\cdot %s + %s) = %s$ (nghìn đồng).''' % (latex(so_vo_max), latex(tong_tien), latex(gia_vo), latex(so_vo_max), latex(gia_thuoc), latex(du)))
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

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
