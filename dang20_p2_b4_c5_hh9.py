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

def bt_dang20_p2_b4_c5_hh9(self):
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
        # Dạng 20: Đường tròn tiếp xúc với cả ba cạnh của tam giác vuông trong thiết kế bao bì
        bo_so = [
            (2, 5, 12, 13),
            (2, 12, 5, 13),
            (3, 8, 15, 17),
            (3, 15, 8, 17),
            (3, 9, 12, 15),
            (3, 12, 9, 15),
            (4, 12, 16, 20),
            (4, 16, 12, 20),
            (5, 12, 35, 37),
            (6, 15, 36, 39),
            (6, 20, 21, 29),
            (6, 21, 20, 29)
        ]
        R, AB, AC, BC = random.choice(bo_so)
        BE = AB - R
        CF = AC - R
        AC_sai = AC + 4

        AB_sq = AB * AB
        two_R = 2 * R
        R_sq = R * R
        two_BE = 2 * BE
        BE_sq = BE * BE
        diff_coeff = two_BE - two_R
        rhs = AB_sq + R_sq - BE_sq

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (A) at (0,0);\n"
            "\\coordinate (B) at (0,2.4);\n"
            "\\coordinate (C) at (3.2,0);\n"
            "\\coordinate (O) at (0.8,0.8);\n"
            "\\coordinate (E) at (0,0.8);\n"
            "\\coordinate (F) at (0.8,0);\n"
            "\\coordinate (D) at (1.28,1.44);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n"
            "\\draw[line width=1pt] (O) circle (0.8);\n"
            "\\draw[line width=1pt, dashed] (O)--(E) (O)--(F) (O)--(D);\n"
            "\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);\n"
            "\\draw[line width=1pt] (0,1.0)--(0.2,1.0)--(0.2,0.8);\n"
            "\\draw[line width=1pt] (1.0,0)--(1.0,0.2)--(0.8,0.2);\n"
            "\\fill (A) circle (1pt) node[below left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above] {$B$};\n"
            "\\fill (C) circle (1pt) node[below right] {$C$};\n"
            "\\fill (O) circle (1pt) node[above right] {$O$};\n"
            "\\fill (E) circle (1pt) node[left] {$E$};\n"
            "\\fill (F) circle (1pt) node[below] {$F$};\n"
            "\\fill (D) circle (1pt) node[above right] {$D$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Một nghệ nhân làm hộp quà bằng cách đặt một chiếc bánh hình trụ tròn (mặt đáy là đường tròn $(O; %s\\text{ cm})$) vào vừa khít bên trong một khuôn giấy hình tam giác $ABC$ vuông tại $A$ sao cho cả ba cạnh $AB$, $AC$, $BC$ của khuôn đều tiếp xúc với đáy bánh. Biết cạnh $AB = %s\\text{ cm}$.\n%s'''
            % (fmt_num(R), fmt_num(AB), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Khoảng cách từ tâm $O$ của đáy bánh đến ba thành khuôn $AB$, $AC$, $BC$ đều bằng $%s\\text{ cm}$' % (fmt_num(R))
        nb_da_1_s = 'Khoảng cách từ tâm $O$ của đáy bánh đến cạnh huyền $BC$ lớn hơn $%s\\text{ cm}$' % (fmt_num(R))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì cả ba cạnh $AB$, $AC$, $BC$ của khuôn đều tiếp xúc với đường tròn $(O; %s\\text{ cm})$ nên khoảng cách từ tâm $O$ đến ba đường thẳng $AB$, $AC$, $BC$ đều bằng bán kính $R = %s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_nb_1_s = (
            '''Sai. Vì cạnh huyền $BC$ tiếp xúc với đường tròn $(O; %s\\text{ cm})$ nên khoảng cách từ tâm $O$ đến đường thẳng $BC$ bằng đúng bán kính $R = %s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R))
        )

        # Thông hiểu
        th_da_1_d = '\\True Tiếp điểm $E \\in AB$ và tiếp điểm $F \\in AC$ tạo với đỉnh $A$ và tâm $O$ một hình vuông $AEOF$ có cạnh $%s\\text{ cm}$' % (fmt_num(R))
        th_da_1_s = 'Tiếp điểm $E \\in AB$ và tiếp điểm $F \\in AC$ tạo với đỉnh $A$ và tâm $O$ một hình chữ nhật có hai cạnh không bằng nhau'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Vì $AB$ tiếp xúc với $(O)$ tại $E$ và $AC$ tiếp xúc với $(O)$ tại $F$ nên $OE \\perp AB$ tại $E$ và $OF \\perp AC$ tại $F$. \\\\ Tứ giác $AEOF$ có $\\widehat{EAF} = \\widehat{AEO} = \\widehat{AFO} = 90^\\circ$ nên là hình chữ nhật, lại có $OE = OF = R = %s\\text{ cm}$ nên $AEOF$ là hình vuông có cạnh bằng $%s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_th_1_s = (
            '''Sai. Tứ giác $AEOF$ có ba góc vuông ($\\widehat{EAF} = \\widehat{AEO} = \\widehat{AFO} = 90^\\circ$) và hai cạnh kề bằng nhau ($OE = OF = R = %s\\text{ cm}$) nên $AEOF$ là hình vuông có cạnh bằng $%s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R))
        )

        # Vận dụng
        vd_da_1_d = '\\True Độ dài hai đoạn từ đỉnh $B$ đến hai tiếp điểm trên cạnh $AB$ và $BC$ đều bằng $%s\\text{ cm}$' % (fmt_num(BE))
        vd_da_1_s = 'Độ dài hai đoạn từ đỉnh $B$ đến hai tiếp điểm trên cạnh $AB$ và $BC$ đều bằng $%s\\text{ cm}$' % (fmt_num(BE + 2))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Gọi $D$ là tiếp điểm của $(O)$ với cạnh $BC$. Vì $AEOF$ là hình vuông cạnh $%s\\text{ cm}$ nên $AE = AF = %s\\text{ cm}$. \\\\ Suy ra $BE = AB - AE = %s - %s = %s\\text{ cm}$. Theo tính chất hai tiếp tuyến cắt nhau tại $B$, ta có $BD = BE = %s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R), fmt_num(AB), fmt_num(R), fmt_num(BE), fmt_num(BE))
        )
        loigiai_vd_1_s = (
            '''Sai. Vì $AE = %s\\text{ cm}$ nên $BE = AB - AE = %s - %s = %s\\text{ cm}$. Theo tính chất hai tiếp tuyến cắt nhau tại $B$, ta có $BD = BE = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(R), fmt_num(AB), fmt_num(R), fmt_num(BE), fmt_num(BE), fmt_num(BE + 2))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Độ dài cạnh $AC$ của khuôn giấy bằng $%s\\text{ cm}$' % (fmt_num(AC))
        vdc_da_1_s = 'Độ dài cạnh $AC$ của khuôn giấy bằng $%s\\text{ cm}$' % (fmt_num(AC_sai))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Đặt $CF = x$ ($x > 0$). Theo tính chất hai tiếp tuyến cắt nhau tại $C$, ta có $CD = CF = x$. \\\\ Khi đó $AC = AF + CF = x + %s$ và $BC = BD + CD = x + %s$. \\\\ Áp dụng định lí Pythagore vào tam giác $ABC$ vuông tại $A$, ta có: \\\\ $AB^2 + AC^2 = BC^2 \\Leftrightarrow %s^2 + (x + %s)^2 = (x + %s)^2$ \\\\ $\\Leftrightarrow %s + x^2 + %sx + %s = x^2 + %sx + %s$ \\\\ $\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\ Vậy độ dài cạnh $AC = %s + %s = %s\\text{ cm}$.'''
            % (
                fmt_num(R), fmt_num(BE),
                fmt_num(AB), fmt_num(R), fmt_num(BE),
                fmt_num(AB_sq), fmt_num(two_R), fmt_num(R_sq), fmt_num(two_BE), fmt_num(BE_sq),
                fmt_num(diff_coeff), fmt_num(rhs), fmt_num(CF),
                fmt_num(CF), fmt_num(R), fmt_num(AC)
            )
        )
        loigiai_vdc_1_s = (
            '''Sai. Đặt $CF = x$ ($x > 0$), suy ra $CD = x$, $AC = x + %s$ và $BC = x + %s$. \\\\ Áp dụng định lí Pythagore vào tam giác $ABC$ vuông tại $A$, ta có: \\\\ $%s^2 + (x + %s)^2 = (x + %s)^2 \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$. \\\\ Vậy độ dài cạnh $AC = %s + %s = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (
                fmt_num(R), fmt_num(BE),
                fmt_num(AB), fmt_num(R), fmt_num(BE), fmt_num(diff_coeff), fmt_num(rhs), fmt_num(CF),
                fmt_num(CF), fmt_num(R), fmt_num(AC), fmt_num(AC_sai)
            )
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
