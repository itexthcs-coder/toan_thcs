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


def bt_dang18_p2_b5_c3_hh8(self):
    # Khai báo biến
    canh_hv = randint(4, 10)
    bo_dinh = random.choice([
        ('A', 'B', 'C', 'D', 'E', 'F', 'I'),
        ('M', 'N', 'P', 'Q', 'E', 'F', 'I')
    ])
    A, B, C, D, E, F, I = bo_dinh

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.6);
\\coordinate (B) at (2.6,2.6);
\\coordinate (C) at (2.6,0);
\\coordinate (D) at (0,0);
\\coordinate (E) at (1.3,2.6);
\\coordinate (F) at (2.6,1.3);
\\coordinate (I) at (0.52,1.04);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (D)--(E) (A)--(F);
\\draw[line width=1pt, dashed] (C)--(I);
\\draw[line width=1pt] (0,2.4)--(0.2,2.4)--(0.2,2.6);
\\draw[line width=1pt] (2.4,2.6)--(2.4,2.4)--(2.6,2.4);
\\fill (A) circle (1pt) node[above left] {$%s$};
\\fill (B) circle (1pt) node[above right] {$%s$};
\\fill (C) circle (1pt) node[below right] {$%s$};
\\fill (D) circle (1pt) node[below left] {$%s$};
\\fill (E) circle (1pt) node[above] {$%s$};
\\fill (F) circle (1pt) node[right] {$%s$};
\\fill (I) circle (1pt) node[below right] {$%s$};
\\end{tikzpicture}
\\end{center}''' % (A, B, C, D, E, F, I))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình vuông $%s%s%s%s$ có cạnh bằng $%s\\text{ cm}$. Gọi $%s$ và $%s$ lần lượt là trung điểm của các cạnh $%s%s$ và $%s%s$. Nối $%s%s$ và $%s%s$ cắt nhau tại $%s$. Xét tính đúng sai của các khẳng định sau:%s'''
                     % (A, B, C, D, canh_hv, E, F, A, B, B, C, D, E, A, F, I, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c)' % (A, D, E, B, A, F)
    nb_da_1_s = '$\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c)' % (A, D, E, C, D, F)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Xét hai tam giác vuông $\\Delta %s%s%s$ và $\\Delta %s%s%s$ có:\\\\
$%s%s = %s%s$ (cạnh hình vuông); $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$; $%s%s = %s%s$ (cùng bằng nửa cạnh hình vuông).\\\\
Suy ra $\\Delta %s%s%s = \\Delta %s%s%s$ (c.g.c).'''
                    % (A, D, E, B, A, F, A, D, B, A, D, A, E, A, B, F, A, E, B, F, A, D, E, B, A, F))

    # Ý b)
    th_da_1_d = '\\True $\\widehat{%s%s%s} = \\widehat{%s%s%s}$' % (A, D, E, B, A, F)
    th_da_1_s = '$\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$' % (A, D, E, B, A, F)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Từ $\\Delta %s%s%s = \\Delta %s%s%s$ suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ (hai góc tương ứng).'''
                    % (A, D, E, B, A, F, A, D, E, B, A, F))

    # Ý c)
    vd_da_1_d = '\\True $%s%s \\perp %s%s$ tại $%s$' % (D, E, A, F, I)
    vd_da_1_s = '$%s%s$ và $%s%s$ cắt nhau tạo thành góc nhọn $60^\\circ$' % (D, E, A, F)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong tam giác $%s%s%s$ vuông tại $%s$, ta có $\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$.\\\\
Mà $\\widehat{%s%s%s} = \\widehat{%s%s%s}$ nên $\\widehat{%s%s%s} + \\widehat{%s%s%s} = 90^\\circ$.\\\\
Xét tam giác $%s%s%s$ có $\\widehat{%s%s%s} = 180^\\circ - (\\widehat{%s%s%s} + \\widehat{%s%s%s}) = 90^\\circ$, suy ra $%s%s \\perp %s%s$ tại $%s$.'''
                    % (A, D, E, A, A, D, E, A, E, D,
                       A, D, E, B, A, F, B, A, F, A, E, D,
                       A, E, I, A, I, E, I, A, E, I, E, A, D, E, A, F, I))

    # Ý d)
    vdc_da_1_d = '\\True Độ dài đoạn thẳng $%s%s$ bằng $%s\\text{ cm}$' % (C, I, canh_hv)
    vdc_da_1_s = 'Độ dài đoạn thẳng $%s%s$ lớn hơn $%s\\text{ cm}$' % (C, I, canh_hv)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Gọi $H$ là trung điểm của cạnh $%s%s$. Tứ giác $%s%s%s%s$ có $%s%s // %s%s$ và $%s%s = %s%s$ nên là hình bình hành, suy ra $%s%s // %s%s$.\\\\
Vì $%s%s \\perp %s%s$ nên $%s%s \\perp %s%s$. Trong tam giác $%s%s%s$, $%s%s$ vừa là đường cao vừa là đường trung tuyến (do $%s$ là trung điểm $%s%s$ và $%s%s // %s%s$) nên tam giác $%s%s%s$ cân tại $%s$, suy ra $%s%s = %s%s = %s\\text{ cm}$.'''
                     % (C, D, E, B, 'H', D, E, B, 'H', D, E, B, 'H', D, D, E, 'H', B,
                        A, F, D, E, 'H', B, A, F, C, D, I, 'H', B, F, B, C, 'H', B, D, E, C, D, I, C, C, I, C, D, canh_hv))

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

    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]

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
