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

def bt_dang14_p2_b4_c5_hh9(self):
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
        # Dạng 14: Vị trí tương đối của đường thẳng và đường tròn trong hàng hải (Vùng phủ sóng hải đăng)
        bo_so = [
            (15, 20, 25, 20),
            (12, 16, 20, 16),
            (9, 12, 15, 12),
            (8, 15, 17, 20),
            (7, 24, 25, 24),
            (6, 8, 10, 16)
        ]
        d_val, h_val, R, van_toc = random.choice(bo_so)
        quang_duong = 2 * h_val
        thoi_gian = round(quang_duong / van_toc, 4)
        thoi_gian_sai = round(thoi_gian - 0.5, 4)

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (H) at (0,0.9);\n"
            "\\coordinate (A) at (-1.2,0.9);\n"
            "\\coordinate (B) at (1.2,0.9);\n"
            "\\draw[line width=1pt] (O) circle (1.5);\n"
            "\\draw[line width=1pt] (-2.3,0.9)--(2.3,0.9) node[above] {$\\Delta$};\n"
            "\\draw[line width=1pt, dashed] (O)--(H) (O)--(A) (O)--(B);\n"
            "\\draw[line width=1pt] (0,0.7)--(0.2,0.7)--(0.2,0.9);\n"
            "\\fill (O) circle (1pt) node[below] {$O$};\n"
            "\\fill (H) circle (1pt) node[above right] {$H$};\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above right] {$B$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Một ngọn hải đăng đặt tại đảo $O$ phát tín hiệu cảnh báo trong vùng hình tròn bán kính $R = %s\\text{ km}$. Một con tàu chạy theo một tuyến đường thẳng $\\Delta$ đi qua vị trí cách đảo $O$ một khoảng ngắn nhất bằng $%s\\text{ km}$.\n%s'''
            % (fmt_num(R), fmt_num(d_val), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Tuyến đường thẳng $\\Delta$ của con tàu cắt đường tròn giới hạn vùng phủ sóng của hải đăng theo một dây cung'
        nb_da_1_s = 'Tuyến đường thẳng $\\Delta$ của con tàu không đi vào vùng phủ sóng của hải đăng'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Khoảng cách từ tâm $O$ đến đường thẳng $\\Delta$ là $d = %s\\text{ km} < R = %s\\text{ km}$ nên đường thẳng $\\Delta$ cắt đường tròn $(O; %s\\text{ km})$ tại hai điểm phân biệt $A$, $B$ tạo thành một dây cung.'''
            % (fmt_num(d_val), fmt_num(R), fmt_num(R))
        )
        loigiai_nb_1_s = (
            '''Sai. Vì khoảng cách từ tâm $O$ đến đường thẳng $\\Delta$ là $d = %s\\text{ km} < R = %s\\text{ km}$ nên đường thẳng $\\Delta$ cắt đường tròn $(O; %s\\text{ km})$ tại hai điểm phân biệt, tức là tàu đi xuyên qua vùng phủ sóng.'''
            % (fmt_num(d_val), fmt_num(R), fmt_num(R))
        )

        # Thông hiểu
        th_da_1_d = '\\True Nếu con tàu chuyển hướng đi theo một đường thẳng tiếp xúc với vùng phủ sóng thì khoảng cách ngắn nhất từ tàu đến đảo $O$ là $%s\\text{ km}$' % (fmt_num(R))
        th_da_1_s = 'Nếu con tàu chuyển hướng đi theo một đường thẳng tiếp xúc với vùng phủ sóng thì khoảng cách ngắn nhất từ tàu đến đảo $O$ là $%s\\text{ km}$' % (fmt_num(d_val))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Khi tuyến đường của tàu là một tiếp tuyến của đường tròn $(O; %s\\text{ km})$ thì khoảng cách từ tâm $O$ đến đường thẳng đó bằng đúng bán kính $R = %s\\text{ km}$.'''
            % (fmt_num(R), fmt_num(R))
        )
        loigiai_th_1_s = (
            '''Sai. Khi tuyến đường của tàu tiếp xúc với đường tròn $(O; %s\\text{ km})$ thì khoảng cách ngắn nhất từ đảo $O$ đến tuyến đường đó phải bằng bán kính $R = %s\\text{ km}$ (khác $%s\\text{ km}$).'''
            % (fmt_num(R), fmt_num(R), fmt_num(d_val))
        )

        # Vận dụng
        vd_da_1_d = '\\True Quãng đường con tàu di chuyển nằm trong vùng nhận được tín hiệu của hải đăng dài $%s\\text{ km}$' % (fmt_num(quang_duong))
        vd_da_1_s = 'Quãng đường con tàu di chuyển nằm trong vùng nhận được tín hiệu của hải đăng dài $%s\\text{ km}$' % (fmt_num(h_val))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Gọi $A$, $B$ là hai giao điểm của $\\Delta$ với đường tròn $(O; %s\\text{ km})$ và $H$ là chân đường vuông góc hạ từ $O$ xuống $\\Delta$. \\\\ Khi đó $OH = %s\\text{ km}$ và $H$ là trung điểm của dây cung $AB$. \\\\ Áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta có: $HA = \\sqrt{OA^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ km}$. \\\\ Vậy quãng đường tàu ở trong vùng phủ sóng là $AB = 2 \\cdot HA = 2 \\cdot %s = %s\\text{ km}$.'''
            % (fmt_num(R), fmt_num(d_val), fmt_num(R), fmt_num(d_val), fmt_num(h_val), fmt_num(h_val), fmt_num(quang_duong))
        )
        loigiai_vd_1_s = (
            '''Sai. Kẻ $OH \\perp AB$ tại $H$, áp dụng định lí Pythagore vào tam giác $OHA$ vuông tại $H$, ta tính được $HA = \\sqrt{%s^2 - %s^2} = %s\\text{ km}$. \\\\ Do đó quãng đường con tàu ở trong vùng phủ sóng là $AB = 2 \\cdot HA = %s\\text{ km}$ (khác $%s\\text{ km}$).'''
            % (fmt_num(R), fmt_num(d_val), fmt_num(h_val), fmt_num(quang_duong), fmt_num(h_val))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Với vận tốc không đổi $%s\\text{ km/h}$, thời gian con tàu ở trong vùng phủ sóng trên tuyến $\\Delta$ là $%s$ giờ' % (fmt_num(van_toc), fmt_num(thoi_gian))
        vdc_da_1_s = 'Với vận tốc không đổi $%s\\text{ km/h}$, thời gian con tàu ở trong vùng phủ sóng trên tuyến $\\Delta$ là $%s$ giờ' % (fmt_num(van_toc), fmt_num(thoi_gian_sai))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Với vận tốc không đổi $v = %s\\text{ km/h}$ trên quãng đường $AB = %s\\text{ km}$, thời gian con tàu ở trong vùng phủ sóng là $t = \\frac{AB}{v} = \\frac{%s}{%s} = %s$ giờ.'''
            % (fmt_num(van_toc), fmt_num(quang_duong), fmt_num(quang_duong), fmt_num(van_toc), fmt_num(thoi_gian))
        )
        loigiai_vdc_1_s = (
            '''Sai. Thời gian con tàu đi hết quãng đường $AB = %s\\text{ km}$ với vận tốc $%s\\text{ km/h}$ là $t = \\frac{AB}{v} = \\frac{%s}{%s} = %s$ giờ (khác $%s$ giờ).'''
            % (fmt_num(quang_duong), fmt_num(van_toc), fmt_num(quang_duong), fmt_num(van_toc), fmt_num(thoi_gian), fmt_num(thoi_gian_sai))
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
