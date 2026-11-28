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


def bt_dang19_p3_b5_c7_ds8(self):
    # Dang 19: Bai toan thuc te tinh he so goc (do doc) cua mat doc tiep can xe lan
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        slope_choice = random.choice([0.05, 0.06, 0.08, 0.12])
        run_val = random.choice([5.0, 7.5, 10.0])
        rise_val = round(slope_choice * run_val, 2)
        
        rise_str = str(rise_val).replace('.', ',')
        run_str = str(run_val).replace('.', ',') if run_val % 1 != 0 else str(int(run_val))
        
        kq = Decimal(str(slope_choice)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        ans_str = str(kq).replace('.', ',')
        
        tikz = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\draw[->, line width=1pt] (-0.5,0) -- (5.5,0) node[below] {$x$ (m)};\n'
            '\\draw[->, line width=1pt] (0,-0.5) -- (0,2.5) node[left] {$y$ (m)};\n'
            '\\draw[line width=1pt] (0,0) -- (4.5,1.2) -- (4.5,0);\n'
            '\\fill (0,0) circle (1pt) node[below left] {$A$};\n'
            '\\fill (4.5,1.2) circle (1pt) node[above right] {$B$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )
        
        noidungcauhoi = (
            'Trong thiết kế đường dốc tiếp cận cho xe lăn tại một tòa nhà, độ dốc được xác định bằng hệ số góc '
            'của đường thẳng mặt dốc trên hệ trục tọa độ $Oxy$ (đơn vị trên hai trục là mét). Biết mặt dốc đi lên từ điểm $A(0; 0)$ '
            'đến bậc thềm cao $%s$ m tại vị trí có khoảng cách ngang là $%s$ m. Tính hệ số góc của đường thẳng biểu diễn mặt dốc này.\n%s'
            % (rise_str, run_str, tikz)
        )
        
        loigiai = (
            'Trên hệ trục tọa độ $Oxy$, điểm bắt đầu của mặt dốc là $A(0; 0)$ và điểm kết thúc của mặt dốc tại bậc thềm là $B(%s; %s)$.\\ '
            'Vì đường thẳng biểu diễn mặt dốc đi qua gốc tọa độ $A(0; 0)$ nên có dạng $y = ax$ ($a \\neq 0$).\\ '
            'Thay tọa độ điểm $B(%s; %s)$ vào phương trình trên, ta được:\\ '
            '$%s = a \\cdot %s \\Leftrightarrow a = \\dfrac{%s}{%s} = %s$.\\ '
            'Vậy hệ số góc của đường thẳng biểu diễn mặt dốc là $%s$.'
            % (run_str, rise_str, run_str, rise_str, rise_str, run_str, rise_str, run_str, ans_str, ans_str)
        )
        
        dapan = '\\shortans[0]{$%s$}\n' % ans_str

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
