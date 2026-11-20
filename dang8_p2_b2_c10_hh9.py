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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang8_p2_b2_c10_hh9(self):
    R = random.choice([3, 6])
    h = randint(5, 10)
    V_tru = R**2 * h
    V_cau = Rational(4, 3) * R**3
    V_tong = V_tru + V_cau
    S_xq_tru = 2 * R * h
    S_cau = 4 * R**2
    S_tp = S_xq_tru + S_cau

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-1.8,0.9)--(1.8,0.9) (-1.8,-0.9)--(1.8,-0.9);
\\draw[line width=1pt] (-1.8,0.9) arc (90:270:0.9cm);
\\draw[line width=1pt] (1.8,-0.9) arc (-90:90:0.9cm);
\\draw[line width=1pt] (-1.8,0.9) arc (90:270:0.25cm and 0.9cm);
\\draw[line width=1pt, dashed] (-1.8,-0.9) arc (-90:90:0.25cm and 0.9cm);
\\draw[line width=1pt] (1.8,0.9) arc (90:270:0.25cm and 0.9cm);
\\draw[line width=1pt, dashed] (1.8,-0.9) arc (-90:90:0.25cm and 0.9cm);
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Một khối hình học $(H)$ được tạo thành bằng cách ghép hai nửa hình cầu có bán kính $R = %s\\text{ cm}$ vào hai đáy của một hình trụ có bán kính đáy $R = %s\\text{ cm}$ và chiều cao $h = %s\\text{ cm}$ như hình vẽ.%s''' % (R, R, h, hinh_ve))

    nb_da_1_d = '\\True Hai nửa hình cầu ở hai đầu ghép lại có tổng thể tích bằng thể tích của một hình cầu bán kính $R = %s\\text{ cm}$' % (R)
    nb_da_1_s = 'Thể tích của khối $(H)$ bằng tổng thể tích của hình trụ và hai hình cầu bán kính $R = %s\\text{ cm}$' % (R)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Hai nửa hình cầu có cùng bán kính $R = %s\\text{ cm}$ ghép lại tạo thành một hình cầu hoàn chỉnh bán kính $R = %s\\text{ cm}$.''' % (R, R))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Thể tích phần hình trụ ở giữa bằng $%s\\pi\\text{ cm}^3$' % (V_tru)
    th_da_1_s = 'Thể tích phần hình trụ ở giữa bằng $%s\\pi\\text{ cm}^3$' % (2 * R * h)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Thể tích hình trụ là $V_{\\text{trụ}} = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (R, h, V_tru))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Thể tích của cả khối hình học $(H)$ bằng $%s\\pi\\text{ cm}^3$' % latex(V_tong)
    vd_da_1_s = 'Thể tích của cả khối hình học $(H)$ bằng $%s\\pi\\text{ cm}^3$' % latex(V_tru + Rational(2, 3) * R**3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Thể tích hình cầu là $V_{\\text{cầu}} = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nThể tích khối $(H)$ là $V = V_{\\text{trụ}} + V_{\\text{cầu}} = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (R, latex(V_cau), V_tru, latex(V_cau), latex(V_tong)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Diện tích bề mặt ngoài của khối hình học $(H)$ bằng $%s\\pi\\text{ cm}^2$' % (S_tp)
    vdc_da_1_s = 'Diện tích bề mặt ngoài của khối hình học $(H)$ bằng $%s\\pi\\text{ cm}^2$' % (S_tp + 2 * R**2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Diện tích bề mặt ngoài gồm diện tích xung quanh hình trụ và diện tích mặt cầu: $S = 2\\pi R h + 4\\pi R^2 = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (S_xq_tru, S_cau, S_tp))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
