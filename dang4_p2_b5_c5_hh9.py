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


def bt_dang4_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    k = random.randint(1, 4)
    R = 3 * k
    r = 1 * k
    oo1 = R + r
    bc_expr = 2 * sqrt(R * r)

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O') at (4,0);
\\coordinate (A) at (3,0);
\\coordinate (B) at (1.5,2.598);
\\coordinate (C) at (4.5,0.866);
\\coordinate (H) at (0.5,0.866);
\\draw[line width=1pt] (O) circle (3cm);
\\draw[line width=1pt] (O') circle (1cm);
\\draw[line width=1pt] (O)--(O');
\\draw[line width=1pt] (B)--(C);
\\draw[line width=1pt] (O)--(B) (O')--(C);
\\draw[line width=1pt, dashed] (O')--(H) (A)--(B) (A)--(C);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O') circle (1pt) node[right] {$O'$};
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (H) circle (1pt) node[left] {$H$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Cho hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc ngoài tại điểm $A$. Kẻ tiếp tuyến chung ngoài $BC$ với $B \\in (O)$ và $C \\in (O')$.
%s""" % (fmt(R), fmt(r), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Độ dài đoạn nối tâm $OO\'$ bằng $%s\\text{ cm}$' % (fmt(oo1))
    nb_da_1_s = 'Độ dài đoạn nối tâm $OO\'$ bằng $%s\\text{ cm}$' % (fmt(R - r))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Vì hai đường tròn $(O; %s\\text{ cm})$ và $(O'; %s\\text{ cm})$ tiếp xúc ngoài tại $A$ nên điểm $A$ nằm giữa $O$ và $O'$, suy ra $OO' = R + r = %s + %s = %s\\text{ cm}$.""" % (fmt(R), fmt(r), fmt(R), fmt(r), fmt(oo1)))

    # Thông hiểu
    th_da_1_d = '\\True Tứ giác $OBCO\'$ là một hình thang vuông'
    th_da_1_s = 'Tứ giác $OBCO\'$ là một hình chữ nhật'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì $BC$ là tiếp tuyến chung của $(O)$ tại $B$ và $(O')$ tại $C$ nên $OB \\perp BC$ và $O'C \\perp BC$. Suy ra $OB // O'C$ và $\\widehat{OBC} = \\widehat{O'CB} = 90^\\circ$. Do đó tứ giác $OBCO'$ là hình thang vuông.""")

    # Vận dụng
    vd_da_1_d = '\\True Độ dài đoạn tiếp tuyến chung ngoài $BC$ bằng $%s\\text{ cm}$' % (latex(bc_expr))
    vd_da_1_s = 'Độ dài đoạn tiếp tuyến chung ngoài $BC$ bằng $%s\\text{ cm}$' % (fmt(oo1))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Kẻ $O'H \\perp OB$ tại $H$. Tứ giác $HBCO'$ có ba góc vuông nên là hình chữ nhật, suy ra $O'H = BC$ và $BH = O'C = %s\\text{ cm}$, do đó $OH = OB - BH = %s - %s = %s\\text{ cm}$. \\\\ Áp dụng định lí Pythagore trong tam giác vuông $OHO'$, ta có: $BC = O'H = \\sqrt{OO'^2 - OH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$.""" % (fmt(r), fmt(R), fmt(r), fmt(R - r), fmt(oo1), fmt(R - r), latex(bc_expr)))

    # Vận dụng cao
    vdc_da_1_d = '\\True Tam giác $ABC$ là tam giác vuông tại $A$'
    vdc_da_1_s = 'Tam giác $ABC$ là tam giác đều'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Kẻ tiếp tuyến chung trong tại $A$ cắt $BC$ tại $M$. Theo tính chất hai tiếp tuyến cắt nhau của $(O)$ và $(O')$, ta có $MA = MB$ và $MA = MC$, suy ra $MA = MB = MC = \\frac{1}{2}BC$. \\\\ Tam giác $ABC$ có đường trung tuyến $AM$ bằng nửa cạnh đối diện $BC$ nên tam giác $ABC$ vuông tại $A$.""")

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
