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

def bt_dang13_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cv_abc = randint(10, 22)
        s_abc = randint(8, 20)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.2,0);
\\coordinate (D1) at (4.7,2.2);
\\coordinate (D2) at (-1.7,2.2);
\\coordinate (D3) at (1.7,-2.2);
\\draw[line width=1pt] (A)--(B)--(C)--cycle;
\\draw[line width=1pt, dashed] (A)--(D1)--(C) (A)--(D2)--(B) (B)--(D3)--(C) (D1)--(D2)--(D3)--cycle;
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[left] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D1) circle (1pt) node[above right] {$D_1$};
\\fill (D2) circle (1pt) node[above left] {$D_2$};
\\fill (D3) circle (1pt) node[below] {$D_3$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Trong mặt phẳng cho ba điểm $A, B, C$ không thẳng hàng. Xét bài toán tìm điểm $D$ sao cho điểm $D$ cùng với ba điểm $A, B, C$ là bốn đỉnh của một hình bình hành (như hình vẽ).
%s''' % (hinh_ve))
        
        nb_da_1_d = '\\True Có tất cả $3$ điểm $D$ thỏa mãn yêu cầu bài toán'
        nb_da_1_s = 'Chỉ có duy nhất $1$ điểm $D$ thỏa mãn yêu cầu bài toán'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Ứng với ba cách chọn một đoạn thẳng làm đường chéo ($BC$, $AC$ hoặc $AB$), ta dựng được $3$ điểm $D_1, D_2, D_3$ thỏa mãn yêu cầu bài toán.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì có $3$ trường hợp tương ứng với việc chọn $BC$, $AC$ hoặc $AB$ làm đường chéo của hình bình hành.''')
        
        th_da_1_d = '\\True Nếu $D_1$ là đỉnh đối diện với đỉnh $A$ trong hình bình hành $ABD_1C$ thì diện tích hình bình hành $ABD_1C$ bằng $%s\\text{ cm}^2$ (biết $S_{ABC} = %s\\text{ cm}^2$)' % (2 * s_abc, s_abc)
        th_da_1_s = 'Nếu $D_1$ là đỉnh đối diện với đỉnh $A$ trong hình bình hành $ABD_1C$ thì diện tích hình bình hành $ABD_1C$ bằng $%s\\text{ cm}^2$ (biết $S_{ABC} = %s\\text{ cm}^2$)' % (s_abc, s_abc)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Đường chéo $BC$ chia hình bình hành $ABD_1C$ thành hai tam giác bằng nhau $\\Delta ABC$ và $\\Delta D_1CB$ nên $S_{ABD_1C} = 2S_{ABC} = 2 \\cdot %s = %s$ ($\\text{cm}^2$).''' % (s_abc, 2 * s_abc))
        loigiai_th_1_s = ('''Mệnh đề sai vì đường chéo $BC$ chia hình bình hành $ABD_1C$ thành hai tam giác bằng nhau nên $S_{ABD_1C} = 2S_{ABC} = %s$ ($\\text{cm}^2$).''' % (2 * s_abc))
        
        vd_da_1_d = '\\True Ba điểm $D_1, D_2, D_3$ tìm được luôn tạo thành một tam giác'
        vd_da_1_s = 'Ba điểm $D_1, D_2, D_3$ tìm được luôn thẳng hàng'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Vì $AD_1 // BC$, $AD_1 = BC$ và $D_2A // BC$, $D_2A = BC$ nên $A$ là trung điểm của $D_1D_2$. Tương tự $B$ là trung điểm của $D_2D_3$ và $C$ là trung điểm của $D_1D_3$. Vì $A, B, C$ không thẳng hàng nên $D_1, D_2, D_3$ không thẳng hàng, tạo thành một tam giác.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì $A, B, C$ lần lượt là trung điểm các cạnh của $\\Delta D_1D_2D_3$ nên ba điểm $D_1, D_2, D_3$ không thẳng hàng.''')
        
        vdc_da_1_d = '\\True Nếu chu vi tam giác $ABC$ bằng $%s$ cm thì chu vi tam giác $D_1D_2D_3$ bằng $%s$ cm' % (cv_abc, 2 * cv_abc)
        vdc_da_1_s = 'Nếu chu vi tam giác $ABC$ bằng $%s$ cm thì chu vi tam giác $D_1D_2D_3$ bằng $%s$ cm' % (cv_abc, 3 * cv_abc)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Ta có $D_1D_2 = 2BC$, $D_2D_3 = 2AC$, $D_1D_3 = 2AB$. Do đó chu vi tam giác $D_1D_2D_3$ gấp đôi chu vi tam giác $ABC$ và bằng $2 \\cdot %s = %s$ (cm).''' % (cv_abc, 2 * cv_abc))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì mỗi cạnh của $\\Delta D_1D_2D_3$ gấp đôi cạnh tương ứng của $\\Delta ABC$ nên chu vi $\\Delta D_1D_2D_3$ bằng $2 \\cdot %s = %s$ cm.''' % (cv_abc, 2 * cv_abc))
        
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
