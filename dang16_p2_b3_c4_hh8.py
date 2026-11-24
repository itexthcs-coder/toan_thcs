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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang16_p2_b3_c4_hh8(self):
    # Dạng 16: Bài toán chuyển động trên khu đất hình vuông (Thực tế)
    t_an = random.choice([15, 20, 25])
    t_binh = 2 * t_an
    gio_xuat_phat_binh = 60 - t_an

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (B) at (0,3);\n'
        '\\coordinate (A) at (3,3);\n'
        '\\coordinate (D) at (3,0);\n'
        '\\coordinate (C) at (0,0);\n'
        '\\coordinate (M) at ($(B)!0.5!(A)$);\n'
        '\\coordinate (I) at (intersection of A--C and M--D);\n'
        '\\draw[line width=1pt] (B)--(A)--(D)--(C)--cycle (A)--(C) (M)--(D);\n'
        '\\fill (A) circle (1pt) node[above right] {$A$};\n'
        '\\fill (B) circle (1pt) node[above left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below left] {$C$};\n'
        '\\fill (D) circle (1pt) node[below right] {$D$};\n'
        '\\fill (M) circle (1pt) node[above] {$M$};\n'
        '\\fill (I) circle (1pt) node[below left] {$I$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Một công viên hình vuông $ABCD$. Nhà bạn An ở vị trí $M$ là trung điểm của cạnh $AB$, nhà bạn Bình ở vị trí đỉnh $D$. Hai bạn đi bộ với cùng một vận tốc trên con đường thẳng $MD$ để gặp nhau tại giao điểm $I$ của $MD$ và đường chéo $AC$. Bạn An xuất phát lúc $7\\text{ giờ}$ và đến điểm $I$ lúc $7\\text{ giờ } %s\\text{ phút}$.\n%s'
        % (t_an, hinh_ve)
    )

    nb_da_1_d = '\\True Đường chéo $AC$ là tia phân giác của góc $DAB$'
    nb_da_1_s = 'Đường chéo $AC$ vuông góc với cạnh $AB$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Theo tính chất của hình vuông $ABCD$, đường chéo $AC$ là tia phân giác của góc $DAB$.'
    loigiai_nb_s = 'Sai. Trong hình vuông $ABCD$, đường chéo $AC$ là tia phân giác của góc $DAB$.'

    th_da_1_d = '\\True Tỉ số quãng đường $\\frac{IM}{ID} = \\frac{1}{2}$'
    th_da_1_s = 'Tỉ số quãng đường $\\frac{IM}{ID} = 1$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Trong tam giác $AMD$ có $AI$ là đường phân giác của góc $A$ nên $\\frac{IM}{ID} = \\frac{AM}{AD}$. Vì $M$ là trung điểm của $AB$ và $AB = AD$ nên $\\frac{AM}{AD} = \\frac{1}{2}$, suy ra $\\frac{IM}{ID} = \\frac{1}{2}$.'
    loigiai_th_s = 'Sai. Áp dụng tính chất đường phân giác trong tam giác $AMD$, ta có $\\frac{IM}{ID} = \\frac{AM}{AD} = \\frac{1}{2}$.'

    vd_da_1_d = '\\True Thời gian bạn Bình đi từ $D$ đến $I$ là $%s\\text{ phút}$' % t_binh
    vd_da_1_s = 'Thời gian bạn Bình đi từ $D$ đến $I$ là $%s\\text{ phút}$' % (t_an + 10)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Vì hai bạn đi với cùng vận tốc mà quãng đường $ID = 2IM$ nên thời gian bạn Bình đi gấp đôi thời gian bạn An đi, tức là $2 \\cdot %s = %s\\text{ phút}$.' % (t_an, t_binh)
    loigiai_vd_s = 'Sai. Quãng đường $ID$ gấp đôi quãng đường $IM$ nên thời gian bạn Bình đi là $2 \\cdot %s = %s\\text{ phút}$.' % (t_an, t_binh)

    vdc_da_1_d = '\\True Để gặp bạn An đúng lúc $7\\text{ giờ } %s\\text{ phút}$ tại $I$, bạn Bình phải xuất phát lúc $6\\text{ giờ } %s\\text{ phút}$' % (t_an, gio_xuat_phat_binh)
    vdc_da_1_s = 'Để gặp bạn An đúng lúc $7\\text{ giờ } %s\\text{ phút}$ tại $I$, bạn Bình phải xuất phát lúc $6\\text{ giờ } %s\\text{ phút}$' % (t_an, t_an)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Bạn Bình cần đi hết $%s\\text{ phút}$ để đến $I$ lúc $7\\text{ giờ } %s\\text{ phút}$, nên bạn Bình phải xuất phát trước bạn An $%s\\text{ phút}$, tức là lúc $6\\text{ giờ } %s\\text{ phút}$.' % (t_binh, t_an, t_an, gio_xuat_phat_binh)
    loigiai_vdc_s = 'Sai. Thời gian di chuyển của bạn Bình là $%s\\text{ phút}$ nên bạn Bình phải xuất phát lúc $6\\text{ giờ } %s\\text{ phút}$.' % (t_binh, gio_xuat_phat_binh)

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

    loigiai_nb_1 = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    loigiai_th_1 = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    loigiai_vd_1 = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    loigiai_vdc_1 = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    list_nb_1 = [nb_da_1]
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    list_vd_1 = [vd_da_1]
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    list_vdc_1 = [vdc_da_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
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
