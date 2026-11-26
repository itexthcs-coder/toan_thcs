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


def bt_dang18_p2_b2_c7_ds8(self):
    # Dạng 18 (Thực tế): Bài toán giảm giá kép (khuyến mãi cửa hàng + thẻ thành viên)
    giam1, giam2, gia_goc_nghin = random.choice([
        (15, 10, 2000),   # 0.85 * 0.90 = 0.765 -> 2000 * 0.765 = 1530
        (20, 5, 500),     # 0.80 * 0.95 = 0.76 -> 500 * 0.76 = 380
        (20, 10, 1500),   # 0.80 * 0.90 = 0.72 -> 1500 * 0.72 = 1080
        (10, 10, 1000)    # 0.90 * 0.90 = 0.81 -> 1000 * 0.81 = 810
    ])
    tl1 = (100 - giam1) / 100
    tl2 = (100 - giam2) / 100
    tl_chung = round(tl1 * tl2, 4)
    tl_cong_don = round(1 - (giam1 + giam2) / 100, 4)
    gia_tra_nghin = int(round(gia_goc_nghin * tl_chung))

    s_tl1 = str(tl1).replace('.', ',')
    s_tl2 = str(tl2).replace('.', ',')
    s_tl_chung = str(tl_chung).replace('.', ',')
    s_tl_cong_don = str(tl_cong_don).replace('.', ',')

    def fmt_num(n):
        return f"{n:,}".replace(",", "\,")

    noidungcauhoi = "Nhân dịp lễ hội mua sắm, một cửa hàng điện tử giảm giá $%s\\%%$ trên giá niêm yết cho tất cả các mẫu tai nghe không dây. Chị Thảo có thẻ thành viên hạng Vàng nên được giảm thêm $%s\\%%$ trên giá đã giảm ở lần thứ nhất. Cuối cùng, chị Thảo chỉ phải thanh toán $%s\,000$ đồng cho chiếc tai nghe đó. Gọi $x$ (nghìn đồng) ($x > 0$) là giá niêm yết ban đầu của chiếc tai nghe. Xét tính đúng, sai của các khẳng định sau:" % (
        giam1, giam2, fmt_num(gia_tra_nghin)
    )

    nb_da_1_d = '\\True Giá của chiếc tai nghe sau lần giảm giá thứ nhất là $%sx$ (nghìn đồng).' % s_tl1
    nb_da_1_s = 'Giá của chiếc tai nghe sau lần giảm giá thứ nhất là $%sx$ (nghìn đồng).' % str(giam1 / 100).replace('.', ',')
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Sau khi giảm giá $%s\\%%$ trên giá niêm yết $x$, giá chiếc tai nghe là $(100\\%% - %s\\%%)x = %sx$ (nghìn đồng).' % (giam1, giam1, s_tl1)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Sau khi áp dụng thêm ưu đãi thẻ thành viên, số tiền chị Thảo phải trả được biểu diễn là $%sx$ (nghìn đồng).' % s_tl_chung
    th_da_1_s = 'Sau khi áp dụng thêm ưu đãi thẻ thành viên, số tiền chị Thảo phải trả được biểu diễn là $%sx$ (nghìn đồng).' % s_tl_cong_don
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Vì được giảm thêm $%s\\%%$ trên giá đã giảm ở lần thứ nhất nên số tiền phải trả là $(100\\%% - %s\\%%) \\cdot %sx = %s \\cdot %sx = %sx$ (nghìn đồng).' % (
        giam2, giam2, s_tl1, s_tl2, s_tl1, s_tl_chung
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Phương trình tính giá niêm yết ban đầu của chiếc tai nghe là $%sx = %s$.' % (s_tl_chung, fmt_num(gia_tra_nghin))
    vd_da_1_s = 'Phương trình tính giá niêm yết ban đầu của chiếc tai nghe là $%sx = %s$.' % (s_tl_cong_don, fmt_num(gia_tra_nghin))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Đổi $%s\,000$ đồng $= %s$ nghìn đồng. Ta có phương trình: $%sx = %s$.' % (
        fmt_num(gia_tra_nghin), fmt_num(gia_tra_nghin), s_tl_chung, fmt_num(gia_tra_nghin)
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Giá niêm yết ban đầu của chiếc tai nghe là $%s\,000$ đồng.' % fmt_num(gia_goc_nghin)
    vdc_da_1_s = 'Giá niêm yết ban đầu của chiếc tai nghe là $%s\,000$ đồng.' % fmt_num(gia_goc_nghin + 200)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Giải phương trình: $%sx = %s \\Leftrightarrow x = \\dfrac{%s}{%s} = %s$ (nghìn đồng) $= %s\,000$ đồng.' % (
        s_tl_chung, fmt_num(gia_tra_nghin), fmt_num(gia_tra_nghin), s_tl_chung, fmt_num(gia_goc_nghin), fmt_num(gia_goc_nghin)
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
