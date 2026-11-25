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


def bt_dang1_p2_b2_c6_ds8(self):
    # Dạng 1: Kiểm tra tính đúng/sai của các phép biến đổi bằng tính chất cơ bản của phân thức
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a = random.choice([2, 3, 4, 5])
        b = random.choice([1, 2, 3, 4])
        while a == b:
            b = random.choice([1, 2, 3, 4])
        c = random.choice([2, 3, 4])

        tu_goc = latex(x - a)
        mau_goc = latex(x + b)
        tu_nhan = latex(expand((x - a) * (x - b)))
        mau_nhan = latex(expand((x + b) * (x - b)))
        tu_doi = latex(a - x)
        mau_doi = latex(-x - b)
        tu_cong = latex(x - a + c)
        mau_cong = latex(x + b + c)

        noidungcauhoi = ('Cho phân thức $P = \\dfrac{%s}{%s}$ (với $x \\neq %s$). Xét tính đúng sai của các khẳng định sau:' % (tu_goc, mau_goc, -b))

        # Ý a
        nb_da_1_d = '\\True Nhân cả tử và mẫu của $P$ với $%s$ (với $x \\neq %s$) ta được phân thức $\\dfrac{%s}{%s}$' % (latex(x - b), b, tu_nhan, mau_nhan)
        nb_da_1_s = 'Nhân cả tử và mẫu của $P$ với $%s$ (với $x \\neq %s$) ta được phân thức $\\dfrac{%s}{%s}$' % (latex(x - b), b, tu_goc, mau_nhan)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Áp dụng tính chất nhân cả tử và mẫu với cùng một đa thức khác $0$: $\\dfrac{%s}{%s} = \\dfrac{(%s)(%s)}{(%s)(%s)} = \\dfrac{%s}{%s}$.' % (tu_goc, mau_goc, tu_goc, latex(x - b), mau_goc, latex(x - b), tu_nhan, mau_nhan))
        list_nb_2 = [loigiai_nb_1]

        # Ý b
        th_da_1_d = '\\True Cộng cả tử và mẫu của $P$ với $%s$ ta không được phân thức mới bằng phân thức $P$' % c
        th_da_1_s = 'Cộng cả tử và mẫu của $P$ với $%s$ ta được phân thức $\\dfrac{%s}{%s}$ bằng phân thức $P$' % (c, tu_cong, mau_cong)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Tính chất cơ bản của phân thức chỉ áp dụng cho phép nhân hoặc phép chia cả tử và mẫu với cùng một đa thức khác $0$, không áp dụng cho phép cộng. Ta thấy $(%s)(%s) \\neq (%s)(%s)$ nên hai phân thức không bằng nhau.' % (tu_goc, mau_cong, mau_goc, tu_cong))
        list_th_2 = [loigiai_th_1]

        # Ý c
        vd_da_1_d = '\\True Đổi dấu cả tử và mẫu của $P$ ta được phân thức $\\dfrac{%s}{%s}$' % (tu_doi, mau_doi)
        vd_da_1_s = 'Đổi dấu cả tử và mẫu của $P$ ta được phân thức $\\dfrac{%s}{%s}$' % (tu_doi, mau_goc)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Áp dụng quy tắc đổi dấu cả tử và mẫu: $\\dfrac{%s}{%s} = \\dfrac{-(%s)}{-(%s)} = \\dfrac{%s}{%s}$.' % (tu_goc, mau_goc, tu_goc, mau_goc, tu_doi, mau_doi))
        list_vd_2 = [loigiai_vd_1]

        # Ý d
        vdc_da_1_d = '\\True Đổi dấu tử thức của $P$ và giữ nguyên mẫu thức thì được phân thức đối của $P$'
        vdc_da_1_s = 'Nhân tử thức của $P$ với $-1$ và giữ nguyên mẫu thức ta được phân thức $\\dfrac{%s}{%s}$ bằng phân thức $P$' % (tu_doi, mau_goc)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Nếu chỉ đổi dấu tử thức mà giữ nguyên mẫu thức thì ta được phân thức mới là phân thức đối của phân thức ban đầu, không bằng phân thức ban đầu.')
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

    # Xuất câu hỏi trắc nghiệm đúng sai
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
