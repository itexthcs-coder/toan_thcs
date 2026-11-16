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


def bt_dang10_p2_b1_c5_hh9(self):
    # Khai báo biến
    R = random.randint(4, 12)

    tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.8,0);
\\coordinate (B) at (1.8,0);
\\coordinate (C) at (50:1.8);
\\coordinate (D) at (-50:1.8);
\\coordinate (H) at (1.157,0);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt] (C)--(D);
\\draw[line width=1pt, dashed] (A)--(C)--(B)--(D)--cycle;
\\draw[line width=1pt] (0.957,0)--(0.957,0.2)--(1.157,0.2);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (D) circle (1pt) node[below right] {$D$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$ và dây cung $CD$ vuông góc với $AB$ tại $H$ ($H$ nằm giữa $O$ và $B$, $H \\ne O$) như hình vẽ. Xét tính đúng sai của các khẳng định sau:
%s''' % (R, tikz_code))

    nb_da_1_d = '\\True Hai điểm $C$ và $D$ đối xứng với nhau qua đường thẳng $AB$'
    nb_da_1_s = 'Hai điểm $C$ và $D$ đối xứng với nhau qua tâm $O$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Đường thẳng $AB$ đi qua tâm $O$ nên $AB$ là trục đối xứng của đường tròn $(O)$. Mà $CD \\perp AB$ tại $H$ với $C, D \\in (O)$ nên giao điểm (khác $C$) của $CD$ với $(O)$ là điểm đối xứng của $C$ qua $AB$, chính là $D$.''')
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Đường thẳng $AB$ là đường trung trực của đoạn thẳng $CD$'
    th_da_1_s = 'Đoạn thẳng $CD$ là đường trung trực của đoạn thẳng $AB$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $C$ và $D$ đối xứng với nhau qua đường thẳng $AB$ nên theo định nghĩa đối xứng trục, đường thẳng $AB$ là đường trung trực của đoạn thẳng $CD$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tam giác $ACD$ và tam giác $BCD$ đều là các tam giác cân'
    vd_da_1_s = 'Chỉ có tam giác $ACD$ cân tại $A$, tam giác $BCD$ không phải tam giác cân'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Vì $A$ và $B$ đều nằm trên đường trung trực $AB$ của đoạn thẳng $CD$ nên $AC = AD$ và $BC = BD$. Vậy tam giác $ACD$ cân tại $A$ và tam giác $BCD$ cân tại $B$.''')
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu $OH = HB$ thì tứ giác $ACBD$ không phải là hình thoi'
    vdc_da_1_s = 'Nếu $OH = HB$ thì tứ giác $ACBD$ là hình thoi'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Ta có $H$ là trung điểm của $CD$. Nếu $OH = HB$ thì $H$ là trung điểm của $OB$, do đó $HA = HO + OA = \\dfrac{3}{2}R \\ne \\dfrac{1}{2}R = HB$, tức là $H$ không phải trung điểm của $AB$. Vì hai đường chéo $AB$ và $CD$ không cắt nhau tại trung điểm của mỗi đường nên $ACBD$ không phải là hình thoi.''')
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
