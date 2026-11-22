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


def bt_dang19_p2_b5_c3_hh8(self):
    # Khai báo biến
    do_dai_AB = random.choice([8, 10, 12, 14])
    khoang_cach_N = Rational(do_dai_AB, 4)

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (M) at (1.5,0);
\\coordinate (B) at (4.0,0);
\\coordinate (C) at (1.5,1.5);
\\coordinate (D) at (0,1.5);
\\coordinate (E) at (4.0,2.5);
\\coordinate (F) at (1.5,2.5);
\\coordinate (O1) at (0.75,0.75);
\\coordinate (O2) at (2.75,1.25);
\\coordinate (N) at (1.75,1.0);
\\draw[line width=1pt] (A)--(B)--(E)--(F)--(M)--cycle (D)--(C)--(M) (A)--(C) (M)--(D) (M)--(E) (B)--(F) (A)--(E) (B)--(C);
\\draw[line width=1pt, dashed] (O1)--(O2);
\\fill (A) circle (1pt) node[below left] {$A$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (B) circle (1pt) node[below right] {$B$};
\\fill (C) circle (1pt) node[left] {$C$};
\\fill (D) circle (1pt) node[above left] {$D$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (F) circle (1pt) node[above] {$F$};
\\fill (O1) circle (1pt) node[left] {$O_1$};
\\fill (O2) circle (1pt) node[right] {$O_2$};
\\fill (N) circle (1pt) node[above] {$N$};
\\end{tikzpicture}
\\end{center}''')

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho đoạn thẳng $AB = %s\\text{ cm}$ và điểm $M$ nằm giữa $A$ và $B$ ($MA \\neq MB$). Trên cùng một nửa mặt phẳng bờ $AB$, vẽ hai hình vuông $AMCD$ và $BMEF$. Gọi $O_1, O_2$ lần lượt là giao điểm hai đường chéo của hai hình vuông $AMCD$ và $BMEF$, $N$ là trung điểm của đoạn thẳng $O_1O_2$. Xét tính đúng sai của các khẳng định sau:%s'''
                     % (do_dai_AB, hinh_ve))

    # Ý a)
    nb_da_1_d = '\\True $AE = BC$ và $AE \\perp BC$'
    nb_da_1_s = '$AE = BC$ và $AE // BC$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Xét $\\Delta AME$ và $\\Delta CMB$ có: $AM = CM$, $\\widehat{AME} = \\widehat{CMB} = 90^\\circ$, $ME = MB$.\\\\
Suy ra $\\Delta AME = \\Delta CMB$ (c.g.c), do đó $AE = BC$ và $\\widehat{AEM} = \\widehat{CBM}$.\\\\
Vì $\\widehat{AEM} + \\widehat{MAE} = 90^\\circ$ nên $\\widehat{CBM} + \\widehat{MAE} = 90^\\circ$, suy ra $AE \\perp BC$.''')

    # Ý b)
    th_da_1_d = '\\True $\\widehat{O_1MO_2} = 90^\\circ$'
    th_da_1_s = '$\\widehat{O_1MO_2} = 60^\\circ$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $MD$ và $ME$ lần lượt là đường chéo của hai hình vuông $AMCD$ và $BMEF$ nên $\\widehat{O_1MA} = 45^\\circ$ và $\\widehat{O_2MB} = 45^\\circ$.\\\\
Do tia $MO_1$ và $MO_2$ nằm trên cùng một nửa mặt phẳng bờ $AB$ nên $\\widehat{O_1MO_2} = 180^\\circ - (45^\\circ + 45^\\circ) = 90^\\circ$.''')

    # Ý c)
    vd_da_1_d = '\\True Tứ giác $MO_1CO_2$ không phải là hình bình hành khi $MA \\neq MB$'
    vd_da_1_s = 'Tứ giác $MO_1CO_2$ luôn là hình bình hành với mọi vị trí của $M$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\widehat{O_1CM} = 45^\\circ$ và $\\widehat{O_2MB} = 45^\\circ$ ở vị trí đồng vị nên $O_1C // MO_2$.\\\\
Tuy nhiên $O_1C = \\dfrac{MD}{2} = \\dfrac{MA\\sqrt{2}}{2}$ còn $MO_2 = \\dfrac{ME}{2} = \\dfrac{MB\\sqrt{2}}{2}$.\\\\
Khi $MA \\neq MB$ thì $O_1C \\neq MO_2$ nên tứ giác $MO_1CO_2$ chỉ là hình thang vuông, không phải hình bình hành.''')

    # Ý d)
    vdc_da_1_d = '\\True Khi $M$ di chuyển giữa $A$ và $B$ thì khoảng cách từ $N$ đến đường thẳng $AB$ luôn không đổi và bằng $%s\\text{ cm}$' % (latex(khoang_cach_N))
    vdc_da_1_s = 'Khi $M$ di chuyển giữa $A$ và $B$ thì khoảng cách từ $N$ đến đường thẳng $AB$ thay đổi phụ thuộc vào $MA$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Gọi $H, K, I$ lần lượt là hình chiếu vuông góc của $O_1, N, O_2$ xuống $AB$.\\\\
Ta có $O_1H = \\dfrac{1}{2}AM$ và $O_2I = \\dfrac{1}{2}MB$.\\\\
Vì $NK$ là đường trung bình của hình thang vuông $O_1HIO_2$ nên:\\\\
$NK = \\dfrac{O_1H + O_2I}{2} = \\dfrac{AM + MB}{4} = \\dfrac{AB}{4} = \\dfrac{%s}{4} = %s\\text{ (cm)}$ (không đổi).'''
                     % (do_dai_AB, latex(khoang_cach_N)))

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
