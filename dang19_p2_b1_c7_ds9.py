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


def bt_dang19_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        fa1, fa2, fa3, fa4 = 4, 12, 6, 3
        noidungcauhoi = ('''Kiểm tra thời gian hoàn thành một chi tiết máy (đơn vị: giây) của $25$ sản phẩm trên mỗi dây chuyền $A$ và $B$, thu được hai bảng tần số:
\\begin{center}
\\textbf{Dây chuyền $A$:} \\quad
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Thời gian (giây) & $18$ & $19$ & $20$ & $21$ \\\\
\\hline
Tần số & $4$ & $12$ & $6$ & $3$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\begin{center}
\\textbf{Dây chuyền $B$:} \\quad
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Thời gian (giây) & $18$ & $19$ & $20$ & $21$ \\\\
\\hline
Tần số & $7$ & $8$ & $7$ & $3$ \\\\
\\hline
\\end{tabular}
\\end{center}''')
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Cả hai dây chuyền đều có cỡ mẫu kiểm tra bằng $25$')
        nb_da_1_s = ('Dây chuyền $A$ có cỡ mẫu lớn hơn dây chuyền $B$')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Dây chuyền $A$ có mức độ tập trung cao hơn ở mốc $19$ giây so với dây chuyền $B$')
        th_da_1_s = ('Dây chuyền $B$ có tần số ở mốc $19$ giây cao hơn dây chuyền $A$')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Tỉ lệ sản phẩm hoàn thành nhanh nhất ($18$ giây) ở dây chuyền $B$ cao hơn ở dây chuyền $A$ là $12\\%$')
        vd_da_1_s = ('Tỉ lệ sản phẩm hoàn thành nhanh nhất ($18$ giây) ở dây chuyền $B$ cao hơn ở dây chuyền $A$ là $3\\%$')
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Nếu tiêu chuẩn đạt yêu cầu là thời gian hoàn thành không quá $19$ giây thì dây chuyền $A$ có nhiều sản phẩm đạt hơn dây chuyền $B$')
        vdc_da_1_s = ('Nếu tiêu chuẩn đạt yêu cầu là thời gian hoàn thành không quá $19$ giây thì dây chuyền $B$ có nhiều sản phẩm đạt hơn dây chuyền $A$')
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        
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
        
        loigiai_nb_1 = ('Đúng. Tổng tần số ở dây chuyền $A$ là $4 + 12 + 6 + 3 = 25$ và ở dây chuyền $B$ là $7 + 8 + 7 + 3 = 25$.') if '\\True' in nb_da_1 else ('Sai. Cả hai bảng tần số đều có tổng tần số bằng $25$ sản phẩm.')
        loigiai_th_1 = ('Đúng. Tại mốc $19$ giây, dây chuyền $A$ có tần số $12$, cao hơn dây chuyền $B$ (tần số $8$).') if '\\True' in th_da_1 else ('Sai. Tần số ở mốc $19$ giây của dây chuyền $A$ là $12$, lớn hơn của dây chuyền $B$ ($8$).')
        loigiai_vd_1 = ('Đúng. Tỉ lệ ở dây chuyền $B$ là $\\dfrac{7}{25} = 28\\%$, ở dây chuyền $A$ là $\\dfrac{4}{25} = 16\\%$, chênh lệch $28\\% - 16\\% = 12\\%$.') if '\\True' in vd_da_1 else ('Sai. Chênh lệch là $3$ sản phẩm trên tổng số $25$ sản phẩm, tương ứng với $\\dfrac{3}{25} \\cdot 100\\% = 12\\%$.')
        loigiai_vdc_1 = ('Đúng. Số sản phẩm hoàn thành trong $18$ hoặc $19$ giây ở dây chuyền $A$ là $4 + 12 = 16$, nhiều hơn dây chuyền $B$ ($7 + 8 = 15$).') if '\\True' in vdc_da_1 else ('Sai. Dây chuyền $A$ có $4 + 12 = 16$ sản phẩm đạt yêu cầu, nhiều hơn dây chuyền $B$ ($7 + 8 = 15$ sản phẩm).')
        
        list_nb_1 = [nb_da_1]
        list_nb_2 = [loigiai_nb_1]
        combined_nb = list(zip(list_nb_1, list_nb_2))
        random.shuffle(combined_nb)
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        list_th_1 = [th_da_1]
        list_th_2 = [loigiai_th_1]
        combined_th = list(zip(list_th_1, list_th_2))
        random.shuffle(combined_th)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        list_vd_1 = [vd_da_1]
        list_vd_2 = [loigiai_vd_1]
        combined_vd = list(zip(list_vd_1, list_vd_2))
        random.shuffle(combined_vd)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        list_vdc_1 = [vdc_da_1]
        list_vdc_2 = [loigiai_vdc_1]
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))
        random.shuffle(combined_vdc)
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
