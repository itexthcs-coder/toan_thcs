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


def bt_dang19_p3_b3_c7_ds9(self):
    def fmt_vn(val):
        s = str(val)
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s.replace('.', ',')

    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        yA, yB, yC, yD = 10, 25, 40, 25
        s1 = Decimal(str(yA + yB)) / Decimal('2')
        s2 = Decimal(str(yB + yC)) / Decimal('2')
        s3 = Decimal(str(yC + yD)) / Decimal('2')
        tong_s = s1 + s2 + s3
        kq_str = fmt_vn(tong_s)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (0,0) -- (5.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,0) -- (0,3.2) node[left] {$y$};
\\draw[line width=1pt] (1,0.7) -- (2,1.75) -- (3,2.8) -- (4,1.75);
\\draw[dashed, line width=1pt] (1,0) -- (1,0.7) (2,0) -- (2,1.75) (3,0) -- (3,2.8) (4,0) -- (4,1.75);
\\fill (1,0.7) circle (1pt) node[above left] {$A(1;10)$};
\\fill (2,1.75) circle (1pt) node[above left] {$B(2;25)$};
\\fill (3,2.8) circle (1pt) node[above] {$C(3;40)$};
\\fill (4,1.75) circle (1pt) node[above right] {$D(4;25)$};
\\node[below] at (1,0) {$1$};
\\node[below] at (2,0) {$2$};
\\node[below] at (3,0) {$3$};
\\node[below] at (4,0) {$4$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Trên mặt phẳng tọa độ của biểu đồ tần số tương đối ghép nhóm dạng đoạn thẳng như hình vẽ dưới đây, bốn điểm liên tiếp là $A(1; 10)$, $B(2; 25)$, $C(3; 40)$, $D(4; 25)$:
%s
Diện tích của đa giác giới hạn bởi đường gấp khúc $ABCD$, trục hoành và hai đường thẳng đứng $x = 1$, $x = 4$ bằng bao nhiêu đơn vị diện tích?''' % (tikz_code))

        loigiai = ('''Đa giác cần tính diện tích gồm ba hình thang vuông liên tiếp có chiều cao đều bằng $1$:
\\begin{itemize}
\\item Hình thang thứ nhất có đáy lớn $25$, đáy nhỏ $10$: $S_1 = \\dfrac{(10 + 25) \\cdot 1}{2} = 17,5$.
\\item Hình thang thứ hai có đáy lớn $40$, đáy nhỏ $25$: $S_2 = \\dfrac{(25 + 40) \\cdot 1}{2} = 32,5$.
\\item Hình thang thứ ba có đáy lớn $40$, đáy nhỏ $25$: $S_3 = \\dfrac{(40 + 25) \\cdot 1}{2} = 32,5$.
\\end{itemize}
Vậy tổng diện tích của đa giác là: $S = 17,5 + 32,5 + 32,5 = %s$ (đơn vị diện tích).''' % (kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
