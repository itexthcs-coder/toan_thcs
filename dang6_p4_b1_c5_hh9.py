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


def bt_dang6_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = [(5, 6, 8), (10, 12, 16), (13, 10, 24), (15, 18, 24)]
        R, ma, np_len = random.choice(bo_so)
        ab = 2 * R

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.8,0);
\\coordinate (B) at (1.8,0);
\\coordinate (M) at (106:1.8);
\\coordinate (N) at (-74:1.8);
\\coordinate (P) at (-106:1.8);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B);
\\draw[line width=1pt] (M)--(N)--(P)--cycle;
\\draw[line width=1pt, dashed] (A)--(M);
\\fill (O) circle (1pt) node[below right] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below right] {$N$};
\\fill (P) circle (1pt) node[below left] {$P$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ đường kính $AB$ và điểm $M \\in (O)$ sao cho $MA = %s\\text{ cm}$. Gọi $N$ là điểm đối xứng với $M$ qua tâm $O$, và $P$ là điểm đối xứng với $M$ qua đường thẳng $AB$ (như hình vẽ). \\\\
a) Chứng minh rằng các điểm $N, P$ cùng thuộc đường tròn $(O)$ và tam giác $MNP$ là tam giác vuông. \\\\
b) Tính độ dài đoạn thẳng $NP$.
%s''' % (R, ma, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì $O$ là tâm đối xứng của đường tròn $(O)$ và $M \\in (O)$ nên điểm $N$ đối xứng với $M$ qua $O$ cũng thuộc đường tròn $(O)$.\\\\
Vì đường thẳng $AB$ đi qua tâm $O$ nên $AB$ là một trục đối xứng của đường tròn $(O)$, suy ra điểm $P$ đối xứng với $M$ qua $AB$ cũng thuộc đường tròn $(O)$.\\\\
Do $N$ đối xứng với $M$ qua $O$ nên $O$ là trung điểm của đoạn thẳng $MN$ và $MN = 2R$.\\\\
Xét tam giác $MNP$ có $PO$ là đường trung tuyến ứng với cạnh $MN$ và $PO = R = \\dfrac{MN}{2}$, suy ra tam giác $MNP$ vuông tại $P$.
\\item Vì $O$ là trung điểm của cả hai đoạn thẳng $AB$ và $MN$ và $AB = MN = 2R = %s\\text{ cm}$ nên tứ giác $AMBN$ là hình chữ nhật, suy ra $BN = MA = %s\\text{ cm}$.\\\\
Mặt khác, $AB$ là đường trung trực của $MP$ và $B \\in AB$ nên $BP = BM$. Do đó tam giác $NBP$ và tam giác $MBN$ bằng nhau (hoặc xét $NP$ đối xứng với $MB$ qua $AB$), suy ra $NP = MB$.\\\\
Áp dụng định lí Pythagore cho tam giác $AMB$ vuông tại $M$ (do $MO = R = \\dfrac{AB}{2}$), ta có:\\\\
$NP = MB = \\sqrt{AB^2 - MA^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ cm}$.
\\end{enumEX}''' % (ab, ma, ab, ma, np_len))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
