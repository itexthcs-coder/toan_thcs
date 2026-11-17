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
from PyQt5.QtGui import QTextCursor, QFont
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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D








def bt_dang15_p2_b3_c5_hh9(self):
    R_dm = Rational(24, 10)
    giay_dm = Rational(16, 10)
    r_dm = R_dm - giay_dm
    goc_quat = 150
    ti_so = Rational(goc_quat, 360)
    S_giay = ti_so * (R_dm**2 - r_dm**2) * pi
    S_tron = round(float(ti_so * (R_dm**2 - r_dm**2) * 3.14), 2)

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.85]
        \fill[cyan!25] (15:2.2cm) arc (15:165:2.2cm) -- (165:0.75cm) arc (165:15:0.75cm) -- cycle;
        \draw[thick] (0,0) -- (15:2.2cm) arc (15:165:2.2cm) -- cycle;
        \draw[thick] (15:0.75cm) arc (15:165:0.75cm);
        \foreach \a in {30,45,...,150} \draw (0,0) -- (\a:2.2cm);
        \fill (0,0) circle (1.5pt);
    \end{tikzpicture}
    \end{center}""")

    noidungcauhoi = (r"""Một chiếc quạt giấy truyền thống khi xòe hết cỡ tạo thành một hình quạt tròn có góc ở tâm bằng $150^\circ$ và bán kính nan quạt dài $2,4\text{ dm}$. Biết rằng khi gấp lại, phần giấy dán trên nan quạt có chiều dài $1,6\text{ dm}$ tính từ mép ngoài vào (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % hinh_ve)

    nb_da_1_d = '\\True Phần không dán giấy ở phía tay cầm tạo thành một hình quạt tròn nhỏ có bán kính $0,8\\text{ dm}$'
    nb_da_1_s = 'Phần không dán giấy ở phía tay cầm tạo thành một hình quạt tròn nhỏ có bán kính $1,6\\text{ dm}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Bán kính phần không dán giấy ở tay cầm là $r = 2,4 - 1,6 = 0,8\text{ (dm)}$.""" )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích phần giấy của chiếc quạt bằng $\\dfrac{5}{12}$ diện tích hình vành khuyên tạo bởi hai đường tròn đồng tâm bán kính $2,4\\text{ dm}$ và $0,8\\text{ dm}$'
    th_da_1_s = 'Diện tích phần giấy của chiếc quạt bằng $\\dfrac{1}{2}$ diện tích hình vành khuyên tạo bởi hai đường tròn đồng tâm bán kính $2,4\\text{ dm}$ và $0,8\\text{ dm}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Vì góc xòe của quạt là $150^\circ$ nên diện tích phần giấy chiếm tỉ lệ $\dfrac{150}{360} = \dfrac{5}{12}$ diện tích hình vành khuyên tương ứng.""" )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích phần giấy của chiếc quạt bằng $%s\\text{ dm}^2$' % latex(S_giay)
    vd_da_1_s = 'Diện tích phần giấy của chiếc quạt bằng $%s\\text{ dm}^2$' % latex(S_giay * 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Diện tích phần giấy là $S = \dfrac{5}{12}\pi(2,4^2 - 0,8^2) = \dfrac{5}{12}\pi(5,76 - 0,64) = %s\text{ (dm}^2\text{)}$.""" % latex(S_giay))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu lấy $\\pi \\approx 3,14$ thì diện tích phần kính của chiếc quạt (làm tròn đến hàng phần trăm) là $%.2f\\text{ dm}^2$' % S_tron
    vdc_da_1_s = 'Nếu lấy $\\pi \\approx 3,14$ thì diện tích phần kính của chiếc quạt (làm tròn đến hàng phần trăm) là $%.2f\\text{ dm}^2$' % (S_tron + 1.25)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Thay $\pi \approx 3,14$, ta được $S \approx \dfrac{32 \cdot 3,14}{15} \approx %.2f\text{ (dm}^2\text{)}$.""" % S_tron)
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
