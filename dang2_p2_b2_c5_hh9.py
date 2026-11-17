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

def bt_dang2_p2_b2_c5_hh9(self):
    R = randint(4, 15)
    BC = 2 * R

    noidungcauhoi = ('''Cho tứ giác lồi $ABCD$ có $\\widehat{BAC} = \\widehat{BDC} = 90^\\circ$ và $BC = %s\\text{ cm}$. Gọi $O$ là trung điểm của đoạn thẳng $BC$ (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (B) at (-1.8,0);
    \\coordinate (C) at (1.8,0);
    \\coordinate (A) at (125:1.8);
    \\coordinate (D) at (40:1.8);
    \\draw[line width=1pt, dashed] (O) circle (1.8);
    \\draw[line width=1pt] (B)--(A)--(D)--(C)--cycle (A)--(C) (B)--(D) (O)--(A) (O)--(D);
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\end{tikzpicture}
    \\end{center}''' % (BC))

    nb_da_1_d = '\\True Bốn điểm $A, B, C, D$ cùng nằm trên đường tròn tâm $O$ bán kính $%s\\text{ cm}$' % (R)
    nb_da_1_s = 'Bốn điểm $A, B, C, D$ cùng nằm trên đường tròn tâm $O$ bán kính $%s\\text{ cm}$' % (BC)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Tam giác $ABC$ vuông tại $A$ có $AO$ là đường trung tuyến ứng với cạnh huyền $BC$ nên $OA = OB = OC = \\dfrac{BC}{2} = \\dfrac{%s}{2} = %s\\text{ cm}$. \\\\ Tương tự, tam giác $DBC$ vuông tại $D$ nên $OD = OB = OC = %s\\text{ cm}$. \\\\ Vậy bốn điểm $A, B, C, D$ cùng nằm trên đường tròn $(O; %s\\text{ cm})$.''' % (BC, R, R, R))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Đoạn thẳng $AD$ là một dây cung của đường tròn $(O)$'
    th_da_1_s = 'Đoạn thẳng $AD$ là một bán kính của đường tròn $(O)$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Vì hai điểm $A$ và $D$ cùng nằm trên đường tròn $(O)$ nên đoạn thẳng $AD$ là một dây cung của đường tròn $(O)$.''')
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu $AD$ không đi qua tâm $O$ thì độ dài $AD$ luôn nhỏ hơn $%s\\text{ cm}$' % (BC)
    vd_da_1_s = 'Nếu $AD$ không đi qua tâm $O$ thì độ dài $AD$ luôn lớn hơn $%s\\text{ cm}$' % (BC)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Trong đường tròn $(O)$, $BC = %s\\text{ cm}$ là đường kính nên là dây cung lớn nhất. Do đó nếu dây $AD$ không đi qua tâm $O$ thì $AD < BC = %s\\text{ cm}$.''' % (BC, BC))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu $\\widehat{AOD} = 60^\\circ$ thì độ dài dây $AD$ bằng $%s\\text{ cm}$' % (R)
    vdc_da_1_s = 'Nếu $\\widehat{AOD} = 60^\\circ$ thì độ dài dây $AD$ bằng $%s\\text{ cm}$' % (BC)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Xét tam giác $OAD$ có $OA = OD = %s\\text{ cm}$ nên tam giác $OAD$ cân tại $O$. \\\\ Khi $\\widehat{AOD} = 60^\\circ$ thì tam giác $OAD$ là tam giác đều, suy ra $AD = OA = %s\\text{ cm}$.''' % (R, R))
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
