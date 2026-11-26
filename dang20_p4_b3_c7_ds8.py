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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang20_p4_b3_c7_ds8(self):
    # Dạng 20 (Thực tế): Hàm số cho bằng biểu đồ đoạn thẳng mô tả mực nước sông trong tuần lũ
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        h1 = random.choice([3.1, 3.2])
        h_eq = random.choice([4.0, 4.1]) # Ngày 2 và Ngày 5 cùng bằng h_eq
        h3 = random.choice([5.1, 5.2])   # Ngày 3 đỉnh lũ
        h4 = random.choice([4.7, 4.8])   # Ngày 4 > 4,5
        h6 = random.choice([3.4, 3.5])

        def fmt_vn(val):
            return str(val).replace('.', ',')

        h1_s, heq_s, h3_s, h4_s, h6_s = fmt_vn(h1), fmt_vn(h_eq), fmt_vn(h3), fmt_vn(h4), fmt_vn(h6)

        hinh_tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (0,0) -- (7,0) node[below] {Ngày $x$};\n'
            '\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {$h$ (m)};\n'
            '\\coordinate (O) at (0,0);\n'
            '\\coordinate (D1) at (1,1.2);\n'
            '\\coordinate (D2) at (2,1.8);\n'
            '\\coordinate (D3) at (3,2.7);\n'
            '\\coordinate (D4) at (4,2.4);\n'
            '\\coordinate (D5) at (5,1.8);\n'
            '\\coordinate (D6) at (6,1.4);\n'
            '\\draw[line width=1pt] (D1) -- (D2) -- (D3) -- (D4) -- (D5) -- (D6);\n'
            '\\fill (O) circle (1pt) node[below left] {$O$};\n'
            '\\fill (D1) circle (1pt) node[below] {$%s$};\n'
            '\\fill (D2) circle (1pt) node[above left] {$%s$};\n'
            '\\fill (D3) circle (1pt) node[above] {$%s$};\n'
            '\\fill (D4) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (D5) circle (1pt) node[above right] {$%s$};\n'
            '\\fill (D6) circle (1pt) node[right] {$%s$};\n'
            '\\foreach \\i in {1,2,3,4,5,6} {\\node at (\\i,-0.25) {$\\i$};}\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        ) % (h1_s, heq_s, h3_s, h4_s, heq_s, h6_s)

        noidungcauhoi = (
            'Biểu đồ đoạn thẳng dưới đây mô tả mực nước $h$ (đơn vị: mét) của một con sông đo được tại trạm thủy văn lúc $7\\text{ giờ}$ sáng trong $6$ ngày liên tiếp ($x \\in \\{1; 2; 3; 4; 5; 6\\}$) của một tuần lũ:\\ %s'
        ) % (hinh_tikz)

        # Nhận biết
        nb_da_1_d = '\\True Mực nước sông đạt đỉnh cao nhất vào Ngày $3$ với mức nước là $h(3) = %s\\text{ m}$' % (h3_s)
        nb_da_1_s = 'Mực nước sông đạt đỉnh cao nhất vào Ngày $4$ với mức nước là $h(4) = %s\\text{ m}$' % (h4_s)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = 'Quan sát điểm cao nhất trên biểu đồ đoạn thẳng là tại ngày $x = 3$ với $h(3) = %s\\text{ m}$.' % (h3_s)

        # Thông hiểu
        th_da_1_d = '\\True Đại lượng mực nước $h$ là một hàm số của ngày đo $x \\in \\{1; 2; 3; 4; 5; 6\\}$'
        th_da_1_s = 'Đại lượng mực nước $h$ không phải là hàm số của ngày đo $x$ vì mực nước lên xuống không đều'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = 'Vì ứng với mỗi ngày đo $x \\in \\{1; 2; 3; 4; 5; 6\\}$ chỉ đo được duy nhất một giá trị mực nước $h$ nên $h$ là hàm số của $x$.'

        # Vận dụng
        vd_da_1_d = '\\True Biết mức báo động lũ cấp II là $4,5\\text{ m}$, có đúng $2$ ngày trong tuần lũ mực nước vượt mức báo động cấp II là Ngày $3$ và Ngày $4$'
        vd_da_1_s = 'Biết mức báo động lũ cấp II là $4,5\\text{ m}$, có tới $4$ ngày trong tuần lũ mực nước vượt mức báo động cấp II'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = 'So sánh các giá trị mực nước với $4,5\\text{ m}$, chỉ có $h(3) = %s\\text{ m} > 4,5\\text{ m}$ và $h(4) = %s\\text{ m} > 4,5\\text{ m}$.' % (h3_s, h4_s)

        # Vận dụng cao
        vdc_da_1_d = '\\True Có hai ngày khác nhau là Ngày $2$ và Ngày $5$ có cùng mực nước $h(2) = h(5) = %s\\text{ m}$ và điều này hoàn toàn phù hợp với định nghĩa hàm số' % (heq_s)
        vdc_da_1_s = 'Vì Ngày $2$ và Ngày $5$ có cùng mực nước $%s\\text{ m}$ nên vi phạm định nghĩa hàm số' % (heq_s)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = (
            'Ta có $h(2) = h(5) = %s\\text{ m}$. Theo định nghĩa hàm số, mỗi giá trị của $x$ cho duy nhất một giá trị của $h$, còn hai giá trị khác nhau của $x$ vẫn có thể cùng cho một giá trị của $h$.'
        ) % (heq_s)

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

        list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
        list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

        combined_nb = list(zip(list_nb_1, list_nb_2))
        combined_th = list(zip(list_th_1, list_th_2))
        combined_vd = list(zip(list_vd_1, list_vd_2))
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))
        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)

        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

        content = (
            '\\begin{minipage}{\\textwidth} \n'
            '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
            '\\choiceTFn \n'
            '{' + str(shuffled_answers_nb[0]) + '}\n'
            '{' + str(shuffled_answers_th[0]) + '}\n'
            '{' + str(shuffled_answers_vd[0]) + '}\n'
            '{' + str(shuffled_answers_vdc[0]) + '}\n'
            '\\loigiai{ \n'
            '\\begin{enumEX}[a)]{1} \n'
            '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
            '\\item ' + str(shuffled_solutions_th[0]) + '\n'
            '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
            '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
            '\\end{enumEX}} \n'
            '\\end{ex}\n \\end{minipage}\n\n'
        )
        return content
