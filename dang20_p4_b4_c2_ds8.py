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


def bt_dang20_p4_b4_c2_ds8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) rectangle (3.4,3.4);
    \\draw[line width=1pt, dashed] (2.0,2.0) rectangle (3.4,3.4);
    \\draw[line width=1pt] (2.0,2.0) -- (3.4,3.4);
    \\draw[line width=1pt] (2.0,2.0) -- (2.0,3.4) (2.0,2.0) -- (3.4,2.0);
    \\draw[line width=1pt, <->] (0,-0.25) -- (3.4,-0.25) node[midway, below] {$a$};
    \\draw[line width=1pt, <->] (-0.25,0) -- (-0.25,3.4) node[midway, left] {$a$};
    \\draw[line width=1pt, <->] (2.0,3.65) -- (3.4,3.65) node[midway, above] {$b$};
    \\draw[line width=1pt, <->] (3.65,2.0) -- (3.65,3.4) node[midway, right] {$b$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho một hình vuông lớn có độ dài cạnh là $a\\text{ (cm)}$. Từ một góc của hình vuông lớn, người ta cắt đi một hình vuông nhỏ có độ dài cạnh là $b\\text{ (cm)}$ ($a > b > 0$). Phần diện tích còn lại có dạng hình chữ $L$, được cắt theo một đường chéo nối hai góc trong và ngoài để chia thành hai hình thang vuông bằng nhau. \\
a) Tính diện tích phần hình chữ $L$ theo $a$ và $b$. \\\\
b) Ghép hai hình thang vuông đó lại với nhau để tạo thành một hình chữ nhật duy nhất. Hãy xác định chiều dài và chiều rộng của hình chữ nhật mới tạo thành theo $a$ và $b$, từ đó giải thích hằng đẳng thức $a^2 - b^2 = (a - b)(a + b)$.'''
                         + tikz_hinh)
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích hình vuông lớn là $a^2\\text{ (cm}^2\\text{)}$ và diện tích hình vuông nhỏ bị cắt đi là $b^2\\text{ (cm}^2\\text{)}$.\\\\
Do đó, diện tích phần hình chữ $L$ còn lại là:
\\begin{align*}
S = a^2 - b^2\\text{ (cm}^2\\text{)}.
\\end{align*}
\\item Mỗi hình thang vuông có đáy lớn bằng $a\\text{ (cm)}$, đáy nhỏ bằng $b\\text{ (cm)}$ và chiều cao bằng $a - b\\text{ (cm)}$.\\\\
Khi ghép hai hình thang vuông bằng nhau dọc theo cạnh bên vát chéo, ta thu được một hình chữ nhật có chiều dài bằng tổng hai đáy là $a + b\\text{ (cm)}$ và chiều rộng bằng chiều cao hình thang là $a - b\\text{ (cm)}$.\\\\
Diện tích hình chữ nhật mới tạo thành là $(a - b)(a + b)\\text{ (cm}^2\\text{)}$.\\\\
Vì hình chữ nhật mới được ghép từ chính phần hình chữ $L$ nên diện tích của chúng bằng nhau, suy ra:
\\begin{align*}
a^2 - b^2 = (a - b)(a + b).
\\end{align*}
\\end{enumEX}''')

    # Xuất câu hỏi và lời giải tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
