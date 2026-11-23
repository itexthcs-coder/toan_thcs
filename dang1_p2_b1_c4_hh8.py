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


def bt_dang1_p2_b1_c4_hh8(self):
    # Khai báo biến
    a = random.randint(2, 5)
    b = random.randint(a + 1, 7)
    while math.gcd(a, b) != 1:
        b = random.randint(a + 1, 7)
    k1 = random.randint(3, 6)
    ab = a * k1
    cd = b * k1
    ef_dm = random.choice([2, 3, 4])
    ef_cm = ef_dm * 10
    gh = (ef_cm * b) // a
    while (ef_cm * b) % a != 0:
        ef_dm = random.choice([2, 3, 4, 6])
        ef_cm = ef_dm * 10
        gh = (ef_cm * b) // a
    d_add = random.randint(4, 8)
    ts1 = Rational(a, b)
    ts_sai_b = Rational(ef_dm, gh)
    ts_moi = Rational(ab + d_add, cd + d_add)

    noidungcauhoi = ("""Cho bốn đoạn thẳng $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$, $EF = %s\\text{ dm}$ và $GH = %s\\text{ cm}$. Xét tính đúng, sai của các khẳng định sau:"""
                     % (ab, cd, ef_dm, gh))

    # Mệnh đề a (Nhận biết)
    nb_da_1_d = '\\True Tỉ số của hai đoạn thẳng $AB$ và $CD$ là $%s$' % (latex(ts1))
    nb_da_1_s = 'Tỉ số của hai đoạn thẳng $AB$ và $CD$ là $%s$' % (latex(Rational(b, a)))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì hai đoạn thẳng $AB$ và $CD$ đã có cùng đơn vị đo là $\\text{cm}$ nên tỉ số của chúng là $\\dfrac{AB}{CD} = \\dfrac{%s}{%s} = %s$."""
                    % (ab, cd, latex(ts1)))

    # Mệnh đề b (Thông hiểu)
    th_da_1_d = '\\True Tỉ số của hai đoạn thẳng $EF$ và $GH$ là $%s$' % (latex(ts1))
    th_da_1_s = 'Tỉ số của hai đoạn thẳng $EF$ và $GH$ là $%s$' % (latex(ts_sai_b))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Đổi đơn vị: $EF = %s\\text{ dm} = %s\\text{ cm}$. \\\\ Tỉ số của hai đoạn thẳng $EF$ và $GH$ là $\\dfrac{EF}{GH} = \\dfrac{%s}{%s} = %s$."""
                    % (ef_dm, ef_cm, ef_cm, gh, latex(ts1)))

    # Mệnh đề c (Vận dụng)
    vd_da_1_d = '\\True Hai đoạn thẳng $AB$ và $CD$ tỉ lệ với hai đoạn thẳng $EF$ và $GH$'
    vd_da_1_s = 'Hai đoạn thẳng $AB$ và $CD$ không tỉ lệ với hai đoạn thẳng $EF$ và $GH$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Ta có $\\dfrac{AB}{CD} = %s$ và $\\dfrac{EF}{GH} = %s$, suy ra $\\dfrac{AB}{CD} = \\dfrac{EF}{GH}$. \\\\ Vậy hai đoạn thẳng $AB$ và $CD$ tỉ lệ với hai đoạn thẳng $EF$ và $GH$."""
                    % (latex(ts1), latex(ts1)))

    # Mệnh đề d (Vận dụng cao)
    vdc_da_1_d = '\\True Nếu kéo dài mỗi đoạn thẳng $AB$ và $CD$ thêm $%s\\text{ cm}$ thì tỉ số của hai đoạn thẳng mới bằng $%s$' % (d_add, latex(ts_moi))
    vdc_da_1_s = 'Nếu kéo dài mỗi đoạn thẳng $AB$ và $CD$ thêm $%s\\text{ cm}$ thì tỉ số của hai đoạn thẳng mới vẫn bằng tỉ số ban đầu' % (d_add)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Khi kéo dài mỗi đoạn thẳng $AB$ và $CD$ thêm $%s\\text{ cm}$ thì độ dài hai đoạn thẳng mới lần lượt là $%s + %s = %s\\text{ (cm)}$ và $%s + %s = %s\\text{ (cm)}$. \\\\ Tỉ số mới là $\\dfrac{%s}{%s} = %s \\neq %s$."""
                     % (d_add, ab, d_add, ab + d_add, cd, d_add, cd + d_add, ab + d_add, cd + d_add, latex(ts_moi), latex(ts1)))

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
