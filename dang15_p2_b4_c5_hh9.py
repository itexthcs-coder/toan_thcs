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

def bt_dang15_p2_b4_c5_hh9(self):
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
        # Dạng 15: Hai tiếp tuyến cắt nhau của đường tròn trong thiên văn – viễn thông (Tầm nhìn vệ tinh)
        bo_so = [
            (6400, 1600, 4800),
            (6400, 7200, 12000),
            (6400, 160, 1440),
            (6400, 2880, 6720)
        ]
        R, h_cao, SA = random.choice(bo_so)
        OS = R + h_cao
        SA_sai = SA + 800
        nua_OS = OS // 2
        oh_exact = sp.Rational(R * R, OS)
        oh_latex = sp.latex(oh_exact)

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (S) at (3.2,0);\n"
            "\\coordinate (A) at (0.8,1.386);\n"
            "\\coordinate (B) at (0.8,-1.386);\n"
            "\\draw[line width=1pt] (O) circle (1.6);\n"
            "\\draw[line width=1pt] (S)--(A) (S)--(B) (O)--(A) (O)--(B) (S)--(O) (A)--(B);\n"
            "\\draw[line width=1pt] (0.973,1.286)--(0.873,1.113)--(0.7,1.213);\n"
            "\\draw[line width=1pt] (0.973,-1.286)--(0.873,-1.113)--(0.7,-1.213);\n"
            "\\fill (O) circle (1pt) node[left] {$O$};\n"
            "\\fill (S) circle (1pt) node[right] {$S$};\n"
            "\\fill (A) circle (1pt) node[above] {$A$};\n"
            "\\fill (B) circle (1pt) node[below] {$B$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Xem Trái Đất là một hình cầu có mặt cắt qua tâm $O$ là đường tròn bán kính $R = %s\\text{ km}$. Một vệ tinh nhân tạo $S$ bay ở độ cao $h = %s\\text{ km}$ so với mặt đất (tức $OS = %s + %s = %s\\text{ km}$). Hai tia giới hạn vùng quan sát trên mặt cắt từ vệ tinh là hai tiếp tuyến $SA$, $SB$ kẻ đến đường tròn $(O)$.\n%s'''
            % (fmt_num(R), fmt_num(h_cao), fmt_num(R), fmt_num(h_cao), fmt_num(OS), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Hai đoạn thẳng giới hạn tầm nhìn $SA$ và $SB$ có độ dài bằng nhau'
        nb_da_1_s = 'Đoạn thẳng giới hạn tầm nhìn $SA$ luôn ngắn hơn đoạn thẳng $SB$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì $SA$ và $SB$ là hai tiếp tuyến của đường tròn $(O)$ cắt nhau tại $S$ nên theo tính chất hai tiếp tuyến cắt nhau, điểm $S$ cách đều hai tiếp điểm $A$ và $B$, tức là $SA = SB$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Theo tính chất hai tiếp tuyến cắt nhau tại $S$, hai đoạn tiếp tuyến $SA$ và $SB$ luôn có độ dài bằng nhau ($SA = SB$).'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Tia $SO$ là tia phân giác của góc quan sát $\\widehat{ASB}$ của vệ tinh'
        th_da_1_s = 'Tia $SO$ vuông góc với tia giới hạn tầm nhìn $SA$ tại $S$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Theo tính chất hai tiếp tuyến cắt nhau, $SO$ là tia phân giác của góc tạo bởi hai tiếp tuyến $\\widehat{ASB}$.'''
        )
        loigiai_th_1_s = (
            '''Sai. Tia $SO$ là tia phân giác của góc $\\widehat{ASB}$, còn bán kính $OA$ mới vuông góc với tiếp tuyến $SA$ tại tiếp điểm $A$.'''
        )

        # Vận dụng
        vd_da_1_d = '\\True Tầm nhìn thẳng tối đa từ vệ tinh $S$ đến đường chân trời Trái Đất (đoạn $SA$) bằng $%s\\text{ km}$' % (fmt_num(SA))
        vd_da_1_s = 'Tầm nhìn thẳng tối đa từ vệ tinh $S$ đến đường chân trời Trái Đất (đoạn $SA$) bằng $%s\\text{ km}$' % (fmt_num(SA_sai))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Vì $SA$ tiếp xúc với đường tròn $(O)$ tại $A$ nên $OA \\perp SA$, suy ra tam giác $OAS$ vuông tại $A$. \\\\ Áp dụng định lí Pythagore vào tam giác $OAS$ vuông tại $A$, ta có: $SA = \\sqrt{OS^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ km}$.'''
            % (fmt_num(OS), fmt_num(R), fmt_num(SA))
        )
        loigiai_vd_1_s = (
            '''Sai. Áp dụng định lí Pythagore vào tam giác $OAS$ vuông tại $A$, ta tính được: $SA = \\sqrt{OS^2 - OA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ km}$ (khác $%s\\text{ km}$).'''
            % (fmt_num(OS), fmt_num(R), fmt_num(SA), fmt_num(SA_sai))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Đoạn thẳng nối hai tiếp điểm $A$ và $B$ vuông góc với đường thẳng $OS$'
        vdc_da_1_s = 'Đoạn thẳng nối hai tiếp điểm $A$ và $B$ đi qua trung điểm của đoạn thẳng $OS$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Theo tính chất hai tiếp tuyến cắt nhau, $OS$ là tia phân giác của góc $\\widehat{AOB}$. Trong tam giác cân $OAB$ ($OA = OB = R$), đường phân giác $OS$ đồng thời là đường cao nên $OS \\perp AB$.'''
        )
        loigiai_vdc_1_s = (
            '''Sai. Gọi $H$ là giao điểm của $AB$ và $OS$. Khi đó $AH$ là đường cao của tam giác $OAS$ vuông tại $A$, nên $OA^2 = OH \\cdot OS \\Rightarrow OH = \\frac{OA^2}{OS} = %s\\text{ km} \\neq \\frac{OS}{2} = %s\\text{ km}$. Do đó $AB$ không đi qua trung điểm của $OS$.'''
            % (oh_latex, fmt_num(nua_OS))
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
