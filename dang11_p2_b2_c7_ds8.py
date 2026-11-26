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


def bt_dang11_p2_b2_c7_ds8(self):
    # Dạng 11: Bài toán viết thêm chữ số vào bên phải số có hai chữ số
    k = random.choice([2, 3])
    max_x = 9 // k
    x_dv = random.randint(1, max_x)
    x_chuc = k * x_dv
    so_ban_dau = 10 * x_chuc + x_dv
    c_them = random.randint(1, 9)
    so_moi = 10 * so_ban_dau + c_them
    hieu = so_moi - so_ban_dau
    he_so_bd = 10 * k + 1
    he_so_moi = 10 * he_so_bd

    noidungcauhoi = "Tìm một số tự nhiên có hai chữ số, biết rằng chữ số hàng chục gấp $%s$ lần chữ số hàng đơn vị. Nếu viết thêm chữ số $%s$ vào bên phải số đó thì được một số mới lớn hơn số ban đầu là $%s$ đơn vị. Gọi $x$ là chữ số hàng đơn vị ($x \\in \\mathbb{N}^*$, $1 \\le x \\le %s$). Xét tính đúng, sai của các khẳng định sau:" % (
        k, c_them, hieu, max_x
    )

    nb_da_1_d = '\\True Chữ số hàng chục là $%sx$ và giá trị của số ban đầu là $%sx$.' % (k, he_so_bd)
    nb_da_1_s = 'Chữ số hàng chục là $%sx$ và giá trị của số ban đầu là $%sx$.' % (k, k + 1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Chữ số hàng chục là $%sx$. Giá trị của số tự nhiên có hai chữ số ban đầu là $10 \\cdot (%sx) + x = %sx$.' % (k, k, he_so_bd)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khi viết thêm chữ số $%s$ vào bên phải số ban đầu, ta được số mới có giá trị là $%sx + %s$.' % (c_them, he_so_moi, c_them)
    th_da_1_s = 'Khi viết thêm chữ số $%s$ vào bên phải số ban đầu, ta được số mới có giá trị là $%sx + %s$.' % (c_them, he_so_bd, c_them)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Viết thêm chữ số $%s$ vào bên phải một số tự nhiên thì số đó tăng lên gấp $10$ lần và cộng thêm $%s$, nên số mới là $10(%sx) + %s = %sx + %s$.' % (
        c_them, c_them, he_so_bd, c_them, he_so_moi, c_them
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Phương trình biểu thị mối quan hệ của bài toán là $%sx + %s - %sx = %s$.' % (he_so_moi, c_them, he_so_bd, hieu)
    vd_da_1_s = 'Phương trình biểu thị mối quan hệ của bài toán là $%sx + %s + %sx = %s$.' % (he_so_moi, c_them, he_so_bd, hieu)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Vì số mới lớn hơn số ban đầu $%s$ đơn vị nên ta có phương trình: $(%sx + %s) - %sx = %s$.' % (
        hieu, he_so_moi, c_them, he_so_bd, hieu
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số tự nhiên ban đầu cần tìm là $%s$.' % so_ban_dau
    vdc_da_1_s = 'Số tự nhiên ban đầu cần tìm là $%s$.' % (10 * x_dv + x_chuc)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Giải phương trình: $%sx = %s \\Leftrightarrow x = %s$ (thỏa mãn). Vậy chữ số hàng đơn vị là $%s$, chữ số hàng chục là $%s$, số cần tìm là $%s$.' % (
        he_so_moi - he_so_bd, hieu - c_them, x_dv, x_dv, x_chuc, so_ban_dau
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
