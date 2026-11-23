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


def bt_dang17_p2_b1_c4_hh8(self):
    ab_dec = random.choice([2.4, 3.0, 3.6])
    ab_10 = int(round(ab_dec * 10))
    ad_10 = ab_10 // 3
    mb_10 = ab_10 // 4
    en_10 = ab_10 - ad_10 - mb_10
    ab_s = str(ab_dec).replace('.', ',')
    ad_s = str(ad_10 / 10).replace('.', ',')
    mb_s = str(mb_10 / 10).replace('.', ',')
    en_s = str(en_10 / 10).replace('.', ',')
    ts_ae_nc = Rational(ad_10, mb_10)

    noidungcauhoi = ("""Một chiếc thang gấp chữ A có hai chân bên $AB$ và $AC$ đều dài $%s\\text{ m}$ (coi như hai đoạn thẳng cắt nhau tại đỉnh $A$). Để đảm bảo an toàn và chống trượt khi sử dụng, người thợ lắp thêm hai thanh giằng ngang $DE$ và $MN$ cùng song song với mặt đất phẳng $BC$ ($D, M \\in AB$ và $E, N \\in AC$) như hình vẽ bên dưới. Biết vị trí chốt $D$ cách đỉnh $A$ một khoảng $AD = %s\\text{ m}$ và vị trí chốt $M$ cách chân $B$ một khoảng $MB = %s\\text{ m}$. Xét tính đúng, sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.8,3.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (D) at ($(A)!0.3333!(B)$);
\\coordinate (E) at ($(A)!0.3333!(C)$);
\\coordinate (M) at ($(A)!0.75!(B)$);
\\coordinate (N) at ($(A)!0.75!(C)$);
\\draw[line width=1pt] (A)--(B) (A)--(C) (D)--(E) (M)--(N);
\\draw[line width=1pt, dashed] (B)--(C);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[right] {$E$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\end{tikzpicture}
\\end{center}"""
                     % (ab_s, ad_s, mb_s))

    nb_da_1_d = '\\True Hai thanh giằng ngang $DE$ và $MN$ song song với nhau'
    nb_da_1_s = 'Hai thanh giằng ngang $DE$ và $MN$ cắt nhau'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Vì $DE // BC$ và $MN // BC$ nên hai thanh giằng ngang $DE$ và $MN$ song song với nhau.""")

    th_da_1_d = '\\True Chốt $E$ cách đỉnh $A$ một khoảng bằng $%s\\text{ m}$' % (ad_s)
    th_da_1_s = 'Chốt $E$ cách đỉnh $A$ một khoảng bằng $%s\\text{ m}$' % (mb_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Xét $\\Delta ABC$ có $DE // BC$, theo định lí Thalès ta có $\\dfrac{AE}{AC} = \\dfrac{AD}{AB}$. \\\\ Vì $AB = AC = %s\\text{ m}$ nên $AE = AD = %s\\text{ m}$."""
                    % (ab_s, ad_s))

    vd_da_1_d = '\\True Khoảng cách $EN$ giữa hai chốt trên chân thang $AC$ bằng $%s\\text{ m}$' % (en_s)
    vd_da_1_s = 'Khoảng cách $EN$ giữa hai chốt trên chân thang $AC$ bằng $%s\\text{ m}$' % (str((en_10 + 2) / 10).replace('.', ','))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tương tự, từ $MN // BC$ và $AB = AC$ suy ra $NC = MB = %s\\text{ m}$. \\\\ Do đó khoảng cách $EN$ giữa hai chốt trên chân thang $AC$ là $EN = AC - AE - NC = %s - %s - %s = %s\\text{ (m)}$."""
                    % (mb_s, ab_s, ad_s, mb_s, en_s))

    vdc_da_1_d = '\\True Tỉ số $\\dfrac{AE}{NC}$ bằng $%s$' % (latex(ts_ae_nc))
    vdc_da_1_s = 'Tỉ số $\\dfrac{AE}{NC}$ bằng $%s$' % (latex(Rational(mb_10, ad_10)))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Ta có tỉ số $\\dfrac{AE}{NC} = \\dfrac{%s}{%s} = %s$."""
                     % (ad_s, mb_s, latex(ts_ae_nc)))

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
