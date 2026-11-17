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

def bt_dang16_p2_b4_c5_hh9(self):
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
        # Dạng 16: Vị trí tương đối của đường tròn tâm là giao điểm hai đường chéo hình chữ nhật với các cạnh trong nghề mộc
        bo_so = [
            (20, 30),
            (15, 25),
            (25, 35),
            (30, 40),
            (18, 28)
        ]
        d_dai, d_ngan = random.choice(bo_so)
        rong = 2 * d_dai
        dai = 2 * d_ngan
        R_giua = (d_dai + d_ngan) // 2

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (A) at (-2.1,1.4);\n"
            "\\coordinate (B) at (2.1,1.4);\n"
            "\\coordinate (C) at (2.1,-1.4);\n"
            "\\coordinate (D) at (-2.1,-1.4);\n"
            "\\coordinate (O) at (0,0);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n"
            "\\draw[line width=1pt, dashed] (A)--(C) (B)--(D);\n"
            "\\draw[line width=1pt] (O) circle (1.4);\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above right] {$B$};\n"
            "\\fill (C) circle (1pt) node[below right] {$C$};\n"
            "\\fill (D) circle (1pt) node[below left] {$D$};\n"
            "\\fill (O) circle (1pt) node[below] {$O$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Bác thợ mộc có một tấm ván hình chữ nhật $ABCD$ kích thước $%s\\text{ cm} \\times %s\\text{ cm}$ ($AB = CD = %s\\text{ cm}$, $AD = BC = %s\\text{ cm}$). Bác vẽ một đường tròn tâm $O$ (là giao điểm hai đường chéo của tấm ván) để cắt ra một mặt bàn tròn nhỏ.\n%s'''
            % (fmt_num(rong), fmt_num(dai), fmt_num(dai), fmt_num(rong), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Khoảng cách từ tâm $O$ đến hai cạnh dài của tấm ván bằng $%s\\text{ cm}$, đến hai cạnh ngắn bằng $%s\\text{ cm}$' % (fmt_num(d_dai), fmt_num(d_ngan))
        nb_da_1_s = 'Khoảng cách từ tâm $O$ đến hai cạnh dài của tấm ván bằng $%s\\text{ cm}$, đến hai cạnh ngắn bằng $%s\\text{ cm}$' % (fmt_num(d_ngan), fmt_num(d_dai))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Giao điểm $O$ của hai đường chéo hình chữ nhật $ABCD$ cách đều hai cạnh dài $AB$, $CD$ một khoảng bằng nửa chiều rộng là $\\frac{%s}{2} = %s\\text{ cm}$ và cách đều hai cạnh ngắn $AD$, $BC$ một khoảng bằng nửa chiều dài là $\\frac{%s}{2} = %s\\text{ cm}$.'''
            % (fmt_num(rong), fmt_num(d_dai), fmt_num(dai), fmt_num(d_ngan))
        )
        loigiai_nb_1_s = (
            '''Sai. Tâm $O$ cách hai cạnh dài một khoảng bằng nửa chiều rộng $\\frac{%s}{2} = %s\\text{ cm}$ và cách hai cạnh ngắn một khoảng bằng nửa chiều dài $\\frac{%s}{2} = %s\\text{ cm}$.'''
            % (fmt_num(rong), fmt_num(d_dai), fmt_num(dai), fmt_num(d_ngan))
        )

        # Thông hiểu
        th_da_1_d = '\\True Đường tròn $(O; %s\\text{ cm})$ tiếp xúc với hai cạnh dài của tấm ván và không giao nhau với hai cạnh ngắn' % (fmt_num(d_dai))
        th_da_1_s = 'Đường tròn $(O; %s\\text{ cm})$ tiếp xúc với cả bốn cạnh của tấm ván' % (fmt_num(d_dai))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Đối với hai cạnh dài, khoảng cách từ $O$ đến mỗi cạnh là $d_1 = %s\\text{ cm} = R$ nên đường tròn $(O; %s\\text{ cm})$ tiếp xúc với hai cạnh dài. \\\\ Đối với hai cạnh ngắn, khoảng cách từ $O$ đến mỗi cạnh là $d_2 = %s\\text{ cm} > R = %s\\text{ cm}$ nên đường tròn không giao nhau với hai cạnh ngắn.'''
            % (fmt_num(d_dai), fmt_num(d_dai), fmt_num(d_ngan), fmt_num(d_dai))
        )
        loigiai_th_1_s = (
            '''Sai. Khoảng cách từ $O$ đến hai cạnh ngắn là $d_2 = %s\\text{ cm} > R = %s\\text{ cm}$ nên đường tròn $(O; %s\\text{ cm})$ chỉ tiếp xúc với hai cạnh dài và không giao nhau với hai cạnh ngắn.'''
            % (fmt_num(d_ngan), fmt_num(d_dai), fmt_num(d_dai))
        )

        # Vận dụng
        vd_da_1_d = '\\True Đường tròn $(O; %s\\text{ cm})$ cắt hai cạnh dài và không giao nhau với hai cạnh ngắn của tấm ván' % (fmt_num(R_giua))
        vd_da_1_s = 'Đường tròn $(O; %s\\text{ cm})$ cắt cả bốn cạnh của tấm ván' % (fmt_num(R_giua))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Với bán kính $R = %s\\text{ cm}$, ta có $d_1 = %s\\text{ cm} < R < d_2 = %s\\text{ cm}$. \\\\ Do đó đường tròn $(O; %s\\text{ cm})$ cắt hai đường thẳng chứa hai cạnh dài tại hai điểm phân biệt và không giao nhau với hai cạnh ngắn.'''
            % (fmt_num(R_giua), fmt_num(d_dai), fmt_num(d_ngan), fmt_num(R_giua))
        )
        loigiai_vd_1_s = (
            '''Sai. Vì $d_1 = %s\\text{ cm} < R = %s\\text{ cm} < d_2 = %s\\text{ cm}$ nên đường tròn $(O; %s\\text{ cm})$ chỉ cắt hai cạnh dài mà không giao nhau với hai cạnh ngắn.'''
            % (fmt_num(d_dai), fmt_num(R_giua), fmt_num(d_ngan), fmt_num(R_giua))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Đường tròn lớn nhất có tâm $O$ nằm trọn trong tấm ván có bán kính bằng $%s\\text{ cm}$' % (fmt_num(d_dai))
        vdc_da_1_s = 'Đường tròn lớn nhất có tâm $O$ nằm trọn trong tấm ván có bán kính bằng $%s\\text{ cm}$' % (fmt_num(d_ngan))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Để đường tròn tâm $O$ bán kính $R$ nằm trọn trong tấm ván hình chữ nhật thì đường tròn không được vượt ra ngoài cả bốn cạnh, tức là $R \\le d_1 = %s\\text{ cm}$ và $R \\le d_2 = %s\\text{ cm}$. \\\\ Suy ra $R \\le %s\\text{ cm}$, do đó bán kính lớn nhất có thể là $%s\\text{ cm}$.'''
            % (fmt_num(d_dai), fmt_num(d_ngan), fmt_num(d_dai), fmt_num(d_dai))
        )
        loigiai_vdc_1_s = (
            '''Sai. Nếu lấy bán kính bằng $%s\\text{ cm} > %s\\text{ cm}$ thì đường tròn sẽ cắt hai cạnh dài và tràn ra ngoài tấm ván. Bán kính lớn nhất để đường tròn nằm trọn trong tấm ván là $%s\\text{ cm}$.'''
            % (fmt_num(d_ngan), fmt_num(d_dai), fmt_num(d_dai))
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
