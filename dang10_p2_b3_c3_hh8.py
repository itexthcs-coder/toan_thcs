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

def bt_dang10_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab = randint(6, 12)
        ad = randint(4, 8)
        cv = 2 * (ab + ad)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.4);
\\coordinate (B) at (5.2,2.4);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (I) at ($(B)!0.38!(D)$);
\\coordinate (M) at ($(A)!0.38!(D)$);
\\coordinate (N) at ($(B)!0.38!(C)$);
\\coordinate (P) at ($(B)!0.38!(A)$);
\\coordinate (Q) at ($(C)!0.38!(D)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (B)--(D) (M)--(N) (P)--(Q);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (I) circle (1pt) node[above left] {$I$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[right] {$N$};
\\fill (P) circle (1pt) node[above] {$P$};
\\fill (Q) circle (1pt) node[below] {$Q$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có $AB = %s$ cm, $AD = %s$ cm. Lấy điểm $I$ bất kì nằm trên đường chéo $BD$. Qua $I$ kẻ đường thẳng song song với $AB$ cắt $AD$ tại $M$, cắt $BC$ tại $N$; kẻ đường thẳng song song với $AD$ cắt $AB$ tại $P$, cắt $CD$ tại $Q$ (như hình vẽ).
%s''' % (ab, ad, hinh_ve))
        
        nb_da_1_d = '\\True Tứ giác $APIM$ là hình bình hành'
        nb_da_1_s = 'Tứ giác $APIM$ không phải là hình bình hành'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Tứ giác $APIM$ có $AP // MI$ (do $AB // MN$) và $AM // PI$ (do $AD // PQ$) nên theo định nghĩa, $APIM$ là hình bình hành.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì tứ giác $APIM$ có các cạnh đối song song nên là hình bình hành.''')
        
        th_da_1_d = '\\True Tứ giác $INQC$ là hình bình hành'
        th_da_1_s = 'Tứ giác $INQC$ chỉ là hình thang'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Tứ giác $INQC$ có $IN // QC$ (do $MN // CD$) và $IQ // NC$ (do $PQ // BC$) nên $INQC$ là hình bình hành.''')
        loigiai_th_1_s = ('''Mệnh đề sai vì tứ giác $INQC$ có các cạnh đối song song nên là hình bình hành.''')
        
        vd_da_1_d = '\\True Hai hình bình hành $APIM$ và $INQC$ chỉ bằng nhau khi $I$ là trung điểm của đường chéo $BD$'
        vd_da_1_s = 'Hai hình bình hành $APIM$ và $INQC$ luôn bằng nhau với mọi vị trí của điểm $I$ trên $BD$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Khi $I$ di chuyển trên $BD$, kích thước của $APIM$ và $INQC$ thay đổi; chúng chỉ bằng nhau khi $I$ là trung điểm của $BD$.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì khi $I$ không phải trung điểm $BD$ thì $AM \\ne MD$, hai hình bình hành $APIM$ và $INQC$ có kích thước khác nhau.''')
        
        vdc_da_1_d = '\\True Tổng chu vi của hai hình bình hành $APIM$ và $INQC$ luôn bằng $%s$ cm' % (cv)
        vdc_da_1_s = 'Tổng chu vi của hai hình bình hành $APIM$ và $INQC$ bằng $%s$ cm' % (ab + ad)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Vì $MIPD$ và $BINP$ cũng là các hình bình hành nên $MI = DP$ và $IQ = MD$. Do đó tổng chu vi hai hình bình hành $APIM$ và $INQC$ là: $2(AP + AM) + 2(IQ + QC) = 2(AP + DP) + 2(MD + AM) = 2(AB + AD) = 2 \\cdot (%s + %s) = %s$ (cm).''' % (ab, ad, cv))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì tổng chu vi của hai hình bình hành $APIM$ và $INQC$ đúng bằng chu vi hình bình hành $ABCD$, tức là $2 \\cdot (%s + %s) = %s$ cm.''' % (ab, ad, cv))
        
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
