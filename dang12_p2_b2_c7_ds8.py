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


def bt_dang12_p2_b2_c7_ds8(self):
    # Dạng 12: Bài toán phân số khi thay đổi tử số và mẫu số
    d_mau, a, b, tu_ps, mau_ps, x_ans = random.choice([
        (7, 3, 2, 3, 4, 3),    # 3/10 -> (3+3)/(10-2) = 6/8 = 3/4
        (5, 2, 1, 2, 3, 6),    # 6/11 -> (6+2)/(11-1) = 8/10... (6+2)/(11-1)=8/10=4/5; sửa: 4/9 -> (4+2)/(9-1)=6/8=3/4
        (6, 4, 1, 4, 5, 16),   # 16/22 -> (16+4)/(22-1) = 20/21... chọn bộ chuẩn:
        (8, 2, 3, 2, 3, 8)     # 8/16 -> (8+2)/(16-3) = 10/13...
    ])
    # Bộ số chuẩn 100% chính xác:
    d_mau, a, b, tu_ps, mau_ps, x_ans = random.choice([
        (7, 3, 2, 3, 4, 3),    # (3+3)/(10-2) = 6/8 = 3/4
        (5, 2, 1, 3, 4, 4),    # (4+2)/(9-1) = 6/8 = 3/4
        (6, 1, 2, 2, 3, 5),    # (5+1)/(11-2) = 6/9 = 2/3
        (9, 4, 1, 2, 3, 6)     # (6+4)/(15-1) = 10/14 = 5/7 -> đổi (9, 1, 2, 2, 3, 9): (9+1)/(18-2) = 10/16 = 5/8; chọn (8, 1, 3, 2, 3, 7): (7+1)/(15-3) = 8/12 = 2/3
    ])
    if (d_mau, a, b, tu_ps, mau_ps, x_ans) == (9, 4, 1, 2, 3, 6):
        d_mau, a, b, tu_ps, mau_ps, x_ans = (8, 1, 3, 2, 3, 7)

    mau_moi_const = d_mau - b
    mau_ban_dau = x_ans + d_mau

    noidungcauhoi = "Một phân số có tử số bé hơn mẫu số là $%s$ đơn vị. Nếu tăng tử số thêm $%s$ đơn vị và giảm mẫu số đi $%s$ đơn vị thì được phân số mới bằng $\\dfrac{%s}{%s}$. Gọi $x$ là tử số của phân số ban đầu ($x \\in \\mathbb{Z}$, $x \\neq -%s$, $x \\neq -%s$). Xét tính đúng, sai của các khẳng định sau:" % (
        d_mau, a, b, tu_ps, mau_ps, d_mau, mau_moi_const
    )

    nb_da_1_d = '\\True Mẫu số của phân số ban đầu là $x + %s$.' % d_mau
    nb_da_1_s = 'Mẫu số của phân số ban đầu là $x - %s$.' % d_mau
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Vì tử số bé hơn mẫu số $%s$ đơn vị nên mẫu số của phân số ban đầu là $x + %s$.' % (d_mau, d_mau)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Phân số mới sau khi thay đổi tử số và mẫu số là $\\dfrac{x + %s}{x + %s}$.' % (a, mau_moi_const)
    th_da_1_s = 'Phân số mới sau khi thay đổi tử số và mẫu số là $\\dfrac{x + %s}{x + %s}$.' % (a, d_mau + b)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Tử số mới là $x + %s$, mẫu số mới là $(x + %s) - %s = x + %s$, nên phân số mới là $\\dfrac{x + %s}{x + %s}$.' % (
        a, d_mau, b, mau_moi_const, a, mau_moi_const
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Phương trình thu được sau khi quy đồng khử mẫu là $%s(x + %s) = %s(x + %s)$.' % (mau_ps, a, tu_ps, mau_moi_const)
    vd_da_1_s = 'Phương trình thu được sau khi quy đồng khử mẫu là $%s(x + %s) = %s(x + %s)$.' % (tu_ps, a, mau_ps, mau_moi_const)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Ta có $\\dfrac{x + %s}{x + %s} = \\dfrac{%s}{%s} \\Rightarrow %s(x + %s) = %s(x + %s)$.' % (
        a, mau_moi_const, tu_ps, mau_ps, mau_ps, a, tu_ps, mau_moi_const
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Phân số ban đầu cần tìm là $\\dfrac{%s}{%s}$.' % (x_ans, mau_ban_dau)
    vdc_da_1_s = 'Phân số ban đầu cần tìm là $\\dfrac{%s}{%s}$.' % (x_ans + 1, mau_ban_dau + 1)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Giải phương trình: $%sx + %s = %sx + %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn). Mẫu số ban đầu là $%s + %s = %s$. Vậy phân số ban đầu là $\\dfrac{%s}{%s}$.' % (
        mau_ps, mau_ps * a, tu_ps, tu_ps * mau_moi_const,
        mau_ps - tu_ps, tu_ps * mau_moi_const - mau_ps * a, x_ans,
        x_ans, d_mau, mau_ban_dau, x_ans, mau_ban_dau
    )
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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n'
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
