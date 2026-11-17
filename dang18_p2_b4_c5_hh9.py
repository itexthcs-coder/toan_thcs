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

def bt_dang18_p2_b4_c5_hh9(self):
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
        # Dạng 18: Vị trí tương đối của đường thẳng và đường tròn, tính chất hai tiếp tuyến cắt nhau trong thực tiễn thể thao
        while True:
            R = random.choice([1.5, 1.6, 1.8, 2.0, 2.1, 2.4])
            d = random.choice([6.5, 7.0, 7.5, 8.0, 8.5, 9.0])
            diff_sq = round(d * d - R * R, 4)
            mc_val = math.sqrt(diff_sq)
            k = int(math.floor(mc_val))
            if abs(mc_val - k) > 1e-6:
                break

        AB = round(2 * R, 4)
        k_sq = k * k

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (A) at (0,1.2);\n"
            "\\coordinate (B) at (0,-1.2);\n"
            "\\coordinate (M) at (3.6,0);\n"
            "\\coordinate (C) at (0.4,1.131);\n"
            "\\coordinate (D) at (0.4,-1.131);\n"
            "\\draw[line width=1pt] (O) circle (1.2);\n"
            "\\draw[line width=1pt] (0,-2.1)--(0,2.1);\n"
            "\\draw[line width=1pt] (-3.6,-2.1)--(-3.6,2.1);\n"
            "\\draw[line width=1pt] (3.6,-2.1)--(3.6,2.1);\n"
            "\\draw[line width=1pt] (M)--(-0.4,1.414);\n"
            "\\draw[line width=1pt] (M)--(-0.4,-1.414);\n"
            "\\draw[line width=1pt] (O)--(C) (O)--(D);\n"
            "\\draw[line width=1pt, dashed] (O)--(M);\n"
            "\\draw[line width=1pt] (0.589,1.064)--(0.522,0.875)--(0.333,0.942);\n"
            "\\draw[line width=1pt] (0.589,-1.064)--(0.522,-0.875)--(0.333,-0.942);\n"
            "\\fill (O) circle (1pt) node[below left] {$O$};\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[below left] {$B$};\n"
            "\\fill (M) circle (1pt) node[right] {$M$};\n"
            "\\fill (C) circle (1pt) node[above] {$C$};\n"
            "\\fill (D) circle (1pt) node[below] {$D$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Vòng tròn trung tâm sân bóng rổ có tâm $O$, bán kính $R = %s\\text{ m}$. Đường vạch giữa sân là một đường thẳng đi qua tâm $O$, cắt vòng tròn tại $A$ và $B$. Hai đường biên dọc song song với nhau, cùng vuông góc với vạch giữa sân và cách tâm $O$ một khoảng $%s\\text{ m}$. Một cầu thủ đứng tại điểm $M$ trên đường biên dọc (cách $O$ một khoảng $OM = %s\\text{ m}$) chuyền bóng theo hai hướng tiếp xúc với vòng tròn trung tâm tại $C$ và $D$.\n%s'''
            % (fmt_num(R), fmt_num(d), fmt_num(d), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Đường vạch giữa sân cắt vòng tròn trung tâm tại hai điểm $A$, $B$ với $AB = %s\\text{ m}$' % (fmt_num(AB))
        nb_da_1_s = 'Đường vạch giữa sân cắt vòng tròn trung tâm tại hai điểm $A$, $B$ với $AB = %s\\text{ m}$' % (fmt_num(R))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì đường vạch giữa sân đi qua tâm $O$ của vòng tròn $(O; %s\\text{ m})$ nên dây cung $AB$ chính là đường kính của vòng tròn trung tâm: $AB = 2R = 2 \\cdot %s = %s\\text{ m}$.'''
            % (fmt_num(R), fmt_num(R), fmt_num(AB))
        )
        loigiai_nb_1_s = (
            '''Sai. Đường vạch giữa sân đi qua tâm $O$ nên cắt vòng tròn trung tâm theo một đường kính có độ dài $AB = 2R = 2 \\cdot %s = %s\\text{ m}$ (khác $%s\\text{ m}$).'''
            % (fmt_num(R), fmt_num(AB), fmt_num(R))
        )

        # Thông hiểu
        th_da_1_d = '\\True Hai đường biên dọc không giao nhau với vòng tròn trung tâm vì khoảng cách $%s\\text{ m} > %s\\text{ m}$' % (fmt_num(d), fmt_num(R))
        th_da_1_s = 'Hai đường biên dọc tiếp xúc với vòng tròn trung tâm vì vuông góc với vạch giữa sân'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Khoảng cách từ tâm $O$ đến mỗi đường biên dọc là $d = %s\\text{ m} > R = %s\\text{ m}$ nên hai đường biên dọc và vòng tròn trung tâm không giao nhau.'''
            % (fmt_num(d), fmt_num(R))
        )
        loigiai_th_1_s = (
            '''Sai. Khoảng cách từ tâm $O$ đến mỗi đường biên dọc là $d = %s\\text{ m} > R = %s\\text{ m}$ nên hai đường biên dọc không giao nhau với vòng tròn trung tâm.'''
            % (fmt_num(d), fmt_num(R))
        )

        # Vận dụng
        vd_da_1_d = '\\True Hai đường chuyền $MC$ và $MD$ tạo với đường thẳng $MO$ hai góc bằng nhau'
        vd_da_1_s = 'Hai đường chuyền $MC$ và $MD$ có độ dài khác nhau tùy thuộc vào hướng ném bóng'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Vì $MC$ và $MD$ là hai tiếp tuyến của đường tròn $(O)$ cắt nhau tại $M$ nên theo tính chất hai tiếp tuyến cắt nhau, $MO$ là tia phân giác của góc $\\widehat{CMD}$. Do đó $\\widehat{CMO} = \\widehat{DMO}$.'''
        )
        loigiai_vd_1_s = (
            '''Sai. Vì $MC$ và $MD$ là hai tiếp tuyến của $(O)$ cắt nhau tại $M$ nên theo tính chất hai tiếp tuyến cắt nhau, điểm $M$ cách đều hai tiếp điểm, suy ra $MC = MD$.'''
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Khoảng cách từ vị trí cầu thủ $M$ đến điểm chạm vòng tròn $C$ lớn hơn $%s\\text{ m}$' % (fmt_num(k))
        vdc_da_1_s = 'Khoảng cách từ vị trí cầu thủ $M$ đến điểm chạm vòng tròn $C$ nhỏ hơn $%s\\text{ m}$' % (fmt_num(k))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Vì $MC$ tiếp xúc với $(O)$ tại $C$ nên $OC \\perp MC$, suy ra tam giác $OCM$ vuông tại $C$. \\\\ Áp dụng định lí Pythagore vào tam giác $OCM$ vuông tại $C$, ta có: $MC = \\sqrt{OM^2 - OC^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s}\\text{ m}$. \\\\ Vì $\\sqrt{%s} > \\sqrt{%s} = %s$ nên $MC > %s\\text{ m}$.'''
            % (fmt_num(d), fmt_num(R), fmt_num(diff_sq), fmt_num(diff_sq), fmt_num(k_sq), fmt_num(k), fmt_num(k))
        )
        loigiai_vdc_1_s = (
            '''Sai. Áp dụng định lí Pythagore vào tam giác $OCM$ vuông tại $C$, ta có: $MC = \\sqrt{OM^2 - OC^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s}\\text{ m}$. \\\\ Vì $\\sqrt{%s} > \\sqrt{%s} = %s$ nên $MC > %s\\text{ m}$ (không nhỏ hơn $%s\\text{ m}$).'''
            % (fmt_num(d), fmt_num(R), fmt_num(diff_sq), fmt_num(diff_sq), fmt_num(k_sq), fmt_num(k), fmt_num(k), fmt_num(k))
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
