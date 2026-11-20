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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang14_p2_b3_c1_ds8(self):
    # Khai báo biến
    x, y = symbols('x y')

    a1 = random.choice([4, 5, 6])
    b1 = random.choice([-5, -4])
    c1 = random.choice([3, 4, 5])

    a2 = random.choice([1, 2])
    b2 = random.choice([-3, -2])
    c2 = random.choice([-2, -1])

    A = a1*x**2 + b1*x*y + c1*y**2
    B = a2*x**2 + b2*x*y + c2*y**2
    kq_dung = simplify(A - B)
    kq_sai = (a1 - a2)*x**2 + (b1 + b2)*x*y + (c1 + c2)*y**2

    noidungcauhoi = ('''Một học sinh thực hiện phép tính $H = (%s) - (%s)$ theo các bước sau:\\\\
\\textit{Bước 1:} $H = %s - %s %s %s$\\\\
\\textit{Bước 2:} $H = (%s - %s) + (%s %s) + (%s %s)$\\\\
\\textit{Bước 3:} $H = %s$.''' % (latex(A), latex(B),
                                        latex(A), latex(a2*x**2), latex(b2*x*y), latex(c2*y**2),
                                        latex(a1*x**2), latex(a2*x**2), latex(b1*x*y), latex(b2*x*y), latex(c1*y**2), latex(c2*y**2),
                                        latex(kq_sai)))

    ######################################################################## Nhận biết ############################################
    nb_da_1_d = '\\True Học sinh đó đã thực hiện sai ngay từ Bước 1.'
    nb_da_1_s = 'Học sinh đó thực hiện đúng Bước 1 nhưng tính toán sai ở Bước 3.'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ('''Học sinh đã bỏ dấu ngoặc có dấu "-" đằng trước ở Bước 1 nhưng không đổi dấu các hạng tử bên trong.''')
    list_nb_2 = [loigiai_nb_1]

    ######################################################################## Thông hiểu ############################################
    th_da_1_d = '\\True Lỗi sai của học sinh là không đổi dấu các hạng tử $%s$ và $%s$ khi bỏ dấu ngoặc.' % (latex(b2*x*y), latex(c2*y**2))
    th_da_1_s = 'Lỗi sai của học sinh là nhóm sai các hạng tử đồng dạng ở Bước 2.'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ('''Khi bỏ dấu ngoặc của $-(%s)$, ta phải đổi dấu thành $-%s + %s + %s$.''' % (latex(B), latex(a2*x**2), latex(abs(b2)*x*y), latex(abs(c2)*y**2)))
    list_th_2 = [loigiai_th_1]

    ######################################################################## Vận dụng ############################################
    vd_da_1_d = '\\True Kết quả đúng của phép tính $H$ phải là $%s$.' % (latex(kq_dung))
    vd_da_1_s = 'Kết quả đúng của phép tính $H$ phải là $%s$.' % (latex(kq_dung - 2*abs(c2)*y**2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ('''Thực hiện đúng: $H = (%s) - (%s) = %s$.''' % (latex(A), latex(B), latex(kq_dung)))
    list_vd_2 = [loigiai_vd_1]

    ######################################################################## Vận dụng cao ############################################
    vdc_da_1_d = '\\True Hiệu giữa kết quả đúng và kết quả sai của học sinh là $%s$.' % (latex(simplify(kq_dung - kq_sai)))
    vdc_da_1_s = 'Hiệu giữa kết quả đúng và kết quả sai của học sinh là $0$.'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ('''Ta có: $(%s) - (%s) = %s$.''' % (latex(kq_dung), latex(kq_sai), latex(simplify(kq_dung - kq_sai))))
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
