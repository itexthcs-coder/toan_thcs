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

def bt_dang1_p2_b4_c5_hh9(self):
    def fmt_num(val):
        if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
            return str(int(val))
        s = ("%.6f" % val).rstrip("0").rstrip(".")
        return s.replace(".", ",")

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Xác định vị trí tương đối của đường thẳng và đường tròn dựa vào khoảng cách từ tâm đến đường thẳng
        bo_so = [
            (3, 4, 5),
            (6, 8, 10),
            (5, 12, 13),
            (9, 12, 15),
            (8, 15, 17),
            (12, 16, 20),
            (7, 24, 25)
        ]
        d1, h, R = random.choice(bo_so)
        day_cung = 2 * h
        day_cung_sai = 2 * d1
        d2 = R
        k_them = random.choice([3, 4, 6, 7, 11])
        d3_sq = R * R + k_them
        R_sq = R * R

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (H) at (0,0.9);\n"
            "\\coordinate (A) at (-1.2,0.9);\n"
            "\\coordinate (B) at (1.2,0.9);\n"
            "\\coordinate (T) at (0,-1.5);\n"
            "\\draw[line width=1pt] (O) circle (1.5);\n"
            "\\draw[line width=1pt] (-2.3,0.9)--(2.3,0.9) node[above] {$d_1$};\n"
            "\\draw[line width=1pt] (-2.3,-1.5)--(2.3,-1.5) node[above] {$d_2$};\n"
            "\\draw[line width=1pt] (-2.3,-2.2)--(2.3,-2.2) node[above] {$d_3$};\n"
            "\\draw[line width=1pt, dashed] (O)--(H) (O)--(T) (O)--(A) (O)--(B);\n"
            "\\draw[line width=1pt] (0,0.7)--(0.2,0.7)--(0.2,0.9);\n"
            "\\draw[line width=1pt] (0,-1.3)--(0.2,-1.3)--(0.2,-1.5);\n"
            "\\fill (O) circle (1pt) node[left] {$O$};\n"
            "\\fill (H) circle (1pt) node[above right] {$H$};\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above right] {$B$};\n"
            "\\fill (T) circle (1pt) node[below] {$T$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho đường tròn $(O; %s\\text{ cm})$ và ba đường thẳng $d_1$, $d_2$, $d_3$ có khoảng cách từ tâm $O$ đến mỗi đường thẳng lần lượt là $%s\\text{ cm}$, $%s\\text{ cm}$ và $\\sqrt{%s}\\text{ cm}$.\n%s'''
            % (fmt_num(R), fmt_num(d1), fmt_num(d2), fmt_num(d3_sq), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Đường thẳng $d_2$ là tiếp tuyến của đường tròn $(O)$ vì có duy nhất một điểm chung với đường tròn'
        nb_da_1_s = 'Đường thẳng $d_2$ không giao nhau với đường tròn $(O)$ vì khoảng cách từ $O$ đến $d_2$ bằng $%s\\text{ cm}$' % (fmt_num(d2))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Khoảng cách từ tâm $O$ đến đường thẳng $d_2$ bằng $%s\\text{ cm} = R$ nên đường thẳng $d_2$ và đường tròn $(O)$ tiếp xúc với nhau, tức là chúng có duy nhất một điểm chung. Khi đó $d_2$ là tiếp tuyến của đường tròn $(O)$.'''
            % (fmt_num(d2))
        )
        loigiai_nb_1_s = (
            '''Sai. Khoảng cách từ tâm $O$ đến đường thẳng $d_2$ bằng $%s\\text{ cm} = R$ nên đường thẳng $d_2$ tiếp xúc với đường tròn $(O)$ tại một tiếp điểm duy nhất, không phải không giao nhau.'''
            % (fmt_num(d2))
        )

        # Thông hiểu
        th_da_1_d = '\\True Đường thẳng $d_3$ không giao nhau với đường tròn $(O)$ vì $\\sqrt{%s} > %s$' % (fmt_num(d3_sq), fmt_num(R))
        th_da_1_s = 'Đường thẳng $d_3$ cắt đường tròn $(O)$ tại hai điểm phân biệt vì $\\sqrt{%s} < %s$' % (fmt_num(d3_sq), fmt_num(R))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Ta có $%s = \\sqrt{%s}$ và $\\sqrt{%s} > \\sqrt{%s} = %s$, tức là khoảng cách từ tâm $O$ đến đường thẳng $d_3$ lớn hơn bán kính $R$. Vậy đường thẳng $d_3$ và đường tròn $(O)$ không giao nhau.'''
            % (fmt_num(R), fmt_num(R_sq), fmt_num(d3_sq), fmt_num(R_sq), fmt_num(R))
        )
        loigiai_th_1_s = (
            '''Sai. Ta có $%s = \\sqrt{%s}$, vì $\\sqrt{%s} > \\sqrt{%s}$ nên khoảng cách từ tâm $O$ đến đường thẳng $d_3$ lớn hơn bán kính $R = %s\\text{ cm}$. Do đó đường thẳng $d_3$ và đường tròn $(O)$ không giao nhau.'''
            % (fmt_num(R), fmt_num(R_sq), fmt_num(d3_sq), fmt_num(R_sq), fmt_num(R))
        )

        # Vận dụng
        vd_da_1_d = '\\True Đường thẳng $d_1$ cắt đường tròn $(O)$ tại hai điểm phân biệt tạo thành một dây cung có độ dài bằng $%s\\text{ cm}$' % (fmt_num(day_cung))
        vd_da_1_s = 'Đường thẳng $d_1$ cắt đường tròn $(O)$ tại hai điểm phân biệt tạo thành một dây cung có độ dài bằng $%s\\text{ cm}$' % (fmt_num(day_cung_sai))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Vì khoảng cách từ tâm $O$ đến đường thẳng $d_1$ là $%s\\text{ cm} < %s\\text{ cm}$ nên $d_1$ cắt đường tròn $(O)$ tại hai điểm phân biệt $A$ và $B$. \\\\ Kẻ $OH \\perp AB$ tại $H$, khi đó $OH = %s\\text{ cm}$ và $H$ là trung điểm của dây cung $AB$. \\\\ Áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta có: $HA = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$. \\\\ Vậy độ dài dây cung $AB = 2 \\cdot HA = 2 \\cdot %s = %s\\text{ cm}$.'''
            % (fmt_num(d1), fmt_num(R), fmt_num(d1), fmt_num(R), fmt_num(d1), fmt_num(h), fmt_num(h), fmt_num(day_cung))
        )
        loigiai_vd_1_s = (
            '''Sai. Vì khoảng cách từ tâm $O$ đến $d_1$ là $%s\\text{ cm} < %s\\text{ cm}$ nên $d_1$ cắt $(O)$ tại hai điểm $A$, $B$. \\\\ Kẻ $OH \\perp AB$ tại $H$, áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta có: $HA = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$. \\\\ Suy ra độ dài dây cung $AB = 2 \\cdot HA = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(d1), fmt_num(R), fmt_num(R), fmt_num(d1), fmt_num(h), fmt_num(day_cung), fmt_num(day_cung_sai))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Khoảng cách từ tâm $O$ đến tiếp điểm của $d_2$ với $(O)$ bằng đúng bán kính $%s\\text{ cm}$' % (fmt_num(R))
        vdc_da_1_s = 'Khoảng cách từ tâm $O$ đến tiếp điểm của $d_2$ với $(O)$ nhỏ hơn bán kính đường tròn'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Gọi $T$ là tiếp điểm của tiếp tuyến $d_2$ và đường tròn $(O; %s\\text{ cm})$. Vì $T$ nằm trên đường tròn $(O)$ và $OT \\perp d_2$ tại $T$ nên khoảng cách từ tâm $O$ đến tiếp điểm $T$ chính là độ dài bán kính $OT = %s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_vdc_1_s = (
            '''Sai. Tiếp điểm $T$ của đường thẳng $d_2$ và đường tròn $(O; %s\\text{ cm})$ thuộc đường tròn $(O)$ nên khoảng cách từ tâm $O$ đến tiếp điểm $T$ bằng đúng bán kính $OT = %s\\text{ cm}$, không nhỏ hơn bán kính đường tròn.'''
            % (fmt_num(R), fmt_num(R))
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)

            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            true_count = count_true_answers(answers)
            if 1 <= true_count <= 3:
                break

        loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
        loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
        loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s
        loigiai_vdc_1 = loigiai_vdc_1_d if vdc_da_1 == vdc_da_1_d else loigiai_vdc_1_s

        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]

        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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

    # Xuất câu trắc nghiệm đúng sai
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
