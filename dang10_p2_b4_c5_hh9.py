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

def bt_dang10_p2_b4_c5_hh9(self):
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
        # Dạng 10: Khoảng cách từ điểm trên đường thẳng ngoài đường tròn đến tiếp điểm
        bo_so = [
            (10, 14, 4, 6),
            (6, 10, 8, 1),
            (8, 12, 4, 5),
            (9, 15, 12, 1),
            (12, 16, 4, 7)
        ]
        R, OH, k_ngoai, k_trong = random.choice(bo_so)
        EH = OH - R
        ha_sq = OH * OH - R * R
        ha_sai = OH + R
        ha_str = "%s" % fmt_num(k_ngoai) if k_trong == 1 else "%s\\sqrt{%s}" % (fmt_num(k_ngoai), fmt_num(k_trong))

        hinh_ve = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "\\coordinate (O) at (0,0);\n"
            "\\coordinate (F) at (0,1.4);\n"
            "\\coordinate (E) at (0,-1.4);\n"
            "\\coordinate (H) at (0,-2.1);\n"
            "\\coordinate (K) at (2.0,-2.1);\n"
            "\\draw[line width=1pt] (O) circle (1.4);\n"
            "\\draw[line width=1pt] (-2.5,-2.1)--(2.8,-2.1) node[above] {$\\Delta$};\n"
            "\\draw[line width=1pt] (-2.0,-1.4)--(2.0,-1.4);\n"
            "\\draw[line width=1pt] (F)--(H);\n"
            "\\draw[line width=1pt, dashed] (O)--(K);\n"
            "\\draw[line width=1pt] (0,-1.9)--(0.2,-1.9)--(0.2,-2.1);\n"
            "\\fill (O) circle (1pt) node[left] {$O$};\n"
            "\\fill (F) circle (1pt) node[above left] {$F$};\n"
            "\\fill (E) circle (1pt) node[above left] {$E$};\n"
            "\\fill (H) circle (1pt) node[below] {$H$};\n"
            "\\fill (K) circle (1pt) node[below] {$K$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        noidungcauhoi = (
            '''Cho đường tròn $(O; %s\\text{ cm})$ và đường thẳng $\\Delta$ không giao nhau với $(O)$. Qua $O$ kẻ đường thẳng vuông góc với $\\Delta$ tại $H$, cắt $(O)$ tại hai điểm $E$ và $F$ ($E$ nằm giữa $O$ và $H$). Biết $OH = %s\\text{ cm}$.\n%s'''
            % (fmt_num(R), fmt_num(OH), hinh_ve)
        )

        # Nhận biết
        nb_da_1_d = '\\True Khoảng cách từ điểm $E$ đến đường thẳng $\\Delta$ bằng $%s\\text{ cm}$' % (fmt_num(EH))
        nb_da_1_s = 'Khoảng cách từ điểm $E$ đến đường thẳng $\\Delta$ bằng $%s\\text{ cm}$' % (fmt_num(R))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1_d = (
            '''Đúng. Vì $OH \\perp \\Delta$ tại $H$ và $E$ nằm giữa $O$, $H$ nên $EH \\perp \\Delta$ tại $H$. \\\\ Do $E$ thuộc đường tròn $(O; %s\\text{ cm})$ nên $OE = %s\\text{ cm}$. Vậy khoảng cách từ $E$ đến đường thẳng $\\Delta$ là $EH = OH - OE = %s - %s = %s\\text{ cm}$.'''
            % (fmt_num(R), fmt_num(R), fmt_num(OH), fmt_num(R), fmt_num(EH))
        )
        loigiai_nb_1_s = (
            '''Sai. Vì $EH \\perp \\Delta$ tại $H$ và $E$ nằm giữa $O$, $H$ nên khoảng cách từ $E$ đến đường thẳng $\\Delta$ là $EH = OH - OE = %s - %s = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(OH), fmt_num(R), fmt_num(EH), fmt_num(R))
        )

        # Thông hiểu
        th_da_1_d = '\\True Tiếp tuyến của đường tròn $(O)$ tại điểm $E$ song song với đường thẳng $\\Delta$'
        th_da_1_s = 'Tiếp tuyến của đường tròn $(O)$ tại điểm $E$ vuông góc với đường thẳng $\\Delta$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1_d = (
            '''Đúng. Tiếp tuyến của đường tròn $(O)$ tại $E$ vuông góc với bán kính $OE$ tại $E$, tức là vuông góc với đường thẳng $OH$. \\\\ Mặt khác, đường thẳng $\\Delta$ cũng vuông góc với đường thẳng $OH$ tại $H$. Do đó tiếp tuyến tại $E$ song song với đường thẳng $\\Delta$.'''
        )
        loigiai_th_1_s = (
            '''Sai. Tiếp tuyến của $(O)$ tại $E$ vuông góc với đường thẳng $OH$, mà $\\Delta$ cũng vuông góc với $OH$ nên hai đường thẳng này song song với nhau, không phải vuông góc.'''
        )

        # Vận dụng
        vd_da_1_d = '\\True Từ điểm $K$ bất kì trên $\\Delta$, kẻ hai tiếp tuyến $KA$, $KB$ đến $(O)$. Độ dài $KA$ nhỏ nhất khi $K$ trùng với $H$'
        vd_da_1_s = 'Từ điểm $K$ bất kì trên $\\Delta$, kẻ hai tiếp tuyến $KA$, $KB$ đến $(O)$. Độ dài $KA$ không đổi khi $K$ di chuyển trên $\\Delta$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1_d = (
            '''Đúng. Trong tam giác $OAK$ vuông tại $A$, theo định lí Pythagore ta có $KA = \\sqrt{OK^2 - OA^2} = \\sqrt{OK^2 - %s^2}$. \\\\ Vì $OH \\perp \\Delta$ tại $H$ nên với mọi điểm $K \\in \\Delta$, ta luôn có $OK \\ge OH$ (quan hệ giữa đường vuông góc và đường xiên), dấu bằng xảy ra khi $K$ trùng với $H$. \\\\ Do đó $KA$ đạt giá trị nhỏ nhất khi $K$ trùng với $H$.'''
            % (fmt_num(R))
        )
        loigiai_vd_1_s = (
            '''Sai. Ta có $KA = \\sqrt{OK^2 - R^2}$. Khi $K$ di chuyển trên $\\Delta$, độ dài $OK$ thay đổi ($OK \\ge OH$) nên độ dài $KA$ thay đổi và đạt giá trị nhỏ nhất khi $K$ trùng với $H$.'''
        )

        # Vận dụng cao
        vdc_da_1_d = '\\True Khi $K$ trùng với $H$, độ dài tiếp tuyến $HA$ bằng $%s\\text{ cm}$' % (ha_str)
        vdc_da_1_s = 'Khi $K$ trùng với $H$, độ dài tiếp tuyến $HA$ bằng $%s\\text{ cm}$' % (fmt_num(ha_sai))
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1_d = (
            '''Đúng. Khi $K$ trùng với $H$, xét tam giác $OAH$ vuông tại $A$, áp dụng định lí Pythagore ta có: $HA = \\sqrt{OH^2 - OA^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s\\text{ cm}$.'''
            % (fmt_num(OH), fmt_num(R), fmt_num(ha_sq), ha_str)
        )
        loigiai_vdc_1_s = (
            '''Sai. Khi $K$ trùng với $H$, áp dụng định lí Pythagore vào tam giác $OAH$ vuông tại $A$, ta có: $HA = \\sqrt{OH^2 - OA^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s} = %s\\text{ cm}$ (khác $%s\\text{ cm}$).'''
            % (fmt_num(OH), fmt_num(R), fmt_num(ha_sq), ha_str, fmt_num(ha_sai))
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
