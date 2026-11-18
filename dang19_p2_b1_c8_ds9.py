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


def bt_dang19_p2_b1_c8_ds9(self):
    ans = 24
    noidungcauhoi = ("""Một công ty du lịch thiết kế tour tham quan khép kín xuất phát từ thành phố $A$, đi qua đúng ba địa điểm $B, C, D$ theo một thứ tự nào đó rồi quay trở về $A$. Khách hàng quay vòng quay ngẫu nhiên để chọn lộ trình.""" % ())
    # Ý 1
    st_1_d = '\\True ' + ('Số lộ trình khác nhau để đi từ $A$ qua đủ ba điểm $B, C, D$ rồi về $A$ là $6$')
    st_1_s = ('Số lộ trình khác nhau để đi từ $A$ qua đủ ba điểm $B, C, D$ rồi về $A$ là $3$')
    sol_1_d = ('Đúng. Thứ tự đi qua ba địa điểm $B, C, D$ là một hoán vị của $3$ phần tử nên có $3 \\cdot 2 \\cdot 1 = 6$ lộ trình.')
    sol_1_s = ('Sai. Có $3 \\cdot 2 \\cdot 1 = 6$ thứ tự sắp xếp ba địa điểm $B, C, D$.')
    pair_1 = [(st_1_d, sol_1_d), (st_1_s, sol_1_s)]
    # Ý 2
    st_2_d = '\\True ' + ('Nếu giữa hai địa điểm bất kì đều có $2$ tuyến đường (một đường cao tốc và một đường ven biển) thì từ $A$ đến $B$ có $2$ cách chọn đường')
    st_2_s = ('Nếu giữa hai địa điểm bất kì đều có $2$ tuyến đường thì lộ trình $A \\to B \\to C \\to D \\to A$ chỉ có $4$ cách đi')
    sol_2_d = ('Đúng. Đoạn từ $A$ đến $B$ có $2$ lựa chọn tuyến đường.')
    sol_2_s = ('Sai. Mỗi chặng trong $4$ chặng của lộ trình có $2$ cách chọn nên riêng thứ tự $A \\to B \\to C \\to D \\to A$ đã có $2^4 = 16$ cách đi.')
    pair_2 = [(st_2_d, sol_2_d), (st_2_s, sol_2_s)]
    # Ý 3
    st_3_d = '\\True ' + ('Nếu công ty bổ sung thêm địa điểm $E$ (đi qua đủ $4$ điểm $B, C, D, E$ theo thứ tự rồi về $A$) thì số thứ tự tham quan là $24$')
    st_3_s = ('Nếu công ty bổ sung thêm địa điểm $E$ (đi qua đủ $4$ điểm $B, C, D, E$ theo thứ tự rồi về $A$) thì số thứ tự tham quan là $12$')
    sol_3_d = ('Đúng. Số hoán vị của $4$ địa điểm $B, C, D, E$ là $4 \\cdot 3 \\cdot 2 \\cdot 1 = 24$.')
    sol_3_s = ('Sai. Số thứ tự đi qua $4$ địa điểm là $4 \\cdot 3 \\cdot 2 \\cdot 1 = 24$.')
    pair_3 = [(st_3_d, sol_3_d), (st_3_s, sol_3_s)]
    # Ý 4
    st_4_d = '\\True ' + ('Với $3$ địa điểm $B, C, D$, số lộ trình mà địa điểm $B$ được tham quan đầu tiên ngay sau khi rời $A$ là $2$')
    st_4_s = ('Với $3$ địa điểm $B, C, D$, số lộ trình mà địa điểm $B$ được tham quan đầu tiên ngay sau khi rời $A$ là $3$')
    sol_4_d = ('Đúng. Hai lộ trình đó là $A \\to B \\to C \\to D \\to A$ và $A \\to B \\to D \\to C \\to A$.')
    sol_4_s = ('Sai. Chỉ có $2$ lộ trình xuất phát từ $A$ đến $B$ đầu tiên.')
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
