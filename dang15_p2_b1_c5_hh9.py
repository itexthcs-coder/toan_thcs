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


def bt_dang15_p2_b1_c5_hh9(self):
    # Khai báo biến
    bo_htc = [(6, 8, 7, 3, 4, 3, 5), (12, 16, 14, 6, 8, 6, 10), (10, 24, 17, 5, 12, 5, 13)]
    ab, cd, h, ha, kd, ok, R = random.choice(bo_htc)
    oh = h - ok

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (-1.6,0);
\\coordinate (C) at (1.6,0);
\\coordinate (A) at (-1.2,2.1);
\\coordinate (B) at (1.2,2.1);
\\coordinate (H) at (0,2.1);
\\coordinate (K) at (0,0);
\\coordinate (O) at (0,0.9);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt] (H)--(K);
\\draw[line width=1pt, dashed] (O)--(A) (O)--(D);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (H) circle (1pt) node[above] {$H$};
\\fill (K) circle (1pt) node[below] {$K$};
\\fill (O) circle (1pt) node[right] {$O$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho hình thang cân $ABCD$ ($AB // CD$, $AB < CD$) có $AB = %s\\text{ cm}$, $CD = %s\\text{ cm}$ và đường cao bằng $%s\\text{ cm}$ (minh họa như hình vẽ). Xét tính đúng sai của các khẳng định sau:
%s''' % (ab, cd, h, tikz_code))

    nb_da_1_d = '\\True Hình thang cân $ABCD$ có một trục đối xứng là đường trung trực của hai đáy $AB$ và $CD$'
    nb_da_1_s = 'Hình thang cân $ABCD$ có hai trục đối xứng là hai đường chéo $AC$ và $BD$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Gọi $H, K$ lần lượt là trung điểm của hai đáy $AB$ và $CD$. Theo tính chất hình thang cân, đường thẳng $HK$ là đường trung trực chung của cả hai đáy $AB$ và $CD$, nên $HK$ là trục đối xứng của hình thang cân $ABCD$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Bốn đỉnh $A, B, C, D$ cùng thuộc một đường tròn có tâm $O$ nằm trên trục đối xứng của hình thang cân'
    th_da_1_s = 'Bốn đỉnh $A, B, C, D$ không cùng thuộc một đường tròn'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Gọi $O$ là giao điểm của đường trung trực cạnh bên $AD$ với đường thẳng $HK$. Vì $O \\in HK$ nên $OA = OB$ và $OD = OC$; lại có $OA = OD$ nên $OA = OB = OC = OD$. Vậy bốn đỉnh $A, B, C, D$ cùng thuộc đường tròn tâm $O$ nằm trên $HK$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tâm $O$ của đường tròn đi qua bốn đỉnh $A, B, C, D$ nằm ở miền trong của hình thang $ABCD$'
    vd_da_1_s = 'Tâm $O$ của đường tròn đi qua bốn đỉnh $A, B, C, D$ nằm ở miền ngoài của hình thang $ABCD$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Đặt $OK = x$ ($0 < x < %s$), ta có $OH = %s - x$, $HA = %s\\text{ cm}$, $KD = %s\\text{ cm}$. Từ $OA^2 = OD^2$, suy ra $(%s - x)^2 + %s^2 = x^2 + %s^2 \\Leftrightarrow %s x = %s \\Leftrightarrow x = %s\\text{ cm}$. Vì $0 < %s < %s$ nên điểm $O$ nằm giữa $H$ và $K$, tức nằm ở miền trong của hình thang $ABCD$.''' % (h, h, ha, kd, h, ha, kd, 2*h, h**2 + ha**2 - kd**2, ok, ok, h))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Bán kính của đường tròn đi qua bốn đỉnh $A, B, C, D$ bằng $%s\\text{ cm}$' % R
    vdc_da_1_s = 'Bán kính của đường tròn đi qua bốn đỉnh $A, B, C, D$ bằng $%s\\text{ cm}$' % (R + 2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Áp dụng định lí Pythagore cho tam giác $OKD$ vuông tại $K$, bán kính đường tròn là $R = OD = \\sqrt{OK^2 + KD^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ cm}$.''' % (ok, kd, R))
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
