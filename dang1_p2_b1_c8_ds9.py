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


def bt_dang1_p2_b1_c8_ds9(self):
    n = random.randint(5, 8)
    k = random.randint(2, n - 1)
    ans = n * (n - 1)
    noidungcauhoi = ("""Một hộp đựng $%s$ viên bi có kích thước và khối lượng giống nhau được đánh số từ $1$ đến $%s$. Lấy ngẫu nhiên lần lượt hai viên bi từ hộp, viên bi lấy ra lần đầu không trả lại vào hộp.""" % (n, n))
    # Ý 1
    st_1_d = '\\True ' + ('Mỗi kết quả của phép thử là một cặp số có thứ tự $(a, b)$ với $a, b \\in \\{1; 2; \\dots; %s\\}$ và $a \\neq b$' % (n))
    st_1_s = ('Mỗi kết quả của phép thử là một cặp số $(a, b)$ với $a, b \\in \\{1; 2; \\dots; %s\\}$ (có thể $a = b$)' % (n))
    sol_1_d = ('Đúng. Vì viên bi lấy ra lần đầu không trả lại vào hộp nên hai viên bi lấy ra có số khác nhau ($a \\neq b$).')
    sol_1_s = ('Sai. Vì viên bi lấy ra lần đầu không trả lại vào hộp nên không thể xảy ra trường hợp $a = b$.')
    pair_1 = [(st_1_d, sol_1_d), (st_1_s, sol_1_s)]
    # Ý 2
    st_2_d = '\\True ' + ('Kết quả $(1, %s)$ và $(%s, 1)$ là hai kết quả khác nhau trong không gian mẫu' % (k, k))
    st_2_s = ('Kết quả $(1, %s)$ và $(%s, 1)$ là cùng một kết quả trong không gian mẫu' % (k, k))
    sol_2_d = ('Đúng. Phép thử thực hiện lần lượt nên thứ tự xuất hiện của viên bi lần $1$ và lần $2$ tạo thành hai kết quả phân biệt.')
    sol_2_s = ('Sai. Vì lấy lần lượt nên $(1, %s)$ (lần $1$ số $1$, lần $2$ số $%s$) khác với $(%s, 1)$ (lần $1$ số $%s$, lần $2$ số $1$).' % (k, k, k, k))
    pair_2 = [(st_2_d, sol_2_d), (st_2_s, sol_2_s)]
    # Ý 3
    st_3_d = '\\True ' + ('Nếu lập bảng hai chiều kích thước $%s \\times %s$ thì có $%s$ ô trên đường chéo chính bị loại bỏ' % (n, n, n))
    st_3_s = ('Nếu lập bảng hai chiều kích thước $%s \\times %s$ thì có $%s$ ô trên đường chéo chính bị loại bỏ' % (n, n, n - 1))
    sol_3_d = ('Đúng. Bảng vuông $%s \\times %s$ có đúng $%s$ cặp trùng nhau $(1, 1); (2, 2); \\dots; (%s, %s)$ bị loại bỏ.' % (n, n, n, n, n))
    sol_3_s = ('Sai. Số cặp trùng nhau bị loại bỏ là $%s$ cặp: $(1, 1); (2, 2); \\dots; (%s, %s)$.' % (n, n, n))
    pair_3 = [(st_3_d, sol_3_d), (st_3_s, sol_3_s)]
    # Ý 4
    st_4_d = '\\True ' + ('Số phần tử của không gian mẫu của phép thử là $%s$' % (ans))
    st_4_s = ('Số phần tử của không gian mẫu của phép thử là $%s$' % (n * n))
    sol_4_d = ('Đúng. Số phần tử của không gian mẫu là $%s \\cdot %s = %s$.' % (n, n - 1, ans))
    sol_4_s = ('Sai. Số phần tử của không gian mẫu là $%s \\cdot %s = %s$ (không phải $%s^2 = %s$).' % (n, n - 1, ans, n, n * n))
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
