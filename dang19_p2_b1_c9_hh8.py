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


def fmt_num(val):
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        if val.is_integer():
            return str(int(val))
        s = ('%.4f' % val).rstrip('0').rstrip('.')
        return s.replace('.', ',')
    if isinstance(val, Decimal):
        s = str(val).rstrip('0').rstrip('.') if '.' in str(val) else str(val)
        return s.replace('.', ',')
    if isinstance(val, Fraction):
        if val.denominator == 1:
            return str(val.numerator)
        return '\dfrac{%s}{%s}' % (val.numerator, val.denominator)
    return str(val)

def bt_dang19_p2_b1_c9_hh8(self):
    # Dạng 19 (Thực tế): Máy ảnh lỗ kim tạo hai tam giác đồng dạng đối đỉnh OAB ~ OA'B'
    d_hop_cm = random.choice([12, 15, 20])
    d_nha_m = random.choice([48, 60, 75, 80])
    while (d_nha_m * 100) % d_hop_cm != 0:
        d_nha_m = random.choice([48, 60, 75, 80, 90])

    k = (d_nha_m * 100) // d_hop_cm
    h_anh_cm = random.choice([4, 5, 6, 8])
    h_nha_m = Fraction(h_anh_cm * k, 100)

    d_hop_m = Decimal(d_hop_cm) / Decimal(100)
    h_anh_m = Decimal(h_anh_cm) / Decimal(100)

    tikz = (
        '\\begin{center}'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]'
        '\\coordinate (O) at (3.2,1.6);'
        '\\coordinate (A) at (0,3.2);'
        '\\coordinate (B) at (0,0);'
        '\\coordinate (A1) at (4.8,0.8);'
        '\\coordinate (B1) at (4.8,2.4);'
        '\\draw[line width=1pt] (A)--(B)--(B1)--(A1)--cycle (A)--(B1);'
        '\\fill (O) circle (1pt) node[above] {$O$};'
        '\\fill (A) circle (1pt) node[above left] {$A$};'
        '\\fill (B) circle (1pt) node[below left] {$B$};'
        '\\fill (A1) circle (1pt) node[below right] {$A^{\prime}$};'
        '\\fill (B1) circle (1pt) node[above right] {$B^{\prime}$};'
        '\\end{tikzpicture}'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một mô hình máy ảnh lỗ kim có dạng hộp kín chiều dài (khoảng cách từ lỗ kim $O$ đến màn hứng ảnh $A^{\prime}B^{\prime}$) là $%s\\text{ cm}$. '
        'Người ta đặt mô hình này cách một tòa nhà cao tầng $AB$ một khoảng $%s\\text{ m}$ để chụp ảnh tòa nhà. '
        'Ánh sáng truyền thẳng qua lỗ kim $O$ tạo thành hai tam giác đồng dạng $\\Delta OAB$ và $\\Delta OA^{\prime}B^{\prime}$ '
        '($AB // A^{\prime}B^{\prime}$), ảnh của tòa nhà trên màn hứng có chiều cao $A^{\prime}B^{\prime} = %s\\text{ cm}$.%s'
        % (d_hop_cm, d_nha_m, h_anh_cm, tikz)
    )

    nb_da_1_d = '\\True $\\Delta OAB \\backsim \\Delta OA^{\prime}B^{\prime}$'
    nb_da_1_s = '$\\Delta OAB \\backsim \\Delta OB^{\prime}A^{\prime}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Vì tòa nhà $AB$ và màn hứng ảnh $A^{\prime}B^{\prime}$ song song với nhau ($AB // A^{\prime}B^{\prime}$) và đường thẳng $AB$ cắt phần kéo dài '
        'của hai cạnh $OA^{\prime}, OB^{\prime}$ nên $\\Delta OAB \\backsim \\Delta OA^{\prime}B^{\prime}$.'
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Đổi đơn vị: chiều dài hộp là $%s\\text{ m}$ và chiều cao ảnh là $%s\\text{ m}$' % (fmt_num(d_hop_m), fmt_num(h_anh_m))
    th_da_1_s = 'Đổi đơn vị: chiều dài hộp là $%s\\text{ m}$ và chiều cao ảnh là $%s\\text{ m}$' % (fmt_num(Decimal(d_hop_cm) / 10), fmt_num(h_anh_m))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Đổi sang đơn vị mét: $%s\\text{ cm} = %s\\text{ m}$ và $%s\\text{ cm} = %s\\text{ m}$.'
        % (d_hop_cm, fmt_num(d_hop_m), h_anh_cm, fmt_num(h_anh_m))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tỉ số đồng dạng của $\\Delta OAB$ với $\\Delta OA^{\prime}B^{\prime}$ bằng $%s$' % k
    vd_da_1_s = 'Tỉ số đồng dạng của $\\Delta OAB$ với $\\Delta OA^{\prime}B^{\prime}$ bằng $%s$' % (k // 10)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Tỉ số đồng dạng của $\\Delta OAB$ với $\\Delta OA^{\prime}B^{\prime}$ bằng tỉ số khoảng cách từ lỗ kim đến tòa nhà '
        'và từ lỗ kim đến màn hứng: $k = \\dfrac{%s}{%s} = %s$.'
        % (d_nha_m, fmt_num(d_hop_m), k)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Chiều cao thực tế $AB$ của tòa nhà bằng $%s\\text{ m}$' % fmt_num(h_nha_m)
    vdc_da_1_s = 'Chiều cao thực tế $AB$ của tòa nhà bằng $%s\\text{ m}$' % fmt_num(h_nha_m + 6)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Vì $\\Delta OAB \\backsim \\Delta OA^{\prime}B^{\prime}$ theo tỉ số đồng dạng $k = %s$ nên $\\dfrac{AB}{A^{\prime}B^{\prime}} = %s$.\\ '
        'Suy ra $AB = %s \\cdot %s = %s\\text{ m}$.'
        % (k, k, fmt_num(h_anh_m), k, fmt_num(h_nha_m))
    )
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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \end{minipage}\n\n')
    return content
