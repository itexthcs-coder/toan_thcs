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


def bt_dang13_p2_b1_c5_hh9(self):
    # Khai báo biến
    nua_R = random.randint(2, 6)
    R = 2 * nua_R
    dk = 2 * R

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.6,0);
\\coordinate (M) at (55:1.6);
\\coordinate (N) at ($(A)!0.5!(M)$);
\\coordinate (I) at ($(O)!0.5!(A)$);
\\draw[line width=1pt] (O) circle (1.6);
\\draw[line width=1pt] (O)--(A);
\\draw[line width=1pt] (A)--(M);
\\draw[line width=1pt, dashed] (O)--(M) (I)--(N);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (N) circle (1pt) node[above left] {$N$};
\\fill (I) circle (1pt) node[below] {$I$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ cố định và điểm $A$ nằm trên $(O)$. Khi điểm $M$ di động trên đường tròn $(O)$, gọi $N$ là trung điểm của đoạn thẳng $AM$ và $P$ là điểm đối xứng với $A$ qua $M$ (minh họa như hình vẽ). Xét tính đúng sai của các khẳng định sau:
%s''' % (R, tikz_code))

    nb_da_1_d = '\\True Khi $M$ trùng với điểm đối xứng của $A$ qua $O$ thì độ dài $AM$ đạt giá trị lớn nhất bằng $%s\\text{ cm}$' % dk
    nb_da_1_s = 'Độ dài đoạn thẳng $AM$ luôn không đổi bằng $%s\\text{ cm}$ khi $M$ di động trên $(O)$' % dk
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta luôn có $AM \\le OA + OM = %s + %s = %s\\text{ cm}$. Dấu đẳng thức xảy ra khi $O$ là trung điểm của $AM$, tức là $M$ trùng với điểm đối xứng của $A$ qua tâm $O$.''' % (R, R, dk))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khi $M \\ne A$, đường trung trực của đoạn thẳng $AM$ luôn là một trục đối xứng của đường tròn $(O)$'
    th_da_1_s = 'Đường trung trực của đoạn thẳng $AM$ chỉ đi qua tâm $O$ khi $AM$ là đường kính của $(O)$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $A, M \\in (O)$ nên $OA = OM = R$, do đó tâm $O$ luôn nằm trên đường trung trực của đoạn thẳng $AM$. Mọi đường thẳng đi qua tâm $O$ đều là trục đối xứng của $(O)$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tập hợp các điểm $P$ khi $M$ di động trên $(O)$ ($M \\ne A$) không nằm trên đường tròn tâm $A$ bán kính $%s\\text{ cm}$' % dk
    vd_da_1_s = 'Tập hợp các điểm $P$ khi $M$ di động trên $(O)$ ($M \\ne A$) nằm trên đường tròn tâm $A$ bán kính $%s\\text{ cm}$' % dk
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì $P$ đối xứng với $A$ qua $M$ nên $M$ là trung điểm của $AP$, suy ra $AP = 2AM$. Do độ dài $AM$ thay đổi trong khoảng $(0; %s]$ khi $M$ di động trên $(O)$ nên độ dài $AP$ thay đổi trong khoảng $(0; %s]$, không cố định bằng $%s\\text{ cm}$.''' % (dk, 2*dk, dk))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khoảng cách từ trung điểm $I$ của $OA$ đến điểm $N$ luôn bằng $%s\\text{ cm}$' % nua_R
    vdc_da_1_s = 'Khoảng cách từ trung điểm $I$ của $OA$ đến điểm $N$ thay đổi theo vị trí của $M$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Trong tam giác $OAM$, $I$ là trung điểm của $OA$ và $N$ là trung điểm của $AM$ nên $IN$ là đường trung bình của tam giác $OAM$. Do đó $IN = \\dfrac{1}{2}OM = \\dfrac{%s}{2} = %s\\text{ cm}$ không đổi.''' % (R, nua_R))
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
