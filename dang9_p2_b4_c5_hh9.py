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

def bt_dang9_p2_b4_c5_hh9(self):
    def fmt_num(val):
        if isinstance(val, int) or (isinstance(val, float) and val.is_integer()):
            return str(int(val))
        s = ("%.6f" % val).rstrip("0").rstrip(".")
        return s.replace(".", ",")

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 9: Tứ giác ngoại tiếp đường tròn và tính chất hai tiếp tuyến cắt nhau
        AM = random.choice([2, 3, 4])
        BM = random.choice([3, 4, 5])
        CN = random.choice([4, 5, 6])
        DP = random.choice([2, 3, 4])

        AB = AM + BM
        BC = BM + CN
        CD = CN + DP
        AD = AM + DP
        AD_sai = AD + 1
        CP = CN

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (M) at (0,1.2);\n"
            "\\coordinate (P) at (0,-1.2);\n"
            "\\coordinate (Q) at (-1.159,0.311);\n"
            "\\coordinate (N) at (1.159,-0.311);\n"
            "\\coordinate (A) at (-0.9,1.2);\n"
            "\\coordinate (B) at (1.559,1.2);\n"
            "\\coordinate (C) at (0.9,-1.2);\n"
            "\\coordinate (D) at (-1.559,-1.2);\n"
            "\\draw[line width=1pt] (O) circle (1.2);\n"
            "\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n"
            "\\draw[line width=1pt, dashed] (O)--(M) (O)--(N) (O)--(P) (O)--(Q);\n"
            "\\fill (O) circle (1pt) node[below left] {$O$};\n"
            "\\fill (A) circle (1pt) node[above left] {$A$};\n"
            "\\fill (B) circle (1pt) node[above right] {$B$};\n"
            "\\fill (C) circle (1pt) node[below right] {$C$};\n"
            "\\fill (D) circle (1pt) node[below left] {$D$};\n"
            "\\fill (M) circle (1pt) node[above] {$M$};\n"
            "\\fill (N) circle (1pt) node[right] {$N$};\n"
            "\\fill (P) circle (1pt) node[below] {$P$};\n"
            "\\fill (Q) circle (1pt) node[left] {$Q$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho tứ giác $ABCD$ có cả bốn cạnh đều tiếp xúc với đường tròn $(O)$ lần lượt tại $M \\in AB$, $N \\in BC$, $P \\in CD$, $Q \\in DA$. Biết $AB = %s\\text{ cm}$, $BC = %s\\text{ cm}$, $CD = %s\\text{ cm}$.\n%s'''
            % (fmt_num(AB), fmt_num(BC), fmt_num(CD), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Ta có các cặp đoạn thẳng bằng nhau: $AM = AQ$, $BM = BN$, $CN = CP$, $DP = DQ$'
        nb_da_1_s = 'Ta có các cặp đoạn thẳng bằng nhau: $AM = BM$, $BN = CN$, $CP = DP$, $DQ = AQ$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Theo tính chất hai tiếp tuyến cắt nhau của đường tròn $(O)$ tại các đỉnh $A$, $B$, $C$, $D$, ta có $AM = AQ$, $BM = BN$, $CN = CP$ và $DP = DQ$.'''
        )
        loigiai_nb_1_s = (
            '''Sai. Theo tính chất hai tiếp tuyến cắt nhau xuất phát từ mỗi đỉnh của tứ giác, hai đoạn tiếp tuyến xuất phát từ cùng một đỉnh mới bằng nhau: $AM = AQ$, $BM = BN$, $CN = CP$ và $DP = DQ$.'''
        )

        # Thông hiểu
        th_da_1_d = '\\True Tổng độ dài hai cạnh đối $AB + CD$ bằng tổng độ dài hai cạnh đối $BC + AD$'
        th_da_1_s = 'Tổng độ dài hai cạnh đối $AB + CD$ luôn lớn hơn tổng độ dài hai cạnh đối $BC + AD$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Cộng vế theo vế bốn đẳng thức $AM = AQ$, $BM = BN$, $CP = CN$, $DP = DQ$, ta được: $(AM + BM) + (CP + DP) = (AQ + DQ) + (BN + CN)$, hay $AB + CD = AD + BC$.'''
        )
        loigiai_th_1_s = (
            '''Sai. Cộng vế theo vế bốn đẳng thức $AM = AQ$, $BM = BN$, $CP = CN$, $DP = DQ$, ta thu được $AB + CD = BC + AD$ (hai tổng luôn bằng nhau).'''
        )

        # Vận dụng
        vd_da_1_d = '\\True Độ dài cạnh $AD$ bằng $%s\\text{ cm}$' % (fmt_num(AD))
        vd_da_1_s = 'Độ dài cạnh $AD$ bằng $%s\\text{ cm}$' % (fmt_num(AD_sai))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Từ hệ thức $AB + CD = BC + AD$, suy ra độ dài cạnh $AD = AB + CD - BC = %s + %s - %s = %s\\text{ cm}$.'''
            % (fmt_num(AB), fmt_num(CD), fmt_num(BC), fmt_num(AD))
        )
        loigiai_vd_1_s = (
            '''Sai. Từ hệ thức $AB + CD = BC + AD$, ta tính được $AD = AB + CD - BC = %s + %s - %s = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(AB), fmt_num(CD), fmt_num(BC), fmt_num(AD), fmt_num(AD_sai))
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Nếu $AM = %s\\text{ cm}$ thì độ dài đoạn thẳng $CP$ bằng $%s\\text{ cm}$' % (fmt_num(AM), fmt_num(CP))
        vdc_da_1_s = 'Nếu $AM = %s\\text{ cm}$ thì độ dài đoạn thẳng $CP$ bằng $%s\\text{ cm}$' % (fmt_num(AM), fmt_num(CP + 1))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Ta có $BM = AB - AM = %s - %s = %s\\text{ cm}$. \\\\ Theo tính chất hai tiếp tuyến cắt nhau, suy ra $BN = BM = %s\\text{ cm}$. \\\\ Do đó $CN = BC - BN = %s - %s = %s\\text{ cm}$, suy ra $CP = CN = %s\\text{ cm}$.'''
            % (fmt_num(AB), fmt_num(AM), fmt_num(BM), fmt_num(BM), fmt_num(BC), fmt_num(BM), fmt_num(CN), fmt_num(CP))
        )
        loigiai_vdc_1_s = (
            '''Sai. Tính lần lượt ta có $BM = AB - AM = %s - %s = %s\\text{ cm}$, suy ra $BN = %s\\text{ cm}$, $CN = BC - BN = %s - %s = %s\\text{ cm}$. Do đó $CP = CN = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(AB), fmt_num(AM), fmt_num(BM), fmt_num(BM), fmt_num(BC), fmt_num(BM), fmt_num(CN), fmt_num(CP), fmt_num(CP + 1))
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)

            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            true_count = count_true_answers(answers)
            if 1 <= true_count <= 3:
                break

        loigiai_nb_1 = loigiai_nb_1_d if nb_da_1 == nb_da_1_d else loigiai_nb_1_s
        loigiai_th_1 = loigiai_th_1_d if th_da_1 == th_da_1_d else loigiai_th_1_s
        loigiai_vd_1 = loigiai_vd_1_d if vd_da_1 == vd_da_1_d else loigiai_vd_1_s
        loigiai_vdc_1 = loigiai_vdc_1_d if vdc_da_1 == vdc_da_1_d else loigiai_vdc_1_s

        list_nb_1 = [nb_da_1]
        list_th_1 = [th_da_1]
        list_vd_1 = [vd_da_1]
        list_vdc_1 = [vdc_da_1]

        list_nb_2 = [loigiai_nb_1]
        list_th_2 = [loigiai_th_1]
        list_vd_2 = [loigiai_vd_1]
        list_vdc_2 = [loigiai_vdc_1]

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

    # Xuất câu trắc nghiệm đúng sai
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choiceTFn \n' +
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
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
