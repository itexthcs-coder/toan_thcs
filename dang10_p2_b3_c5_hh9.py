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








def bt_dang10_p2_b3_c5_hh9(self):
    a_val = random.choice([2, 4, 6, 8])
    Sq_val = Rational(1, 4) * (a_val**2) * pi
    St_val = Rational(1, 2) * (a_val**2)
    Svp_val = Sq_val - St_val
    S_la = 2 * Svp_val
    ti_so = simplify(S_la / (a_val**2))

    hinh_ve = (r"""\begin{center}
    \begin{tikzpicture}[scale=0.8]
        \coordinate (A) at (0,0);
        \coordinate (B) at (2.4cm,0);
        \coordinate (C) at (2.4cm,2.4cm);
        \coordinate (D) at (0,2.4cm);
        \fill[green!25] (B) arc (0:90:2.4cm) -- (D) arc (180:270:2.4cm) -- cycle;
        \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
        \draw[thick] (B) arc (0:90:2.4cm);
        \draw[thick] (D) arc (180:270:2.4cm);
        \draw[dashed] (B) -- (D);
        \node[below left] at (A) {$A$};
        \node[below right] at (B) {$B$};
        \node[above right] at (C) {$C$};
        \node[above left] at (D) {$D$};
    \end{tikzpicture}
    \end{center}""")

    noidungcauhoi = (r"""Cho hình vuông $ABCD$ cạnh $a = %d\text{ cm}$. Vẽ hai cung tròn tâm $A$ và tâm $C$ cùng có bán kính bằng $%d\text{ cm}$ nằm bên trong hình vuông, hai cung này cắt nhau tại $B$ và $D$ tạo thành một phần giao nhau ở giữa (phần tô màu như hình vẽ). Xét tính đúng sai của các khẳng định sau:
    %s""" % (a_val, a_val, hinh_ve))

    nb_da_1_d = '\\True Diện tích của một hình quạt tròn tâm $A$, bán kính $AB = %d\\text{ cm}$, cung $\\overset\\frown{BD}$ bằng $%s\\text{ cm}^2$' % (a_val, latex(Sq_val))
    nb_da_1_s = 'Diện tích của một hình quạt tròn tâm $A$, bán kính $AB = %d\\text{ cm}$, cung $\\overset\\frown{BD}$ bằng $%s\\text{ cm}^2$' % (a_val, latex(2 * Sq_val))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = (r"""Hình quạt tròn $ABD$ ứng với cung $90^\circ$, bán kính %d\text{ cm} có diện tích $S_q = \dfrac{90}{360}\pi \cdot %d^2 = %s\text{ (cm}^2\text{)}$.""" % (a_val, a_val, latex(Sq_val)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Diện tích hình viên phân giới hạn bởi cung nhỏ $\\overset\\frown{BD}$ (tâm $A$) và dây $BD$ bằng $%s\\text{ (cm}^2\\text{)}$' % latex(Svp_val)
    th_da_1_s = 'Diện tích hình viên phân giới hạn bởi cung nhỏ $\\overset\\frown{BD}$ (tâm $A$) và dây $BD$ bằng $%s\\text{ (cm}^2\\text{)}$' % latex(Sq_val + St_val)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = (r"""Diện tích một nửa phần giao nhau (hình viên phân) là $S_{vp} = S_q - S_{\triangle ABD} = %s - %s = %s\text{ (cm}^2\text{)}$.""" % (latex(Sq_val), latex(St_val), latex(Svp_val)))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Diện tích phần giao nhau của hai hình quạt tròn bằng $%s\\text{ (cm}^2\\text{)}$' % latex(S_la)
    vd_da_1_s = 'Diện tích phần giao nhau của hai hình quạt tròn bằng $%s\\text{ (cm}^2\\text{)}$' % latex(Svp_val)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = (r"""Diện tích phần giao nhau gồm hai hình viên phân bằng nhau nên $S = 2S_{vp} = %s\text{ (cm}^2\text{)}$.""" % latex(S_la))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Tỉ số giữa diện tích phần giao nhau và diện tích hình vuông $ABCD$ bằng $%s$' % latex(ti_so)
    vdc_da_1_s = 'Tỉ số giữa diện tích phần giao nhau và diện tích hình vuông $ABCD$ bằng $%s$' % latex(Rational(1, 2) * pi)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = (r"""Diện tích hình vuông $ABCD$ là $a^2 = %d\text{ cm}^2$. \\ Tỉ số cần tìm là $\dfrac{%s}{%d} = %s$.""" % (a_val**2, latex(S_la), a_val**2, latex(ti_so)))
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
