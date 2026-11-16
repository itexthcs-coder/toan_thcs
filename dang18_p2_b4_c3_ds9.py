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


def bt_dang18_p2_b4_c3_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        planets = [
            ("Sao Mộc", 11.86, 5.2),
            ("Sao Thổ", 29.46, 9.5),
            ("Sao Hỏa", 1.88, 1.5)
        ]
        p_name, T_val, R_r1 = random.choice(planets)
        T_str = str(T_val).replace('.', ',')
        R_r1_str = str(R_r1).replace('.', ',')
        R_r1_wrong_str = str(round(R_r1 + 0.3, 1)).replace('.', ',')

        R_hyp = random.choice([4, 9])
        T_hyp = int((R_hyp**3)**0.5)
        T_hyp_wrong = int(R_hyp * 1.5)

        noidungcauhoi = ('Trong thiên văn học, chu kì quay $T$ (tính bằng năm Trái Đất) của một hành tinh quanh Mặt Trời và khoảng cách trung bình $R$ (tính bằng đơn vị thiên văn AU) từ hành tinh đó đến Mặt Trời liên hệ với nhau bởi công thức $R = \\sqrt[3]{T^2}$. Xét tính đúng sai của các khẳng định sau:')

        nb_da_1_d = '\\True Đối với Trái Đất có chu kì quay $T = 1$ năm thì khoảng cách $R = 1\\text{ AU}$.'
        nb_da_1_s = 'Đối với Trái Đất có chu kì quay $T = 1$ năm thì khoảng cách $R = 3\\text{ AU}$.'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thay $T = 1$ vào công thức, ta được $R = \\sqrt[3]{1^2} = \\sqrt[3]{1} = 1\\text{ AU}$.')
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True %s có chu kì quay quanh Mặt Trời xấp xỉ $T = %s$ năm thì khoảng cách trung bình đến Mặt Trời là $R = \\sqrt[3]{(%s)^2}\\text{ AU}$.' % (p_name, T_str, T_str)
        th_da_1_s = '%s có chu kì quay quanh Mặt Trời xấp xỉ $T = %s$ năm thì khoảng cách trung bình đến Mặt Trời là $R = \\sqrt{(%s)^3}\\text{ AU}$.' % (p_name, T_str, T_str)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Thay $T = %s$ vào công thức $R = \\sqrt[3]{T^2}$, ta được $R = \\sqrt[3]{(%s)^2}\\text{ AU}$.' % (T_str, T_str))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Sử dụng máy tính cầm tay, khoảng cách trung bình từ %s đến Mặt Trời làm tròn đến chữ số thập phân thứ nhất là $%s\\text{ AU}$.' % (p_name, R_r1_str)
        vd_da_1_s = 'Sử dụng máy tính cầm tay, khoảng cách trung bình từ %s đến Mặt Trời làm tròn đến chữ số thập phân thứ nhất là $%s\\text{ AU}$.' % (p_name, R_r1_wrong_str)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Bấm máy tính cầm tay giá trị $\\sqrt[3]{(%s)^2}$ và làm tròn đến chữ số thập phân thứ nhất ta được $%s\\text{ AU}$.' % (T_str, R_r1_str))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Nếu một hành tinh giả định cách Mặt Trời $%s\\text{ AU}$ thì chu kì quay của nó quanh Mặt Trời là $%s$ năm.' % (R_hyp, T_hyp)
        vdc_da_1_s = 'Nếu một hành tinh giả định cách Mặt Trời $%s\\text{ AU}$ thì chu kì quay của nó quanh Mặt Trời là $%s$ năm.' % (R_hyp, T_hyp_wrong)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Ta có $\\sqrt[3]{T^2} = %s \\Rightarrow T^2 = %s^3 = %s$. Vì $T > 0$ nên $T = \\sqrt{%s} = %s$ năm.' % (R_hyp, R_hyp, R_hyp**3, R_hyp**3, T_hyp))
        list_vdc_2 = [loigiai_vdc_1]

        def count_true_answers(answers):
            return sum('\\True' in ans for ans in answers)

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break

        combined_nb = list(zip([nb_da_1], list_nb_2))
        combined_th = list(zip([th_da_1], list_th_2))
        combined_vd = list(zip([vd_da_1], list_vd_2))
        combined_vdc = list(zip([vdc_da_1], list_vdc_2))

        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

        content = ('\\begin{minipage}{\\textwidth} \n'
                   '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                   '\\choiceTFn \n'
                   '{' + str(shuffled_answers_nb[0]) + '}\n'
                   '{' + str(shuffled_answers_th[0]) + '}\n'
                   '{' + str(shuffled_answers_vd[0]) + '}\n'
                   '{' + str(shuffled_answers_vdc[0]) + '}\n'
                   '\\loigiai{ \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                   '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                   '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                   '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                   '\\end{enumEX}} \n'
                   '\\end{ex}\n \\end{minipage}\n\n')
        return content
