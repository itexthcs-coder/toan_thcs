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


def bt_dang18_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        x = symbols('x')
        c0 = random.choice([80, 100, 120])
        N0 = c0 + random.choice([160, 200, 240])
        b_prof = N0 + c0
        c_prof = N0 * c0
        x_opt = b_prof // 2
        L_max = (x_opt - c0) * (N0 - x_opt)

        diff_p = random.choice([20, 30])
        x_high = x_opt + diff_p
        x_low = x_opt - diff_p
        L_target = (x_high - c0) * (N0 - x_high)

        noidungcauhoi = ('Một xưởng sản xuất thủ công nhận thấy rằng nếu bán mỗi chiếc túi xách với giá $x$ (nghìn đồng, $%s \\le x \\le %s$) thì số lượng túi bán được trong một tuần là $%s - x$ (chiếc). Biết chi phí sản xuất mỗi chiếc túi là $%s$ nghìn đồng. Xét tính đúng sai của các khẳng định sau:' % (c0, N0, N0, c0))

        nb_da_1_d = '\\True Số tiền lãi thu được trên mỗi chiếc túi bán ra là $x - %s$ (nghìn đồng)' % (c0)
        nb_da_1_s = 'Số tiền lãi thu được trên mỗi chiếc túi bán ra là $%s - x$ (nghìn đồng)' % (c0)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Lợi nhuận thu được trên mỗi sản phẩm bằng giá bán trừ chi phí sản xuất, tức là $x - %s$ (nghìn đồng).' % (c0))

        th_da_1_d = '\\True Tổng lợi nhuận $L(x)$ (nghìn đồng) thu được trong một tuần được mô hình hóa bởi công thức $L(x) = -x^2 + %sx - %s$' % (b_prof, c_prof)
        th_da_1_s = 'Tổng lợi nhuận $L(x)$ (nghìn đồng) thu được trong một tuần được mô hình hóa bởi công thức $L(x) = -x^2 + %sx - %s$' % (N0 - c0, c_prof)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Tổng lợi nhuận trong tuần là: $L(x) = (x - %s)(%s - x) = %sx - x^2 - %s + %sx = -x^2 + %sx - %s$.' % (c0, N0, N0, c_prof, c0, b_prof, c_prof))

        vd_da_1_d = '\\True Nếu xưởng muốn thu được lợi nhuận đúng $%s$ nghìn đồng mỗi tuần thì phải định giá bán là $%s$ nghìn đồng/chiếc' % (L_max, x_opt)
        vd_da_1_s = 'Nếu xưởng muốn thu được lợi nhuận đúng $%s$ nghìn đồng mỗi tuần thì phải định giá bán là $%s$ nghìn đồng/chiếc' % (L_max, x_opt + 10)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Giải phương trình $-x^2 + %sx - %s = %s \\Leftrightarrow x^2 - %sx + %s = 0 \\Leftrightarrow (x - %s)^2 = 0 \\Leftrightarrow x = %s$ (thỏa mãn điều kiện).' % (b_prof, c_prof, L_max, b_prof, x_opt**2, x_opt, x_opt))

        vdc_da_1_d = '\\True Có hai mức giá bán khác nhau giúp xưởng đạt mức lợi nhuận $%s$ nghìn đồng mỗi tuần, trong đó mức giá cao hơn là $%s$ nghìn đồng/chiếc' % (L_target, x_high)
        vdc_da_1_s = 'Có hai mức giá bán khác nhau giúp xưởng đạt mức lợi nhuận $%s$ nghìn đồng mỗi tuần, trong đó mức giá cao hơn là $%s$ nghìn đồng/chiếc' % (L_target, x_low)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Giải phương trình $-x^2 + %sx - %s = %s \\Leftrightarrow x^2 - %sx + %s = 0$. \\\\ Có $\\Delta\\prime = %s^2 - %s = %s \\Rightarrow \\sqrt{\\Delta\\prime} = %s$. \\\\ Hai nghiệm là $x_1 = %s + %s = %s$ và $x_2 = %s - %s = %s$ (đều thỏa mãn). Mức giá cao hơn là $%s$ nghìn đồng/chiếc.' % (b_prof, c_prof, L_target, b_prof, c_prof + L_target, x_opt, c_prof + L_target, diff_p**2, diff_p, x_opt, diff_p, x_high, x_opt, diff_p, x_low, x_high))

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

        combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
        combined_th = list(zip([th_da_1], [loigiai_th_1]))
        combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
        combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

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
