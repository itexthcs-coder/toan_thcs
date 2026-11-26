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


def bt_dang16_p2_b2_c7_ds8(self):
    # Dạng 16 (Thực tế): Nấu chảy hợp kim và thêm bạc nguyên chất để hạ hàm lượng vàng
    so_vong, nang_moi_vong, pct_vang_bd, pct_vang_moi, x_ans = random.choice([
        (8, 25, 80, 64, 50),    # M = 200, Vang = 160 -> 160 = 0.64(200 + x) -> 200 + x = 250 -> x = 50
        (10, 18, 90, 75, 36),   # M = 180, Vang = 162 -> 162 = 0.75(180 + x) -> 180 + x = 216 -> x = 36
        (6, 25, 80, 60, 50),    # M = 150, Vang = 120 -> 120 = 0.60(150 + x) -> 150 + x = 200 -> x = 50
        (8, 20, 75, 60, 40)     # M = 160, Vang = 120 -> 120 = 0.60(160 + x) -> 160 + x = 200 -> x = 40
    ])
    tong_m = so_vong * nang_moi_vong
    pct_bac_bd = 100 - pct_vang_bd
    vang_nc = int(round(tong_m * pct_vang_bd / 100))
    tl_vang_moi = str(pct_vang_moi / 100).replace('.', ',')
    vang_trong_m_bd = str(round(tong_m * pct_vang_moi / 100, 2)).replace('.', ',')
    hieu_vang = str(round(vang_nc - tong_m * pct_vang_moi / 100, 2)).replace('.', ',')

    noidungcauhoi = "Một nghệ nhân kim hoàn có $%s$ chiếc vòng tay giống hệt nhau, mỗi chiếc nặng $%s\\text{ g}$, được chế tác từ hợp kim gồm $%s\\%%$ vàng nguyên chất và $%s\\%%$ bạc. Nghệ nhân quyết định nấu chảy toàn bộ số vòng tay này và thêm vào một lượng bạc nguyên chất để hạ hàm lượng vàng xuống còn $%s\\%%$ nhằm chế tác mẫu trang sức mới. Gọi $x$ ($\\text{g}$) ($x > 0$) là khối lượng bạc nguyên chất cần thêm vào. Xét tính đúng, sai của các khẳng định sau:" % (
        so_vong, nang_moi_vong, pct_vang_bd, pct_bac_bd, pct_vang_moi
    )

    nb_da_1_d = '\\True Tổng khối lượng hợp kim ban đầu của $%s$ chiếc vòng tay là $%s\\text{ g}$.' % (so_vong, tong_m)
    nb_da_1_s = 'Tổng khối lượng hợp kim ban đầu của $%s$ chiếc vòng tay là $%s\\text{ g}$.' % (so_vong, tong_m + 20)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Tổng khối lượng của $%s$ chiếc vòng tay là $%s \\cdot %s = %s$ ($\\text{g}$).' % (so_vong, so_vong, nang_moi_vong, tong_m)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khối lượng vàng nguyên chất có trong $%s$ chiếc vòng tay là $%s\\text{ g}$ và không đổi sau khi nấu chảy.' % (so_vong, vang_nc)
    th_da_1_s = 'Khối lượng vàng nguyên chất có trong $%s$ chiếc vòng tay là $%s\\text{ g}$.' % (so_vong, tong_m - vang_nc)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Khối lượng vàng nguyên chất ban đầu là $%s\\%% \\cdot %s = %s$ ($\\text{g}$). Vì chỉ thêm bạc nguyên chất nên khối lượng vàng nguyên chất không thay đổi.' % (
        pct_vang_bd, tong_m, vang_nc
    )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Phương trình biểu thị tỉ lệ vàng trong hợp kim mới là $%s = %s(%s + x)$.' % (vang_nc, tl_vang_moi, tong_m)
    vd_da_1_s = 'Phương trình biểu thị tỉ lệ vàng trong hợp kim mới là $%s + x = %s(%s + x)$.' % (vang_nc, tl_vang_moi, tong_m)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Khối lượng hợp kim sau khi thêm $x$ ($\\text{g}$) bạc là $%s + x$ ($\\text{g}$). Vì hàm lượng vàng lúc sau chiếm $%s\\%%$ nên ta có phương trình: $%s = %s(%s + x)$.' % (
        tong_m, pct_vang_moi, vang_nc, tl_vang_moi, tong_m
    )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nghệ nhân cần thêm vào $%s\\text{ g}$ bạc nguyên chất.' % x_ans
    vdc_da_1_s = 'Nghệ nhân cần thêm vào $%s\\text{ g}$ bạc nguyên chất.' % (x_ans - 10)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Giải phương trình: $%s = %s + %sx \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn). Vậy nghệ nhân cần thêm $%s\\text{ g}$ bạc.' % (
        vang_nc, vang_trong_m_bd, tl_vang_moi, tl_vang_moi, hieu_vang, x_ans, x_ans
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
