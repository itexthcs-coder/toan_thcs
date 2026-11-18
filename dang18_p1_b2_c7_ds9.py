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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang18_p1_b2_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cap_goc = random.choice([(144, 40), (126, 35), (108, 30), (162, 45), (54, 15)])
        goc_an, f_kq = cap_goc
        goc_nha = 108

        hinh_quat = f'''\\begin{{center}}
        \\begin{{tikzpicture}}[scale=0.85]
        \\fill[orange!55] (0,0) -- (0:2) arc (0:{goc_an}:2) -- cycle;
        \\fill[cyan!45] (0,0) -- ({goc_an}:2) arc ({goc_an}:{goc_an+goc_nha}:2) -- cycle;
        \\fill[gray!35] (0,0) -- ({goc_an+goc_nha}:2) arc ({goc_an+goc_nha}:360:2) -- cycle;
        \\draw[thick] (0,0) circle (2);
        \\draw (0,0) -- (0:2) (0,0) -- ({goc_an}:2) (0,0) -- ({goc_an+goc_nha}:2);
        \\node at ({goc_an/2}:1.15) {{\\footnotesize ${goc_an}^\\circ$}};
        \\fill[orange!55] (2.6, 1.0) rectangle (2.9, 1.3); \\node[right] at (3.0, 1.15) {{\\footnotesize Tiền ăn}};
        \\fill[cyan!45] (2.6, 0.3) rectangle (2.9, 0.6); \\node[right] at (3.0, 0.45) {{\\footnotesize Tiền nhà}};
        \\fill[gray!35] (2.6, -0.4) rectangle (2.9, -0.1); \\node[right] at (3.0, -0.25) {{\\footnotesize Chi khác}};
        \\end{{tikzpicture}}
        \\end{{center}}'''

        # Các đáp án trắc nghiệm
        du = [f'${f_kq}\\%$']
        da = random.choice(du)
        s = list(set([f'${f_kq - 5}\\%$', f'${f_kq + 5}\\%$', f'${f_kq + 10}\\%$', f'${100 - f_kq}\\%$']) - set(du))
        das1, das2, das3 = random.sample(s, 3)

        # Câu hỏi
        noidungcauhoi = f'''Trên một biểu đồ hình quạt tròn biểu diễn cơ cấu chi tiêu hằng tháng của một gia đình, hình quạt biểu diễn khoản ``Tiền ăn'' có góc ở tâm đo được là ${goc_an}^\\circ$ (như hình vẽ):{hinh_quat}Khoản ``Tiền ăn'' chiếm bao nhiêu phần trăm trong tổng chi tiêu của gia đình đó?'''

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = f'''Gọi $f$ là tần số tương đối của khoản ``Tiền ăn''. Ta có:
        $$ 360^\\circ \\cdot f = {goc_an}^\\circ \\Rightarrow f = \\frac{{{goc_an}^\\circ}}{{360^\\circ}} \\cdot 100\\% = {f_kq}\\%. $$'''

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
