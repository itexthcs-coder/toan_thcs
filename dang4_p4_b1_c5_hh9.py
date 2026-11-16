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


def bt_dang4_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mp = random.randint(8, 22)
        r_str = str(mp // 2) if mp % 2 == 0 else (str(mp // 2) + ',5')

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (I) at (0,0);
\\coordinate (M) at (-1.8,0);
\\coordinate (P) at (1.8,0);
\\coordinate (N) at (115:1.8);
\\coordinate (Q) at (-65:1.8);
\\draw[line width=1pt] (M)--(N)--(P)--(Q)--cycle;
\\draw[line width=1pt, dashed] (M)--(P) (N)--(Q) (I)--(N) (I)--(Q);
\\fill (I) circle (1pt) node[below left] {$I$};
\\fill (M) circle (1pt) node[left] {$M$};
\\fill (N) circle (1pt) node[above left] {$N$};
\\fill (P) circle (1pt) node[right] {$P$};
\\fill (Q) circle (1pt) node[below right] {$Q$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho tứ giác $MNPQ$ có $\\widehat{MNP} = \\widehat{MQP} = 90^{\\circ}$ và $MP = %s\\text{ cm}$. Gọi $I$ là trung điểm của đoạn thẳng $MP$ (như hình vẽ). \\\\
a) Chứng minh rằng bốn điểm $M, N, P, Q$ cùng thuộc đường tròn đường kính $MP$ và tính bán kính của đường tròn đó. \\\\
b) Chứng minh rằng đường trung trực của đoạn thẳng $NQ$ luôn đi qua tâm $I$.
%s''' % (mp, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Xét tam giác $MNP$ vuông tại $N$ có $NI$ là đường trung tuyến ứng với cạnh huyền $MP$, suy ra:\\\\
$IM = IN = IP = \\dfrac{MP}{2}$.\\\\
Xét tam giác $MQP$ vuông tại $Q$ có $QI$ là đường trung tuyến ứng với cạnh huyền $MP$, suy ra:\\\\
$IM = IQ = IP = \\dfrac{MP}{2}$.\\\\
Từ đó ta có $IM = IN = IP = IQ = \\dfrac{MP}{2} = \\dfrac{%s}{2} = %s\\text{ cm}$.\\\\
Vậy bốn điểm $M, N, P, Q$ cùng thuộc đường tròn tâm $I$ đường kính $MP$, có bán kính bằng $%s\\text{ cm}$.
\\item Theo câu a, ta có $IN = IQ = %s\\text{ cm}$.\\\\
Do điểm $I$ cách đều hai đầu mút $N$ và $Q$ của đoạn thẳng $NQ$ nên điểm $I$ nằm trên đường trung trực của đoạn thẳng $NQ$, tức là đường trung trực của đoạn thẳng $NQ$ luôn đi qua tâm $I$.
\\end{enumEX}''' % (mp, r_str, r_str, r_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
