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

def bt_dang2_p2_b4_c5_hh9(self):
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
        # Dạng 2: Nhận biết tiếp tuyến của đường tròn thông qua quan hệ vuông góc với bán kính tại tiếp điểm
        bo_so = [
            (6, 8, 10),
            (5, 12, 13),
            (8, 15, 17),
            (9, 12, 15),
            (12, 16, 20),
            (7, 24, 25)
        ]
        AB, AC, BC = random.choice(bo_so)
        khoang_cach_sai = AC

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (A) at (0,0);\n"
            "\\coordinate (B) at (0,1.6);\n"
            "\\coordinate (C) at (2.4,0);\n"
            "\\draw[line width=1pt] (B) circle (1.6);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--cycle;\n"
            "\\draw[line width=1pt] (-0.8,0)--(3.0,0);\n"
            "\\draw[line width=1pt] (0,0.2)--(0.2,0.2)--(0.2,0);\n"
            "\\fill (A) circle (1pt) node[below left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above left] {$B$};\n"
            "\\fill (C) circle (1pt) node[below right] {$C$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho tam giác $ABC$ vuông tại $A$ có $AB = %s\\text{ cm}$, $AC = %s\\text{ cm}$. Vẽ đường tròn $(B; BA)$.\n%s'''
            % (fmt_num(AB), fmt_num(AC), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Đường thẳng $AC$ là tiếp tuyến của đường tròn $(B; BA)$ tại tiếp điểm $A$'
        nb_da_1_s = 'Đường thẳng $AC$ cắt đường tròn $(B; BA)$ tại hai điểm phân biệt'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Điểm $A$ nằm trên đường tròn $(B; BA)$ và đường thẳng $AC$ vuông góc với bán kính $BA$ tại $A$ (do tam giác $ABC$ vuông tại $A$). Theo dấu hiệu nhận biết tiếp tuyến, đường thẳng $AC$ là tiếp tuyến của đường tròn $(B; BA)$ tại tiếp điểm $A$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Vì $AC \\perp BA$ tại $A$ và $A$ nằm trên đường tròn $(B; BA)$ nên $AC$ là tiếp tuyến của đường tròn $(B; BA)$, do đó chúng chỉ có duy nhất một điểm chung là tiếp điểm $A$.'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Khoảng cách từ tâm $B$ đến đường thẳng $AC$ bằng $%s\\text{ cm}$' % (fmt_num(AB))
        th_da_1_s = 'Khoảng cách từ tâm $B$ đến đường thẳng $AC$ bằng $%s\\text{ cm}$' % (fmt_num(khoang_cach_sai))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Vì tam giác $ABC$ vuông tại $A$ nên $BA \\perp AC$ tại $A$. Do đó khoảng cách từ tâm $B$ đến đường thẳng $AC$ chính là độ dài đoạn thẳng $BA = %s\\text{ cm}$.'''
            % (fmt_num(AB))
        )
        loigiai_th_1_s = (
            '''Sai. Vì $BA \\perp AC$ tại $A$ nên khoảng cách từ tâm $B$ đến đường thẳng $AC$ bằng độ dài đoạn $BA = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(AB), fmt_num(khoang_cach_sai))
        )

        # Vận dụng
        vd_da_1_d = '\\True Đường thẳng $BC$ cắt đường tròn $(B; BA)$ tại hai điểm phân biệt'
        vd_da_1_s = 'Đường thẳng $BC$ không giao nhau với đường tròn $(B; BA)$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Vì đường thẳng $BC$ đi qua tâm $B$ của đường tròn $(B; BA)$ nên khoảng cách từ tâm $B$ đến đường thẳng $BC$ bằng $0\\text{ cm} < BA = %s\\text{ cm}$. Vậy đường thẳng $BC$ cắt đường tròn $(B; BA)$ tại hai điểm phân biệt.'''
            % (fmt_num(AB))
        )
        loigiai_vd_1_s = (
            '''Sai. Đường thẳng $BC$ đi qua tâm $B$ của đường tròn $(B; BA)$ nên đường thẳng $BC$ luôn cắt đường tròn $(B; BA)$ tại hai điểm phân biệt là hai đầu mút của một đường kính.'''
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Nếu vẽ thêm đường tròn $(C; CA)$ thì đường thẳng $AB$ là tiếp tuyến của đường tròn $(C; CA)$'
        vdc_da_1_s = 'Nếu vẽ thêm đường tròn $(C; CA)$ thì đường thẳng $BC$ là tiếp tuyến chung của cả hai đường tròn $(B; BA)$ và $(C; CA)$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Điểm $A$ nằm trên đường tròn $(C; CA)$ và đường thẳng $AB$ vuông góc với bán kính $CA$ tại $A$ (do $\\widehat{BAC} = 90^\\circ$). Theo dấu hiệu nhận biết tiếp tuyến, đường thẳng $AB$ là tiếp tuyến của đường tròn $(C; CA)$ tại tiếp điểm $A$.'''
        )
        loigiai_vdc_1_s = (
            '''Sai. Đường thẳng $BC$ đi qua tâm $B$ của đường tròn $(B; BA)$ và đi qua tâm $C$ của đường tròn $(C; CA)$ nên $BC$ cắt cả hai đường tròn tại hai điểm phân biệt, không phải tiếp tuyến chung.'''
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
