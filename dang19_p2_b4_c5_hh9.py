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

def bt_dang19_p2_b4_c5_hh9(self):
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
        # Dạng 19: Hai tiếp tuyến cắt nhau của đường tròn và tam giác đều trong thiết kế cảnh quan
        R = random.choice([3, 4, 5, 6, 7, 8, 9, 10])
        OS = 2 * R
        chu_vi = 3 * R
        d_sai = R + 0.5

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (S) at (-3.2,0);\n"
            "\\coordinate (A) at (-0.8,1.386);\n"
            "\\coordinate (B) at (-0.8,-1.386);\n"
            "\\draw[line width=1pt] (O) circle (1.6);\n"
            "\\draw[line width=1pt] (S)--(A)--(B)--cycle;\n"
            "\\draw[line width=1pt] (O)--(A) (O)--(B) (S)--(O);\n"
            "\\draw[line width=1pt] (-0.973,1.286)--(-0.873,1.113)--(-0.7,1.213);\n"
            "\\draw[line width=1pt] (-0.973,-1.286)--(-0.873,-1.113)--(-0.7,-1.213);\n"
            "\\fill (O) circle (1pt) node[right] {$O$};\n"
            "\\fill (S) circle (1pt) node[left] {$S$};\n"
            "\\fill (A) circle (1pt) node[above] {$A$};\n"
            "\\fill (B) circle (1pt) node[below] {$B$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Trong công viên có một bồn hoa hình tròn tâm $O$, bán kính $R = %s\\text{ m}$. Từ một ghế đá đặt tại điểm $S$ cách tâm bồn hoa $OS = %s\\text{ m}$, người ta lát hai lối đi thẳng tiếp xúc với bồn hoa tại $A$ và $B$, đồng thời lát thêm một lối đi thẳng nối hai tiếp điểm $A$ và $B$.\n%s'''
            % (fmt_num(R), fmt_num(OS), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Lối đi $AB$ vuông góc với đường thẳng nối ghế đá $S$ và tâm $O$ của bồn hoa'
        nb_da_1_s = 'Lối đi $AB$ song song với đường thẳng nối ghế đá $S$ và tâm $O$ của bồn hoa'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì $SA$ và $SB$ là hai tiếp tuyến của đường tròn $(O)$ cắt nhau tại $S$ nên $SO$ là tia phân giác của góc $\\widehat{AOB}$. \\\\ Trong tam giác cân $OAB$ ($OA = OB = R$), đường phân giác $SO$ đồng thời là đường cao nên $SO \\perp AB$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Trong tam giác cân $OAB$, tia phân giác $SO$ của góc ở đỉnh $\\widehat{AOB}$ đồng thời là đường cao nên $SO \\perp AB$ (không phải song song).'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Góc tạo bởi hai lối đi $SA$ và $SB$ xuất phát từ ghế đá bằng $60^\\circ$'
        th_da_1_s = 'Góc tạo bởi hai lối đi $SA$ và $SB$ xuất phát từ ghế đá bằng $45^\\circ$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Vì $SA$ tiếp xúc với $(O)$ tại $A$ nên $OA \\perp SA$, suy ra tam giác $OAS$ vuông tại $A$. \\\\ Xét tam giác $OAS$ vuông tại $A$, ta có: $\\sin \\widehat{ASO} = \\frac{OA}{OS} = \\frac{%s}{%s} = \\frac{1}{2} \\Rightarrow \\widehat{ASO} = 30^\\circ$. \\\\ Vì $SO$ là tia phân giác của góc $\\widehat{ASB}$ nên $\\widehat{ASB} = 2\\widehat{ASO} = 2 \\cdot 30^\\circ = 60^\\circ$.'''
            % (fmt_num(R), fmt_num(OS))
        )
        loigiai_th_1_s = (
            '''Sai. Trong tam giác $OAS$ vuông tại $A$, ta có $\\sin \\widehat{ASO} = \\frac{OA}{OS} = \\frac{%s}{%s} = \\frac{1}{2} \\Rightarrow \\widehat{ASO} = 30^\\circ$. \\\\ Suy ra góc tạo bởi hai lối đi là $\\widehat{ASB} = 2\\widehat{ASO} = 60^\\circ$ (khác $45^\\circ$).'''
            % (fmt_num(R), fmt_num(OS))
        )

        # Vận dụng
        vd_da_1_d = '\\True Ba lối đi $SA$, $SB$ và $AB$ tạo thành một tam giác đều có chu vi bằng $%s\\sqrt{3}\\text{ m}$' % (fmt_num(chu_vi))
        vd_da_1_s = 'Ba lối đi $SA$, $SB$ và $AB$ tạo thành một tam giác đều có chu vi bằng $%s\\text{ m}$' % (fmt_num(chu_vi))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Áp dụng định lí Pythagore vào tam giác $OAS$ vuông tại $A$, ta có: $SA = SB = \\sqrt{OS^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\sqrt{3}\\text{ m}$. \\\\ Tam giác $SAB$ cân tại $S$ ($SA = SB$) lại có $\\widehat{ASB} = 60^\\circ$ nên tam giác $SAB$ là tam giác đều. \\\\ Vậy chu vi của tam giác $SAB$ bằng $3 \\cdot %s\\sqrt{3} = %s\\sqrt{3}\\text{ m}$.'''
            % (fmt_num(OS), fmt_num(R), fmt_num(R), fmt_num(R), fmt_num(chu_vi))
        )
        loigiai_vd_1_s = (
            '''Sai. Áp dụng định lí Pythagore vào tam giác $OAS$ vuông tại $A$, ta tính được $SA = SB = \\sqrt{%s^2 - %s^2} = %s\\sqrt{3}\\text{ m}$. \\\\ Vì tam giác $SAB$ đều nên chu vi của tam giác $SAB$ bằng $3 \\cdot %s\\sqrt{3} = %s\\sqrt{3}\\text{ m}$ (khác $%s\\text{ m}$).'''
            % (fmt_num(OS), fmt_num(R), fmt_num(R), fmt_num(R), fmt_num(chu_vi), fmt_num(chu_vi))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Khoảng cách ngắn nhất từ ghế đá $S$ đến mép bồn hoa bằng $%s\\text{ m}$' % (fmt_num(R))
        vdc_da_1_s = 'Khoảng cách ngắn nhất từ ghế đá $S$ đến mép bồn hoa lớn hơn $%s\\text{ m}$' % (fmt_num(d_sai))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Khoảng cách ngắn nhất từ điểm $S$ nằm ngoài đường tròn $(O; R)$ đến mép bồn hoa chính là khoảng cách từ $S$ đến giao điểm của đoạn thẳng $OS$ với đường tròn $(O)$, bằng $OS - R = %s - %s = %s\\text{ m}$.'''
            % (fmt_num(OS), fmt_num(R), fmt_num(R))
        )
        loigiai_vdc_1_s = (
            '''Sai. Khoảng cách ngắn nhất từ ghế đá $S$ đến mép bồn hoa là $OS - R = %s - %s = %s\\text{ m}$ (nhỏ hơn $%s\\text{ m}$).'''
            % (fmt_num(OS), fmt_num(R), fmt_num(R), fmt_num(d_sai))
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
