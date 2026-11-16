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


def bt_dang14_p2_b1_c5_hh9(self):
    # Khai báo biến
    R1 = random.randint(4, 10)
    bc = 2 * R1

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (A) at (1.1,2.6);
\\coordinate (D) at (2.523,1.12);
\\coordinate (E) at (0.391,0.925);
\\coordinate (H) at (1.1,0.465);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (I) at ($(A)!0.5!(H)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt] (B)--(D) (C)--(E);
\\draw[line width=1pt, dashed] (E)--(D) (I)--(M);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[above right] {$D$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (I) circle (1pt) node[right] {$I$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho tam giác $ABC$ nhọn có $BC = %s\\text{ cm}$, hai đường cao $BD$ và $CE$ cắt nhau tại trực tâm $H$. Gọi $M$ là trung điểm của cạnh $BC$ và $I$ là trung điểm của đoạn thẳng $AH$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
%s''' % (bc, tikz_code))

    nb_da_1_d = '\\True Bốn điểm $B, E, D, C$ cùng thuộc đường tròn đường kính $BC$, bán kính $R = %s\\text{ cm}$' % R1
    nb_da_1_s = 'Bốn điểm $B, E, D, C$ cùng thuộc đường tròn tâm $M$, bán kính $R = %s\\text{ cm}$' % bc
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Hai tam giác $BEC$ vuông tại $E$ và $BDC$ vuông tại $D$ có chung cạnh huyền $BC$ và $M$ là trung điểm của $BC$ nên $MB = MC = ME = MD = \\dfrac{BC}{2} = %s\\text{ cm}$. Vậy $B, E, D, C$ cùng thuộc đường tròn đường kính $BC$.''' % R1)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Bốn điểm $A, E, H, D$ cùng thuộc đường tròn tâm $I$, đường kính $AH$'
    th_da_1_s = 'Bốn điểm $A, E, H, D$ cùng thuộc đường tròn tâm $M$, đường kính $BC$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Hai tam giác $AEH$ vuông tại $E$ và $ADH$ vuông tại $D$ có chung cạnh huyền $AH$ với trung điểm $I$ nên $IA = IE = IH = ID = \\dfrac{AH}{2}$. Do đó $A, E, H, D$ cùng thuộc đường tròn tâm $I$ đường kính $AH$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Hai điểm $D$ và $E$ luôn đối xứng với nhau qua đường thẳng $IM$'
    vd_da_1_s = 'Hai điểm $D$ và $E$ đối xứng với nhau qua đường thẳng $AH$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $ID = IE = \\dfrac{AH}{2}$ và $MD = ME = \\dfrac{BC}{2}$ nên $IM$ là đường trung trực của đoạn thẳng $DE$. Vậy $D$ và $E$ đối xứng với nhau qua đường thẳng $IM$.''')
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Độ dài đoạn thẳng $DE$ luôn nhỏ hơn $%s\\text{ cm}$' % bc
    vdc_da_1_s = 'Độ dài đoạn thẳng $DE$ luôn bằng $%s\\text{ cm}$' % R1
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì tam giác $ABC$ nhọn nên ba điểm $M, D, E$ không thẳng hàng. Áp dụng bất đẳng thức tam giác cho tam giác $MDE$, ta có $DE < MD + ME = %s + %s = %s\\text{ cm}$.''' % (R1, R1, bc))
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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
