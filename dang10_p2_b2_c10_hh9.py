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


def bt_dang10_p2_b2_c10_hh9(self):
    R = 3
    h_tru = randint(4, 8)
    h_non = 4
    l_non = 5
    V_nuacau = Rational(2, 3) * R**3
    V_tru = R**2 * h_tru
    V_non = Rational(1, 3) * R**2 * h_non
    V_tong = V_nuacau + V_tru + V_non
    S_ngoai = 2 * R**2 + 2 * R * h_tru + R * l_non

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-1,0) arc (180:360:1cm and 0.3cm);
\\draw[line width=1pt, dashed] (1,0) arc (0:180:1cm and 0.3cm);
\\draw[line width=1pt] (-1,1.8) arc (180:360:1cm and 0.3cm);
\\draw[line width=1pt, dashed] (1,1.8) arc (0:180:1cm and 0.3cm);
\\draw[line width=1pt] (-1,0)--(-1,1.8) (1,0)--(1,1.8);
\\draw[line width=1pt] (1,1.8) arc (0:180:1cm);
\\draw[line width=1pt] (-1,0)--(0,-1.4)--(1,0);
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Một khối hình học $(T)$ gồm ba phần có cùng bán kính đáy $R = %s\\text{ cm}$: phần trên cùng là nửa hình cầu, phần ở giữa là hình trụ có chiều cao $h_1 = %s\\text{ cm}$ và phần dưới cùng là hình nón có chiều cao $h_2 = %s\\text{ cm}$.%s''' % (R, h_tru, h_non, hinh_ve))

    nb_da_1_d = '\\True Độ dài đường sinh của hình nón phía dưới bằng $%s\\text{ cm}$' % (l_non)
    nb_da_1_s = 'Độ dài đường sinh của hình nón phía dưới bằng $%s\\text{ cm}$' % (h_non + R)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Đường sinh của hình nón là $l = \\sqrt{R^2 + h_2^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.''' % (R, h_non, l_non))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Tổng thể tích của phần nửa hình cầu và phần hình nón bằng $%s\\pi\\text{ cm}^3$' % latex(V_nuacau + V_non)
    th_da_1_s = 'Tổng thể tích của phần nửa hình cầu và phần hình nón bằng $%s\\pi\\text{ cm}^3$' % latex(V_nuacau + 3 * V_non)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $V_{\\text{nửa cầu}} = \\dfrac{2}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$ và $V_{\\text{nón}} = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$. Tổng của chúng là $%s\\pi\\text{ (cm}^3\\text{)}$.''' % (R, latex(V_nuacau), R, h_non, latex(V_non), latex(V_nuacau + V_non)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Thể tích của cả khối hình học $(T)$ bằng $%s\\pi\\text{ cm}^3$' % latex(V_tong)
    vd_da_1_s = 'Thể tích của cả khối hình học $(T)$ bằng $%s\\pi\\text{ cm}^3$' % latex(V_tong + V_tru)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Thể tích hình trụ là $V_{\\text{trụ}} = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$. Vậy $V_{(T)} = %s\\pi + %s\\pi = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (R, h_tru, V_tru, latex(V_nuacau + V_non), V_tru, latex(V_tong)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Diện tích bề mặt ngoài của khối hình học $(T)$ bằng $%s\\pi\\text{ cm}^2$' % (S_ngoai)
    vdc_da_1_s = 'Diện tích bề mặt ngoài của khối hình học $(T)$ bằng $%s\\pi\\text{ cm}^2$' % (S_ngoai + 2 * R**2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Diện tích bề mặt ngoài là $S = 2\\pi R^2 + 2\\pi R h_1 + \\pi R l = 2\\pi \\cdot %s^2 + 2\\pi \\cdot %s \\cdot %s + \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (R, R, h_tru, R, l_non, S_ngoai))
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
               '\\end{ex}\n \end{minipage}\n\n')
    return content
