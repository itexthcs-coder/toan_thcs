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


def bt_dang13_p3_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x = symbols('x')
        k = randint(2, 5)
        a = Rational(1, k)
        f = a * x**2
        S = 2 * (k**2)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình vuông $OABC$ có đỉnh $O(0;0)$, hai đỉnh $A$ và $C$ nằm trên parabol $(P): y=%s$ (với hoành độ của $A$ âm và của $C$ dương), đỉnh $B$ nằm trên trục tung $Oy$. Diện tích hình vuông $OABC$ bằng bao nhiêu?
\\begin{center}
\\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[->, line width=1pt] (-3.2,0) -- (3.2,0) node[below] {$x$};
\\draw[->, line width=1pt] (0,-0.8) -- (0,4.8) node[left] {$y$};
\\draw[line width=1pt, smooth, samples=100, domain=-2.4:2.4] plot (\\x, {0.5*(\\x)^2});
\\coordinate (O) at (0,0);
\\coordinate (A) at (-2,2);
\\coordinate (B) at (0,4);
\\coordinate (C) at (2,2);
\\draw[line width=1pt] (O)--(A)--(B)--(C)--cycle;
\\draw[line width=1pt, dashed] (A)--(C);
\\fill (O) circle (1pt) node[below left] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\end{tikzpicture}
\\end{center}'''
                         % (latex(f)))

        # Nội dung lời giải
        loigiai = ('''Vì $OABC$ là hình vuông có $O(0;0)$ và $B$ nằm trên trục tung $Oy$ nên trục tung $Oy$ là đường chéo chứa tia phân giác của góc vuông $\\widehat{AOC}$. \\\\
Do đó góc tạo bởi tia $OC$ và tia $Ox$ bằng $45^\\circ$, suy ra điểm $C$ có hoành độ và tung độ bằng nhau: $x_C = y_C = m$ ($m > 0$). \\\\
Vì $C(m; m)$ nằm trên parabol $(P): y = %s$ nên: \\\\
$m = %s m^2 \\Leftrightarrow %s m^2 - m = 0 \\Leftrightarrow m(%s m - 1) = 0$. \\\\
Do $m > 0$ nên $m = %s$, suy ra $C(%s; %s)$ và $A(-%s; %s)$. \\\\
Bình phương độ dài cạnh hình vuông $OABC$ là: \\\\
$OC^2 = %s^2 + %s^2 = %s + %s = %s$. \\\\
Vậy diện tích hình vuông $OABC$ là $S = OC^2 = %s$.'''
                   % (latex(f),
                      latex(a), latex(a), latex(a),
                      str(k), str(k), str(k), str(k), str(k),
                      str(k), str(k), str(k**2), str(k**2), str(S),
                      str(S)))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(S))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
