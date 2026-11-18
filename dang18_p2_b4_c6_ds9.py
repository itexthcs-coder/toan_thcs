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


def bt_dang18_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        dai = random.choice([12, 16, 20])
        rong = random.choice([8, 10, 15])
        cao = random.choice([3, 4, 5])
        giam_pt = random.choice([10, 20, 25])

        v_cu = dai * rong * cao
        s_day_moi = Decimal(dai * rong) * Decimal(100 - giam_pt) / Decimal(100)
        v_moi = s_day_moi * Decimal(cao)

        b_eq = dai + rong
        c_eq = Decimal(dai * rong) - s_day_moi
        delta = Decimal(b_eq**2) - Decimal(4) * c_eq
        x_exact = (Decimal(b_eq) - delta.sqrt()) / Decimal(2)
        x_round = x_exact.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        dai_moi = Decimal(dai) - x_round
        rong_moi = Decimal(rong) - x_round

        noidungcauhoi = ('''Một công ty bánh kẹo sản xuất loại hộp bánh quy dạng hình hộp chữ nhật có chiều dài $%s\\text{ cm}$, chiều rộng $%s\\text{ cm}$ và chiều cao $%s\\text{ cm}$. Do chi phí nguyên liệu đầu vào tăng cao nhưng vẫn muốn giữ nguyên giá bán niêm yết, công ty quyết định giảm $%s\\%%$ thể tích mỗi hộp bánh bằng cách giữ nguyên chiều cao $%s\\text{ cm}$, đồng thời giảm cả chiều dài và chiều rộng đi cùng một độ dài $x\\text{ (cm)}$ (kết quả làm tròn đến hàng phần trăm của cm).
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (3.6,0);
\\coordinate (C) at (4.6,0.8);
\\coordinate (D) at (1,0.8);
\\coordinate (A1) at (0,1.2);
\\coordinate (B1) at (3.6,1.2);
\\coordinate (C1) at (4.6,2);
\\coordinate (D1) at (1,2);
\\draw[line width=1pt] (A)--(B)--(C)--(C1)--(D1)--(A1)--cycle;
\\draw[line width=1pt] (A1)--(B1)--(C1) (B)--(B1);
\\draw[line width=1pt, dashed] (A)--(D)--(C) (D)--(D1);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\node at (1.8,-0.3) {$%s\\text{ cm}$};
\\node[below right] at (4.1,0.4) {$%s\\text{ cm}$};
\\node[right] at (4.65,1.4) {$%s\\text{ cm}$};
\\end{tikzpicture}
\\end{center}''' % (fmt_num(dai), fmt_num(rong), fmt_num(cao), fmt_num(giam_pt), fmt_num(cao), fmt_num(dai), fmt_num(rong), fmt_num(cao)))

        nb_da_1_d = '\\True Điều kiện thích hợp của ẩn $x$ là $0 < x < %s$' % (fmt_num(rong))
        nb_da_1_s = 'Điều kiện thích hợp của ẩn $x$ là $0 < x < %s$' % (fmt_num(dai))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Vì chiều rộng ban đầu là $%s\\text{ cm}$ nhỏ hơn chiều dài $%s\\text{ cm}$ nên độ dài giảm $x$ phải thoả mãn $0 < x < %s$.''' % (fmt_num(rong), fmt_num(dai), fmt_num(rong)))

        th_da_1_d = '\\True Thể tích của hộp bánh quy mới sau khi giảm $%s\\%%$ là $%s\\text{ cm}^3$' % (fmt_num(giam_pt), fmt_num(v_moi))
        th_da_1_s = 'Thể tích của hộp bánh quy mới sau khi giảm $%s\\%%$ là $%s\\text{ cm}^3$' % (fmt_num(giam_pt), fmt_num(v_cu))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thể tích hộp bánh ban đầu là $%s \\cdot %s \\cdot %s = %s\\text{ (cm}^3\\text{)}$. \\\\ Sau khi giảm $%s\\%%$, thể tích hộp bánh mới là $%s \\cdot (100\\%% - %s\\%%) = %s\\text{ (cm}^3\\text{)}$.''' % (fmt_num(dai), fmt_num(rong), fmt_num(cao), fmt_num(v_cu), fmt_num(giam_pt), fmt_num(v_cu), fmt_num(giam_pt), fmt_num(v_moi)))

        vd_da_1_d = '\\True Phương trình tìm độ dài $x$ là $(%s - x)(%s - x) = %s$' % (fmt_num(dai), fmt_num(rong), fmt_num(s_day_moi))
        vd_da_1_s = 'Phương trình tìm độ dài $x$ là $(%s + x)(%s + x) = %s$' % (fmt_num(dai), fmt_num(rong), fmt_num(s_day_moi))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Hộp bánh mới có chiều dài $%s - x\\text{ (cm)}$, chiều rộng $%s - x\\text{ (cm)}$ và chiều cao $%s\\text{ cm}$. \\\\ Ta có phương trình: $%s(%s - x)(%s - x) = %s \\Leftrightarrow (%s - x)(%s - x) = %s$.''' % (fmt_num(dai), fmt_num(rong), fmt_num(cao), fmt_num(cao), fmt_num(dai), fmt_num(rong), fmt_num(v_moi), fmt_num(dai), fmt_num(rong), fmt_num(s_day_moi)))

        vdc_da_1_d = '\\True Chiều dài và chiều rộng của hộp bánh mới lần lượt là $%s\\text{ cm}$ và $%s\\text{ cm}$' % (fmt_num(dai_moi), fmt_num(rong_moi))
        vdc_da_1_s = 'Chiều dài và chiều rộng của hộp bánh mới lần lượt là $%s\\text{ cm}$ và $%s\\text{ cm}$' % (fmt_num(dai_moi + Decimal('1.00')), fmt_num(rong_moi + Decimal('1.00')))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khai triển phương trình $(%s - x)(%s - x) = %s$, ta được $x^2 - %sx + %s = 0$. \\\\ Giải phương trình với điều kiện $0 < x < %s$, ta tìm được $x \\approx %s\\text{ (cm)}$. \\\\ Vậy chiều dài mới là $%s - %s = %s\\text{ (cm)}$ và chiều rộng mới là $%s - %s = %s\\text{ (cm)}$.''' % (fmt_num(dai), fmt_num(rong), fmt_num(s_day_moi), fmt_num(b_eq), fmt_num(c_eq), fmt_num(rong), fmt_num(x_round), fmt_num(dai), fmt_num(x_round), fmt_num(dai_moi), fmt_num(rong), fmt_num(x_round), fmt_num(rong_moi)))

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
