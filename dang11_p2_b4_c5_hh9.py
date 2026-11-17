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

def bt_dang11_p2_b4_c5_hh9(self):
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
        # Dạng 11: Vị trí tương đối của đường thẳng và đường tròn trong thiết kế giao thông (Vòng xuyến)
        bo_so = [
            (12, 9, 15),
            (16, 12, 20),
            (15, 8, 17),
            (24, 7, 25),
            (8, 6, 10)
        ]
        d_cat, h_cat, R = random.choice(bo_so)
        d_ngoai = R + 3
        day_cung = 2 * h_cat

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (H) at (0,0.9);\n"
            "\\coordinate (A) at (-1.2,0.9);\n"
            "\\coordinate (B) at (1.2,0.9);\n"
            "\\coordinate (T) at (0,-1.5);\n"
            "\\draw[line width=1pt] (O) circle (1.5);\n"
            "\\draw[line width=1pt] (-2.3,0.9)--(2.3,0.9);\n"
            "\\draw[line width=1pt] (-2.3,-1.5)--(2.3,-1.5);\n"
            "\\draw[line width=1pt] (-2.3,-2.1)--(2.3,-2.1);\n"
            "\\draw[line width=1pt, dashed] (O)--(H) (O)--(T) (O)--(A);\n"
            "\\fill (O) circle (1pt) node[left] {$O$};\n"
            "\\fill (H) circle (1pt) node[above right] {$H$};\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above right] {$B$};\n"
            "\\fill (T) circle (1pt) node[below] {$T$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Một vòng xuyến giao thông hình tròn có tâm $O$ và bán kính mép ngoài $R = %s\\text{ m}$. Một dải phân cách thẳng chạy ngang qua khu vực ngã tư, có khoảng cách ngắn nhất từ tâm vòng xuyến $O$ đến mép dải phân cách là $d$.\n%s'''
            % (fmt_num(R), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Nếu $d = %s\\text{ m}$ thì dải phân cách nằm hoàn toàn bên ngoài và không chạm vào vòng xuyến' % (fmt_num(d_ngoai))
        nb_da_1_s = 'Nếu $d = %s\\text{ m}$ thì mép dải phân cách tiếp xúc với vòng xuyến tại một điểm' % (fmt_num(d_ngoai))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Khi $d = %s\\text{ m} > R = %s\\text{ m}$, đường thẳng chứa mép dải phân cách và đường tròn biên của vòng xuyến không giao nhau nên dải phân cách nằm hoàn toàn bên ngoài vòng xuyến.'''
            % (fmt_num(d_ngoai), fmt_num(R))
        )
        loigiai_nb_1_s = (
            '''Sai. Khi $d = %s\\text{ m} > R = %s\\text{ m}$, đường thẳng chứa mép dải phân cách và đường tròn biên của vòng xuyến không giao nhau nên không có điểm chung nào.'''
            % (fmt_num(d_ngoai), fmt_num(R))
        )

        # Thông hiểu
        th_da_1_d = '\\True Nếu $d = %s\\text{ m}$ thì mép dải phân cách tiếp xúc với đường tròn biên của vòng xuyến tại đúng một điểm' % (fmt_num(R))
        th_da_1_s = 'Nếu $d = %s\\text{ m}$ thì mép dải phân cách cắt đường tròn biên của vòng xuyến tại hai điểm' % (fmt_num(R))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Khi $d = %s\\text{ m} = R$, đường thẳng chứa mép dải phân cách và đường tròn $(O; %s\\text{ m})$ tiếp xúc với nhau tại đúng một tiếp điểm.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_th_1_s = (
            '''Sai. Khi $d = %s\\text{ m} = R$, đường thẳng chứa mép dải phân cách tiếp xúc với đường tròn biên của vòng xuyến tại duy nhất một tiếp điểm.'''
            % (fmt_num(R))
        )

        # Vận dụng
        vd_da_1_d = '\\True Nếu $d = %s\\text{ m}$ thì mép dải phân cách cắt đường tròn biên của vòng xuyến theo một đoạn thẳng dài $%s\\text{ m}$' % (fmt_num(d_cat), fmt_num(day_cung))
        vd_da_1_s = 'Nếu $d = %s\\text{ m}$ thì mép dải phân cách cắt đường tròn biên của vòng xuyến theo một đoạn thẳng dài $%s\\text{ m}$' % (fmt_num(d_cat), fmt_num(h_cat))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Khi $d = %s\\text{ m} < R = %s\\text{ m}$, mép dải phân cách cắt đường tròn $(O)$ tại hai điểm $A$, $B$. \\\\ Kẻ $OH \\perp AB$ tại $H$, ta có $OH = %s\\text{ m}$ và $H$ là trung điểm của $AB$. \\\\ Áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta có: $HA = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ m}$. \\\\ Vậy chiều dài đoạn thẳng cắt qua vòng xuyến là $AB = 2 \\cdot HA = 2 \\cdot %s = %s\\text{ m}$.'''
            % (fmt_num(d_cat), fmt_num(R), fmt_num(d_cat), fmt_num(R), fmt_num(d_cat), fmt_num(h_cat), fmt_num(h_cat), fmt_num(day_cung))
        )
        loigiai_vd_1_s = (
            '''Sai. Khi $d = %s\\text{ m} < R = %s\\text{ m}$, kẻ $OH \\perp AB$ tại $H$, áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$ ta tính được $HA = \\sqrt{%s^2 - %s^2} = %s\\text{ m}$. \\\\ Do đó đoạn thẳng cắt qua vòng xuyến dài $AB = 2 \\cdot HA = %s\\text{ m}$ (khác $%s\\text{ m}$).'''
            % (fmt_num(d_cat), fmt_num(R), fmt_num(R), fmt_num(d_cat), fmt_num(h_cat), fmt_num(day_cung), fmt_num(h_cat))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Để mép dải phân cách không cắt qua phần bên trong vòng xuyến thì khoảng cách $d$ phải thỏa mãn $d \\ge %s\\text{ m}$' % (fmt_num(R))
        vdc_da_1_s = 'Để mép dải phân cách không cắt qua phần bên trong vòng xuyến thì khoảng cách $d$ phải thỏa mãn $d < %s\\text{ m}$' % (fmt_num(R))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Mép dải phân cách không cắt qua phần bên trong vòng xuyến khi đường thẳng chứa nó tiếp xúc hoặc không giao nhau với đường tròn $(O; %s\\text{ m})$, tức là khoảng cách $d \\ge R = %s\\text{ m}$.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_vdc_1_s = (
            '''Sai. Nếu $d < %s\\text{ m}$ thì đường thẳng sẽ cắt đường tròn $(O; %s\\text{ m})$ tại hai điểm và đi xuyên qua phần bên trong vòng xuyến. Điều kiện đúng phải là $d \\ge %s\\text{ m}$.'''
            % (fmt_num(R), fmt_num(R), fmt_num(R))
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
