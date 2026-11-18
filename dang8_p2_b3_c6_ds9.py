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

def bt_dang8_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a1 = random.choice([2, 3])
        b1 = random.choice([1, 2])
        c1 = random.choice([4, 6])
        k = random.choice([2, 3])
        a2, b2, c2_par = a1 * k, b1 * k, c1 * k + 3
        c2_coincide = c1 * k
        hsg = Rational(-a1, b1)

        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-1,0) -- (3.8,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,3.2) node[left] {$y$};
\\coordinate (O) at (0,0);
\\draw[line width=1pt] (-0.5,2.2) -- (2.5,-0.5) node[right] {$(d_1)$};
\\draw[line width=1pt] (-0.2,2.8) -- (3.2,-0.26) node[right] {$(d_2)$};
\\fill (O) circle (1pt) node[below left] {$O$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai phương trình bậc nhất hai ẩn $(1): %sx + %sy = %s$ và $(2): %sx + %sy = %s$ có đường thẳng biểu diễn tập nghiệm lần lượt là $(d_1)$ và $(d_2)$ (như hình vẽ minh họa). %s'''
                         % (a1, b1, c1, a2, b2, c2_par, hinh_ve))

        # Nhận biết
        nb_da_1_d = '\\True Hai đường thẳng $(d_1)$ và $(d_2)$ song song với nhau, kí hiệu $(d_1) // (d_2)$'
        nb_da_1_s = 'Hai đường thẳng $(d_1)$ và $(d_2)$ cắt nhau tại một điểm duy nhất'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $(d_1): y = %sx + %s$ và $(d_2): y = %sx + %s$. Vì hai đường thẳng có cùng hệ số góc $%s$ và tung độ gốc khác nhau ($%s \\neq %s$) nên $(d_1) // (d_2)$.'''
                        % (latex(hsg), latex(Rational(c1, b1)), latex(hsg), latex(Rational(c2_par, b2)), latex(hsg), latex(Rational(c1, b1)), latex(Rational(c2_par, b2))))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Không có cặp số $(x; y)$ nào đồng thời là nghiệm của cả hai phương trình $(1)$ và $(2)$'
        th_da_1_s = 'Có vô số cặp số $(x; y)$ đồng thời là nghiệm của cả hai phương trình $(1)$ và $(2)$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Do hai đường thẳng $(d_1)$ và $(d_2)$ song song với nhau nên chúng không có điểm chung, nghĩa là hai phương trình đã cho không có nghiệm chung.'''
                        % ())
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Đường thẳng biểu diễn tập nghiệm của phương trình $%sx + %sy = %s$ trùng với đường thẳng $(d_1)$' % (a2, b2, c2_coincide)
        vd_da_1_s = 'Đường thẳng biểu diễn tập nghiệm của phương trình $%sx + %sy = %s$ vuông góc với đường thẳng $(d_1)$' % (a2, b2, c2_coincide)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Chia cả hai vế của phương trình $%sx + %sy = %s$ cho $%s$ ta được phương trình $%sx + %sy = %s$, do đó hai phương trình có cùng tập nghiệm nên hai đường thẳng biểu diễn trùng nhau.'''
                        % (a2, b2, c2_coincide, k, a1, b1, c1))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Hai đường thẳng $(d_1)$ và $(d_2)$ có cùng hệ số góc bằng $%s$' % (latex(hsg))
        vdc_da_1_s = 'Hai đường thẳng $(d_1)$ và $(d_2)$ có hai hệ số góc đối nhau'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Từ phương trình $(1)$ rút $y$ theo $x$ ta được $y = %sx + %s$, suy ra hệ số góc của $(d_1)$ và $(d_2)$ đều bằng $%s$.'''
                         % (latex(hsg), latex(Rational(c1, b1)), latex(hsg)))
        list_vdc_2 = [loigiai_vdc_1]

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
