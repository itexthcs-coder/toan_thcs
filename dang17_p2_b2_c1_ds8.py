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


def bt_dang17_p2_b2_c1_ds8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        tap = randint(2, 4)
        so_vo_nam = tap * 10
        hop = randint(1, 3)
        so_but_nam = hop * 12

        vo_lan = randint(12, 18)
        but_lan = randint(6, 10)
        thuoc_lan = randint(2, 4)

        tong_vo = so_vo_nam + vo_lan
        tong_but = so_but_nam + but_lan

        x0 = 8
        y0 = 5
        z0 = 15
        tong_tien = tong_vo * x0 + tong_but * y0 + thuoc_lan * z0

        noidungcauhoi = ('''Một cửa hàng văn phòng phẩm niêm yết giá: một quyển vở giá $x$ nghìn đồng, một chiếc bút bi giá $y$ nghìn đồng và một bộ thước kẻ giá $z$ nghìn đồng. Bạn Nam mua $%s$ tập vở (mỗi tập $10$ quyển) và $%s$ hộp bút bi (gồm $12$ chiếc mỗi hộp); bạn Lan mua $%s$ quyển vở, $%s$ chiếc bút bi và $%s$ bộ thước kẻ. Xét tính đúng, sai của các khẳng định sau:''' % (tap, hop, vo_lan, but_lan, thuoc_lan))

        nb_da_1_d = '\\True Đa thức biểu thị tổng số tiền bạn Nam phải trả là $%sx + %sy$ (nghìn đồng).' % (so_vo_nam, so_but_nam)
        nb_da_1_s = 'Đa thức biểu thị tổng số tiền bạn Nam phải trả là $%sx + %sy$ (nghìn đồng).' % (tap, hop)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Bạn Nam mua $%s \\cdot 10 = %s$ quyển vở và $%s \\cdot 12 = %s$ chiếc bút bi nên số tiền bạn Nam phải trả là $%sx + %sy$ (nghìn đồng).''' % (tap, so_vo_nam, hop, so_but_nam, so_vo_nam, so_but_nam))

        th_da_1_d = '\\True Đa thức biểu thị tổng số tiền bạn Lan phải trả là $%sx + %sy + %sz$ (nghìn đồng).' % (vo_lan, but_lan, thuoc_lan)
        th_da_1_s = 'Đa thức biểu thị tổng số tiền bạn Lan phải trả là $%sxyz$ (nghìn đồng).' % (vo_lan + but_lan + thuoc_lan)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Số tiền bạn Lan phải trả để mua $%s$ quyển vở, $%s$ chiếc bút bi và $%s$ bộ thước kẻ là $%sx + %sy + %sz$ (nghìn đồng).''' % (vo_lan, but_lan, thuoc_lan, vo_lan, but_lan, thuoc_lan))

        vd_da_1_d = '\\True Đa thức thu gọn biểu thị tổng số tiền cả hai bạn phải trả là $%sx + %sy + %sz$ (nghìn đồng), có bậc bằng $1$.' % (tong_vo, tong_but, thuoc_lan)
        vd_da_1_s = 'Đa thức thu gọn biểu thị tổng số tiền cả hai bạn phải trả là $%sx + %sy + %sz$ (nghìn đồng), có bậc bằng $3$.' % (tong_vo, tong_but, thuoc_lan)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Tổng số tiền cả hai bạn phải trả là $(%sx + %sy) + (%sx + %sy + %sz) = %sx + %sy + %sz$ (nghìn đồng). Đa thức này có bậc bằng $1$.''' % (so_vo_nam, so_but_nam, vo_lan, but_lan, thuoc_lan, tong_vo, tong_but, thuoc_lan))

        vdc_da_1_d = '\\True Nếu $x = %s$, $y = %s$ và $z = %s$ thì tổng số tiền cả hai bạn phải trả là $%s$ nghìn đồng.' % (x0, y0, z0, tong_tien)
        vdc_da_1_s = 'Nếu $x = %s$, $y = %s$ và $z = %s$ thì tổng số tiền cả hai bạn phải trả là $%s$ nghìn đồng.' % (x0, y0, z0, tong_tien + 20)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Thay $x = %s$, $y = %s$, $z = %s$ vào đa thức tổng, ta được: $%s \\cdot %s + %s \\cdot %s + %s \\cdot %s = %s$ (nghìn đồng).''' % (x0, y0, z0, tong_vo, x0, tong_but, y0, thuoc_lan, z0, tong_tien))

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
