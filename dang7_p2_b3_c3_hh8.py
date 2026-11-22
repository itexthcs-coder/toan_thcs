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

def bt_dang7_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ngan = randint(3, 6)
        dai = randint(ngan + 2, 11)
        cv = 2 * (dai + ngan)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.2);
\\coordinate (B) at (4.8,2.2);
\\coordinate (D) at (0,0);
\\coordinate (C) at (3.6,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Một sợi dây xích được chia thành bốn đoạn thẳng: hai đoạn dài cùng có độ dài $%s$ dm và hai đoạn ngắn cùng có độ dài $%s$ dm, được xếp xen kẽ nhau rồi móc hai đầu mút lại thành một tứ giác $ABCD$ có các đỉnh tại các điểm chia (giả sử bốn đỉnh không thẳng hàng) (như hình vẽ).
%s''' % (dai, ngan, hinh_ve))
        
        nb_da_1_d = '\\True Tứ giác $ABCD$ luôn là một hình bình hành'
        nb_da_1_s = 'Tứ giác $ABCD$ chỉ là hình bình hành khi góc tại đỉnh $A$ bằng $90^\\circ$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Vì hai đoạn dài và hai đoạn ngắn xếp xen kẽ nhau nên tứ giác $ABCD$ có các cạnh đối bằng nhau ($AB = CD = %s$ dm, $BC = DA = %s$ dm). Theo Định lí 2a, tứ giác $ABCD$ là hình bình hành.''' % (dai, ngan))
        loigiai_nb_1_s = ('''Mệnh đề sai vì tứ giác có các cạnh đối bằng nhau luôn là hình bình hành với mọi số đo góc tại đỉnh $A$.''')
        
        th_da_1_d = '\\True Khi thay đổi độ mở góc tại đỉnh $A$, chu vi khung dây xích $ABCD$ không đổi và bằng $%s$ dm' % (cv)
        th_da_1_s = 'Khi thay đổi độ mở góc tại đỉnh $A$, chu vi khung dây xích $ABCD$ thay đổi theo'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Độ dài bốn đoạn dây xích không đổi nên chu vi tứ giác $ABCD$ luôn bằng $2 \\cdot (%s + %s) = %s$ (dm).''' % (dai, ngan, cv))
        loigiai_th_1_s = ('''Mệnh đề sai vì tổng độ dài bốn đoạn dây xích luôn không đổi và bằng $%s$ dm.''' % (cv))
        
        vd_da_1_d = '\\True Khi thay đổi hình dạng khung dây xích, khoảng cách giữa hai cạnh đối $AB$ và $CD$ có thể thay đổi'
        vd_da_1_s = 'Khi thay đổi hình dạng khung dây xích, khoảng cách giữa hai cạnh đối $AB$ và $CD$ luôn không đổi'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Khi kéo dãn khung dây xích, góc tại đỉnh $A$ thay đổi làm cho chiều cao (khoảng cách giữa hai đường thẳng song song $AB$ và $CD$) thay đổi.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì chiều cao ứng với cạnh $CD$ phụ thuộc vào độ lớn của góc $D$.''')
        
        vdc_da_1_d = '\\True Nếu căng hai sợi dây mảnh nối $A$ với $C$ và nối $B$ với $D$ thì hai sợi dây này luôn cắt nhau tại trung điểm của mỗi sợi'
        vdc_da_1_s = 'Nếu căng hai sợi dây mảnh nối $A$ với $C$ và nối $B$ với $D$ thì hai sợi dây này luôn có độ dài bằng nhau'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Vì $ABCD$ luôn là hình bình hành nên hai đường chéo $AC$ và $BD$ luôn cắt nhau tại trung điểm của mỗi đường.''')
        loigiai_vdc_1_s = ('''Mệnh đề sai vì hai đường chéo của hình bình hành cắt nhau tại trung điểm của mỗi đường nhưng độ dài của chúng không nhất thiết bằng nhau.''')
        
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
