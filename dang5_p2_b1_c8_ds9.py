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


def bt_dang5_p2_b1_c8_ds9(self):
    m = random.randint(3, 5)
    n = random.randint(2, 4)
    ans = m * n
    noidungcauhoi = ("""Một nhà hàng phục vụ bữa trưa tự chọn gồm $%s$ món mặn (kí hiệu $M_1, M_2, \\dots, M_%s$) và $%s$ món canh (kí hiệu $C_1, C_2, \\dots, C_%s$). Mỗi khách hàng chọn ngẫu nhiên một món mặn và một món canh.""" % (m, m, n, n))
    # Ý 1
    st_1_d = '\\True ' + ('Mỗi kết quả của phép thử là một cặp $(M_i, C_j)$ với $1 \\le i \\le %s$ và $1 \\le j \\le %s$' % (m, n))
    st_1_s = ('Mỗi kết quả của phép thử là một cặp $(M_i, M_j)$ với $1 \\le i, j \\le %s$' % (m))
    sol_1_d = ('Đúng. Khách hàng chọn $1$ món mặn $M_i$ trong $%s$ món và $1$ món canh $C_j$ trong $%s$ món.' % (m, n))
    sol_1_s = ('Sai. Khách hàng chọn một món mặn và một món canh nên kết quả có dạng $(M_i, C_j)$.')
    pair_1 = [(st_1_d, sol_1_d), (st_1_s, sol_1_s)]
    # Ý 2
    st_2_d = '\\True ' + ('Lập bảng hai chiều mô tả không gian mẫu ta cần kẻ bảng gồm $%s$ hàng và $%s$ cột (không kể hàng và cột tiêu đề)' % (m, n))
    st_2_s = ('Lập bảng hai chiều mô tả không gian mẫu ta cần kẻ bảng gồm $%s$ hàng và $%s$ cột (không kể hàng và cột tiêu đề)' % (m + n, 2))
    sol_2_d = ('Đúng. Bảng có $%s$ hàng ứng với $%s$ món mặn và $%s$ cột ứng với $%s$ món canh.' % (m, m, n, n))
    sol_2_s = ('Sai. Bảng hai chiều gồm $%s$ hàng và $%s$ cột.' % (m, n))
    pair_2 = [(st_2_d, sol_2_d), (st_2_s, sol_2_s)]
    # Ý 3
    st_3_d = '\\True ' + ('Số phần tử của không gian mẫu của phép thử là $%s$' % (ans))
    st_3_s = ('Số phần tử của không gian mẫu của phép thử là $%s$' % (m + n))
    sol_3_d = ('Đúng. Số phần tử của không gian mẫu là $%s \\cdot %s = %s$.' % (m, n, ans))
    sol_3_s = ('Sai. Số phần tử của không gian mẫu là $%s \\cdot %s = %s$ (không phải $%s + %s = %s$).' % (m, n, ans, m, n, m + n))
    pair_3 = [(st_3_d, sol_3_d), (st_3_s, sol_3_s)]
    # Ý 4
    st_4_d = '\\True ' + ('Nếu nhà hàng bổ sung thêm $1$ món canh mới thì số phần tử của không gian mẫu tăng thêm $%s$' % (m))
    st_4_s = ('Nếu nhà hàng bổ sung thêm $1$ món canh mới thì số phần tử của không gian mẫu tăng thêm $1$')
    sol_4_d = ('Đúng. Khi tăng thêm $1$ món canh thì số phần tử mới là $%s \\cdot (%s + 1) = %s$, tăng thêm đúng $%s$ phần tử.' % (m, n, m * (n + 1), m))
    sol_4_s = ('Sai. Mỗi món canh mới kết hợp được với tất cả $%s$ món mặn nên không gian mẫu tăng thêm $%s$ phần tử.' % (m, m))
    pair_4 = [(st_4_d, sol_4_d), (st_4_s, sol_4_s)]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        c1 = random.choice(pair_1)
        c2 = random.choice(pair_2)
        c3 = random.choice(pair_3)
        c4 = random.choice(pair_4)
        answers = [c1[0], c2[0], c3[0], c4[0]]
        if 1 <= count_true_answers(answers) <= 3:
            break

    shuffled_answers_nb = [c1[0]]
    shuffled_solutions_nb = [c1[1]]
    shuffled_answers_th = [c2[0]]
    shuffled_solutions_th = [c2[1]]
    shuffled_answers_vd = [c3[0]]
    shuffled_solutions_vd = [c3[1]]
    shuffled_answers_vdc = [c4[0]]
    shuffled_solutions_vdc = [c4[1]]

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
