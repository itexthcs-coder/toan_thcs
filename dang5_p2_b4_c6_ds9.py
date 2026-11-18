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


def bt_dang5_p2_b4_c6_ds9(self):
    def fmt_num(val):
        return str(int(val))

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        canh_day = random.randint(8, 16)
        chieu_cao = random.randint(5, 12)
        s_xq_coef = 4 * chieu_cao
        tong_dien_tich = canh_day**2 + s_xq_coef * canh_day
        the_tich = (canh_day**2) * chieu_cao

        noidungcauhoi = ('''Một xưởng sản xuất bao bì cần làm những chiếc hộp đựng bánh dạng hình hộp chữ nhật không nắp, có đáy là hình vuông và chiều cao cố định là $%s\\text{ cm}$. Để tiết kiệm giấy bìa, tổng diện tích xung quanh và diện tích đáy của mỗi hộp được thiết kế đúng bằng $%s\\text{ cm}^2$. Gọi $x\\text{ (cm)}$ là độ dài cạnh đáy của chiếc hộp ($x > 0$).
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (3,0);
\\coordinate (C) at (4.2,0.9);
\\coordinate (D) at (1.2,0.9);
\\coordinate (A1) at (0,2);
\\coordinate (B1) at (3,2);
\\coordinate (C1) at (4.2,2.9);
\\coordinate (D1) at (1.2,2.9);
\\draw[line width=1pt] (A)--(B)--(C)--(C1)--(D1)--(A1)--cycle;
\\draw[line width=1pt] (A1)--(B1)--(C1) (B)--(B1);
\\draw[line width=1pt, dashed] (A)--(D)--(C) (D)--(D1);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\node at (1.5,-0.3) {$x\\text{ (cm)}$};
\\node[right] at (4.25,1.9) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}''' % (fmt_num(chieu_cao), fmt_num(tong_dien_tich), fmt_num(chieu_cao)))

        nb_da_1_d = '\\True Diện tích đáy của chiếc hộp là $x^2\\text{ (cm}^2\\text{)}$'
        nb_da_1_s = 'Diện tích đáy của chiếc hộp là $4x\\text{ (cm}^2\\text{)}$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì đáy chiếc hộp là hình vuông cạnh $x\\text{ (cm)}$ nên diện tích đáy là $x^2\\text{ (cm}^2\\text{)}$.''')

        th_da_1_d = '\\True Diện tích xung quanh của chiếc hộp là $%sx\\text{ (cm}^2\\text{)}$' % (fmt_num(s_xq_coef))
        th_da_1_s = 'Diện tích xung quanh của chiếc hộp là $%sx\\text{ (cm}^2\\text{)}$' % (fmt_num(2 * chieu_cao))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Diện tích xung quanh của hình hộp chữ nhật có đáy vuông cạnh $x$, chiều cao $%s\\text{ cm}$ là $4 \\cdot x \\cdot %s = %sx\\text{ (cm}^2\\text{)}$.''' % (fmt_num(chieu_cao), fmt_num(chieu_cao), fmt_num(s_xq_coef)))

        vd_da_1_d = '\\True Phương trình tìm cạnh đáy $x$ là $x^2 + %sx - %s = 0$' % (fmt_num(s_xq_coef), fmt_num(tong_dien_tich))
        vd_da_1_s = 'Phương trình tìm cạnh đáy $x$ là $x^2 + %sx + %s = 0$' % (fmt_num(s_xq_coef), fmt_num(tong_dien_tich))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Tổng diện tích xung quanh và diện tích đáy bằng $%s\\text{ cm}^2$ nên ta có phương trình: $x^2 + %sx = %s \\Leftrightarrow x^2 + %sx - %s = 0$.''' % (fmt_num(tong_dien_tich), fmt_num(s_xq_coef), fmt_num(tong_dien_tich), fmt_num(s_xq_coef), fmt_num(tong_dien_tich)))

        vdc_da_1_d = '\\True Thể tích của chiếc hộp đựng bánh này là $%s\\text{ cm}^3$' % (fmt_num(the_tich))
        vdc_da_1_s = 'Thể tích của chiếc hộp đựng bánh này là $%s\\text{ cm}^3$' % (fmt_num(the_tich + 120))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        b_half = s_xq_coef // 2
        delta_p = b_half**2 + tong_dien_tich
        sqrt_dp = int(math.isqrt(delta_p))
        loigiai_vdc_1 = ('''Giải phương trình $x^2 + %sx - %s = 0$: \\\\ Ta có $\\Delta' = %s^2 - 1 \\cdot (-%s) = %s$, $\\sqrt{\\Delta'} = %s$. \\\\ Nghiệm của phương trình là $x_1 = -%s + %s = %s$ (thoả mãn) và $x_2 = -%s - %s = -%s$ (loại). \\\\ Vậy cạnh đáy của hộp là $%s\\text{ cm}$ và thể tích của chiếc hộp là $%s^2 \\cdot %s = %s\\text{ cm}^3$.''' % (fmt_num(s_xq_coef), fmt_num(tong_dien_tich), fmt_num(b_half), fmt_num(tong_dien_tich), fmt_num(delta_p), fmt_num(sqrt_dp), fmt_num(b_half), fmt_num(sqrt_dp), fmt_num(canh_day), fmt_num(b_half), fmt_num(sqrt_dp), fmt_num(canh_day + s_xq_coef), fmt_num(canh_day), fmt_num(canh_day), fmt_num(chieu_cao), fmt_num(the_tich)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb)
    combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th)
    combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd)
    combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc)

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
