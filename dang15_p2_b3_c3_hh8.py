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

def bt_dang15_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab = randint(8, 14)
        am = randint(2, 5)
        bm = ab - am
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.4);
\\coordinate (B) at (5.2,2.4);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (M) at ($(A)!0.3!(B)$);
\\coordinate (N) at ($(B)!0.35!(C)$);
\\coordinate (P) at ($(C)!0.3!(D)$);
\\coordinate (Q) at ($(D)!0.35!(A)$);
\\coordinate (O) at ($(A)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (M)--(P) (N)--(Q);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[below] {$P$};
\\fill (Q) circle (1pt) node[left] {$Q$};
\\fill (O) circle (1pt) node[above right] {$O$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có giao điểm hai đường chéo là $O$. Trên các cạnh $AB, BC, CD, DA$ lần lượt lấy các điểm $M, N, P, Q$ sao cho $AM = CP$ và $BN = DQ$ (như hình vẽ).
%s''' % (hinh_ve))
        
        nb_da_1_d = '\\True $BM = DP$ và $CN = AQ$'
        nb_da_1_s = '$BM = CN$ và $DP = AQ$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Vì $ABCD$ là hình bình hành nên $AB = CD$ và $BC = DA$. Mà $AM = CP$ và $BN = DQ$ nên $AB - AM = CD - CP \\Rightarrow BM = DP$, và $BC - BN = DA - DQ \\Rightarrow CN = AQ$.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì $AB = CD$ và $AM = CP$ nên $BM = DP$, còn $CN = AQ$.''')
        
        th_da_1_d = '\\True Tứ giác $MNPQ$ luôn là một hình bình hành'
        th_da_1_s = 'Tứ giác $MNPQ$ chỉ là hình bình hành khi $M, N, P, Q$ là trung điểm bốn cạnh'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Ta có $\\Delta AMQ = \\Delta CPN$ (c.g.c) vì $AM = CP$, $\\widehat{A} = \\widehat{C}$, $AQ = CN$, suy ra $MQ = NP$. Tương tự $\\Delta BMN = \\Delta DPQ$ (c.g.c) nên $MN = PQ$. Tứ giác $MNPQ$ có các cạnh đối bằng nhau nên là hình bình hành.''')
        loigiai_th_1_s = ('''Mệnh đề sai vì $MNPQ$ luôn có các cạnh đối bằng nhau ($MQ = NP$ và $MN = PQ$) nên luôn là hình bình hành.''')
        
        vd_da_1_d = '\\True Giao điểm hai đường chéo của hình bình hành $MNPQ$ trùng với điểm $O$'
        vd_da_1_s = 'Giao điểm hai đường chéo của hình bình hành $MNPQ$ không trùng với điểm $O$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Tứ giác $AMCP$ có $AM // CP$ và $AM = CP$ nên là hình bình hành, suy ra hai đường chéo $AC$ và $MP$ cắt nhau tại trung điểm $O$ của $AC$. Tương tự $NQ$ cũng đi qua trung điểm $O$ của $BD$. Vậy giao điểm của $MP$ và $NQ$ trùng với $O$.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì $O$ là trung điểm của cả $MP$ và $NQ$ nên giao điểm hai đường chéo của $MNPQ$ trùng với $O$.''')
        
        vdc_da_1_d = '\\True Biết $AB = %s$ cm và $AM = %s$ cm thì độ dài đoạn thẳng $DP$ bằng $%s$ cm' % (ab, am, bm)
        vdc_da_1_s = 'Biết $AB = %s$ cm và $AM = %s$ cm thì độ dài đoạn thẳng $DP$ bằng $%s$ cm' % (ab, am, am)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Ta có $CD = AB = %s$ cm và $CP = AM = %s$ cm. Suy ra $DP = CD - CP = %s - %s = %s$ (cm).''' % (ab, am, ab, am, bm))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $DP = CD - CP = %s - %s = %s$ cm.''' % (ab, am, bm))
        
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
