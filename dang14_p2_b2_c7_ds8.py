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


def bt_dang14_p2_b2_c7_ds8(self):
    # Dạng 14: Bài toán hình học về diện tích hình chữ nhật khi thay đổi kích thước
    # (x - g)(x + d + t) = x(x + d) => (t - g)x - g(d + t) = 0 => x = g(d + t) / (t - g)
    g, t, d, rong = random.choice([
        (2, 3, 6, 18),   # (x-2)(x+9) = x(x+6) => x = 18
        (2, 4, 5, 9),    # (x-2)(x+9) = x(x+5) => 2x = 18 => x = 9
        (3, 4, 5, 27),   # (x-3)(x+9) = x(x+5) => x = 27
        (2, 5, 4, 6)     # (x-2)(x+9) = x(x+4) => 3x = 18 => x = 6
    ])
    dai_moi_const = d + t
    hs_x_moi = dai_moi_const - g
    hang_tu_moi = g * dai_moi_const

    noidungcauhoi = "Cho một hình chữ nhật có chiều rộng là $x$ ($\\text{cm}$) ($x > %s$) và chiều dài hơn chiều rộng $%s\\text{ cm}$. Nếu giảm chiều rộng đi $%s\\text{ cm}$ và tăng chiều dài thêm $%s\\text{ cm}$ thì diện tích hình chữ nhật mới bằng diện tích hình chữ nhật ban đầu. Xét tính đúng, sai của các khẳng định sau:" % (
        g, d, g, t
    )

    nb_da_1_d = '\\True Diện tích hình chữ nhật ban đầu là $x(x + %s)$ ($\\text{cm}^2$).' % d
    nb_da_1_s = 'Diện tích hình chữ nhật ban đầu là $2(2x + %s)$ ($\\text{cm}^2$).' % d
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Chiều rộng ban đầu là $x$ ($\\text{cm}$), chiều dài ban đầu là $x + %s$ ($\\text{cm}$) nên diện tích ban đầu là $x(x + %s)$ ($\\text{cm}^2$).' % (d, d)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Chiều dài của hình chữ nhật mới là $x + %s$ ($\\text{cm}$).' % dai_moi_const
    th_da_1_s = 'Chiều dài của hình chữ nhật mới là $x + %s$ ($\\text{cm}$).' % (d - t)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Chiều dài ban đầu là $x + %s$ ($\\text{cm}$), sau khi tăng thêm $%s\\text{ cm}$ thì chiều dài mới là $(x + %s) + %s = x + %s$ ($\\text{cm}$).' % (
        d, t, d, t, dai_moi_const
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Phương trình biểu thị sự bằng nhau của hai diện tích là $(x - %s)(x + %s) = x(x + %s)$.' % (g, dai_moi_const, d)
    vd_da_1_s = 'Phương trình biểu thị sự bằng nhau của hai diện tích là $(x + %s)(x - %s) = x(x + %s)$.' % (g, dai_moi_const, d)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Chiều rộng mới là $x - %s$ ($\\text{cm}$), chiều dài mới là $x + %s$ ($\\text{cm}$), nên phương trình diện tích là $(x - %s)(x + %s) = x(x + %s)$.' % (
        g, dai_moi_const, g, dai_moi_const, d
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Chiều rộng ban đầu của hình chữ nhật là $%s\\text{ cm}$.' % rong
    vdc_da_1_s = 'Chiều rộng ban đầu của hình chữ nhật là $%s\\text{ cm}$.' % (rong + 3)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Khai triển phương trình: $x^2 + %sx - %s = x^2 + %sx \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện $x > %s$).' % (
        hs_x_moi, hang_tu_moi, d, t - g, hang_tu_moi, rong, g
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
