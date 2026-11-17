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


def bt_dang16_p2_b1_c6_ds9(self):
    def fmt_num(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    a_coef = random.choice([500, 600, 700, 800])
    m_car = 2 * a_coef
    w_10 = a_coef * 100
    v_target = random.choice([20, 25, 30])
    w_target = a_coef * (v_target ** 2)

    bang_tabular = (
        '\\begin{center}\n'
        '\\begin{tabular}{|c|c|c|c|}\n'
        '\\hline\n'
        'Vận tốc $v$ ($\\text{m/s}$) & $0$ & $10$ & $%s$ \\\\ \n'
        '\\hline\n'
        'Động năng $W_đ$ ($\\text{J}$) & $0$ & $?$ & $%s$ \\\\ \n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}' % (fmt_num(v_target), fmt_num(w_target))
    )

    noidungcauhoi = (
        'Động năng $W_đ$ (tính bằng Jun, ký hiệu $\\text{J}$) của một ô tô có khối lượng $m = %s\\text{ kg}$ đang chuyển động với vận tốc $v$ ($\\text{m/s}$) được tính theo công thức $W_đ = \\frac{1}{2}mv^2$.%s' % (fmt_num(m_car), bang_tabular)
    )

    nb_da_1_d = '\\True Công thức biểu thị động năng $W_đ$ theo vận tốc $v$ của ô tô này là $W_đ = %sv^2$' % (fmt_num(a_coef))
    nb_da_1_s = 'Công thức biểu thị động năng $W_đ$ theo vận tốc $v$ của ô tô này là $W_đ = %sv^2$' % (fmt_num(m_car))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Thay khối lượng $m = %s\\text{ kg}$ vào công thức động năng ta được: $W_đ = \\frac{1}{2} \\cdot %s \\cdot v^2 = %sv^2$.' % (fmt_num(m_car), fmt_num(m_car), fmt_num(a_coef))
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khi ô tô chạy với vận tốc $10\\text{ m/s}$, động năng của xe là $%s\\text{ J}$' % (fmt_num(w_10))
    th_da_1_s = 'Khi ô tô chạy với vận tốc $10\\text{ m/s}$, động năng của xe là $%s\\text{ J}$' % (fmt_num(a_coef * 10))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay $v = 10$ vào công thức ta được: $W_đ = %s \\cdot 10^2 = %s \\cdot 100 = %s\\text{ (J)}$.' % (fmt_num(a_coef), fmt_num(a_coef), fmt_num(w_10))
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu tài xế tăng vận tốc xe lên gấp đôi thì động năng của xe tăng lên gấp $4$ lần'
    vd_da_1_s = 'Nếu tài xế tăng vận tốc xe lên gấp đôi thì động năng của xe cũng tăng lên gấp đôi'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Khi tăng vận tốc lên gấp đôi (từ $v$ thành $2v$), động năng mới là $W_đ\\prime = %s(2v)^2 = 4 \\cdot %sv^2 = 4W_đ$. Vậy động năng tăng gấp $4$ lần.' % (fmt_num(a_coef), fmt_num(a_coef))
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khi xe đạt động năng $%s\\text{ J}$ thì vận tốc của xe là $%s\\text{ m/s}$' % (fmt_num(w_target), fmt_num(v_target))
    vdc_da_1_s = 'Khi xe đạt động năng $%s\\text{ J}$ thì vận tốc của xe là $%s\\text{ m/s}$' % (fmt_num(w_target), fmt_num(v_target + 5))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Thay $W_đ = %s$ vào công thức $W_đ = %sv^2$ ta được: \\\\ $%sv^2 = %s \\Leftrightarrow v^2 = %s$. Vì $v > 0$ nên $v = %s\\text{ (m/s)}$.' % (fmt_num(w_target), fmt_num(a_coef), fmt_num(a_coef), fmt_num(w_target), fmt_num(v_target**2), fmt_num(v_target))
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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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
