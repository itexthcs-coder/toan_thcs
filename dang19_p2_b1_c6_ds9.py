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


def bt_dang19_p2_b1_c6_ds9(self):
    def fmt_dec(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
            return s.replace('.', ',')
        return s

    price_k = random.choice([300, 400, 500])
    coef_c = Decimal(str(price_k)) * Decimal('3.14')
    coef_c_str = fmt_dec(coef_c)

    c_05 = coef_c * Decimal('0.25')
    c_05_str = fmt_dec(c_05)

    r_max = 2
    c_max = coef_c * Decimal(str(r_max ** 2))
    c_max_str = fmt_dec(c_max)

    noidungcauhoi = (
        'Một xưởng sản xuất nhận gia công các tấm kính cường lực hình tròn bán kính $r$ (mét) ($r > 0$). Chi phí vật liệu và cắt kính là $%s$ nghìn đồng/$\\text{m}^2$ (lấy $\\pi \\approx 3,14$). Gọi $C$ (nghìn đồng) là chi phí để làm một tấm kính bán kính $r$.' % (str(price_k))
    )

    nb_da_1_d = '\\True Công thức tính chi phí $C$ (nghìn đồng) theo bán kính $r$ (mét) là $C = %sr^2$' % (coef_c_str)
    nb_da_1_s = 'Công thức tính chi phí $C$ (nghìn đồng) theo bán kính $r$ (mét) là $C = %sr$' % (coef_c_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (
        'Diện tích tấm kính hình tròn là $S = \\pi r^2 \\approx 3,14r^2$ ($\\text{m}^2$). \\\\ Chi phí gia công tấm kính là $C = %s \\cdot 3,14r^2 = %sr^2$ (nghìn đồng).' % (str(price_k), coef_c_str)
    )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Một tấm kính bàn ăn có bán kính $0,5\\text{ m}$ sẽ có chi phí gia công là $%s$ nghìn đồng' % (c_05_str)
    th_da_1_s = 'Một tấm kính bàn ăn có bán kính $0,5\\text{ m}$ sẽ có chi phí gia công là $%s$ nghìn đồng' % (fmt_dec(coef_c * Decimal('0.5')))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (
        'Thay $r = 0,5$ vào công thức ta được: $C = %s \\cdot (0,5)^2 = %s \\cdot 0,25 = %s$ (nghìn đồng).' % (coef_c_str, coef_c_str, c_05_str)
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu khách hàng đặt một tấm kính có bán kính $1\\text{ m}$ thì chi phí sẽ gấp $4$ lần so với tấm kính bán kính $0,5\\text{ m}$'
    vd_da_1_s = 'Nếu khách hàng đặt một tấm kính có bán kính $1\\text{ m}$ thì chi phí sẽ gấp đôi so với tấm kính bán kính $0,5\\text{ m}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (
        'Bán kính $1\\text{ m}$ gấp $2$ lần bán kính $0,5\\text{ m}$, mà chi phí $C$ tỉ lệ thuận với $r^2$ nên chi phí sẽ tăng $2^2 = 4$ lần.'
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Với ngân sách tối đa $%s$ nghìn đồng cho một tấm kính, xưởng có thể làm tấm kính có bán kính lớn nhất là $2\\text{ m}$' % (c_max_str)
    vdc_da_1_s = 'Với ngân sách tối đa $%s$ nghìn đồng cho một tấm kính, xưởng có thể làm tấm kính có bán kính lớn nhất là $4\\text{ m}$' % (c_max_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (
        'Ta có $%sr^2 \\le %s \\Leftrightarrow r^2 \\le 4$. Vì $r > 0$ nên $r \\le 2\\text{ (m)}$. Vậy bán kính lớn nhất có thể làm là $2\\text{ m}$.' % (coef_c_str, c_max_str)
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
