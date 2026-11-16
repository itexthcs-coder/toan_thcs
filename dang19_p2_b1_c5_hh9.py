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


def bt_dang19_p2_b1_c5_hh9(self):
    # Khai báo biến
    R = random.randint(5, 15)

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (130:1.8);
\\coordinate (B) at (10:1.8);
\\coordinate (C) at (-10:1.8);
\\coordinate (D) at (-130:1.8);
\\coordinate (H) at ($(A)!0.5!(B)$);
\\coordinate (K) at ($(C)!0.5!(D)$);
\\coordinate (I) at (1.18,0);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B) (C)--(D);
\\draw[line width=1pt, dashed] (O)--(H) (O)--(K) (O)--(I);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (H) circle (1pt) node[above right] {$H$};
\\fill (K) circle (1pt) node[below right] {$K$};
\\fill (I) circle (1pt) node[above] {$I$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ có hai dây cung $AB$ và $CD$ bằng nhau và cắt nhau tại điểm $I$ nằm bên trong đường tròn ($I \\ne O$). Gọi $H$ và $K$ lần lượt là trung điểm của $AB$ và $CD$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
%s''' % (R, tikz_code))

    nb_da_1_d = '\\True Đường thẳng $OH$ là trục đối xứng của đường tròn $(O)$ và $OH \\perp AB$'
    nb_da_1_s = 'Đường thẳng $AB$ là trục đối xứng của đường tròn $(O)$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì $OA = OB = R$ nên đường trung trực của $AB$ đi qua $O$ và trung điểm $H$ của $AB$, chính là đường thẳng $OH$. Suy ra $OH$ là trục đối xứng của $(O)$ và $OH \\perp AB$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Hai đoạn thẳng $OH$ và $OK$ có độ dài bằng nhau'
    th_da_1_s = 'Độ dài đoạn thẳng $OH$ luôn lớn hơn độ dài đoạn thẳng $OK$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Xét hai tam giác vuông $OHA$ và $OKC$ có $OA = OC = R$ và $AH = \\dfrac{AB}{2} = \\dfrac{CD}{2} = CK$. Suy ra $\\Delta OHA = \\Delta OKC$ (cạnh huyền - cạnh góc vuông), do đó $OH = OK$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đường thẳng $OI$ là đường trung trực của đoạn thẳng $HK$'
    vd_da_1_s = 'Đường thẳng $OI$ đi qua trung điểm của $HK$ nhưng không vuông góc với $HK$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Hai tam giác vuông $OHI$ và $OKI$ có chung cạnh huyền $OI$ và $OH = OK$ nên $\\Delta OHI = \\Delta OKI$ (cạnh huyền - cạnh góc vuông), suy ra $IH = IK$. Kết hợp với $OH = OK$, ta được $OI$ là đường trung trực của đoạn thẳng $HK$.''')
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Hai điểm $A$ và $C$ không nhất thiết đối xứng với nhau qua đường thẳng $OI$'
    vdc_da_1_s = 'Hai điểm $A$ và $C$ luôn đối xứng với nhau qua đường thẳng $OI$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Do $OI$ là trục đối xứng của $(O)$ và hai tia $HA, KD$ đối xứng nhau qua $OI$ (vì $HA = KD$) nên điểm đối xứng với $A$ qua $OI$ là điểm $D$ (còn điểm đối xứng với $B$ qua $OI$ là điểm $C$), chứ không phải $A$ và $C$ đối xứng nhau qua $OI$.''')
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
