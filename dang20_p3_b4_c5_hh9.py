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


def bt_dang20_p3_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        d_songsong = randint(8, 20)
        duong_kinh = randint(4, d_songsong - 1)
        if duong_kinh % 2 != 0:
            duong_kinh -= 1
        r = duong_kinh // 2
        kq_str = '1'

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (-3,2.2)--(3,2.2) node[right] {$a_1$};
\\draw[line width=1pt] (-3,0)--(3,0) node[right] {$a_2$};
\\draw[line width=1pt] (-3,-2.2)--(3,-2.2) node[right] {$a_3$};
\\coordinate (O) at (0,0.4);
\\draw[line width=1pt] (O) circle (0.9);
\\fill (O) circle (1pt) node[above] {$O$};
\\end{tikzpicture}
\\end{center}''')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên sân gạch phẳng người ta kẻ các đường thẳng song song cách đều nhau một khoảng $%s\\text{ cm}$. Một người chơi ném một chiếc vòng tròn bằng nhựa có đường kính $%s\\text{ cm}$ xuống sân. Hỏi có tối đa bao nhiêu đường thẳng trên sân có thể có điểm chung (cắt hoặc tiếp xúc) với chiếc vòng tròn đó cùng một lúc?'''
                         %(str(d_songsong), str(duong_kinh)))
        
        # Nội dung lời giải
        loigiai = ('''%s \\\\
Bán kính của chiếc vòng tròn là $R = \\dfrac{%s}{2} = %s\\text{ (cm)}$. \\\\
Xét một dải nằm giữa hai đường thẳng song song kề nhau $a_1$ và $a_2$ có khoảng cách là $%s\\text{ cm}$. \\\\
Gọi $d_1, d_2$ lần lượt là khoảng cách từ tâm $O$ của chiếc vòng đến $a_1$ và $a_2$, ta luôn có $d_1 + d_2 \\ge %s\\text{ cm}$. \\\\
Giả sử chiếc vòng có điểm chung (cắt hoặc tiếp xúc) với đường thẳng $a_1$, khi đó $d_1 \\le R = %s\\text{ cm}$. \\\\
Suy ra khoảng cách từ $O$ đến $a_2$ là $d_2 \\ge %s - d_1 \\ge %s - %s = %s\\text{ (cm)}$. \\\\
Vì $%s\\text{ cm} > R = %s\\text{ cm}$ nên chiếc vòng không giao với đường thẳng $a_2$ cũng như tất cả các đường thẳng khác. \\\\
Vậy chiếc vòng có thể có điểm chung với tối đa $1$ đường thẳng cùng một lúc.'''
                   %(hinhve, str(duong_kinh), str(r), str(d_songsong), str(d_songsong), str(r), str(d_songsong), str(d_songsong), str(r), str(d_songsong - r), str(d_songsong - r), str(r)))
        
        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))

    # Xuất câu hỏi trả lời ngắn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
