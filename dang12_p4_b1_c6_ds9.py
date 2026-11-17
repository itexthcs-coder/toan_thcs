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


def bt_dang12_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mau_a = randint(2, 5)
        coord_b = mau_a
        coord_c = 2 * mau_a

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho parabol $(P): y = \\frac{1}{%s}x^2$. Tìm tọa độ hai điểm $A$ và $B$ thuộc $(P)$ (với $x_A < 0 < x_B$) sao cho tứ giác $OACB$ là một hình vuông nhận điểm $C$ nằm trên trục tung $Oy$ làm đỉnh đối diện với gốc tọa độ $O$.'''
                         %(latex(mau_a)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Vì $OACB$ là hình vuông nhận $OC$ là đường chéo nằm trên trục tung $Oy$ và $a = \\frac{1}{%s} > 0$ nên điểm $C$ nằm trên tia $Oy$, còn hai đỉnh $A, B$ đối xứng nhau qua đường chéo $OC$. \\\\
Trong hình vuông $OACB$, hai đường chéo $OC$ và $AB$ vuông góc với nhau và cắt nhau tại trung điểm $H$ của mỗi đường, đồng thời $HA = HB = HO = HC$. \\\\
Vì $B$ nằm ở góc phần tư thứ nhất và $HB = HO$ nên hoành độ và tung độ của điểm $B$ bằng nhau: $x_B = y_B > 0$. \\\\
Mặt khác, điểm $B$ thuộc parabol $(P): y = \\frac{1}{%s}x^2$ nên: \\\\
$y_B = \\frac{1}{%s}x_B^2 \\Rightarrow x_B = \\frac{1}{%s}x_B^2$. \\\\
Vì $x_B > 0$, chia cả hai vế cho $x_B$ ta được $x_B = %s$, suy ra $y_B = %s$. \\\\
Do đó $B(%s; %s)$. Vì $A$ đối xứng với $B$ qua trục tung $Oy$ nên $A(-%s; %s)$ (và đỉnh $C(0; %s)$). \\\\
Vậy tọa độ hai điểm cần tìm là $A(-%s; %s)$ và $B(%s; %s)$. \\\\
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.2,0) -- (3.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.6) -- (0,4.8) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.5:2.5] plot(\\x, {0.5*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2,2);
\\coordinate (B) at (2,2);
\\coordinate (C) at (0,4);
\\draw[line width=1pt] (O)--(A)--(C)--(B)--cycle;
\\draw[line width=1pt, dashed] (A)--(B);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[above right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                   %(latex(mau_a),
                     latex(mau_a),
                     latex(mau_a), latex(mau_a),
                     latex(coord_b), latex(coord_b),
                     latex(coord_b), latex(coord_b), latex(coord_b), latex(coord_b), latex(coord_c),
                     latex(coord_b), latex(coord_b), latex(coord_b), latex(coord_b)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
