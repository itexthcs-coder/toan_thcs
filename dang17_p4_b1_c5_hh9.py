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


def bt_dang17_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(4, 15)

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (-1.8,0);
\\coordinate (B) at (1.8,0);
\\coordinate (C) at (0,1.8);
\\coordinate (D) at (0,-1.8);
\\coordinate (M) at (130:1.8);
\\coordinate (N) at (-130:1.8);
\\coordinate (P) at (-50:1.8);
\\coordinate (H) at (-1.157,0);
\\coordinate (K) at (0,1.379);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B) (C)--(D);
\\draw[line width=1pt] (M)--(N)--(P);
\\draw[line width=1pt, dashed] (M)--(P) (M)--(K) (H)--(K);
\\fill (O) circle (1pt) node[below right] {$O$};
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[right] {$B$};
\\fill (C) circle (1pt) node[above] {$C$};
\\fill (D) circle (1pt) node[below] {$D$};
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[below left] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\fill (K) circle (1pt) node[above right] {$K$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; %s\\text{ cm})$ có hai đường kính $AB$ và $CD$ vuông góc với nhau. Lấy điểm $M$ bất kì trên cung nhỏ $AC$ ($M \\ne A, M \\ne C$). Gọi $N$ là điểm đối xứng với $M$ qua đường thẳng $AB$, và $P$ là điểm đối xứng với $N$ qua đường thẳng $CD$ (như hình vẽ). \\\\
a) Chứng minh rằng điểm $P$ thuộc đường tròn $(O; %s\\text{ cm})$ và hai điểm $M, P$ đối xứng với nhau qua tâm $O$. \\\\
b) Gọi $H, K$ lần lượt là hình chiếu vuông góc của $M$ trên $AB$ và $CD$. Chứng minh rằng độ dài đoạn thẳng $HK$ không phụ thuộc vào vị trí của điểm $M$ trên cung nhỏ $AC$.
%s''' % (R, R, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì đường thẳng $AB$ đi qua tâm $O$ nên $AB$ là trục đối xứng của đường tròn $(O; %s\\text{ cm})$, suy ra $N \\in (O; %s\\text{ cm})$. Tương tự, $CD$ cũng là trục đối xứng của $(O)$ nên $P \\in (O; %s\\text{ cm})$, do đó $OM = ON = OP = %s\\text{ cm}$.\\\\
Vì $N$ đối xứng với $M$ qua $AB$ nên $AB$ là đường phân giác của $\\widehat{MON}$, suy ra $\\widehat{AOM} = \\widehat{AON}$.\\\\
Vì $P$ đối xứng với $N$ qua $CD$ nên $CD$ là đường phân giác của $\\widehat{NOP}$, suy ra $\\widehat{DON} = \\widehat{DOP}$.\\\\
Mặt khác, $AB \\perp CD$ tại $O$ nên $\\widehat{AON} + \\widehat{DON} = \\widehat{AOD} = 90^{\\circ}$.\\\\
Ta có $\\widehat{MOP} = \\widehat{MOA} + \\widehat{AON} + \\widehat{NOD} + \\widehat{DOP} = 2(\\widehat{AON} + \\widehat{DON}) = 2 \\cdot 90^{\\circ} = 180^{\\circ}$.\\\\
Do đó ba điểm $M, O, P$ thẳng hàng và $OM = OP$, tức là $O$ là trung điểm của $MP$. Vậy $M$ và $P$ đối xứng với nhau qua tâm $O$.
\\item Xét tứ giác $OHMK$ có ba góc vuông $\\widehat{HOK} = \\widehat{OHM} = \\widehat{OKM} = 90^{\\circ}$ nên $OHMK$ là hình chữ nhật.\\\\
Theo tính chất hình chữ nhật, hai đường chéo $HK$ và $OM$ bằng nhau, suy ra $HK = OM = %s\\text{ cm}$.\\\\
Vậy độ dài đoạn thẳng $HK$ luôn bằng $%s\\text{ cm}$, không phụ thuộc vào vị trí của điểm $M$ trên cung nhỏ $AC$.
\\end{enumEX}''' % (R, R, R, R, R, R))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
