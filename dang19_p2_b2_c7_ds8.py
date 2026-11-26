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


def bt_dang19_p2_b2_c7_ds8(self):
    # Dạng 19 (Thực tế): Bài toán năng suất vượt mức (hoàn thành sớm và vượt sản lượng)
    ngay_kd, som, vuot_ns, vuot_sp, ns_kd = random.choice([
        (20, 2, 15, 30, 120),   # 18(x + 15) = 20x + 30 -> 2x = 240 -> x = 120, tong = 2400
        (25, 1, 2, 8, 20),      # 24(x + 2) = 25x + 8 -> x = 40 -> đổi cho chẵn: (25, 2, 10, 30, 100): 23(x+10) = 25x + 30 -> 2x = 200 -> x = 100, tong = 2500
        (15, 3, 20, 60, 60),    # 12(x + 20) = 15x + 60 -> 3x = 180 -> x = 60, tong = 900
        (30, 3, 12, 54, 90)     # 27(x + 12) = 30x + 54 -> 3x = 270 -> x = 90, tong = 2700
    ])
    if (ngay_kd, som, vuot_ns, vuot_sp, ns_kd) == (25, 1, 2, 8, 20):
        ngay_kd, som, vuot_ns, vuot_sp, ns_kd = (25, 2, 10, 30, 100)

    ngay_tt = ngay_kd - som
    tong_kd = ngay_kd * ns_kd

    def fmt_num(n):
        return f"{n:,}".replace(",", "\,")

    noidungcauhoi = "Một phân xưởng dệt được giao kế hoạch sản xuất một lô khăn bông trong $%s$ ngày. Nhờ cải tiến dây chuyền, mỗi ngày phân xưởng dệt vượt mức kế hoạch $%s$ chiếc khăn nên chẳng những đã hoàn thành sớm hơn dự định $%s$ ngày mà còn làm vượt mức được giao thêm $%s$ chiếc khăn nữa. Gọi $x$ (chiếc) ($x \\in \\mathbb{N}^*$) là số khăn phân xưởng phải dệt mỗi ngày theo kế hoạch. Xét tính đúng, sai của các khẳng định sau:" % (
        ngay_kd, vuot_ns, som, vuot_sp
    )

    nb_da_1_d = '\\True Tổng số khăn phân xưởng được giao theo kế hoạch là $%sx$ (chiếc).' % ngay_kd
    nb_da_1_s = 'Tổng số khăn phân xưởng được giao theo kế hoạch là $%s + x$ (chiếc).' % ngay_kd
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Vì dự định làm trong $%s$ ngày, mỗi ngày dệt $x$ chiếc khăn nên tổng số khăn được giao là $%sx$ (chiếc).' % (ngay_kd, ngay_kd)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Thời gian thực tế phân xưởng làm việc là $%s$ ngày với năng suất mỗi ngày là $x + %s$ (chiếc).' % (ngay_tt, vuot_ns)
    th_da_1_s = 'Thời gian thực tế phân xưởng làm việc là $%s$ ngày với năng suất mỗi ngày là $x + %s$ (chiếc).' % (ngay_kd + som, vuot_ns)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Vì hoàn thành sớm hơn dự định $%s$ ngày nên thời gian thực tế là $%s - %s = %s$ (ngày), năng suất thực tế mỗi ngày là $x + %s$ (chiếc).' % (
        som, ngay_kd, som, ngay_tt, vuot_ns
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Phương trình biểu thị mối quan hệ giữa sản lượng thực tế và kế hoạch là $%s(x + %s) = %sx + %s$.' % (ngay_tt, vuot_ns, ngay_kd, vuot_sp)
    vd_da_1_s = 'Phương trình biểu thị mối quan hệ giữa sản lượng thực tế và kế hoạch là $%s(x + %s) = %sx - %s$.' % (ngay_tt, vuot_ns, ngay_kd, vuot_sp)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Tổng số khăn thực tế dệt được là $%s(x + %s)$ (chiếc), nhiều hơn kế hoạch $%s$ chiếc nên ta có phương trình: $%s(x + %s) = %sx + %s$.' % (
        ngay_tt, vuot_ns, vuot_sp, ngay_tt, vuot_ns, ngay_kd, vuot_sp
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tổng số khăn phân xưởng được giao theo kế hoạch ban đầu là $%s$ chiếc.' % fmt_num(tong_kd)
    vdc_da_1_s = 'Tổng số khăn phân xưởng được giao theo kế hoạch ban đầu là $%s$ chiếc.' % fmt_num(tong_kd + vuot_sp)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Giải phương trình: $%sx + %s = %sx + %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn). Vậy tổng số khăn được giao theo kế hoạch là $%s \\cdot %s = %s$ (chiếc).' % (
        ngay_tt, ngay_tt * vuot_ns, ngay_kd, vuot_sp,
        ngay_kd - ngay_tt, ngay_tt * vuot_ns - vuot_sp, ns_kd,
        ngay_kd, ns_kd, fmt_num(tong_kd)
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
