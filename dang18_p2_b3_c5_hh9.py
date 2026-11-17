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








def bt_dang18_p2_b3_c5_hh9(self):
    d_bon = random.choice([6, 8, 10])
    r_trong = d_bon // 2
    be_rong = random.choice([1, 2])
    R_ngoai = r_trong + be_rong

    S_loi = (R_ngoai**2 - r_trong**2) * pi
    C_ngoai = round(2 * 3.14 * R_ngoai, 2)
    don_gia = 250000
    chi_phi = int(round((R_ngoai**2 - r_trong**2) * 3.14 * don_gia))

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \fill[gray!30] (0,0) circle (2cm);
        \fill[green!30] (0,0) circle (1.3cm);
        \draw[thick] (0,0) circle (2cm);
        \draw[thick] (0,0) circle (1.3cm);
        \node at (0,0) {\scriptsize Bồn hoa};
    \end{tikzpicture}
    \end{center}"""())

    noidungcauhoi = (r"""Trong một công viên, người ta xây một bồn hoa hình tròn có đường kính $%d\text{ m}$. Xung quanh bồn hoa, người ta làm một lối đi lát gạch dạng hình vành khuyên có bề rộng lối đi là $%d\text{ m}$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % (d_bon, be_rong, hinh_ve))

    nb_da_1_d = '\\True Bán kính vòng trong của lối đi bằng $%d\\text{ m}$ và bán kính vòng ngoài của lối đi bằng $%d\\text{ m}$' % (r_trong, R_ngoai)
    nb_da_1_s = 'Bán kính vòng trong của lối đi bằng $%d\\text{ m}$ và bán kính vòng ngoài của lối đi bằng $%d\\text{ m}$' % (d_bon, d_bon + be_rong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Bán kính vòng trong bằng bán kính bồn hoa $r = \dfrac{%d}{2} = %d\text{ (m)}$, bán kính vòng ngoài là $R = %d + %d = %d\text{ (m)}$.""" % (d_bon, r_trong, r_trong, be_rong, R_ngoai))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích bề mặt lối đi lát gạch bằng $%s\\text{ m}^2$' % latex(S_loi)
    th_da_1_s = 'Diện tích bề mặt lối đi lát gạch bằng $%s\\text{ m}^2$' % latex(((R_ngoai - r_trong)**2)*pi)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Diện tích lối đi hình vành khuyên là $S_v = \pi(%d^2 - %d^2) = %s\text{ (m}^2\text{)}$.""" % (R_ngoai, r_trong, latex(S_loi)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Chu vi mép ngoài của lối đi (lấy $\\pi \\approx 3,14$) bằng $%.2f\\text{ m}$' % C_ngoai
    vd_da_1_s = 'Chu vi mép ngoài của lối đi (lấy $\\pi \\approx 3,14$) bằng $%.2f\\text{ m}$' % (C_ngoai / 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Chu vi mép ngoài của lối đi là $C = 2\pi R \approx 2 \cdot 3,14 \cdot %d = %.2f\text{ (m)}$.""" % (R_ngoai, C_ngoai))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu chi phí lát gạch hoàn thiện là $250\\,000\\text{ đồng/m}^2$ (lấy $\\pi \\approx 3,14$) thì tổng chi phí làm lối đi là $%s\\text{ đồng}$' % f"{chi_phi:,}".replace(",", "\,")
    vdc_da_1_s = 'Nếu chi phí lát gạch hoàn thiện là $250\\,000\\text{ đồng/m}^2$ (lấy $\\pi \\approx 3,14$) thì tổng chi phí làm lối đi là $%s\\text{ đồng}$' % f"{chi_phi + 2500000:,}".replace(",", "\,")
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Diện tích lối đi gần đúng là $%d \cdot 3,14 = %.2f\text{ m}^2$. \\ Tổng chi phí làm lối đi là $%.2f \cdot 250\,000 = %s\text{ (đồng)}$.""" % (R_ngoai**2 - r_trong**2, (R_ngoai**2 - r_trong**2)*3.14, (R_ngoai**2 - r_trong**2)*3.14, f"{chi_phi:,}".replace(",", "\,")))
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
