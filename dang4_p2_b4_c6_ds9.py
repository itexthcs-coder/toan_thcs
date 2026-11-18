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


def bt_dang4_p2_b4_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k_val = random.choice([0.2, 0.4, 0.5])
        x1 = random.choice([80, 100, 120])
        x2 = random.choice([160, 200, 240])
        if x1 == x2:
            x2 += 60
        a_demand = int(k_val * (x1 + x2))
        doanh_thu = int(k_val * x1 * x2)
        p_at_x2 = int(a_demand - k_val * x2)
        p_at_x1 = int(a_demand - k_val * x1)

        noidungcauhoi = ('''Một cửa hàng kinh doanh phụ kiện điện thoại khảo sát thấy nhu cầu của khách hàng đối với một mẫu ốp lưng được cho bởi công thức $p = %s - %sx$, trong đó $p$ là giá bán mỗi chiếc (nghìn đồng) và $x$ là số lượng ốp lưng bán được ($x \\in \\mathbb{N}^*$). Doanh thu $R$ (nghìn đồng) được tính theo công thức $R = x \\cdot p$. Cửa hàng đặt mục tiêu đạt doanh thu $%s\\text{ nghìn đồng}$.''' % (fmt_num(a_demand), fmt_num(k_val), fmt_num(doanh_thu)))

        nb_da_1_d = '\\True Phương trình tìm số lượng ốp lưng cần bán để đạt mục tiêu là $%sx^2 - %sx + %s = 0$' % (fmt_num(k_val), fmt_num(a_demand), fmt_num(doanh_thu))
        nb_da_1_s = 'Phương trình tìm số lượng ốp lưng cần bán để đạt mục tiêu là $%sx^2 + %sx - %s = 0$' % (fmt_num(k_val), fmt_num(a_demand), fmt_num(doanh_thu))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thay $R = %s$ và $p = %s - %sx$ vào công thức $R = x \\cdot p$, ta được: \\\\ $x(%s - %sx) = %s \\Leftrightarrow %sx^2 - %sx + %s = 0$.''' % (fmt_num(doanh_thu), fmt_num(a_demand), fmt_num(k_val), fmt_num(a_demand), fmt_num(k_val), fmt_num(doanh_thu), fmt_num(k_val), fmt_num(a_demand), fmt_num(doanh_thu)))

        th_da_1_d = '\\True Phương trình trên có hai nghiệm phân biệt là $x_1 = %s$ và $x_2 = %s$' % (fmt_num(x1), fmt_num(x2))
        th_da_1_s = 'Phương trình trên có hai nghiệm phân biệt là $x_1 = %s$ và $x_2 = %s$' % (fmt_num(x1 - 20), fmt_num(x2 + 20))
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        b_norm = x1 + x2
        c_norm = x1 * x2
        loigiai_th_1 = ('''Chia hai vế của phương trình cho $%s$, ta được $x^2 - %sx + %s = 0$. \\\\ Giải phương trình này ta tìm được hai nghiệm phân biệt $x_1 = %s$ và $x_2 = %s$ (đều thoả mãn $x \\in \\mathbb{N}^*$).''' % (fmt_num(k_val), fmt_num(b_norm), fmt_num(c_norm), fmt_num(x1), fmt_num(x2)))

        vd_da_1_d = '\\True Nếu cửa hàng muốn bán được nhiều hàng để quảng bá thương hiệu ($%s\\text{ chiếc}$) thì giá bán mỗi chiếc ốp lưng là $%s\\text{ nghìn đồng}$' % (fmt_num(x2), fmt_num(p_at_x2))
        vd_da_1_s = 'Nếu cửa hàng muốn bán được nhiều hàng để quảng bá thương hiệu ($%s\\text{ chiếc}$) thì giá bán mỗi chiếc ốp lưng là $%s\\text{ nghìn đồng}$' % (fmt_num(x2), fmt_num(p_at_x1))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Khi bán $x = %s$ chiếc ốp lưng, giá bán mỗi chiếc là $p = %s - %s \\cdot %s = %s\\text{ (nghìn đồng)}$.''' % (fmt_num(x2), fmt_num(a_demand), fmt_num(k_val), fmt_num(x2), fmt_num(p_at_x2)))

        vdc_da_1_d = '\\True Để đạt doanh thu $%s\\text{ nghìn đồng}$ với mức giá bán cao nhất có thể, cửa hàng cần bán $%s\\text{ chiếc}$ ốp lưng' % (fmt_num(doanh_thu), fmt_num(x1))
        vdc_da_1_s = 'Để đạt doanh thu $%s\\text{ nghìn đồng}$ với mức giá bán cao nhất có thể, cửa hàng cần bán $%s\\text{ chiếc}$ ốp lưng' % (fmt_num(doanh_thu), fmt_num(x2))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Khi $x = %s$ thì giá bán là $p = %s - %s \\cdot %s = %s\\text{ (nghìn đồng)}$, cao hơn so với trường hợp bán $%s$ chiếc ($p = %s\\text{ nghìn đồng}$). Vậy cửa hàng cần bán $%s\\text{ chiếc}$.''' % (fmt_num(x1), fmt_num(a_demand), fmt_num(k_val), fmt_num(x1), fmt_num(p_at_x1), fmt_num(x2), fmt_num(p_at_x2), fmt_num(x1)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

    combined_nb = list(zip(list_nb_1, list_nb_2)); random.shuffle(combined_nb)
    combined_th = list(zip(list_th_1, list_th_2)); random.shuffle(combined_th)
    combined_vd = list(zip(list_vd_1, list_vd_2)); random.shuffle(combined_vd)
    combined_vdc = list(zip(list_vdc_1, list_vdc_2)); random.shuffle(combined_vdc)

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
