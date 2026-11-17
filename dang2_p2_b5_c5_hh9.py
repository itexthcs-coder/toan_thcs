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


def bt_dang2_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    am = random.randint(3, 6)
    bm = random.randint(4, 8)
    ab = am + bm
    r_dung = ab + am
    r_ngoai = bm - 1
    kc_ngan = ab - (am + r_ngoai)

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (M) at (2,0);
\\coordinate (B) at (5,0);
\\draw[line width=1pt] (A) circle (2cm);
\\draw[line width=1pt] (B) circle (3cm);
\\draw[line width=1pt] (A)--(B);
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (B) circle (1pt) node[below] {$B$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Cho đoạn thẳng $AB = %s\\text{ cm}$. Lấy điểm $M$ nằm giữa $A$ và $B$ sao cho $AM = %s\\text{ cm}$. Vẽ hai đường tròn $(A; %s\\text{ cm})$ và $(B; R)$ ($R > 0$).
%s""" % (fmt(ab), fmt(am), fmt(am), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Khi $R = %s\\text{ cm}$, hai đường tròn $(A)$ và $(B)$ tiếp xúc ngoài tại $M$' % (fmt(bm))
    nb_da_1_s = 'Khi $R = %s\\text{ cm}$, hai đường tròn $(A)$ và $(B)$ cắt nhau tại hai điểm phân biệt' % (fmt(bm))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì $M$ nằm giữa $A$ và $B$ nên $BM = AB - AM = %s - %s = %s\\text{ cm}$. Khi $R = %s\\text{ cm}$, ta có $AB = %s + %s = %s\\text{ cm}$ và $M$ thuộc cả hai đường tròn nên $(A)$ và $(B)$ tiếp xúc ngoài tại $M$.""" % (fmt(ab), fmt(am), fmt(bm), fmt(bm), fmt(am), fmt(bm), fmt(ab)))

    # Thông hiểu
    th_da_1_d = '\\True Khi $R = %s\\text{ cm}$, đường tròn $(B)$ đựng đường tròn $(A)$' % (fmt(r_dung))
    th_da_1_s = 'Khi $R = %s\\text{ cm}$, đường tròn $(B)$ tiếp xúc trong với đường tròn $(A)$' % (fmt(r_dung))
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Khi $R = %s\\text{ cm}$, ta có $R - AM = %s - %s = %s\\text{ cm} > AB = %s\\text{ cm}$. Vì $AB < R - AM$ nên đường tròn $(B)$ đựng đường tròn $(A)$.""" % (fmt(r_dung), fmt(r_dung), fmt(am), fmt(r_dung - am), fmt(ab)))

    # Vận dụng
    vd_da_1_d = '\\True Để hai đường tròn $(A)$ và $(B)$ cắt nhau thì điều kiện của $R$ là $%s\\text{ cm} < R < %s\\text{ cm}$' % (fmt(bm), fmt(r_dung))
    vd_da_1_s = 'Để hai đường tròn $(A)$ và $(B)$ cắt nhau thì điều kiện của $R$ là $%s\\text{ cm} < R < %s\\text{ cm}$' % (fmt(am), fmt(ab))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Hai đường tròn $(A; %s\\text{ cm})$ và $(B; R)$ cắt nhau khi và chỉ khi $|R - %s| < %s < R + %s$. \\\\ Giải hệ bất phương trình: $R + %s > %s \\Leftrightarrow R > %s$ và $R - %s < %s \\Leftrightarrow R < %s$. \\\\ Vậy điều kiện là $%s\\text{ cm} < R < %s\\text{ cm}$.""" % (fmt(am), fmt(am), fmt(ab), fmt(am), fmt(am), fmt(ab), fmt(bm), fmt(am), fmt(ab), fmt(r_dung), fmt(bm), fmt(r_dung)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Khi $R = %s\\text{ cm}$, hai đường tròn ở ngoài nhau và khoảng cách ngắn nhất giữa một điểm trên $(A)$ và một điểm trên $(B)$ bằng $%s\\text{ cm}$' % (fmt(r_ngoai), fmt(kc_ngan))
    vdc_da_1_s = 'Khi $R = %s\\text{ cm}$, hai đường tròn ở ngoài nhau và khoảng cách ngắn nhất giữa một điểm trên $(A)$ và một điểm trên $(B)$ bằng $%s\\text{ cm}$' % (fmt(r_ngoai), fmt(kc_ngan + 1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Khi $R = %s\\text{ cm}$, tổng hai bán kính là $%s + %s = %s\\text{ cm} < AB = %s\\text{ cm}$ nên hai đường tròn ở ngoài nhau. \\\\ Khoảng cách ngắn nhất giữa hai điểm bất kì trên hai đường tròn đạt được tại hai giao điểm của đoạn nối tâm $AB$ với $(A)$ và $(B)$, giá trị bằng $AB - (AM + R) = %s - %s = %s\\text{ cm}$.""" % (fmt(r_ngoai), fmt(am), fmt(r_ngoai), fmt(am + r_ngoai), fmt(ab), fmt(ab), fmt(am + r_ngoai), fmt(kc_ngan)))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
