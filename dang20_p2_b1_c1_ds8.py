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


def bt_dang20_p2_b1_c1_ds8(self):
    # Dạng 20: Ứng dụng trừ đơn thức đồng dạng trong bài toán diện tích và chi phí lát gạch sân vườn
    a1 = randint(4, 6)
    b1 = randint(3, 5)
    a2 = randint(2, 3)
    s_san = a1 * b1
    s_hoa = a2
    s_gach = s_san - s_hoa
    don_gia = random.choice([100, 120, 150])
    hs_chi_phi = don_gia * s_gach

    noidungcauhoi = ('Một khoảng sân hình chữ nhật có chiều dài $%sx\\text{ (m)}$ và chiều rộng $%sy\\text{ (m)}$. Ở chính giữa sân người ta xây một bồn hoa hình chữ nhật có chiều dài $%sx\\text{ (m)}$ và chiều rộng $y\\text{ (m)}$, phần diện tích sân còn lại dùng để lát gạch ($x, y > 0$).'
                     % (a1, b1, a2))

    nb_da_1_d = '\\True Diện tích toàn bộ khoảng sân là $%sxy\\text{ (m}^{2})$.' % s_san
    nb_da_1_s = 'Diện tích toàn bộ khoảng sân là $%sxy\\text{ (m}^{2})$.' % (a1 + b1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Diện tích toàn bộ khoảng sân hình chữ nhật là: $S_{\\text{sân}} = %sx \\cdot %sy = %sxy\\text{ (m}^{2})$.'
                    % (a1, b1, s_san))

    th_da_1_d = '\\True Diện tích của bồn hoa là $%sxy\\text{ (m}^{2})$.' % s_hoa
    th_da_1_s = 'Diện tích của bồn hoa là $%s(x + y)\\text{ (m}^{2})$.' % s_hoa
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Diện tích của bồn hoa là: $S_{\\text{hoa}} = %sx \\cdot y = %sxy\\text{ (m}^{2})$.'
                    % (a2, s_hoa))

    vd_da_1_d = '\\True Diện tích phần sân dùng để lát gạch được biểu thị bởi đơn thức thu gọn $%sxy\\text{ (m}^{2})$.' % s_gach
    vd_da_1_s = 'Diện tích phần sân dùng để lát gạch được biểu thị bởi đơn thức thu gọn $%sxy\\text{ (m}^{2})$.' % (s_san + s_hoa)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Diện tích phần sân lát gạch là: $S_{\\text{gạch}} = S_{\\text{sân}} - S_{\\text{hoa}} = %sxy - %sxy = %sxy\\text{ (m}^{2})$.'
                    % (s_san, s_hoa, s_gach))

    vdc_da_1_d = '\\True Biết chi phí lát gạch là $%s$ nghìn đồng/$\\text{m}^{2}$, biểu thức biểu thị tổng chi phí lát gạch (tính theo nghìn đồng) là một đơn thức có hệ số bằng $%s$.' % (don_gia, hs_chi_phi)
    vdc_da_1_s = 'Biết chi phí lát gạch là $%s$ nghìn đồng/$\\text{m}^{2}$, biểu thức biểu thị tổng chi phí lát gạch (tính theo nghìn đồng) là một đơn thức có hệ số bằng $%s$.' % (don_gia, don_gia * s_san)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tổng chi phí lát gạch là: $%s \\cdot %sxy = %sxy$ (nghìn đồng), đây là đơn thức có hệ số bằng $%s$.'
                     % (don_gia, s_gach, hs_chi_phi, hs_chi_phi))

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

    combined = list(zip([nb_da_1, th_da_1, vd_da_1, vdc_da_1],
                        [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers[0]) + '}\n'
               '{' + str(shuffled_answers[1]) + '}\n'
               '{' + str(shuffled_answers[2]) + '}\n'
               '{' + str(shuffled_answers[3]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions[0]) + '\n'
               '\\item ' + str(shuffled_solutions[1]) + '\n'
               '\\item ' + str(shuffled_solutions[2]) + '\n'
               '\\item ' + str(shuffled_solutions[3]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
