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

def bt_dang17_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        s1 = randint(10, 22)
        s2 = randint(12, 25)
        s_tong = s1 + s2
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (2.2,2.2);
\\coordinate (B) at (0.8,0.5);
\\coordinate (C) at (3.8,0.5);
\\coordinate (D) at (-0.6,1.2);
\\coordinate (E) at (0.8,2.9);
\\coordinate (F) at (3.7,2.8);
\\coordinate (G) at (5.3,1.1);
\\coordinate (H) at (2.2,2.85);
\\coordinate (M) at (0.8,-0.15);
\\coordinate (N) at (3.8,-0.15);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (A)--(B)--(D)--(E)--cycle (A)--(C)--(G)--(F)--cycle (B)--(C)--(N)--(M)--cycle;
\\draw[line width=1pt, dashed] (E)--(H)--(F) (A)--(H);
\\fill (A) circle (1pt) node[below] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[above left] {$E$};
\\fill (F) circle (1pt) node[above right] {$F$};
\\fill (G) circle (1pt) node[right] {$G$};
\\fill (H) circle (1pt) node[above] {$H$};
\\fill (M) circle (1pt) node[below left] {$M$};
\\fill (N) circle (1pt) node[below right] {$N$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho tam giác $ABC$. Về phía ngoài tam giác $ABC$, dựng hai hình bình hành bất kì $ABDE$ và $ACFG$. Gọi $H$ là giao điểm của hai đường thẳng $DE$ và $FG$. Dựng hình bình hành $BCNM$ về phía ngoài tam giác $ABC$ sao cho $BM // AH$ và $BM = AH$ (như hình vẽ).
%s''' % (hinh_ve))
        
        nb_da_1_d = '\\True Tứ giác $ABMH$ là hình bình hành'
        nb_da_1_s = 'Tứ giác $ABMH$ không phải là hình bình hành'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Tứ giác $ABMH$ có một cặp cạnh đối song song và bằng nhau ($BM // AH$ và $BM = AH$) nên theo Định lí 2b, $ABMH$ là hình bình hành.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì theo giả thiết $BM // AH$ và $BM = AH$ nên tứ giác $ABMH$ là hình bình hành.''')
        
        th_da_1_d = '\\True $MH = AB$ và $MH // AB$'
        th_da_1_s = '$MH = AC$ và $MH // AC$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Vì $ABMH$ là hình bình hành nên hai cạnh đối $MH$ và $AB$ song song và bằng nhau ($MH = AB$, $MH // AB$).''')
        loigiai_th_1_s = ('''Mệnh đề sai vì $MH$ và $AB$ là hai cạnh đối của hình bình hành $ABMH$ nên $MH = AB$ và $MH // AB$.''')
        
        vd_da_1_d = '\\True Tứ giác $ACNH$ cũng là một hình bình hành'
        vd_da_1_s = 'Tứ giác $ACNH$ không phải là hình bình hành'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Vì $BCNM$ là hình bình hành nên $CN // BM$ và $CN = BM$. Kết hợp với $BM // AH$ và $BM = AH$, ta suy ra $CN // AH$ và $CN = AH$. Do đó tứ giác $ACNH$ là hình bình hành.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì $CN // AH$ và $CN = AH$ nên tứ giác $ACNH$ là hình bình hành.''')
        
        vdc_da_1_d = '\\True Nếu diện tích hai hình bình hành $ABDE$ và $ACFG$ lần lượt là $%s\\text{ cm}^2$ và $%s\\text{ cm}^2$ thì diện tích hình bình hành $BCNM$ bằng $%s\\text{ cm}^2$' % (s1, s2, s_tong)
        vdc_da_1_s = 'Nếu diện tích hai hình bình hành $ABDE$ và $ACFG$ lần lượt là $%s\\text{ cm}^2$ và $%s\\text{ cm}^2$ thì diện tích hình bình hành $BCNM$ bằng $%s\\text{ cm}^2$' % (s1, s2, abs(s2 - s1) + 1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Ta có $S_{ABDE} = S_{ABMH}$ (chung đáy $AB$, chung chiều cao giữa $AB$ và $DE$) và $S_{ACFG} = S_{ACNH}$ (chung đáy $AC$, chung chiều cao giữa $AC$ và $FG$). Mặt khác $S_{BCNM} = S_{ABMH} + S_{ACNH}$ (do $\\Delta ABC = \\Delta MHN$) nên $S_{BCNM} = S_{ABDE} + S_{ACFG} = %s + %s = %s$ ($\\text{cm}^2$).''' % (s1, s2, s_tong))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì theo định lí Pappus về diện tích hình bình hành, $S_{BCNM} = S_{ABDE} + S_{ACFG} = %s + %s = %s$ ($\\text{cm}^2$).''' % (s1, s2, s_tong))
        
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
