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



def bt_dang17_p4_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R1 = randint(7, 12)
        b_rong = randint(6, 10)
        R2 = R1 + b_rong
        r_hoa = Rational(randint(3, 5), 2)
        d_max = R1 - r_hoa
        
        r_hoa_str = str(float(r_hoa)).replace('.', ',')
        d_max_str = str(float(d_max)).replace('.', ',')

        hinhve = '''
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (I) at (1.1,0);
\\draw[line width=1pt] (O) circle (2.6cm);
\\draw[line width=1pt] (O) circle (1.6cm);
\\draw[line width=1pt] (I) circle (0.5cm);
\\draw[line width=1pt] (O)--(1.6,0);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (I) circle (1pt) node[above] {$I$};
\\end{tikzpicture}
\\end{center}
'''

        noidungcauhoi = ('''Tại một ngã tư lớn, kỹ sư giao thông thiết kế một đảo tròn trung tâm (vòng xuyến) có tâm $O$ và bán kính $R_1 = %s\\text{ m}$. Bao quanh vòng xuyến là hai làn đường xe chạy đồng tâm tạo thành một hình vành khăn có bề rộng tổng cộng là $%s\\text{ m}$.\\\\
        a) Tính bán kính $R_2$ của đường tròn mép ngoài cùng làn đường và nêu vị trí tương đối giữa mép trong và mép ngoài của làn đường.\\\\
        b) Để trang trí, người ta xây một bồn hoa hình tròn $(I)$ có bán kính $r = %s\\text{ m}$ nằm hoàn toàn trong phạm vi của đảo tròn trung tâm. Hỏi tâm $I$ của bồn hoa có thể đặt cách tâm $O$ của vòng xuyến một khoảng tối đa là bao nhiêu mét để bồn hoa không lấn ra ngoài làn đường xe chạy? %s'''
                         % (latex(R1), latex(b_rong), r_hoa_str, hinhve))

        loigiai = ('''\\begin{enumEX}[a)]{1}
        \\item Bán kính đường tròn mép ngoài cùng của làn đường là: $R_2 = R_1 + %s = %s + %s = %s\\text{ (m)}$.\\\\
        Vì đường tròn mép trong $(O; %s\\text{ m})$ và đường tròn mép ngoài $(O; %s\\text{ m})$ có cùng tâm $O$ và bán kính khác nhau nên vị trí tương đối của chúng là hai đường tròn đồng tâm (trường hợp đặc biệt của đường tròn này đựng đường tròn kia).
        \\item Để bồn hoa $(I; %s\\text{ m})$ nằm hoàn toàn trong phạm vi đảo tròn trung tâm $(O; %s\\text{ m})$ thì đường tròn $(O)$ phải đựng đường tròn $(I)$ hoặc tiếp xúc trong với $(I)$ tại mép đảo.\\\\
        Do đó khoảng cách giữa hai tâm phải thỏa mãn điều kiện: $OI \\le R_1 - r = %s - %s = %s\\text{ (m)}$.\\\\
        Dấu bằng xảy ra khi bồn hoa tiếp xúc trong với mép của đảo tròn trung tâm.\\\\
        Vậy tâm $I$ của bồn hoa có thể đặt cách tâm $O$ của vòng xuyến một khoảng tối đa là $%s\\text{ m}$.
        \\end{enumEX}'''
                   % (latex(b_rong), latex(R1), latex(b_rong), latex(R2),
                      latex(R1), latex(R2),
                      r_hoa_str, latex(R1), latex(R1), r_hoa_str, d_max_str, d_max_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\n\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
