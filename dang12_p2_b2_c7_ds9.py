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


def bt_dang12_p2_b2_c7_ds9(self):
    he_so = random.choice([1, 2])
    m_trang, m_den, m_xanh = 36 * he_so, 28 * he_so, 16 * he_so
    n_lan = 80 * he_so

    noidungcauhoi = ('Trong một hộp kín có $20$ viên bi cùng kích thước gồm ba màu: Trắng, Đen và Xanh. Bạn An thực hiện $%s$ lần lấy ngẫu nhiên $1$ viên bi, ghi lại màu rồi trả lại vào hộp và trộn đều. Kết quả thu được: $%s$ lần bi Trắng, $%s$ lần bi Đen và $%s$ lần bi Xanh. Xét tính đúng sai của các khẳng định sau:' % (n_lan, m_trang, m_den, m_xanh))

    nb_da_1_d = '\\True Tần số tương đối xuất hiện bi Trắng, bi Đen, bi Xanh lần lượt là $45\\%$, $35\\%$ và $20\\%$'
    nb_da_1_s = 'Tần số tương đối xuất hiện bi Trắng, bi Đen, bi Xanh lần lượt là $40\\%$, $35\\%$ và $25\\%$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Các tần số tương đối lần lượt là $\\frac{%s}{%s} \\cdot 100\\%% = 45\\%%$, $\\frac{%s}{%s} \\cdot 100\\%% = 35\\%%$ và $\\frac{%s}{%s} \\cdot 100\\%% = 20\\%%$.' % (m_trang, n_lan, m_den, n_lan, m_xanh, n_lan))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Xác suất ước lượng để lấy được viên bi không phải màu Xanh là $80\\%$'
    th_da_1_s = 'Xác suất ước lượng để lấy được viên bi không phải màu Xanh là $20\\%$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Xác suất ước lượng lấy được bi không phải màu Xanh (tức màu Trắng hoặc Đen) là $45\\% + 35\\% = 80\\%$.')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Dựa vào kết quả thực nghiệm, ước lượng trong hộp có khoảng $9$ viên bi Trắng, $7$ viên bi Đen và $4$ viên bi Xanh'
    vd_da_1_s = 'Dựa vào kết quả thực nghiệm, ước lượng trong hộp có khoảng $10$ viên bi Trắng, $6$ viên bi Đen và $4$ viên bi Xanh'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Ước lượng số bi mỗi loại trong $20$ viên bi: Trắng có $20 \\cdot 45\\% = 9$ viên; Đen có $20 \\cdot 35\\% = 7$ viên; Xanh có $20 \\cdot 20\\% = 4$ viên.')
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tần số tương đối của bi Trắng là cơ sở để ước lượng xác suất lấy được bi Trắng trong một lần thử'
    vdc_da_1_s = 'Nếu An thực hiện thêm $20$ lần lấy bi nữa thì chắc chắn sẽ lấy được đúng $9$ lần bi màu Trắng'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Tần số tương đối chỉ là ước lượng cho xác suất xuất hiện giá trị đó chứ không khẳng định chắc chắn kết quả tuyệt đối của các lần thử tiếp theo.')
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

    list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
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
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
