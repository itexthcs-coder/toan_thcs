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


def bt_dang13_p2_b4_c9_hh9(self):
    hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (90:1.7);
\\coordinate (E) at (45:1.7);
\\coordinate (D) at (0:1.7);
\\coordinate (H) at (-45:1.7);
\\coordinate (C) at (-90:1.7);
\\coordinate (G) at (-135:1.7);
\\coordinate (B) at (180:1.7);
\\coordinate (F) at (135:1.7);
\\draw[line width=1pt] (O) circle (1.7);
\\draw[line width=1pt] (E)--(A)--(F)--(B)--(G)--(C)--(H)--(D)--cycle;
\\draw[line width=1pt, dashed] (A)--(B)--(C)--(D)--cycle;
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (H) circle (1pt) node[below right] {$H$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (G) circle (1pt) node[below left] {$G$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (F) circle (1pt) node[above left] {$F$};
\\end{tikzpicture}
\\end{center}'''

    noidungcauhoi = ('''Biết rằng bốn đỉnh $A, B, C, D$ của một hình vuông cùng nằm trên một đường tròn $(O)$ theo thứ tự ngược chiều quay của kim đồng hồ. Phép quay thuận chiều $45^\\circ$ tâm $O$ biến các điểm $A, B, C, D$ lần lượt thành các điểm $E, F, G, H$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau: %s''' % (hinh_tikz))

    nb_da_1_d = '\\True Số đo cung nhỏ $AE$ bằng $45^\\circ$'
    nb_da_1_s = 'Số đo cung nhỏ $AE$ bằng $90^\\circ$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Theo định nghĩa phép quay thuận chiều $45^\\circ$ tâm $O$ biến $A$ thành $E$, điểm $A$ di chuyển tạo nên cung nhỏ $AE$ có số đo bằng $45^\\circ$.''')

    th_da_1_d = '\\True Thứ tự các điểm nằm trên đường tròn $(O)$ theo chiều quay của kim đồng hồ là $E, A, H, D, G, C, F, B$'
    th_da_1_s = 'Thứ tự các điểm nằm trên đường tròn $(O)$ theo chiều quay của kim đồng hồ là $A, E, B, F, C, G, D, H$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì $A, B, C, D$ xếp ngược chiều kim đồng hồ nên thứ tự thuận chiều kim đồng hồ của bốn đỉnh hình vuông là $A, D, C, B$. Khi quay thuận chiều $45^\\circ$, $E$ nằm giữa $A$ và $D$, $H$ nằm giữa $D$ và $C$, $G$ nằm giữa $C$ và $B$, $F$ nằm giữa $B$ và $A$. Vậy thứ tự thuận chiều kim đồng hồ là $E, A, H, D, G, C, F, B$ (tức $A, E, D, H, C, G, B, F$).''')

    vd_da_1_d = '\\True Đa giác $EAFBGCHD$ có tám cạnh bằng nhau và tám góc bằng nhau'
    vd_da_1_s = 'Đa giác $EAFBGCHD$ có tám cạnh bằng nhau nhưng các góc không bằng nhau'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Tám đỉnh chia đường tròn $(O)$ thành $8$ cung nhỏ bằng nhau (mỗi cung $45^\\circ$) nên đa giác lồi $EAFBGCHD$ có $8$ cạnh bằng nhau và $8$ góc đều bằng $135^\\circ$, là một bát giác đều.''')

    vdc_da_1_d = '\\True Phép quay thuận chiều $45^\\circ$ tâm $O$ biến bát giác đều $EAFBGCHD$ thành chính nó'
    vdc_da_1_s = 'Phép quay thuận chiều $45^\\circ$ tâm $O$ không giữ nguyên bát giác đều $EAFBGCHD$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Phép quay thuận chiều $45^\\circ$ tâm $O$ biến mỗi đỉnh của bát giác đều $EAFBGCHD$ thành đỉnh kế tiếp của nó nên giữ nguyên bát giác đều này.''')

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
