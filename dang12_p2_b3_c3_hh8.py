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

def bt_dang12_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        s_abcd = randint(12, 30)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.0,2.0);
\\coordinate (B) at (3.2,2.0);
\\coordinate (E) at (5.4,2.0);
\\coordinate (F) at (0,0);
\\coordinate (D) at (2.2,0);
\\coordinate (C) at (4.4,0);
\\draw[line width=1pt] (A)--(E)--(D)--(F)--cycle (B)--(C) (A)--(F) (D)--(E) (B)--(F);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[above] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (E) circle (1pt) node[above right] {$E$};
\\fill (F) circle (1pt) node[below left] {$F$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$. Lấy điểm $E$ sao cho $B$ là trung điểm của $AE$, lấy điểm $F$ sao cho $C$ là trung điểm của $DF$ (như hình vẽ).
%s''' % (hinh_ve))
        
        nb_da_1_d = '\\True $AE = DF$ và $AE // DF$'
        nb_da_1_s = '$AE = 2DF$ và $AE // DF$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Vì $B$ là trung điểm của $AE$ và $C$ là trung điểm của $DF$ nên $AE = 2AB$ và $DF = 2CD$. Mà $ABCD$ là hình bình hành nên $AB = CD$ và $AB // CD$, suy ra $AE = DF$ và $AE // DF$.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì $AB = CD$ nên $AE = 2AB = 2CD = DF$.''')
        
        th_da_1_d = '\\True Hai tứ giác $AEFD$ và $ABFC$ đều là hình bình hành'
        th_da_1_s = 'Tứ giác $AEFD$ là hình bình hành nhưng $ABFC$ không phải là hình bình hành'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Tứ giác $AEFD$ có $AE // DF$ và $AE = DF$ nên là hình bình hành. Tứ giác $ABFC$ có $AB // CF$ (do $AB // CD$) và $AB = CF$ (cùng bằng $CD$) nên cũng là hình bình hành.''')
        loigiai_th_1_s = ('''Mệnh đề sai vì $CF = CD = AB$ và $CF // AB$ nên $ABFC$ cũng là hình bình hành.''')
        
        vd_da_1_d = '\\True Ba đoạn thẳng $AF, DE, BC$ cắt nhau tại trung điểm của mỗi đường'
        vd_da_1_s = 'Ba đoạn thẳng $AF, DE, BC$ đôi một song song với nhau'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Gọi $O$ là trung điểm của $AF$. Vì $AEFD$ là hình bình hành nên hai đường chéo $AF$ và $DE$ cắt nhau tại trung điểm $O$ của mỗi đường. Vì $ABFC$ là hình bình hành nên hai đường chéo $AF$ và $BC$ cũng cắt nhau tại trung điểm $O$ của mỗi đường. Vậy trung điểm của ba đoạn thẳng $AF, DE, BC$ trùng nhau.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì $AF$ là đường chéo chung của hai hình bình hành $AEFD$ và $ABFC$ nên ba đoạn thẳng $AF, DE, BC$ đồng quy tại trung điểm của mỗi đường.''')
        
        vdc_da_1_d = '\\True Nếu diện tích hình bình hành $ABCD$ bằng $%s\\text{ cm}^2$ thì diện tích hình bình hành $AEFD$ bằng $%s\\text{ cm}^2$' % (s_abcd, 2 * s_abcd)
        vdc_da_1_s = 'Nếu diện tích hình bình hành $ABCD$ bằng $%s\\text{ cm}^2$ thì diện tích hình bình hành $AEFD$ bằng $%s\\text{ cm}^2$' % (s_abcd, 3 * s_abcd)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Hai hình bình hành $AEFD$ và $ABCD$ có chung chiều cao hạ từ $D$ xuống đường thẳng $AB$ và đáy $AE = 2AB$ nên $S_{AEFD} = 2S_{ABCD} = 2 \\cdot %s = %s$ ($\\text{cm}^2$).''' % (s_abcd, 2 * s_abcd))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $AE = 2AB$ và chung chiều cao nên $S_{AEFD} = 2S_{ABCD} = %s$ ($\\text{cm}^2$).''' % (2 * s_abcd))
        
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
        
        loigiai_nb_1 = loigiai_nb_1_d if '\\True' in nb_da_1 else loigiai_nb_1_s
        loigiai_th_1 = loigiai_th_1_d if '\\True' in th_da_1 else loigiai_th_1_s
        loigiai_vd_1 = loigiai_vd_1_d if '\\True' in vd_da_1 else loigiai_vd_1_s
        loigiai_vdc_1 = loigiai_vdc_1_d if '\\True' in vdc_da_1 else loigiai_vdc_1_s
        
        shuffled_answers_nb = [nb_da_1]
        shuffled_solutions_nb = [loigiai_nb_1]
        shuffled_answers_th = [th_da_1]
        shuffled_solutions_th = [loigiai_th_1]
        shuffled_answers_vd = [vd_da_1]
        shuffled_solutions_vd = [loigiai_vd_1]
        shuffled_answers_vdc = [vdc_da_1]
        shuffled_solutions_vdc = [loigiai_vdc_1]
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
