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


def bt_dang18_p2_b1_c4_hh8(self):
    n = random.choice([4, 5])
    nc_10 = random.choice([12, 15])
    cb_10 = nc_10 * n
    mn_10 = 15
    ab_10 = mn_10 * n
    mn2_10 = 20
    nc2_10 = (mn2_10 * cb_10) // ab_10

    nc_s = str(nc_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
    cb_s = str(cb_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
    mn_s = str(mn_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
    ab_s = str(ab_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
    mn2_s = str(mn2_10 / 10).rstrip('0').rstrip('.').replace('.', ',')
    nc2_s = str(nc2_10 / 10).rstrip('0').rstrip('.').replace('.', ',')

    noidungcauhoi = ("""Vào một thời điểm buổi sáng, tia nắng mặt trời chiếu xiên tạo với mặt đất phẳng một góc không đổi, các tia nắng được coi là song song với nhau. Một cột đèn đường thẳng đứng $AB$ có bóng in trên mặt đất là đoạn $BC = %s\\text{ m}$. Cùng lúc đó, một cọc tiêu $MN$ cao $%s\\text{ m}$ cắm thẳng đứng trên mặt đất (sao cho điểm $M$ nằm trên đoạn $AC$ và điểm $N$ nằm trên đoạn $BC$) có bóng in trên mặt đất là đoạn $NC = %s\\text{ m}$ (như hình vẽ bên dưới). Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (A) at (0,3);
\\coordinate (C) at (4.8,0);
\\coordinate (N) at (3.6,0);
\\coordinate (M) at (3.6,0.75);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (3.6,0.25)--(3.85,0.25)--(3.85,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\end{tikzpicture}
\\end{center}"""
                     % (cb_s, mn_s, nc_s))

    nb_da_1_d = '\\True $MN // AB$ vì cả hai cùng vuông góc với mặt đất $BC$'
    nb_da_1_s = '$MN // AC$ vì cả hai cùng vuông góc với mặt đất $BC$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì cột đèn $AB$ và cọc tiêu $MN$ cùng cắm thẳng đứng vuông góc với mặt đất $BC$ nên $MN // AB$.""")

    th_da_1_d = '\\True Tỉ số $\\dfrac{CN}{CB}$ bằng $\\dfrac{1}{%s}$' % (n)
    th_da_1_s = 'Tỉ số $\\dfrac{CN}{CB}$ bằng $\\dfrac{1}{%s}$' % (n + 1)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Ta có tỉ số $\\dfrac{CN}{CB} = \\dfrac{%s}{%s} = \\dfrac{1}{%s}$."""
                    % (nc_s, cb_s, n))

    vd_da_1_d = '\\True Độ dài đoạn thẳng $AM$ gấp $%s$ lần độ dài đoạn thẳng $MC$' % (n - 1)
    vd_da_1_s = 'Độ dài đoạn thẳng $AM$ gấp $%s$ lần độ dài đoạn thẳng $MC$' % (n)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Xét $\\Delta CAB$ có $MN // AB$, theo định lí Thalès trong tam giác ta có $\\dfrac{CM}{MA} = \\dfrac{CN}{NB} = \\dfrac{%s}{%s - %s} = \\dfrac{1}{%s}$, suy ra $AM = %s MC$."""
                    % (nc_s, cb_s, nc_s, n - 1, n - 1))

    vdc_da_1_d = '\\True Nếu thay cọc tiêu $MN$ bằng một cọc cao $%s\\text{ m}$ cắm thẳng đứng tại vị trí $N\'$ trên đoạn $BC$ sao cho đỉnh cọc $M\'$ vẫn chạm tia nắng $AC$, thì khoảng cách $N\'C$ bằng $%s\\text{ m}$' % (mn2_s, nc2_s)
    vdc_da_1_s = 'Nếu thay cọc tiêu $MN$ bằng một cọc cao $%s\\text{ m}$ cắm thẳng đứng tại vị trí $N\'$ trên đoạn $BC$ sao cho đỉnh cọc $M\'$ vẫn chạm tia nắng $AC$, thì khoảng cách $N\'C$ bằng $%s\\text{ m}$' % (mn2_s, str((nc2_10 + 4) / 10).rstrip('0').rstrip('.').replace('.', ','))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Chiều cao cột đèn $AB$ là $AB = %s \\cdot %s = %s\\text{ (m)}$. \\\\ Khi đặt cọc cao $%s\\text{ m}$ tại $N'$, áp dụng định lí Thalès ta có $\\dfrac{N'C}{BC} = \\dfrac{M'N'}{AB} = \\dfrac{%s}{%s} = \\dfrac{1}{%s} \\Rightarrow N'C = \\dfrac{%s}{%s} = %s\\text{ (m)}$."""
                     % (n, mn_s, ab_s, mn2_s, mn2_s, ab_s, ab_10 // mn2_10, cb_s, ab_10 // mn2_10, nc2_s))

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

    combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
    combined_th = list(zip([th_da_1], [loigiai_th_1]))
    combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
    combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
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
