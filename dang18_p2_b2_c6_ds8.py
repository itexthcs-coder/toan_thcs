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


def bt_dang18_p2_b2_c6_ds8(self):
    # Dạng 18: Thực tế chuyển động - Bài toán vận tốc và thời gian di chuyển trên đường bộ
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        s_tong = 180
        s1 = 60
        s2 = s_tong - s1
        dv = 15
        v1 = 45

        noidungcauhoi = ('Một xe khách xuất phát từ bến xe A đi đến bến xe B cách nhau $%s\\text{ km}$. Trên $%s\\text{ km}$ đầu tiên đường đông nên xe chạy với vận tốc $x\\text{ km/h}$ ($x > 0$). Trên quãng đường còn lại đường thông thoáng hơn nên xe tăng vận tốc thêm $%s\\text{ km/h}$. Xét tính đúng sai của các khẳng định sau:' % (s_tong, s1, dv))

        # Ý a
        nb_da_1_d = '\\True Phân thức biểu thị thời gian xe chạy trên $%s\\text{ km}$ đầu tiên là $\\dfrac{%s}{x}$ (giờ)' % (s1, s1)
        nb_da_1_s = 'Phân thức biểu thị thời gian xe chạy trên $%s\\text{ km}$ đầu tiên là $\\dfrac{x}{%s}$ (giờ)' % (s1, s1)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thời gian bằng quãng đường chia vận tốc nên thời gian đi $%s\\text{ km}$ đầu là $\\dfrac{%s}{x}$ (giờ).' % (s1, s1))
        list_nb_2 = [loigiai_nb_1]

        # Ý b
        th_da_1_d = '\\True Phân thức biểu thị thời gian xe chạy trên quãng đường còn lại là $\\dfrac{%s}{x + %s}$ (giờ)' % (s2, dv)
        th_da_1_s = 'Phân thức biểu thị thời gian xe chạy trên quãng đường còn lại là $\\dfrac{%s}{x + %s}$ (giờ)' % (s_tong, dv)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Quãng đường còn lại dài $%s - %s = %s\\text{ km}$ và vận tốc trên chặng này là $(x + %s)\\text{ km/h}$ nên thời gian đi là $\\dfrac{%s}{x + %s}$ (giờ).' % (s_tong, s1, s2, dv, s2, dv))
        list_th_2 = [loigiai_th_1]

        # Ý c
        vd_da_1_d = '\\True Mẫu thức chung của hai phân thức biểu thị thời gian trên hai chặng đường là $x(x + %s)$' % dv
        vd_da_1_s = 'Mẫu thức chung của hai phân thức biểu thị thời gian trên hai chặng đường là $2x + %s$' % dv
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Hai mẫu thức $x$ và $x + %s$ không có nhân tử chung nào khác $1$ nên mẫu thức chung là $x(x + %s)$.' % (dv, dv))
        list_vd_2 = [loigiai_vd_1]

        # Ý d
        vdc_da_1_d = '\\True Nếu vận tốc trên $%s\\text{ km}$ đầu là $%s\\text{ km/h}$ thì tổng thời gian xe chạy trên cả hai chặng đường là $3$ giờ $20$ phút' % (s1, v1)
        vdc_da_1_s = 'Nếu vận tốc trên $%s\\text{ km}$ đầu là $%s\\text{ km/h}$ thì tổng thời gian xe chạy trên cả hai chặng đường là $3$ giờ $40$ phút' % (s1, v1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Thay $x = %s$, thời gian chặng đầu là $\\dfrac{%s}{%s} = \\dfrac{4}{3}$ giờ ($1$ giờ $20$ phút), thời gian chặng sau là $\\dfrac{%s}{%s + %s} = \\dfrac{120}{60} = 2$ giờ. Tổng thời gian là $3$ giờ $20$ phút.' % (v1, s1, v1, s2, v1, dv))
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
