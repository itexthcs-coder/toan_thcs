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








def bt_dang14_p2_b3_c5_hh9(self):
    d1, n1 = 20, 6
    d2, n2 = 30, 10
    R1, R2 = d1 // 2, d2 // 2
    goc1, goc2 = 360 // n1, 360 // n2

    S1 = Rational(1, n1) * (R1**2) * pi
    S2 = Rational(1, n2) * (R2**2) * pi

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \draw[thick] (-2.2,0) circle (1.2cm);
        \foreach \a in {0,60,...,300} \draw (-2.2,0) -- ++(\a:1.2cm);
        \node[below] at (-2.2,-1.3) {\scriptsize Bánh cỡ vừa};
        \draw[thick] (2.2,0) circle (1.6cm);
        \foreach \a in {0,36,...,324} \draw (2.2,0) -- ++(\a:1.6cm);
        \node[below] at (2.2,-1.7) {\scriptsize Bánh cỡ lớn};
    \end{tikzpicture}
    \end{center}""")

    noidungcauhoi = (r"""Một cửa hàng bán hai cỡ bánh pizza hình tròn cùng độ dày. Bánh cỡ vừa có đường kính $%d\text{ cm}$ được cắt thành $%d$ miếng đều nhau dạng hình quạt tròn; bánh cỡ lớn có đường kính $%d\text{ cm}$ được cắt thành $%d$ miếng đều nhau dạng hình quạt tròn (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % (d1, n1, d2, n2, hinh_ve))

    nb_da_1_d = '\\True Mỗi miếng bánh cỡ vừa có góc ở tâm bằng $%d^\\circ$ và bán kính $%d\\text{ cm}$' % (goc1, R1)
    nb_da_1_s = 'Mỗi miếng bánh cỡ vừa có góc ở tâm bằng $%d^\\circ$ và bán kính $%d\\text{ cm}$' % (goc1, d1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Bánh cỡ vừa có bán kính $R_1 = \dfrac{%d}{2} = %d\text{ (cm)}$ và chia làm %d phần nên góc ở tâm mỗi miếng là $\dfrac{360^\circ}{%d} = %d^\circ$.""" % (d1, R1, n1, n1, goc1))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích bề mặt của một miếng bánh cỡ vừa là $%s\\text{ cm}^2$' % latex(S1)
    th_da_1_s = 'Diện tích bề mặt của một miếng bánh cỡ vừa là $%s\\text{ cm}^2$' % latex(2 * S1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Diện tích bề mặt một miếng bánh cỡ vừa là $S_1 = \dfrac{1}{%d}\pi \cdot %d^2 = %s\text{ (cm}^2\text{)}$.""" % (n1, R1, latex(S1)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích bề mặt của một miếng bánh cỡ lớn là $%s\\text{ cm}^2$' % latex(S2)
    vd_da_1_s = 'Diện tích bề mặt của một miếng bánh cỡ lớn là $%s\\text{ cm}^2$' % latex(Rational(45, 2) * pi + 5*pi)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Bánh cỡ lớn có bán kính $R_2 = %d\text{ cm}$, diện tích một miếng là $S_2 = \dfrac{1}{%d}\pi \cdot %d^2 = %s\text{ (cm}^2\text{)}$.""" % (R2, n2, R2, latex(S2)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Diện tích bề mặt của $3$ miếng bánh cỡ vừa lớn hơn diện tích bề mặt của $2$ miếng bánh cỡ lớn'
    vdc_da_1_s = 'Diện tích bề mặt của $3$ miếng bánh cỡ vừa nhỏ hơn diện tích bề mặt của $2$ miếng bánh cỡ lớn'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Diện tích $3$ miếng bánh cỡ vừa là $3 \cdot %s = 50\pi\text{ (cm}^2\text{)}$, còn diện tích $2$ miếng bánh cỡ lớn là $2 \cdot %s = 45\pi\text{ (cm}^2\text{)}$. Vì $50\pi > 45\pi$ nên khẳng định đúng.""" % (latex(S1), latex(S2)))
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
