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


def bt_dang18_p2_b2_c10_hh9(self):
    R_coc = random.choice([4, 5, 6])
    r_bi = random.choice([1, 2])
    so_bi = random.choice([3, 6])
    # V_bi = so_bi * 4/3 * pi * r_bi^3 = pi * R_coc^2 * delta_h => delta_h = (4 * so_bi * r_bi^3) / (3 * R_coc^2)
    # Chọn bộ số đẹp: R_coc = 4, r_bi = 2, so_bi = 6 => delta_h = (4 * 6 * 8) / (3 * 16) = 192 / 48 = 4 cm!
    R_coc = random.choice([4, 8])
    r_bi = 2
    so_bi = 6 if R_coc == 4 else 24
    delta_h = (4 * so_bi * (r_bi**3)) // (3 * (R_coc**2))
    h_bandau = randint(6, 10)
    h_sau = h_bandau + delta_h
    V_tong_bi = Rational(4, 3) * so_bi * (r_bi**3)

    noidungcauhoi = ('''Một chiếc cốc hình trụ có bán kính đáy $R = %s\\text{ cm}$, đang chứa nước ở độ cao $h_0 = %s\\text{ cm}$ (cốc đủ cao để nước không tràn ra ngoài). Người ta thả chìm hoàn toàn $%s$ viên bi sắt đặc hình cầu cùng có bán kính $r = %s\\text{ cm}$ vào cốc.''' % (R_coc, h_bandau, so_bi, r_bi))

    nb_da_1_d = '\\True Thể tích của một viên bi sắt bằng $%s\\pi\\text{ cm}^3$' % latex(Rational(4, 3) * r_bi**3)
    nb_da_1_s = 'Thể tích của một viên bi sắt bằng $%s\\pi\\text{ cm}^3$' % latex(4 * r_bi**3)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Thể tích một viên bi là $V_1 = \\dfrac{4}{3}\\pi r^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (r_bi, latex(Rational(4, 3) * r_bi**3)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Thể tích phần nước dâng lên trong cốc bằng $%s\\pi\\text{ cm}^3$' % latex(V_tong_bi)
    th_da_1_s = 'Thể tích phần nước dâng lên trong cốc bằng $%s\\pi\\text{ cm}^3$' % latex(Rational(4, 3) * r_bi**3)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Thể tích phần nước dâng lên đúng bằng tổng thể tích của $%s$ viên bi: $V_{\\text{dâng}} = %s \\cdot %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (so_bi, so_bi, latex(Rational(4, 3) * r_bi**3), latex(V_tong_bi)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Mực nước trong cốc dâng thêm một đoạn bằng $%s\\text{ cm}$' % (delta_h)
    vd_da_1_s = 'Mực nước trong cốc dâng thêm một đoạn bằng $%s\\text{ cm}$' % (delta_h + 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Độ cao mực nước dâng thêm là $\\Delta h = \\dfrac{V_{\\text{dâng}}}{\\pi R^2} = \\dfrac{%s\\pi}{\\pi \\cdot %s^2} = %s\\text{ (cm)}$.''' % (latex(V_tong_bi), R_coc, delta_h))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Độ cao mực nước trong cốc sau khi thả $%s$ viên bi là $%s\\text{ cm}$' % (so_bi, h_sau)
    vdc_da_1_s = 'Độ cao mực nước trong cốc sau khi thả $%s$ viên bi là $%s\\text{ cm}$' % (so_bi, h_bandau + delta_h + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Độ cao mực nước mới trong cốc là $h = h_0 + \\Delta h = %s + %s = %s\\text{ (cm)}$.''' % (h_bandau, delta_h, h_sau))
    list_vdc_2 = [loigiai_vdc_1]

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
