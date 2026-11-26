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


def bt_dang6_p2_b2_c7_ds8(self):
    # Dạng 6: Biến đổi và giải phương trình có hệ số thập phân
    c1, c2, a, b, nghiem = random.choice([
        (0.4, 0.25, 5, 4, 3),   # 0.4(x-5) + 0.25(2x+4) = 0.9x - 1 = 1.7 (x=3)
        (0.5, 0.2, 4, 5, 4),    # 0.5(x-4) + 0.2(2x+5) = 0.9x - 1 = 2.6 (x=4)
        (0.3, 0.35, 2, 2, 6),   # 0.3(x-2) + 0.35(2x+2) = 1.0x + 0.1 = 6.1 (x=6)
        (0.6, 0.2, 5, 5, 3)     # 0.6(x-5) + 0.2(2x+5) = 1.0x - 2 = 1.0 (x=3)
    ])
    hs_x = round(c1 + 2 * c2, 2)
    hang_tu = round(-c1 * a + c2 * b, 2)
    rhs = round(hs_x * nghiem + hang_tu, 2)

    s_c1 = str(c1).replace('.', ',')
    s_c2 = str(c2).replace('.', ',')
    s_rhs = str(rhs).replace('.', ',')
    s_hs_x = str(hs_x).replace('.', ',')
    dau_ht = "+" if hang_tu >= 0 else "-"
    s_ht = str(abs(hang_tu)).replace('.', ',')

    noidungcauhoi = "Cho phương trình $%s(x - %s) + %s(2x + %s) = %s$. Xét tính đúng, sai của các khẳng định sau:" % (
        s_c1, a, s_c2, b, s_rhs
    )

    nb_da_1_d = '\\True Khi nhân cả hai vế với $100$ để đưa về hệ số nguyên, ta được $%s(x - %s) + %s(2x + %s) = %s$.' % (
        int(round(c1 * 100)), a, int(round(c2 * 100)), b, int(round(rhs * 100))
    )
    nb_da_1_s = 'Khi nhân cả hai vế với $100$ để đưa về hệ số nguyên, ta được $%s(x - %s) + %s(2x + %s) = %s$.' % (
        int(round(c1 * 100)), a, int(round(c2 * 100)), b, int(round(rhs * 10))
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Nhân cả hai vế của phương trình với $100$, ta được: $%s(x - %s) + %s(2x + %s) = %s$.' % (
        int(round(c1 * 100)), a, int(round(c2 * 100)), b, int(round(rhs * 100))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Thu gọn vế trái của phương trình ban đầu ta được $%sx %s %s$.' % (s_hs_x, dau_ht, s_ht)
    th_da_1_s = 'Thu gọn vế trái của phương trình ban đầu ta được $%sx %s %s$.' % (s_hs_x, "-" if hang_tu >= 0 else "+", s_ht)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Khai triển vế trái: $%sx - %s + %sx + %s = %sx %s %s$.' % (
        s_c1, str(round(c1 * a, 2)).replace('.', ','),
        str(round(2 * c2, 2)).replace('.', ','), str(round(c2 * b, 2)).replace('.', ','),
        s_hs_x, dau_ht, s_ht
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nghiệm của phương trình đã cho là $x = %s$.' % nghiem
    vd_da_1_s = 'Nghiệm của phương trình đã cho là $x = %s$.' % (nghiem + 1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Ta có: $%sx %s %s = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$.' % (
        s_hs_x, dau_ht, s_ht, s_rhs, s_hs_x, str(round(hs_x * nghiem, 2)).replace('.', ','), nghiem
    )
    list_vd_2 = [loigiai_vd_1]

    if nghiem % 3 == 0:
        vdc_da_1_d = '\\True Nghiệm $x$ của phương trình chia hết cho $3$.'
        vdc_da_1_s = 'Nghiệm $x$ của phương trình là một số chẵn.'
        loigiai_vdc_1 = 'Vì nghiệm của phương trình là $x = %s$ chia hết cho $3$ nên khẳng định này đúng.' % nghiem
    else:
        vdc_da_1_d = '\\True Nghiệm $x$ của phương trình là một số nguyên chẵn.'
        vdc_da_1_s = 'Nghiệm $x$ của phương trình là một số lẻ.'
        loigiai_vdc_1 = 'Vì nghiệm của phương trình là $x = %s$ là số nguyên chẵn nên khẳng định này đúng.' % nghiem
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
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
