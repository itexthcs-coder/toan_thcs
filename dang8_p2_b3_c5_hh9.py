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








def bt_dang8_p2_b3_c5_hh9(self):
    k = random.choice([2, 4, 6])
    BC_val = k * sqrt(3)
    R_val = Rational(k, 2) * sqrt(3)
    tong_l = Rational(120, 180) * R_val * pi
    Sq_de = Rational(1, 6) * (R_val**2) * pi
    St_de = Rational(R_val**2, 4) * sqrt(3)
    Svp_de = simplify(Sq_de - St_de)

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \coordinate (B) at (-2cm,0);
        \coordinate (C) at (2cm,0);
        \coordinate (A) at (90:3.464cm);
        \coordinate (D) at (120:2cm);
        \coordinate (E) at (60:2cm);
        \draw[thick] (A) -- (B) -- (C) -- cycle;
        \draw[thick] (C) arc (0:180:2cm);
        \fill (0,0) circle (1.5pt) node[below] {$O$};
        \node[above] at (A) {$A$};
        \node[below left] at (B) {$B$};
        \node[below right] at (C) {$C$};
        \node[above left] at (D) {$D$};
        \node[above right] at (E) {$E$};
    \end{tikzpicture}
    \end{center}""")

    noidungcauhoi = (r"""Cho tam giác đều $ABC$ có cạnh bằng $%s\text{ cm}$. Nửa đường tròn đường kính $BC$ tâm $O$ cắt hai cạnh $AB$ và $AC$ lần lượt tại $D$ và $E$ ($D \neq B, E \neq C$) (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % (latex(BC_val), hinh_ve))

    nb_da_1_d = '\\True Bán kính của nửa đường tròn đường kính $BC$ là $R = %s\\text{ cm}$' % latex(R_val)
    nb_da_1_s = 'Bán kính của nửa đường tròn đường kính $BC$ là $R = %s\\text{ cm}$' % latex(BC_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Bán kính của nửa đường tròn là $R = \dfrac{BC}{2} = \dfrac{%s}{2} = %s\text{ (cm)}$.""" % (latex(BC_val), latex(R_val)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Ba cung nhỏ $\\overset\\frown{BD}, \\overset\\frown{DE}, \\overset\\frown{EC}$ bằng nhau và mỗi cung có số đo bằng $60^\\circ$'
    th_da_1_s = 'Cung nhỏ $\\overset\\frown{DE}$ có số đo bằng $90^\\circ$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Các tam giác $OBD$ và $OCE$ cân có góc ở đáy bằng $60^\circ$ nên là các tam giác đều, suy ra $\widehat{BOD} = \widehat{COE} = 60^\circ \implies \widehat{DOE} = 60^\circ$. Vậy ba cung nhỏ $\overset\\frown{BD}, \overset\\frown{DE}, \overset\\frown{EC}$ bằng nhau và đều có số đo $60^\circ$.""" )
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tổng độ dài hai cung nhỏ $\\overset\\frown{BD}$ và $\\overset\\frown{EC}$ bằng $%s\\text{ cm}$' % latex(tong_l)
    vd_da_1_s = 'Tổng độ dài hai cung nhỏ $\\overset\\frown{BD}$ và $\\overset\\frown{EC}$ bằng $%s\\text{ cm}$' % latex(tong_l / 2)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Tổng số đo hai cung $\overset\\frown{BD}$ và $\overset\\frown{EC}$ là $120^\circ$, do đó tổng độ dài của chúng là $l = \dfrac{120}{180}\pi \cdot %s = %s\text{ (cm)}$.""" % (latex(R_val), latex(tong_l)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Diện tích hình viên phân giới hạn bởi dây $DE$ và cung nhỏ $\\overset\\frown{DE}$ bằng $%s\\text{ (cm}^2\\text{)}$' % latex(Svp_de)
    vdc_da_1_s = 'Diện tích hình viên phân giới hạn bởi dây $DE$ và cung nhỏ $\\overset\\frown{DE}$ bằng $%s\\text{ (cm}^2\\text{)}$' % latex(Sq_de)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Tam giác $ODE$ đều cạnh $R = %s\text{ cm}$ và góc ở tâm $\widehat{DOE} = 60^\circ$. \\ Diện tích hình viên phân cần tìm là $S = S_q - S_{\triangle ODE} = \dfrac{1}{6}\pi R^2 - \dfrac{R^2\sqrt{3}}{4} = %s\text{ (cm}^2\text{)}$.""" % (latex(R_val), latex(Svp_de)))
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
