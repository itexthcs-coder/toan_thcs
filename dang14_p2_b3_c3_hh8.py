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

def bt_dang14_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        io = randint(150, 400)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (I) at (0,0);
\\coordinate (A) at (2.2,2.6);
\\coordinate (B) at (3.6,0);
\\coordinate (C) at (5.8,2.6);
\\coordinate (O) at ($(I)!0.5!(C)$);
\\draw[line width=1pt] (I)--(3.1,3.66) node[left] {$a$};
\\draw[line width=1pt] (I)--(5.2,0) node[below] {$b$};
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt, dashed] (I)--(C) (A)--(C)--(B);
\\fill (I) circle (1pt) node[below left] {$I$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\fill (O) circle (1pt) node[below right] {$O$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Hai con đường thẳng $a$ và $b$ cắt nhau tại ngã tư $I$ tạo thành một góc nhọn. Bên trong góc đó có một điểm dân cư $O$. Người ta muốn mở một con đường thẳng đi qua $O$ cắt đường $a$ tại $A$ và cắt đường $b$ tại $B$ sao cho hai đoạn đường $OA$ và $OB$ bằng nhau (như hình vẽ).
%s''' % (hinh_ve))
        
        nb_da_1_d = '\\True Đoạn đường $AB$ cần mở chính là một đường chéo của hình bình hành nhận $IA$ và $IB$ làm hai cạnh liên tiếp'
        nb_da_1_s = 'Đoạn đường $AB$ cần mở luôn vuông góc với một trong hai con đường $a$ hoặc $b$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Khi dựng hình bình hành $IACB$ có hai cạnh liên tiếp nằm trên $a$ và $b$ sao cho giao điểm hai đường chéo là $O$, thì đường chéo $AB$ đi qua $O$ và thỏa mãn $OA = OB$.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì đoạn đường $AB$ là đường chéo của hình bình hành có hai cạnh liên tiếp nằm trên $a$ và $b$, không nhất thiết vuông góc với $a$ hay $b$.''')
        
        th_da_1_d = '\\True Để xác định điểm $A$, ta lấy điểm $C$ đối xứng với $I$ qua $O$, sau đó từ $C$ kẻ đường thẳng song song với đường $b$ cắt đường $a$ tại $A$'
        th_da_1_s = 'Để xác định điểm $A$, ta kẻ từ $O$ đường thẳng vuông góc với đường $a$ tại $A$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Lấy $C$ trên tia $IO$ sao cho $OC = OI$; từ $C$ kẻ đường thẳng song song với $b$ cắt $a$ tại $A$ và kẻ đường thẳng song song với $a$ cắt $b$ tại $B$. Khi đó $IACB$ là hình bình hành có hai đường chéo $IC$ và $AB$ cắt nhau tại trung điểm $O$ của $IC$, suy ra $O$ là trung điểm của $AB$ hay $OA = OB$.''')
        loigiai_th_1_s = ('''Mệnh đề sai vì nếu kẻ vuông góc với $a$ thì $O$ không nhất thiết là trung điểm của $AB$.''')
        
        vd_da_1_d = '\\True Nếu khoảng cách từ ngã tư $I$ đến điểm dân cư $O$ bằng $%s$ m thì độ dài đoạn thẳng $IC$ bằng $%s$ m' % (io, 2 * io)
        vd_da_1_s = 'Nếu khoảng cách từ ngã tư $I$ đến điểm dân cư $O$ bằng $%s$ m thì độ dài đoạn đường $AB$ luôn bằng $%s$ m' % (io, 2 * io)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Vì $O$ là trung điểm của đường chéo $IC$ trong hình bình hành $IACB$ nên $IC = 2 \\cdot IO = 2 \\cdot %s = %s$ (m).''' % (io, 2 * io))
        loigiai_vd_1_s = ('''Mệnh đề sai vì $2 \\cdot IO = IC = %s$ m, còn trong hình bình hành $IACB$ hai đường chéo $AB$ và $IC$ không nhất thiết bằng nhau.''' % (2 * io))
        
        vdc_da_1_d = '\\True Với mỗi vị trí điểm dân cư $O$ nằm trong góc nhọn tạo bởi $a$ và $b$, ta chỉ vẽ được duy nhất một con đường thẳng $AB$ thỏa mãn yêu cầu bài toán'
        vdc_da_1_s = 'Với mỗi vị trí điểm dân cư $O$ nằm trong góc nhọn tạo bởi $a$ và $b$, ta vẽ được vô số con đường thẳng $AB$ thỏa mãn yêu cầu bài toán'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Với mỗi điểm $O$ cho trước, điểm $C$ đối xứng với $I$ qua $O$ là duy nhất; qua $C$ chỉ kẻ được duy nhất một đường thẳng song song với $b$ cắt $a$ tại $A$ duy nhất, nên đường thẳng $AB$ đi qua $O$ và $A$ là duy nhất.''')
        loigiai_vdc_1_s = ('''Mệnh đề sai vì qua điểm $C$ chỉ có duy nhất một đường thẳng song song với $b$ nên vị trí của $A$ và $B$ là duy nhất.''')
        
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
