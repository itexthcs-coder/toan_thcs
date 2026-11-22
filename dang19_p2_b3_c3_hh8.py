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

def bt_dang19_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ad = randint(4, 9)
        ab = 2 * ad
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.0,2.2);
\\coordinate (B) at (5.8,2.2);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4.8,0);
\\coordinate (E) at ($(A)!0.5!(B)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (D)--(E)--(C);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (E) circle (1pt) node[above] {$E$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có $AB = 2AD$ và $AD = %s$ cm. Gọi $E$ là trung điểm của cạnh $AB$ (như hình vẽ).
%s''' % (ad, hinh_ve))
        
        nb_da_1_d = '\\True Tam giác $ADE$ là tam giác cân tại $A$'
        nb_da_1_s = 'Tam giác $ADE$ là tam giác cân tại $D$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Vì $E$ là trung điểm của $AB$ nên $AE = \\frac{1}{2}AB = AD = %s$ cm. Do đó $\\Delta ADE$ cân tại $A$.''' % (ad))
        loigiai_nb_1_s = ('''Mệnh đề sai vì $AE = \\frac{1}{2}AB = AD$ nên $\\Delta ADE$ cân tại $A$.''')
        
        th_da_1_d = '\\True Tia $DE$ là tia phân giác của góc $ADC$'
        th_da_1_s = 'Tia $DE$ không phải là tia phân giác của góc $ADC$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Vì $\\Delta ADE$ cân tại $A$ nên $\\widehat{ADE} = \\widehat{AED}$. Mặt khác $AB // CD$ nên $\\widehat{AED} = \\widehat{EDC}$ (hai góc so le trong). Suy ra $\\widehat{ADE} = \\widehat{EDC}$, hay tia $DE$ là tia phân giác của $\\widehat{ADC}$.''')
        loigiai_th_1_s = ('''Mệnh đề sai vì $\\widehat{ADE} = \\widehat{AED} = \\widehat{EDC}$ nên $DE$ là tia phân giác của $\\widehat{ADC}$.''')
        
        vd_da_1_d = '\\True Tia $CE$ là tia phân giác của góc $BCD$'
        vd_da_1_s = 'Tam giác $BCE$ không phải là tam giác cân'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Tương tự, ta có $BE = \\frac{1}{2}AB = BC$ nên $\\Delta BCE$ cân tại $B$, suy ra $\\widehat{BCE} = \\widehat{BEC}$. Mà $\\widehat{BEC} = \\widehat{ECD}$ (so le trong) nên $\\widehat{BCE} = \\widehat{ECD}$, hay $CE$ là tia phân giác của $\\widehat{BCD}$.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì $BE = BC$ nên $\\Delta BCE$ cân tại $B$ và $CE$ là tia phân giác của $\\widehat{BCD}$.''')
        
        vdc_da_1_d = '\\True Góc $DEC$ có số đo bằng $90^\\circ$'
        vdc_da_1_s = 'Góc $DEC$ có số đo bằng $60^\\circ$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Trong hình bình hành $ABCD$, hai góc kề cạnh $CD$ bù nhau nên $\\widehat{ADC} + \\widehat{BCD} = 180^\\circ$. Vì $DE$ và $CE$ lần lượt là tia phân giác của $\\widehat{ADC}$ và $\\widehat{BCD}$ nên $\\widehat{EDC} + \\widehat{ECD} = \\frac{1}{2}(\\widehat{ADC} + \\widehat{BCD}) = 90^\\circ$. Xét $\\Delta DEC$ có $\\widehat{DEC} = 180^\\circ - (\\widehat{EDC} + \\widehat{ECD}) = 180^\\circ - 90^\\circ = 90^\\circ$.''')
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $DE$ và $CE$ là hai tia phân giác của hai góc trong cùng phía bù nhau nên vuông góc với nhau, tức là $\\widehat{DEC} = 90^\\circ$.''')
        
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
