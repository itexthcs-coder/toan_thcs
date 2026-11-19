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


def bt_dang18_p3_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_du_lieu = [
            (12, 18, 60, 6),
            (12, 24, 30, 10),
            (16, 24, 45, 9),
            (10, 20, 72, 6),
            (8, 16, 45, 6)
        ]
        so_cabin, chu_ky, goc_cach_dinh, dap_an = random.choice(bo_du_lieu)
        goc_quay = 180 - goc_cach_dinh
        kq_str = str(dap_an)

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\draw[line width=1pt] (O) circle (1.7);
\\foreach \\i in {0,30,...,330} {
    \\draw[line width=1pt] (O)--(\\i:1.7);
    \\fill (\\i:1.7) circle (1pt);
}
\\draw[line width=1pt] (-0.8,-2.1)--(O)--(0.8,-2.1);
\\fill (O) circle (1pt) node[below left] {$O$};
\\node[above] at (90:1.7) {Cao nhất};
\\node[below] at (270:1.7) {Cabin $1$};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Một vòng quay mặt trời trong công viên có $%s$ cabin được bố trí cách đều nhau trên vành tròn tâm $O$, tạo thành các đỉnh của một đa giác đều $%s$ cạnh (như hình vẽ). Vòng quay chuyển động đều theo chiều kim đồng hồ và mất đúng $%s$ phút để quay hết một vòng tròn $360^\\circ$. Tại thời điểm bắt đầu, cabin số $1$ đang ở vị trí thấp nhất. Hỏi sau ít nhất bao nhiêu phút thì cabin số $1$ di chuyển tới vị trí tạo với vị trí cao nhất một góc ở tâm bằng $%s^\\circ$ (theo chiều quay của vòng quay, chưa vượt qua vị trí cao nhất)? %s'''
                         % (so_cabin, so_cabin, chu_ky, goc_cach_dinh, hinh_tikz))

        loigiai = ('''Vị trí thấp nhất và vị trí cao nhất đối xứng nhau qua tâm $O$ nên tạo với nhau một góc ở tâm bằng $180^\\circ$. \\
Khi cabin số $1$ đi từ vị trí thấp nhất đến vị trí chưa vượt qua điểm cao nhất và cách điểm cao nhất một góc ở tâm $%s^\\circ$, góc quay mà cabin số $1$ đã thực hiện là:
$$\\alpha = 180^\\circ - %s^\\circ = %s^\\circ.$$
Vì vòng quay mất $%s$ phút để quay hết $360^\\circ$ nên thời gian cần thiết để quay góc $%s^\\circ$ là:
$$t = %s \\cdot \\frac{%s^\\circ}{360^\\circ} = %s \\text{ (phút)}.$$'''
                   % (goc_cach_dinh, goc_cach_dinh, goc_quay, chu_ky, goc_quay, chu_ky, goc_quay, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
