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








def bt_dang12_p2_b3_c5_hh9(self):
    d_mm = random.choice([600, 700])
    d_m = Rational(d_mm, 1000)
    C_xe = d_m * pi
    r_lip = random.choice([4, 5])
    ti_so_vong = random.choice([3, 4])
    r_dia = r_lip * ti_so_vong
    so_vong_dap = random.choice([10, 20])
    tong_vong_bx = so_vong_dap * ti_so_vong
    quang_duong = round(float(tong_vong_bx * d_m * 3.14), 1)

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \draw[thick] (0,0) circle (0.6cm);
        \node at (0,0) {\scriptsize Líp};
        \draw[thick] (3.2cm,0) circle (1.1cm);
        \node at (3.2cm,0) {\scriptsize Giò đĩa};
        \draw[thick] (0,0.6cm) -- (3.2cm,1.1cm);
        \draw[thick] (0,-0.6cm) -- (3.2cm,-1.1cm);
    \end{tikzpicture}
    \end{center}"""())

    noidungcauhoi = (r"""Một chiếc xe đạp thể thao có bánh xe (khi bơm căng) đường kính $%d\text{ mm}$. Bộ truyền chuyển động gồm giò đĩa có bán kính $%d\text{ cm}$ và líp gắn với bánh xe sau có bán kính $%d\text{ cm}$ (như hình vẽ). Khi người đi xe đạp đều đặn $%d$ vòng giò đĩa, xét tính đúng sai của các khẳng định sau:
    %s""" % (d_mm, r_dia, r_lip, so_vong_dap, hinh_ve))

    nb_da_1_d = '\\True Chu vi của bánh xe đạp là $%s\\text{ m}$' % latex(C_xe)
    nb_da_1_s = 'Chu vi của bánh xe đạp là $%s\\text{ m}$' % latex(2 * C_xe)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Đổi $%d\text{ mm} = %s\text{ m}$. Chu vi bánh xe là $C = \pi d = %s\text{ (m)}$.""" % (d_mm, latex(d_m), latex(C_xe)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khi giò đĩa quay $1$ vòng thì bánh xe sau quay được $%d$ vòng' % ti_so_vong
    th_da_1_s = 'Khi giò đĩa quay $1$ vòng thì bánh xe sau quay được $%d$ vòng' % (ti_so_vong + 1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Khi giò đĩa quay $1$ vòng, độ dài xích dịch chuyển bằng chu vi giò đĩa $2\pi \cdot %d$, làm líp (và bánh xe sau) quay số vòng là $\dfrac{2\pi \cdot %d}{2\pi \cdot %d} = %d$ (vòng).""" % (r_dia, r_dia, r_lip, ti_so_vong))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Khi người đi xe đạp $%d$ vòng giò đĩa thì bánh xe quay được $%d$ vòng' % (so_vong_dap, tong_vong_bx)
    vd_da_1_s = 'Khi người đi xe đạp $%d$ vòng giò đĩa thì bánh xe quay được $%d$ vòng' % (so_vong_dap, so_vong_dap)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Khi đạp $%d$ vòng giò đĩa, bánh xe quay được $%d \cdot %d = %d$ (vòng).""" % (so_vong_dap, so_vong_dap, ti_so_vong, tong_vong_bx))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Quãng đường chiếc xe đạp di chuyển được (làm tròn đến hàng phần chục, lấy $\\pi \\approx 3,14$) là $%.1f\\text{ m}$' % quang_duong
    vdc_da_1_s = 'Quãng đường chiếc xe đạp di chuyển được (làm tròn đến hàng phần chục, lấy $\\pi \\approx 3,14$) là $%.1f\\text{ m}$' % (quang_duong + 10.5)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Quãng đường xe di chuyển được là $S = %d \cdot %s \approx %d \cdot %s \cdot 3,14 \approx %.1f\text{ (m)}$.""" % (tong_vong_bx, latex(C_xe), tong_vong_bx, latex(d_m), quang_duong))
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
