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

def bt_dang11_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab = randint(5, 12)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,3);
\\coordinate (B) at (0,0);
\\coordinate (C) at (4.5,0);
\\coordinate (M) at (1.8,0);
\\coordinate (N) at (2.7,1.8);
\\coordinate (P) at (0.6,1.2);
\\coordinate (I) at ($(N)!0.5!(P)$);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(N) (M)--(P) (N)--(P) (A)--(M);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[below] {$M$};
\\fill (N) circle (1pt) node[above right] {$N$};
\\fill (P) circle (1pt) node[above left] {$P$};
\\fill (I) circle (1pt) node[above left] {$I$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho tam giác $ABC$. Từ một điểm $M$ tùy ý trên cạnh $BC$, kẻ đường thẳng song song với $AB$ cắt cạnh $AC$ tại $N$ và kẻ đường thẳng song song với $AC$ cắt cạnh $AB$ tại $P$. Gọi $I$ là trung điểm của đoạn thẳng $NP$ (như hình vẽ).
%s''' % (hinh_ve))
        
        nb_da_1_d = '\\True Tứ giác $APMN$ là hình bình hành'
        nb_da_1_s = 'Tứ giác $APMN$ không phải là hình bình hành'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Tứ giác $APMN$ có $AP // MN$ (vì $AB // MN$) và $AN // MP$ (vì $AC // MP$) nên theo định nghĩa, tứ giác $APMN$ là hình bình hành.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì tứ giác $APMN$ có các cạnh đối song song nên là hình bình hành.''')
        
        th_da_1_d = '\\True Ba điểm $A, I, M$ thẳng hàng và $I$ là trung điểm của đoạn thẳng $AM$'
        th_da_1_s = 'Điểm $I$ không nằm trên đoạn thẳng $AM$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Trong hình bình hành $APMN$, hai đường chéo $AM$ và $NP$ cắt nhau tại trung điểm của mỗi đường. Vì $I$ là trung điểm của $NP$ nên $I$ cũng là trung điểm của $AM$, suy ra ba điểm $A, I, M$ thẳng hàng.''')
        loigiai_th_1_s = ('''Mệnh đề sai vì $AM$ và $NP$ là hai đường chéo của hình bình hành $APMN$ nên trung điểm $I$ của $NP$ trùng với trung điểm của $AM$.''')
        
        vd_da_1_d = '\\True Nếu $\\Delta ABC$ cân tại $A$ có $AB = AC = %s$ cm thì tổng $MN + MP$ luôn bằng $%s$ cm với mọi vị trí của $M$ trên $BC$' % (ab, ab)
        vd_da_1_s = 'Nếu $\\Delta ABC$ cân tại $A$ có $AB = AC = %s$ cm thì tổng $MN + MP$ luôn bằng $%s$ cm với mọi vị trí của $M$ trên $BC$' % (ab, 2 * ab)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Vì $\\Delta ABC$ cân tại $A$ nên $\\widehat{B} = \\widehat{C}$. Mặt khác $MP // AC$ nên $\\widehat{PMB} = \\widehat{C} = \\widehat{B}$, suy ra $\\Delta PBM$ cân tại $P$, do đó $MP = PB$. Lại có $MN = AP$ (hai cạnh đối của hình bình hành $APMN$), nên $MN + MP = AP + PB = AB = %s$ cm.''' % (ab))
        loigiai_vd_1_s = ('''Mệnh đề sai vì $MP = PB$ và $MN = AP$ nên $MN + MP = AP + PB = AB = %s$ cm.''' % (ab))
        
        vdc_da_1_d = '\\True Khi điểm $M$ di chuyển trên cạnh $BC$ thì trung điểm $I$ của $NP$ luôn nằm trên đường trung bình ứng với cạnh $BC$ của $\\Delta ABC$'
        vdc_da_1_s = 'Khi điểm $M$ di chuyển trên cạnh $BC$ thì điểm $I$ là một điểm cố định'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Vì $I$ luôn là trung điểm của đoạn thẳng $AM$ với $M \\in BC$ nên khi $M$ di chuyển trên cạnh $BC$, điểm $I$ di chuyển trên đường trung bình song song với cạnh $BC$ của $\\Delta ABC$.''')
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $I$ là trung điểm của $AM$; khi $M$ thay đổi trên $BC$ thì vị trí của $I$ cũng thay đổi theo trên đường trung bình ứng với cạnh $BC$.''')
        
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
