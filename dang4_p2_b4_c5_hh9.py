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

def bt_dang4_p2_b4_c5_hh9(self):
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
        # Dạng 4: Tính độ dài đoạn thẳng và góc liên quan đến hai tiếp tuyến cắt nhau của đường tròn
        R = random.choice([4, 5, 6, 7, 8, 9, 10])
        OP = 2 * R
        OP_sai = R + 4

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (P) at (-3.0,0);\n"
            "\\coordinate (M) at (-0.75,1.299);\n"
            "\\coordinate (N) at (-0.75,-1.299);\n"
            "\\draw[line width=1pt] (O) circle (1.5);\n"
            "\\draw[line width=1pt] (P)--(M) (P)--(N) (O)--(M) (O)--(N) (P)--(O) (M)--(N);\n"
            "\\draw[line width=1pt] (-0.923,1.199)--(-0.823,1.026)--(-0.65,1.126);\n"
            "\\draw[line width=1pt] (-0.923,-1.199)--(-0.823,-1.026)--(-0.65,-1.126);\n"
            "\\fill (O) circle (1pt) node[right] {$O$};\n"
            "\\fill (P) circle (1pt) node[left] {$P$};\n"
            "\\fill (M) circle (1pt) node[above] {$M$};\n"
            "\\fill (N) circle (1pt) node[below] {$N$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Từ điểm $P$ nằm ngoài đường tròn $(O; %s\\text{ cm})$, kẻ hai tiếp tuyến $PM$, $PN$ đến đường tròn ($M$, $N$ là các tiếp điểm) sao cho $\\widehat{MPN} = 60^\\circ$.\n%s'''
            % (fmt_num(R), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Tia $PO$ là tia phân giác của góc $\\widehat{MPN}$ nên $\\widehat{MPO} = 30^\\circ$'
        nb_da_1_s = 'Tia $PO$ là tia phân giác của góc $\\widehat{MPN}$ nên $\\widehat{MPO} = 60^\\circ$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì $PM$ và $PN$ là hai tiếp tuyến của đường tròn $(O)$ cắt nhau tại $P$ nên theo tính chất hai tiếp tuyến cắt nhau, $PO$ là tia phân giác của góc $\\widehat{MPN}$. Do đó $\\widehat{MPO} = \\frac{1}{2}\\widehat{MPN} = \\frac{1}{2} \\cdot 60^\\circ = 30^\\circ$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Theo tính chất hai tiếp tuyến cắt nhau, $PO$ là tia phân giác của góc $\\widehat{MPN}$ nên $\\widehat{MPO} = \\frac{1}{2}\\widehat{MPN} = 30^\\circ$ (khác $60^\\circ$).'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Độ dài đoạn thẳng $OP$ bằng $%s\\text{ cm}$' % (fmt_num(OP))
        th_da_1_s = 'Độ dài đoạn thẳng $OP$ bằng $%s\\text{ cm}$' % (fmt_num(OP_sai))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Vì $PM$ tiếp xúc với đường tròn $(O)$ tại $M$ nên $OM \\perp PM$, suy ra tam giác $OMP$ vuông tại $M$. \\\\ Xét tam giác $OMP$ vuông tại $M$ có $\\widehat{MPO} = 30^\\circ$, ta có: $OP = \\frac{OM}{\\sin 30^\\circ} = 2 \\cdot OM = 2 \\cdot %s = %s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(OP))
        )
        loigiai_th_1_s = (
            '''Sai. Xét tam giác $OMP$ vuông tại $M$ có $\\widehat{MPO} = 30^\\circ$, ta có $OP = 2 \\cdot OM = 2 \\cdot %s = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(R), fmt_num(OP), fmt_num(OP_sai))
        )

        # Vận dụng
        vd_da_1_d = '\\True Độ dài hai tiếp tuyến $PM = PN = %s\\sqrt{3}\\text{ cm}$' % (fmt_num(R))
        vd_da_1_s = 'Độ dài hai tiếp tuyến $PM = PN = %s\\sqrt{2}\\text{ cm}$' % (fmt_num(R))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Áp dụng định lí Pythagore vào tam giác $OMP$ vuông tại $M$, ta có: $PM = \\sqrt{OP^2 - OM^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{3 \\cdot %s^2} = %s\\sqrt{3}\\text{ cm}$. \\\\ Theo tính chất hai tiếp tuyến cắt nhau, ta có $PN = PM = %s\\sqrt{3}\\text{ cm}$.'''
            % (fmt_num(OP), fmt_num(R), fmt_num(R), fmt_num(R), fmt_num(R))
        )
        loigiai_vd_1_s = (
            '''Sai. Áp dụng định lí Pythagore vào tam giác $OMP$ vuông tại $M$, ta có $PM = \\sqrt{OP^2 - OM^2} = \\sqrt{%s^2 - %s^2} = %s\\sqrt{3}\\text{ cm}$. Suy ra $PN = PM = %s\\sqrt{3}\\text{ cm}$ (khác $%s\\sqrt{2}\\text{ cm}$).'''
            % (fmt_num(OP), fmt_num(R), fmt_num(R), fmt_num(R), fmt_num(R))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Độ dài dây cung $MN$ bằng $%s\\sqrt{3}\\text{ cm}$' % (fmt_num(R))
        vdc_da_1_s = 'Tam giác $OMN$ là tam giác vuông cân tại $O$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Tam giác $PMN$ có $PM = PN$ (tính chất hai tiếp tuyến cắt nhau) và $\\widehat{MPN} = 60^\\circ$ nên tam giác $PMN$ là tam giác đều. Do đó độ dài dây cung $MN = PM = %s\\sqrt{3}\\text{ cm}$.'''
            % (fmt_num(R))
        )
        loigiai_vdc_1_s = (
            '''Sai. Trong tứ giác $OMPN$ có $\\widehat{OMP} = \\widehat{ONP} = 90^\\circ$ và $\\widehat{MPN} = 60^\\circ$ nên $\\widehat{MON} = 360^\\circ - 90^\\circ - 90^\\circ - 60^\\circ = 120^\\circ \\neq 90^\\circ$. Vậy tam giác $OMN$ là tam giác cân tại $O$ có góc ở đỉnh bằng $120^\\circ$, không phải tam giác vuông cân.'''
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
