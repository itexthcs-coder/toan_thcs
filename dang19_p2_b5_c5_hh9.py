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


def bt_dang19_p2_b5_c5_hh9(self):
    def fmt(val):
        return str(val).replace('.', ',')

    k = random.choice([10, 20])
    s1s2 = 12 * k
    r1 = 7 * k
    r2 = 8 * k
    s2s3 = 5 * k
    r3 = 10 * k
    s1s3 = s1s2 + s2s3

    tikz_code = (
"""\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S1) at (0,0);
\\coordinate (S2) at (3.6,0);
\\coordinate (P1) at (1.575,1.38);
\\coordinate (P2) at (1.575,-1.38);
\\draw[line width=1pt] (S1) circle (2.1cm);
\\draw[line width=1pt] (S2) circle (2.4cm);
\\draw[line width=1pt] (S1)--(S2);
\\draw[line width=1pt, dashed] (P1)--(P2);
\\fill (S1) circle (1pt) node[left] {$S_1$};
\\fill (S2) circle (1pt) node[right] {$S_2$};
\\fill (P1) circle (1pt) node[above] {$P_1$};
\\fill (P2) circle (1pt) node[below] {$P_2$};
\\end{tikzpicture}
\\end{center}"""
    )

    noidungcauhoi = ("""Hai trạm địa chấn $S_1$ và $S_2$ đặt cách nhau $%s\\text{ km}$. Khi xảy ra động đất, trạm $S_1$ đo được tâm chấn nằm trên đường tròn $(S_1; %s\\text{ km})$, trạm $S_2$ đo được tâm chấn nằm trên đường tròn $(S_2; %s\\text{ km})$.
%s""" % (fmt(s1s2), fmt(r1), fmt(r2), tikz_code))

    # Nhận biết
    nb_da_1_d = '\\True Dữ liệu từ hai trạm cho thấy hai đường tròn khả dĩ cắt nhau tại hai điểm phân biệt'
    nb_da_1_s = 'Dữ liệu từ hai trạm cho thấy hai đường tròn khả dĩ tiếp xúc ngoài với nhau'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    loigiai_nb_1 = ("""Ta có $R_2 - R_1 = %s - %s = %s\\text{ km}$ và $R_1 + R_2 = %s + %s = %s\\text{ km}$. Vì $%s < S_1S_2 = %s < %s$ nên hai đường tròn $(S_1)$ và $(S_2)$ cắt nhau tại hai điểm phân biệt $P_1, P_2$.""" % (fmt(r2), fmt(r1), fmt(r2 - r1), fmt(r1), fmt(r2), fmt(r1 + r2), fmt(r2 - r1), fmt(s1s2), fmt(r1 + r2)))

    # Thông hiểu
    th_da_1_d = '\\True Chưa thể xác định được duy nhất một vị trí chính xác của tâm chấn nếu chỉ dùng dữ liệu từ hai trạm $S_1$ và $S_2$'
    th_da_1_s = 'Có thể xác định được duy nhất một vị trí chính xác của tâm chấn chỉ bằng dữ liệu từ hai trạm $S_1$ và $S_2$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    loigiai_th_1 = ("""Vì hai đường tròn cắt nhau tại $2$ giao điểm $P_1, P_2$ nên cả hai vị trí này đều thỏa mãn khoảng cách đo được từ $S_1$ và $S_2$, cần có thêm trạm thứ ba để xác định duy nhất tâm chấn.""")

    # Vận dụng
    vd_da_1_d = '\\True Hai vị trí khả dĩ $P_1, P_2$ của tâm chấn nằm đối xứng nhau qua đường thẳng nối hai trạm $S_1S_2$'
    vd_da_1_s = 'Hai vị trí khả dĩ $P_1, P_2$ của tâm chấn nằm cùng một phía đối với đường thẳng $S_1S_2$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    loigiai_vd_1 = ("""Đường nối tâm $S_1S_2$ là đường trung trực của dây chung $P_1P_2$ nên hai vị trí khả dĩ $P_1$ và $P_2$ đối xứng nhau qua đường thẳng $S_1S_2$.""")

    # Vận dụng cao
    vdc_da_1_d = '\\True Nếu một trạm thứ ba $S_3$ nằm trên đường thẳng $S_1S_2$ (với $S_2$ nằm giữa $S_1, S_3$ và $S_2S_3 = %s\\text{ km}$) đo được khoảng cách đến tâm chấn là $%s\\text{ km}$ thì đường tròn $(S_3; %s\\text{ km})$ sẽ tiếp xúc ngoài với đường tròn $(S_1; %s\\text{ km})$' % (fmt(s2s3), fmt(r3), fmt(r3), fmt(r1))
    vdc_da_1_s = 'Nếu một trạm thứ ba $S_3$ nằm trên đường thẳng $S_1S_2$ (với $S_2$ nằm giữa $S_1, S_3$ và $S_2S_3 = %s\\text{ km}$) đo được khoảng cách đến tâm chấn là $%s\\text{ km}$ thì đường tròn $(S_3; %s\\text{ km})$ sẽ nằm ngoài đường tròn $(S_1; %s\\text{ km})$' % (fmt(s2s3), fmt(r3), fmt(r3), fmt(r1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    loigiai_vdc_1 = ("""Vì $S_2$ nằm giữa $S_1$ và $S_3$ nên $S_1S_3 = S_1S_2 + S_2S_3 = %s + %s = %s\\text{ km}$. Mặt khác tổng bán kính của $(S_1)$ và $(S_3)$ là $R_1 + R_3 = %s + %s = %s\\text{ km} = S_1S_3$. Vậy $(S_3)$ tiếp xúc ngoài với $(S_1)$.""" % (fmt(s1s2), fmt(s2s3), fmt(s1s3), fmt(r1), fmt(r3), fmt(r1 + r3)))

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
