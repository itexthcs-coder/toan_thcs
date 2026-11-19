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




def bt_dang20_p2_b3_c5_hh9(self):
    R_m = Rational(8, 10)
    day_ab = R_m * sqrt(2)
    l_khung = Rational(1, 2) * R_m * pi
    Sq_kinh = Rational(1, 4) * (R_m**2) * pi
    St_kinh = Rational(1, 2) * (R_m**2)
    S_kinh = Sq_kinh - St_kinh
    S_kinh_tron = round(float(Rational(1, 4) * (0.8**2) * 3.14 - 0.5 * (0.8**2)), 2)

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.85]
        \fill[cyan!20] (45:2.2cm) arc (45:135:2.2cm) -- cycle;
        \draw[very thick] (45:2.2cm) arc (45:135:2.2cm);
        \draw[very thick] (45:2.2cm) -- (135:2.2cm);
        \draw[dashed] (0,0) -- (45:2.2cm);
        \draw[dashed] (0,0) -- (135:2.2cm);
        \fill (0,0) circle (1.5pt) node[below] {$O$};
    \end{tikzpicture}
    \end{center}""")

    noidungcauhoi = (r"""Một ô thoáng cửa sổ phía trên có dạng hình viên phân được giới hạn bởi một cung tròn có số đo $90^\circ$ của đường tròn bán kính $R = 0,8\text{ m}$ và một thanh ngang (dây căng cung đó, như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % hinh_ve)

    nb_da_1_d = '\\True Chiều dài thanh ngang (dây cung) của ô thoáng bằng $0,8\\sqrt{2}\\text{ m}$'
    nb_da_1_s = 'Chiều dài thanh ngang (dây cung) của ô thoáng bằng $1,6\text{ m}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Dây cung căng cung $90^\circ$ là cạnh huyền của tam giác vuông cân có cạnh góc vuông bằng $R = 0,8\text{ m}$ nên có độ dài bằng $0,8\sqrt{2}\text{ m}$.""" )
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Chiều dài phần khung uốn cong (cung tròn $90^\\circ$) của ô thoáng bằng $0,4\\pi\text{ m}$'
    th_da_1_s = 'Chiều dài phần khung uốn cong (cung tròn $90^\\circ$) của ô thoáng bằng $0,8\\pi\\text{ m}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Độ dài cung tròn $90^\circ$ bán kính $0,8\text{ m}$ là $l = \dfrac{90}{180}\pi \cdot 0,8 = 0,4\pi\text{ (m)}$.""" )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích phần kính cần lắp cho ô thoáng (hình viên phân) bằng $0,16\\pi - 0,32\text{ (m}^2\\text{)}$'
    vd_da_1_s = 'Diện tích phần kính cần lắp cho ô thoáng (hình viên phân) bằng $0,16\\pi - 0,64\\text{ (m}^2\\text{)}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Diện tích hình viên phân là $S = \dfrac{1}{4}\pi \cdot 0,8^2 - \dfrac{1}{2} \cdot 0,8^2 = 0,16\pi - 0,32\text{ (m}^2\text{)}$.""" )
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu lấy $\\pi \\approx 3,14$ thì diện tích phần kính của ô thoáng (làm tròn đến hàng phần trăm) là $%.2f\\text{ m}^2$' % S_kinh_tron
    vdc_da_1_s = 'Nếu lấy $\\pi \\approx 3,14$ thì diện tích phần kính của ô thoáng (làm tròn đến hàng phần trăm) là $%.2f\\text{ m}^2$' % (S_kinh_tron + 0.14)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Thay $\pi \approx 3,14$, ta được $S \approx 0,16 \cdot 3,14 - 0,32 = 0,5024 - 0,32 = 0,1824 \approx %.2f\text{ (m}^2\text{)}$.""" % S_kinh_tron)
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
