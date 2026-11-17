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

def bt_dang13_p2_b4_c5_hh9(self):
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
        # Dạng 13: Dây cung và tiếp tuyến của đường tròn trong kiến trúc cổng vòm
        bo_so = [
            (3, 4, 5),
            (6, 8, 10),
            (5, 12, 13),
            (9, 12, 15),
            (8, 15, 17)
        ]
        OH, HA, R = random.choice(bo_so)
        CH = R - OH
        AB = 2 * HA
        AB_sai = HA

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (C) at (0,1.8);\n"
            "\\coordinate (H) at (0,1.08);\n"
            "\\coordinate (A) at (-1.44,1.08);\n"
            "\\coordinate (B) at (1.44,1.08);\n"
            "\\draw[line width=1pt] (1.8,0) arc (0:180:1.8);\n"
            "\\draw[line width=1pt] (A)--(B);\n"
            "\\draw[line width=1pt] (-1.8,1.8)--(1.8,1.8);\n"
            "\\draw[line width=1pt] (O)--(C);\n"
            "\\draw[line width=1pt, dashed] (O)--(A) (O)--(B);\n"
            "\\draw[line width=1pt] (0,1.28)--(0.2,1.28)--(0.2,1.08);\n"
            "\\fill (O) circle (1pt) node[below] {$O$};\n"
            "\\fill (C) circle (1pt) node[above] {$C$};\n"
            "\\fill (H) circle (1pt) node[below right] {$H$};\n"
            "\\fill (A) circle (1pt) node[left] {$A$};\n"
            "\\fill (B) circle (1pt) node[right] {$B$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Một cổng chào có phần vòm phía trên là một cung tròn thuộc đường tròn tâm $O$, bán kính $R = %s\\text{ m}$. Người ta lắp một thanh giằng thép nằm ngang nối hai điểm $A$, $B$ trên vòm cổng cách đỉnh cao nhất $C$ của vòm một khoảng thẳng đứng bằng $%s\\text{ m}$ (tức $OC \\perp AB$ tại $H$ và $CH = %s\\text{ m}$).\n%s'''
            % (fmt_num(R), fmt_num(CH), fmt_num(CH), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Đường thẳng chứa thanh giằng $AB$ cắt đường tròn $(O; %s\\text{ m})$ tại hai điểm phân biệt $A$ và $B$' % (fmt_num(R))
        nb_da_1_s = 'Đường thẳng chứa thanh giằng $AB$ tiếp xúc với đường tròn $(O; %s\\text{ m})$' % (fmt_num(R))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Thanh giằng $AB$ nối hai điểm phân biệt $A$ và $B$ cùng nằm trên đường tròn $(O; %s\\text{ m})$ nên đường thẳng $AB$ cắt đường tròn $(O; %s\\text{ m})$ tại hai điểm phân biệt $A$ và $B$.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_nb_1_s = (
            '''Sai. Đường thẳng chứa thanh giằng $AB$ đi qua hai điểm phân biệt $A$, $B$ của đường tròn $(O; %s\\text{ m})$ nên nó cắt đường tròn tại hai điểm phân biệt, không phải tiếp xúc.'''
            % (fmt_num(R))
        )

        # Thông hiểu
        th_da_1_d = '\\True Khoảng cách từ tâm $O$ đến thanh giằng $AB$ bằng $%s\\text{ m}$' % (fmt_num(OH))
        th_da_1_s = 'Khoảng cách từ tâm $O$ đến thanh giằng $AB$ bằng $%s\\text{ m}$' % (fmt_num(CH))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Vì $OC \\perp AB$ tại $H$ nên khoảng cách từ tâm $O$ đến đường thẳng $AB$ là độ dài đoạn $OH$. \\\\ Ta có $OH = OC - CH = %s - %s = %s\\text{ m}$.'''
            % (fmt_num(R), fmt_num(CH), fmt_num(OH))
        )
        loigiai_th_1_s = (
            '''Sai. Vì $OC \\perp AB$ tại $H$ nên khoảng cách từ tâm $O$ đến $AB$ là $OH = OC - CH = %s - %s = %s\\text{ m}$ (khác $%s\\text{ m}$).'''
            % (fmt_num(R), fmt_num(CH), fmt_num(OH), fmt_num(CH))
        )

        # Vận dụng
        vd_da_1_d = '\\True Chiều dài thanh giằng thép $AB$ cần dùng là $%s\\text{ m}$' % (fmt_num(AB))
        vd_da_1_s = 'Chiều dài thanh giằng thép $AB$ cần dùng là $%s\\text{ m}$' % (fmt_num(AB_sai))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Trong tam giác cân $OAB$ ($OA = OB = R$), đường cao $OH$ đồng thời là đường trung tuyến nên $H$ là trung điểm của $AB$. \\\\ Áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta có: $HA = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ m}$. \\\\ Vậy chiều dài thanh giằng thép là $AB = 2 \\cdot HA = 2 \\cdot %s = %s\\text{ m}$.'''
            % (fmt_num(R), fmt_num(OH), fmt_num(HA), fmt_num(HA), fmt_num(AB))
        )
        loigiai_vd_1_s = (
            '''Sai. Áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta tính được $HA = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ m}$. \\\\ Suy ra chiều dài thanh giằng thép là $AB = 2 \\cdot HA = %s\\text{ m}$ (khác $%s\\text{ m}$).'''
            % (fmt_num(R), fmt_num(OH), fmt_num(HA), fmt_num(AB), fmt_num(AB_sai))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Tiếp tuyến của vòm cổng tại điểm cao nhất $C$ song song với thanh giằng $AB$'
        vdc_da_1_s = 'Tiếp tuyến của vòm cổng tại điểm cao nhất $C$ tạo với thanh giằng $AB$ một góc $45^\\circ$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Tiếp tuyến của vòm cổng tại $C$ vuông góc với bán kính $OC$ tại $C$. \\\\ Mặt khác, thanh giằng $AB$ cũng vuông góc với $OC$ tại $H$. Do đó tiếp tuyến tại $C$ song song với thanh giằng $AB$.'''
        )
        loigiai_vdc_1_s = (
            '''Sai. Tiếp tuyến của vòm cổng tại $C$ vuông góc với bán kính $OC$, mà thanh giằng $AB$ cũng vuông góc với $OC$ nên hai đường thẳng này song song với nhau.'''
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
